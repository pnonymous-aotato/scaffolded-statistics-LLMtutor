"""
Subgroup analysis — corrected for Course B's extra 'attempt' column.
"""

import csv
import random
import re
from scipy import stats
from scipy.stats import rankdata

random.seed(42)

BASE = "./data/raw_canvas_exports"

LIKERT_MAP = {
    "Strongly Disagree": 1, "Strongly disagree": 1, "strongly disagree": 1,
    "Disagree": 2, "disagree": 2,
    "Neutral": 3, "neutral": 3,
    "Neither Agree nor Disagree": 3, "Neither Agree Nor Disagree": 3,
    "Agree": 4, "agree": 4,
    "Strongly Agree": 5, "Strongly agree": 5, "strongly agree": 5,
    "": None, "nan": None, "NA": None,
}

FILES = {
    "T1_A": f"{BASE}/AI Use Survey _ 01 Survey Student Analysis Report 2200.csv",
    "T3_A": f"{BASE}/AI Use Survey _ 03 Survey Student Analysis Report 2200.csv",
    "T1_B": f"{BASE}/AI Use Survey _ 01 Survey Student Analysis Report 4200.csv",
    "T3_B": f"{BASE}/AI Use Survey _ 03 Survey Student Analysis Report 4200.csv",
    "demo_A": f"{BASE}/Demographic Survey (BONUS POINTS) Survey Student Analysis Report 2200.csv",
    "demo_B": f"{BASE}/Demographic Survey (BONUS POINTS) Survey Student Analysis Report 4200.csv",
}


def load_likert(path):
    out = {}
    with open(path) as f:
        reader = csv.reader(f); next(reader)
        for row in reader:
            if not row or not row[0]: continue
            sid = row[0]
            vals = [LIKERT_MAP.get(row[i].strip() if i < len(row) else "", None)
                    for i in range(2, 24, 2)]
            out[sid] = vals
    return out


def load_demo(path):
    """
    Auto-detect the column offset:
    - Course A: id, section, Q1, ans1, Q2, ans2, ... → Q starts at col 2
    - Course B: id, section, attempt, Q1, ans1, Q2, ans2, ... → Q starts at col 3
    Find the first column whose header starts with 'What is your gender'.
    """
    out = {}
    with open(path) as f:
        reader = csv.reader(f)
        header = next(reader)
        # Find gender column
        gender_col = None
        for i, h in enumerate(header):
            if "What is your gender" in h:
                gender_col = i
                break
        if gender_col is None:
            raise ValueError(f"Could not find gender column in {path}")

        # Answer is in the SAME column as the question header (Canvas format quirk)
        ans_base = gender_col

        # Column offsets for each demographic (each question occupies 2 columns)
        # gender=0, major=2, hispanic=4, race=6, age=8, language=10, standing=12,
        # credits=14, employment=16, tech=18, device=20, prior_ai=22, platforms=24
        def ans(step):
            return ans_base + 2 * step

        for row in reader:
            if not row or not row[0]: continue
            sid = row[0]
            def safe(i):
                return row[i].strip() if i < len(row) else ""
            out[sid] = {
                "gender":     safe(ans(0)),
                "major":      safe(ans(1)),
                "hispanic":   safe(ans(2)),
                "race":       safe(ans(3)),
                "age":        safe(ans(4)),
                "language":   safe(ans(5)),
                "standing":   safe(ans(6)),
                "credits":    safe(ans(7)),
                "employment": safe(ans(8)),
                "tech":       safe(ans(9)),
                "device":     safe(ans(10)),
                "prior_ai":   safe(ans(11)),
                "ai_platforms": safe(ans(12)),
            }
    return out


likert = {k: load_likert(v) for k, v in FILES.items() if "demo" not in k}
demo   = {"A": load_demo(FILES["demo_A"]), "B": load_demo(FILES["demo_B"])}

# Quick sanity check
print("Demo Course A hispanic distribution:", [demo["A"][sid].get("hispanic") for sid in list(demo["A"].keys())[:10]])
print("Demo Course B hispanic distribution:", [demo["B"][sid].get("hispanic") for sid in list(demo["B"].keys())[:10]])
print("Demo Course B prior_ai distribution:", [demo["B"][sid].get("prior_ai") for sid in list(demo["B"].keys())[:10]])
print("Demo Course B employment distribution:", [demo["B"][sid].get("employment") for sid in list(demo["B"].keys())[:5]])
print()


def compute_diff(sid, item_idx, course):
    t1 = likert[f"T1_{course}"].get(sid)
    t3 = likert[f"T3_{course}"].get(sid)
    if t1 is None or t3 is None:
        return None
    v1 = t1[item_idx]; v3 = t3[item_idx]
    if v1 is None or v3 is None:
        return None
    return v3 - v1


def compute_composite_diff(sid, course):
    t1 = likert[f"T1_{course}"].get(sid)
    t3 = likert[f"T3_{course}"].get(sid)
    if t1 is None or t3 is None:
        return None
    paired_items = [(a, b) for a, b in zip(t1, t3) if a is not None and b is not None]
    if len(paired_items) < 5:
        return None
    t1_mean = sum(p[0] for p in paired_items)/len(paired_items)
    t3_mean = sum(p[1] for p in paired_items)/len(paired_items)
    return t3_mean - t1_mean


def glass_rank_biserial(group1, group2):
    if not group1 or not group2: return None
    all_vals = group1 + group2
    ranks = rankdata(all_vals, method="average")
    n1, n2 = len(group1), len(group2)
    mean_r1 = sum(ranks[:n1])/n1
    mean_r2 = sum(ranks[n1:])/n2
    return 2*(mean_r1 - mean_r2)/(n1 + n2)


def bootstrap_rbs(g1, g2, B=5000, seed=42):
    if not g1 or not g2: return (None, None)
    rng = random.Random(seed)
    samples = []
    for _ in range(B):
        b1 = [g1[rng.randrange(len(g1))] for _ in range(len(g1))]
        b2 = [g2[rng.randrange(len(g2))] for _ in range(len(g2))]
        v = glass_rank_biserial(b1, b2)
        if v is not None:
            samples.append(v)
    samples.sort()
    return (samples[int(0.025 * len(samples))], samples[int(0.975 * len(samples)) - 1])


def mann_whitney_exact(g1, g2):
    if not g1 or not g2: return None, None
    try:
        res = stats.mannwhitneyu(g1, g2, alternative="two-sided", method="exact")
        return float(res.statistic), float(res.pvalue)
    except Exception:
        res = stats.mannwhitneyu(g1, g2, alternative="two-sided", method="asymptotic")
        return float(res.statistic), float(res.pvalue)


def descriptives(diffs):
    if not diffs: return None
    n = len(diffs)
    mean_d = sum(diffs)/n
    sorted_d = sorted(diffs)
    median_d = sorted_d[n//2] if n%2 else (sorted_d[n//2-1] + sorted_d[n//2])/2
    return dict(n=n, mean=mean_d, median=median_d,
                n_plus=sum(1 for x in diffs if x > 0),
                n_zero=sum(1 for x in diffs if x == 0),
                n_minus=sum(1 for x in diffs if x < 0))


def classify_hispanic(v):
    v = (v or "").strip().lower()
    if v.startswith("y") or v == "hispanic" or v == "hispanic or latino(a)":  return "Hispanic/Latino"
    if v.startswith("n") or v == "non-hispanic":  return "Non-Hispanic"
    return None


def classify_language(v):
    v = (v or "").strip()
    if not v: return None
    if v.lower() == "english": return "English"
    return "Other"


def classify_prior_ai(v):
    v = (v or "").strip().lower()
    if v.startswith("y"): return "Prior AI user"
    if v.startswith("n"): return "No prior AI"
    return None


def classify_employment(v, course):
    """Return label based on textual response. Dichotomize: not employed vs employed."""
    v_clean = (v or "").strip().lower()
    if not v_clean: return None
    nums = re.findall(r'\d+', v_clean)
    # Look for explicit "not employed" / "no" / "0"
    if ("not" in v_clean and "employ" in v_clean) or v_clean == "0" or v_clean == "no":
        return "Not employed"
    if nums:
        max_hrs = max(int(n) for n in nums)
        if max_hrs == 0:
            return "Not employed"
        if max_hrs >= 20:
            return "Working 20+ hrs"
        return "Working <20 hrs"
    return None


def run_subgroup(course, item_idx_or_composite, classifier_fn, attr_name, label):
    ids = set(likert[f"T1_{course}"].keys()) & set(likert[f"T3_{course}"].keys()) & set(demo[course].keys())
    diffs_by_group = {}
    for sid in ids:
        if item_idx_or_composite == "composite":
            d = compute_composite_diff(sid, course)
        else:
            d = compute_diff(sid, item_idx_or_composite, course)
        if d is None: continue
        attr = demo[course][sid].get(attr_name, "")
        grp = classifier_fn(attr, course) if attr_name == "employment" else classifier_fn(attr)
        if grp is None: continue
        diffs_by_group.setdefault(grp, []).append(d)

    groups_sorted = sorted(diffs_by_group.items(), key=lambda kv: -len(kv[1]))
    if len(groups_sorted) < 2:
        return {"label": label, "course": course,
                "error": f"Only groups formed: {[(k, len(v)) for k,v in diffs_by_group.items()]}"}
    g1_name, g1 = groups_sorted[0]
    g2_name, g2 = groups_sorted[1]

    U, p = mann_whitney_exact(g1, g2)
    rbs = glass_rank_biserial(g1, g2)
    ci_lo, ci_hi = bootstrap_rbs(g1, g2, B=5000, seed=42)
    d1 = descriptives(g1); d2 = descriptives(g2)
    return {
        "label": label, "course": course,
        "g1_name": g1_name, "g1_n": d1["n"], "g1_mean": d1["mean"], "g1_median": d1["median"],
        "g1_plus": d1["n_plus"], "g1_zero": d1["n_zero"], "g1_minus": d1["n_minus"],
        "g2_name": g2_name, "g2_n": d2["n"], "g2_mean": d2["mean"], "g2_median": d2["median"],
        "g2_plus": d2["n_plus"], "g2_zero": d2["n_zero"], "g2_minus": d2["n_minus"],
        "U": U, "p": p, "r_bs": rbs, "ci_lo": ci_lo, "ci_hi": ci_hi,
    }


SUBGROUP_PLAN = [
    dict(label="A1: Hispanic/Latino × Q7 equity",     item=6,           classifier=classify_hispanic,   attr="hispanic"),
    dict(label="A2: Prior AI use × composite Q1-Q11", item="composite", classifier=classify_prior_ai,   attr="prior_ai"),
    dict(label="A3: English primary × Q2 crit think.", item=1,          classifier=classify_language,   attr="language"),
    dict(label="A4: Employment hrs × Q8 prep",         item=7,          classifier=classify_employment, attr="employment"),
]

print("="*100)
print("PRE-SPECIFIED SUBGROUP ANALYSES (Mann-Whitney U exact, Glass rank-biserial)")
print("="*100)

all_rows = []
for spec in SUBGROUP_PLAN:
    for course in ["A", "B"]:
        r = run_subgroup(course, spec["item"], spec["classifier"], spec["attr"], spec["label"])
        if "error" in r:
            print(f"\n[{r['label']} | Course {course}] {r['error']}")
            continue
        print(f"\n[{r['label']} | Course {course}]")
        print(f"  {r['g1_name']}: n={r['g1_n']}, Δ̄={r['g1_mean']:+.2f}, +/0/-={r['g1_plus']}/{r['g1_zero']}/{r['g1_minus']}")
        print(f"  {r['g2_name']}: n={r['g2_n']}, Δ̄={r['g2_mean']:+.2f}, +/0/-={r['g2_plus']}/{r['g2_zero']}/{r['g2_minus']}")
        print(f"  Mann-Whitney U={r['U']:.1f}, exact p={r['p']:.3f}")
        print(f"  Glass r_bs={r['r_bs']:+.2f} [95% CI {r['ci_lo']:+.2f}, {r['ci_hi']:+.2f}]")
        all_rows.append(r)

with open("./data/subgroup_results.csv", "w", newline="") as f:
    fields = ["label","course","g1_name","g1_n","g1_mean","g1_median","g1_plus","g1_zero","g1_minus",
              "g2_name","g2_n","g2_mean","g2_median","g2_plus","g2_zero","g2_minus",
              "U","p","r_bs","ci_lo","ci_hi"]
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    for r in all_rows:
        writer.writerow({k: (round(v, 3) if isinstance(v, float) else v) for k, v in r.items() if k in fields})
print(f"\nWrote ./data/subgroup_results.csv ({len(all_rows)} rows)")
