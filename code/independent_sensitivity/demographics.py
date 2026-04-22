"""
demographics.py
===============
Parse the demographic CSVs and produce a clean summary table.
"""
import pandas as pd, re
from pathlib import Path

HERE = Path('./survey/survey')
OUT = HERE / 'analysis_out'

FILES = {
    'A': 'Demographic Survey (BONUS POINTS) Survey Student Analysis Report 2200.csv',
    'B': 'Demographic Survey (BONUS POINTS) Survey Student Analysis Report 4200.csv',
}

def demo_colmap(col):
    if not isinstance(col, str) or ':' not in col: return None
    t = col.split(':', 1)[1].strip().lower()
    if 'gender' in t: return 'gender'
    if 'current major' in t: return 'major'
    if 'hispanic or latino' in t: return 'hispanic'
    if 'race/ethnicity' in t: return 'race'
    if 'what is your age' in t: return 'age'
    if 'primary language' in t: return 'language'
    if 'academic standing' in t: return 'standing'
    if 'credit hours' in t: return 'units'
    if 'employed, how many hours' in t: return 'work_hours'
    if 'regular access' in t: return 'access'
    if 'type of device' in t: return 'device'
    if 'ai tools like chatgpt' in t: return 'ai_use'
    if 'what specific ai platforms' in t: return 'ai_platform'
    if 'used ai tools for studying' in t: return 'ai_use_desc'
    if 'non-ai tools' in t: return 'non_ai_desc'
    return None

rows = []
for c, fn in FILES.items():
    df = pd.read_csv(HERE / fn)
    cm = {col: demo_colmap(col) for col in df.columns if demo_colmap(col)}
    for _, r in df.iterrows():
        rec = {'course': c, 'canvas_id': r['id']}
        for col, key in cm.items():
            v = r[col]
            rec[key] = v if isinstance(v, str) and v.strip() else None
        rows.append(rec)
demo = pd.DataFrame(rows)
demo.to_csv(OUT / 'demographics_raw.csv', index=False)

# Summary counts per course
def top_counts(series, k=3):
    return series.dropna().value_counts().head(k).to_dict()

summary = []
for c in ['A', 'B']:
    g = demo.query("course == @c")
    n = g['canvas_id'].nunique()
    summary.append(f"\n### Course {c}  (N={n})")
    for key in ['gender','hispanic','race','language','standing',
                'access','device','ai_use','ai_platform']:
        if key in g.columns:
            top = top_counts(g[key])
            summary.append(f"  {key}: {top}")
        else:
            summary.append(f"  {key}: MISSING")

md = "\n".join(summary)
(OUT / 'demographics_summary.md').write_text(md)
print(md)
