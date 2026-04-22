# Paper-to-Repository Section Crosswalk

For JSDSE reviewers: a detailed section-by-section mapping from the
manuscript to the supporting material in this repository. Use this
document to verify any specific claim, quote, table, or figure in
the paper.

## Section 1 — Introduction

No supplementary material required. The introduction is narrative
and cites published literature only.

## Section 2 — Literature

No supplementary material required. All citations are in the
reference list of the manuscript.

## Section 3 — Course Context

Course-context descriptions are narrative. See §7.1 for demographic
data.

## Section 4 — The SMARTS Framework and Course-Aligned Assistants

### §4.1 The SMARTS Protocol (Figures 2 and 3)

The in-paper Figures 2 and 3 reproduce the SMARTS thinking-partner
prompt verbatim. The corresponding repository content is:

- `prompts/01_thinking_partner_bot.md` — full template with
  placeholder variables and deployment notes. The Markdown version
  includes five response-pattern categories, a forbidden-phrases
  list, and an end-of-response self-check that are all present in
  the deployed version but not all reproduced in the paper figure
  for space reasons.

- `prompts/00_README.md` — six-archetype overview including
  recommended models, deployment targets, and quick customization
  checklist.

### §4.2 Course-Aligned Custom GPT Implementation

- `prompts/02_coding_tutor_bot.md` — the R-tutor specialization.
  Restricted to `mosaic` and `BSDA` packages; explains every line
  of code; beginner-friendly tone.

- `prompts/03_topic_ta_bot.md` — the chapter-specific in-class
  assistant template. One bot per chapter, restricted to that
  chapter's materials.

### §4.3 SMARTS in Action: Annotated Examples

Four worked examples; full transcripts in `transcripts/`:

- **Example 1** (Course A, Lipitor hypothesis test) —
  `transcripts/courseA_01_lipitor_hypothesis_test.pdf`
- **Example 2** (Course A, ANOVA + Tukey HSD) —
  `transcripts/courseA_02_anova_tukey_gpa.pdf`
- **Example 3** (Course B, unbiasedness of $\hat\theta = nY_{(1)}$, custom GPT) —
  `transcripts/courseB_03_unbiased_nY1_custom_gpt.pdf`
- **Example 4** (Course B, unbiasedness of $S^2$, free prompt) —
  `transcripts/courseB_04_unbiased_S2_free_prompt.pdf`

## Section 5 — Academic Integrity and Assessment Design

- `prompts/04_assessment_delivery_bot.md` — the Mini-Gauntlet
  template. Implements refusal-by-default posture, two-attempt
  limit per item, and answer + explanation dual scoring.

## Section 6 — Methods

### §6.3 Participants and sample size

- `data/demographics_summary.csv` (pending) — underlying counts
  for Table 3. Course A: 15 enrolled / 14 demographic responses /
  14–13 AI Use Survey responses across waves. Course B: 18
  enrolled / 18 demographic responses / 17–17 AI Use Survey
  responses.

### §6.4 Data sources

- `data/survey_instrument.pdf` (pending) — de-identified survey
  questionnaire (11 Likert + 5 essay items).
- `data/essay_corpus_long.csv` — the 428 open-ended responses.

### §6.5 Analysis plan

Both quantitative and qualitative procedures described in this
section are implemented in `code/`:

- Thematic analysis: `code/code_course_A.py`, `code/code_course_B.py`
- Likert trend analysis: `code/likert_analysis.R` (pending)
- BCa bootstrap CIs: `code/bootstrap_bca.R` (pending)

See `data/codebook_themes.md` and the two `phase1_memo_course_*.md`
files for the Braun & Clarke phase-by-phase documentation.

### §6.7 Limitations (including reflexivity statement)

The reflexivity statement is supported by:

- `data/course_A_coded.csv` and `data/course_B_coded.csv` — each
  coded extract has a coder note for boundary cases, providing an
  auditable trail of coding decisions.

## Section 7 — Results

### §7.1 Participants and demographics

- `data/demographics_summary.csv` (pending)

### §7.2 Likert trends

- `data/likert_item_wave_means.csv` (pending) — the raw data
  underlying Tables 4, 5, and S1.

### §7.3 Open-ended thematic analysis

- **Table 5 (theme counts):** derived from
  `data/course_A_coded.csv` and `data/course_B_coded.csv` via
  `code/code_course_*.py`.
- **Each quotation cited:** trace `respondent_id` in
  `data/essay_corpus_long.csv` to the full response.
- **Theme definitions and code-to-theme mapping:**
  `data/codebook_themes.md`.

## Section 8 — Discussion

### §8.4 Limitations

Discussed in text; no supplementary material required.

### §8.5 Broader Portfolio of Course-Aligned Assistants

Maps to the six bot archetypes:

- Skeleton layer: `prompts/01_thinking_partner_bot.md`
- Course-aligned layer:
  - `prompts/02_coding_tutor_bot.md` (R-tutor)
  - `prompts/03_topic_ta_bot.md` (chapter-specific)
  - `prompts/05_exam_review_bot.md` (exam review + practice
    generator)
  - `prompts/06_course_concierge_bot.md` (syllabus assistant)
- Variant layer: `prompts/04_assessment_delivery_bot.md`
  (Mini-Gauntlet family)

### §8.6 Data and materials availability

This repository is the supplementary repository referenced throughout
the paper. Its URL will be injected here on acceptance.

## Appendix B — Supplementary Likert Tables

- `data/likert_item_wave_means.csv` (pending) — underlying data for
  Table S1 (all 11 instrument items).

## Appendix C — Six Worked SMARTS Sessions

Sessions 1–4 are the full transcripts underlying §4.3 Examples 1–4
(see §4.3 mapping above). Sessions 5 and 6 are additional
illustrations:

- **Session 5** (Course A, R-tutor Histogram) —
  `transcripts/courseA_05_rtutor_histogram.pdf` (pending)
- **Session 6** (Course B, Mini-Gauntlet attempted circumvention) —
  `transcripts/courseB_06_mini_gauntlet_circumvention.pdf` (pending)

## Appendix D — Anonymized Course Syllabi

Referenced in the manuscript; syllabi themselves are to be released
in a separate pending upload with institutional-identifier redaction.

---

## Items marked "pending" in this crosswalk

Content that is referenced in the paper and scheduled for release in
this repository but not yet populated:

1. `data/demographics_summary.csv`
2. `data/likert_item_wave_means.csv`
3. `data/survey_instrument.pdf`
4. `transcripts/courseA_05_rtutor_histogram.pdf`
5. `transcripts/courseB_06_mini_gauntlet_circumvention.pdf`
6. `code/likert_analysis.R`
7. `code/bootstrap_bca.R`
8. Anonymized syllabi for Appendix D

Each item will be populated before the manuscript is published. The
current repository version is tagged as `v1.0.0-revision1` for the
pre-review revision submission.
