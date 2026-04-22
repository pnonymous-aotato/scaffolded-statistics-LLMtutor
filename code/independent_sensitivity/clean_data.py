"""
clean_data.py
=============
Build the canonical long-format paired Likert dataset from Canvas exports.

Key steps:
  1. Read the 6 Likert CSVs (Course A x T1/T2/T3, Course B x T1/T2/T3)
  2. Extract ONLY the 11 Likert items (drop open-ended, metadata, score cols)
  3. Map text responses -> ordinal 1..5
  4. Anonymize Canvas id to stable S_A_001, S_B_001, ... codes
  5. Write:
       - long.csv         : (anon_id, course, wave, item, response_ord, response_text)
       - wide_per_wave.csv: one row per (anon_id, wave) with 11 item columns
       - meta.csv         : one row per anon_id with participation pattern (T1/T2/T3)
       - pair_audit.txt   : human-readable summary of who appears in which waves
"""

import re
import pandas as pd
from pathlib import Path

LIKERT_MAP = {
    'strongly disagree': 1,
    'disagree':           2,
    'neutral':            3,
    'agree':              4,
    'strongly agree':     5,
}

# Short item keys that we'll use throughout the analysis (Q1..Q11)
ITEM_STEMS = [
    (1,  "enhanced"),     # The AI tutor has enhanced my overall learning experience
    (2,  "critical"),     # encourages me to think critically and solve problems independently
    (3,  "recall"),       # helps me recall and apply previous concepts
    (4,  "userfriendly"), # user-friendly and accessible during class activities
    (5,  "feedback"),     # feedback as helpful as feedback from the instructor
    (6,  "prompts"),      # prompts provided by the instructor help me effectively utilize
    (7,  "support"),      # supports my learning regardless of background
    (8,  "prepared"),     # I feel prepared before attending lecture
    (9,  "examples"),     # I can understand examples covered in lecture
    (10, "reduce"),       # reduce my need to seek additional resources
    (11, "aware"),        # aware of the university's efforts to integrate AI
]

def normalize(s):
    if not isinstance(s, str):
        return None
    s = s.strip().lower().replace('\u2019', "'")
    return LIKERT_MAP.get(s)

def match_item(col):
    """Given a column name like '2543531: The AI tutor has enhanced...', return (qnum, stem) or None."""
    if not isinstance(col, str) or ':' not in col:
        return None
    text = col.split(':', 1)[1].strip().lower()
    # Exclude open-ended prompts (they all ask or describe, not declare)
    if text.startswith('how has using') or text.startswith('considering your'):
        return None
    if text.startswith('what features') or text.startswith('do you feel'):
        return None
    if text.startswith('any suggestions'):
        return None
    # anchor-phrase matching on the DECLARATIVE Likert stems
    if text.startswith('the ai tutor has enhanced'): return (1, 'enhanced')
    if text.startswith('the ai tutor encourages me to think critically'): return (2, 'critical')
    if text.startswith('the ai tutor helps me recall'): return (3, 'recall')
    if text.startswith('the ai tutor is user-friendly') or text.startswith('the ai tutor is user friendly'): return (4, 'userfriendly')
    if text.startswith('the feedback provided by the ai tutor'): return (5, 'feedback')
    if text.startswith('the prompts provided by the instructor'): return (6, 'prompts')
    if text.startswith('the ai tutor supports my learning'): return (7, 'support')
    if text.startswith('i feel prepared before attending lecture'): return (8, 'prepared')
    if text.startswith('i can understand examples covered'): return (9, 'examples')
    if text.startswith('the course materials and ai tutor reduce'): return (10, 'reduce')
    if text.startswith('i am aware') and 'integrate ai' in text: return (11, 'aware')
    return None

FILES = {
    ('A', 'T1'): 'AI Use Survey _ 01 Survey Student Analysis Report 2200.csv',
    ('A', 'T2'): 'AI Use Survey _ 02 Survey Student Analysis Report 2200.csv',
    ('A', 'T3'): 'AI Use Survey _ 03 Survey Student Analysis Report 2200.csv',
    ('B', 'T1'): 'AI Use Survey _ 01 Survey Student Analysis Report 4200.csv',
    ('B', 'T2'): 'AI Use Survey _ 02 Survey Student Analysis Report 4200.csv',
    ('B', 'T3'): 'AI Use Survey _ 03 Survey Student Analysis Report 4200.csv',
}

def load_wave(path, course, wave):
    df = pd.read_csv(path)
    # find the 11 Likert columns in THIS file
    col_map = {}
    for col in df.columns:
        m = match_item(col)
        if m is not None:
            qnum, stem = m
            col_map[col] = (qnum, stem)
    if len(col_map) != 11:
        missing = set(range(1, 12)) - {q for q, _ in col_map.values()}
        raise RuntimeError(f"{course} {wave}: matched only {len(col_map)} Likert items; missing qnums={missing}")

    rows = []
    for _, row in df.iterrows():
        canvas_id = row['id']
        for col, (qnum, stem) in col_map.items():
            raw = row[col]
            ord_val = normalize(raw) if isinstance(raw, str) else None
            rows.append({
                'canvas_id': canvas_id,
                'course': course,
                'wave': wave,
                'qnum': qnum,
                'stem': stem,
                'response_text': raw if isinstance(raw, str) else None,
                'response_ord': ord_val,
            })
    return pd.DataFrame(rows)

def main():
    here = Path(__file__).parent
    all_long = pd.concat([load_wave(here / FILES[k], k[0], k[1]) for k in FILES],
                         ignore_index=True)

    # Anonymize: S_A_001, S_A_002, ... S_B_001, ...
    anon = {}
    for course in ['A', 'B']:
        ids = sorted(all_long.query("course == @course")['canvas_id'].unique())
        for i, cid in enumerate(ids, start=1):
            anon[(course, cid)] = f"S_{course}_{i:03d}"
    all_long['anon_id'] = [anon[(c, cid)] for c, cid in zip(all_long['course'], all_long['canvas_id'])]

    # Save long format (this is the canonical file — use this for all analysis)
    long_out = all_long[['anon_id', 'course', 'wave', 'qnum', 'stem',
                         'response_ord', 'response_text']].copy()
    long_out.to_csv(here / 'long.csv', index=False)

    # Wide-per-wave: one row per (anon_id, wave), columns Q1..Q11
    wide = long_out.pivot_table(index=['anon_id', 'course', 'wave'],
                                columns='qnum', values='response_ord',
                                aggfunc='first').reset_index()
    wide.columns = ['anon_id', 'course', 'wave'] + [f"Q{i}" for i in range(1, 12)]
    wide.to_csv(here / 'wide_per_wave.csv', index=False)

    # Participation pattern: who showed up at which waves
    pat = (long_out.groupby(['anon_id', 'course', 'wave'])['response_ord']
           .apply(lambda x: 1 if x.notna().any() else 0)
           .unstack('wave', fill_value=0)
           .reset_index())
    for w in ['T1', 'T2', 'T3']:
        if w not in pat.columns: pat[w] = 0
    pat['n_waves'] = pat[['T1', 'T2', 'T3']].sum(axis=1)
    pat['pattern'] = pat[['T1', 'T2', 'T3']].apply(
        lambda r: ''.join(['T1' if r['T1'] else '--',
                           'T2' if r['T2'] else '--',
                           'T3' if r['T3'] else '--']), axis=1)
    pat.to_csv(here / 'meta.csv', index=False)

    # ===== Audit =====
    lines = []
    lines.append("=== PAIRED DATA AUDIT ===")
    lines.append(f"\nTotal long-format rows: {len(long_out)}")
    lines.append(f"Total unique students: {long_out['anon_id'].nunique()}")
    lines.append("\nPer-wave response counts (students with >= 1 answered item):")
    for c in ['A', 'B']:
        for w in ['T1', 'T2', 'T3']:
            n = (long_out.query("course==@c and wave==@w and response_ord.notna()")
                 ['anon_id'].nunique())
            lines.append(f"  Course {c}, {w}: n = {n}")

    lines.append("\nParticipation patterns (how many waves each student appeared in):")
    for c in ['A', 'B']:
        sub = pat.query("course == @c")
        lines.append(f"\n  Course {c}:")
        for nw in [3, 2, 1]:
            lines.append(f"    Appeared in exactly {nw} waves: n = {(sub['n_waves']==nw).sum()}")
        lines.append("    Exact patterns:")
        for p, cnt in sub['pattern'].value_counts().items():
            lines.append(f"      {p}: {cnt}")

    lines.append("\nComplete-cases (students in ALL 3 waves) — these are the paired analysis sample:")
    for c in ['A', 'B']:
        n3 = ((pat['course']==c) & (pat['n_waves']==3)).sum()
        lines.append(f"  Course {c}: n = {n3}")

    audit = "\n".join(lines)
    (here / 'pair_audit.txt').write_text(audit)
    print(audit)

if __name__ == "__main__":
    main()
