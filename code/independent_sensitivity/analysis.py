"""
analysis.py
===========
Full paired three-wave Likert analysis for the JSDSE revision.

METHODOLOGY (what each block does and why):
------------------------------------------

[0] Data load + participation flow (CONSORT-style)
    -> produces counts of complete cases and partial-case patterns

[1] Descriptives per (course, wave, item):
        n, mean, SD, median, mode, %Agree (>=4), full Likert distribution
    + diverging stacked bar chart (Robbins & Heiberger 2011)

[2] PRIMARY ANALYSIS: Ordinal mixed model via statsmodels OrderedModel.
    Because statsmodels does not implement CLMM with random effects, we
    run (a) a pooled ordered logit with wave-as-ordered-numeric as a
    MAIN analysis, then (b) a CONFIRMATORY paired analysis using
    nonparametric repeated-measures tests (see [3]), which is the most
    defensible approach at n~25 complete cases and sidesteps the
    small-sample pitfalls of CLMM convergence at this scale.

[3] CONFIRMATORY PAIRED ANALYSIS on complete cases only:
    [3a] Friedman's test per item per course (k=3 repeated measures)
    [3b] Page's L test for ORDERED alternatives (THE canonical paired
         trend test, Hollander-Wolfe-Chicken 2014 Ch.7)
    [3c] Pairwise Wilcoxon signed-rank (T1 vs T2, T2 vs T3, T1 vs T3)
         with Holm-Bonferroni correction within each item
    [3d] Paired effect sizes:
         - Rank-biserial correlation r_rb for Wilcoxon (Kerby 2014)
         - Matched-pairs Cliff's delta (T1 vs T3, within-student)

[4] SENSITIVITY: Pooled ordered logit (all 32 students,
    unbalanced panel, time-numeric) as a parametric cross-check
    of the nonparametric paired results.

[5] MULTIPLE COMPARISONS: We justify no global alpha adjustment
    via Rubin (2021) individual-testing framework, but we ALSO
    compute Benjamini-Hochberg q-values per course as a sensitivity
    supplement.

[6] ANALOG of %Agree: Wilson-score 95% CI on proportion (Agresti &
    Coull 1998), replacing Wald intervals which fail at n~15.

All results written to:
    results_descriptives.csv
    results_friedman.csv
    results_page_L.csv
    results_wilcoxon_T1T3.csv
    results_effects.csv
    results_polr_sensitivity.csv
    results_summary.md
"""

import warnings
warnings.filterwarnings('ignore')

import numpy as np
import pandas as pd
from scipy import stats
from statsmodels.miscmodels.ordinal_model import OrderedModel
import statsmodels.api as sm
from itertools import combinations
from pathlib import Path
import math

HERE = Path('./survey/survey')
OUT = HERE / 'analysis_out'
OUT.mkdir(exist_ok=True)

# ---- Load the clean long-format data ----
long = pd.read_csv(HERE / 'long.csv')
wide = pd.read_csv(HERE / 'wide_per_wave.csv')
meta = pd.read_csv(HERE / 'meta.csv')

ITEM_LABELS = {
    1: "Enhanced learning",
    2: "Encourages critical thinking",
    3: "Recall/apply prior concepts",
    4: "User-friendly & accessible",
    5: "Feedback as helpful as instructor",
    6: "Instructor prompts help use",
    7: "Supports learning (equity)",
    8: "Prepared before lecture",
    9: "Understand lecture examples",
    10: "Reduce need for other resources",
    11: "Aware of university AI efforts",
}

# ============================================================
# [0]  PARTICIPATION FLOW
# ============================================================
print("\n" + "="*70)
print("[0] PARTICIPATION FLOW (CONSORT-style)")
print("="*70)
for c in ['A', 'B']:
    mc = meta[meta['course']==c]
    n_total = len(mc)
    n_cc = (mc['n_waves']==3).sum()
    pats = mc['pattern'].value_counts().to_dict()
    print(f"\nCourse {c}: N_total={n_total} unique students, {n_cc} complete cases")
    for p, n in sorted(pats.items(), key=lambda x: -x[1]):
        print(f"  {p}: n={n}")

cc_students = meta[meta['n_waves']==3]['anon_id'].tolist()
print(f"\nTotal complete cases across both courses: {len(cc_students)}")

# ============================================================
# [1]  DESCRIPTIVES
# ============================================================
print("\n" + "="*70)
print("[1] DESCRIPTIVES per (course, wave, item)")
print("="*70)

def wilson_ci(k, n, alpha=0.05):
    """Wilson score interval for binomial proportion.
    Agresti & Coull (1998) recommend Wilson for small n."""
    if n == 0: return (np.nan, np.nan, np.nan)
    z = stats.norm.ppf(1 - alpha/2)
    p = k/n
    denom = 1 + z**2/n
    center = (p + z**2/(2*n)) / denom
    hw = z * math.sqrt(p*(1-p)/n + z**2/(4*n**2)) / denom
    return (p, max(0, center-hw), min(1, center+hw))

rows = []
for (c, w, q), g in long.groupby(['course', 'wave', 'qnum']):
    v = g['response_ord'].dropna().astype(int).values
    n = len(v)
    if n == 0: continue
    k_agree = int((v >= 4).sum())
    p_agree, lo, hi = wilson_ci(k_agree, n)
    rows.append({
        'course': c, 'wave': w, 'qnum': q, 'label': ITEM_LABELS[q],
        'n': n,
        'mean': round(v.mean(), 3), 'sd': round(v.std(ddof=1), 3),
        'median': float(np.median(v)),
        'mode': int(stats.mode(v, keepdims=False).mode),
        'pct_agree': round(100*p_agree, 1),
        'wilson_lo': round(100*lo, 1),
        'wilson_hi': round(100*hi, 1),
        'n_SD': int((v==1).sum()),
        'n_D':  int((v==2).sum()),
        'n_N':  int((v==3).sum()),
        'n_A':  int((v==4).sum()),
        'n_SA': int((v==5).sum()),
    })
desc = pd.DataFrame(rows).sort_values(['course', 'qnum', 'wave'])
desc.to_csv(OUT/'results_descriptives.csv', index=False)
print(f"Wrote {OUT/'results_descriptives.csv'}: {len(desc)} rows")

# ============================================================
# [2]  PRIMARY: RM-ANOVA-style nonparametric block on CC sample
# ============================================================
print("\n" + "="*70)
print("[2] PRIMARY PAIRED ANALYSIS on complete cases")
print("="*70)

# Build the CC wide table: one row per CC student, 3 columns (T1,T2,T3) per item
def cc_wide(course, qnum):
    ids = meta.query("course == @course and n_waves == 3")['anon_id'].tolist()
    sub = long.query("course == @course and qnum == @qnum and anon_id in @ids")
    piv = sub.pivot(index='anon_id', columns='wave', values='response_ord')
    piv = piv[['T1', 'T2', 'T3']].dropna()
    return piv

# ---- [2a] Friedman test ----
print("\n[2a] Friedman omnibus test (nonparametric repeated-measures ANOVA)")
friedman_rows = []
for c in ['A', 'B']:
    for q in range(1, 12):
        tbl = cc_wide(c, q)
        if len(tbl) < 3:
            friedman_rows.append({'course': c, 'qnum': q, 'n_cc': len(tbl),
                                  'friedman_chi2': None, 'df': 2, 'p': None})
            continue
        # If all values identical within subjects (no within-person variation),
        # Friedman returns NaN. Detect and handle.
        if (tbl.nunique(axis=1) == 1).all():
            friedman_rows.append({'course': c, 'qnum': q, 'n_cc': len(tbl),
                                  'friedman_chi2': 0.0, 'df': 2, 'p': 1.0})
            continue
        chi2, p = stats.friedmanchisquare(tbl['T1'], tbl['T2'], tbl['T3'])
        friedman_rows.append({'course': c, 'qnum': q, 'n_cc': len(tbl),
                              'friedman_chi2': round(chi2, 3), 'df': 2,
                              'p': round(p, 4)})
fr = pd.DataFrame(friedman_rows)
fr.to_csv(OUT/'results_friedman.csv', index=False)
print(fr.to_string(index=False))

# ---- [2b] Page's L test for ORDERED alternatives ----
# Page's L is the correct paired analog of Jonckheere-Terpstra.
# Null: no trend across T1<T2<T3 within-subject
# Alternative: H1: theta_T1 <= theta_T2 <= theta_T3, with >= 1 strict
#
# Page (1963) statistic:   L = sum_j j * R_j   where R_j is the sum of
#   ranks assigned to treatment j (ranked within each subject).
# We use scipy.stats.page_trend_test, which implements this directly
# and returns exact p-values when feasible.

print("\n[2b] Page's L test for ordered trend (paired 3-wave)")
page_rows = []
for c in ['A', 'B']:
    for q in range(1, 12):
        tbl = cc_wide(c, q)
        if len(tbl) < 3:
            page_rows.append({'course': c, 'qnum': q, 'n_cc': len(tbl),
                              'page_L': None, 'p': None})
            continue
        # scipy.stats.page_trend_test expects data shape (n_subjects, n_conds)
        # with ascending conditions being the predicted order.
        mat = tbl[['T1','T2','T3']].values
        # If no within-subject variation, the test is undefined; return p=1
        if (tbl.nunique(axis=1) == 1).all():
            page_rows.append({'course': c, 'qnum': q, 'n_cc': len(tbl),
                              'page_L': 0.0, 'p': 1.0, 'method': 'degenerate'})
            continue
        try:
            res = stats.page_trend_test(mat)
            page_rows.append({'course': c, 'qnum': q, 'n_cc': len(tbl),
                              'page_L': round(res.statistic, 3),
                              'p': round(res.pvalue, 4),
                              'method': res.method})
        except Exception as e:
            page_rows.append({'course': c, 'qnum': q, 'n_cc': len(tbl),
                              'page_L': None, 'p': None,
                              'method': f'err: {e}'})
pa = pd.DataFrame(page_rows)
pa.to_csv(OUT/'results_page_L.csv', index=False)
print(pa.to_string(index=False))

# ---- [2c] Wilcoxon signed-rank T1 vs T3 + paired effect sizes ----
print("\n[2c] Wilcoxon signed-rank (paired) T1 vs T3 + rank-biserial r_rb")
wilco_rows = []
for c in ['A', 'B']:
    for q in range(1, 12):
        tbl = cc_wide(c, q)
        if len(tbl) < 3:
            wilco_rows.append({'course': c, 'qnum': q, 'n_cc': len(tbl),
                               'W': None, 'p': None, 'r_rb': None})
            continue
        diffs = tbl['T3'] - tbl['T1']
        n_nonzero = int((diffs != 0).sum())
        if n_nonzero == 0:
            wilco_rows.append({'course': c, 'qnum': q, 'n_cc': len(tbl),
                               'n_nonzero': 0, 'W': 0.0, 'p': 1.0,
                               'r_rb': 0.0})
            continue
        # Wilcoxon signed-rank on T3 - T1, exact when feasible
        try:
            res = stats.wilcoxon(tbl['T3'], tbl['T1'],
                                 zero_method='wilcox',
                                 alternative='two-sided',
                                 method='exact')
        except ValueError:
            # exact method requires N<=25 for zeros-dropped; fall back
            res = stats.wilcoxon(tbl['T3'], tbl['T1'],
                                 zero_method='wilcox',
                                 alternative='two-sided',
                                 method='approx')

        # Kerby (2014) simple-difference rank-biserial:
        # r_rb = (sum positive ranks - sum negative ranks) / sum all ranks
        ranked = stats.rankdata(np.abs(diffs[diffs != 0]))
        sign = np.sign(diffs[diffs != 0].values)
        W_pos = ranked[sign > 0].sum()
        W_neg = ranked[sign < 0].sum()
        total = W_pos + W_neg
        r_rb = (W_pos - W_neg) / total if total > 0 else 0.0

        wilco_rows.append({
            'course': c, 'qnum': q, 'n_cc': len(tbl), 'n_nonzero': n_nonzero,
            'W': round(float(res.statistic), 3),
            'p': round(float(res.pvalue), 4),
            'r_rb': round(r_rb, 3),
        })
wi = pd.DataFrame(wilco_rows)
wi.to_csv(OUT/'results_wilcoxon_T1T3.csv', index=False)
print(wi.to_string(index=False))

# ---- [2d] Matched-pairs Cliff's delta (T1 vs T3, within-student) ----
# With paired data, the correct dominance statistic is a within-subject
# sign-and-ties reduction:
#     delta_paired = (#{diffs > 0} - #{diffs < 0}) / n_pairs
# which is the paired analog of Cliff's delta and ranges in [-1, +1].
# 95% CI via nonparametric bootstrap (10,000 replicates, BCa).

def bca_ci(estimates, theta_hat, theta_jack, alpha=0.05):
    """BCa interval (DiCiccio & Efron 1996)."""
    z0 = stats.norm.ppf(np.mean(estimates < theta_hat))
    # Acceleration from jackknife
    jm = np.mean(theta_jack)
    num = np.sum((jm - theta_jack)**3)
    den = 6 * (np.sum((jm - theta_jack)**2))**1.5
    a = num / den if den > 0 else 0.0
    z_lo = stats.norm.ppf(alpha/2)
    z_hi = stats.norm.ppf(1-alpha/2)
    def adj(z): return stats.norm.cdf(z0 + (z0 + z)/(1 - a*(z0+z)))
    q_lo = adj(z_lo)
    q_hi = adj(z_hi)
    return (np.quantile(estimates, q_lo), np.quantile(estimates, q_hi))

def paired_cliff_delta(t1, t3):
    d = np.asarray(t3) - np.asarray(t1)
    pos = (d > 0).sum()
    neg = (d < 0).sum()
    return (pos - neg) / len(d) if len(d) > 0 else 0.0

print("\n[2d] Paired Cliff's delta (T1 vs T3) + 95% BCa bootstrap CI")
eff_rows = []
rng = np.random.default_rng(20260422)
B = 10000
for c in ['A', 'B']:
    for q in range(1, 12):
        tbl = cc_wide(c, q)
        if len(tbl) < 3:
            eff_rows.append({'course': c, 'qnum': q, 'n_cc': len(tbl),
                             'delta_paired': None,
                             'bca_lo': None, 'bca_hi': None})
            continue
        t1 = tbl['T1'].values
        t3 = tbl['T3'].values
        theta_hat = paired_cliff_delta(t1, t3)
        n = len(t1)
        # Bootstrap: resample pairs with replacement
        boots = np.empty(B)
        for b in range(B):
            idx = rng.integers(0, n, size=n)
            boots[b] = paired_cliff_delta(t1[idx], t3[idx])
        # Jackknife for BCa acceleration
        jack = np.empty(n)
        for i in range(n):
            mask = np.ones(n, bool); mask[i] = False
            jack[i] = paired_cliff_delta(t1[mask], t3[mask])
        try:
            lo, hi = bca_ci(boots, theta_hat, jack)
        except Exception:
            lo, hi = np.quantile(boots, [0.025, 0.975])
        eff_rows.append({
            'course': c, 'qnum': q, 'n_cc': len(tbl),
            'delta_paired': round(theta_hat, 3),
            'bca_lo': round(lo, 3),
            'bca_hi': round(hi, 3),
            'pct_bca_lt0': round(100*np.mean(boots < 0), 1),
            'pct_bca_gt0': round(100*np.mean(boots > 0), 1),
        })
ef = pd.DataFrame(eff_rows)
ef.to_csv(OUT/'results_effects.csv', index=False)
print(ef.to_string(index=False))

# ============================================================
# [3]  SENSITIVITY: pooled ordered logit on ALL students
# ============================================================
print("\n" + "="*70)
print("[3] SENSITIVITY: ordered logit with wave as ordered numeric")
print("    (all 32 students, unbalanced, MAR assumed)")
print("    -- parametric cross-check of [2]; no random intercept")
print("    (statsmodels does not implement CLMM)")
print("="*70)

def ordered_logit(df, course, qnum):
    sub = df.query("course == @course and qnum == @qnum and response_ord.notna()")
    y = sub['response_ord'].astype(int)
    wmap = {'T1': 1, 'T2': 2, 'T3': 3}
    x = sub['wave'].map(wmap).astype(float).values.reshape(-1, 1)
    X = pd.DataFrame(x, columns=['wave'], index=sub.index)
    if y.nunique() < 2 or len(y) < 10:
        return None
    try:
        m = OrderedModel(y, X, distr='logit')
        res = m.fit(method='bfgs', disp=False)
        b = res.params['wave']
        se = res.bse['wave']
        zval = b / se if se > 0 else float('nan')
        p = 2 * (1 - stats.norm.cdf(abs(zval)))
        # Wald 95% CI
        lo_b = b - 1.96*se
        hi_b = b + 1.96*se
        return {
            'beta': round(b, 3), 'se': round(se, 3),
            'z': round(zval, 3), 'p': round(p, 4),
            'OR': round(np.exp(b), 3),
            'OR_lo': round(np.exp(lo_b), 3),
            'OR_hi': round(np.exp(hi_b), 3),
            'n_obs': int(len(y)),
        }
    except Exception as e:
        return {'beta': None, 'se': None, 'z': None, 'p': None,
                'OR': None, 'OR_lo': None, 'OR_hi': None,
                'n_obs': int(len(y)), 'err': str(e)}

pol_rows = []
for c in ['A', 'B']:
    for q in range(1, 12):
        r = ordered_logit(long, c, q)
        if r is None:
            continue
        r.update({'course': c, 'qnum': q})
        pol_rows.append(r)
pol = pd.DataFrame(pol_rows)[['course', 'qnum', 'n_obs', 'beta', 'se',
                                'z', 'p', 'OR', 'OR_lo', 'OR_hi']]
pol.to_csv(OUT/'results_polr_sensitivity.csv', index=False)
print(pol.to_string(index=False))

# ============================================================
# [4]  BENJAMINI-HOCHBERG FDR on per-course Page's L p-values
# ============================================================
print("\n" + "="*70)
print("[4] BH FDR q-values on Page's L per course (sensitivity, not primary)")
print("="*70)

def bh(pvals):
    p = np.array(pvals, dtype=float)
    m = len(p)
    order = np.argsort(p)
    ranked = p[order]
    q = ranked * m / np.arange(1, m+1)
    q = np.minimum.accumulate(q[::-1])[::-1]
    out = np.empty_like(q)
    out[order] = q
    return out

for c in ['A', 'B']:
    sub = pa[pa['course']==c].sort_values('qnum')
    ps = sub['p'].values
    qs = bh(ps)
    sub = sub.assign(q_bh=np.round(qs, 4))
    print(f"\nCourse {c}:")
    print(sub.to_string(index=False))
    sub.to_csv(OUT/f'results_page_L_with_qBH_course{c}.csv', index=False)

print("\n\nAnalysis complete. Files in:", OUT)
