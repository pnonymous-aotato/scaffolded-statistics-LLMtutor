"""
essays.py
=========
Extract open-ended responses from the same 6 CSVs and organize them
by course, wave, student anon_id, and prompt. Produces:

  - essays_long.csv: anon_id, course, wave, prompt_id, prompt_text, response
  - essay_sample_by_prompt.md: representative quotes, 2-3 per prompt per wave per course
  - word_counts.csv: per-course, per-wave summary (n responses, mean/median length)
  - themes_topkw.csv: simple top-frequency keyword lists per prompt (for anchor-writing)
"""
import re
import pandas as pd
from pathlib import Path
from collections import Counter

HERE = Path('./survey/survey')
OUT = HERE / 'analysis_out'
OUT.mkdir(exist_ok=True)

FILES = {
    ('A', 'T1'): 'AI Use Survey _ 01 Survey Student Analysis Report 2200.csv',
    ('A', 'T2'): 'AI Use Survey _ 02 Survey Student Analysis Report 2200.csv',
    ('A', 'T3'): 'AI Use Survey _ 03 Survey Student Analysis Report 2200.csv',
    ('B', 'T1'): 'AI Use Survey _ 01 Survey Student Analysis Report 4200.csv',
    ('B', 'T2'): 'AI Use Survey _ 02 Survey Student Analysis Report 4200.csv',
    ('B', 'T3'): 'AI Use Survey _ 03 Survey Student Analysis Report 4200.csv',
}

# Five open-ended prompts the paper describes, matched by distinctive phrases
def classify_open(col):
    if not isinstance(col, str) or ':' not in col: return None
    text = col.split(':', 1)[1].strip().lower()
    if text.startswith('considering your work'):    return 'P1_balance'
    if text.startswith('what features of the ai tutor'): return 'P2_features'
    if text.startswith('do you feel the ai tutor accommodates'): return 'P3_equity'
    if text.startswith('how has using the ai tutor'): return 'P4_critical'
    if text.startswith('any suggestions'):           return 'P5_suggest'
    return None

PROMPT_LABELS = {
    'P1_balance':  'Work-life-class balance',
    'P2_features': 'Helpful features / needs improvement',
    'P3_equity':   'Accommodates all students equally?',
    'P4_critical': 'Effect on critical thinking',
    'P5_suggest':  'Suggestions',
}

# Load the anonymization map from the clean step
meta = pd.read_csv(HERE / 'meta.csv')
anon_map = dict(zip(
    pd.read_csv(HERE / 'long.csv')[['anon_id']].drop_duplicates()['anon_id'],
    pd.read_csv(HERE / 'long.csv')[['anon_id']].drop_duplicates()['anon_id']
))
# Rebuild canvas_id -> anon_id mapping by re-reading
all_canvas = {}
for (c, w), fn in FILES.items():
    df = pd.read_csv(HERE / fn)
    for cid in df['id']:
        all_canvas.setdefault(c, set()).add(cid)
canvas_to_anon = {}
for c, ids in all_canvas.items():
    for i, cid in enumerate(sorted(ids), start=1):
        canvas_to_anon[(c, cid)] = f"S_{c}_{i:03d}"

rows = []
for (c, w), fn in FILES.items():
    df = pd.read_csv(HERE / fn)
    col_map = {}
    for col in df.columns:
        k = classify_open(col)
        if k: col_map[col] = k
    for _, r in df.iterrows():
        anon = canvas_to_anon[(c, r['id'])]
        for col, key in col_map.items():
            txt = r[col]
            if isinstance(txt, str) and len(txt.strip()) > 2:
                rows.append({
                    'anon_id': anon, 'course': c, 'wave': w,
                    'prompt_id': key,
                    'prompt_label': PROMPT_LABELS[key],
                    'response': txt.strip(),
                    'n_words': len(re.findall(r'\w+', txt)),
                })
ess = pd.DataFrame(rows)
ess.to_csv(OUT / 'essays_long.csv', index=False)
print(f'Total essay responses: {len(ess)}')
print(f"Unique students with >=1 essay: {ess['anon_id'].nunique()}")
print("\nBy course x wave:")
print(ess.groupby(['course','wave'])['response'].count())

# ---- Word-count summary ----
summary = (ess.groupby(['course','wave','prompt_id'])
           .agg(n=('response','count'),
                mean_words=('n_words','mean'),
                median_words=('n_words','median'))
           .round(1)
           .reset_index())
summary.to_csv(OUT / 'essays_summary.csv', index=False)

# ---- Keyword frequency per prompt (simple bag-of-words, stopword removal) ----
STOP = set("""
a about above after again against all am an and any are aren't as at be
because been before being below between both but by can cannot could
couldn't did didn't do does doesn't doing don't down during each few for
from further had hadn't has hasn't have haven't having he he'd he'll
he's her here here's hers herself him himself his how how's i i'd i'll
i'm i've if in into is isn't it it's its itself let's me more most
mustn't my myself no nor not of off on once only or other ought our ours
ourselves out over own same shan't she she'd she'll she's should
shouldn't so some such than that that's the their theirs them
themselves then there there's these they they'd they'll they're they've
this those through to too under until up very was wasn't we we'd we'll
we're we've were weren't what what's when when's where where's which
while who who's whom why why's with won't would wouldn't you you'd
you'll you're you've your yours yourself yourselves like just also get
got really think feel know use used using able way ways thing things
ai chatgpt tutor gpt get got get gets getting give gives given go going
one two help helps helped helping make makes made making
""".split())

kw_rows = []
for (c, w, p), g in ess.groupby(['course','wave','prompt_id']):
    blob = ' '.join(g['response'].str.lower())
    words = re.findall(r"[a-z']+", blob)
    words = [x for x in words if x not in STOP and len(x) > 2]
    for word, n in Counter(words).most_common(15):
        kw_rows.append({'course': c, 'wave': w, 'prompt_id': p,
                        'word': word, 'n': n})
kw = pd.DataFrame(kw_rows)
kw.to_csv(OUT / 'essays_top_keywords.csv', index=False)

# ---- Sample quotes: pick the most substantive (longest, <300 chars) per
#      (course, wave, prompt), up to 2. Output as markdown. ----
def best_quotes(g, k=2):
    g = g.copy()
    g['score'] = g['n_words'].clip(upper=60)  # prefer substantive but not rambling
    g = g.sort_values('score', ascending=False)
    out = []
    for _, r in g.head(k).iterrows():
        txt = r['response'].replace('\n', ' ').replace('\r', ' ')[:350]
        out.append(f"    > \"{txt}\" (Course {r['course']}, {r['wave']}, {r['anon_id']})")
    return out

md = ["# Essay / open-ended responses — summary and representative quotes\n"]
md.append(f"Total open-ended responses: **{len(ess)}** from "
          f"**{ess['anon_id'].nunique()}** unique students.\n")
md.append("Responses broken down:")
md.append("")
md.append("| Course | Wave | P1 balance | P2 features | P3 equity | P4 critical | P5 suggest |")
md.append("|---|---|---|---|---|---|---|")
for (c, w), g in ess.groupby(['course','wave']):
    counts = g['prompt_id'].value_counts().to_dict()
    row = f"| {c} | {w} |"
    for p in ['P1_balance','P2_features','P3_equity','P4_critical','P5_suggest']:
        row += f" {counts.get(p, 0)} |"
    md.append(row)
md.append("")

for p in ['P1_balance','P2_features','P3_equity','P4_critical','P5_suggest']:
    md.append(f"\n## {PROMPT_LABELS[p]} (`{p}`)\n")
    for c in ['A', 'B']:
        for w in ['T1','T2','T3']:
            g = ess.query("course==@c and wave==@w and prompt_id==@p")
            if len(g) == 0: continue
            md.append(f"### Course {c}, {w}  — n={len(g)}  "
                      f"(mean words: {g['n_words'].mean():.0f}, "
                      f"median: {g['n_words'].median():.0f})")
            quotes = best_quotes(g, 2)
            md.extend(quotes)
            md.append("")

(OUT / 'essays_samples.md').write_text('\n'.join(md))
print('wrote', OUT / 'essays_long.csv')
print('wrote', OUT / 'essays_summary.csv')
print('wrote', OUT / 'essays_top_keywords.csv')
print('wrote', OUT / 'essays_samples.md')
