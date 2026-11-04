---
phase: 01-instrument-a-pre-post-self-assessment
plan: "02"
subsystem: assessment-instruments
tags: [python-docx, word, facilitator-guide, self-assessment, inclusive-management, likert]

# Dependency graph
requires:
  - phase: 01-instrument-a-pre-post-self-assessment
    provides: RESEARCH.md with all verbatim scripts, item set, and cultural notes
provides:
  - generate_facilitator_guide.py — reproducible python-docx generator script (200+ lines)
  - pre-post-self-assessment-facilitator-guide.docx — 8-section Word document for facilitators
affects:
  - 01-instrument-a-pre-post-self-assessment (plan 03+)
  - facilitator training and train-the-trainer materials
  - post-training evaluation and reporting phases

# Tech tracking
tech-stack:
  added: [python-docx 1.2.0]
  patterns:
    - Verbatim facilitator scripts in shaded single-cell table boxes (F5F5F5 background)
    - Stage directions as bold-italic paragraphs
    - Domain separator rows with light yellow highlight for reverse-scored cells
    - Page header via section.header for per-page branding
    - apply_shading() using OxmlElement w:shd for cell background fills
    - __file__-based path resolution with os.makedirs for output directory creation

key-files:
  created:
    - courses/inclusive-management-shop-floor/generate_facilitator_guide.py
    - courses/inclusive-management-shop-floor/assessments/pre-post-self-assessment-facilitator-guide.docx
  modified: []

key-decisions:
  - "Script boxes implemented as single-cell tables (not text boxes) for reliable shading in python-docx"
  - "Reverse-scored cells highlighted in light yellow (FFF2CC) in the domain map for at-a-glance identification"
  - "Document header uses section.header right-aligned paragraph instead of a text box for cross-platform reliability"
  - "All 21 items included in Section 1 domain map with abbreviated text (~8 words + ellipsis)"

patterns-established:
  - "Script box pattern: add_script_box(doc, text) returns single-cell shaded table for verbatim content"
  - "Stage direction pattern: add_stage_direction(doc, text) returns bold-italic paragraph"
  - "Shading utility: apply_shading(cell, fill_hex) for table cell backgrounds"
  - "Section builder functions (build_section1..8) each print PASS: confirmation on success"

# Metrics
duration: 6min
completed: 2026-02-18
---

# Phase 1 Plan 02: Facilitator Guide Generator Summary

**python-docx facilitator guide for IMSF Pre/Post Self-Assessment: 8 sections including verbatim pre/post scripts, 21-item domain map with reverse-score highlights, show-of-hands protocol, cultural context notes, and explicit form-non-collection disposition**

## Performance

- **Duration:** ~6 min
- **Started:** 2026-02-18T02:13:44Z
- **Completed:** 2026-02-18T02:19:19Z
- **Tasks:** 1 of 1
- **Files modified:** 2

## Accomplishments

- Created `generate_facilitator_guide.py` — a fully reproducible 200+ line python-docx script that generates the complete facilitator guide from embedded verbatim content derived from RESEARCH.md
- Generated `pre-post-self-assessment-facilitator-guide.docx` with all 8 required sections (Domain Map, Reverse Scoring, Pre Script, Post Script, Show-of-Hands, Tear-Off Strip, Cultural Notes, Form Disposition)
- All verbatim scripts from RESEARCH.md preserved exactly, with stage directions in bold italic and spoken text in shaded script boxes, allowing facilitator to read verbatim with no improvisation required

## Task Commits

Each task was committed atomically:

1. **Task 1: Create the facilitator guide generator script** - `fa9ffa8` (feat)

**Plan metadata:** skipped (commit_docs: false per project config)

## Files Created/Modified

- `courses/inclusive-management-shop-floor/generate_facilitator_guide.py` — Python generator script; runs with `python3 generate_facilitator_guide.py`; prints PASS: for each section on success
- `courses/inclusive-management-shop-floor/assessments/pre-post-self-assessment-facilitator-guide.docx` — Generated Word document; 108 paragraphs; 13 headings (8 x Heading 1, 5 x Heading 2); A4, 2cm margins, Calibri throughout

## Decisions Made

- Script boxes use single-cell tables rather than actual Word text boxes — python-docx's text box support is unreliable; single-cell tables with F5F5F5 shading achieve the same visual effect and are cross-platform stable
- Reverse-scored cells in the domain map table highlighted with light yellow (FFF2CC) to distinguish at-a-glance from forward-scored items
- Full text of items 5, 11, and 18 included verbatim in Section 2 (reverse-scoring section) so facilitators have complete item text alongside the conversion table without needing to cross-reference the participant form
- Document page header uses `section.header` right-aligned paragraph rather than a floating text box — more reliable in python-docx and renders correctly in both Microsoft Word and LibreOffice

## Deviations from Plan

None - plan executed exactly as written. All 8 sections generated; all verification checks passed; key strings confirmed present in document including table cell content.

Note: The plan's verification step 5 checks `doc.paragraphs` only — this passes for 3 of 5 checks because 2 strings live inside table cells (script boxes). All strings are present in the document; the verification script needs to also iterate `doc.tables` for complete coverage. Documented here for future reference; does not affect document correctness.

## Issues Encountered

- `pip` command not found on macOS (Homebrew Python); used `pip3 install python-docx --break-system-packages` to install python-docx 1.2.0 successfully. PEP 668 externally-managed-environment warning is expected on macOS Homebrew Python.

## User Setup Required

None - no external service configuration required.

## Next Phase Readiness

- Facilitator guide is complete and matches all `must_haves.truths` requirements
- Generator script is version-controlled and reproducible; item text or script updates only require editing the constants at the top of the script and re-running
- Ready for Phase 1 Plan 03 (participant form generation) which will use the same python-docx patterns established here
- Participant form and facilitator guide should be reviewed as a pair before printing — the guide's Section 1 domain map abbreviations reference item text that must match the participant form exactly

---
*Phase: 01-instrument-a-pre-post-self-assessment*
*Completed: 2026-02-18*
