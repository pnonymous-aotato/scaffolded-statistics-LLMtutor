# Student-LLM Interaction Transcripts

Six annotated transcripts of student interactions with SMARTS-governed
custom GPTs (and, for comparison, one student-written system prompt).
Released as full verbatim PDF exports to support independent
inspection of the annotated excerpts in §4.3 and Appendix C.

## Paper mapping

| File | Paper reference | Course | Topic | Bot |
|---|---|---|---|---|
| `courseA_01_lipitor_hypothesis_test.pdf` | §4.3 Ex. 1 · App. C Sess. 1 | A (Course A) | Hypothesis test, Lipitor efficacy claim | SMARTS custom GPT |
| `courseA_02_anova_tukey_gpa.pdf` | §4.3 Ex. 2 · App. C Sess. 2 | A (Course A) | One-way ANOVA + Tukey HSD on GPA data | SMARTS custom GPT with explicit phase labels |
| `courseB_03_unbiased_nY1_custom_gpt.pdf` | §4.3 Ex. 3 · App. C Sess. 3 | B (Course B) | Unbiasedness of $\hat{\theta} = nY_{(1)}$ | Proof Construction Coaching custom GPT |
| `courseB_04_unbiased_S2_free_prompt.pdf` | §4.3 Ex. 4 · App. C Sess. 4 | B (Course B) | Unbiasedness of $S^2$ | Student-written system prompt (free prompt) |
| `courseA_05_rtutor_histogram.pdf` | App. C Sess. 5 | A (Course A) | Histogram construction in R | R-tutor custom GPT |
| `courseB_06_mini_gauntlet_circumvention.pdf` | App. C Sess. 6 | B (Course B) | Assessment delivery, attempted circumvention | Mini-Gauntlet custom GPT |

Files 5 and 6 are currently placeholders. When the PDFs are uploaded,
the `*.PLACEHOLDER` markers will be replaced with the actual
transcripts.

## Reproduction notes

- PDFs are the original ChatGPT-to-PDF exports provided by students
  with their assignment submissions. A cosmetic footer
  ("Printed using ChatGPT to PDF, powered by PDFCrowd HTML to PDF
  API") was present in the original exports.
- All student identifying information has been removed or was never
  present in the exports.
- The §4.3 excerpts reproduce turn-level content verbatim from these
  PDFs with minimal typographical adjustment only:
  - redaction of URL-style share links;
  - consistent notation for order statistics and hats on estimators;
  - line wrapping for the journal typesetter.
- Statistical content, student answers, and assistant responses are
  not modified.

## How to verify an annotated excerpt in §4.3 or Appendix C

1. Locate the example or session number in the paper (e.g., "Example 3"
   or "Session 3").
2. Open the corresponding transcript PDF from the table above.
3. The annotated excerpt in the paper reproduces the pivotal turns;
   the full transcript provides the complete surrounding context.
4. SMARTS phase labels in §4.3 are the coder's (instructor's)
   interpretive additions and are not present in the raw transcript.
   The coding is consistent with the SOLO-adapted rubric described in
   §6.5 of the manuscript.

## The custom GPT vs. free prompt comparison (§4.3 Examples 3 and 4)

Transcripts 3 and 4 constitute a direct side-by-side comparison of
two scaffolding regimes on adjacent unbiasedness topics:

- **Transcript 3** uses the Proof Construction Coaching custom GPT
  (see `../prompts/01_thinking_partner_bot.md` for the template).
  The assistant draws an explicit line between general formulas
  (shared freely) and application to the student's specific problem
  (withheld).

- **Transcript 4** uses a student-written system prompt that is
  pedagogically reasonable but softens that boundary — it asks for
  "hints, not entire solutions" but does not enforce a FRAME opener,
  does not prohibit completing identities after student consent, and
  privileges confirmation ("exactly right!") alongside
  hint-privileging.

The comparison is illustrative, not a statistical demonstration.
See §4.3 closing paragraph and §6.7 Limitations for the appropriate
caveats.

## License

All transcripts are released under Creative Commons Attribution 4.0
International (CC BY 4.0). Collected under the IRB protocol documented
in §7.1 of the paper with student consent for supplementary release.
