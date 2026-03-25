# Usage Guide

Comprehensive guide to using the Student Handout Generator system.

---

## Table of Contents

- [Quick Start](#quick-start)
- [Configuration](#configuration)
- [Single Module Generation](#single-module-generation)
- [AI Question Generation](#ai-question-generation)
- [Question Review Process](#question-review-process)
- [Batch Processing](#batch-processing)
- [Advanced Features](#advanced-features)
- [CLI Reference](#cli-reference)
- [Common Tasks](#common-tasks)

---

## Quick Start

Generate your first handout in 5 minutes!

### Prerequisites

- Installation complete (see [INSTALLATION.md](INSTALLATION.md))
- API key configured in `.env`
- Framework markdown file ready

### Step 1: Validate Your Setup

```bash
python3 generate_handout.py --help
```

### Step 2: Test with Dry Run

```bash
python3 generate_handout.py \
  --input courses/ml-for-engineers/frameworks/module-0-framework-REVISED.md \
  --dry-run
```

### Step 3: Generate Questions (First Time)

```bash
python3 generate_handout.py \
  --input courses/ml-for-engineers/frameworks/module-0-framework-REVISED.md
```

If questions need to be generated, you'll see:
```
[INFO] Generating questions for module-0...
[INFO] Questions saved to: question_banks/staging/module-0-staging.json
[BLOCKED] Questions need review before generating handout
[INFO] Run: python3 generate_handout.py --review-questions module-0
```

### Step 4: Review Questions

```bash
python3 generate_handout.py --review-questions module-0
```

Interactive review interface will guide you through approving questions.

### Step 5: Generate Handout

```bash
python3 generate_handout.py \
  --input courses/ml-for-engineers/frameworks/module-0-framework-REVISED.md
```

Output:
```
[SUCCESS] Handout generated: handouts/ml-for-engineers/module-0/ML-ENG-module-0-handout.pdf
[INFO] Processing time: 2m 34s
```

---

## Configuration

### Configuration File: `handout_config.yaml`

The main configuration file controls all aspects of handout generation.

#### Global Settings

```yaml
global:
  output_directory: "./handouts"
  archive_old_versions: true
  page_size: "A4"  # or "Letter"
  fonts:
    body: "Inter"
    heading: "Inter"
    code: "JetBrains Mono"
```

**Parameters:**
- `output_directory`: Where PDFs are saved
- `archive_old_versions`: Keep previous versions in `/archive/` subdirectory
- `page_size`: Paper size (A4 or Letter)
- `fonts`: Font families (must be installed on system)

#### Dark Theme Branding

```yaml
branding:
  logo_path: "./assets/logo.png"
  theme: "dark"
  colors:
    # Backgrounds (darkest to lightest)
    background_primary: "#0D1117"
    background_secondary: "#161B22"
    background_tertiary: "#21262D"

    # Text (highest to lowest contrast)
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
```

**Color Scheme:**
- Based on GitHub Dark theme
- High contrast for readability
- Question boxes use accent colors for borders

#### Question Configuration

```yaml
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
```

**Key Parameters:**
- `questions_per_section`: Target number of questions per major section (H2 headings)
- `require_review`: Always true - questions must be reviewed before inclusion
- `types`: Question types to generate
- `ai_generation.model`: Claude model to use
- `max_retries`: API retry attempts

#### Content Transformation

```yaml
content:
  exclude_patterns:
    - "## Video Production Notes"
    - "### For Instructors"
    - "<!-- INSTRUCTOR ONLY -->"
  include_toc: true
  include_learning_outcomes: true
  include_assessments: true
```

**Exclude Patterns:**
Sections matching these patterns are removed from student handouts:
- Section headers (exact match)
- HTML comments
- Custom markers

#### Image Settings

```yaml
images:
  base_directory: "./images"
  max_width: 500  # pixels
  placeholder_on_missing: true
  placeholder_color: "#21262D"
  formats_supported:
    - png
    - jpg
    - jpeg
    - svg
```

**Image Handling:**
- `max_width`: Maximum image width for dark theme readability
- `placeholder_on_missing`: Show placeholder for missing images (vs. skip)
- `placeholder_color`: Dark background for placeholders

#### PDF Output

```yaml
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
```

#### Module-Specific Overrides

Override global settings for specific modules:

```yaml
modules:
  module-0:
    questions:
      questions_per_section: 5  # Lighter for intro module
  module-10:
    questions:
      questions_per_section: 10  # More for capstone
```

### Custom Configuration Files

Use a custom config file:

```bash
python3 generate_handout.py \
  --input framework.md \
  --config custom_config.yaml
```

---

## Single Module Generation

### Basic Usage

```bash
python3 generate_handout.py --input <framework-file>
```

### Example

```bash
python3 generate_handout.py \
  --input courses/ml-for-engineers/frameworks/module-1-framework-REVISED.md
```

### Output Location

Default: `./handouts/<course-name>/module-<N>/`

Example:
```
handouts/
└── ml-for-engineers/
    └── module-1/
        ├── ML-ENG-module-1-handout.pdf
        └── metadata.json
```

### Custom Output Directory

```bash
python3 generate_handout.py \
  --input framework.md \
  --output ~/Documents/student-materials
```

### Processing Steps

1. **Parse Framework** - Extract metadata and content structure
2. **Transform Content** - Remove instructor sections, clean content
3. **Check Questions** - Load or generate questions
4. **Review Gate** - Block if questions need review
5. **Process Images** - Embed images or create placeholders
6. **Layout** - Combine content + questions + images into HTML
7. **Render PDF** - Convert to PDF with dark theme styling
8. **Save** - Write to output directory

### Processing Time

- **Small modules** (<500 lines): ~2 minutes
- **Medium modules** (500-1000 lines): ~3 minutes
- **Large modules** (>1000 lines): ~5 minutes

Times include AI question generation. Regeneration with approved questions: ~30 seconds.

---

## AI Question Generation

### How It Works

1. **Content Analysis** - AI analyzes each major section
2. **Question Generation** - Creates 5-10 contextual questions per section
3. **Staging** - Questions saved to staging file with `"status": "pending_review"`
4. **Review Required** - Handout generation blocks until review complete

### Question Types

The AI generates 5 types of questions:

#### 1. Multiple Choice

```json
{
  "type": "multiple_choice",
  "question_text": "What is Google Colab?",
  "options": [
    "A graphics editing tool",
    "A cloud-based Jupyter notebook with free GPU",
    "A Google Meet alternative",
    "A data storage service"
  ],
  "correct_answer": "B",
  "explanation": "Google Colab provides free cloud-based Jupyter notebooks..."
}
```

#### 2. True/False

```json
{
  "type": "true_false",
  "question_text": "You need to install Python before using Colab.",
  "options": ["True", "False"],
  "correct_answer": "False",
  "explanation": "Colab runs entirely in the browser with Python pre-installed."
}
```

#### 3. Short Answer

```json
{
  "type": "short_answer",
  "question_text": "Name 3 Python libraries pre-installed in Google Colab.",
  "correct_answer": "pandas, numpy, scikit-learn (or matplotlib, tensorflow, etc.)"
}
```

#### 4. Reflection

```json
{
  "type": "reflection",
  "question_text": "Which of the 5 ML demos relates most to your industry? Why?",
  "correct_answer": null,
  "explanation": "There is no single correct answer. Reflect on your context."
}
```

#### 5. Application Scenario

```json
{
  "type": "application",
  "question_text": "You need to train a deep learning model on a large dataset. Your laptop has only a CPU. What are three solutions?",
  "correct_answer": "1) Use Google Colab with free GPU, 2) Enable GPU runtime..."
}
```

### Question Placement

Questions are placed:
- **After H2 sections** (major topics)
- **End of sessions** (comprehensive review)
- **Module conclusion** (cumulative assessment)
- **Average frequency:** 1 question per 150-200 lines of content

### Regenerate Questions

To regenerate questions (overwrites staging file):

```bash
python3 generate_handout.py \
  --input framework.md \
  --regenerate-questions
```

**Warning:** This discards pending questions. Approved questions are not affected.

---

## Question Review Process

### Starting a Review Session

```bash
python3 generate_handout.py --review-questions <module-id>
```

Example:
```bash
python3 generate_handout.py --review-questions module-0
```

### Review Interface

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

### Review Actions

#### A - Approve

Approve the question as-is. Moves to approved question bank.

```
Your choice: a

✓ Question approved

Question 4 of 15...
```

#### E - Edit

Edit question text, options, or answer before approving.

```
Your choice: e

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

#### R - Reject

Reject the question. Moves to rejected bank for reference.

```
Your choice: r

Reason for rejection (optional):
> Too obvious, doesn't test understanding

✓ Question rejected
```

#### S - Skip

Skip for now. Keeps status as "pending_review". Can review later.

```
Your choice: s

⏭ Question skipped (will remain pending)
```

#### Q - Quit

Exit review session. Skipped questions remain pending.

```
Your choice: q

Review Session Summary:
  Total questions: 15
  Approved: 8
  Edited: 3
  Rejected: 2
  Skipped: 2

Progress saved. Resume with: python3 generate_handout.py --review-questions module-0
```

### Resume Interrupted Session

If you quit or the session is interrupted:

```bash
# Same command resumes where you left off
python3 generate_handout.py --review-questions module-0
```

Only pending questions are shown.

### Review Status

Check review status for all modules:

```bash
python3 generate_handout.py --review-status --course ml-for-engineers
```

Output:
```
Question Review Status - ml-for-engineers
═══════════════════════════════════════════

✓ module-0: 15/15 approved (100%)
✓ module-1: 18/18 approved (100%)
⏸ module-2: 12/20 approved (60%) - 8 pending
✗ module-3: 0/22 generated - Needs generation
✓ module-4: 16/16 approved (100%)
```

### Question Files

Questions are stored in three locations:

**Staging (Pending Review):**
```
question_banks/staging/module-0-staging.json
```

**Approved:**
```
question_banks/approved/module-0.json
```

**Rejected (Reference):**
```
question_banks/rejected/module-0-rejected.json
```

---

## Batch Processing

Process multiple modules in one command.

### Batch All Modules

```bash
python3 generate_handout.py --batch --course ml-for-engineers
```

### Batch Specific Modules

```bash
python3 generate_handout.py \
  --batch \
  --course ml-for-engineers \
  --modules 0,1,2
```

### Pre-Flight Check

Before processing, the system checks question review status:

```
Checking question review status...

Modules ready:
  ✓ module-0 (15 questions approved)
  ✓ module-1 (18 questions approved)

Modules blocked (need review):
  ⏸ module-2 (8/20 questions pending)
  ⏸ module-3 (22/22 questions pending)

[BLOCKED] Cannot proceed. Review questions first:
  python3 generate_handout.py --review-questions module-2
  python3 generate_handout.py --review-questions module-3
```

### Batch Processing Output

```
Batch Processing: ml-for-engineers
═══════════════════════════════════

[1/11] Processing module-0...
  ├─ Parsing framework... ✓
  ├─ Transforming content... ✓
  ├─ Loading questions (15 approved)... ✓
  ├─ Processing images (5 found)... ✓
  ├─ Rendering PDF... ✓
  └─ Saved: handouts/ml-for-engineers/module-0/ML-ENG-module-0-handout.pdf
  Time: 2m 15s

[2/11] Processing module-1...
  ├─ Parsing framework... ✓
  ├─ Transforming content... ✓
  ├─ Loading questions (18 approved)... ✓
  ├─ Processing images (8 found)... ✓
  ├─ Rendering PDF... ✓
  └─ Saved: handouts/ml-for-engineers/module-1/ML-ENG-module-1-handout.pdf
  Time: 3m 02s

...

Batch Complete
══════════════
  Total modules: 11
  Successful: 11
  Failed: 0
  Total time: 28m 45s
```

### Error Handling in Batch

If a module fails, batch processing continues:

```
[5/11] Processing module-4...
  ├─ Parsing framework... ✓
  ├─ Transforming content... ✓
  ├─ Loading questions... ✗ ERROR: Question file corrupted
  └─ FAILED: Skipping module-4

[6/11] Processing module-5...
  ├─ Parsing framework... ✓
  ...
```

Errors are logged to `logs/handout_generation.log`.

---

## Advanced Features

### Use Approved Questions (Skip AI)

Regenerate handout using existing question bank (no AI calls):

```bash
python3 generate_handout.py \
  --input framework.md \
  --use-approved-questions
```

**Use when:**
- Content changed but questions remain valid
- Want faster regeneration (~30 seconds vs. 3 minutes)
- Avoiding API costs

### Force Unreviewed Questions

Generate handout with unreviewed questions (adds warning banner):

```bash
python3 generate_handout.py \
  --input framework.md \
  --force-unreviewed
```

**Warning Banner on PDF:**
```
⚠ WARNING: This handout contains unreviewed AI-generated questions.
Please verify accuracy before distribution to students.
```

**Use when:**
- Quick draft needed
- Internal review only
- Not for student distribution

### Dry Run Mode

Validate without generating:

```bash
python3 generate_handout.py \
  --input framework.md \
  --dry-run
```

**Checks performed:**
- Framework file exists and is valid
- Metadata extraction
- Content structure
- Image references (warns if missing)
- Question bank status
- Configuration validity

**No files created.**

### Verbose Logging

See detailed processing information:

```bash
python3 generate_handout.py \
  --input framework.md \
  --verbose
```

Output includes:
- Detailed parsing steps
- API request/response summaries
- Image processing details
- Layout decisions
- PDF rendering metrics

### Multiple Output Formats

Generate PDF and HTML:

```bash
python3 generate_handout.py \
  --input framework.md \
  --formats pdf,html
```

**HTML output:** Same dark theme, viewable in browser, interactive TOC.

### Archive Old Versions

Automatically archive previous handouts:

```yaml
# In handout_config.yaml
global:
  archive_old_versions: true
```

Directory structure:
```
handouts/
└── module-0/
    ├── ML-ENG-module-0-handout.pdf  (latest)
    └── archive/
        ├── ML-ENG-module-0-handout-2026-01-10T14-30-00.pdf
        └── ML-ENG-module-0-handout-2026-01-09T09-15-00.pdf
```

---

## CLI Reference

### Complete Command Syntax

```bash
python3 generate_handout.py [OPTIONS]
```

### Global Options

| Option | Short | Type | Description |
|--------|-------|------|-------------|
| `--help` | `-h` | flag | Show help message |
| `--version` | | flag | Show version info |

### Generation Options

| Option | Short | Required | Default | Description |
|--------|-------|----------|---------|-------------|
| `--input` | `-i` | Yes* | - | Path to framework markdown file |
| `--output` | `-o` | No | `./handouts` | Output directory |
| `--config` | | No | `handout_config.yaml` | Config file path |
| `--formats` | `-f` | No | `pdf` | Output formats (pdf,html) |
| `--dry-run` | | No | False | Validate without generating |
| `--verbose` | `-v` | No | False | Verbose logging |

*Not required if using `--batch`, `--review-questions`, or `--review-status`

### Question Options

| Option | Description |
|--------|-------------|
| `--review-questions <module-id>` | Start interactive question review |
| `--review-status --course <name>` | Show review status for all modules |
| `--use-approved-questions` | Skip AI generation, use approved bank |
| `--force-unreviewed` | Generate with unreviewed questions (warning added) |
| `--regenerate-questions` | Re-generate AI questions (overwrites staging) |

### Batch Options

| Option | Short | Description |
|--------|-------|-------------|
| `--batch` | `-b` | Enable batch processing |
| `--course` | `-c` | Course name (required with `--batch`) |
| `--modules` | `-m` | Comma-separated module numbers (e.g., `0,1,2`) |

### Examples

**Single module with custom output:**
```bash
python3 generate_handout.py \
  -i frameworks/module-0.md \
  -o ~/Desktop/handouts \
  -v
```

**Batch specific modules:**
```bash
python3 generate_handout.py \
  --batch \
  --course ml-for-engineers \
  --modules 0,1,2,3
```

**Review questions:**
```bash
python3 generate_handout.py --review-questions module-5
```

**Quick regeneration:**
```bash
python3 generate_handout.py \
  -i frameworks/module-0.md \
  --use-approved-questions
```

---

## Common Tasks

### Task 1: Generate First Handout for New Module

```bash
# Step 1: Generate (triggers AI question generation)
python3 generate_handout.py --input frameworks/module-X.md

# Step 2: Review generated questions
python3 generate_handout.py --review-questions module-X

# Step 3: Generate handout with approved questions
python3 generate_handout.py --input frameworks/module-X.md
```

### Task 2: Update Handout After Content Changes

Content changed, questions remain valid:

```bash
python3 generate_handout.py \
  --input frameworks/module-X.md \
  --use-approved-questions
```

### Task 3: Regenerate Questions After Major Content Revision

```bash
# Regenerate questions
python3 generate_handout.py \
  --input frameworks/module-X.md \
  --regenerate-questions

# Review new questions
python3 generate_handout.py --review-questions module-X

# Generate handout
python3 generate_handout.py --input frameworks/module-X.md
```

### Task 4: Check Status Before Batch Generation

```bash
# Check review status
python3 generate_handout.py --review-status --course ml-for-engineers

# Review any pending modules
python3 generate_handout.py --review-questions module-X

# Batch generate
python3 generate_handout.py --batch --course ml-for-engineers
```

### Task 5: Generate Handouts for Entire Course

```bash
# Full workflow
for module in {0..10}; do
  # Generate questions
  python3 generate_handout.py \
    --input courses/ml-for-engineers/frameworks/module-${module}-framework-REVISED.md

  # Review questions
  python3 generate_handout.py --review-questions module-${module}
done

# Batch generate all
python3 generate_handout.py --batch --course ml-for-engineers
```

### Task 6: Create Custom Question Bank Manually

Create `question_banks/approved/module-X.json`:

```json
{
  "module_id": "module-X",
  "module_title": "Your Module Title",
  "version": "1.0",
  "last_reviewed": "2026-01-11T14:30:00Z",
  "questions": [
    {
      "id": "mx-s1-q1",
      "type": "multiple_choice",
      "question_text": "Your question?",
      "options": ["A", "B", "C", "D"],
      "correct_answer": "B",
      "explanation": "Explanation here",
      "difficulty": "medium",
      "points": 2,
      "learning_outcome": "LO text",
      "source_section": "section-1",
      "source": "manual",
      "status": "approved",
      "reviewed_at": "2026-01-11T14:30:00Z",
      "reviewer_notes": "Manually created"
    }
  ]
}
```

Then generate:
```bash
python3 generate_handout.py \
  --input frameworks/module-X.md \
  --use-approved-questions
```

### Task 7: Extract Just the Questions (No PDF)

Questions are saved during generation:

```bash
# Generate questions only
python3 generate_handout.py \
  --input framework.md \
  --dry-run

# Questions saved to: question_banks/staging/module-X-staging.json
```

Review and approve, then access:
```bash
cat question_banks/approved/module-X.json
```

---

## Tips & Best Practices

### Question Review

- **Review in batches:** Set aside 30-60 minutes to review all questions for a module
- **Use edit sparingly:** Most AI questions are high quality; minor edits are fine
- **Reject obviously wrong:** Low-quality questions should be rejected
- **Add review notes:** Help future maintainers understand your edits

### Batch Processing

- **Review first:** Always review questions before batch generation
- **Process incrementally:** Start with modules 0-3, verify quality, then continue
- **Check logs:** Review `logs/handout_generation.log` after batch runs

### Configuration

- **Start with defaults:** Default config is well-tuned
- **Module overrides:** Use for special cases (intro/capstone modules)
- **Version control config:** Track changes to `handout_config.yaml`

### Performance

- **Use approved questions:** For quick regeneration after minor edits
- **Batch at night:** Process large batches during off-hours
- **Monitor API usage:** Track Claude API costs if processing many modules

### Quality Assurance

- **Spot check PDFs:** Review a few pages of each generated handout
- **Test printing:** Print sample pages to verify dark theme readability
- **Student feedback:** Gather feedback after first distribution

---

## Exit Codes

| Code | Meaning | Action |
|------|---------|--------|
| `0` | Success | All modules generated successfully |
| `1` | Fatal error | Check logs, fix issue, retry |
| `2` | Partial success | Some modules failed, check summary |
| `3` | Blocked by review | Review questions, then retry |
| `4` | Configuration error | Fix `handout_config.yaml`, retry |

Check exit code in shell:
```bash
python3 generate_handout.py --input framework.md
echo $?  # Shows exit code
```

---

## Next Steps

- **Review [API_REFERENCE.md](API_REFERENCE.md)** for Python API usage
- **Check [TROUBLESHOOTING.md](TROUBLESHOOTING.md)** for common issues
- **Read [PRD](PRD-Student-Handout-Generator-v2.md)** for detailed specs
- **Explore [ARCHITECTURE.md](ARCHITECTURE.md)** for system design

---

**Usage guide version:** 1.0
**Last updated:** 2026-01-11
