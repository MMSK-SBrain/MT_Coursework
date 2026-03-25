# Changelog

All notable changes to the Student Handout Generator project.

---

## [1.0.0] - 2026-01-11

### Initial Release

Production-ready release with all 12 user stories complete.

### Added

#### Story 1: Foundation & Configuration
- Configuration management system with YAML validation
- Centralized error handling framework
- Security utilities for input validation and path sanitization
- Comprehensive logging system (file + console)
- Data models for all core entities (FrameworkMetadata, ContentSection, Question, ImageReference, HandoutDocument)
- Requirements.txt with all dependencies

#### Story 2: Framework Parser
- Markdown file parser supporting up to 5000 lines
- YAML frontmatter metadata extraction
- Hierarchical section parsing (H1-H6 headings)
- Code block, table, and list handling
- Image reference detection
- UTF-8 encoding support

#### Story 3: Content Transformer
- Instructor content filtering (removes production notes, pedagogy sections)
- Pattern-based exclusion rules (configurable via YAML)
- HTML comment removal (`<!-- INSTRUCTOR ONLY -->`)
- Content cleaning and normalization
- Section-level filtering with `include_in_handout` flag

#### Story 4: Manual Question Bank Support
- JSON question bank loader with schema validation
- Support for 5 question types:
  - Multiple Choice
  - True/False
  - Short Answer
  - Reflection
  - Application Scenario
- Contextual question placement algorithm
- Manual question creation workflow

#### Story 5: Image Processor
- Image detection from markdown references
- Path resolution with base directory support
- Image validation (PNG, JPG, SVG formats)
- Automatic resizing (max 500px width, maintains aspect ratio)
- Dark background optimization
- Placeholder generation for missing images (#21262D background)
- Image metadata extraction (dimensions, alt text, captions)

#### Story 6: Layout Engine
- Dark theme HTML template system (Jinja2)
- Dark theme CSS stylesheet (GitHub Dark inspired)
- Content assembly (content + questions + images)
- Table of contents generation with hyperlinks
- Question box templates with color-coded borders by type:
  - Blue (#58A6FF): Multiple Choice, True/False
  - Green (#3FB950): Short Answer, Application
  - Purple (#A371F7): Reflection
- Code block templates with syntax highlighting
- Pagination handling (avoid orphan headings)
- Header/footer with module title and page numbers

#### Story 7: PDF Renderer
- WeasyPrint integration for PDF generation
- Dark theme rendering (#0D1117 background, #E6EDF3 text)
- Font embedding (Inter, JetBrains Mono)
- Image embedding with proper scaling
- A4 page configuration with 20-25mm margins
- Header/footer generation
- PDF validation
- Print-ready output (<10MB per handout)

#### Story 8: CLI - Single Module Generation
- Command-line interface with argparse
- Progress indicators during generation
- Dry-run validation mode
- Verbose logging mode
- Custom output directory support
- Configuration file override
- Multiple output formats (PDF, HTML)
- Clear success/error messaging
- Processing time: 2-5 minutes per module

#### Story 9: AI Question Generator
- Anthropic Claude API integration (claude-sonnet-4-20250514)
- Contextual question generation (5-10 per section)
- All 5 question types supported
- Learning outcome alignment
- Configurable prompts in `src/ai_prompts.py`
- Retry logic with exponential backoff (3 attempts)
- API timeout handling (60s default, configurable)
- Staging file system for pending review
- Environment variable API key management (ANTHROPIC_API_KEY)

#### Story 10: Question Review Interface
- Interactive terminal UI using Rich library
- Question display with full context:
  - Question text and type
  - Answer options
  - Suggested correct answer
  - Source section
  - Learning outcome
- Review actions: Approve, Edit, Reject, Skip, Quit
- Edit workflow for all question fields
- Approved questions → `question_banks/approved/`
- Rejected questions → `question_banks/rejected/` (reference)
- Resume capability for interrupted sessions
- Review statistics and summary report
- Handout generation blocks if questions pending review

#### Story 11: Batch Processor
- Multi-module batch processing
- Pre-flight question review status check
- Sequential processing with progress indication
- Continue-on-failure error handling
- Summary report (successful/failed/blocked)
- Module filtering (process specific modules)
- Archive previous versions in `/archive/` subdirectory
- Processing time: <30 minutes for 11 modules

#### Story 12: Testing & QA
- Comprehensive test suite (80%+ coverage)
- Unit tests for all components
- Integration tests for full pipeline
- Mock Claude API for tests
- Test fixtures (sample frameworks, questions, images)
- Security validation tests
- Performance tests for large files
- pytest configuration with coverage reporting

### Configuration

- `handout_config.yaml` - Main configuration file with:
  - Global settings (output directory, page size, fonts)
  - Dark theme branding (full color palette)
  - Question configuration (types, AI settings, directories)
  - Content transformation rules
  - Image processing settings
  - PDF output specifications
  - Module-specific overrides

### Documentation

- `README.md` - Project overview and quick start
- `INSTALLATION.md` - Complete installation guide
- `USAGE_GUIDE.md` - Comprehensive usage guide
- `API_REFERENCE.md` - Python API documentation
- `TROUBLESHOOTING.md` - Common issues and solutions
- `PRD-Student-Handout-Generator-v2.md` - Product requirements
- `ARCHITECTURE.md` - System architecture and implementation plan

### Features

- Automated PDF handout generation from markdown frameworks
- AI-powered question generation with mandatory review workflow
- Professional dark theme design (GitHub Dark inspired)
- Contextual question placement (after major sections)
- Image embedding with intelligent placeholders
- Table of contents with page numbers
- Headers/footers with module metadata
- Batch processing for entire courses
- Question review status tracking
- Archive versioning
- Dry-run validation mode
- Verbose logging
- Multiple output formats (PDF, HTML)
- Configuration via YAML
- Secure API key management
- Input validation and sanitization
- Comprehensive error handling
- Progress tracking during generation

### CLI Commands

- `--input` / `-i` - Generate handout from framework file
- `--batch` / `-b` - Batch process all modules
- `--course` / `-c` - Specify course name
- `--modules` / `-m` - Process specific modules
- `--review-questions` - Start interactive question review
- `--review-status` - Show question review status
- `--use-approved-questions` - Skip AI, use approved bank
- `--force-unreviewed` - Generate with unreviewed questions (adds warning)
- `--regenerate-questions` - Re-generate AI questions
- `--output` / `-o` - Custom output directory
- `--config` - Custom configuration file
- `--formats` / `-f` - Output formats (pdf,html)
- `--dry-run` - Validate without generating
- `--verbose` / `-v` - Verbose logging

### Exit Codes

- `0` - Success (all modules generated)
- `1` - Fatal error (system cannot proceed)
- `2` - Partial success (some modules failed in batch)
- `3` - Blocked by review (unreviewed questions)
- `4` - Configuration error

### Dependencies

- Python 3.11+
- Pandoc 3.0+
- WeasyPrint 60.0+
- Anthropic API (Claude)
- Pango, gdk-pixbuf, libffi (system libraries)
- Inter font (body text)
- JetBrains Mono font (code blocks)

### Performance

- Single module: 2-5 minutes (with AI generation)
- Single module: ~30 seconds (with approved questions)
- Batch (11 modules): <30 minutes
- PDF size: <10MB per handout (with images)

### Security

- API key stored in environment variables only
- Input path validation (prevent path traversal)
- Configuration schema validation
- Markdown sanitization
- Atomic file writes
- Secure error messages (no secrets logged)

---

## Future Enhancements

### Planned for v1.1

- Light theme option for printing
- Answer key generation (separate PDF)
- Question difficulty auto-calibration
- Batch question approval interface
- Performance optimizations

### Planned for v1.2

- HTML output with interactive elements
- Glossary auto-generation
- Question bank sharing across modules
- Parallel processing support

### Planned for v2.0

- Web-based configuration interface
- Multi-course management
- Analytics on question quality
- Cloud storage integration
- LMS export formats (SCORM)

---

## Version History

| Version | Date | Description |
|---------|------|-------------|
| 1.0.0 | 2026-01-11 | Initial production release with all 12 stories |
| 0.9.0 | 2026-01-10 | Beta release (Stories 1-11 complete) |
| 0.5.0 | 2026-01-08 | Alpha release (Stories 1-7 complete) |
| 0.1.0 | 2026-01-05 | Proof of concept (Story 1 complete) |

---

## Migration Guide

### From Manual Handout Creation

If you were previously creating handouts manually:

1. **Prepare framework files:**
   - Ensure YAML frontmatter with required metadata
   - Mark instructor-only sections appropriately

2. **Create question banks:**
   - Convert existing questions to JSON format
   - Place in `question_banks/approved/`

3. **Organize images:**
   - Move images to `images/<course>/<module>/` directory
   - Update markdown references

4. **Generate first handout:**
   ```bash
   python3 generate_handout.py --input frameworks/module-0.md
   ```

5. **Review output:**
   - Verify content correctness
   - Check image placement
   - Review question placement

### From v0.x to v1.0

No migration needed for first release.

---

## Known Issues

### v1.0.0

- **WeasyPrint on Apple Silicon:** Requires manual compilation flags during installation (documented in INSTALLATION.md)
- **Large images (>10MB):** Skipped with warning (recommended to compress before processing)
- **HTML comments in code blocks:** May be incorrectly filtered if they match exclusion patterns (workaround: use different markers)
- **Table of contents page numbers:** May be off by 1-2 pages for very long documents (WeasyPrint pagination quirk)

---

## Contributors

**Course Generator Team**
- Initial development and release

---

## License

See LICENSE file for details.

---

**Changelog maintained according to:** [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)
**Versioning follows:** [Semantic Versioning](https://semver.org/)
