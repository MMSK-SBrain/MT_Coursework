# Course Generator

A web app for teachers to design industry-relevant courses that still meet academic requirements: from a course handout or module sheet, through job-role research, course–job fit and learning outcomes, down to hour-wise lesson plans, slides, case studies and explainer videos.

The design is in [docs/plans/2026-11-04-course-generator-app-design.md](docs/plans/2026-11-04-course-generator-app-design.md).

## Layout

| Folder | What it holds |
|---|---|
| `courses/` | The four active courses (AEZC517, AELZC441, AEZC516, TUV SUD). They become the app's first imported courses and the AI harness's worked examples. |
| `reference/` | Material the app reuses: the markdown-to-pptx tool and the dark theme. |
| `.claude/skills/course-design-skill/` | Instructional-design rules (CO → MO → SO) used for the app's prompts. |
| `legacy/` | Older and inactive courses, kept untouched for reference. |
| `docs/plans/` | Design and implementation plans. |

The previous Python student-handout generator was removed; tag `pre-cleanup` holds the repository as it was before this restructure.

## GitHub Pages

`index.md` and `courses/tuv-sud-automotive-technician/` are still published through `.github/workflows`, with the same URLs as before.
