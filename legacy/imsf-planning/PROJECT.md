# Course Generator — IMSF Assessment Suite

## What This Is

Course Generator is a tool for creating vocational training courses with AI-powered handout generation, question banks, and storytelling frameworks. The current milestone (v1.1) focuses on creating a complete, scientifically-designed assessment package for the Inclusive Management for Shop Floor Supervisors (IMSF) course — 8 printable documents covering participant instruments and facilitator evaluation guides for use on the training day.

## Core Value

Facilitators can confidently measure, evaluate, and evidence behavioral change in male shop floor managers through assessment instruments grounded in behavioral science and tailored to the Indian manufacturing context.

## Requirements

### Validated

- ✓ Student Handout Generator (PDF pipeline from markdown) — v1.0.0
- ✓ AI question generation with mandatory human review workflow — v1.0.0
- ✓ Dark-themed PDF output (WeasyPrint) — v1.0.0
- ✓ Batch processing for courses — v1.0.0
- ✓ Question bank management (staging → review → approve) — v1.0.0
- ✓ CLI with 12+ flags — v1.0.0
- ✓ Course Design skill (CO → MO → SO hierarchy) — v1.0.0
- ✓ Storytelling Framework Generator skill — v1.0.0
- ✓ IMSF course design (00-requirements.md, 02-course-structure.md) — v1.0.0

### Active

- [ ] Pre-Training Self-Assessment (participant Likert 1-5 questionnaire)
- [ ] Pre-Assessment Scoring & Interpretation Guide (facilitator)
- [ ] Scenario-Based Assessment (participant multiple choice, Module 6)
- [ ] Scenario Answer Key with Rationale (facilitator)
- [ ] Personal Action Plan (participant template, Module 7)
- [ ] Action Plan Evaluation Rubric (facilitator)
- [ ] Post-Training Self-Assessment (same items as Pre, Likert 1-5)
- [ ] Post-Assessment Scoring + Pre/Post Comparison Tool (facilitator)

### Out of Scope

- 30/60/90-day follow-up instruments — deferred to v1.2
- Digital/online form versions — printable only for v1.1
- Light theme handout generator — separate v1.1 track, not this milestone
- Answer key generator feature in CLI — future enhancement

## Context

- **Course:** Inclusive Management for Shop Floor Supervisors (IMSF)
- **Target participants:** Male managers/supervisors, Indian manufacturing, 28-50 years, engineering background
- **Facilitator:** External female consultant with PhD in Emotional Intelligence
- **Training format:** 1 day (9AM–5PM), 7 modules, 50/50 theory/practice
- **Training driver:** Reactive (complaints filed by women employees re: rude behavior, lack of courtesy)
- **Key behaviors to assess:** Politeness, empathy, unconscious bias awareness, menstrual health sensitivity, fair task allocation, active listening, conflict resolution
- **Assessment science basis:** Behavioral change measurement, not knowledge recall
- **Cultural context:** Indian workplace; examples and language must be locally resonant
- **Proposal document:** `courses/inclusive-management-shop-floor/Training_Proposal_IMSF.docx`
- **Course structure:** `courses/inclusive-management-shop-floor/02-course-structure.md`

## Constraints

- **Language:** English
- **Format:** Printable Word/PDF documents only
- **Audience literacy:** Engineering graduates — can handle structured formats
- **Sensitivity:** Psychologically safe language; no shaming; growth framing
- **Assessment type:** Behavior-focused (not knowledge quiz) — Likert + MCQ scenarios
- **Volume:** 8 documents total (4 participant + 4 facilitator guides)

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Likert 1-5 for Pre/Post | Standard for behavioral self-assessment; allows pre/post delta measurement | — Pending |
| MCQ for scenarios | Appropriate for this audience; structured choices reduce ambiguity | — Pending |
| Training-day only (no 30/60/90 day) | Scope control; follow-ups can be added in v1.2 | — Pending |
| 8 documents (4+4 pairing) | Every participant instrument paired with facilitator guide for completeness | — Pending |

---
*Last updated: 2026-02-17 after milestone v1.1 kickoff*
