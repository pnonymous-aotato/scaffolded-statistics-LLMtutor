# Phase 1 Familiarization Memo — Course A (Course A, Introductory Statistics)

**Coder:** A. redacted (solo, reflexivity declared in §6.7)
**Corpus:** 189 substantive free-text responses (n = 14/12/13 students at T1/T2/T3, five essay questions per wave)
**Approach:** Hybrid inductive/deductive — deductive scaffolding from the five survey question domains, inductive codes generated within each domain.

---

## 1. First-read impressions

Course A responses are shorter on average than Course B, and the vocabulary reflects an introductory-statistics and general-education audience. Students frequently name specific course artifacts: R, RStudio, "r code," hypothesis testing, ANOVA, Duncan tests. A small number of responses (3 of 189 across the whole corpus) are either off-topic ("social media" alone), monosyllabic ("yes" / "no"), or non-substantive ("N/A"); these are retained in the data but coded as `nonsubstantive_response` rather than discarded, so the denominator is honest.

The *tone* of Course A is strongly positive and usage-focused. The typical Q12-balance response describes AI as a time-saving, anywhere-anytime help resource. By T3, responses become noticeably shorter and more affirmative — a handful of students explicitly say "it works great!" Responses rarely theorize about AI; they describe concrete instances of use.

Two distinctive patterns stood out on first read:
1. **Course-specificity of R help.** Students consistently name R coding help as the most valuable feature. The R tutor GPT (mentioned explicitly in several T3 responses — T3_A_01, T3_A_09, T3_A_10, T3_A_11) emerges as the most praised tool.
2. **Absence-compensation.** At least four students mention using AI to catch up after missing class for sport travel or illness (T1_A_09, T3_A_03). This is a concrete equity function not anticipated in the instrument design.

---

## 2. Domain-by-domain initial observations

### Q12 — Work-life-class balance
Dominant construction: time-efficiency + availability. Most students use "help" language; three students name specific hindrances (T1_A_13 "shortcut to learning," T2_A_10 "distraction if I rely too much," T3_A_13 "hindered" due to HSI-1 account not connected). By T3, responses are more compressed and more positive (e.g., T3_A_11 "helps me make plans and summarise bigger things").

### Q13 — Most helpful features / improvements
Most helpful feature: R code assistance (dominant — 8+ responses across waves). Step-by-step explanation is the second most praised feature. Course-aligned content mentioned several times ("the professors guidelines and the materials he uses," "class specific"). Improvements identified: don't give answer immediately, improve loading speed, enable image-link sharing, limit scope/relevance.

### Q14 — Equity / accommodates all students equally
Dominant response: yes, equal. Three distinct qualifications emerge:
- **Dependent on student effort/input** ("gives you whatever you put into it")
- **Dependent on prompting skill** (explicit at T3 — "if you are taught how to use/prompt the tool")
- **Accessibility gaps** (vision impairment, English language)

Notable evolution across waves: T1 responses are almost universally "yes equal"; by T3, at least two students (T3_A_09, T3_A_10) articulate a conditional view that equality depends on teaching students how to prompt. This is an interesting longitudinal pattern.

### Q15 — Critical thinking / specific instance
Responses split three ways:
- **Helped critical thinking** via step-by-step visualization, concept reinforcement, mock exams
- **Hindered critical thinking** via over-reliance, cognitive shortcut, memorization concerns
- **Ambivalent** — both helped and hindered, typically with a balance concern

Specific named instances include: mock exam generation (T1_A_06), ANOVA/Duncan project (T3_A_04), formula recall (T1_A_13), R code debugging (T1_A_08). These concrete examples are high-value extracts.

### Q16 — Suggestions
Most responses at all waves are "none / works great" (~60% of responses). Substantive suggestions fall into three areas:
- Scope control (limit to what's relevant)
- Technical fixes (image saving, load speed, HSI-1 account connection)
- Deployment (standardize across classes; keep consistent)

---

## 3. Preliminary code candidates (to be formalized in Phase 2)

I'll use these as a starting set and refine during systematic coding:

**Q12 Balance:**
- `benefit_time_efficiency` — AI saves time on homework/study
- `benefit_availability` — accessible anytime, outside class hours
- `benefit_language_accessibility` — simpler explanations, language support
- `benefit_absence_compensation` — catches up after missed class
- `concern_cognitive_shortcut` — replaces rather than supports learning
- `concern_over_reliance` — weakens independent problem-solving
- `nonsubstantive_response` — "yes," "N/A," off-topic

**Q13 Features:**
- `feature_r_code_help` — R tutor, syntax, RStudio
- `feature_step_by_step` — stepwise breakdown of problems
- `feature_course_alignment` — matches professor's materials/style
- `feature_multiple_approaches` — several ways to understand same problem
- `feature_chapter_specific_gpts` — specific GPTs over general
- `improve_scope_relevance` — don't go beyond course scope
- `improve_verification` — AI sometimes wrong; need to double-check
- `improve_technical` — load speed, image handling, account integration

**Q14 Equity:**
- `equity_yes_unconditional` — accommodates all equally
- `equity_conditional_on_effort` — depends on student input
- `equity_conditional_on_prompting` — depends on prompting skill
- `equity_concern_accessibility` — vision, internet access
- `equity_concern_language` — English-as-second-language barrier
- `equity_concern_instructor_guidance` — depends on instructor teaching how to use

**Q15 Critical thinking:**
- `crit_helps_step_reasoning` — walks through reasoning, visualizes steps
- `crit_helps_concept_recall` — reinforces forgotten concepts
- `crit_helps_independent_practice` — generates practice problems
- `crit_hinders_over_reliance` — crutch, skips genuine thinking
- `crit_hinders_copy_paste` — verbatim copying weakens understanding
- `crit_ambivalent` — both helped and hindered
- `crit_specific_instance` — named concrete use (this is a meta-code for extract-tagging)

**Q16 Suggestions:**
- `suggest_none` — no suggestions / works great
- `suggest_scope_relevance` — keep output relevant / limit scope
- `suggest_technical` — specific technical improvements
- `suggest_deployment` — standardization / more use / different integration

---

## 4. Boundary cases and coding-rule decisions

**Ambivalent responses** (e.g., T3_A_06: "helped hinder my ability to manage and succeed") — code with BOTH the benefit and concern codes; note ambivalence as a structural theme rather than forcing a binary.

**Non-substantive responses** — kept in denominator but coded `nonsubstantive_response`. Reporting convention in §7.3: report "n of [total] respondents provided substantive responses to this item."

**Off-topic responses** (T1_A_05 Q12: "social media") — coded `nonsubstantive_response` but quoted noted-where-relevant. These may reflect student confusion about the prompt rather than genuine position.

**Double-coding** — a single response can receive multiple codes. This is standard Braun & Clarke practice; codebook will track code co-occurrence for the §7.3 report.

---

## 5. Questions held open for Phase 2–3

1. Should "equity_conditional_on_prompting" and "equity_concern_instructor_guidance" be merged into a single theme about prompting-skill-as-equity-issue? Probably yes based on first read.
2. "Benefit_absence_compensation" appeared spontaneously in enough responses to warrant a code, but it may cluster under benefit_availability at theme level.
3. Longitudinal patterns worth tracking explicitly: Does conditional-equity framing emerge only by T3? Does "works great" compression at T3 reflect satisfaction or survey fatigue? Report these cautiously.

---

## 6. Reflexivity note (specific to this course)

I designed SMARTS and the R-tutor GPT, and I taught both sections of Course A in spring 2025. This creates both an advantage — I recognize when students are describing specific tools (the R tutor GPT mentioned by name, the chapter-specific GPTs praised at T2 and T3) — and a risk: I may over-code positive responses as "confirming SMARTS" and miss critiques that reframe what I'd otherwise read as praise. To mitigate, I will explicitly tag every response that contains a concern or limitation (not just net-positive responses) and report code frequencies symmetrically (benefit codes and concern codes reported in parallel columns).
