# Student Handout Generator - Architecture & Implementation Plan

**Version:** 1.0
**Date:** 2026-01-11
**Based on:** PRD-Student-Handout-Generator-v2.md

---

## Executive Summary

This document outlines the architecture and implementation strategy for the Student Handout Generation System, broken down into 12 user stories organized into 4 parallel execution waves.

### Goals
- Automate handout generation from framework markdown files
- AI-powered question generation with mandatory review
- Professional dark-themed PDF output
- Batch processing for entire courses

### Success Criteria
- Generate handouts for all 11 modules (M0-M10) of ML-for-Engineers
- Processing time: 2-5 minutes per module
- High-quality dark-themed PDF output
- 5-10 contextual questions per chapter

---

## System Architecture

### Component Overview

```
┌─────────────────────────────────────────────────────────┐
│                  CLI Interface                          │
│              (generate_handout.py)                      │
└────────────────────┬────────────────────────────────────┘
                     │
        ┌────────────┼────────────┐
        ▼            ▼            ▼
   ┌─────────┐  ┌─────────┐  ┌─────────┐
   │ Config  │  │  Batch  │  │ Question│
   │ Manager │  │Processor│  │Reviewer │
   └────┬────┘  └────┬────┘  └────┬────┘
        │            │            │
        └────────────┼────────────┘
                     │
        ┌────────────┼────────────┐
        ▼            ▼            ▼
   ┌─────────┐  ┌─────────┐  ┌─────────┐
   │Framework│  │ Content │  │Question │
   │ Parser  │  │Transform│  │Generator│
   └────┬────┘  └────┬────┘  └────┬────┘
        │            │            │
        └────────────┼────────────┘
                     │
        ┌────────────┼────────────┐
        ▼            ▼            ▼
   ┌─────────┐  ┌─────────┐  ┌─────────┐
   │  Image  │  │ Layout  │  │   PDF   │
   │Processor│  │ Engine  │  │Renderer │
   └─────────┘  └─────────┘  └─────────┘
```

### Data Flow

```
Framework MD → Parse → Transform → Generate Questions (AI)
                                           ↓
                                    Review (Manual)
                                           ↓
                        ← Approved Questions
                        ↓
              Combine: Content + Questions + Images
                        ↓
                  Layout (HTML + CSS)
                        ↓
                  Render PDF (WeasyPrint)
                        ↓
                  Dark-Themed Handout
```

---

## User Stories Breakdown

### Wave 1: Foundation (Stories 1-3)
**Execution: Parallel**
**Estimated Time: 6-8 hours**

#### Story 1: Foundation & Configuration
**Priority:** P0
**Components:** ConfigManager, Error Handler, Security, Logging

**Tasks:**
- [ ] Create project directory structure
- [ ] Set up Python package structure (src/)
- [ ] Implement ConfigManager (load/validate YAML)
- [ ] Create error handling framework
- [ ] Set up logging system
- [ ] Create data models (dataclasses)
- [ ] Security utilities (path validation, input sanitization)
- [ ] Create requirements.txt

**Files:**
- `src/__init__.py`
- `src/config_manager.py`
- `src/error_handler.py`
- `src/security.py`
- `src/models.py` (data models)
- `handout_config.yaml` (default config)
- `requirements.txt`

**Acceptance Criteria:**
- Config loads and validates against schema
- Logging to file and console works
- Error handling framework in place
- All data models defined

---

#### Story 2: Framework Parser
**Priority:** P0
**Components:** FrameworkParser

**Tasks:**
- [ ] Implement markdown file reader
- [ ] Parse YAML frontmatter for metadata
- [ ] Parse markdown structure (headings, sections)
- [ ] Extract content by section
- [ ] Handle code blocks, tables, lists
- [ ] Detect image references
- [ ] Output structured data (FrameworkMetadata, ContentSection)

**Files:**
- `src/framework_parser.py`
- `tests/test_framework_parser.py`

**Acceptance Criteria:**
- Parse framework files up to 5000 lines
- Extract all metadata correctly
- Preserve markdown formatting
- Handle UTF-8 encoding
- Return structured section hierarchy

---

#### Story 3: Content Transformer
**Priority:** P0
**Components:** ContentTransformer

**Tasks:**
- [ ] Implement content filtering (exclude instructor sections)
- [ ] Pattern matching for exclusion rules
- [ ] Section removal based on patterns
- [ ] Clean and normalize content
- [ ] Apply transformation rules from config
- [ ] Output cleaned markdown

**Files:**
- `src/content_transformer.py`
- `tests/test_content_transformer.py`

**Acceptance Criteria:**
- Remove "## Video Production Notes" sections
- Remove "### For Instructors" sections
- Remove content between `<!-- INSTRUCTOR ONLY -->` tags
- Preserve all student-facing content
- Configurable exclusion patterns

---

### Wave 2: Core Processing (Stories 4-7)
**Execution: Parallel**
**Estimated Time: 8-10 hours**

#### Story 4: Manual Question Bank Support
**Priority:** P0 (MVP Requirement)
**Components:** Question loading and placement

**Tasks:**
- [ ] Implement JSON question bank loader
- [ ] Validate question schema
- [ ] Question placement algorithm (insert after sections)
- [ ] Support all question types (MCQ, T/F, short answer, reflection, application)
- [ ] Question formatting for layout

**Files:**
- `src/question_loader.py`
- `tests/test_question_loader.py`
- `question_banks/approved/sample.json` (example)

**Acceptance Criteria:**
- Load questions from JSON files
- Validate against schema
- Place questions contextually in content
- Support all 5 question types
- Handle missing question banks gracefully

---

#### Story 5: Image Processor
**Priority:** P0
**Components:** ImageProcessor

**Tasks:**
- [ ] Detect image references in markdown
- [ ] Resolve image paths
- [ ] Validate image files exist
- [ ] Resize images (max 500px width)
- [ ] Optimize for dark backgrounds
- [ ] Generate placeholders for missing images
- [ ] Create ImageReference objects

**Files:**
- `src/image_processor.py`
- `tests/test_image_processor.py`
- `assets/placeholder.png` (generated)

**Acceptance Criteria:**
- Support PNG, JPG, SVG formats
- Auto-resize maintaining aspect ratio
- Create dark-themed placeholders (#21262D background)
- Handle missing images gracefully
- Output list of ImageReference objects

---

#### Story 6: Layout Engine
**Priority:** P0
**Components:** LayoutEngine, Jinja2 templates

**Tasks:**
- [ ] Create dark theme HTML template (Jinja2)
- [ ] Create dark theme CSS stylesheet
- [ ] Implement content assembly (content + questions + images)
- [ ] Generate table of contents with page numbers
- [ ] Handle pagination and page breaks
- [ ] Create question box templates (color-coded by type)
- [ ] Create code block templates with syntax highlighting
- [ ] Render final HTML

**Files:**
- `src/layout_engine.py`
- `templates/dark_theme.html`
- `templates/dark_theme.css`
- `templates/partials/question_box.html`
- `templates/partials/code_block.html`
- `tests/test_layout_engine.py`

**Acceptance Criteria:**
- HTML output with dark theme (#0D1117 background, #E6EDF3 text)
- Question boxes with colored left borders by type
- TOC with hyperlinks
- Headers/footers with page numbers
- Code blocks with syntax highlighting
- Proper pagination (avoid orphan headings)

---

#### Story 7: PDF Renderer
**Priority:** P0
**Components:** PDFRenderer, WeasyPrint integration

**Tasks:**
- [ ] Integrate WeasyPrint
- [ ] Apply CSS styling for dark theme
- [ ] Embed fonts (Inter, JetBrains Mono)
- [ ] Embed images
- [ ] Configure page setup (A4, margins)
- [ ] Generate headers/footers
- [ ] Validate PDF output
- [ ] Save PDF to output directory

**Files:**
- `src/pdf_renderer.py`
- `assets/fonts/Inter-Regular.ttf`
- `assets/fonts/Inter-Bold.ttf`
- `assets/fonts/JetBrainsMono-Regular.ttf`
- `tests/test_pdf_renderer.py`

**Acceptance Criteria:**
- Generate print-ready PDF
- Dark theme renders correctly
- Fonts embedded (portable)
- Images embedded
- Page size: A4 with 20-25mm margins
- File size < 10MB per handout

---

### Wave 3: AI & CLI (Stories 8-10)
**Execution: Parallel**
**Estimated Time: 10-12 hours**

#### Story 8: CLI - Single Module Generation
**Priority:** P0 (MVP Requirement)
**Components:** Command-line interface

**Tasks:**
- [ ] Create `generate_handout.py` CLI script
- [ ] Implement argument parsing (argparse)
- [ ] Orchestrate pipeline: parse → transform → layout → render
- [ ] Progress indicators
- [ ] Error handling and user feedback
- [ ] Dry-run mode
- [ ] Verbose logging mode
- [ ] Output path handling

**Files:**
- `generate_handout.py`
- `README.md` (usage instructions)

**CLI Arguments:**
```bash
--input / -i        # Path to framework markdown
--config            # Custom config file
--output / -o       # Output directory
--dry-run           # Validate without generating
--verbose / -v      # Verbose logging
--use-approved-questions  # Skip AI, use approved bank
--force-unreviewed  # Generate with unreviewed questions
```

**Acceptance Criteria:**
- Single command generates handout
- Clear progress indication
- Success/error messages
- Processing time < 5 minutes per module
- Help documentation (--help)

---

#### Story 9: AI Question Generator
**Priority:** P0
**Components:** QuestionGenerator, Claude API integration

**Tasks:**
- [ ] Integrate Anthropic Claude API
- [ ] Implement question generation prompts
- [ ] Generate questions by section
- [ ] Support all question types (MCQ, T/F, short answer, reflection, application)
- [ ] Implement retry logic with exponential backoff
- [ ] Save questions to staging files
- [ ] Handle API errors (rate limits, timeouts)
- [ ] API key management (environment variables)

**Files:**
- `src/question_generator.py`
- `src/ai_prompts.py` (prompt templates)
- `.env.example`
- `tests/test_question_generator.py`

**Acceptance Criteria:**
- Generate 5-10 questions per major section
- Questions saved to `question_banks/staging/{module_id}-staging.json`
- All questions marked `"status": "pending_review"`
- API errors handled gracefully (3 retries)
- API key from environment variable (ANTHROPIC_API_KEY)
- Questions align with learning outcomes

---

#### Story 10: Question Review Interface
**Priority:** P0
**Components:** QuestionReviewer, Rich terminal UI

**Tasks:**
- [ ] Create interactive terminal interface (rich library)
- [ ] Display questions with context
- [ ] Implement review actions: Approve, Edit, Reject, Skip
- [ ] Edit workflow for question text/options/answer
- [ ] Save approved questions to approved directory
- [ ] Save rejected questions to rejected directory
- [ ] Track review statistics
- [ ] Resume capability (skip questions remain pending)
- [ ] Summary report after review

**Files:**
- `src/question_reviewer.py`
- `tests/test_question_reviewer.py`

**CLI Command:**
```bash
python generate_handout.py --review-questions module-0
```

**Acceptance Criteria:**
- Interactive terminal UI with rich formatting
- Show question + type + options + source section + LO
- Actions: [A]pprove, [E]dit, [R]eject, [S]kip, [Q]uit
- Edit workflow allows modifying all fields
- Approved → `question_banks/approved/{module_id}.json`
- Rejected → `question_banks/rejected/{module_id}-rejected.json`
- Summary: "Reviewed 15: 12 approved, 2 edited, 1 rejected"
- Can resume interrupted sessions

---

### Wave 4: Batch & Testing (Stories 11-12)
**Execution: Parallel**
**Estimated Time: 8-10 hours**

#### Story 11: Batch Processor
**Priority:** P1
**Components:** BatchProcessor

**Tasks:**
- [ ] Discover framework files in course directory
- [ ] Check question review status for all modules
- [ ] Block generation if any questions pending review
- [ ] Process modules sequentially
- [ ] Progress indication (current module, ETA)
- [ ] Continue on individual failures (with error log)
- [ ] Summary report (successful/failed/blocked)
- [ ] Archive old versions

**Files:**
- `src/batch_processor.py`
- `tests/test_batch_processor.py`

**CLI Command:**
```bash
python generate_handout.py --batch --course ml-for-engineers
python generate_handout.py --batch --course ml-for-engineers --modules 0,1,2
python generate_handout.py --review-status --course ml-for-engineers
```

**Acceptance Criteria:**
- Batch process all 11 modules
- Check review status before processing
- List modules with pending reviews
- Progress bar with ETA
- Summary report
- Processing time < 30 minutes for full course
- Archive previous handouts in `/archive/`

---

#### Story 12: Testing & QA
**Priority:** P1
**Components:** Comprehensive test suite

**Tasks:**
- [ ] Unit tests for all components (80%+ coverage)
- [ ] Integration tests (full pipeline)
- [ ] Validation tests (PDF quality checks)
- [ ] Create test fixtures (sample framework files, images, questions)
- [ ] Mock Claude API for tests
- [ ] Test error handling (missing files, API failures, etc.)
- [ ] Performance tests (large framework files)
- [ ] Security tests (path traversal, input validation)

**Files:**
- `tests/test_*.py` (all test files)
- `tests/fixtures/` (test data)
- `tests/conftest.py` (pytest configuration)
- `.github/workflows/tests.yml` (optional CI)

**Test Coverage:**
- Framework parser: Parse errors, large files, malformed markdown
- Content transformer: Exclusion patterns, edge cases
- Question generator: API mocking, error handling
- Question reviewer: Status transitions, file operations
- Image processor: Missing images, large files, unsupported formats
- Layout engine: Complex content, edge cases
- PDF renderer: Font embedding, image embedding
- Batch processor: Mixed states, partial failures
- Security: Path validation, input sanitization
- Integration: End-to-end single module, batch processing

---

## Implementation Strategy

### Execution Waves

#### **Wave 1: Foundation** (Parallel Execution)
Launch 3 agents in parallel:
1. **Agent 1:** Story 1 (Foundation & Configuration)
2. **Agent 2:** Story 2 (Framework Parser)
3. **Agent 3:** Story 3 (Content Transformer)

**Dependencies:** None (all independent)

---

#### **Wave 2: Core Processing** (Parallel Execution)
Launch 4 agents in parallel:
1. **Agent 4:** Story 4 (Manual Question Bank)
2. **Agent 5:** Story 5 (Image Processor)
3. **Agent 6:** Story 6 (Layout Engine)
4. **Agent 7:** Story 7 (PDF Renderer)

**Dependencies:** Depends on Wave 1 completion (data models, config)

---

#### **Wave 3: AI & CLI** (Parallel Execution)
Launch 3 agents in parallel:
1. **Agent 8:** Story 8 (CLI Interface)
2. **Agent 9:** Story 9 (AI Question Generator)
3. **Agent 10:** Story 10 (Question Review Interface)

**Dependencies:** Depends on Wave 1 & 2 completion

---

#### **Wave 4: Batch & QA** (Parallel Execution)
Launch 2 agents in parallel:
1. **Agent 11:** Story 11 (Batch Processor)
2. **Agent 12:** Story 12 (Testing & QA)

**Dependencies:** Depends on all previous waves

---

## Technology Stack

### Core Dependencies
```txt
# Document Processing
mistune>=3.0.0
pypandoc>=1.12
markdown-it-py>=3.0.0

# PDF Generation
weasyprint>=60.0
Pillow>=10.0.0

# AI Integration
anthropic>=0.40.0

# Configuration & Templating
PyYAML>=6.0
Jinja2>=3.1.0
python-dotenv>=1.0.0

# Terminal UI
rich>=13.0.0

# Testing
pytest>=7.4.0
pytest-cov>=4.1.0
pytest-mock>=3.12.0

# Utilities
click>=8.1.0  # Alternative to argparse
