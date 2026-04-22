#!/usr/bin/env python3
"""
Phase 2 coding: Course B thematic coding.
Systematic hand-coding pass, separate from Course A.
"""

import csv

CODED = [
    # ======================================================================
    # Q12_balance
    # ======================================================================
    # T1 (n=17)
    ("T1_B_01", "Q12_balance", ["benefit_understanding_scaffold", "benefit_specific_domain_coding"], "coding in work too, laying out bases"),
    ("T1_B_02", "Q12_balance", ["benefit_time_efficiency", "future_framing"], "'frontier of the future' language"),
    ("T1_B_03", "Q12_balance", ["benefit_availability"], "tutoring centers have limited hours"),
    ("T1_B_04", "Q12_balance", ["benefit_understanding_scaffold"], "explains complex terms"),
    ("T1_B_05", "Q12_balance", ["benefit_understanding_scaffold", "concern_time_cost"], "deeper understanding but longer assignment time"),
    ("T1_B_06", "Q12_balance", ["benefit_understanding_scaffold", "concern_getting_answers"], "difficult to learn without getting answers"),
    ("T1_B_07", "Q12_balance", ["benefit_time_efficiency", "benefit_verification", "benefit_immediate_feedback"], "confirm answers + practice + instant feedback"),
    ("T1_B_08", "Q12_balance", ["benefit_time_efficiency", "benefit_availability"], "online tutor almost as helpful as instructor"),
    ("T1_B_09", "Q12_balance", ["benefit_understanding_scaffold", "trade_off_metacognitive", "concern_responsible_use"], "starting ideas but 'learn how to use responsibly' — not homework answer generator"),
    ("T1_B_10", "Q12_balance", ["trade_off_metacognitive", "concern_memory_retention", "benefit_understanding_scaffold"], "explicit ambivalence — memory retention impacted"),
    ("T1_B_11", "Q12_balance", ["benefit_immediate_feedback", "benefit_course_alignment"], "prefers asking Qs; feedback like class"),
    ("T1_B_12", "Q12_balance", ["benefit_theorem_recall"], "formulas faster than searching"),
    ("T1_B_13", "Q12_balance", ["benefit_understanding_scaffold", "improve_skipped_steps"], "helps steps but skips simple algebra"),
    ("T1_B_14", "Q12_balance", ["benefit_independent_practice", "benefit_time_efficiency"], "exam/midterm practice"),
    ("T1_B_15", "Q12_balance", ["benefit_summarize_other_classes"], "summarizes readings for other classes"),
    ("T1_B_16", "Q12_balance", ["benefit_availability", "benefit_understanding_scaffold"], "step by step anytime"),
    ("T1_B_17", "Q12_balance", ["benefit_time_efficiency", "benefit_understanding_scaffold"], "quicker, rephrase or detail"),
    # T2 (n=14)
    ("T2_B_01", "Q12_balance", ["benefit_availability", "benefit_time_efficiency"], "ease of access"),
    ("T2_B_02", "Q12_balance", ["trade_off_metacognitive"], "'depends on how I use it' — explicit metacognition"),
    ("T2_B_03", "Q12_balance", ["concern_forced_use"], "should be optional, not required"),
    ("T2_B_04", "Q12_balance", ["benefit_time_efficiency"], "minimize setup time"),
    ("T2_B_05", "Q12_balance", ["benefit_time_efficiency"], "homework faster"),
    ("T2_B_06", "Q12_balance", ["benefit_absence_compensation", "feature_chapter_specific_gpts"], "catch up; chapter-specific praised"),
    ("T2_B_07", "Q12_balance", ["benefit_availability"], "always available vs. in-person"),
    ("T2_B_08", "Q12_balance", ["benefit_memory_roadblocks"], "past roadblocks in memory"),
    ("T2_B_09", "Q12_balance", ["benefit_understanding_scaffold"], "explains complex topics simply"),
    ("T2_B_10", "Q12_balance", ["benefit_availability"], "outside office hours, late night"),
    ("T2_B_11", "Q12_balance", ["benefit_time_efficiency"], "less stressful, faster"),
    ("T2_B_12", "Q12_balance", ["benefit_immediate_feedback"], ""),
    ("T2_B_13", "Q12_balance", ["benefit_absence_compensation"], "missed lectures"),
    ("T2_B_14", "Q12_balance", ["benefit_concept_recall", "benefit_time_efficiency"], ""),
    # T3 (n=17)
    ("T3_B_01", "Q12_balance", ["benefit_availability"], "accessible any time"),
    ("T3_B_02", "Q12_balance", ["benefit_multiple_approaches"], "different methods"),
    ("T3_B_03", "Q12_balance", ["benefit_time_efficiency"], "brief"),
    ("T3_B_04", "Q12_balance", ["benefit_generic"], "'makes things easier'"),
    ("T3_B_05", "Q12_balance", ["benefit_immediate_feedback", "benefit_independent_practice"], "tutor-like"),
    ("T3_B_06", "Q12_balance", ["benefit_availability"], "convenience + accuracy"),
    ("T3_B_07", "Q12_balance", ["benefit_step_by_step", "trade_off_metacognitive", "concern_independent_thinking"], "long, explicit ambivalence — hinders own thinking"),
    ("T3_B_08", "Q12_balance", ["benefit_understanding_scaffold"], "explains complex subjects"),
    ("T3_B_09", "Q12_balance", ["trade_off_metacognitive", "concern_learning_vs_completion"], "faster completion vs. real learning"),
    ("T3_B_10", "Q12_balance", ["benefit_theorem_recall"], "theorems/formulas without notes"),
    ("T3_B_11", "Q12_balance", ["benefit_theorem_recall"], "definitions, formulas, symbols"),
    ("T3_B_12", "Q12_balance", ["benefit_generic"], "'extremely helpful with difficult schedule'"),
    ("T3_B_13", "Q12_balance", ["benefit_theorem_recall", "benefit_time_efficiency"], "reduce textbook search time"),
    ("T3_B_14", "Q12_balance", ["concern_forced_use"], "'when forced to use AI... too much time'"),
    ("T3_B_15", "Q12_balance", ["benefit_time_efficiency", "benefit_ideation"], "time crunch, research ideas"),
    ("T3_B_16", "Q12_balance", ["benefit_time_efficiency", "benefit_independent_practice"], "cut study time"),
    ("T3_B_17", "Q12_balance", ["benefit_availability"], "always available"),

    # ======================================================================
    # Q13_features
    # ======================================================================
    # T1
    ("T1_B_01", "Q13_features", ["nonsubstantive_response"], "N/A"),
    ("T1_B_02", "Q13_features", ["improve_prompting_clarity"], "prompts don't generate clear answers"),
    ("T1_B_03", "Q13_features", ["feature_course_alignment", "improve_dont_give_answer", "improve_prompting_clarity"], "knows material; needs hint-privileging"),
    ("T1_B_04", "Q13_features", ["feature_theorem_lookup", "improve_notation"], "definitions and theorems; variable notation"),
    ("T1_B_05", "Q13_features", ["feature_course_alignment", "improve_dont_give_answer"], "pulls from book; show steps not answer"),
    ("T1_B_06", "Q13_features", ["feature_course_alignment"], "Stats gpt work done as in class"),
    ("T1_B_07", "Q13_features", ["feature_verification", "improve_accuracy_concern"], "instant answers/hints; AI sometimes incorrect"),
    ("T1_B_08", "Q13_features", ["feature_step_by_step", "improve_dont_give_answer"], "step-by-step; full solution if not specific"),
    ("T1_B_09", "Q13_features", ["feature_low_prompting_burden"], "understands minimal context"),
    ("T1_B_10", "Q13_features", ["feature_prior_knowledge_surfacing", "feature_step_by_step"], "what prior knowledge, similar example problems"),
    ("T1_B_11", "Q13_features", ["feature_course_alignment", "improve_dont_give_answer"], "feedback like book/lectures; copy-paste auto-solves"),
    ("T1_B_12", "Q13_features", ["feature_step_by_step", "feature_hint_privileging"], "steps without final answer"),
    ("T1_B_13", "Q13_features", ["feature_definitions", "improve_skipped_steps", "improve_prompting_clarity"], "good definitions; skips steps; prompt engineering"),
    ("T1_B_14", "Q13_features", ["feature_practice_generation"], "exam 1 prep, similar problems"),
    ("T1_B_15", "Q13_features", ["feature_summarize_notes"], "summarize; break down"),
    ("T1_B_16", "Q13_features", ["feature_step_by_step"], "break down step by step"),
    ("T1_B_17", "Q13_features", ["feature_conversational", "feature_definitions"], "conversational, explains not just answers"),
    # T2
    ("T2_B_01", "Q13_features", ["feature_clarity", "feature_conversational"], "well-formatted; ask for clarification"),
    ("T2_B_02", "Q13_features", ["feature_low_embarrassment"], "no judgment, clear doubts"),
    ("T2_B_03", "Q13_features", ["feature_step_by_step", "feature_course_alignment"], "pulls notes from book"),
    ("T2_B_04", "Q13_features", ["feature_practice_generation"], "replicates questions with different scenarios"),
    ("T2_B_05", "Q13_features", ["feature_step_by_step"], "simple to follow"),
    ("T2_B_06", "Q13_features", ["concern_course_alignment"], "low confidence tutor explains like professor"),
    ("T2_B_07", "Q13_features", ["feature_step_by_step", "improve_accuracy_concern", "contains_ai_transcript_excerpt"], "long response with LaTeX; AI gets stuck without full answer — contains specimen dialogue"),
    ("T2_B_08", "Q13_features", ["feature_hint_privileging", "improve_skipped_steps"], "no full solution; but skips to final"),
    ("T2_B_09", "Q13_features", ["feature_theorem_lookup", "improve_visuals", "improve_prompting_clarity"], "theorems/formulas; visuals; right questions"),
    ("T2_B_10", "Q13_features", ["improve_accuracy_concern", "contains_ai_transcript_excerpt"], "argued with AI; gave up; asked professor"),
    ("T2_B_11", "Q13_features", ["feature_course_alignment"], "has notes and detailed explanations"),
    ("T2_B_12", "Q13_features", ["feature_customization"], "personalizing own chatbot"),
    ("T2_B_13", "Q13_features", ["feature_chapter_reference", "feature_step_by_step"], "steps + what chapter to look at"),
    ("T2_B_14", "Q13_features", ["feature_step_by_step", "feature_definitions"], ""),
    # T3
    ("T3_B_01", "Q13_features", ["feature_availability", "feature_patience", "improve_classroom_integration"], "'positivity' = patience; unclear how to use during lecture"),
    ("T3_B_02", "Q13_features", ["feature_course_alignment"], "pulls from book"),
    ("T3_B_03", "Q13_features", ["feature_chapter_reference"], "bring back earlier concepts"),
    ("T3_B_04", "Q13_features", ["feature_course_alignment"], "notes and books in GPT"),
    ("T3_B_05", "Q13_features", ["feature_availability", "improve_instruction_following", "improve_dont_give_answer"], "doesn't follow specific method; offers shortcuts"),
    ("T3_B_06", "Q13_features", ["nonsubstantive_response"], "'no issue with features'"),
    ("T3_B_07", "Q13_features", ["feature_hint_privileging", "improve_question_reference"], "small hints, partial steps useful; confused about which question"),
    ("T3_B_08", "Q13_features", ["feature_theorem_lookup"], "specific theorem retrieval"),
    ("T3_B_09", "Q13_features", ["feature_low_embarrassment", "feature_think_out_loud", "improve_dont_give_answer"], "no embarrassment; think out loud and correct; but gives full answer after 2 chats"),
    ("T3_B_10", "Q13_features", ["feature_step_by_step"], ""),
    ("T3_B_11", "Q13_features", ["feature_step_by_step", "improve_skipped_steps"], "sometimes gave answer, skipped steps"),
    ("T3_B_12", "Q13_features", ["feature_course_alignment", "improve_course_explanations"], "exactly professor's notation; tutor can't explain beyond notes"),
    ("T3_B_13", "Q13_features", ["feature_hint_privileging", "feature_course_alignment", "crit_specific_instance"], "MLE example — refers to theorems without giving solution"),
    ("T3_B_14", "Q13_features", ["nonsubstantive_response"], "N/A"),
    ("T3_B_15", "Q13_features", ["feature_step_by_step", "improve_dont_give_answer"], "detailed steps; wish not give answer immediately"),
    ("T3_B_16", "Q13_features", ["feature_definitions"], "definition + explanation"),
    ("T3_B_17", "Q13_features", ["feature_step_by_step"], "great reasoning, easy ways"),

    # ======================================================================
    # Q14_equity
    # ======================================================================
    # T1
    ("T1_B_01", "Q14_equity", ["equity_yes_unconditional"], "adds extra info"),
    ("T1_B_02", "Q14_equity", ["equity_cannot_speak_for_others"], "only for self"),
    ("T1_B_03", "Q14_equity", ["equity_conditional_prompting"], "prompt-dependent"),
    ("T1_B_04", "Q14_equity", ["equity_yes_unconditional"], "one-line yes"),
    ("T1_B_05", "Q14_equity", ["equity_conditional_prompting"], "individual prompts"),
    ("T1_B_06", "Q14_equity", ["equity_yes_unconditional"], "one-word yes"),
    ("T1_B_07", "Q14_equity", ["equity_yes_unconditional", "equity_access_through_campus"], "library or mobile"),
    ("T1_B_08", "Q14_equity", ["equity_yes_unconditional"], ""),
    ("T1_B_09", "Q14_equity", ["equity_yes_unconditional"], "versatile"),
    ("T1_B_10", "Q14_equity", ["equity_yes_unconditional"], "brief"),
    ("T1_B_11", "Q14_equity", ["equity_conditional_prompting"], "learning curve, watched classmates"),
    ("T1_B_12", "Q14_equity", ["equity_yes_unconditional"], "explains clearly"),
    ("T1_B_13", "Q14_equity", ["equity_concern_premium_access"], "not premium — but will change"),
    ("T1_B_14", "Q14_equity", ["equity_conditional_discipline"], "math yes, philosophy/essays no"),
    ("T1_B_15", "Q14_equity", ["equity_access_through_campus"], "library/lab access"),
    ("T1_B_16", "Q14_equity", ["equity_yes_unconditional"], "no issues"),
    ("T1_B_17", "Q14_equity", ["equity_yes_unconditional"], "brief"),
    # T2
    ("T2_B_01", "Q14_equity", ["equity_yes_unconditional"], ""),
    ("T2_B_02", "Q14_equity", ["equity_yes_unconditional"], "adapts via prompting"),
    ("T2_B_03", "Q14_equity", ["equity_yes_unconditional"], "one-word"),
    ("T2_B_04", "Q14_equity", ["nonsubstantive_response"], "n/a"),
    ("T2_B_05", "Q14_equity", ["equity_yes_unconditional"], "everyone has access"),
    ("T2_B_06", "Q14_equity", ["equity_yes_unconditional"], "one-word"),
    ("T2_B_07", "Q14_equity", ["equity_yes_unconditional", "equity_language_support"], "understands other languages"),
    ("T2_B_08", "Q14_equity", ["equity_yes_unconditional"], ""),
    ("T2_B_09", "Q14_equity", ["equity_yes_unconditional"], "one-word"),
    ("T2_B_10", "Q14_equity", ["equity_conditional_prompting"], "learning curve — after class, everything great"),
    ("T2_B_11", "Q14_equity", ["equity_yes_unconditional"], ""),
    ("T2_B_12", "Q14_equity", ["equity_yes_unconditional", "equity_concern_visual_learners"], "majority equal; visual learners struggle"),
    ("T2_B_13", "Q14_equity", ["equity_yes_unconditional"], ""),
    ("T2_B_14", "Q14_equity", ["equity_yes_unconditional"], "understanding what problem asks"),
    # T3
    ("T3_B_01", "Q14_equity", ["equity_yes_unconditional", "equity_language_support"], "different languages"),
    ("T3_B_02", "Q14_equity", ["equity_yes_unconditional"], "no challenges"),
    ("T3_B_03", "Q14_equity", ["equity_yes_unconditional"], "everyone benefits"),
    ("T3_B_04", "Q14_equity", ["equity_yes_unconditional"], "one-word"),
    ("T3_B_05", "Q14_equity", ["equity_conditional_self_discipline"], "'abuse the system — receiving answers instead of engaging'"),
    ("T3_B_06", "Q14_equity", ["equity_cannot_speak_for_others"], "accommodates my needs"),
    ("T3_B_07", "Q14_equity", ["equity_premium_resolved"], "had to have premium before; now resolved"),
    ("T3_B_08", "Q14_equity", ["equity_language_support"], "struggle with English; AI helps"),
    ("T3_B_09", "Q14_equity", ["equity_yes_unconditional"], "adapts to individual learning style"),
    ("T3_B_10", "Q14_equity", ["equity_yes_unconditional"], "accessible nowadays"),
    ("T3_B_11", "Q14_equity", ["equity_language_support"], "rephrase simpler, define phrases"),
    ("T3_B_12", "Q14_equity", ["equity_yes_unconditional"], "one-word yes"),
    ("T3_B_13", "Q14_equity", ["equity_yes_unconditional", "equity_conditional_complexity"], "but complex questions still unclear"),
    ("T3_B_14", "Q14_equity", ["nonsubstantive_response"], "N/A"),
    ("T3_B_15", "Q14_equity", ["equity_access_through_campus"], "library access"),
    ("T3_B_16", "Q14_equity", ["equity_conditional_discipline"], "subject-dependent; math fine, essays/answers not"),
    ("T3_B_17", "Q14_equity", ["equity_yes_unconditional"], ""),

    # ======================================================================
    # Q15_critthink
    # ======================================================================
    # T1
    ("T1_B_01", "Q15_critthink", ["crit_hinders_cognitive_shortcut"], "'avoid thinking of what I need to do'"),
    ("T1_B_02", "Q15_critthink", ["crit_helps_unstuck"], "shed light when stuck"),
    ("T1_B_03", "Q15_critthink", ["crit_helps_understanding_scaffold", "crit_specific_instance"], "did problem twice, easier second time"),
    ("T1_B_04", "Q15_critthink", ["crit_hinders_gives_answer", "improve_socratic_questioning"], "spits answer; doesn't ask questions"),
    ("T1_B_05", "Q15_critthink", ["crit_helps_step_reasoning", "concern_course_alignment"], "helps steps but confusing when off-class"),
    ("T1_B_06", "Q15_critthink", ["crit_helps_hint_privileging"], "hint then figure out independently"),
    ("T1_B_07", "Q15_critthink", ["crit_helps_adaptive"], "can request specific format"),
    ("T1_B_08", "Q15_critthink", ["crit_ambivalent"], "'if used wrong, limits critical thinking; if used as tutor, opposite'"),
    ("T1_B_09", "Q15_critthink", ["crit_ambivalent", "crit_hinders_gives_answer"], "eager to give full answer"),
    ("T1_B_10", "Q15_critthink", ["crit_hinders_memory_retention", "trade_off_metacognitive"], "unable to recall easily; 'but still worth it'"),
    ("T1_B_11", "Q15_critthink", ["crit_helps_why_questions", "crit_specific_instance"], "t-distribution vs normal; asking why"),
    ("T1_B_12", "Q15_critthink", ["crit_helps_step_reasoning"], "many problems, show steps"),
    ("T1_B_13", "Q15_critthink", ["crit_helps_unstuck", "crit_specific_instance"], "stuck 30 min now hint unsticks"),
    ("T1_B_14", "Q15_critthink", ["crit_helps_specific_instance", "crit_specific_instance"], "exam 1 — repeat process, key flaws"),
    ("T1_B_15", "Q15_critthink", ["crit_helps_method_identification"], "what method to use"),
    ("T1_B_16", "Q15_critthink", ["crit_helps_step_reasoning", "crit_helps_independent_practice"], "reproduce process on my own"),
    ("T1_B_17", "Q15_critthink", ["crit_helps_understanding_scaffold"], "expand learning"),
    # T2
    ("T2_B_01", "Q15_critthink", ["improve_prompting_clarity"], "specifically ask for less info"),
    ("T2_B_02", "Q15_critthink", ["crit_hinders_confusion", "concern_learning_vs_completion"], "ends up teaching self; just wants it done"),
    ("T2_B_03", "Q15_critthink", ["crit_external_backup"], "YouTube for clarity"),
    ("T2_B_04", "Q15_critthink", ["crit_helps_understanding_scaffold"], "straightforward answer + examples"),
    ("T2_B_05", "Q15_critthink", ["crit_helps_independent_practice"], "practice with help"),
    ("T2_B_06", "Q15_critthink", ["nonsubstantive_response"], "single '-'"),
    ("T2_B_07", "Q15_critthink", ["crit_helps_retrospective", "crit_specific_instance"], "easy in hindsight; concept understanding"),
    ("T2_B_08", "Q15_critthink", ["crit_helps_unstuck", "crit_hinders_dependence", "concern_exam_transfer"], "roadblocks; but miss it on tests"),
    ("T2_B_09", "Q15_critthink", ["crit_helps_hint_privileging", "crit_specific_instance"], "professor fixed to stop giving answers"),
    ("T2_B_10", "Q15_critthink", ["crit_helps_comparison", "crit_helps_error_diagnosis"], "compare with AI's answer; explain where went wrong"),
    ("T2_B_11", "Q15_critthink", ["crit_helps_pacing"], "own pace; helpful answers"),
    ("T2_B_12", "Q15_critthink", ["crit_helps_independent_practice", "improve_dont_give_answer"], "similar problems; but gives full solution even when programmed"),
    ("T2_B_13", "Q15_critthink", ["crit_helps_error_diagnosis"], "steps to find where messed up"),
    ("T2_B_14", "Q15_critthink", ["crit_helps_why_questions"], "how and why things done"),
    # T3
    ("T3_B_01", "Q15_critthink", ["crit_helps_specific_instance", "crit_specific_instance"], "hypothesis testing, identifying hypothesis"),
    ("T3_B_02", "Q15_critthink", ["crit_hinders_reliance_tool"], "'tool of reliance — may not need to think'"),
    ("T3_B_03", "Q15_critthink", ["crit_helps_generic"], "useful tool — brief"),
    ("T3_B_04", "Q15_critthink", ["crit_neutral"], "'not really'"),
    ("T3_B_05", "Q15_critthink", ["crit_helps_step_reasoning", "crit_helps_independent_practice"], "confidence in solving"),
    ("T3_B_06", "Q15_critthink", ["crit_helps_theorem_connection"], "identify and connect theorems"),
    ("T3_B_07", "Q15_critthink", ["crit_hinders_crutch", "concern_learning_vs_completion"], "'ai tutor crutch' — skipping critical thinking entirely"),
    ("T3_B_08", "Q15_critthink", ["crit_ambivalent", "crit_helps_hint_privileging"], "spits answer, but right prompt → helps think"),
    ("T3_B_09", "Q15_critthink", ["crit_hinders_reassurance"], "'constant need of reassurance... just in case'"),
    ("T3_B_10", "Q15_critthink", ["crit_helps_independent_practice"], "practice questions"),
    ("T3_B_11", "Q15_critthink", ["crit_helps_clarification"], "clarify thoughts; reorganize answer"),
    ("T3_B_12", "Q15_critthink", ["crit_helps_argument_with_ai"], "'questioned its results and had to argue with it'"),
    ("T3_B_13", "Q15_critthink", ["crit_ambivalent", "crit_hinders_memory_offloading"], "long; explicit 'offloading my memory'"),
    ("T3_B_14", "Q15_critthink", ["concern_forced_use"], "don't like using in class"),
    ("T3_B_15", "Q15_critthink", ["crit_helps_specific_instance", "crit_specific_instance"], "likelihood function — what to do next, reasons why"),
    ("T3_B_16", "Q15_critthink", ["nonsubstantive_response"], "n/a"),
    ("T3_B_17", "Q15_critthink", ["crit_helps_independent_work", "improve_scope_relevance"], "better at own work; but too much info"),

    # ======================================================================
    # Q16_suggest
    # ======================================================================
    # T1
    ("T1_B_01", "Q16_suggest", ["suggest_none"], ""),
    ("T1_B_02", "Q16_suggest", ["suggest_assignment_per_topic"], "AI tutor assignment for every topic"),
    ("T1_B_03", "Q16_suggest", ["suggest_textbook_integration", "suggest_class_notes", "suggest_practice_exam"], "extensive — scan full textbook, master notes, tailored practice exams"),
    ("T1_B_04", "Q16_suggest", ["suggest_none"], ""),
    ("T1_B_05", "Q16_suggest", ["suggest_dont_give_answer"], ""),
    ("T1_B_06", "Q16_suggest", ["suggest_none"], ""),
    ("T1_B_07", "Q16_suggest", ["suggest_none"], ""),
    ("T1_B_08", "Q16_suggest", ["suggest_none"], ""),
    ("T1_B_09", "Q16_suggest", ["suggest_dont_give_answer"], ""),
    ("T1_B_10", "Q16_suggest", ["suggest_none"], ""),
    ("T1_B_11", "Q16_suggest", ["suggest_dont_auto_solve"], "don't answer copy-paste"),
    ("T1_B_12", "Q16_suggest", ["suggest_none"], ""),
    ("T1_B_13", "Q16_suggest", ["suggest_none"], ""),
    ("T1_B_14", "Q16_suggest", ["suggest_dont_give_answer", "concern_homework_upload"], "spits answers; uncomfortable uploading homework"),
    ("T1_B_15", "Q16_suggest", ["suggest_dont_give_answer"], ""),
    ("T1_B_16", "Q16_suggest", ["suggest_none"], ""),
    ("T1_B_17", "Q16_suggest", ["suggest_none"], ""),
    # T2
    ("T2_B_01", "Q16_suggest", ["suggest_none"], ""),
    ("T2_B_02", "Q16_suggest", ["suggest_dont_spit_answer", "suggest_step_by_step_interaction"], ""),
    ("T2_B_03", "Q16_suggest", ["suggest_none"], "N/A"),
    ("T2_B_04", "Q16_suggest", ["suggest_none"], ""),
    ("T2_B_05", "Q16_suggest", ["suggest_none"], ""),
    ("T2_B_06", "Q16_suggest", ["suggest_none"], ""),
    ("T2_B_07", "Q16_suggest", ["suggest_consistency", "suggest_socratic_opener"], "step by step; ask what student knows"),
    ("T2_B_08", "Q16_suggest", ["suggest_dont_skip_steps"], "elaborate more, don't skip"),
    ("T2_B_09", "Q16_suggest", ["suggest_none"], ""),
    ("T2_B_10", "Q16_suggest", ["suggest_none"], ""),
    ("T2_B_11", "Q16_suggest", ["suggest_question_format"], "pdf format for assignments"),
    ("T2_B_12", "Q16_suggest", ["suggest_visuals"], "graphs, charts, diagrams"),
    ("T2_B_13", "Q16_suggest", ["suggest_none"], ""),
    ("T2_B_14", "Q16_suggest", ["suggest_none"], ""),
    # T3
    ("T3_B_01", "Q16_suggest", ["suggest_assignment_design"], "more frequent, shorter assignments"),
    ("T3_B_02", "Q16_suggest", ["suggest_dont_give_answer"], "less straightforward answers"),
    ("T3_B_03", "Q16_suggest", ["suggest_reference_fix"], "wouldn't talk about right example"),
    ("T3_B_04", "Q16_suggest", ["suggest_pdf_alongside"], "class the pdf for the assignment"),
    ("T3_B_05", "Q16_suggest", ["suggest_none"], ""),
    ("T3_B_06", "Q16_suggest", ["suggest_none"], ""),
    ("T3_B_07", "Q16_suggest", ["suggest_reference_fix"], "better question reference"),
    ("T3_B_09", "Q16_suggest", ["suggest_simplification", "suggest_scope_relevance"], "language too complex, too much info"),
    ("T3_B_10", "Q16_suggest", ["suggest_none"], ""),
    ("T3_B_11", "Q16_suggest", ["suggest_none"], ""),
    ("T3_B_12", "Q16_suggest", ["suggest_iteration"], "each version has improved"),
    ("T3_B_13", "Q16_suggest", ["suggest_reference_fix"], "gives different question than asked"),
    ("T3_B_14", "Q16_suggest", ["suggest_not_required"], "don't make required"),
    ("T3_B_15", "Q16_suggest", ["suggest_class_notes_integration"], "notes + examples in chat"),
    ("T3_B_16", "Q16_suggest", ["suggest_none"], "n/a"),
    ("T3_B_17", "Q16_suggest", ["suggest_dont_give_answer"], "help do things independently"),
]

# Write
out_path = './data/course_B_coded.csv'
with open(out_path, 'w', newline='', encoding='utf-8') as fh:
    writer = csv.writer(fh)
    writer.writerow(['respondent_id', 'question', 'codes', 'coder_note'])
    for rid, q, codes, note in CODED:
        writer.writerow([rid, q, ';'.join(codes), note])

print(f"Total coded (Course B): {len(CODED)}")
print(f"Written to: {out_path}")

# Frequencies
from collections import Counter, defaultdict
freq_by_q = defaultdict(Counter)
for rid, q, codes, note in CODED:
    for c in codes:
        freq_by_q[q][c] += 1

print("\n=== Code frequencies by question (Course B) ===")
for q in ['Q12_balance', 'Q13_features', 'Q14_equity', 'Q15_critthink', 'Q16_suggest']:
    print(f"\n--- {q} ---")
    for code, n in sorted(freq_by_q[q].items(), key=lambda x: -x[1]):
        print(f"  {n:3d}  {code}")
