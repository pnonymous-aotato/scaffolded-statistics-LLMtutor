# Independent Sensitivity Analysis Pipeline

Scripts used by a second analyst to independently produce the
sensitivity analyses reported in Appendix~E of the paper:

- Friedman omnibus test
- Page's L ordered-trend test
- Paired Cliff's δ with BCa bootstrap
- Pooled ordered logistic regression

## Files

| Script | Purpose |
|---|---|
| `clean_data.py` | Data cleaning pipeline (produces `long.csv`, `wide_per_wave.csv`, `meta.csv`) |
| `analysis.py` | Full statistical analysis (Friedman, Page's L, paired Wilcoxon, Cliff's δ with BCa, ordered logit sensitivity) |
| `figures.py` | All figure generation (diverging stacked bars, trajectory plots, CONSORT flow, transition heatmaps) |
| `essays.py` | Open-ended response extraction and keyword analysis |
| `demographics.py` | Demographic cleaning |

## How this relates to the primary analysis

The primary T1→T3 paired Wilcoxon + rank-biserial analysis is in
`../run_paired_main.py` (same directory one level up). The independent
sensitivity pipeline uses a stricter complete-case subsample
(T1∩T2∩T3, n=11 Course A, n=14 Course B) to enable three-wave trend
tests. Both analyses are directionally concordant.

## Seeds

Deterministic: `np.random.default_rng(20260422)` throughout.

## Dependencies

- scipy
- numpy
- pandas
- matplotlib

## Reproduce

```bash
python3 clean_data.py
python3 analysis.py
python3 figures.py
python3 essays.py
python3 demographics.py
```
