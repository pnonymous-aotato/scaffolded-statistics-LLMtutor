# Analysis Code

Scripts that reproduce the quantitative and qualitative analyses
reported in the paper.

## Contents

| File | Paper reference | Language | Dependencies |
|---|---|---|---|
| `code_course_A.py` | §7.3 (Themes A1–A5) | Python 3 | standard library only |
| `code_course_B.py` | §7.3 (Themes B1–B7) | Python 3 | standard library only |
| `likert_analysis.R` | §7.2 Tables 4, 5, S1 | R | `stats`, `boot`, `clm` (pending) |
| `bootstrap_bca.R` | §7.2 Cliff's δ CIs | R | `boot` (pending) |

## Reproducing the thematic analysis

```bash
python3 code_course_A.py
python3 code_course_B.py
```

Each script:

1. Reads the corresponding `course_X_coded.csv` from `../data/`
2. Recomputes the code frequency table (by question, by theme)
3. Prints summary statistics matching those in §7.3 Table 5

The scripts are the canonical record of the coding decisions
documented in the Braun & Clarke thematic analysis. Each of the 428
coded extracts is represented as a tuple with the codes assigned and
an optional coder note for boundary cases.

## Reproducing the Likert trend analysis

The Likert trend analysis uses:

- **Jonckheere–Terpstra trend test** — `DescTools::JonckheereTerpstraTest`
  applied within each (item, course) combination.
- **Cliff's δ** — custom implementation matching the definition
  $\delta = P(Y > X) - P(Y < X)$ with $X$ = T1, $Y$ = T3.
- **95% bootstrap CI for δ** — 5,000 percentile-bootstrap replications
  (to be upgraded to BCa in `bootstrap_bca.R`).
- **Proportional-odds ordinal regression** — `MASS::polr` with wave
  as an ordered numeric predictor.

The analysis script `likert_analysis.R` is pending inclusion in this
repository; it will be added when the revised manuscript is resubmitted.

## Licenses

All code in this directory is released under CC BY 4.0 consistent
with the rest of the repository.
