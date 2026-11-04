# Course Generator: design

Date: 2026-11-04 · Status: draft for review · Prototype: https://claude.ai/artifact/5qtFPcKY3RSG8ETobXbanE

## Objective

A free web utility on the Reynlab website that helps teachers design courses that are relevant to industry and still meet academic requirements. It goes from a course handout or a module list all the way to hour-wise lesson plans, and then, as paid features, to slides, case studies and explainer videos.

## Users and accounts

- Teachers sign up with Google or email, then fill in a short profile: institution, subject and role. The free tier unlocks straight away.
- Extra sign-ups are limited by email and by device.
- Teacher accounts are separate from Reynlab's learner accounts.

## Free and paid

| Free (every teacher, every month) | Paid |
|---|---|
| 1 course, design only, exported as `.md` | Full case studies |
| Inputs, job roles, course–job fit, outcomes, learning plans | Slide decks (`.pptx`) |
| Hour-wise lesson plans | Instructor guide as `.docx` |
| Industry examples | Videos beyond the free allowance |
| Further-learning links | Extra courses beyond 1 a month |
| 1 video of up to 5 minutes | |

## User flow

1. **Inputs.** The teacher uploads a course handout (`.docx`, `.pdf` or `.txt`), a module sheet (`.xlsx`), or both. The app combines them into one module list and flags where they disagree. A course brief (audience, hours, industry, job market) is filled in from the files, and the teacher can edit it.
2. **Job roles.** A broad search starts from the module keywords. It returns roles with posting counts, skills, experience level and a module-match %. The teacher picks the relevant roles or adds their own.
3. **Course–job fit.** The app compares the modules with the selected roles and proposes changes labelled Add, Strengthen or Trim, each with the reason, target module and hours. The teacher accepts, changes or rejects each one. Changes that conflict with the handout are marked as academic requirements. The teacher then confirms the course structure, which becomes v2.
4. **Outcomes.** Course objectives and learning outcomes are drafted from the confirmed structure. Each one can be edited inline or given a suggested edit: quick options (raise Bloom level, make it measurable, add industry context, shorten, split, match handout wording) or a free-text instruction. Suggestions are shown next to the original before anything is replaced. The teacher locks outcomes one by one, then freezes the set.
5. **Learning plans.** One course can have several plans. Each plan has:
   - a **learning path**, which decides the outputs and which video types are allowed:

     | Family | Paths |
     |---|---|
     | Live | Classroom, Lab, Bootcamp |
     | Blended | Flipped, Hybrid, Cohort |
     | Self-paced | eLearning, Microlearning |
     | Content | YouTube, Shorts |

   - a **teaching style**, set per plan and changeable per session. There are 17 styles in four families (Explain, Engage, Apply, Investigate), plus Auto, which picks a style from the outcome's Bloom level.
   - an optional **audience variant**, such as freshers and experienced.
6. **Build.** Per session: an hour-wise plan in timed blocks, industry examples, further-learning links, and, as paid features, case studies, slides, the instructor guide and video.
7. **Changes ripple down.** Editing frozen outcomes or the confirmed structure marks every dependent item as out of date.

Video rules by path:

| Path | Video |
|---|---|
| Classroom, Lab, Bootcamp | Demonstration only |
| eLearning | None |
| Flipped | Pre-class videos |
| Microlearning, YouTube, Shorts | Whiteboard animation, explainroo motion graphics, screen demo, slides with voice-over |

## Content model

```
Course → Module → Session → Hour block (minutes, activity, SO ids, style)
                                 └─ industry example · further-learning links · quick check
                                 └─ paid: case study · slides · video
```

- **Outcome hierarchy.** Course objectives (CO) → course learning outcomes (LO) → module outcomes (MO, 1–3 per module, each serving at least one LO) → session outcomes (SO, per lesson, each serving at least one MO) → hour blocks (each teaching block names the SOs it serves).
- **Roll-up.** An MO is met when some SO serves it at the same Bloom level or higher. An LO is met when all its MOs are met. Gaps are shown as warnings, never silently filled.
- Each item stores the ids it was built from: outcome ids, role ids and the version of the course structure. That's what lets changes ripple down.
- Case studies are labelled **Real, sourced** (with checkable links) or **Composite** (realistic but made up), and never left unlabelled.
- Further-learning links come from the YouTube Data API and web search. Teachers approve each one, and links are re-checked periodically so dead ones get flagged.

## AI harness (OpenRouter: Qwen, GLM)

The aim is flagship-level quality from cheap models. The approach:

1. **Small, narrow calls.** One call per outcome, session or block. Never one whole-course prompt.
2. **Structured output.** Every call returns JSON checked against a schema (zod). If the check fails, the call is retried once with the error attached.
3. **Facts are supplied, never recalled.** Job data, handout text, YouTube results and a maintained list of standards are passed in as context. The model writes around those facts.
4. **Rules checked in code:**
   - Bloom verbs come from an approved list.
   - The blocks in an hour add up to 60 minutes.
   - Every outcome is covered by some session.
   - Every SO is served by a block, and every teaching block serves an SO.
   - Every MO is met by its SOs (Bloom level roll-up); unmet ones get one repair.
   - No vague verbs such as "understand" or "know".
   - Every link resolves.
5. **Rubric review.** A stronger, still cheap, model scores the draft against a rubric for that stage. A low score triggers one automatic repair. This is used on the high-stakes stages: outcomes and course–job fit.
   - **Session content check.** For every session, a reviewer judges whether each block actually delivers the SOs it names (yes / partly / no, with a reason). Blocks below the threshold are rewritten once (title, activity, quick check only). This is the main guard that open-model content meets each lesson's objectives.
6. **Examples in the prompt.** The four imported courses (AEZC517, AELZC441, AEZC516, TUV SUD) are used as worked examples for each stage.
7. **Test set.** 5–10 fixed course briefs, run per stage on Qwen, GLM and Claude as a baseline, scored with the rubrics plus human review. The model for each stage is chosen on quality per unit of cost. The test set is re-run whenever a prompt changes.
8. **Easy switching and traceability.** Each stage has a main model and a backup, set in configuration. Every output records its model, its prompt version and its cost.

## Feedback

- **On every output:** thumbs up or down, a category (inaccurate, low quality, not industry-relevant, wrong level, missing something) and free text.
- **For the whole site:** a feedback button on every page.
- Feedback is stored with the model and prompt version. Thumbs-down items go into the test set.
- An admin view groups feedback by stage and model.

## Architecture

- TypeScript throughout.
- Next.js app with Postgres for courses, users, quotas and feedback, plus object storage for uploads and exports.
- A background job queue for long generations, job searches and video rendering.
- explainroo (`/Volumes/Dev/explainroo`, Node) runs in video render workers.
- Exports: `.md` (free), and `.pptx` and `.docx` via pptxgenjs and docx (paid).

## Phases

0. **Repo cleanup.** Tag `pre-cleanup`. Delete the Python handout generator and outdated reports. Move non-active courses to `legacy/`. Keep the four active courses for import.
1. **Harness and test set first.** Prove that Qwen and GLM meet the rubric for outcomes, course–job fit and hour-wise plans before building the UI. This is the biggest risk.
2. **Free MVP.** Accounts, quotas, stages 1–5, hour-wise plans, industry examples, further-learning links, `.md` export and feedback.
3. **Paid.** Payments, case studies, slides and the instructor guide `.docx`.
4. **Video.** explainroo render workers, the free 5-minute allowance, and adding images, video clips and whiteboard scenes to explainroo.
5. **Later, to be decided:** CO–PO/PSO mapping for NBA, institution templates, assessments mapped to outcomes, a public library of shared plans, regional languages, LMS export, present mode, and the Reynlab platform Excel export.

## Open decisions

- **Jobs data source.** A job-listing API with India coverage, or a web-search API. No scraping of LinkedIn or Naukri.
- **Payment provider and pricing for paid items.** Razorpay is the likely choice for India.
- **Whether saved role selections and fit decisions allow a "market changed since you confirmed" re-check later.**
- **Hosting:** Vercel plus a separate worker host, or one VPS.
