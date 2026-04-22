#!/usr/bin/env python3
"""
Phase 2 coding: Course A thematic coding.
Each response is coded with one or more codes from the Phase 1 codebook,
with a brief coder note explaining the decision for boundary cases.

This is a manual coding pass — codes are assigned by the coder after
reading each response in context, not by pattern-matching. The coder
notes serve as an audit trail for the §7.3 write-up and the OSF
supplementary codebook.
"""

import csv

# Each tuple: (respondent_id, question, codes, coder_note)
# Codes are from the Phase 1 Course A codebook.
# coder_note is only included where the coding decision is non-obvious.

CODED = [
    # ======================================================================
    # Q12_balance (Work-life-class balance)
    # ======================================================================
    # T1
    ("T1_A_01", "Q12_balance", ["benefit_time_efficiency", "benefit_availability"], ""),
    ("T1_A_02", "Q12_balance", ["benefit_understanding_scaffold"], "helps break down question for understanding"),
    ("T1_A_03", "Q12_balance", ["benefit_understanding_scaffold", "benefit_time_efficiency"], "concepts broken down, time reduced"),
    ("T1_A_04", "Q12_balance", ["benefit_generic"], "minimal content — 'it has helped me'"),
    ("T1_A_05", "Q12_balance", ["nonsubstantive_response"], "answered 'social media' — appears off-prompt"),
    ("T1_A_06", "Q12_balance", ["benefit_language_accessibility"], "simpler explanation of difficult language"),
    ("T1_A_07", "Q12_balance", ["benefit_availability", "benefit_absence_compensation"], "home/away-from-prof access"),
    ("T1_A_08", "Q12_balance", ["benefit_understanding_scaffold", "benefit_availability"], "concise descriptions"),
    ("T1_A_09", "Q12_balance", ["benefit_understanding_scaffold", "concern_over_reliance_ack"], "explicitly says 'I use it as a tool... not have it do it for me' — demonstrates awareness"),
    ("T1_A_10", "Q12_balance", ["benefit_availability"], "can ask as many questions as needed"),
    ("T1_A_11", "Q12_balance", ["benefit_understanding_scaffold"], "helps when confused or stuck"),
    ("T1_A_12", "Q12_balance", ["benefit_understanding_scaffold", "benefit_grammar_writing"], "grammar and problem-solving reminders"),
    ("T1_A_13", "Q12_balance", ["concern_cognitive_shortcut"], "critique-only response — 'shortcut to learning, hurting the student'"),
    ("T1_A_14", "Q12_balance", ["benefit_understanding_scaffold"], "helps remember/refresh concepts"),
    # T2
    ("T2_A_01", "Q12_balance", ["benefit_understanding_scaffold", "concern_cognitive_shortcut"], "ambivalent — stepping stone vs. giving answer too early"),
    ("T2_A_02", "Q12_balance", ["benefit_time_efficiency", "benefit_understanding_scaffold"], "study more efficiently, break down"),
    ("T2_A_03", "Q12_balance", ["benefit_time_efficiency"], "assignments more organized"),
    ("T2_A_04", "Q12_balance", ["benefit_availability"], "when instructor not available"),
    ("T2_A_05", "Q12_balance", ["benefit_ideation"], "getting ideas — brief"),
    ("T2_A_07", "Q12_balance", ["benefit_understanding_scaffold"], "break down question"),
    ("T2_A_08", "Q12_balance", ["benefit_understanding_scaffold"], "step-by-step examples"),
    ("T2_A_09", "Q12_balance", ["benefit_availability", "benefit_r_code"], "help outside class, R code errors"),
    ("T2_A_10", "Q12_balance", ["benefit_time_efficiency", "concern_over_reliance_ack"], "ambivalent — time saver but distraction risk"),
    ("T2_A_11", "Q12_balance", ["benefit_time_efficiency", "benefit_understanding_scaffold"], "time crunch + precision"),
    ("T2_A_12", "Q12_balance", ["benefit_grammar_writing", "benefit_understanding_scaffold"], "grammar + concept explanation"),
    # T3
    ("T3_A_01", "Q12_balance", ["benefit_understanding_scaffold", "benefit_course_alignment"], "stat-generated GPT, course-aligned steps"),
    ("T3_A_02", "Q12_balance", ["benefit_r_code"], "brief — R codes only"),
    ("T3_A_03", "Q12_balance", ["benefit_absence_compensation"], "missed class due to sports travel"),
    ("T3_A_04", "Q12_balance", ["benefit_understanding_scaffold"], "organized clear explanations"),
    ("T3_A_05", "Q12_balance", ["benefit_availability", "benefit_understanding_scaffold"], "ask questions until understanding"),
    ("T3_A_06", "Q12_balance", ["benefit_understanding_scaffold", "trade_off_metacognitive"], "'helped hinder' phrasing — ambivalent"),
    ("T3_A_07", "Q12_balance", ["benefit_time_efficiency"], "speed up assignments"),
    ("T3_A_08", "Q12_balance", ["benefit_understanding_scaffold"], "explains in parts"),
    ("T3_A_09", "Q12_balance", ["benefit_time_efficiency"], "time management through compartmentalization"),
    ("T3_A_10", "Q12_balance", ["benefit_time_efficiency"], "homework faster"),
    ("T3_A_11", "Q12_balance", ["benefit_planning_summary"], "plans and summaries"),
    ("T3_A_12", "Q12_balance", ["benefit_ideation"], "brief — gives ideas"),
    ("T3_A_13", "Q12_balance", ["concern_technical_access"], "HSI-1 account not connected — hindered"),

    # ======================================================================
    # Q13_features (Most helpful features / improvements)
    # ======================================================================
    # T1
    ("T1_A_01", "Q13_features", ["feature_course_alignment", "improve_scope_relevance"], "has professors guidelines but sometimes off-scope problems"),
    ("T1_A_02", "Q13_features", ["improve_dont_give_answer"], "should work with you instead"),
    ("T1_A_03", "Q13_features", ["feature_course_alignment", "improve_prompting_clarity", "improve_accuracy_concern"], "word prompts carefully; AI not always correct"),
    ("T1_A_04", "Q13_features", ["feature_ideation", "feature_definitions"], "options/ideas; clarifies definitions"),
    ("T1_A_05", "Q13_features", ["feature_r_code"], "R code help"),
    ("T1_A_06", "Q13_features", ["feature_r_code", "feature_step_by_step"], "R code + step-by-step"),
    ("T1_A_07", "Q13_features", ["feature_r_code", "feature_multiple_approaches"], "R code + multiple ways to same answer"),
    ("T1_A_08", "Q13_features", ["feature_definitions"], "good descriptions of topics"),
    ("T1_A_09", "Q13_features", ["feature_step_by_step"], "each step, break down more"),
    ("T1_A_10", "Q13_features", ["nonsubstantive_response"], "N/A"),
    ("T1_A_11", "Q13_features", ["feature_conversational", "improve_more_examples"], "asks questions like talking to someone; wants more examples"),
    ("T1_A_12", "Q13_features", ["feature_r_code"], "R code reminders"),
    ("T1_A_13", "Q13_features", ["feature_step_by_step"], "math feature, break down step by step"),
    ("T1_A_14", "Q13_features", ["feature_clarity"], "straightforward, clears up confusion"),
    # T2
    ("T2_A_01", "Q13_features", ["benefit_generic"], "no issues — non-specific"),
    ("T2_A_02", "Q13_features", ["feature_adaptive_practice"], "makes quizzes, adapts"),
    ("T2_A_03", "Q13_features", ["feature_chapter_specific_gpts"], "'various bots' — chapter-specific praised"),
    ("T2_A_04", "Q13_features", ["feature_chapter_specific_gpts", "feature_r_code"], "specific GPT bots, R focus"),
    ("T2_A_05", "Q13_features", ["feature_ideation", "improve_technical"], "gives ideas; load speed concern"),
    ("T2_A_07", "Q13_features", ["feature_step_by_step"], "provides solutions — but brief"),
    ("T2_A_08", "Q13_features", ["feature_clarity", "feature_step_by_step"], "specific responses with further explanation"),
    ("T2_A_09", "Q13_features", ["improve_technical"], "save link with uploaded images"),
    ("T2_A_10", "Q13_features", ["feature_step_by_step", "improve_prompting_clarity"], "step-by-step; improve understanding questions"),
    ("T2_A_11", "Q13_features", ["improve_prompting_clarity", "feature_course_alignment"], "tailored script would help"),
    ("T2_A_12", "Q13_features", ["feature_grammar_writing", "improve_technical"], "grammar; can't open certain links"),
    # T3
    ("T3_A_01", "Q13_features", ["feature_r_code", "feature_course_alignment"], "R tutor specifically praised, course-aligned"),
    ("T3_A_02", "Q13_features", ["nonsubstantive_response"], "'I really don't know'"),
    ("T3_A_03", "Q13_features", ["feature_r_code", "feature_course_alignment"], "R studio + hypothesis testing match class"),
    ("T3_A_04", "Q13_features", ["feature_chapter_specific_gpts"], "bots including DOE assistant"),
    ("T3_A_05", "Q13_features", ["feature_r_code"], "R code inputs effective"),
    ("T3_A_06", "Q13_features", ["feature_step_by_step"], "explains every step in stat math"),
    ("T3_A_07", "Q13_features", ["feature_course_alignment"], "class specific"),
    ("T3_A_08", "Q13_features", ["feature_step_by_step", "feature_hint_privileging"], "breaks down rather than giving answer"),
    ("T3_A_09", "Q13_features", ["feature_r_code", "improve_scope_relevance"], "R tutor; but code more complex than needed"),
    ("T3_A_10", "Q13_features", ["feature_r_code", "improve_scope_relevance"], "R tutor; practice questions off-topic"),
    ("T3_A_11", "Q13_features", ["feature_r_code"], "R code GPT"),
    ("T3_A_12", "Q13_features", ["feature_time_efficiency", "improve_accuracy_concern"], "quick; sometimes outdated"),
    ("T3_A_13", "Q13_features", ["feature_clarity"], "explanations"),

    # ======================================================================
    # Q14_equity
    # ======================================================================
    # T1
    ("T1_A_01", "Q14_equity", ["equity_conditional_effort"], "'gives you whatever you put into it'"),
    ("T1_A_02", "Q14_equity", ["equity_yes_unconditional"], ""),
    ("T1_A_03", "Q14_equity", ["equity_conditional_prompting"], "user-dependent"),
    ("T1_A_04", "Q14_equity", ["equity_yes_unconditional", "improve_scope_relevance"], "equal but subject-dependent"),
    ("T1_A_05", "Q14_equity", ["equity_yes_unconditional"], "brief yes"),
    ("T1_A_06", "Q14_equity", ["equity_yes_unconditional", "equity_concern_accessibility"], "equal but vision access concern"),
    ("T1_A_07", "Q14_equity", ["equity_yes_unconditional"], "works for me, assumes same for others"),
    ("T1_A_08", "Q14_equity", ["equity_yes_unconditional"], ""),
    ("T1_A_09", "Q14_equity", ["equity_conditional_prompting"], "if you ask it specifically"),
    ("T1_A_10", "Q14_equity", ["equity_yes_unconditional"], "different ways to teach material"),
    ("T1_A_11", "Q14_equity", ["equity_yes_unconditional"], "everyone has it"),
    ("T1_A_12", "Q14_equity", ["equity_yes_unconditional"], ""),
    ("T1_A_13", "Q14_equity", ["equity_conditional_prompting"], "if students know how to use it"),
    ("T1_A_14", "Q14_equity", ["equity_yes_unconditional"], "no bias"),
    # T2
    ("T2_A_01", "Q14_equity", ["equity_yes_unconditional"], "can break steps as needed"),
    ("T2_A_02", "Q14_equity", ["equity_yes_unconditional"], ""),
    ("T2_A_03", "Q14_equity", ["equity_yes_unconditional"], ""),
    ("T2_A_04", "Q14_equity", ["equity_yes_unconditional"], "brief yes"),
    ("T2_A_05", "Q14_equity", ["equity_yes_unconditional"], "'like a robot' — implicitly impartial"),
    ("T2_A_07", "Q14_equity", ["equity_yes_unconditional"], ""),
    ("T2_A_08", "Q14_equity", ["equity_yes_unconditional", "equity_concern_cost_access"], "accessible, free"),
    ("T2_A_09", "Q14_equity", ["equity_concern_instructor_guidance"], "'only if features are well explained by instructor'"),
    ("T2_A_10", "Q14_equity", ["equity_concern_language", "equity_conditional_prompting"], "clarity of questions + English"),
    ("T2_A_11", "Q14_equity", ["equity_conditional_prompting"], "prompts should be taught first"),
    ("T2_A_12", "Q14_equity", ["equity_yes_unconditional"], ""),
    # T3
    ("T3_A_01", "Q14_equity", ["equity_yes_unconditional"], "brief"),
    ("T3_A_02", "Q14_equity", ["equity_yes_unconditional"], "one-word yes"),
    ("T3_A_03", "Q14_equity", ["equity_yes_unconditional"], "altercations for any student"),
    ("T3_A_04", "Q14_equity", ["equity_yes_unconditional"], ""),
    ("T3_A_05", "Q14_equity", ["equity_yes_unconditional"], "ask until understanding"),
    ("T3_A_06", "Q14_equity", ["equity_yes_unconditional"], "everyone in class succeeded"),
    ("T3_A_07", "Q14_equity", ["equity_yes_unconditional"], "one-word"),
    ("T3_A_08", "Q14_equity", ["equity_yes_unconditional"], "brief"),
    ("T3_A_09", "Q14_equity", ["equity_conditional_prompting"], "'effectiveness at prompts determines quality' — explicit conditional at T3"),
    ("T3_A_10", "Q14_equity", ["equity_conditional_prompting", "equity_concern_instructor_guidance"], "yes, IF taught how to prompt"),
    ("T3_A_11", "Q14_equity", ["equity_yes_unconditional"], "personal instructor for everyone"),
    ("T3_A_12", "Q14_equity", ["equity_yes_unconditional"], ""),
    ("T3_A_13", "Q14_equity", ["equity_yes_unconditional"], "one-word"),

    # ======================================================================
    # Q15_critthink
    # ======================================================================
    # T1
    ("T1_A_01", "Q15_critthink", ["crit_helps_step_reasoning", "crit_helps_understanding_scaffold"], "visual understanding, step by step"),
    ("T1_A_02", "Q15_critthink", ["crit_helps_ideation"], "gives ideas — brief"),
    ("T1_A_03", "Q15_critthink", ["crit_helps_step_reasoning", "crit_hinders_over_reliance"], "breaking steps but reliance risk"),
    ("T1_A_04", "Q15_critthink", ["crit_hinders_copy_paste"], "copying text word for word"),
    ("T1_A_05", "Q15_critthink", ["crit_helps_independent_practice"], "reflective problem solving"),
    ("T1_A_06", "Q15_critthink", ["crit_helps_independent_practice"], "make exam questions"),
    ("T1_A_07", "Q15_critthink", ["crit_helps_step_reasoning"], "ideas that help progression"),
    ("T1_A_08", "Q15_critthink", ["crit_helps_step_reasoning", "crit_specific_instance"], "R code debugging example"),
    ("T1_A_09", "Q15_critthink", ["crit_helps_absence_compensation", "crit_helps_step_reasoning"], "missed class due to sport; review steps"),
    ("T1_A_10", "Q15_critthink", ["crit_helps_step_reasoning"], "understanding each step"),
    ("T1_A_11", "Q15_critthink", ["crit_helps_step_reasoning", "crit_specific_instance"], "test statistic formula example"),
    ("T1_A_12", "Q15_critthink", ["crit_helps_generic"], "no specific instance"),
    ("T1_A_13", "Q15_critthink", ["crit_helps_concept_recall", "crit_specific_instance"], "individual project, RScript recall"),
    ("T1_A_14", "Q15_critthink", ["crit_helps_independent_practice", "crit_specific_instance"], "individual project on variance/mean"),
    # T2
    ("T2_A_01", "Q15_critthink", ["crit_helps_step_reasoning"], "guides through steps"),
    ("T2_A_02", "Q15_critthink", ["crit_helps_independent_practice"], "practice problems"),
    ("T2_A_03", "Q15_critthink", ["crit_helps_specific_instance"], "converting R to Word"),
    ("T2_A_04", "Q15_critthink", ["crit_helps_independent_practice", "crit_specific_instance"], "mock exams before exam"),
    ("T2_A_05", "Q15_critthink", ["crit_helps_ideation"], "getting ideas — brief"),
    ("T2_A_07", "Q15_critthink", ["crit_helps_understanding_scaffold"], "understand more; doesn't change solving"),
    ("T2_A_08", "Q15_critthink", ["crit_helps_step_reasoning", "crit_specific_instance"], "R code errors, step-by-step debugging"),
    ("T2_A_09", "Q15_critthink", ["crit_ambivalent", "crit_hinders_over_reliance"], "helps when stuck; but harder to remember independently"),
    ("T2_A_10", "Q15_critthink", ["crit_ambivalent", "crit_specific_instance"], "caught math mistake; but writing got harder"),
    ("T2_A_11", "Q15_critthink", ["crit_ambivalent", "improve_prompting_clarity"], "different approaches than professor — both a feature and challenge"),
    ("T2_A_12", "Q15_critthink", ["crit_helps_different_perspective"], "different POV"),
    # T3
    ("T3_A_01", "Q15_critthink", ["crit_helps_follow_up_questions"], "follow-up questions on prior answer"),
    ("T3_A_02", "Q15_critthink", ["crit_helps_feedback"], "gives feedback — brief"),
    ("T3_A_03", "Q15_critthink", ["crit_helps_hint_privileging"], "'won't give you the fully answer but helps you get there'"),
    ("T3_A_04", "Q15_critthink", ["crit_helps_specific_instance"], "ANOVA, Duncan tests, group project"),
    ("T3_A_05", "Q15_critthink", ["crit_helps_concept_recall"], "remind of concepts throughout course"),
    ("T3_A_06", "Q15_critthink", ["crit_helps_independent_practice", "crit_specific_instance"], "practice for final exam"),
    ("T3_A_07", "Q15_critthink", ["crit_helps_time_efficiency"], "speed up assignments"),
    ("T3_A_08", "Q15_critthink", ["crit_neutral"], "'hasn't affected'"),
    ("T3_A_09", "Q15_critthink", ["crit_hinders_over_reliance"], "lacking critical thinking on tests"),
    ("T3_A_10", "Q15_critthink", ["crit_hinders_cognitive_shortcut"], "harder to want to learn when you can search"),
    ("T3_A_11", "Q15_critthink", ["crit_helps_independent_practice"], "exam prep"),
    ("T3_A_12", "Q15_critthink", ["crit_hinders_cognitive_shortcut"], "don't have to think"),
    ("T3_A_13", "Q15_critthink", ["crit_helps_why_questions"], "reasons why formulas work"),

    # ======================================================================
    # Q16_suggest
    # ======================================================================
    # T1
    ("T1_A_01", "Q16_suggest", ["suggest_none"], ""),
    ("T1_A_02", "Q16_suggest", ["suggest_none"], ""),
    ("T1_A_03", "Q16_suggest", ["suggest_none"], "still figuring out"),
    ("T1_A_04", "Q16_suggest", ["suggest_fewer_restrictions"], "remove limits/regulations"),
    ("T1_A_05", "Q16_suggest", ["suggest_none"], ""),
    ("T1_A_07", "Q16_suggest", ["suggest_none"], ""),
    ("T1_A_08", "Q16_suggest", ["suggest_none"], ""),
    ("T1_A_09", "Q16_suggest", ["suggest_none"], "balanced"),
    ("T1_A_10", "Q16_suggest", ["suggest_none"], ""),
    ("T1_A_11", "Q16_suggest", ["suggest_none"], "works great"),
    ("T1_A_12", "Q16_suggest", ["suggest_none"], ""),
    ("T1_A_13", "Q16_suggest", ["suggest_scope_relevance"], "limit databases to relevant sources"),
    ("T1_A_14", "Q16_suggest", ["suggest_none"], ""),
    # T2
    ("T2_A_01", "Q16_suggest", ["suggest_none"], "good pace"),
    ("T2_A_02", "Q16_suggest", ["suggest_none"], ""),
    ("T2_A_03", "Q16_suggest", ["suggest_none"], ""),
    ("T2_A_04", "Q16_suggest", ["suggest_accuracy"], "make sure response is actually helpful / on-topic"),
    ("T2_A_05", "Q16_suggest", ["suggest_none"], ""),
    ("T2_A_07", "Q16_suggest", ["suggest_none"], ""),
    ("T2_A_08", "Q16_suggest", ["suggest_none"], ""),
    ("T2_A_09", "Q16_suggest", ["suggest_technical"], "image link sharing"),
    ("T2_A_10", "Q16_suggest", ["suggest_none"], ""),
    ("T2_A_11", "Q16_suggest", ["suggest_deployment_standardization", "suggest_iteration"], "standardized model across classes; iterative"),
    ("T2_A_12", "Q16_suggest", ["suggest_none"], ""),
    # T3
    ("T3_A_01", "Q16_suggest", ["suggest_none"], "'AWESOME'"),
    ("T3_A_02", "Q16_suggest", ["suggest_none"], ""),
    ("T3_A_03", "Q16_suggest", ["suggest_none"], ""),
    ("T3_A_04", "Q16_suggest", ["suggest_none"], ""),
    ("T3_A_05", "Q16_suggest", ["suggest_none"], ""),
    ("T3_A_06", "Q16_suggest", ["suggest_none"], ""),
    ("T3_A_07", "Q16_suggest", ["suggest_none"], ""),
    ("T3_A_08", "Q16_suggest", ["suggest_none"], ""),
    ("T3_A_09", "Q16_suggest", ["suggest_iteration", "suggest_feedback_loop"], "incorporating student/faculty feedback"),
    ("T3_A_10", "Q16_suggest", ["suggest_scope_relevance"], "limit generation scope"),
    ("T3_A_11", "Q16_suggest", ["suggest_consistency"], "keep them consistent"),
    ("T3_A_12", "Q16_suggest", ["suggest_none"], ""),
    ("T3_A_13", "Q16_suggest", ["suggest_none"], ""),
]

# Write coded output
out_path = './data/course_A_coded.csv'
with open(out_path, 'w', newline='', encoding='utf-8') as fh:
    writer = csv.writer(fh)
    writer.writerow(['respondent_id', 'question', 'codes', 'coder_note'])
    for rid, q, codes, note in CODED:
        writer.writerow([rid, q, ';'.join(codes), note])

print(f"Total coded: {len(CODED)}")
print(f"Written to: {out_path}")

# Code frequency by question
from collections import Counter, defaultdict
freq_by_q = defaultdict(Counter)
for rid, q, codes, note in CODED:
    for c in codes:
        freq_by_q[q][c] += 1

print("\n=== Code frequencies by question (Course A) ===")
for q in ['Q12_balance', 'Q13_features', 'Q14_equity', 'Q15_critthink', 'Q16_suggest']:
    print(f"\n--- {q} ---")
    for code, n in sorted(freq_by_q[q].items(), key=lambda x: -x[1]):
        print(f"  {n:3d}  {code}")
