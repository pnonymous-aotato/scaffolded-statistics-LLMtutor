# Educator Bot Template Set — README

Six reusable system-prompt templates for educators deploying LLM-based tutors, TAs, testers, and concierges for a course. Each template is stripped of course-specific content and ready to be adapted with a small set of placeholder replacements. All templates avoid references to any specific textbook — they refer to *"instructor-provided materials"* loaded into the bot's knowledge.

---

## The Six Archetypes

| # | Archetype | What it does | Best use |
|---|---|---|---|
| 1 | **Thinking Partner** | SMARTS + FRAME problem-solving coach. Refuses to hand out answers. | Homework and assignment support, especially proof-based or multi-step problems |
| 2 | **Coding Tutor** | Teaches code for a specific language/package stack, line by line. | Stat/programming courses where students need to learn software from zero |
| 3 | **Topic TA** | Explains concepts from instructor-provided materials. Can surface slide files on request. | Replacement/supplement for a single chapter or topic unit |
| 4 | **Assessment Delivery** | Runs locked, no-hints-allowed quizzes with equality guarantees. | In-class or timed assessments; replaces traditional short quizzes |
| 5 | **Exam Review & Practice Generator** | Builds unlimited fresh practice problems parallel to real exams, with hint ladders. | Exam prep where students need volume of varied practice |
| 6 | **Course Concierge** | 24/7 logistics and policy Q&A (syllabus, schedule, deadlines). Does not do academic content. | One bot per course for the whole term |

The six are designed to **compose**: a student in a course might use the Concierge for "when is the midterm," the Topic TA for "what's a CDF," the Thinking Partner for their assignment, the Coding Tutor for R help, the Practice Generator to drill, and the Assessment bot for the in-class quiz. Each bot is told explicitly to redirect out-of-scope queries to the appropriate sibling.

---

## Shared Template-Variable Convention

All six templates use `{{DOUBLE_CURLY_CAPS}}` placeholders. Common variables across multiple templates:

| Variable | Meaning | Example |
|---|---|---|
| `{{COURSE_CODE}}` | Short course code | `Course A` |
| `{{COURSE_NAME}}` | Full course title | `Introduction to Statistical Concepts` |
| `{{COURSE_LEVEL}}` | Level descriptor | `introductory`, `upper-division`, `graduate` |
| `{{INSTRUCTOR_NAME}}` | Instructor's name | `Dr. Jane Smith` |
| `{{INSTITUTION}}` | University/school | `CSU redacted` |
| `{{TERM}}` | Academic term | `Fall 2026` |
| `{{TOPIC_SCOPE}}` | Topical scope the bot covers | `hypothesis testing and confidence intervals` |
| `{{TOPIC_CONCEPTS_LIST}}` | Bullet list of in-scope concepts | *(see each template)* |
| `{{BOT_NAME}}` | Bot's display name/persona | `StatsBuddy` |
| `{{BOT_TONE}}` | Stylistic descriptor | `cheerful and encouraging`, `precise and formal` |

Template-specific variables are listed at the top of each file.

---

## Deployment Guide

Each template is deployable to:
- **OpenAI Custom GPT Builder** → paste into *Instructions* field
- **Claude Projects** → paste into project system prompt
- **API-based custom wrappers** → use as the system message

### Recommended models

| Archetype | Minimum | Recommended |
|---|---|---|
| Thinking Partner | GPT-4o / Claude Sonnet 4 | GPT-5 / Claude Opus 4.7 |
| Coding Tutor | GPT-4o-mini / Claude Haiku | GPT-5 / Claude Opus 4.7 |
| Topic TA | GPT-4o / Claude Sonnet 4 | GPT-5 / Claude Sonnet 4.6 |
| Assessment Delivery | GPT-5 / Claude Opus 4.7 only | Same |
| Exam Review | GPT-4o / Claude Sonnet 4 | GPT-5 / Claude Opus 4.7 |
| Course Concierge | GPT-4o-mini / Claude Haiku | GPT-4o / Claude Sonnet 4.6 |

For archetypes with strict refusal behavior (Thinking Partner, Assessment Delivery), cheaper models leak answers under student pressure. Do not go below the Minimum column.

### Knowledge files to upload

Each template specifies what should go into the bot's Knowledge section. At minimum, every bot benefits from:
- **Instructor-provided materials** relevant to the bot's scope (lecture notes, slide decks, worked examples, solution keys where appropriate)
- **A course syllabus** (used especially by Concierge)
- **The course's key-concepts reference** if one exists

Do not upload solution keys to the Thinking Partner bot. Do not upload the actual exam file to the Exam Review bot as readable text (use it as an internal blueprint only — see that template).

---

## Files in this set

1. `01_thinking_partner_bot.md`
2. `02_coding_tutor_bot.md`
3. `03_topic_ta_bot.md`
4. `04_assessment_delivery_bot.md`
5. `05_exam_review_bot.md`
6. `06_course_concierge_bot.md`

Each is a standalone markdown file containing: a placeholder legend, deployment notes, and the pasteable system prompt in a code block.

---

## Quick customization checklist (for any template)

Before deploying any bot:

1. **Replace every `{{PLACEHOLDER}}`** in the prompt. Grep the file first to confirm none remain.
2. **Upload knowledge files** listed in the template's deployment notes.
3. **Set conversation starters** (2–4 suggested tappable openers) — each template includes examples.
4. **Choose a model** from the recommendation table above.
5. **Do a live-fire test**: open a fresh chat, paste a challenging or adversarial message, confirm the bot follows the protocol. Weak models fail this test silently.
