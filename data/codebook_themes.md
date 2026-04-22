# Phase 3–5 Codebook: Thematic Analysis of Open-Ended Survey Responses

**Courses:** Course A (Course A, Introductory Statistics) and Course B (Course B, Advanced Mathematical Statistics), HSI-1 Spring 2025
**Data:** 428 substantive free-text responses across 5 prompts × 3 waves × 2 courses
**Approach:** Hybrid inductive/deductive thematic analysis following Braun & Clarke (2006). Deductive scaffolding from the five survey question domains (Q12 balance, Q13 features/improvements, Q14 equity, Q15 critical thinking, Q16 suggestions), with inductive codes generated within each domain.
**Separate analyses per course.** Themes from Course A and Course B are not merged; patterns are reported side-by-side with explicit noting of similarities and divergences.
**Coder:** A. redacted (solo, reflexivity declared in §6.7).

---

## Part 1 — Course A (Course A) Themes

### Theme A1: Time-efficient, on-demand scaffolding
*Dominant benefit frame; appears across all five domains*

**Included codes**: `benefit_time_efficiency` (7 mentions), `benefit_availability` (8), `benefit_understanding_scaffold` (14), `benefit_absence_compensation` (4), `feature_step_by_step` (8), `crit_helps_step_reasoning` (9), `crit_helps_independent_practice` (7)

**Definition.** Students describe the AI assistant primarily as an on-demand scaffolding resource that compresses time-to-understanding. The theme captures the assistant's role as a 24/7 available tutor that breaks concepts into manageable steps, supports students in reviewing content after missed class sessions, and enables repeated practice without social friction. Unlike traditional tutoring, the assistant is immediately accessible; unlike lecture, it is responsive to specific student questions.

**Concrete instances.** Sport travel absence (T1_A_09), illness catch-up (T3_A_03), step-by-step debugging of R code (T1_A_08), formula recall during individual project (T1_A_13), generating mock exam questions (T1_A_06, T3_A_06), ANOVA and Duncan tests for group project (T3_A_04).

**Wave pattern.** Most stable theme across waves. Consistent saliency at T1/T2/T3. No evolution detected.

---

### Theme A2: R code assistance as the distinctive course-level affordance
*Course-specific, rises to prominence by T3*

**Included codes**: `feature_r_code` (11), `feature_course_alignment` (6), `feature_chapter_specific_gpts` (3), `benefit_r_code` (2)

**Definition.** For Course A students, the AI assistant's most-praised function is R coding help, made possible by the course-aligned R-tutor Custom GPT restricted to the `mosaic` and `BSDA` packages. The theme differs from Theme A1 in specificity: where A1 describes generic scaffolding, A2 captures students' recognition that this particular tool works *because* it aligns to their course's specific computational stack and the instructor's teaching conventions. References to "the R tutor" become more explicit and more frequent at T3.

**Concrete instances.** "The R tutor explanations are effective" (T3_A_09), "the R studio and hypothesis testing features were great and the same exact thing as what we learned in class" (T3_A_03), "the R script tutor was the most helpful with reminding me for r codes" (T3_A_10).

**Wave pattern.** Clear emergence pattern. At T1, students mention R help generically; by T3, students name "the R tutor" as the specific artifact, reflecting consolidation of the tool's identity in student use over the semester.

---

### Theme A3: Equity as near-universal but prompting-conditional
*Distinctive longitudinal shift from unconditional to conditional equity*

**Included codes**: `equity_yes_unconditional` (29), `equity_conditional_prompting` (7), `equity_concern_instructor_guidance` (2), `equity_conditional_effort` (1), `equity_concern_accessibility` (1), `equity_concern_language` (1)

**Definition.** Course A students overwhelmingly affirm that the AI assistant accommodates students equally — at the level of access and availability. However, a minority articulate a more sophisticated conditional view: that *realized* equity depends on students' prompting skill, which in turn depends on the instructor's explicit teaching of prompt engineering.

**Concrete instances.** "I personally think that it accommodates for all students equally because if you ask it to do a specific thing then it will most likely do that for you" (T1_A_09, unconditional). "I do not think AI accommodates the needs of all students equally; I think a student's effectiveness at utilizing prompts determines the quality of a student's experience with AI" (T3_A_09, conditional).

**Wave pattern.** Most notable longitudinal pattern in Course A qualitative data. At T1, 10 of 14 equity responses are unconditional; at T3, the conditional framing appears in 3 of 13. While small in absolute numbers, this is a substantive shift in qualitative framing — students who have spent a semester using the tool articulate a more skill-mediated view of equity than students at baseline.

**Theme-level interpretive claim.** The longitudinal shift is consistent with the paper's argument that prompt engineering (the F-R-A-M-E discipline) is a *learnable* equity lever. At baseline students assume tool access implies equitable use; by end of semester some students recognize that tool access without prompting instruction under-serves equity.

---

### Theme A4: Critical thinking trade-off
*Ambivalent, both-helped-and-hindered framing*

**Included codes**: `crit_helps_step_reasoning` (9), `crit_helps_independent_practice` (7), `crit_hinders_over_reliance` (3), `crit_hinders_cognitive_shortcut` (2), `crit_hinders_copy_paste` (1), `crit_ambivalent` (3), `concern_cognitive_shortcut` (2), `concern_over_reliance_ack` (2)

**Definition.** A subset of Course A students articulate the AI assistant's impact on critical thinking as a structural trade-off: the same scaffolding that helps at the point of confusion can, if used indiscriminately, short-circuit the effortful struggle that constitutes learning. Students who articulate this trade-off frame themselves as active managers of the tool rather than passive consumers.

**Concrete instances.** "I use it as a tool to help me do my work not have it [do] it for me" (T1_A_09, explicit self-management). "AI ends up being a shortcut to learning the material, which I think ends up hurting the student more than helping them actually understand the material" (T1_A_13, pure concern). "At times I would find myself leaning on AI too much; if I needed to solve a problem for a test, I would find myself lacking the critical thinking needed to tackle certain problems" (T3_A_09, late-wave self-awareness).

**Wave pattern.** Positive framings dominate at T1 and T2; ambivalent and concern framings appear more frequently at T3. Students develop critical distance from the tool over the semester.

---

### Theme A5: Suggestions concentrated on constraint design
*Most responses want more constraint, not less*

**Included codes**: `suggest_none` (29), `suggest_scope_relevance` (2), `suggest_iteration` (2), `suggest_accuracy` (1), `suggest_consistency` (1), `suggest_deployment_standardization` (1)

**Definition.** The clear majority of Course A suggestion-item responses are "none / works great." Among students who do offer substantive suggestions, the common thread is a desire for more constraint (keep output relevant, limit scope, improve accuracy, standardize deployment) rather than less. No students suggested fewer restrictions except one T1 response (T1_A_04: "remove limits/regulations").

**Wave pattern.** Pattern holds across all waves.

---

## Part 2 — Course B (Course B) Themes

### Theme B1: On-demand theorem and definition retrieval
*Course-distinctive frame; absent in Course A*

**Included codes**: `benefit_theorem_recall` (4), `feature_theorem_lookup` (3), `feature_definitions` (3), `benefit_concept_recall` (1), `feature_chapter_reference` (2)

**Definition.** Students in the advanced mathematical statistics course describe a distinctive use case absent from introductory responses: using the AI assistant as a rapid theorem-and-definition retrieval system, particularly for problem-solving contexts where the relevant theorem is known by name but not immediately recalled in full form. This theme captures the substitution of AI-mediated lookup for textbook page-flipping during problem-solving.

**Concrete instances.** "AI tools such as ChatGPT reduce time for me flipping through my textbook looking for the certain theorems and definition that I need to solve a problem" (T3_B_13, explicit comparison to textbook use). "AI tools help me do my homework a lot faster because I don't have to search all my notes to look for theorems or formulas" (T3_B_10).

**Wave pattern.** Stable across waves; most strongly articulated at T3 when students have accumulated enough course material that theorem retrieval becomes a frequent need.

---

### Theme B2: Course-aligned instruction as the critical affordance
*The discriminator between useful and unhelpful AI*

**Included codes**: `feature_course_alignment` (10), `improve_course_explanations` (1), `concern_course_alignment` (2)

**Definition.** Course B students repeatedly identify course-alignment — the AI assistant's use of the professor's notation, the textbook's definitions, and the lecture's worked-example conventions — as the feature that makes the tool pedagogically useful rather than confusing. The theme is expressed most clearly in contrast: generic ChatGPT is dispreferred; the course-aligned Custom GPT is preferred.

**Concrete instances.** "I didn't like using AI before because it seemed like it would always try to teach me a different way that I wasn't taught in class and I would end up more confused" (T1_B_11, explicit contrast). "The most helpful thing about the AI tutor was that the teaching style and notation was exactly like the professor's" (T3_B_12). "One of the features that I found most helpful is that it searches and pulls information directly from the book and class notes. I find this very helpful because there is less of a chance to receive an explanation that differs from what we are learning in class" (T1_B_05).

**Wave pattern.** Consistent across waves. This is the course's defining affordance.

---

### Theme B3: Hint-privileging interaction style as central design concern
*Most-frequent improvement request; contested execution*

**Included codes**: `improve_dont_give_answer` (6 in Q13 + 6 in Q16), `feature_hint_privileging` (3), `improve_skipped_steps` (3), `crit_helps_hint_privileging` (3), `crit_hinders_gives_answer` (2), `improve_socratic_questioning` (1), `suggest_socratic_opener` (1), `suggest_dont_spit_answer` (many)

**Definition.** The most frequently articulated improvement request across both the features question (Q13) and the suggestions question (Q16) concerns the AI's tendency to give full answers when students want hints. When the hint-privileging mechanism works as intended, students praise it as critical-thinking scaffolding; when it fails (e.g., the AI gives the full answer after two clarification turns), students criticize it. Several students explicitly appreciate when the professor "fixed" the system prompt to reduce answer-giving.

**Concrete instances.** "I found the AI's abilities to only provide small hints and partial steps really useful in helping me learn" (T3_B_07, working as intended). "At the beginning it would just give the answers but once the professor fixed it has helped me think more about the problems" (T2_B_09, system-prompt iteration noted). "I found it most help that I could... think out loud to the AI tutor and it will correct where my thought process might have gone wrong. I think a feature that needs improvement is not giving into the answer too quickly because you can ask it to not give you the answer, but after about two more chats expressing confusion, the AI tutor gives the full answer" (T3_B_09, mixed).

**Theme-level interpretive claim.** This theme directly substantiates the paper's argument that refusal-and-escalation mechanisms are central to the SMARTS design. Students *recognize* the mechanism, value it when working, and request its strengthening when it fails. This is evidence that the hint-privileging protocol is operating as a visible pedagogical contract rather than invisible infrastructure.

**Wave pattern.** Consistent across waves; most articulated at T2 and T3 when students have accumulated enough interaction to notice patterns.

---

### Theme B4: Critical engagement with AI as cognitive work
*Course-distinctive advanced-level pattern*

**Included codes**: `crit_helps_argument_with_ai` (1, T3_B_12), `improve_accuracy_concern` (2), `crit_helps_why_questions` (2), `crit_helps_error_diagnosis` (2), `crit_helps_comparison` (1), `crit_helps_theorem_connection` (1), specimen excerpt T2_B_07 and T2_B_10

**Definition.** A subset of Course B students describe arguing with, questioning, or critically evaluating the AI's output as a cognitive exercise in its own right. This posture is *distinct* from Theme A4's critical-thinking trade-off: in A4, students worry that the tool displaces thinking; in B4, students describe using the tool to sharpen thinking by contesting its claims. The extended transcript excerpt at T2_B_07 (where a student explicitly works through a variance computation and catches the AI's apparent inconsistency with the instructor's review sheet) and T2_B_10 (where a student argues with the AI, fails to get a satisfactory explanation, and goes to the instructor) are the clearest exemplars.

**Concrete instances.** "It has really helped me think critically. There have been many times where I have questioned its results and had to argue with it" (T3_B_12). "I came across a question with the last version that the bot could answer because it had the solution but it could not explain the solution to me. After arguing with it, I gave up and asked Dr. Y and he was able to explain" (T2_B_10, extended instance where critical engagement hits a limit).

**Theme-level interpretive claim.** The theme is significant because it instantiates a pedagogical goal (students as critical evaluators of AI output) without requiring explicit scaffolding — the behavior emerges from the combination of an advanced-subject-matter course and a course-aligned but fallible tool. The theme is rare in the corpus (five or six students) but consistent in pattern.

**Wave pattern.** Appears at all three waves in Course B, not detected at all in Course A. This is the cleanest course-level difference in the qualitative data.

---

### Theme B5: Ambivalence about memory and cognitive offloading
*Longitudinal theme; emerges by T3*

**Included codes**: `concern_memory_retention` (2), `crit_hinders_memory_retention` (1), `crit_hinders_memory_offloading` (1), `crit_hinders_crutch` (1), `crit_hinders_reliance_tool` (1), `crit_hinders_reassurance` (1), `trade_off_metacognitive` (4)

**Definition.** By end of semester, a distinct cluster of Course B students articulate that AI use has materially weakened their ability to recall course material without AI assistance. Unlike Theme A4's general concern about over-reliance, Course B students name specific losses: memory for formulas, confidence in solving without reassurance, and what one student calls "offloading my memory to the AI." This theme is notably absent at T1 and becomes prominent by T3.

**Concrete instances.** "I have a very busy life so using the AI does help me get through the lessons... However, as it is helping me recall what I would need to know in order to complete the assignment, I do feel like my memory retention for courses has been impacted greatly... I am unable to recall formulas and theorem with ease" (T1_B_10, early articulation). "I do feel that overtime it definitely has hindered my ability to think critically because there is an ai tutor crutch that I can use whenever I get stuck" (T3_B_07). "Sometimes feel like im offloading my memory to the AI and rely on it. This hinders my learning because im overly relying on it for guidance and too lazy to put actual practice and test my mind" (T3_B_13).

**Wave pattern.** Most important longitudinal finding in Course B. Rarely articulated at T1; appears more explicitly at T2; most developed at T3.

**Theme-level interpretive claim.** This theme is consistent with the external evidence summarized in the manuscript's §2 (Lee et al. 2025 on confidence-in-AI ↔ reduced critical thinking; Gerlich 2025 on cognitive offloading). The fact that advanced-statistics students independently articulate the same concern adds qualitative evidence to the quantitative literature.

---

### Theme B6: Equity as effectively universal with low-salience qualifications
*Different from Course A: fewer conditional qualifications*

**Included codes**: `equity_yes_unconditional` (31), `equity_conditional_prompting` (4), `equity_language_support` (4), `equity_access_through_campus` (3), `equity_cannot_speak_for_others` (2), `equity_conditional_discipline` (2), others rare

**Definition.** Course B students overwhelmingly view the AI assistant as equitable. Qualifications exist but are less prominent than in Course A: prompting skill appears as an issue but fewer students elevate it to an equity claim; language support is named by several students as a concrete benefit rather than a gap; the ChatGPT-premium access concern appears and then resolves during the semester; subject-level limitations (works for math but not essays) are noted.

**Wave pattern.** Stable across waves; less longitudinal evolution than Course A's equity theme.

**Theme-level interpretive claim.** The contrast with Course A's Theme A3 is worth noting. Course A students, who come from more heterogeneous academic backgrounds, articulate a sharper equity-as-prompting-skill concern; Course B students, who are mostly mathematics majors with stronger prior preparation, articulate equity concerns less sharply. This is consistent with the broader literature (Rao et al. 2026, Krupp et al. 2024) that unstructured AI benefits students with strong foundations disproportionately.

---

### Theme B7: Sophisticated suggestion-making
*Distinctive suggestion patterns — pedagogical design-level thinking*

**Included codes**: `suggest_assignment_per_topic`, `suggest_textbook_integration`, `suggest_class_notes`, `suggest_practice_exam`, `suggest_assignment_design`, `suggest_socratic_opener`, `suggest_pdf_alongside`, `suggest_class_notes_integration`, `suggest_reference_fix` (3), `suggest_not_required`, `suggest_visuals`, `suggest_dont_skip_steps`

**Definition.** While the majority of Course B suggestion responses are "none," the substantive suggestions that do appear are notably more pedagogically sophisticated than in Course A. Course B students propose specific assignment-design modifications (frequency, size, format), integration with course artifacts (class notes, PDFs, textbook), and design-level features (Socratic opener, visual support, reference accuracy). Several responses read like instructional-design recommendations rather than user feedback.

**Concrete instances.** "Before I get to that though, I do want to say that I personally believe that AI tutoring is and will be extremely beneficial... Improvements: Access to the whole textbook and being able to scan the whole textbook. Educators input all notes and in class examples..." (T1_B_03, extended multi-item design critique). "It would be helpful if there were more assignments with tutor assistance but less questions on each assignment. Ex: Having 10 AI assisted assignments throughout the course 1 every friday except the first week, last week, or test weeks with about 3-4 questions each assignment in order for students to keep that familiarity" (T3_B_01, detailed pedagogical proposal).

**Wave pattern.** Similar pattern at all waves; sophistication appears from T1 onward, reflecting the advanced-course student population.

---

## Part 3 — Cross-course comparison (for Discussion, not Results)

The seven Course B themes and five Course A themes are not derived from a joint analysis, per the user's instruction to conduct separate thematic analyses. However, patterns that recur across both courses can be noted for Discussion:

- **Time-efficiency/scaffolding** (Theme A1 and B1+B2 jointly): shared across courses; the benefit mechanism is similar but the *content* of what is scaffolded differs (R code in A, theorems/derivations in B)
- **Hint-privileging** (Theme B3): present as a specific concern only in Course B; barely surfaces in Course A
- **Critical-thinking trade-off** (Theme A4 and Theme B5): both courses articulate over-reliance concerns; Course B students articulate them in more cognitively specific terms (memory offloading, formula recall loss)
- **Equity** (Theme A3 and Theme B6): both converge on "yes unconditional" as the modal response; Course A shows more longitudinal shift toward prompting-conditional framing
- **Critical engagement with AI** (Theme B4): course-distinctive to Course B; the mathematical-proof content of advanced statistics creates conditions for arguing with the AI that are absent in introductory statistics

## Part 4 — Code-to-theme mapping (Master Codebook)

### Course A (189 responses, 38 coded units per wave aggregated across 5 questions)

| Theme | Codes included | Total code instances |
|---|---|---|
| A1 Time-efficient scaffolding | benefit_time_efficiency; benefit_availability; benefit_understanding_scaffold; benefit_absence_compensation; feature_step_by_step; crit_helps_step_reasoning; crit_helps_independent_practice | ~57 |
| A2 R code assistance, course-aligned | feature_r_code; feature_course_alignment; feature_chapter_specific_gpts; benefit_r_code | ~22 |
| A3 Equity: unconditional vs prompting-conditional | equity_yes_unconditional; equity_conditional_prompting; equity_concern_instructor_guidance; equity_conditional_effort; equity_concern_accessibility; equity_concern_language | ~41 |
| A4 Critical-thinking trade-off | crit_hinders_over_reliance; crit_hinders_cognitive_shortcut; crit_hinders_copy_paste; crit_ambivalent; concern_cognitive_shortcut; concern_over_reliance_ack | ~13 |
| A5 Suggestions: constraint, not freedom | suggest_none; suggest_scope_relevance; suggest_iteration; suggest_accuracy; suggest_consistency; suggest_deployment_standardization | ~36 |

### Course B (239 responses, 48 coded units per wave aggregated across 5 questions)

| Theme | Codes included | Total code instances |
|---|---|---|
| B1 On-demand theorem/definition retrieval | benefit_theorem_recall; feature_theorem_lookup; feature_definitions; benefit_concept_recall; feature_chapter_reference | ~13 |
| B2 Course-aligned instruction as critical affordance | feature_course_alignment; improve_course_explanations; concern_course_alignment | ~13 |
| B3 Hint-privileging interaction style | improve_dont_give_answer; feature_hint_privileging; improve_skipped_steps; crit_helps_hint_privileging; crit_hinders_gives_answer; improve_socratic_questioning; suggest_socratic_opener; suggest_dont_spit_answer | ~25 |
| B4 Critical engagement with AI as cognitive work | crit_helps_argument_with_ai; improve_accuracy_concern; crit_helps_why_questions; crit_helps_error_diagnosis; crit_helps_comparison; crit_helps_theorem_connection | ~9 |
| B5 Memory and cognitive offloading ambivalence | concern_memory_retention; crit_hinders_memory_retention; crit_hinders_memory_offloading; crit_hinders_crutch; crit_hinders_reliance_tool; crit_hinders_reassurance; trade_off_metacognitive | ~11 |
| B6 Equity as effectively universal | equity_yes_unconditional; equity_conditional_prompting; equity_language_support; equity_access_through_campus; equity_cannot_speak_for_others; equity_conditional_discipline | ~46 |
| B7 Sophisticated suggestion-making | suggest_assignment_per_topic; suggest_textbook_integration; suggest_class_notes; suggest_practice_exam; suggest_assignment_design; suggest_socratic_opener; suggest_pdf_alongside; suggest_reference_fix | ~15 |

---

## Part 5 — Reflexivity notes

As documented in §6.7, the coding was conducted by the instructor of both courses. Throughout coding, I was alert to two specific risks:

1. **Over-coding positive responses as confirming SMARTS.** Mitigated by explicit parallel coding of concern/limitation expressions, which surfaced Theme A4, Theme B3 (the critical part), and Theme B5 — all of which contain substantial critical material.

2. **Under-coding legitimate critiques that challenge my design commitments.** The clearest example was T2_B_07 (a long transcript where the student appears to catch the AI apparently inconsistent with *my* review sheet). My first instinct was to code this as "AI accuracy concern"; on reflection I recognized that the student was demonstrating critical thinking by questioning both the AI *and* my own materials. I coded it under Theme B4 (critical engagement with AI) rather than under the improvement code, and I note the recoding decision here as transparent evidence of reflexive adjustment.

A secondary note: the corpus contains several responses where students praise the R tutor (Course A) or the chapter-specific GPTs (Course B) by name. Because I designed those tools, I am predisposed to read those as evidence of design success. They appear in the codebook as face-value evidence but should be interpreted by readers with that coder position in mind.
