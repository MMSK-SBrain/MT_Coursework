# Product Requirements Document (PRD)
## Student Handout Generation System

**Version:** 2.0  
**Date:** 2026-01-11  
**Author:** Course Generator Team  
**Status:** Draft for Implementation  

---

## 1. Executive Summary

### 1.1 Overview
The Student Handout Generation System is an automated tool that transforms existing course framework markdown files into professional, student-ready PDF handouts. These handouts will include the original framework content, self-study questions, visual elements (images, diagrams), and consistent formatting suitable for distribution to learners.

### 1.2 Business Value
- **Efficiency:** Automate creation of student materials, reducing manual effort by 80%+
- **Consistency:** Ensure uniform formatting and quality across all course modules
- **Scalability:** Easily generate handouts for multiple courses and modules
- **Maintenance:** Single-source-of-truth approach allows easy updates to framework → handout pipeline

### 1.3 Success Criteria
- Generate handouts for all 11 modules (M0-M10) of ML-for-Engineers course
- Processing time: 2-5 minutes per module (on target hardware)
- PDF output quality: Print-ready, professional dark-themed formatting
- Question bank: 5-10 self-study questions per chapter/session
- Zero manual intervention required for regeneration after initial setup (except mandatory question review)

### 1.4 Target Hardware Baseline
- **Machine:** MacBook Pro M1, 16GB RAM
- **OS:** macOS 12+
- **Storage:** 1GB free space for tools + generated files

---

## 2. Problem Statement

### 2.1 Current State
- Course framework files exist as detailed markdown documents (~1000-1200 lines each)
- Framework files contain instructor-level detail, pedagogical notes, production guidelines
- No student-facing handout materials currently exist
- Manual creation of handouts is time-consuming and inconsistent

### 2.2 Pain Points
- **Time-intensive:** Creating handouts manually takes 3-4 hours per module
- **Inconsistency:** Manual creation leads to varying formats, styles, and quality
- **Maintenance burden:** Updates to frameworks require duplicate effort in handouts
- **Scalability:** Cannot efficiently support multiple courses or frequent updates
- **Missing elements:** Need to add questions, images, and student-appropriate context

### 2.3 Target Users
- **Primary:** Single user (course administrator) generating student materials on local machine
- **End beneficiaries:** Students receiving professional study materials

---

## 3. Goals & Objectives

### 3.1 Primary Goals
1. **Automate handout generation** from framework markdown files
2. **Integrate self-study questions** contextually throughout content (with mandatory review)
3. **Embed visual elements** (images, diagrams, charts) to enhance learning
4. **Produce professional PDF output** with dark minimalist styling suitable for printing and digital distribution

### 3.2 Secondary Goals
1. Support batch processing for all modules in a course
2. Enable customization of question types and density
3. Allow branding customization (logos, colors, fonts)
4. Generate table of contents, page numbers, headers/footers
5. Support multiple output formats (PDF primary, HTML optional)

### 3.3 Non-Goals (Out of Scope for v1.0)
- Interactive handouts with embedded videos/animations
- LMS integration or SCORM packaging
- Real-time collaborative editing of handouts
- Automated translation to multiple languages
- Student progress tracking within handouts
- Distribution or deployment to other machines
- Accessibility compliance (WCAG/PDF-UA)
- Multi-user support

---

## 4. Functional Requirements

### 4.1 Core Features

#### FR-1: Framework File Processing
**Priority:** P0 (Must Have)
- **Description:** System shall read and parse markdown framework files
- **Acceptance Criteria:**
  - Parse all markdown syntax (headers, lists, code blocks, tables)
  - Preserve formatting and structure
  - Handle files up to 5000 lines
  - Support UTF-8 encoding
  - Extract metadata (module number, title, duration, etc.)

#### FR-2: Content Transformation
**Priority:** P0 (Must Have)
- **Description:** Transform instructor-focused content to student-appropriate format
- **Acceptance Criteria:**
  - Remove instructor-only sections (production notes, pedagogy comments)
  - Preserve learning content, activities, and assessments
  - Convert technical jargon to student-friendly language (where flagged)
  - Maintain code examples, demo links, and resources

#### FR-3: Self-Study Question Generation
**Priority:** P0 (Must Have)
- **Description:** Automatically generate contextual self-study questions using AI
- **Acceptance Criteria:**
  - Generate 5-10 questions per major section/chapter
  - Support multiple question types:
    - Multiple choice
    - True/False
    - Short answer
    - Reflection prompts
    - Application scenarios
  - Questions should align with learning outcomes
  - Include space for student answers (blank lines or answer boxes)
  - AI-generated questions saved to staging file for review

#### FR-3a: Mandatory Question Review Workflow
**Priority:** P0 (Must Have)
- **Description:** AI-generated questions MUST be manually reviewed before inclusion in handouts
- **Acceptance Criteria:**
  - AI-generated questions saved to staging file: `question_banks/{module_id}-staging.json`
  - Staging file includes `"status": "pending_review"` flag on each question
  - CLI command to review questions: `python generate_handout.py --review-questions module-0`
  - Interactive terminal review interface showing:
    - Question text and type
    - Answer options (if applicable)
    - Suggested correct answer
    - Source section from framework
    - Learning outcome alignment
  - Review actions per question: **[A]pprove**, **[E]dit**, **[R]eject**, **[S]kip**
  - Approved questions moved to `question_banks/{module_id}.json` with `"status": "approved"`
  - Rejected questions logged to `question_banks/{module_id}-rejected.json` for reference
  - Handout generation **BLOCKS** if any questions have `"status": "pending_review"`
  - Override flag available: `--force-unreviewed` (generates with warning banner on handout)
  - Summary report after review session: approved/edited/rejected/skipped counts

#### FR-4: Image Integration
**Priority:** P0 (Must Have)
- **Description:** Embed images, diagrams, and visual aids into handouts
- **Acceptance Criteria:**
  - Support common image formats (PNG, JPG, SVG)
  - Auto-resize images to fit page width (max 500px for dark theme)
  - Add captions and figure numbers
  - Reference images from `/images/` subdirectories
  - Handle missing images gracefully (placeholder or skip with warning)
  - Maintain aspect ratios

#### FR-5: PDF Generation
**Priority:** P0 (Must Have)
- **Description:** Generate professional, print-ready PDF documents with dark minimalist styling
- **Acceptance Criteria:**
  - Dark theme with high-contrast text (#E6EDF3 on #0D1117)
  - Clean, readable typography (Inter font family)
  - Consistent page layout (margins: 20-25mm)
  - Automatic page breaks (avoid orphan headings)
  - Table of contents with page numbers
  - Headers with module/chapter titles (muted color)
  - Footers with page numbers (centered)
  - Hyperlinked TOC entries
  - Embedded fonts for portability
  - Code blocks with syntax highlighting (JetBrains Mono)
  - Question boxes with colored left border by type

#### FR-6: Batch Processing
**Priority:** P1 (Should Have)
- **Description:** Process multiple modules in a single operation
- **Acceptance Criteria:**
  - Accept directory path as input
  - Process all framework files in directory
  - Generate handouts for each module
  - Progress indication during batch processing
  - Summary report of successful/failed generations
  - Continue processing on individual failures (with error log)
  - Skip modules with unreviewed questions (list them in summary)

### 4.2 Configuration & Customization

#### FR-7: Question Configuration
**Priority:** P1 (Should Have)
- **Description:** Configurable question generation parameters
- **Acceptance Criteria:**
  - Config file (YAML) to specify:
    - Questions per section (default: 5-10)
    - Question types enabled
    - Question difficulty distribution
    - AI prompt templates for question generation
  - Override defaults per module if needed

#### FR-8: Styling & Branding
**Priority:** P1 (Should Have)
- **Description:** Customizable visual styling and branding
- **Acceptance Criteria:**
  - Config file for:
    - Logo image path
    - Color scheme (using dark theme palette)
    - Font family selections
    - Page size (A4, Letter, etc.)
    - Margin sizes
  - CSS-based styling for PDF generation
  - Template system for page layouts

#### FR-9: Content Filters
**Priority:** P2 (Nice to Have)
- **Description:** Rules to filter/transform specific content types
- **Acceptance Criteria:**
  - Define patterns to exclude (e.g., sections marked with specific tags)
  - Find-and-replace rules for terminology
  - Section reordering capabilities
  - Conditional inclusion based on metadata

### 4.3 Output & Distribution

#### FR-10: Multi-Format Output
**Priority:** P2 (Nice to Have)
- **Description:** Generate handouts in multiple formats beyond PDF
- **Acceptance Criteria:**
  - PDF (primary, P0)
  - HTML with dark styling (P2)
  - Markdown enhanced version (P2)

#### FR-11: Output Organization
**Priority:** P1 (Should Have)
- **Description:** Organized directory structure for generated handouts
- **Acceptance Criteria:**
  - Consistent naming convention: `{course-code}-module-{N}-handout.pdf`
  - Separate directories per course
  - Images bundled with handouts
  - Metadata files (JSON) with generation timestamps
  - Archive previous versions in `/archive/` subdirectory

---

## 5. Technical Requirements

### 5.1 Technology Stack

#### TR-1: Programming Language
**Requirement:** Python 3.11+
- **Rationale:** Rich ecosystem for document processing, AI integration, and PDF generation; native ARM support on M1
- **Libraries:**
  - `mistune` or `markdown-it-py`: Markdown parsing
  - `Pandoc` (via `pypandoc`): Document conversion
  - `WeasyPrint`: PDF generation with CSS styling
  - `Pillow`: Image processing
  - `PyYAML`: Configuration management
  - `Jinja2`: Templating for layouts
  - `anthropic`: AI question generation (Claude API)
  - `rich`: Terminal UI for question review interface

#### TR-2: External Dependencies
- **Pandoc:** Standalone installation required (`brew install pandoc`)
- **WeasyPrint dependencies:** `brew install pango gdk-pixbuf libffi`
- **Fonts:** Inter and JetBrains Mono (embedded in output)

#### TR-3: System Requirements
- **OS:** macOS 12+ (Apple Silicon optimized)
- **Hardware:** MacBook Pro M1, 16GB RAM
- **Storage:** 1GB free space for tools + generated files
- **Network:** Required for AI-powered question generation (Claude API)

### 5.2 Architecture Components

#### TR-4: Modular Design
System shall consist of independent, testable modules:

1. **FrameworkParser**
   - Reads markdown files
   - Extracts metadata
   - Parses structure (sections, chapters)
   - Outputs structured data (JSON/dict)

2. **ContentTransformer**
   - Filters instructor-only content
   - Applies transformation rules
   - Simplifies technical language (optional)
   - Outputs cleaned markdown

3. **QuestionGenerator**
   - Analyzes content sections
   - Generates contextual questions via Claude API
   - Saves to staging file for review
   - Supports manual question banks as fallback
   - Outputs question objects

4. **QuestionReviewer**
   - Interactive terminal interface (using `rich`)
   - Loads staging questions
   - Presents questions for approval/edit/reject
   - Saves approved questions to final bank
   - Tracks review statistics

5. **ImageProcessor**
   - Locates referenced images
   - Validates image files
   - Resizes and optimizes for dark background
   - Generates placeholders if missing
   - Outputs processed image references

6. **LayoutEngine**
   - Combines content + questions + images
   - Applies dark theme templates
   - Handles pagination
   - Generates intermediate format (HTML)

7. **PDFRenderer**
   - Converts HTML to PDF via WeasyPrint
   - Applies dark theme CSS styling
   - Embeds fonts and images
   - Validates output
   - Outputs final PDF file

8. **BatchProcessor**
   - Orchestrates pipeline for multiple files
   - Manages sequential processing
   - Handles errors and logging
   - Generates summary reports

9. **ConfigManager**
   - Loads configuration files
   - Validates settings against schema
   - Provides defaults
   - Merges global + module-specific configs

### 5.3 Data Flow

```
Framework Markdown Files
         ↓
   FrameworkParser → Structured Data
         ↓
   ContentTransformer → Cleaned Content
         ↓
   QuestionGenerator → Staging Questions (pending review)
         ↓
   QuestionReviewer → Approved Questions ← [MANUAL STEP]
         ↓
   ImageProcessor → Content + Questions + Images
         ↓
   LayoutEngine → Formatted Document (HTML)
         ↓
   PDFRenderer → Final PDF Handout
```

### 5.4 Configuration Schema

#### TR-5: Configuration File Structure
**File:** `handout_config.yaml`

```yaml
# Global Configuration
global:
  output_directory: "./handouts"
  archive_old_versions: true
  page_size: "A4"  # A4, Letter
  fonts:
    body: "Inter"
    heading: "Inter"
    code: "JetBrains Mono"

# Dark Theme Branding
branding:
  logo_path: "./assets/logo.png"
  theme: "dark"  # dark | light (dark is default)
  colors:
    # Background layers
    background_primary: "#0D1117"
    background_secondary: "#161B22"
    background_tertiary: "#21262D"
    # Text
    text_primary: "#E6EDF3"
    text_secondary: "#8B949E"
    text_muted: "#484F58"
    # Accents
    accent_blue: "#58A6FF"
    accent_green: "#3FB950"
    accent_orange: "#D29922"
    accent_red: "#F85149"
    accent_purple: "#A371F7"
    # Borders
    border_default: "#30363D"

# Question Generation
questions:
  enabled: true
  questions_per_section: 7
  require_review: true  # Cannot be disabled
  types:
    - multiple_choice
    - true_false
    - short_answer
    - reflection
    - application
  ai_generation:
    enabled: true
    provider: "anthropic"
    api_key_env_var: "ANTHROPIC_API_KEY"
    model: "claude-sonnet-4-20250514"
    max_retries: 3
    timeout_seconds: 60
  staging_directory: "./question_banks/staging"
  approved_directory: "./question_banks/approved"
  rejected_directory: "./question_banks/rejected"

# Content Transformation
content:
  exclude_patterns:
    - "## Video Production Notes"
    - "### For Instructors"
    - "<!-- INSTRUCTOR ONLY -->"
  include_toc: true
  include_learning_outcomes: true
  include_assessments: true

# Images
images:
  base_directory: "./images"
  max_width: 500  # pixels (optimized for dark theme)
  placeholder_on_missing: true
  placeholder_color: "#21262D"
  formats_supported:
    - png
    - jpg
    - jpeg
    - svg

# PDF Output
pdf:
  margins:
    top: 20mm
    bottom: 20mm
    left: 25mm
    right: 25mm
  header:
    enabled: true
    format: "{module_title}"
    color: "#8B949E"
  footer:
    enabled: true
    format: "Page {page_number}"
    color: "#484F58"
  page_break_before_sections: true

# Module-Specific Overrides (optional)
modules:
  module-0:
    questions:
      questions_per_section: 5  # Lighter for intro module
  module-10:
    questions:
      questions_per_section: 10  # More for capstone
```

---

## 6. Security Requirements

### 6.1 API Key Management

#### SR-1: Secrets Handling
**Priority:** P0 (Must Have)
- **Description:** Secure handling of AI API keys
- **Requirements:**
  - API keys stored in environment variables only (never in config files)
  - Config file references env var name: `api_key_env_var: "ANTHROPIC_API_KEY"`
  - System validates env var exists before attempting API calls
  - Clear error message if API key missing: "ANTHROPIC_API_KEY environment variable not set"
  - API key never logged or included in error messages
  - `.env` file support via `python-dotenv` (optional)
  - `.env` added to `.gitignore` template

### 6.2 Input Validation

#### SR-2: File Path Security
**Priority:** P1 (Should Have)
- **Description:** Prevent path traversal and malicious file access
- **Requirements:**
  - Validate all input file paths are within expected directories
  - Reject paths containing `..` or absolute paths outside project
  - Sanitize image paths from markdown before file system access
  - Log and reject files with suspicious patterns

#### SR-3: Markdown Sanitization
**Priority:** P1 (Should Have)
- **Description:** Safe processing of markdown content
- **Requirements:**
  - Strip or escape HTML tags in markdown (configurable)
  - Validate markdown structure before processing
  - Handle malformed markdown gracefully (log warning, continue)
  - Limit maximum file size processing (5MB default)

### 6.3 Output Safety

#### SR-4: Generated File Safety
**Priority:** P2 (Nice to Have)
- **Description:** Safe output file handling
- **Requirements:**
  - Validate output directory exists and is writable
  - Never overwrite files without archiving (if configured)
  - Use atomic writes (write to temp, then rename)
  - Set appropriate file permissions (owner read/write only)

---

## 7. Error Handling Specification

### 7.1 Error Categories

| Category | Severity | Behavior | Example |
|----------|----------|----------|---------|
| **Fatal** | Critical | Stop immediately, exit code 1 | Missing required config, API auth failure |
| **Blocking** | High | Stop current module, continue batch | Unreviewed questions, corrupted framework file |
| **Recoverable** | Medium | Log warning, use fallback, continue | Missing image (use placeholder), API timeout (retry) |
| **Informational** | Low | Log info, continue normally | Skipped empty section, unused config option |

### 7.2 Error Messages Format

All error messages follow this structure:
```
[SEVERITY] [MODULE] Error description
  → Context: Additional details
  → Action: What the system did or what user should do
```

Example:
```
[ERROR] [QuestionGenerator] API request failed after 3 retries
  → Context: Module 3, Section "Neural Networks Basics"
  → Action: Using cached questions from previous run. Review question_banks/module-3-staging.json
```

### 7.3 Specific Error Handling

#### Framework Parser Errors
| Error | Severity | Handling |
|-------|----------|----------|
| File not found | Fatal | Exit with clear path message |
| Invalid UTF-8 encoding | Fatal | Exit, suggest file encoding fix |
| Missing required metadata | Blocking | Skip module, log which fields missing |
| Malformed markdown | Recoverable | Log warning, attempt best-effort parse |
| File exceeds size limit | Blocking | Skip module, suggest splitting |

#### Question Generator Errors
| Error | Severity | Handling |
|-------|----------|----------|
| API key not set | Fatal | Exit with env var setup instructions |
| API authentication failed | Fatal | Exit with "check API key" message |
| API rate limited | Recoverable | Exponential backoff (3 retries), then use cached |
| API timeout | Recoverable | Retry up to 3 times, then use cached |
| Invalid API response | Recoverable | Log response, retry once, then skip section |
| Unreviewed questions exist | Blocking | Block generation, list pending modules |

#### Image Processor Errors
| Error | Severity | Handling |
|-------|----------|----------|
| Image not found | Recoverable | Use placeholder, log warning |
| Unsupported format | Recoverable | Skip image, log warning |
| Corrupted image file | Recoverable | Use placeholder, log warning |
| Image too large (>10MB) | Recoverable | Skip image, log warning |

#### PDF Renderer Errors
| Error | Severity | Handling |
|-------|----------|----------|
| WeasyPrint not installed | Fatal | Exit with install instructions |
| Font not found | Recoverable | Fall back to system font, log warning |
| Output directory not writable | Fatal | Exit with permissions message |
| PDF generation failed | Blocking | Skip module, log full error |

### 7.4 Logging Configuration

```yaml
logging:
  level: "INFO"  # DEBUG, INFO, WARNING, ERROR
  format: "[{timestamp}] [{level}] [{module}] {message}"
  file: "./logs/handout_generation.log"
  console: true
  max_file_size: "10MB"
  backup_count: 3
```

### 7.5 Exit Codes

| Code | Meaning |
|------|---------|
| 0 | Success (all modules generated) |
| 1 | Fatal error (system cannot proceed) |
| 2 | Partial success (some modules failed in batch) |
| 3 | Blocked by review (unreviewed questions) |
| 4 | Configuration error |

---

## 8. User Stories

### 8.1 Primary User Stories

**US-1: As a course administrator**, I want to generate a student handout from a framework file with a single command, so that I can quickly create distribution materials.

**Acceptance Criteria:**
- Run script: `python generate_handout.py --input frameworks/module-0-framework-REVISED.md`
- If questions need review: Prompted to run `--review-questions` first
- If questions approved: Output PDF handout in `handouts/module-0/` directory
- Processing time: 2-5 minutes
- Success confirmation message with output path

**US-2: As a course administrator**, I want to review AI-generated questions before they're included in handouts, so that I can ensure accuracy and quality.

**Acceptance Criteria:**
- Run script: `python generate_handout.py --review-questions module-0`
- Interactive terminal shows each question with context
- Can approve, edit, reject, or skip each question
- Approved questions automatically saved
- Summary shows counts: "Reviewed 15 questions: 12 approved, 2 edited, 1 rejected"
- Can resume review if interrupted (skipped questions remain pending)

**US-3: As a course administrator**, I want to batch-generate handouts for an entire course, so that I can produce all materials efficiently.

**Acceptance Criteria:**
- Run script: `python generate_handout.py --batch --course ml-for-engineers`
- System checks all modules for unreviewed questions first
- If any pending reviews: Lists modules, prompts to review first
- If all reviewed: Processes all 11 modules sequentially
- Progress indicator shows current module and ETA
- Summary report lists successful/failed generations
- Processing time: < 30 minutes for all modules

**US-4: As a course administrator**, I want handouts with a professional dark theme, so that they look modern and are easy to read.

**Acceptance Criteria:**
- PDF uses dark background (#0D1117) with light text (#E6EDF3)
- Question boxes have colored left borders by type
- Code blocks have syntax highlighting on dark background
- All text meets readability contrast standards
- Consistent styling throughout document

**US-5: As a course administrator**, I want images automatically embedded in handouts, so that visual learners have supporting diagrams.

**Acceptance Criteria:**
- Images referenced in framework markdown are detected
- Images from `images/` directory are embedded
- Images display at appropriate sizes (max 500px width)
- Missing images show dark placeholder with "Image not found" text
- Image captions appear below in muted color

### 8.2 Secondary User Stories

**US-6: As a course administrator**, I want to provide custom question banks for specific modules, so that I can skip AI generation when I have pre-written questions.

**Acceptance Criteria:**
- Create JSON file with custom questions in `question_banks/approved/`
- Mark questions with `"source": "manual"` 
- System uses manual questions instead of generating AI ones
- Manual questions skip review (already approved)
- Can mix manual and AI questions

**US-7: As a course administrator**, I want to exclude instructor-only content from student handouts, so that students see only relevant material.

**Acceptance Criteria:**
- Sections marked "For Instructors" are automatically removed
- Production notes, pedagogy comments excluded
- Content between `<!-- INSTRUCTOR ONLY -->` tags excluded
- Student-facing content remains intact
- Configurable exclusion patterns in YAML

**US-8: As a course administrator**, I want to regenerate handouts quickly when only content changed (not questions), so that I don't re-review unchanged questions.

**Acceptance Criteria:**
- Flag: `--use-approved-questions` skips AI generation
- Uses existing approved question bank
- Only regenerates PDF from current content + existing questions
- Processing time: < 30 seconds per module

---

## 9. System Architecture

### 9.1 High-Level Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     Command Line Interface                   │
│                    (generate_handout.py)                     │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ├─ Config Loader (handout_config.yaml)
                       │
┌──────────────────────▼──────────────────────────────────────┐
│                    Batch Processor                           │
│  - Discovers framework files                                 │
│  - Checks question review status                             │
│  - Orchestrates pipeline                                     │
│  - Handles errors & logging                                  │
└──────────────────────┬──────────────────────────────────────┘
                       │
       ┌───────────────┼───────────────┐
       │               │               │
       ▼               ▼               ▼
┌─────────────┐ ┌─────────────┐ ┌─────────────┐
│  Framework  │ │   Content   │ │  Question   │
│   Parser    │ │ Transformer │ │  Generator  │
└──────┬──────┘ └──────┬──────┘ └──────┬──────┘
       │               │               │
       └───────────────┼───────────────┘
                       │
                       ▼
              ┌────────────────┐
              │    Question    │  ← [MANUAL REVIEW GATE]
              │    Reviewer    │
              └────────┬───────┘
                       │
                       ▼
              ┌────────────────┐
              │     Image      │
              │   Processor    │
              └────────┬───────┘
                       │
                       ▼
              ┌────────────────┐
              │     Layout     │
              │     Engine     │
              └────────┬───────┘
                       │
                       ▼
              ┌────────────────┐
              │      PDF       │
              │    Renderer    │
              └────────┬───────┘
                       │
                       ▼
              ┌────────────────┐
              │ Student Handout│
              │   (PDF File)   │
              └────────────────┘
```

### 9.2 Directory Structure

```
Course_Generator/
├── generate_handout.py              # Main CLI script
├── handout_config.yaml              # Global configuration
├── requirements.txt                 # Python dependencies
├── README.md                        # Usage documentation
├── .env.example                     # Example environment variables
├── .gitignore                       # Includes .env, logs/, etc.
│
├── src/                             # Source code
│   ├── __init__.py
│   ├── framework_parser.py
│   ├── content_transformer.py
│   ├── question_generator.py
│   ├── question_reviewer.py         # NEW: Interactive review UI
│   ├── image_processor.py
│   ├── layout_engine.py
│   ├── pdf_renderer.py
│   ├── batch_processor.py
│   ├── config_manager.py
│   ├── error_handler.py             # NEW: Centralized error handling
│   └── security.py                  # NEW: Input validation utilities
│
├── templates/                       # Layout templates
│   ├── dark_theme.html              # Main dark theme template
│   ├── dark_theme.css               # Dark theme styles
│   └── question_box.html            # Question box partial
│
├── assets/                          # Branding assets
│   ├── logo.png
│   └── fonts/
│       ├── Inter-Regular.ttf
│       ├── Inter-Bold.ttf
│       └── JetBrainsMono-Regular.ttf
│
├── question_banks/                  # Question repositories
│   ├── staging/                     # AI-generated, pending review
│   │   ├── module-0-staging.json
│   │   └── ...
│   ├── approved/                    # Reviewed and approved
│   │   ├── module-0.json
│   │   └── ...
│   └── rejected/                    # Rejected questions (for reference)
│       └── module-0-rejected.json
│
├── courses/                         # Input course frameworks
│   └── ml-for-engineers/
│       ├── frameworks/              # Source framework files
│       │   ├── module-0-framework-REVISED.md
│       │   ├── module-1-framework-REVISED.md
│       │   └── ...
│       ├── handouts/                # Generated handouts (output)
│       │   ├── module-0/
│       │   │   ├── ML-ENG-module-0-handout.pdf
│       │   │   └── metadata.json
│       │   └── archive/             # Previous versions
│       └── images/                  # Source images
│           ├── module-0/
│           ├── module-1/
│           └── shared/
│
├── tests/                           # Unit and integration tests
│   ├── test_framework_parser.py
│   ├── test_content_transformer.py
│   ├── test_question_generator.py
│   ├── test_question_reviewer.py
│   ├── test_security.py
│   └── fixtures/                    # Test data
│       ├── sample_framework.md
│       └── sample_questions.json
│
└── logs/                            # Processing logs
    └── handout_generation.log
```

---

## 10. Data Models

### 10.1 Framework Metadata

```python
@dataclass
class FrameworkMetadata:
    course_code: str           # e.g., "ML-ENG-M0"
    module_number: int         # e.g., 0
    module_title: str          # e.g., "The Hook - Welcome to Machine Learning"
    duration: str              # e.g., "1 week (self-paced)"
    video_content: str         # e.g., "~4.5 hours"
    hands_on_time: str         # e.g., "~2-3 hours"
    theory_practice_ratio: str # e.g., "70% / 30%"
    file_path: Path            # Original framework file path
    last_updated: datetime     # From file or metadata
```

### 10.2 Content Section

```python
@dataclass
class ContentSection:
    id: str                    # Unique identifier
    level: int                 # Header level (1-6)
    title: str                 # Section title
    content: str               # Markdown content
    subsections: list['ContentSection']  # Nested sections
    metadata: dict[str, Any]   # Additional metadata
    include_in_handout: bool   # Filter flag
    question_count: int        # Number of questions to add
```

### 10.3 Question Object

```python
@dataclass
class Question:
    id: str                    # Unique identifier (e.g., "m0-s1-q1")
    type: QuestionType         # Enum: MULTIPLE_CHOICE, TRUE_FALSE, SHORT_ANSWER, REFLECTION, APPLICATION
    question_text: str         # The question
    options: list[str] | None  # For MCQ/T-F
    correct_answer: str | None # For auto-graded questions
    explanation: str | None    # Answer explanation
    points: int                # Score value
    difficulty: str            # "easy", "medium", "hard"
    learning_outcome: str | None  # Associated LO
    source_section: str        # Section ID this relates to
    source: str                # "ai_generated" or "manual"
    status: str                # "pending_review", "approved", "rejected"
    reviewed_at: datetime | None  # When reviewed
    reviewer_notes: str | None # Notes from review
```

### 10.4 Image Reference

```python
@dataclass
class ImageReference:
    id: str                    # Unique identifier
    original_path: str         # Path in markdown
    resolved_path: Path | None # Actual file path (None if missing)
    alt_text: str              # Image description
    caption: str | None        # Figure caption
    width: int                 # Display width (pixels)
    height: int                # Display height (pixels)
    exists: bool               # File found flag
    placeholder_used: bool     # If placeholder was substituted
```

### 10.5 Handout Document

```python
@dataclass
class HandoutDocument:
    metadata: FrameworkMetadata
    sections: list[ContentSection]
    questions: list[Question]
    images: list[ImageReference]
    toc: list[TOCEntry]
    generation_timestamp: datetime
    config_used: dict[str, Any]
    output_path: Path
    warnings: list[str]        # Non-fatal issues during generation
    question_review_complete: bool
```

### 10.6 Question Review Session

```python
@dataclass
class ReviewSession:
    module_id: str
    started_at: datetime
    completed_at: datetime | None
    questions_total: int
    questions_approved: int
    questions_edited: int
    questions_rejected: int
    questions_skipped: int
```

---

## 11. API Specifications

### 11.1 Command Line Interface

#### Basic Usage
```bash
# Generate single handout (will prompt if questions need review)
python generate_handout.py --input frameworks/module-0-framework-REVISED.md

# Review AI-generated questions (required before first generation)
python generate_handout.py --review-questions module-0

# Generate using already-approved questions (skip AI generation)
python generate_handout.py --input frameworks/module-0-framework-REVISED.md \
                           --use-approved-questions

# Force generation with unreviewed questions (adds warning banner)
python generate_handout.py --input frameworks/module-0-framework-REVISED.md \
                           --force-unreviewed

# Batch process entire course
python generate_handout.py --batch --course ml-for-engineers

# Batch with specific modules only
python generate_handout.py --batch --course ml-for-engineers --modules 0,1,2

# Generate with custom config
python generate_handout.py --input frameworks/module-0-framework-REVISED.md \
                           --config custom_config.yaml

# Specify output directory
python generate_handout.py --input frameworks/module-0-framework-REVISED.md \
                           --output ./custom_output/

# Generate multiple formats
python generate_handout.py --input frameworks/module-0-framework-REVISED.md \
                           --formats pdf,html

# Dry run (validate without generating)
python generate_handout.py --input frameworks/module-0-framework-REVISED.md \
                           --dry-run

# Verbose logging
python generate_handout.py --input frameworks/module-0-framework-REVISED.md \
                           --verbose

# Check review status for all modules
python generate_handout.py --review-status --course ml-for-engineers
```

#### CLI Arguments

| Argument | Short | Type | Required | Default | Description |
|----------|-------|------|----------|---------|-------------|
| `--input` | `-i` | str | Yes* | - | Path to framework markdown file |
| `--batch` | `-b` | flag | No | False | Batch process all modules in course |
| `--course` | `-c` | str | Yes** | - | Course name for batch processing |
| `--modules` | `-m` | str | No | all | Comma-separated module numbers for batch |
| `--config` | - | str | No | `handout_config.yaml` | Path to config file |
| `--output` | `-o` | str | No | `./handouts` | Output directory |
| `--formats` | `-f` | str | No | `pdf` | Comma-separated: pdf,html |
| `--dry-run` | - | flag | No | False | Validate without generating |
| `--verbose` | `-v` | flag | No | False | Enable verbose logging |
| `--review-questions` | - | str | No | - | Module ID to review questions for |
| `--review-status` | - | flag | No | False | Show review status for all modules |
| `--use-approved-questions` | - | flag | No | False | Skip AI generation, use approved bank |
| `--force-unreviewed` | - | flag | No | False | Generate with unreviewed questions (adds warning) |
| `--regenerate-questions` | - | flag | No | False | Re-generate AI questions (overwrites staging) |

*Required unless `--batch`, `--review-questions`, or `--review-status` is used
**Required when `--batch` or `--review-status` is used

### 11.2 Python API

```python
from handout_generator import HandoutGenerator, Config, QuestionReviewer

# Initialize generator with config
config = Config.from_file("handout_config.yaml")
generator = HandoutGenerator(config)

# Check if questions need review
status = generator.get_review_status("module-0")
print(f"Pending: {status.pending}, Approved: {status.approved}")

# Review questions interactively
reviewer = QuestionReviewer(config)
session = reviewer.start_session("module-0")
# ... interactive review happens ...
print(f"Session complete: {session.questions_approved} approved")

# Generate single handout (after review)
handout = generator.generate(
    input_path="frameworks/module-0-framework-REVISED.md",
    output_format="pdf"
)

# Access generated document
print(f"Generated: {handout.output_path}")
print(f"Questions: {len(handout.questions)}")
print(f"Warnings: {handout.warnings}")

# Batch processing
results = generator.batch_generate(
    course_name="ml-for-engineers",
    output_formats=["pdf"]
)

# Check results
for module, result in results.items():
    if result.success:
        print(f"✓ {module}: {result.output_path}")
    elif result.blocked_by_review:
        print(f"⏸ {module}: Needs question review")
    else:
        print(f"✗ {module}: {result.error}")
```

### 11.3 Question Review Interface

When running `--review-questions module-0`, the terminal displays:

```
╭──────────────────────────────────────────────────────────────────╮
│  Question Review: Module 0 - The Hook                            │
│  Progress: 3/15 questions                                        │
╰──────────────────────────────────────────────────────────────────╯

Question 3 of 15                                    [Multiple Choice]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  What is the primary advantage of using Google Colab for ML?

    A) It has the best code editor
    B) Free GPU access in the cloud
    C) Required for Python programming
    D) Faster than all local setups

  Suggested Answer: B
  Difficulty: easy

────────────────────────────────────────────────────────────────────
Source Section: Session 3 - GPU Introduction
Learning Outcome: Understand cloud computing benefits for ML
────────────────────────────────────────────────────────────────────

  [A] Approve    [E] Edit    [R] Reject    [S] Skip    [Q] Quit

  Your choice: _
```

After editing (if chosen):
```
  Edit Question Text (or press Enter to keep):
  > What is the PRIMARY benefit of Google Colab for beginners?

  Edit Options (comma-separated, or Enter to keep):
  > 

  Edit Correct Answer (A/B/C/D, or Enter to keep):
  > 

  Add Review Note (optional):
  > Clarified "primary benefit" for beginners

  ✓ Question updated and approved
```

---

## 12. Question Generation Specification

### 12.1 Question Types

#### Multiple Choice
```json
{
  "id": "m0-s3-q1",
  "type": "multiple_choice",
  "question_text": "What is Google Colab?",
  "options": [
    "A graphics editing tool",
    "A cloud-based Jupyter notebook with free GPU",
    "A Google Meet alternative",
    "A data storage service"
  ],
  "correct_answer": "B",
  "explanation": "Google Colab provides free cloud-based Jupyter notebooks with GPU access, making it ideal for ML learning.",
  "difficulty": "easy",
  "points": 1,
  "source_section": "session-3-gpu-intro",
  "source": "ai_generated",
  "status": "pending_review"
}
```

#### True/False
```json
{
  "id": "m0-s2-q1",
  "type": "true_false",
  "question_text": "You need to install Python before using Colab.",
  "options": ["True", "False"],
  "correct_answer": "False",
  "explanation": "Colab runs entirely in the browser with Python pre-installed.",
  "difficulty": "easy",
  "points": 1,
  "source_section": "session-2-setup",
  "source": "ai_generated",
  "status": "pending_review"
}
```

#### Short Answer
```json
{
  "id": "m0-s3-q2",
  "type": "short_answer",
  "question_text": "Name 3 Python libraries that are pre-installed in Google Colab.",
  "correct_answer": "pandas, numpy, scikit-learn (or matplotlib, tensorflow, etc.)",
  "explanation": "Colab comes with most popular data science libraries pre-installed.",
  "difficulty": "medium",
  "points": 2,
  "source_section": "session-3-gpu-intro",
  "source": "ai_generated",
  "status": "pending_review"
}
```

#### Reflection
```json
{
  "id": "m0-s1-q1",
  "type": "reflection",
  "question_text": "Which of the 5 ML demos (stock predictor, cricket predictor, face detection, sentiment analyzer, chatbot) relates most to your industry or interests? Why?",
  "correct_answer": null,
  "explanation": "There is no single correct answer. Reflect on your own context and interests.",
  "difficulty": "easy",
  "points": 2,
  "source_section": "session-1-demos",
  "source": "ai_generated",
  "status": "pending_review"
}
```

#### Application Scenario
```json
{
  "id": "m0-s3-q3",
  "type": "application",
  "question_text": "You need to train a complex deep learning model on a large dataset. Your laptop has only a CPU. What are three solutions you learned in this module to address this problem?",
  "correct_answer": "1) Use Google Colab with free GPU, 2) Enable GPU runtime in Colab settings, 3) Use cloud computing services like AWS/GCP with GPU instances",
  "explanation": "This module introduced cloud-based solutions for GPU access.",
  "difficulty": "medium",
  "points": 3,
  "source_section": "session-3-gpu-intro",
  "source": "ai_generated",
  "status": "pending_review"
}
```

### 12.2 Question Placement Rules

- **After major sections:** Insert questions after H2 (##) sections
- **Session completion:** Add comprehensive questions at end of each session
- **Module conclusion:** Include cumulative questions at module end
- **Frequency:** Average 1 question per 150-200 lines of content
- **Visual separation:** Questions in styled boxes with colored left border
- **Grouping:** Questions grouped in "Self-Study Check" boxes (3-5 questions per box)

### 12.3 AI Prompt Templates

#### System Prompt for Question Generation
```
You are an expert instructional designer creating self-study questions for a machine learning course.

Your role is to generate high-quality assessment questions that:
1. Test genuine understanding, not just memorization
2. Are appropriate for beginners (clear language, minimal jargon)
3. Align with stated learning outcomes
4. Include helpful explanations for answers
5. Cover different cognitive levels (recall, understanding, application)

Always output valid JSON matching the specified schema.
```

#### Question Generation Prompt
```
Context:
- Course: {course_name}
- Module: {module_title}
- Section: {section_title}
- Learning Outcome: {learning_outcome}
- Target Audience: Beginner-level engineering students with no prior ML experience

Content to assess:
---
{section_content}
---

Task:
Generate {question_count} questions with the following distribution:
- {mcq_count} multiple choice (4 options each)
- {tf_count} true/false
- {short_count} short answer
- {reflection_count} reflection

Requirements:
1. Each multiple choice question must have plausible distractors
2. Include explanations that teach, not just confirm correctness
3. Vary difficulty: 40% easy, 40% medium, 20% hard
4. Questions should be self-contained (student can answer without re-reading)
5. Avoid trick questions or ambiguous wording

Output format: JSON array of question objects matching this schema:
{schema}
```

---

## 13. Dark Theme Design Specification

### 13.1 Color Palette

```yaml
# Primary backgrounds (darkest to lightest)
background:
  primary: "#0D1117"      # Main page background
  secondary: "#161B22"    # Content boxes, question boxes
  tertiary: "#21262D"     # Code blocks, highlights

# Text colors (highest to lowest contrast)
text:
  primary: "#E6EDF3"      # Main body text (high contrast)
  secondary: "#8B949E"    # Subdued text, captions, headers
  muted: "#484F58"        # Footer, metadata, timestamps

# Accent colors (functional)
accent:
  blue: "#58A6FF"         # Links, MCQ questions, primary actions
  green: "#3FB950"        # Success, correct answers, application questions
  orange: "#D29922"       # Warnings, important notes
  red: "#F85149"          # Errors, critical info
  purple: "#A371F7"       # Reflection questions

# Question box borders by type
question_borders:
  multiple_choice: "#58A6FF"   # Blue
  true_false: "#58A6FF"        # Blue
  short_answer: "#3FB950"      # Green
  reflection: "#A371F7"        # Purple
  application: "#3FB950"       # Green

# Borders
border:
  default: "#30363D"      # Subtle borders
  emphasis: "#8B949E"     # Emphasized borders

# Code syntax highlighting (GitHub Dark theme)
syntax:
  keyword: "#FF7B72"      # Red
  string: "#A5D6FF"       # Light blue
  comment: "#8B949E"      # Gray
  function: "#D2A8FF"     # Purple
  number: "#79C0FF"       # Blue
  operator: "#FF7B72"     # Red
```

### 13.2 Typography

```yaml
fonts:
  heading: "Inter"
  body: "Inter"
  code: "JetBrains Mono"

sizes:
  h1: "28pt"              # Module title
  h2: "22pt"              # Session titles
  h3: "16pt"              # Subsections
  h4: "14pt"              # Minor headings
  body: "11pt"            # Main content
  code: "10pt"            # Code blocks
  caption: "9pt"          # Image captions, footer
  question_label: "10pt"  # "Q1", "Multiple Choice" labels

weights:
  heading: 600            # Semi-bold
  body: 400               # Regular
  emphasis: 600           # Semi-bold
  code: 400               # Regular

line_height:
  body: 1.6
  heading: 1.3
  code: 1.4

paragraph_spacing: "12pt"
```

### 13.3 Layout Specifications

```yaml
page:
  size: "A4"              # 210mm × 297mm
  orientation: "portrait"

margins:
  top: "20mm"
  bottom: "20mm"
  left: "25mm"
  right: "25mm"

content_width: "160mm"    # 210 - 25 - 25

header:
  height: "12mm"
  content: "{module_title}"
  font_size: "10pt"
  color: "#8B949E"
  border_bottom: "1px solid #30363D"
  margin_bottom: "8mm"

footer:
  height: "10mm"
  content: "Page {page_number}"
  font_size: "9pt"
  color: "#484F58"
  alignment: "center"
  margin_top: "8mm"

images:
  max_width: "500px"
  alignment: "center"
  caption_margin_top: "8px"
  caption_color: "#8B949E"
  border_radius: "4px"
  placeholder_bg: "#21262D"
```

### 13.4 Component Styles

#### Question Box
```css
.question-box {
  background: #161B22;
  border-left: 3px solid #58A6FF;  /* Varies by question type */
  border-radius: 6px;
  padding: 16px 20px;
  margin: 24px 0;
  page-break-inside: avoid;
}

.question-box-header {
  display: flex;
  justify-content: space-between;
  margin-bottom: 12px;
}

.question-number {
  background: #58A6FF;
  color: #0D1117;
  padding: 2px 8px;
  border-radius: 4px;
  font-size: 10pt;
  font-weight: 600;
}

.question-type {
  color: #8B949E;
  font-size: 9pt;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.question-text {
  color: #E6EDF3;
  font-size: 11pt;
  line-height: 1.6;
  margin-bottom: 12px;
}

.question-options {
  margin-left: 20px;
}

.question-option {
  color: #E6EDF3;
  padding: 4px 0;
}

.answer-space {
  border-bottom: 1px solid #30363D;
  margin-top: 16px;
  padding-bottom: 40px;
}

/* Type-specific borders */
.question-box.reflection {
  border-left-color: #A371F7;
}

.question-box.application,
.question-box.short_answer {
  border-left-color: #3FB950;
}
```

#### Code Block
```css
.code-block {
  background: #161B22;
  border: 1px solid #30363D;
  border-radius: 6px;
  padding: 16px;
  font-family: "JetBrains Mono", monospace;
  font-size: 10pt;
  line-height: 1.4;
  overflow-x: auto;
  margin: 16px 0;
}

.code-block code {
  color: #E6EDF3;
}

/* Syntax highlighting */
.code-block .keyword { color: #FF7B72; }
.code-block .string { color: #A5D6FF; }
.code-block .comment { color: #8B949E; }
.code-block .function { color: #D2A8FF; }
.code-block .number { color: #79C0FF; }
```

#### Table of Contents
```css
.toc {
  background: #161B22;
  border-radius: 6px;
  padding: 20px 24px;
  margin: 24px 0;
}

.toc-title {
  color: #E6EDF3;
  font-size: 16pt;
  font-weight: 600;
  margin-bottom: 16px;
  padding-bottom: 8px;
  border-bottom: 1px solid #30363D;
}

.toc-item {
  color: #58A6FF;
  padding: 4px 0;
  text-decoration: none;
}

.toc-item:hover {
  text-decoration: underline;
}

.toc-page {
  color: #8B949E;
  float: right;
}
```

#### Important Note Box
```css
.note-box {
  background: #161B22;
  border-left: 3px solid #D29922;
  border-radius: 6px;
  padding: 12px 16px;
  margin: 16px 0;
}

.note-box.warning {
  border-left-color: #F85149;
}

.note-label {
  color: #D29922;
  font-size: 10pt;
  font-weight: 600;
  text-transform: uppercase;
  margin-bottom: 4px;
}
```

### 13.5 Visual Layout Example

```
┌─────────────────────────────────────────────────────────────────┐
│ Module 3: Neural Networks                           #8B949E     │ ← Header
│─────────────────────────────────────────────────────────────────│
│ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  #0D1117 bg  │
│                                                                 │
│   Session 1: Introduction to Neural Networks                    │ ← H2 #E6EDF3
│   ──────────────────────────────────────────                    │
│                                                                 │
│   Body text in Inter 11pt. Clean and readable with              │ ← Body #E6EDF3
│   1.6 line height. Links appear in blue (#58A6FF).              │
│                                                                 │
│   ┌─────────────────────────────────────────────────────────┐   │
│   │ ▌ import tensorflow as tf                    #161B22   │   │ ← Code block
│   │ ▌ model = tf.keras.Sequential()                        │   │
│   │ ▌ model.add(tf.keras.layers.Dense(10))                 │   │
│   └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│   ┌─────────────────────────────────────────────────────────┐   │
│   │▐ Q1                                    Multiple Choice │   │ ← Question box
│   │▐                                               #161B22 │   │
│   │▐ What is a neural network?                             │   │
│   │▐                                                       │   │
│   │▐   ○ A) A type of database                             │   │
│   │▐   ○ B) A machine learning model inspired by the brain │   │
│   │▐   ○ C) A programming language                         │   │
│   │▐   ○ D) A cloud computing service                      │   │
│   │▐                                                       │   │
│   │▐ Your answer: _______________________________          │   │
│   └─┴───────────────────────────────────────────────────────┘   │
│     ↑ Blue border (#58A6FF)                                     │
│                                                                 │
│   ┌─────────────────────────────────────────────────────────┐   │
│   │▐ Q2                                         Reflection │   │ ← Purple border
│   │▐                                                       │   │
│   │▐ How might neural networks apply to your industry?     │   │
│   │▐                                                       │   │
│   │▐ ________________________________________________      │   │
│   │▐ ________________________________________________      │   │
│   │▐ ________________________________________________      │   │
│   └─┴───────────────────────────────────────────────────────┘   │
│     ↑ Purple border (#A371F7)                                   │
│                                                                 │
│─────────────────────────────────────────────────────────────────│
│                           Page 12                       #484F58 │ ← Footer
└─────────────────────────────────────────────────────────────────┘
```

---

## 14. Implementation Phases

### Phase 1: MVP (Minimum Viable Product) - Week 1-2

**Goal:** Basic end-to-end pipeline working for a single module

**Deliverables:**
- [ ] Framework parser (reads markdown, extracts metadata)
- [ ] Basic content transformer (removes instructor sections)
- [ ] Manual question bank support (from JSON files)
- [ ] Image detection and basic embedding
- [ ] PDF generation with dark theme using WeasyPrint
- [ ] CLI to process single framework file
- [ ] Generated handout for Module 0 as proof-of-concept

**Success Criteria:**
- Can generate PDF handout for Module 0
- Questions from JSON bank appear in appropriate locations
- At least 2-3 images embedded
- PDF has dark theme and is readable
- Processing time < 5 minutes

**Estimated Effort:** 25-35 hours

---

### Phase 2: AI Questions & Review - Week 3-4

**Goal:** AI-powered question generation with mandatory review workflow

**Deliverables:**
- [ ] Claude API integration for question generation
- [ ] Question staging file system
- [ ] Interactive terminal review interface (using `rich`)
- [ ] Review status tracking per module
- [ ] Handout generation blocking on unreviewed questions
- [ ] Question type variety (MCQ, T/F, short answer, reflection, application)
- [ ] Error handling for API failures (retry, fallback)

**Success Criteria:**
- AI generates contextually relevant questions
- Review interface is intuitive and fast
- Can approve/edit/reject questions efficiently
- Approved questions persist correctly
- Generation blocked until review complete

**Estimated Effort:** 30-40 hours

---

### Phase 3: Batch & Polish - Week 5-6

**Goal:** Batch processing and production-quality output

**Deliverables:**
- [ ] Batch processor for all modules in a course
- [ ] Configuration system (YAML-based) with validation
- [ ] Improved layout templates (TOC, headers, footers)
- [ ] Image optimization and placeholder handling
- [ ] Comprehensive error handling and logging
- [ ] Security input validation
- [ ] Generate handouts for all 11 ML-for-Engineers modules

**Success Criteria:**
- Batch generate all 11 modules successfully
- Consistent dark theme formatting across all handouts
- Processing time < 30 minutes for full course
- Configuration changes work without code edits
- Clear error messages for any failures

**Estimated Effort:** 25-35 hours

---

### Phase 4: Documentation & Testing - Week 7

**Goal:** Complete documentation and test coverage

**Deliverables:**
- [ ] Comprehensive README with quick start guide
- [ ] Configuration reference documentation
- [ ] Unit tests for all modules (80%+ coverage)
- [ ] Integration tests for full pipeline
- [ ] Sample question banks and configuration examples

**Success Criteria:**
- New user can set up and generate first handout in < 30 minutes
- All tests pass
- Documentation covers all CLI commands and config options

**Estimated Effort:** 15-20 hours

---

## 15. Dependencies & Constraints

### 15.1 Technical Dependencies

| Dependency | Version | Purpose | Installation |
|------------|---------|---------|--------------|
| Python | 3.11+ | Runtime environment | System (pre-installed on macOS) |
| Pandoc | 3.0+ | Document conversion | `brew install pandoc` |
| WeasyPrint | 60+ | PDF rendering | `pip install weasyprint` |
| PyYAML | 6.0+ | Config parsing | `pip install pyyaml` |
| Jinja2 | 3.1+ | Templating | `pip install jinja2` |
| Pillow | 10.0+ | Image processing | `pip install pillow` |
| mistune | 3.0+ | Markdown parsing | `pip install mistune` |
| anthropic | 0.40+ | AI question generation | `pip install anthropic` |
| rich | 13.0+ | Terminal UI | `pip install rich` |
| python-dotenv | 1.0+ | Environment variables | `pip install python-dotenv` |

### 15.2 System Dependencies (Homebrew)

```bash
# Install all system dependencies
brew install pandoc pango gdk-pixbuf libffi
```

### 15.3 Input Constraints

- **Framework files:** Must be valid markdown format
- **File size:** Optimized for files up to 5000 lines (~200KB)
- **Images:** PNG, JPG, SVG formats only; max 10MB per image
- **Metadata:** Must include module number and title in YAML frontmatter
- **Encoding:** UTF-8 required

### 15.4 Output Constraints

- **PDF size:** Target < 10MB per handout (with images)
- **Page count:** Estimated 30-60 pages per module
- **Image count:** Recommend 5-15 images per handout
- **Question count:** 30-70 questions per module

### 15.5 Performance Targets

| Operation | Target | Hardware |
|-----------|--------|----------|
| Single module (small, <500 lines) | < 2 min | M1 MacBook Pro, 16GB |
| Single module (large, 1000+ lines) | < 5 min | M1 MacBook Pro, 16GB |
| Batch (11 modules) | < 30 min | M1 MacBook Pro, 16GB |
| PDF rendering only (cached questions) | < 30 sec | M1 MacBook Pro, 16GB |
| Question review (per question) | ~10 sec | User dependent |

### 15.6 Deployment

- **Target Environment:** Local macOS installation only
- **Installation Method:** Clone repository + pip install + Homebrew dependencies
- **No containerization required**
- **No CI/CD pipeline required**
- **Single user, single machine**

---

## 16. Success Metrics & KPIs

### 16.1 Functional Metrics

| Metric | Target | Measurement Method |
|--------|--------|-------------------|
| **Generation Success Rate** | 95%+ | (Successful generations / Total attempts) × 100 |
| **Processing Speed** | < 5 min per module | Average time from CLI execution to PDF output |
| **Batch Processing Time** | < 30 min for 11 modules | Total time for full course generation |
| **Question Generation Rate** | 7+ questions per section | Count of AI-generated questions per major section |
| **PDF Quality Score** | Pass/Fail checklist | Manual verification: dark theme, images, TOC, questions |

### 16.2 Quality Metrics

| Metric | Target | Measurement Method |
|--------|--------|-------------------|
| **Image Embedding Success** | 90%+ | (Embedded images / Total images referenced) × 100 |
| **Question Variety** | 4+ types per module | Count distinct question types used |
| **Content Fidelity** | 100% | Original student content preserved without errors |
| **Formatting Consistency** | 100% | All modules use same dark template/styling |

### 16.3 Review Process Metrics

| Metric | Target | Measurement Method |
|--------|--------|-------------------|
| **Question Approval Rate** | 70%+ | (Approved / Total generated) × 100 |
| **Review Time per Question** | < 15 sec | Average time in review interface |
| **Edit Rate** | < 20% | Questions needing edits before approval |
| **Rejection Rate** | < 15% | Questions rejected as unusable |

---

## 17. Testing Strategy

### 17.1 Unit Tests

Test each module independently:
- `test_framework_parser.py`: Parse various markdown structures, metadata extraction
- `test_content_transformer.py`: Filter rules, pattern exclusion, transformations
- `test_question_generator.py`: API mocking, question schema validation
- `test_question_reviewer.py`: Status transitions, file operations
- `test_image_processor.py`: Image detection, resizing, placeholders
- `test_pdf_renderer.py`: PDF creation, styling application
- `test_security.py`: Path validation, input sanitization
- `test_config_manager.py`: Config loading, validation, defaults

**Target Coverage:** 80%+ line coverage

### 17.2 Integration Tests

Test end-to-end workflows:
- Single module generation (Module 0) with pre-approved questions
- Question generation → staging → review → approval flow
- Batch generation with mixed states (some approved, some blocked)
- Configuration overrides (custom colors, margins)
- Error handling (missing images, malformed markdown, API failures)

### 17.3 Validation Tests

Quality checks on generated handouts:
- PDF opens without errors in Preview (macOS)
- Dark theme colors render correctly
- All images display (or show placeholders)
- TOC links work
- Page numbers are accurate
- Questions are properly formatted with correct border colors
- Code blocks have syntax highlighting
- No orphaned headings or broken layouts

### 17.4 Test Fixtures

```
tests/fixtures/
├── sample_framework_small.md      # <500 lines
├── sample_framework_large.md      # >1000 lines
├── sample_framework_malformed.md  # Invalid markdown
├── sample_framework_no_metadata.md
├── sample_questions_approved.json
├── sample_questions_staging.json
├── sample_config.yaml
└── images/
    ├── valid_image.png
    ├── large_image.png           # >10MB
    └── corrupted_image.png
```

---

## 18. Documentation Requirements

### 18.1 README.md Contents

1. **Overview** - What the tool does
2. **Quick Start** - Get first handout generated in 5 minutes
3. **Prerequisites** - Python, Homebrew dependencies
4. **Installation** - Step-by-step setup
5. **Configuration** - API key setup, config file basics
6. **Usage Examples** - Common CLI commands
7. **Question Review** - How to review AI-generated questions
8. **Troubleshooting** - Common errors and solutions

### 18.2 Configuration Reference

- Complete `handout_config.yaml` with all options documented
- Environment variable requirements
- Module-specific override examples

### 18.3 Inline Code Documentation

- Docstrings for all public functions/classes (Google style)
- Type hints for all function signatures
- Comments for complex logic
- Example usage in docstrings

---

## 19. Risk Assessment & Mitigation

### 19.1 Technical Risks

| Risk | Likelihood | Impact | Mitigation Strategy |
|------|------------|--------|---------------------|
| **WeasyPrint dark theme issues** | Medium | High | Test extensively; have fallback CSS; check color rendering on different PDF viewers |
| **Claude API rate limits** | Low | Medium | Implement retry with exponential backoff; cache generated questions |
| **Claude API costs** | Medium | Low | Monitor usage; batch questions per API call; reuse approved questions |
| **Large file memory issues** | Low | Medium | Stream processing; test with largest framework files |
| **Font embedding failures** | Low | Medium | Include fallback fonts; test PDF portability |

### 19.2 Process Risks

| Risk | Likelihood | Impact | Mitigation Strategy |
|------|------------|--------|---------------------|
| **AI generates poor questions** | Medium | Medium | Mandatory review workflow; track rejection rate; refine prompts |
| **Review bottleneck** | Medium | Medium | Make review interface fast; allow batch approve for trusted patterns |
| **Lost approved questions** | Low | High | Archive all question banks; include in version control |
| **Config file errors** | Medium | Low | Schema validation; clear error messages; example files |

### 19.3 Quality Risks

| Risk | Likelihood | Impact | Mitigation Strategy |
|------|------------|--------|---------------------|
| **Inconsistent PDF output** | Low | Medium | Strict templating; automated visual checks |
| **Missing content in handouts** | Low | High | Validation step comparing input/output sections |
| **Broken images** | Medium | Low | Pre-flight image validation; clear placeholders |

---

## 20. Future Enhancements (Post-v1.0)

### 20.1 Short-term (v1.1)
- Light theme option for printing
- Answer key generation (separate PDF)
- Question difficulty auto-calibration based on review feedback
- Batch question approval for similar question types

### 20.2 Medium-term (v1.2)
- HTML output with interactive elements
- Glossary auto-generation from content
- Question bank sharing across modules (for common concepts)
- Performance optimization (parallel processing)

### 20.3 Long-term (v2.0+)
- Web-based configuration interface
- Multiple course support with unified question bank
- Analytics on question quality and review patterns
- Integration with cloud storage for outputs

---

## 21. Appendices

### Appendix A: Sample Question Bank Format

**File:** `question_banks/approved/module-0.json`

```json
{
  "module_id": "module-0",
  "module_title": "The Hook - Welcome to Machine Learning",
  "version": "1.0",
  "last_reviewed": "2026-01-11T14:30:00Z",
  "questions": [
    {
      "id": "m0-s1-q1",
      "type": "multiple_choice",
      "question_text": "Which of the following is NOT an application of ML shown in the demos?",
      "options": [
        "Stock price prediction",
        "Face detection",
        "Weather forecasting",
        "Sentiment analysis"
      ],
      "correct_answer": "C",
      "explanation": "The five demos were: stock predictor, cricket predictor, face detection, sentiment analyzer, and chatbot. Weather forecasting was not included.",
      "difficulty": "easy",
      "points": 1,
      "learning_outcome": "Recognize common ML applications",
      "source_section": "session-1-demos",
      "source": "ai_generated",
      "status": "approved",
      "reviewed_at": "2026-01-11T14:25:00Z",
      "reviewer_notes": null
    },
    {
      "id": "m0-s1-q2",
      "type": "reflection",
      "question_text": "Which of the 5 demos excited you most and why? How might similar technology apply to your work?",
      "options": null,
      "correct_answer": null,
      "explanation": "Reflect on your interests and how ML could apply to your field. 2-3 sentences.",
      "difficulty": "easy",
      "points": 2,
      "learning_outcome": "Connect ML concepts to personal context",
      "source_section": "session-1-demos",
      "source": "ai_generated",
      "status": "approved",
      "reviewed_at": "2026-01-11T14:26:00Z",
      "reviewer_notes": "Added 'to your work' for specificity"
    }
  ]
}
```

### Appendix B: Staging Question Format

**File:** `question_banks/staging/module-0-staging.json`

```json
{
  "module_id": "module-0",
  "generated_at": "2026-01-11T10:00:00Z",
  "model_used": "claude-sonnet-4-20250514",
  "questions_pending": 15,
  "questions_reviewed": 0,
  "questions": [
    {
      "id": "m0-s1-q1-staging",
      "type": "multiple_choice",
      "question_text": "Which of the following is NOT an application of ML shown in the demos?",
      "options": [
        "Stock price prediction",
        "Face detection", 
        "Weather forecasting",
        "Sentiment analysis"
      ],
      "correct_answer": "C",
      "explanation": "The five demos were: stock predictor, cricket predictor, face detection, sentiment analyzer, and chatbot.",
      "difficulty": "easy",
      "points": 1,
      "learning_outcome": "Recognize common ML applications",
      "source_section": "session-1-demos",
      "source": "ai_generated",
      "status": "pending_review",
      "reviewed_at": null,
      "reviewer_notes": null
    }
  ]
}
```

### Appendix C: Configuration Schema (JSON Schema)

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "global": {
      "type": "object",
      "properties": {
        "output_directory": {"type": "string"},
        "archive_old_versions": {"type": "boolean"},
        "page_size": {"type": "string", "enum": ["A4", "Letter"]}
      },
      "required": ["output_directory"]
    },
    "branding": {
      "type": "object",
      "properties": {
        "logo_path": {"type": "string"},
        "theme": {"type": "string", "enum": ["dark", "light"]},
        "colors": {
          "type": "object",
          "properties": {
            "background_primary": {"type": "string", "pattern": "^#[0-9A-Fa-f]{6}$"},
            "text_primary": {"type": "string", "pattern": "^#[0-9A-Fa-f]{6}$"}
          }
        }
      }
    },
    "questions": {
      "type": "object",
      "properties": {
        "enabled": {"type": "boolean"},
        "require_review": {"type": "boolean", "const": true},
        "questions_per_section": {"type": "integer", "minimum": 1, "maximum": 20},
        "types": {
          "type": "array",
          "items": {
            "type": "string",
            "enum": ["multiple_choice", "true_false", "short_answer", "reflection", "application"]
          }
        },
        "ai_generation": {
          "type": "object",
          "properties": {
            "enabled": {"type": "boolean"},
            "provider": {"type": "string", "enum": ["anthropic"]},
            "api_key_env_var": {"type": "string"},
            "model": {"type": "string"}
          }
        }
      },
      "required": ["enabled", "require_review"]
    }
  },
  "required": ["global", "questions"]
}
```

### Appendix D: Markdown Metadata Conventions

Framework files must include YAML frontmatter:

```markdown
---
course_code: ML-ENG-M0
module_number: 0
module_title: "The Hook - Welcome to Machine Learning"
duration: "1 week"
video_content: "~4.5 hours"
hands_on_time: "~2-3 hours"
last_updated: 2026-01-05
version: 2.0
---

# Module 0: The Hook - Welcome to Machine Learning

## Session 1: The 5 Amazing Demos
...
```

**Required fields:**
- `course_code`
- `module_number`
- `module_title`

**Optional fields:**
- `duration`
- `video_content`
- `hands_on_time`
- `last_updated`
- `version`

### Appendix E: Image Directory Structure

```
courses/ml-for-engineers/images/
├── module-0/
│   ├── demo-stock-predictor.png
│   ├── demo-cricket-predictor.png
│   ├── demo-face-detection.png
│   ├── colab-interface.png
│   └── gpu-comparison-chart.png
├── module-1/
│   ├── data-exploration-workflow.png
│   ├── pandas-dataframe.png
│   └── visualization-examples.png
└── shared/
    ├── ml-workflow.png
    ├── course-roadmap.png
    └── logo.png
```

Reference in markdown:
```markdown
![Google Colab Interface](../images/module-0/colab-interface.png)
```

### Appendix F: Environment Setup

**`.env.example`:**
```bash
# Anthropic API Key (required for AI question generation)
ANTHROPIC_API_KEY=sk-ant-xxxxxxxxxxxxxxxxxxxxx

# Optional: Override default config path
HANDOUT_CONFIG_PATH=./custom_config.yaml

# Optional: Log level (DEBUG, INFO, WARNING, ERROR)
LOG_LEVEL=INFO
```

**Setup steps:**
```bash
# 1. Clone repository
git clone <repo-url>
cd Course_Generator

# 2. Install system dependencies
brew install pandoc pango gdk-pixbuf libffi

# 3. Create virtual environment
python3.11 -m venv venv
source venv/bin/activate

# 4. Install Python dependencies
pip install -r requirements.txt

# 5. Set up environment variables
cp .env.example .env
# Edit .env and add your ANTHROPIC_API_KEY

# 6. Verify installation
python generate_handout.py --help
```

### Appendix G: Complete CSS Dark Theme

```css
/* Dark Theme Stylesheet for Student Handouts */
/* Version: 2.0 */

/* ========== Page Setup ========== */
@page {
  size: A4;
  margin: 20mm 25mm;
  background: #0D1117;
  
  @top-center {
    content: string(module-title);
    font-family: "Inter", sans-serif;
    font-size: 10pt;
    color: #8B949E;
    border-bottom: 1px solid #30363D;
    padding-bottom: 8mm;
  }
  
  @bottom-center {
    content: "Page " counter(page);
    font-family: "Inter", sans-serif;
    font-size: 9pt;
    color: #484F58;
  }
}

/* ========== Base Styles ========== */
body {
  font-family: "Inter", -apple-system, sans-serif;
  font-size: 11pt;
  line-height: 1.6;
  color: #E6EDF3;
  background: #0D1117;
}

/* ========== Typography ========== */
h1 {
  font-size: 28pt;
  font-weight: 600;
  color: #E6EDF3;
  margin: 0 0 24px 0;
  string-set: module-title content();
}

h2 {
  font-size: 22pt;
  font-weight: 600;
  color: #E6EDF3;
  margin: 32px 0 16px 0;
  page-break-after: avoid;
}

h3 {
  font-size: 16pt;
  font-weight: 600;
  color: #E6EDF3;
  margin: 24px 0 12px 0;
}

h4 {
  font-size: 14pt;
  font-weight: 600;
  color: #8B949E;
  margin: 20px 0 8px 0;
}

p {
  margin: 0 0 12pt 0;
}

a {
  color: #58A6FF;
  text-decoration: none;
}

a:hover {
  text-decoration: underline;
}

/* ========== Lists ========== */
ul, ol {
  margin: 12px 0;
  padding-left: 24px;
}

li {
  margin: 4px 0;
}

/* ========== Code ========== */
code {
  font-family: "JetBrains Mono", monospace;
  font-size: 10pt;
  background: #161B22;
  padding: 2px 6px;
  border-radius: 4px;
}

pre {
  background: #161B22;
  border: 1px solid #30363D;
  border-radius: 6px;
  padding: 16px;
  overflow-x: auto;
  margin: 16px 0;
}

pre code {
  background: none;
  padding: 0;
  font-size: 10pt;
  line-height: 1.4;
}

/* Syntax Highlighting */
.highlight .k { color: #FF7B72; }  /* Keyword */
.highlight .s { color: #A5D6FF; }  /* String */
.highlight .c { color: #8B949E; }  /* Comment */
.highlight .nf { color: #D2A8FF; } /* Function */
.highlight .mi { color: #79C0FF; } /* Number */

/* ========== Tables ========== */
table {
  width: 100%;
  border-collapse: collapse;
  margin: 16px 0;
}

th, td {
  padding: 12px;
  text-align: left;
  border: 1px solid #30363D;
}

th {
  background: #161B22;
  font-weight: 600;
  color: #E6EDF3;
}

td {
  background: #0D1117;
}

tr:nth-child(even) td {
  background: #161B22;
}

/* ========== Images ========== */
img {
  max-width: 500px;
  height: auto;
  display: block;
  margin: 16px auto;
  border-radius: 4px;
}

.image-caption {
  text-align: center;
  font-size: 9pt;
  color: #8B949E;
  margin-top: 8px;
}

.image-placeholder {
  background: #21262D;
  border: 1px dashed #30363D;
  border-radius: 4px;
  padding: 40px;
  text-align: center;
  color: #484F58;
  font-size: 10pt;
}

/* ========== Question Boxes ========== */
.question-box {
  background: #161B22;
  border-left: 3px solid #58A6FF;
  border-radius: 6px;
  padding: 16px 20px;
  margin: 24px 0;
  page-break-inside: avoid;
}

.question-box.reflection {
  border-left-color: #A371F7;
}

.question-box.application,
.question-box.short_answer {
  border-left-color: #3FB950;
}

.question-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 12px;
}

.question-number {
  background: #58A6FF;
  color: #0D1117;
  padding: 2px 8px;
  border-radius: 4px;
  font-size: 10pt;
  font-weight: 600;
}

.question-box.reflection .question-number {
  background: #A371F7;
}

.question-box.application .question-number,
.question-box.short_answer .question-number {
  background: #3FB950;
}

.question-type {
  color: #8B949E;
  font-size: 9pt;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.question-text {
  color: #E6EDF3;
  font-size: 11pt;
  line-height: 1.6;
  margin-bottom: 12px;
}

.question-options {
  margin-left: 20px;
}

.question-option {
  color: #E6EDF3;
  padding: 6px 0;
}

.answer-line {
  border-bottom: 1px solid #30363D;
  margin: 8px 0;
  height: 24px;
}

.answer-box {
  border: 1px solid #30363D;
  border-radius: 4px;
  min-height: 80px;
  margin-top: 12px;
}

/* ========== Note Boxes ========== */
.note-box {
  background: #161B22;
  border-left: 3px solid #D29922;
  border-radius: 6px;
  padding: 12px 16px;
  margin: 16px 0;
}

.note-box.warning {
  border-left-color: #F85149;
}

.note-box.tip {
  border-left-color: #3FB950;
}

.note-label {
  font-size: 10pt;
  font-weight: 600;
  text-transform: uppercase;
  margin-bottom: 4px;
}

.note-box .note-label {
  color: #D29922;
}

.note-box.warning .note-label {
  color: #F85149;
}

.note-box.tip .note-label {
  color: #3FB950;
}

/* ========== Table of Contents ========== */
.toc {
  background: #161B22;
  border-radius: 6px;
  padding: 20px 24px;
  margin: 24px 0;
}

.toc-title {
  color: #E6EDF3;
  font-size: 16pt;
  font-weight: 600;
  margin-bottom: 16px;
  padding-bottom: 8px;
  border-bottom: 1px solid #30363D;
}

.toc-item {
  display: block;
  color: #58A6FF;
  padding: 4px 0;
  text-decoration: none;
}

.toc-item-h2 {
  margin-left: 0;
}

.toc-item-h3 {
  margin-left: 20px;
  font-size: 10pt;
}

.toc-page {
  color: #8B949E;
  float: right;
}

/* ========== Self-Study Section ========== */
.self-study-section {
  background: #161B22;
  border-radius: 6px;
  padding: 20px;
  margin: 32px 0;
}

.self-study-title {
  color: #58A6FF;
  font-size: 14pt;
  font-weight: 600;
  margin-bottom: 16px;
  padding-bottom: 8px;
  border-bottom: 1px solid #30363D;
}

/* ========== Utility Classes ========== */
.text-muted {
  color: #8B949E;
}

.text-small {
  font-size: 9pt;
}

.page-break {
  page-break-before: always;
}

.no-break {
  page-break-inside: avoid;
}
```

---

## 22. Approval & Sign-off

### Document Review

| Role | Name | Date | Status |
|------|------|------|--------|
| Author | Course Generator Team | 2026-01-11 | Draft Complete |
| Reviewer | [Your Name] | [Date] | ________ |

### Change Log

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-01-11 | Course Generator Team | Initial PRD creation |
| 2.0 | 2026-01-11 | Course Generator Team | Added: mandatory question review workflow, security requirements, error handling spec, dark theme design system, M1 performance targets, simplified deployment |

---

## 23. References & Resources

### Technical Documentation
- [WeasyPrint Documentation](https://weasyprint.readthedocs.io/)
- [Pandoc User Guide](https://pandoc.org/MANUAL.html)
- [Anthropic Claude API](https://docs.anthropic.com/)
- [Rich Terminal Library](https://rich.readthedocs.io/)
- [Python Type Hints PEP 484](https://peps.python.org/pep-0484/)

### Design References
- [GitHub Dark Theme](https://github.com/primer/primitives)
- [Inter Font Family](https://rsms.me/inter/)
- [JetBrains Mono](https://www.jetbrains.com/lp/mono/)

### Instructional Design
- [Bloom's Taxonomy](https://cft.vanderbilt.edu/guides-sub-pages/blooms-taxonomy/)
- [Writing Good Multiple Choice Questions](https://cft.vanderbilt.edu/guides-sub-pages/writing-good-multiple-choice-test-questions/)

---

**END OF DOCUMENT**

*This PRD is a living document and will be updated as the project evolves.*
