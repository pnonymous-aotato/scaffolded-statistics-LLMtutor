# Data Files

Research data supporting the survey and thematic analysis reported in
§6–§7 of the paper. All files are de-identified; respondent IDs are
opaque course-internal identifiers that cannot be mapped to student
records without access to the instructor's roster.

## What is and is NOT in this folder

This folder contains the **cleaned, de-identified intermediate data**
needed to reproduce every number, table, and figure in the paper.

**Not included (FERPA):** The raw Canvas survey exports (CSV exports of
each wave's attitude and demographic surveys) contain individual-level
student response rows paired to institutional Canvas IDs. Even with
names stripped, these rows constitute an educational record under
FERPA and cannot be released publicly. Qualified researchers seeking
replication access may contact the authors for a Data Use Agreement.
The cleaned intermediate CSVs in this folder (Likert means by item
and wave, thematic codings with opaque wave-response IDs, paired and
subgroup results) are the reproducible analytical inputs to the
reported tables and figures.

Python scripts in `../code/` expect raw Canvas exports at
`./data/raw_canvas_exports/` if you have them under a Data Use
Agreement. All downstream analyses (`paired_item_results.csv`,
`subgroup_results.csv`, `sensitivity_*.csv`) reproduce directly from
the files in this folder.

## Contents

| File | Paper reference | Rows | Description |
|---|---|---:|---|
| `essay_corpus_long.csv` | §6.4, §7.3 | 428 | The full de-identified corpus of student free-text responses. |
| `course_A_coded.csv` | §7.3 (Themes A1–A5) | 189 | Thematic coding of Course A (the introductory statistics course) responses. |
| `course_B_coded.csv` | §7.3 (Themes B1–B7) | 239 | Same schema as Course A. |
| `codebook_themes.md` | §7.3 Table 5 | — | Final codebook with theme definitions, code-to-theme mappings, exemplar quotes. |
| `phase1_memo_course_A.md` | §6.5 | — | Familiarization memo (Braun & Clarke Phase 1) for Course A. |
| `phase1_memo_course_B.md` | §6.5 | — | Same for Course B. |
| `demographics_summary.csv` | §7.1 Table 1 | *pending* | Underlying counts for the demographics table. |
| `paired_item_results.csv` | §7.2 Tables 2, 3, S1 | 22 | **NEW.** Paired T1→T3 results for all 11 Likert items × 2 courses. |
| `subgroup_results.csv` | §7.4 Table 4 | 8 | **NEW.** Pre-specified subgroup comparisons (4 analyses × 2 courses). |
| `survey_instrument.pdf` | §6.4 Appendix B | *pending* | De-identified survey questionnaire (11 Likert + 5 essay items). |

## Schema: `paired_item_results.csv`

| Column | Description |
|---|---|
| `course` | `Course A` or `Course B` |
| `item` | Q1–Q11 |
| `name` | Short item description |
| `n` | Paired T1∩T3 sample size |
| `t1_mean`, `t1_sd` | T1 descriptive statistics |
| `t3_mean`, `t3_sd` | T3 descriptive statistics |
| `mean_d`, `sd_d` | Mean and SD of T3−T1 |
| `median_d`, `iqr_lo`, `iqr_hi` | Median paired difference and IQR |
| `n_plus`, `n_zero`, `n_minus` | Tripartite count |
| `V` | Wilcoxon signed-rank statistic (Pratt zero handling) |
| `p_exact` | Exact two-sided p-value |
| `r_rb`, `ci_lo`, `ci_hi` | Matched-pairs rank-biserial correlation and 95% CI |

## Schema: `subgroup_results.csv`

| Column | Description |
|---|---|
| `label` | Analysis label, e.g. "A1: Hispanic/Latino × Q7 equity" |
| `course` | `A` or `B` |
| `g1_name`, `g2_name` | Subgroup labels |
| `g1_n`, `g2_n` | Subgroup sizes |
| `g1_mean`, `g2_mean`, `g1_median`, `g2_median` | Per-subgroup descriptives |
| `g*_plus`, `g*_zero`, `g*_minus` | Tripartite counts per subgroup |
| `U`, `p` | Mann-Whitney U statistic, exact p |
| `r_bs`, `ci_lo`, `ci_hi` | Glass rank-biserial correlation, 95% CI |

## Reproducing the paired Likert analysis

```bash
python3 ../code/run_paired_main.py        # generates paired_item_results.csv
python3 ../code/run_subgroup_analyses.py  # generates subgroup_results.csv
python3 ../code/make_figure5.py           # regenerates Figure 5 (arrow plot)
```

These scripts require `scipy` and `matplotlib`.

## Analytical choices documented in the paper

- **Wilcoxon signed-rank with Pratt zeros, exact method:** §6.5, citing
  Bellera, Julien & Hanley (2010); Pratt (1959); Meek, Ozgur &
  Dunning (2007)
- **Matched-pairs rank-biserial:** §6.5, citing Kerby (2014)
- **Percentile bootstrap (not BCa):** §6.5, reflecting the small-sample
  caveat in Mangiafico (2016)
- **No multiple-comparison adjustment:** §6.5 inferential framing

## License

CC BY 4.0. Cite the paper and respect de-identification.
