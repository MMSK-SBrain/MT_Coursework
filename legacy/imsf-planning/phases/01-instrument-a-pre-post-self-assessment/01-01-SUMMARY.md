---
phase: 01-instrument-a-pre-post-self-assessment
plan: 01
subsystem: assessment-instruments
tags: [python-docx, docx, word, likert, self-assessment, imsf, behavioral-assessment]

# Dependency graph
requires: []
provides:
  - "generate_participant_form.py: Python script that generates the participant self-assessment .docx"
  - "assessments/pre-post-self-assessment-participant.docx: Print-ready participant form"
affects:
  - 01-02 (facilitator guide — references same 21 items and domain structure)
  - 01-03 (any PDF export or packaging step)

# Tech tracking
tech-stack:
  added:
    - python-docx 1.2.0 (installed system-wide via pip3 --break-system-packages)
  patterns:
    - "apply_shading(cell, hex): OxmlElement approach for OOXML cell background shading"
    - "set_row_height(row, cm, rule): WD_ROW_HEIGHT_RULE.AT_LEAST for item rows, EXACTLY for separators"
    - "Domain boundaries set: separator rows after items 3, 6, 9, 12, 15, 18 — not after 21"
    - "SCRIPT_DIR + os.path.abspath(__file__) for portable path resolution"

key-files:
  created:
    - courses/inclusive-management-shop-floor/generate_participant_form.py
    - courses/inclusive-management-shop-floor/assessments/pre-post-self-assessment-participant.docx
  modified: []

key-decisions:
  - "WD_ROW_HEIGHT_RULE.EXACTLY (not .EXACT) is the correct attribute name in python-docx 1.2.0"
  - "Post column shading applied per-cell (not per-column) to ensure header cell also shaded"
  - "Separator rows use merge(cells[0], cells[2]) to span all 3 columns cleanly"
  - "Scale numbers use em-spaces (wide spacing) for circling legibility: '1   2   3   4   5'"

patterns-established:
  - "Pattern: generate_participant_form.py is the canonical source — edit script, re-run to regenerate docx"
  - "Pattern: All 21 items defined in ITEMS list at top of script for easy future editing"
  - "Pattern: PASS/FAIL print protocol for CI-friendly verification of each section"
  - "Pattern: try/except wrapping main() with sys.exit(1) on any exception"

# Metrics
duration: 4min
completed: 2026-02-18
---

# Phase 1 Plan 01: Participant Self-Assessment Form Summary

**python-docx generator producing a print-ready A4 'My Management Practices' form with all 21 behavioral items, grey-shaded Post (PM) column, 6 domain separator rows, self-reflection section, domain-averaging grid, and anonymous tear-off strip**

## Performance

- **Duration:** 4 min
- **Started:** 2026-02-18T02:14:54Z
- **Completed:** 2026-02-18T02:18:54Z
- **Tasks:** 1 of 1
- **Files modified:** 2

## Accomplishments

- Created `generate_participant_form.py` (427 lines) generating a fully structured participant self-assessment form
- Generated `assessments/pre-post-self-assessment-participant.docx` — 28-row 3-column table (1 header + 21 item rows + 6 separator rows)
- All 21 behavioral items present in exact domain order; reverse-scored items 5, 11, 18 indistinguishable from forward items; no reverse-score markers on form
- Post (PM) column cells shaded #DCDCDC throughout including header; domain separators shaded #F0F0F0
- Form title "My Management Practices" — words "assessment", "evaluation", "test" absent from entire document
- Self-reflection (3 questions), domain-averaging grid (Groups 1-7 + Total), and anonymous tear-off strip all present

## Task Commits

1. **Task 1: Create the participant form generator script** - `11cb5af` (feat)

## Files Created/Modified

- `courses/inclusive-management-shop-floor/generate_participant_form.py` — Python script using python-docx to generate the participant .docx; 427 lines; try/except with PASS/FAIL output
- `courses/inclusive-management-shop-floor/assessments/pre-post-self-assessment-participant.docx` — Generated Word document; 39KB; contains main 3-column table + domain-averaging grid table

## Decisions Made

- Used `WD_ROW_HEIGHT_RULE.EXACTLY` (python-docx 1.2.0 renamed `.EXACT` to `.EXACTLY`); auto-corrected after first run
- Applied shading per-cell rather than per-column to ensure consistent coverage including header row
- Used merged separator cells (`row.cells[0].merge(row.cells[2])`) for clean full-width domain breaks
- Scale numbers formatted with triple spaces for participant circling legibility

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 1 - Bug] WD_ROW_HEIGHT_RULE.EXACT renamed to EXACTLY in python-docx 1.2.0**

- **Found during:** Task 1 (first run of generate_participant_form.py)
- **Issue:** Plan specified `.EXACT` rule but python-docx 1.2.0 uses `.EXACTLY`; script exited with AttributeError after header block
- **Fix:** Changed `WD_ROW_HEIGHT_RULE.EXACT` to `WD_ROW_HEIGHT_RULE.EXACTLY` in `add_separator_row()`
- **Files modified:** courses/inclusive-management-shop-floor/generate_participant_form.py
- **Verification:** Script ran to completion with all 7 PASS messages on second run
- **Committed in:** 11cb5af (Task 1 commit)

---

**Total deviations:** 1 auto-fixed (1 bug — API naming change in library version)
**Impact on plan:** Minor one-line fix required by python-docx 1.2.0 vs. older API. No scope creep. Final output matches all plan specifications.

## Issues Encountered

- python-docx 1.2.0 changed `WD_ROW_HEIGHT_RULE.EXACT` to `WD_ROW_HEIGHT_RULE.EXACTLY` — resolved immediately on first test run by auto-fix.

## User Setup Required

None - no external service configuration required. python-docx 1.2.0 was already installed system-wide.

## Next Phase Readiness

- `generate_participant_form.py` is ready; can be re-run at any time to regenerate the .docx after item edits
- `assessments/` directory created; ready for facilitator guide (.docx) in Plan 02
- All 21 items validated in output; domain structure (7 groups of 3) confirmed in table row count (28 rows = 1 header + 21 items + 6 separators)
- No blockers for Plan 02

---
*Phase: 01-instrument-a-pre-post-self-assessment*
*Completed: 2026-02-18*
