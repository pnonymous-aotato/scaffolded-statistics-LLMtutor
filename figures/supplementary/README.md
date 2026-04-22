# Supplementary Figures

Additional figures complementing the main paper's Figure 5 (CONSORT
participation flow) and Figure 6 (T1→T3 paired-change arrow plot).
These figures are referenced in the paper's Appendix E and are intended
for readers who want deeper item-level or transition-level views of
the data.

All figures were generated directly from the cleaned Canvas survey data
using scripts in `../../code/` and share the visual style (color palette,
typography) of the main-paper figures.

## Contents

| File | Description | Generator |
|---|---|---|
| `divergingBars_courseA.png` | Course A (Course A) diverging stacked bar chart showing response distribution for all 11 Likert items across three waves (T1/T2/T3). Bars are centered at the Neutral midpoint per the Robbins & Heiberger (2011) convention. | `code/make_diverging_bars.py` |
| `divergingBars_courseB.png` | Same for Course B (Course B). | `code/make_diverging_bars.py` |
| `trajectory_Q7.png` | Individual student trajectories for Q7 (Supports learning regardless of background) across all three waves, shown side by side for Course A and Course B. Red diamonds trace the per-wave median. This is the item with the notable decline in Course A. | `code/make_supplementary_figures.py` |
| `trajectory_Q8.png` | Same for Q8 (Prepared before lecture) — our strongest primary effect in Course A. | `code/make_supplementary_figures.py` |
| `trajectory_Q9.png` | Same for Q9 (Understand lecture examples) — one of the three Course A items with rank-biserial CI excluding zero. | `code/make_supplementary_figures.py` |
| `transitions_Q7.png` | T1→T3 transition heatmap for Q7 in both courses. Each cell counts students moving from the T1 response (row) to the T3 response (column). Shows the downward movement pattern on the equity item in Course A. | `code/make_supplementary_figures.py` |
| `transitions_Q8.png` | Same for Q8 — shows the upward transition pattern that produces the paired r_rb = +0.70 effect. | `code/make_supplementary_figures.py` |

## Reproduction

```bash
cd ../../code
python3 make_diverging_bars.py
python3 make_supplementary_figures.py
```

All scripts read from the cleaned Canvas CSVs and are deterministic
(seeded `numpy.random.seed(42)` for the trajectory jitter).

## Citation

All figures are released under CC BY 4.0 per the repository license.
Cite the main paper when reusing.
