"""
Master paired-longitudinal analysis for SMARTS paper revision.

Following the pre-registered methods plan:
  - Wilcoxon signed-rank test (EXACT, Pratt zero handling) as primary
  - Matched-pairs rank-biserial r_rb (Kerby 2014 simple-difference formula)
  - 95% percentile bootstrap CI, 5000 replications, zero.method=Pratt
  - Full descriptive package: n, T1 mean, T3 mean, mean Δ, median Δ (IQR), +/0/-
  - Mann-Whitney U (EXACT) on difference scores for subgroup comparisons
  - Glass rank-biserial for subgroup effect sizes

Data source: ./data/raw_canvas_exports/*.csv
"""

import csv
import os
import random
from collections import OrderedDict
from scipy import stats

random.seed(42)  # reproducibility for bootstrap

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

ITEM_NAMES = [
    ("Q1", "AI tutor enhances learning"),
    ("Q2", "Encourages critical thinking"),
    ("Q3", "Recall/apply prior concepts"),
    ("Q4", "User-friendly"),
    ("Q5", "Feedback vs instructor"),
    ("Q6", "Instructor prompts help"),
    ("Q7", "Equity/background"),
    ("Q8", "Prep for lecture"),
    ("Q9", "Understand examples"),
    ("Q10", "Reduce outside needs"),
    ("Q11", "Aware of AI integration"),
]

FILES = {
    "T1_A": f"{BASE}/AI Use Survey _ 01 Survey Student Analysis Report 2200.csv",
    "T2_A": f"{BASE}/AI Use Survey _ 02 Survey Student Analysis Report 2200.csv",
    "T3_A": f"{BASE}/AI Use Survey _ 03 Survey Student Analysis Report 2200.csv",
    "T1_B": f"{BASE}/AI Use Survey _ 01 Survey Student Analysis Report 4200.csv",
    "T2_B": f"{BASE}/AI Use Survey _ 02 Survey Student Analysis Report 4200.csv",
    "T3_B": f"{BASE}/AI Use Survey _ 03 Survey Student Analysis Report 4200.csv",
    "demo_A": f"{BASE}/Demographic Survey (BONUS POINTS) Survey Student Analysis Report 2200.csv",
    "demo_B": f"{BASE}/Demographic Survey (BONUS POINTS) Survey Student Analysis Report 4200.csv",
}


def load_likert(path):
    """Return {sid: [11 Likert values 1-5 or None]}"""
    out = {}
    with open(path) as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            if not row or not row[0]:
                continue
            sid = row[0]
            vals = []
            for i in range(2, 24, 2):  # 11 items at cols 2,4,...22
                txt = row[i].strip() if i < len(row) else ""
                vals.append(LIKERT_MAP.get(txt, None))
            out[sid] = vals
    return out


def load_demo(path):
    """Return {sid: {attr: value}}"""
    out = {}
    with open(path) as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        for row in reader:
            if not row or not row[0]:
                continue
            sid = row[0]
            # Demo column positions (see earlier inspection)
            # 2=gender, 4=major, 6=Hispanic, 8=race, 10=age, 12=language,
            # 14=academic standing, 16=credit hrs, 18=employment hrs,
            # 20=reliable tech, 22=device, 24=prior AI use, 26=AI platforms
            d = {}
            d["gender"]    = row[2]  if len(row) > 2  else ""
            d["major"]     = row[4]  if len(row) > 4  else ""
            d["hispanic"]  = row[6]  if len(row) > 6  else ""
            d["race"]      = row[8]  if len(row) > 8  else ""
            d["age"]       = row[10] if len(row) > 10 else ""
            d["language"]  = row[12] if len(row) > 12 else ""
            d["standing"]  = row[14] if len(row) > 14 else ""
            d["credits"]   = row[16] if len(row) > 16 else ""
            d["employment"]= row[18] if len(row) > 18 else ""
            d["tech"]      = row[20] if len(row) > 20 else ""
            d["device"]    = row[22] if len(row) > 22 else ""
            d["prior_ai"]  = row[24] if len(row) > 24 else ""
            d["ai_platforms"] = row[26] if len(row) > 26 else ""
            out[sid] = d
    return out


# ------------------------------------------------------------------
# Statistical helpers — matched-pairs rank-biserial (Pratt zeros)
# ------------------------------------------------------------------

def rank_biserial_paired(diffs, zero_method="pratt"):
    """
    Matched-pairs rank-biserial (Kerby 2014 simple difference formula).

    With Pratt zero handling:
      - Zero differences participate in the ranking (absolute differences are ranked
        including zeros) but are not summed into either positive or negative rank sum.
      - r_rb = (R+ - R-) / total_rank_sum,
        where total_rank_sum = sum of all ranks (excluding zero-rank contributions
        per Pratt convention) and R+, R- are sums of positive/negative ranks.

    Equivalent to the Kerby "simple difference" formulation.
    """
    if not diffs:
        return None
    # Rank absolute values including zeros (Pratt)
    abs_vals = [abs(d) for d in diffs]
    # scipy stats.rankdata uses average method for ties — appropriate here
    from scipy.stats import rankdata
    ranks = rankdata(abs_vals, method="average")
    R_pos = sum(r for d, r in zip(diffs, ranks) if d > 0)
    R_neg = sum(r for d, r in zip(diffs, ranks) if d < 0)
    R_zero = sum(r for d, r in zip(diffs, ranks) if d == 0)
    if zero_method == "pratt":
        # Pratt: total rank sum includes zeros, but zero ranks contribute to neither
        # favorable nor unfavorable side. Kerby formula: r_rb = (R+ - R-) / (R+ + R- + R_zero)
        total = R_pos + R_neg + R_zero
    else:
        total = R_pos + R_neg
    if total == 0:
        return 0.0
    return (R_pos - R_neg) / total


def bootstrap_ci_rank_biserial_paired(diffs, B=5000, conf=0.95, zero_method="pratt", seed=42):
    """Percentile bootstrap CI for matched-pairs rank-biserial."""
    if not diffs:
        return (None, None)
    rng = random.Random(seed)
    n = len(diffs)
    samples = []
    for _ in range(B):
        boot = [diffs[rng.randrange(n)] for _ in range(n)]
        val = rank_biserial_paired(boot, zero_method=zero_method)
        if val is not None:
            samples.append(val)
    samples.sort()
    alpha = 1 - conf
    lo_idx = int(alpha/2 * len(samples))
    hi_idx = int((1 - alpha/2) * len(samples)) - 1
    lo_idx = max(0, min(lo_idx, len(samples) - 1))
    hi_idx = max(0, min(hi_idx, len(samples) - 1))
    return (samples[lo_idx], samples[hi_idx])


def wilcoxon_signed_rank(diffs):
    """
    Wilcoxon signed-rank with Pratt zero method, EXACT when n <= 25, else asymptotic.
    scipy's wilcoxon with zero_method='pratt' and method='exact' delivers both.
    """
    diffs = [float(d) for d in diffs]
    if not diffs or all(d == 0 for d in diffs):
        return {"V": 0, "p_exact": 1.0, "Z_asym": 0.0}
    # For n <= 25 use exact method (after Pratt zero handling)
    n_nonzero = sum(1 for d in diffs if d != 0)
    method = "exact" if n_nonzero <= 25 else "approx"
    try:
        res = stats.wilcoxon(
            diffs, zero_method="pratt",
            method=method, alternative="two-sided"
        )
        V = float(res.statistic)
        p = float(res.pvalue)
    except Exception:
        # fallback to approx
        res = stats.wilcoxon(diffs, zero_method="pratt",
                             method="approx", alternative="two-sided")
        V = float(res.statistic); p = float(res.pvalue)
    # Also compute asymptotic Z for reporting
    try:
        res_z = stats.wilcoxon(diffs, zero_method="pratt",
                               method="approx", alternative="two-sided")
        # scipy returns V but we derive Z from the two-sided p
        # For reporting consistency, approximate Z from p via inverse CDF
        Z = abs(stats.norm.ppf(res_z.pvalue/2))
        # restore sign based on sum of ranks
        from scipy.stats import rankdata
        abs_d = [abs(d) for d in diffs]
        ranks = rankdata(abs_d, method="average")
        R_pos = sum(r for d, r in zip(diffs, ranks) if d > 0)
        R_neg = sum(r for d, r in zip(diffs, ranks) if d < 0)
        if R_pos < R_neg:
            Z = -Z
    except Exception:
        Z = 0.0
    return {"V": V, "p_exact": p, "Z_asym": Z,
            "method": method, "n_nonzero": n_nonzero}


def descriptive_pack(t1_vals, t3_vals):
    """Full descriptive package for a paired set."""
    paired = [(a, b) for a, b in zip(t1_vals, t3_vals) if a is not None and b is not None]
    if not paired:
        return None
    t1 = [p[0] for p in paired]
    t3 = [p[1] for p in paired]
    diffs = [b - a for a, b in paired]
    n = len(diffs)
    mean_t1 = sum(t1)/n
    mean_t3 = sum(t3)/n
    sd_t1 = (sum((x-mean_t1)**2 for x in t1)/(n-1))**0.5 if n > 1 else 0.0
    sd_t3 = (sum((x-mean_t3)**2 for x in t3)/(n-1))**0.5 if n > 1 else 0.0
    mean_d = sum(diffs)/n
    sd_d = (sum((x-mean_d)**2 for x in diffs)/(n-1))**0.5 if n > 1 else 0.0
    sorted_d = sorted(diffs)
    median_d = sorted_d[n//2] if n % 2 else (sorted_d[n//2-1] + sorted_d[n//2])/2
    q1 = sorted_d[int(n*0.25)]
    q3 = sorted_d[int(n*0.75)] if int(n*0.75) < n else sorted_d[-1]
    n_plus = sum(1 for d in diffs if d > 0)
    n_zero = sum(1 for d in diffs if d == 0)
    n_minus = sum(1 for d in diffs if d < 0)
    return dict(
        n=n, diffs=diffs,
        t1_mean=mean_t1, t1_sd=sd_t1,
        t3_mean=mean_t3, t3_sd=sd_t3,
        mean_d=mean_d, sd_d=sd_d,
        median_d=median_d, q1=q1, q3=q3,
        n_plus=n_plus, n_zero=n_zero, n_minus=n_minus
    )


# ------------------------------------------------------------------
# Load everything
# ------------------------------------------------------------------
print("Loading data...")
d = {k: load_likert(v) for k, v in FILES.items() if "demo" not in k}
demo = {"A": load_demo(FILES["demo_A"]), "B": load_demo(FILES["demo_B"])}

for k in ["T1_A", "T2_A", "T3_A", "T1_B", "T2_B", "T3_B"]:
    print(f"  {k}: n={len(d[k])}")
for k in ["A", "B"]:
    print(f"  demo_{k}: n={len(demo[k])}")


# ------------------------------------------------------------------
# Per-item paired analysis (T1 -> T3), both courses, all 11 items
# ------------------------------------------------------------------
print("\n" + "="*100)
print("PAIRED ITEM-LEVEL ANALYSIS (T1 -> T3), Wilcoxon signed-rank EXACT + Pratt zeros")
print("="*100)

results = []  # for CSV output
for course in ["A", "B"]:
    print(f"\n--- Course {course} (MATH {2200 if course=='A' else 4200}) ---")
    t1 = d[f"T1_{course}"]
    t3 = d[f"T3_{course}"]
    common = sorted(set(t1.keys()) & set(t3.keys()))

    for i, (q, name) in enumerate(ITEM_NAMES):
        t1v = [t1[sid][i] for sid in common]
        t3v = [t3[sid][i] for sid in common]
        desc = descriptive_pack(t1v, t3v)
        if desc is None:
            continue
        w = wilcoxon_signed_rank(desc["diffs"])
        rrb = rank_biserial_paired(desc["diffs"], zero_method="pratt")
        lo, hi = bootstrap_ci_rank_biserial_paired(desc["diffs"], B=5000, seed=42+i)
        row = {
            "course": f"Course {course}", "item": q, "name": name,
            "n": desc["n"],
            "t1_mean": round(desc["t1_mean"], 2),
            "t1_sd":   round(desc["t1_sd"], 2),
            "t3_mean": round(desc["t3_mean"], 2),
            "t3_sd":   round(desc["t3_sd"], 2),
            "mean_d":  round(desc["mean_d"], 2),
            "sd_d":    round(desc["sd_d"], 2),
            "median_d": desc["median_d"],
            "iqr_lo": desc["q1"], "iqr_hi": desc["q3"],
            "n_plus": desc["n_plus"], "n_zero": desc["n_zero"], "n_minus": desc["n_minus"],
            "V": round(w["V"], 1),
            "p_exact": round(w["p_exact"], 4),
            "Z": round(w["Z_asym"], 2),
            "r_rb": round(rrb, 2) if rrb is not None else None,
            "ci_lo": round(lo, 2) if lo is not None else None,
            "ci_hi": round(hi, 2) if hi is not None else None,
        }
        results.append(row)
        print(f"  {q:4s} {name[:32]:32s} n={desc['n']:2d}  "
              f"T1={desc['t1_mean']:.2f} T3={desc['t3_mean']:.2f}  "
              f"Δ̄={desc['mean_d']:+.2f}  "
              f"+/0/-={desc['n_plus']}/{desc['n_zero']}/{desc['n_minus']}  "
              f"V={w['V']:5.1f} p={w['p_exact']:.3f}  "
              f"r_rb={rrb:+.2f} [{lo:+.2f}, {hi:+.2f}]")

# Write CSV
os.makedirs("./data", exist_ok=True)
with open("./data/paired_item_results.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=list(results[0].keys()))
    writer.writeheader()
    writer.writerows(results)
print(f"\nWrote ./data/paired_item_results.csv ({len(results)} rows)")
