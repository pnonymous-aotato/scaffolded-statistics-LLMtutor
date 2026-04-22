# Phase 1 Familiarization Memo — Course B (Course B, Advanced Mathematical Statistics)

**Coder:** A. redacted (solo, reflexivity declared in §6.7)
**Corpus:** 239 substantive free-text responses (n = 17/14/17 students at T1/T2/T3, five essay questions per wave)
**Approach:** Hybrid inductive/deductive — deductive scaffolding from the five survey question domains, inductive codes generated within each domain, coded independently of Course A (separate thematic analyses per course, per user instruction).

---

## 1. First-read impressions

Course B responses are substantially longer and more technically elaborated than Course A. Students use discipline-specific vocabulary (MLE, likelihood function, hypothesis testing, theorems, ANOVA, Duncan tests, sampling distributions, order statistics). One T2 response (T2_B_07) pastes a genuine back-and-forth with the AI including LaTeX-rendered variance computation, demonstrating how the students engage in mathematical dialogue with the assistant. This concrete evidence of proof-style interaction is unique to Course B and valuable for §4.3 and §7.4.

The *tone* is more reflective and more metacognitively aware than Course A. Students articulate specific trade-offs: availability vs. memory retention (T1_B_10), quick problem-solving vs. deeper critical thinking (T3_B_07, T3_B_13), convenience vs. genuine learning (T3_B_09). This meta-awareness is an interesting contrast to Course A's more instrumental framing and likely deserves its own theme.

Two distinctive features of Course B emerged on first read:

1. **Textbook/theorem lookup as a central use case.** Multiple students (T1_B_04, T2_B_09, T3_B_10, T3_B_11, T3_B_13) describe asking the AI for specific theorems or definitions to avoid flipping through Wackerly. This is a course-level distinctive — introductory students don't describe it this way.

2. **Epistemic tension and verification.** Course B students are noticeably more vigilant about AI errors. T2_B_07's long excerpt shows the student arguing with the AI's variance computation; T3_B_12 says "many times where I have questioned its results and had to argue with it"; T2_B_10 describes "arguing with it, I gave up and asked Dr. Y." This critical-engagement-with-AI pattern is rich and warrants a distinct code family.

---

## 2. Domain-by-domain initial observations

### Q12 — Work-life-class balance
Dominant construction: availability + time efficiency, like Course A. But richer qualifications:
- Several students name the trade-off explicitly: "helps me do homework faster… but it hinders the learning process at the same time" (T3_B_09)
- One student (T1_B_05) describes AI as *increasing* time on task because engaging deeply with it takes longer than shortcut approaches
- Metacognitive framing: "it really depends on how I use it and how well I already understand the concept" (T2_B_02)
- "Forced use" appears as a distinct concern (T2_B_03, T3_B_14): required AI use feels burdensome when student would rather work unaided

### Q13 — Most helpful features / improvements
Most helpful features identified (ordered by frequency):
- **Theorem/definition retrieval** — the course-distinctive feature, absent in Course A
- **Course-aligned content** — pulls from the book, matches class notation ("exactly like the professor's") — T1_B_11 is explicit: students disliked generic ChatGPT because "it would always try to teach me a different way that I wasn't taught in class"
- **Step-by-step problem breakdown** — shared with Course A but more specific here (e.g., MLE derivations)
- **Chapter-specific GPTs** — explicitly praised ("chapters curated for specific chapters," "the Stats gpt")
- **Hint-privileging / not giving full answer** — double-edged: praised when it works, complained about when it fails
- **Non-judgment / low-embarrassment help** — T3_B_09 explicit: "question I might feel too embarrassed to ask my actual professor"

Improvements identified:
- Don't give answer too quickly (recurring, prominent — this is *the* dominant improvement theme)
- Skips steps when doing derivations
- Doesn't always reference the correct question when asked
- Doesn't handle visual/diagram content well
- Occasional incorrectness in answers

### Q14 — Equity
Less diverse than Course A. Dominant response: yes, equal. Qualifications present but fewer:
- **Learning curve / prompting skill** — T1_B_11 "learning curve" and "seeing how my classmates worded questions"
- **ChatGPT premium access** — T1_B_13 and T3_B_07 mention premium as a past inequity, now resolved
- **Visual learners** — T2_B_12 notes AI "tends to struggle in this area"
- **Subject dependence** — T1_B_14 distinguishes math (AI helpful) from philosophy/essay writing (AI not useful)
- **English language** — T3_B_08 "I usually struggle with English and AI has helped"
- **Self-discipline / abuse of system** — T3_B_05: "others may not learn effectively because they can abuse the system"

### Q15 — Critical thinking / specific instance
Tone is noticeably more ambivalent than Course A. At T1, most responses describe net benefit; by T3, a distinct "AI tutor crutch" framing emerges:
- T3_B_07: "ai tutor crutch that I can use whenever I get stuck. Instead of genuinely thinking... skipping that critical thinking completely"
- T3_B_13: "sometimes feel like im offloading my memory to the AI"
- T3_B_02: "tool of reliance, where I may not think or need to think about how to solve the question anymore"

Counterposed to these are strong positive instances:
- T1_B_11: ability to ask "why" instead of memorizing — "nice to be able to remind myself why I am doing certain steps"
- T1_B_13: "if I get stuck I can ask for a hint and that will help get me unstuck"
- T3_B_12: arguing with the AI as a critical-thinking exercise
- T3_B_15: "Whenever i got stuck on how to give the likelihood for a function AI tutor would help me with what I should do next and give reasons as to why"

Concrete named instances include MLE derivation, likelihood functions, hypothesis testing, exam preparation, ANOVA — a rich set of discipline-specific examples.

### Q16 — Suggestions
Like Course A, many "none / no improvements." But substantive suggestions are more pedagogically sophisticated:
- Don't spit out answers (dominant — same as Course A)
- Build in Socratic questioning before giving answers (T2_B_07)
- Add visuals/diagrams (T2_B_12)
- Provide PDFs alongside AI access (T3_B_04)
- More frequent but shorter AI assignments (T3_B_01 — a concrete pedagogical design suggestion)
- Don't make it a requirement (T3_B_14 — links back to the "forced use" concern)
- Resolve reference-confusion issues where AI cites wrong question

---

## 3. Preliminary code candidates (to be formalized in Phase 2)

**Q12 Balance:**
- `benefit_time_efficiency`
- `benefit_availability`
- `benefit_theorem_recall` — retrieve specific theorems/definitions quickly (course-distinctive)
- `benefit_immediate_feedback`
- `benefit_low_embarrassment` — ask without judgment
- `benefit_absence_compensation`
- `concern_time_cost` — AI engagement takes longer than expected
- `concern_memory_retention` — weakens ability to recall without AI
- `concern_forced_use` — mandatory AI use is burdensome
- `trade_off_metacognitive` — explicit articulation of benefit/concern trade-off
- `nonsubstantive_response`

**Q13 Features:**
- `feature_theorem_lookup` — theorems, definitions, book references
- `feature_course_alignment` — notation and style matches class
- `feature_step_by_step` — stepwise problem breakdown
- `feature_chapter_specific_gpts`
- `feature_hint_privileging` — gives hints, withholds full answer
- `feature_low_embarrassment`
- `feature_practice_problem_generation`
- `improve_dont_give_answer` — dominant improvement theme
- `improve_skipped_steps` — skips algebra in derivations
- `improve_question_reference` — doesn't cite the right textbook question
- `improve_visual_support` — doesn't render diagrams well
- `improve_prompting_clarity` — student acknowledges prompt engineering skill gap
- `improve_accuracy_concern` — AI sometimes incorrect

**Q14 Equity:**
- `equity_yes_unconditional`
- `equity_conditional_prompting` — learning curve, prompting skill
- `equity_conditional_discipline` — works for math, not essays/philosophy
- `equity_conditional_self_discipline` — depends on whether student abuses the system
- `equity_concern_premium_access` — retrospective concern about ChatGPT premium (resolved)
- `equity_concern_visual_learners`
- `equity_concern_language`

**Q15 Critical thinking:**
- `crit_helps_why_questions` — explains why, not just how
- `crit_helps_theorem_connection` — connects problem to relevant theorems
- `crit_helps_step_reasoning`
- `crit_helps_argument_with_ai` — student argues with AI, both learn
- `crit_helps_practice_generation`
- `crit_hinders_crutch` — skipping genuine thinking
- `crit_hinders_memory_offloading` — offloading to AI weakens recall
- `crit_hinders_reassurance_dependence` — constant need for reassurance
- `crit_ambivalent` — explicitly both
- `crit_specific_instance` — extract-tagging meta-code

**Q16 Suggestions:**
- `suggest_none`
- `suggest_dont_spit_answer` — dominant substantive suggestion
- `suggest_socratic_opener` — AI should ask what student knows first
- `suggest_visuals`
- `suggest_pdf_alongside`
- `suggest_assignment_design` — frequency/size of assignments
- `suggest_not_required` — don't force use
- `suggest_reference_fix` — cite right textbook question

---

## 4. Boundary cases and coding-rule decisions

**Mathematical content in responses** — where students paste excerpts of their dialogue with the AI (e.g., T2_B_07), the substance is not the response *about* AI but a specimen of AI use. Code these as `crit_specific_instance` with additional tag `contains_ai_transcript_excerpt`, and treat the LaTeX portion as data for §4.3 / Appendix C rather than for thematic frequency counts.

**Metacognitive responses** — responses that articulate "it depends on how I use it" (e.g., T2_B_02) are distinctive to Course B. Code as `trade_off_metacognitive`. This may elevate to a theme by itself given its prominence.

**Critical-engagement-with-AI** — responses describing *arguing with* the AI (T2_B_10, T3_B_12) are distinct from responses describing the AI *helping* the student think. This is a fundamentally different posture toward the tool and may warrant a theme-level distinction: "AI as interlocutor" vs. "AI as source." Decision for Phase 3.

**Longitudinal divergence** — Course B T3 responses to Q15 show a clear shift toward articulating cognitive offloading concerns. This is worth reporting as a longitudinal pattern, potentially the most important qualitative finding for this course.

---

## 5. Questions held open for Phase 2–3

1. Should the "AI as interlocutor" posture (arguing, questioning, critical engagement) be elevated to its own theme in Course B, given it's distinctive and pedagogically meaningful? This is the most important theme-level decision to resolve.
2. Is "trade-off metacognitive" a theme in its own right or a cross-cutting pattern within each of the five domains?
3. The T3 emergence of "crutch" and "offloading" language — single theme or a cross-wave evolution to report?

---

## 6. Reflexivity note (specific to this course)

I taught Course B and know its students individually. I designed the SMARTS prompts and the chapter-specific GPTs for Course B. The T2_B_07 transcript excerpt shows a student pushing back on *my* review sheet notation — I read this with mixed feelings as both instructor and coder, and I want to explicitly flag that my first instinct was to code it as "accuracy concern about AI" rather than "student demonstrating critical thinking by questioning AI *and* the instructor." I will code it as the latter, which is what the data actually shows, and let that coding decision stand as an example of reflexivity-in-action.

In Course B my reflexivity risk is symmetrical to Course A: I am prone to over-interpret ambivalent responses as confirming SMARTS's hint-privileging design (because that's what I was trying to build), and I may underweight genuine critiques such as "forced use is burdensome" or "should not be required." Mitigation: same as Course A — every concern/limitation coded explicitly, parallel reporting of benefit/concern code frequencies.
