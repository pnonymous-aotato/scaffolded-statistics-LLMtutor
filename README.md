# SMARTS: Scaffolded LLM Tutors in Statistics Education

Supplementary materials for the paper **"From Answer Generators to
Thinking Partners: Scaffolded LLM Tutors in Statistics Education"**
(manuscript UJSE-2025-0250, *Journal of Statistics and Data Science
Education*).

This repository is the single canonical source for everything the
paper references as "supplementary material" or "released in the
supplementary repository." It serves three audiences:

1. **JSDSE reviewers and readers** — verifying that what the paper
   claims is actually in the materials.
2. **Statistics educators who want to adopt the approach** — system
   prompts, deployment guides, and transcripts they can read to
   understand how the assistants behave.
3. **Secondary-analysis researchers** — the full de-identified essay
   corpus, coded thematic data, and analysis code.

## How the repository maps to the paper

| Paper reference | Content in this repository |
|---|---|
| Figures 2 and 3 (SMARTS thinking-partner prompt) | `prompts/01_thinking_partner_bot.md` |
| §4.2 Course-Aligned Custom GPT Implementation | `prompts/` (all six templates) |
| §4.3 Example 1 (Lipitor hypothesis test) | `transcripts/courseA_01_lipitor_hypothesis_test.pdf` |
| §4.3 Example 2 (ANOVA + Tukey) | `transcripts/courseA_02_anova_tukey_gpa.pdf` |
| §4.3 Example 3 (unbiasedness of $\hat{\theta} = nY_{(1)}$) | `transcripts/courseB_03_unbiased_nY1_custom_gpt.pdf` |
| §4.3 Example 4 (unbiasedness of $S^2$, free prompt) | `transcripts/courseB_04_unbiased_S2_free_prompt.pdf` |
| Appendix C Session 5 (R-tutor Histogram) | `transcripts/courseA_05_rtutor_histogram.pdf` *(pending)* |
| Appendix C Session 6 (Mini-Gauntlet circumvention) | `transcripts/courseB_06_mini_gauntlet_circumvention.pdf` *(pending)* |
| §6.4 Open-ended survey corpus | `data/essay_corpus_long.csv` |
| §6.5 Qualitative analysis method | `data/codebook_themes.md` |
| §7.3 Thematic analysis (Course A themes) | `data/course_A_coded.csv`, `data/phase1_memo_course_A.md` |
| §7.3 Thematic analysis (Course B themes) | `data/course_B_coded.csv`, `data/phase1_memo_course_B.md` |
| §8.5 Broader portfolio of assistants | `prompts/` (all six archetypes including Mini-Gauntlet) |
| §8.6 Reproducibility statement | This repository |

## Repository structure

```
smarts-statistics-education/
├── README.md                    this file
├── LICENSE                      CC BY 4.0
├── CITATION.cff                 machine-readable citation metadata
│
├── paper/
│   ├── full_manuscript.pdf      current blinded manuscript
│   ├── appendix_links.md        section-by-section map to repo content
│   └── figures/                 source files for Figures 1, 2, 3
│
├── prompts/                     six bot archetypes (Markdown)
│   ├── 00_README.md             overview + deployment guide
│   ├── 01_thinking_partner_bot.md
│   ├── 02_coding_tutor_bot.md
│   ├── 03_topic_ta_bot.md
│   ├── 04_assessment_delivery_bot.md
│   ├── 05_exam_review_bot.md
│   └── 06_course_concierge_bot.md
│
├── data/                        de-identified research data
│   ├── README.md
│   ├── essay_corpus_long.csv            428 student open-ended responses
│   ├── course_A_coded.csv               thematic coding — Course A (189 rows)
│   ├── course_B_coded.csv               thematic coding — Course B (239 rows)
│   ├── codebook_themes.md               theme definitions & code-to-theme mapping
│   ├── phase1_memo_course_A.md          familiarization memo — Course A
│   ├── phase1_memo_course_B.md          familiarization memo — Course B
│   ├── demographics_summary.csv         underlying counts for Table 3 (pending)
│   ├── likert_item_wave_means.csv       underlying data for Tables 4, 5, S1 (pending)
│   └── survey_instrument.pdf            de-identified survey questionnaire (pending)
│
├── transcripts/                 annotated student-LLM interaction transcripts
│   ├── README.md
│   ├── courseA_01_lipitor_hypothesis_test.pdf          (§4.3 Example 1 / App. C Session 1)
│   ├── courseA_02_anova_tukey_gpa.pdf                  (§4.3 Example 2 / App. C Session 2)
│   ├── courseB_03_unbiased_nY1_custom_gpt.pdf          (§4.3 Example 3 / App. C Session 3)
│   ├── courseB_04_unbiased_S2_free_prompt.pdf          (§4.3 Example 4 / App. C Session 4)
│   ├── courseA_05_rtutor_histogram.pdf                 (App. C Session 5 — pending)
│   └── courseB_06_mini_gauntlet_circumvention.pdf      (App. C Session 6 — pending)
│
├── code/                        analysis scripts
│   ├── README.md
│   ├── code_course_A.py                 thematic coding script, Course A
│   ├── code_course_B.py                 thematic coding script, Course B
│   ├── likert_analysis.R                (pending) Cliff's delta, J-T tests
│   └── bootstrap_bca.R                  (pending) BCa bootstrap CIs
│
└── cite/
    ├── CITATION.bib                     BibTeX
    └── CITATION.ris                     RIS
```

## Quick start for adopters

If you're a statistics instructor who wants to try this approach in
your own course:

1. **Read** `prompts/00_README.md` for the six-archetype overview.
2. **Start with the Thinking Partner** (`prompts/01_thinking_partner_bot.md`)
   — the highest-leverage prompt. Replace the `{{PLACEHOLDER}}`
   variables with your course details, paste into a Custom GPT or
   Claude Project, and test it.
3. **Skim the transcripts** in `transcripts/` to see how the bot
   behaves in practice.
4. **Consult the paper** (`paper/full_manuscript.pdf`) for the full
   pedagogical rationale, survey data, and thematic analysis.

## License

All materials in this repository are released under the **Creative
Commons Attribution 4.0 International (CC BY 4.0)** license. Reuse,
adaptation, and commercial reuse are permitted provided the paper is
cited:

> author, A., et al. (2026). From Answer Generators to Thinking
> Partners: Scaffolded LLM Tutors in Statistics Education.
> *Journal of Statistics and Data Science Education* (in press).

See `LICENSE` for full license text. Machine-readable citation
metadata is in `cite/CITATION.bib` and `cite/CITATION.ris`.

## Data privacy and IRB

The essay corpus and transcripts contain no personally identifying
information. Respondent IDs (e.g., `T1_A_07`) are opaque and
cannot be mapped to student records. Research was conducted under
the IRB protocol documented in §7.1 of the manuscript.

Researchers wishing to re-use the corpus for secondary analysis are
asked to respect the de-identification convention: do not attempt to
re-identify respondents.

## Getting help / contributing

This repository is tied to a specific published study. It is not an
active software project. Questions:

- Implementation or adoption questions about the bot templates:
  open an issue tagged `adoption-question`.
- Questions about the study itself, methodology, or data:
  email the corresponding author (see paper title page).

Community-contributed adaptations of the templates (additional
languages, discipline-specific specializations) are welcome as pull
requests.

## Versioning

The repository is versioned by manuscript revision. The current
version corresponds to UJSE-2025-0250 Revision 1 (pre-review).
Substantive updates after manuscript acceptance will be released as
tagged versions and archived via Zenodo for DOI assignment.
