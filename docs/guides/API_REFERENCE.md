# API Reference

Python API documentation for the Student Handout Generator system.

---

## Table of Contents

- [Overview](#overview)
- [Core Classes](#core-classes)
- [Data Models](#data-models)
- [Integration Patterns](#integration-patterns)
- [Usage Examples](#usage-examples)

---

## Overview

The Student Handout Generator provides a Python API for programmatic access to all features.

### Import Structure

```python
from src.config_manager import ConfigManager
from src.framework_parser import FrameworkParser
from src.content_transformer import ContentTransformer
from src.question_generator import QuestionGenerator
from src.question_reviewer import QuestionReviewer
from src.question_loader import QuestionLoader
from src.image_processor import ImageProcessor
from src.layout_engine import LayoutEngine
from src.pdf_renderer import PDFRenderer
from src.batch_processor import BatchProcessor
from src.models import (
    FrameworkMetadata,
    ContentSection,
    Question,
    ImageReference,
    HandoutDocument
)
```

---

## Core Classes

### ConfigManager

Manages configuration loading and validation.

#### Class Definition

```python
class ConfigManager:
    """Configuration manager for handout generation system."""

    def __init__(self, config_path: str = "handout_config.yaml"):
        """Initialize config manager.

        Args:
            config_path: Path to YAML configuration file
        """

    @classmethod
    def from_file(cls, config_path: str) -> 'ConfigManager':
        """Load configuration from file.

        Args:
            config_path: Path to YAML config file

        Returns:
            ConfigManager instance

        Raises:
            FileNotFoundError: If config file not found
            ValidationError: If config invalid
        """

    def get(self, key: str, default: Any = None) -> Any:
        """Get configuration value.

        Args:
            key: Dot-notation key (e.g., "questions.enabled")
            default: Default value if key not found

        Returns:
            Configuration value
        """

    def get_module_config(self, module_id: str) -> dict:
        """Get merged config for specific module.

        Args:
            module_id: Module identifier (e.g., "module-0")

        Returns:
            Merged global + module-specific config
        """

    def validate(self) -> bool:
        """Validate configuration against schema.

        Returns:
            True if valid

        Raises:
            ValidationError: If invalid with details
        """
```

#### Usage Example

```python
# Load default config
config = ConfigManager()

# Load custom config
config = ConfigManager.from_file("custom_config.yaml")

# Get configuration values
output_dir = config.get("global.output_directory")
questions_enabled = config.get("questions.enabled", default=True)

# Get module-specific config
module_config = config.get_module_config("module-0")
questions_per_section = module_config.get("questions.questions_per_section")

# Validate configuration
try:
    config.validate()
    print("Configuration valid")
except ValidationError as e:
    print(f"Invalid config: {e}")
```

---

### FrameworkParser

Parses markdown framework files.

#### Class Definition

```python
class FrameworkParser:
    """Parser for framework markdown files."""

    def __init__(self, config: ConfigManager):
        """Initialize parser.

        Args:
            config: Configuration manager instance
        """

    def parse_file(self, file_path: str) -> tuple[FrameworkMetadata, list[ContentSection]]:
        """Parse framework file.

        Args:
            file_path: Path to markdown file

        Returns:
            Tuple of (metadata, sections)

        Raises:
            FileNotFoundError: If file not found
            ParsingError: If parsing fails
        """

    def extract_metadata(self, content: str) -> FrameworkMetadata:
        """Extract YAML frontmatter metadata.

        Args:
            content: Raw file content

        Returns:
            FrameworkMetadata object

        Raises:
            MetadataError: If metadata missing or invalid
        """

    def parse_sections(self, content: str) -> list[ContentSection]:
        """Parse content into hierarchical sections.

        Args:
            content: Markdown content (without frontmatter)

        Returns:
            List of top-level ContentSection objects
        """

    def detect_images(self, content: str) -> list[str]:
        """Detect image references in markdown.

        Args:
            content: Markdown content

        Returns:
            List of image paths
        """
```

#### Usage Example

```python
parser = FrameworkParser(config)

# Parse file
metadata, sections = parser.parse_file("frameworks/module-0.md")

print(f"Module: {metadata.module_title}")
print(f"Sections: {len(sections)}")

# Access section hierarchy
for section in sections:
    print(f"- {section.title} (Level {section.level})")
    for subsection in section.subsections:
        print(f"  - {subsection.title}")

# Detect images
images = parser.detect_images(open("frameworks/module-0.md").read())
print(f"Images found: {len(images)}")
```

---

### ContentTransformer

Transforms content for student handouts.

#### Class Definition

```python
class ContentTransformer:
    """Transforms framework content for student handouts."""

    def __init__(self, config: ConfigManager):
        """Initialize transformer.

        Args:
            config: Configuration manager instance
        """

    def transform(self, sections: list[ContentSection]) -> list[ContentSection]:
        """Transform sections by applying filters.

        Args:
            sections: List of content sections

        Returns:
            Filtered and transformed sections
        """

    def should_exclude_section(self, section: ContentSection) -> bool:
        """Check if section should be excluded.

        Args:
            section: Content section

        Returns:
            True if section should be excluded
        """

    def clean_content(self, content: str) -> str:
        """Clean content by removing instructor-only markers.

        Args:
            content: Raw markdown content

        Returns:
            Cleaned content
        """
```

#### Usage Example

```python
transformer = ContentTransformer(config)

# Transform sections
cleaned_sections = transformer.transform(sections)

print(f"Original: {len(sections)} sections")
print(f"Cleaned: {len(cleaned_sections)} sections")

# Check individual section
if transformer.should_exclude_section(section):
    print(f"Excluding: {section.title}")

# Clean content
cleaned = transformer.clean_content(section.content)
```

---

### QuestionGenerator

Generates questions using AI.

#### Class Definition

```python
class QuestionGenerator:
    """AI-powered question generator."""

    def __init__(self, config: ConfigManager):
        """Initialize generator.

        Args:
            config: Configuration manager instance

        Raises:
            APIKeyError: If ANTHROPIC_API_KEY not set
        """

    def generate_for_module(
        self,
        metadata: FrameworkMetadata,
        sections: list[ContentSection]
    ) -> list[Question]:
        """Generate questions for entire module.

        Args:
            metadata: Framework metadata
            sections: Content sections

        Returns:
            List of generated questions

        Raises:
            APIError: If API call fails after retries
        """

    def generate_for_section(
        self,
        section: ContentSection,
        learning_outcome: str | None = None
    ) -> list[Question]:
        """Generate questions for single section.

        Args:
            section: Content section
            learning_outcome: Associated learning outcome

        Returns:
            List of questions for section
        """

    def save_to_staging(
        self,
        module_id: str,
        questions: list[Question]
    ) -> str:
        """Save questions to staging file.

        Args:
            module_id: Module identifier
            questions: List of questions

        Returns:
            Path to staging file
        """
```

#### Usage Example

```python
generator = QuestionGenerator(config)

# Generate for entire module
questions = generator.generate_for_module(metadata, sections)
print(f"Generated {len(questions)} questions")

# Generate for specific section
section_questions = generator.generate_for_section(
    section=sections[0],
    learning_outcome="Understand ML fundamentals"
)

# Save to staging
staging_path = generator.save_to_staging("module-0", questions)
print(f"Saved to: {staging_path}")
```

---

### QuestionReviewer

Interactive question review interface.

#### Class Definition

```python
class QuestionReviewer:
    """Interactive terminal-based question reviewer."""

    def __init__(self, config: ConfigManager):
        """Initialize reviewer.

        Args:
            config: Configuration manager instance
        """

    def start_session(self, module_id: str) -> ReviewSession:
        """Start interactive review session.

        Args:
            module_id: Module identifier

        Returns:
            ReviewSession with statistics

        Raises:
            FileNotFoundError: If staging file not found
        """

    def get_review_status(self, module_id: str) -> dict:
        """Get review status for module.

        Args:
            module_id: Module identifier

        Returns:
            Dict with counts: {pending, approved, rejected}
        """

    def load_approved_questions(self, module_id: str) -> list[Question]:
        """Load approved questions for module.

        Args:
            module_id: Module identifier

        Returns:
            List of approved questions

        Raises:
            FileNotFoundError: If no approved questions
        """
```

#### Usage Example

```python
reviewer = QuestionReviewer(config)

# Check status
status = reviewer.get_review_status("module-0")
print(f"Pending: {status['pending']}")
print(f"Approved: {status['approved']}")

# Start review session (interactive)
session = reviewer.start_session("module-0")

# After session
print(f"Reviewed: {session.questions_total}")
print(f"Approved: {session.questions_approved}")
print(f"Rejected: {session.questions_rejected}")

# Load approved questions
approved = reviewer.load_approved_questions("module-0")
print(f"Loaded {len(approved)} approved questions")
```

---

### QuestionLoader

Loads questions from JSON files.

#### Class Definition

```python
class QuestionLoader:
    """Loads and manages question banks."""

    def __init__(self, config: ConfigManager):
        """Initialize loader.

        Args:
            config: Configuration manager instance
        """

    def load_approved(self, module_id: str) -> list[Question]:
        """Load approved question bank.

        Args:
            module_id: Module identifier

        Returns:
            List of approved questions

        Raises:
            FileNotFoundError: If bank doesn't exist
        """

    def load_staging(self, module_id: str) -> list[Question]:
        """Load staging questions.

        Args:
            module_id: Module identifier

        Returns:
            List of staging questions
        """

    def validate_schema(self, questions: list[Question]) -> bool:
        """Validate questions against schema.

        Args:
            questions: List of questions

        Returns:
            True if valid

        Raises:
            ValidationError: If invalid
        """
```

#### Usage Example

```python
loader = QuestionLoader(config)

# Load approved questions
try:
    questions = loader.load_approved("module-0")
    print(f"Loaded {len(questions)} questions")
except FileNotFoundError:
    print("No approved questions yet")

# Validate questions
try:
    loader.validate_schema(questions)
    print("Questions valid")
except ValidationError as e:
    print(f"Invalid: {e}")
```

---

### ImageProcessor

Processes and embeds images.

#### Class Definition

```python
class ImageProcessor:
    """Image processing for handouts."""

    def __init__(self, config: ConfigManager):
        """Initialize processor.

        Args:
            config: Configuration manager instance
        """

    def process_images(
        self,
        image_paths: list[str],
        base_directory: str
    ) -> list[ImageReference]:
        """Process list of image paths.

        Args:
            image_paths: List of image paths from markdown
            base_directory: Base directory for image resolution

        Returns:
            List of ImageReference objects
        """

    def resize_image(
        self,
        image_path: str,
        max_width: int = 500
    ) -> str:
        """Resize image to max width.

        Args:
            image_path: Path to image file
            max_width: Maximum width in pixels

        Returns:
            Path to resized image

        Raises:
            ImageError: If resize fails
        """

    def create_placeholder(
        self,
        alt_text: str,
        width: int = 500,
        height: int = 300
    ) -> str:
        """Create placeholder image.

        Args:
            alt_text: Alternative text for image
            width: Placeholder width
            height: Placeholder height

        Returns:
            Path to placeholder image
        """
```

#### Usage Example

```python
processor = ImageProcessor(config)

# Process images
image_refs = processor.process_images(
    image_paths=["images/demo.png", "images/chart.jpg"],
    base_directory="courses/ml-for-engineers"
)

for ref in image_refs:
    if ref.exists:
        print(f"✓ {ref.original_path}")
    else:
        print(f"✗ {ref.original_path} (placeholder used)")

# Resize specific image
resized_path = processor.resize_image("images/large.png", max_width=500)

# Create placeholder
placeholder = processor.create_placeholder("Image not found", 500, 300)
```

---

### LayoutEngine

Assembles content into HTML layout.

#### Class Definition

```python
class LayoutEngine:
    """Layout engine for handout assembly."""

    def __init__(self, config: ConfigManager):
        """Initialize engine.

        Args:
            config: Configuration manager instance
        """

    def assemble(
        self,
        metadata: FrameworkMetadata,
        sections: list[ContentSection],
        questions: list[Question],
        images: list[ImageReference]
    ) -> str:
        """Assemble components into HTML.

        Args:
            metadata: Framework metadata
            sections: Content sections
            questions: Questions to embed
            images: Image references

        Returns:
            HTML string with dark theme styling
        """

    def generate_toc(self, sections: list[ContentSection]) -> str:
        """Generate table of contents HTML.

        Args:
            sections: Content sections

        Returns:
            TOC HTML
        """

    def place_questions(
        self,
        sections: list[ContentSection],
        questions: list[Question]
    ) -> list[ContentSection]:
        """Place questions in appropriate sections.

        Args:
            sections: Content sections
            questions: Questions to place

        Returns:
            Sections with embedded questions
        """
```

#### Usage Example

```python
engine = LayoutEngine(config)

# Assemble full handout
html = engine.assemble(
    metadata=metadata,
    sections=sections,
    questions=questions,
    images=image_refs
)

# Generate TOC separately
toc_html = engine.generate_toc(sections)

# Place questions
sections_with_questions = engine.place_questions(sections, questions)
```

---

### PDFRenderer

Renders PDF from HTML.

#### Class Definition

```python
class PDFRenderer:
    """PDF renderer using WeasyPrint."""

    def __init__(self, config: ConfigManager):
        """Initialize renderer.

        Args:
            config: Configuration manager instance

        Raises:
            ImportError: If WeasyPrint not installed
        """

    def render(
        self,
        html: str,
        output_path: str,
        metadata: FrameworkMetadata
    ) -> str:
        """Render HTML to PDF.

        Args:
            html: HTML content
            output_path: PDF output path
            metadata: Framework metadata for headers

        Returns:
            Path to generated PDF

        Raises:
            RenderError: If PDF generation fails
        """

    def validate_output(self, pdf_path: str) -> bool:
        """Validate generated PDF.

        Args:
            pdf_path: Path to PDF file

        Returns:
            True if valid

        Raises:
            ValidationError: If invalid
        """
```

#### Usage Example

```python
renderer = PDFRenderer(config)

# Render PDF
pdf_path = renderer.render(
    html=html,
    output_path="handouts/module-0/handout.pdf",
    metadata=metadata
)

print(f"PDF generated: {pdf_path}")

# Validate
try:
    renderer.validate_output(pdf_path)
    print("PDF valid")
except ValidationError as e:
    print(f"Invalid PDF: {e}")
```

---

### BatchProcessor

Batch processing orchestrator.

#### Class Definition

```python
class BatchProcessor:
    """Batch processor for multiple modules."""

    def __init__(self, config: ConfigManager):
        """Initialize processor.

        Args:
            config: Configuration manager instance
        """

    def process_course(
        self,
        course_name: str,
        module_ids: list[str] | None = None
    ) -> dict[str, ProcessingResult]:
        """Process all modules in course.

        Args:
            course_name: Course identifier
            module_ids: Specific modules to process (None = all)

        Returns:
            Dict mapping module_id to ProcessingResult
        """

    def check_review_status(
        self,
        course_name: str
    ) -> dict[str, dict]:
        """Check question review status for all modules.

        Args:
            course_name: Course identifier

        Returns:
            Dict mapping module_id to status info
        """

    def discover_modules(self, course_name: str) -> list[str]:
        """Discover all modules in course.

        Args:
            course_name: Course identifier

        Returns:
            List of module IDs
        """
```

#### Usage Example

```python
batch = BatchProcessor(config)

# Check review status first
status = batch.check_review_status("ml-for-engineers")
for module_id, info in status.items():
    print(f"{module_id}: {info['approved']}/{info['total']} approved")

# Process all modules
results = batch.process_course("ml-for-engineers")

# Check results
successful = [m for m, r in results.items() if r.success]
failed = [m for m, r in results.items() if not r.success]

print(f"Successful: {len(successful)}")
print(f"Failed: {len(failed)}")

# Process specific modules
results = batch.process_course(
    course_name="ml-for-engineers",
    module_ids=["module-0", "module-1", "module-2"]
)
```

---

## Data Models

### FrameworkMetadata

```python
@dataclass
class FrameworkMetadata:
    """Framework file metadata."""

    course_code: str           # e.g., "ML-ENG-M0"
    module_number: int         # e.g., 0
    module_title: str          # e.g., "The Hook - Welcome to ML"
    duration: str              # e.g., "1 week (self-paced)"
    video_content: str         # e.g., "~4.5 hours"
    hands_on_time: str         # e.g., "~2-3 hours"
    theory_practice_ratio: str # e.g., "70% / 30%"
    file_path: Path            # Original framework file path
    last_updated: datetime     # From file or metadata
```

**Usage:**
```python
metadata = FrameworkMetadata(
    course_code="ML-ENG-M0",
    module_number=0,
    module_title="The Hook",
    duration="1 week",
    video_content="4.5 hours",
    hands_on_time="2-3 hours",
    theory_practice_ratio="70/30",
    file_path=Path("frameworks/module-0.md"),
    last_updated=datetime.now()
)

print(f"Module {metadata.module_number}: {metadata.module_title}")
```

---

### ContentSection

```python
@dataclass
class ContentSection:
    """Content section with hierarchy."""

    id: str                    # Unique identifier
    level: int                 # Header level (1-6)
    title: str                 # Section title
    content: str               # Markdown content
    subsections: list['ContentSection']  # Nested sections
    metadata: dict[str, Any]   # Additional metadata
    include_in_handout: bool   # Filter flag
    question_count: int        # Questions to add
```

**Usage:**
```python
section = ContentSection(
    id="session-1",
    level=2,
    title="Introduction to ML",
    content="# Content here...",
    subsections=[],
    metadata={"learning_outcome": "Understand ML basics"},
    include_in_handout=True,
    question_count=7
)

# Traverse hierarchy
for subsection in section.subsections:
    print(f"  - {subsection.title}")
```

---

### Question

```python
@dataclass
class Question:
    """Question object."""

    id: str                    # Unique ID (e.g., "m0-s1-q1")
    type: QuestionType         # Enum: MULTIPLE_CHOICE, TRUE_FALSE, etc.
    question_text: str         # The question
    options: list[str] | None  # For MCQ/T-F
    correct_answer: str | None # Correct answer
    explanation: str | None    # Answer explanation
    points: int                # Score value
    difficulty: str            # "easy", "medium", "hard"
    learning_outcome: str | None  # Associated LO
    source_section: str        # Section ID
    source: str                # "ai_generated" or "manual"
    status: str                # "pending_review", "approved", "rejected"
    reviewed_at: datetime | None  # Review timestamp
    reviewer_notes: str | None # Review notes
```

**Usage:**
```python
from src.models import QuestionType

question = Question(
    id="m0-s1-q1",
    type=QuestionType.MULTIPLE_CHOICE,
    question_text="What is ML?",
    options=["A", "B", "C", "D"],
    correct_answer="B",
    explanation="ML is...",
    points=1,
    difficulty="easy",
    learning_outcome="Understand ML definition",
    source_section="session-1",
    source="ai_generated",
    status="approved",
    reviewed_at=datetime.now(),
    reviewer_notes=None
)
```

---

### ImageReference

```python
@dataclass
class ImageReference:
    """Image reference with metadata."""

    id: str                    # Unique identifier
    original_path: str         # Path in markdown
    resolved_path: Path | None # Actual file path
    alt_text: str              # Image description
    caption: str | None        # Figure caption
    width: int                 # Display width
    height: int                # Display height
    exists: bool               # File found flag
    placeholder_used: bool     # Placeholder substituted
```

**Usage:**
```python
image_ref = ImageReference(
    id="img-1",
    original_path="../images/demo.png",
    resolved_path=Path("images/demo.png"),
    alt_text="ML Demo Screenshot",
    caption="Figure 1: ML Demo",
    width=500,
    height=300,
    exists=True,
    placeholder_used=False
)

if image_ref.exists:
    print(f"Image found: {image_ref.resolved_path}")
```

---

### HandoutDocument

```python
@dataclass
class HandoutDocument:
    """Complete handout document."""

    metadata: FrameworkMetadata
    sections: list[ContentSection]
    questions: list[Question]
    images: list[ImageReference]
    toc: list[TOCEntry]
    generation_timestamp: datetime
    config_used: dict[str, Any]
    output_path: Path
    warnings: list[str]        # Non-fatal issues
    question_review_complete: bool
```

**Usage:**
```python
handout = HandoutDocument(
    metadata=metadata,
    sections=sections,
    questions=questions,
    images=image_refs,
    toc=toc_entries,
    generation_timestamp=datetime.now(),
    config_used=config.to_dict(),
    output_path=Path("handouts/module-0/handout.pdf"),
    warnings=["Image not found: demo.png"],
    question_review_complete=True
)

print(f"Generated: {handout.output_path}")
print(f"Warnings: {len(handout.warnings)}")
```

---

## Integration Patterns

### Pattern 1: Complete Pipeline

```python
from src import (
    ConfigManager, FrameworkParser, ContentTransformer,
    QuestionGenerator, QuestionReviewer, ImageProcessor,
    LayoutEngine, PDFRenderer
)

# Initialize components
config = ConfigManager()
parser = FrameworkParser(config)
transformer = ContentTransformer(config)
generator = QuestionGenerator(config)
reviewer = QuestionReviewer(config)
image_proc = ImageProcessor(config)
layout = LayoutEngine(config)
renderer = PDFRenderer(config)

# Parse framework
metadata, sections = parser.parse_file("framework.md")

# Transform content
sections = transformer.transform(sections)

# Generate questions
questions = generator.generate_for_module(metadata, sections)
staging_path = generator.save_to_staging("module-0", questions)

# Review questions (interactive)
session = reviewer.start_session("module-0")

# Load approved questions
questions = reviewer.load_approved_questions("module-0")

# Process images
image_paths = parser.detect_images(open("framework.md").read())
images = image_proc.process_images(image_paths, "images/")

# Assemble layout
html = layout.assemble(metadata, sections, questions, images)

# Render PDF
pdf_path = renderer.render(html, "handout.pdf", metadata)

print(f"Complete! {pdf_path}")
```

---

### Pattern 2: Question Management

```python
from src import ConfigManager, QuestionGenerator, QuestionReviewer

config = ConfigManager()
generator = QuestionGenerator(config)
reviewer = QuestionReviewer(config)

# Generate questions
questions = generator.generate_for_module(metadata, sections)
generator.save_to_staging("module-0", questions)

# Check status
status = reviewer.get_review_status("module-0")
if status["pending"] > 0:
    print(f"{status['pending']} questions need review")

# Review (interactive)
session = reviewer.start_session("module-0")

# Use approved questions
approved = reviewer.load_approved_questions("module-0")
print(f"Using {len(approved)} approved questions")
```

---

### Pattern 3: Batch Processing

```python
from src import ConfigManager, BatchProcessor

config = ConfigManager()
batch = BatchProcessor(config)

# Check status
status = batch.check_review_status("ml-for-engineers")

# Process all modules
results = batch.process_course("ml-for-engineers")

# Report results
for module_id, result in results.items():
    if result.success:
        print(f"✓ {module_id}: {result.output_path}")
    elif result.blocked_by_review:
        print(f"⏸ {module_id}: Needs review")
    else:
        print(f"✗ {module_id}: {result.error}")
```

---

## Usage Examples

### Example 1: Custom Question Bank

```python
from src import ConfigManager, QuestionLoader
from src.models import Question, QuestionType
from datetime import datetime

config = ConfigManager()
loader = QuestionLoader(config)

# Create custom questions
questions = [
    Question(
        id="custom-q1",
        type=QuestionType.MULTIPLE_CHOICE,
        question_text="Custom question?",
        options=["A", "B", "C", "D"],
        correct_answer="B",
        explanation="Because...",
        points=2,
        difficulty="medium",
        learning_outcome="LO-1",
        source_section="intro",
        source="manual",
        status="approved",
        reviewed_at=datetime.now(),
        reviewer_notes="Manually created"
    )
]

# Save to approved bank
import json
bank_path = "question_banks/approved/module-custom.json"
with open(bank_path, "w") as f:
    json.dump({
        "module_id": "module-custom",
        "questions": [q.__dict__ for q in questions]
    }, f, indent=2, default=str)

# Load and use
loaded = loader.load_approved("module-custom")
print(f"Loaded {len(loaded)} custom questions")
```

---

### Example 2: Image Placeholder Generation

```python
from src import ConfigManager, ImageProcessor

config = ConfigManager()
processor = ImageProcessor(config)

# Process with missing images
image_paths = ["images/found.png", "images/missing.png"]
refs = processor.process_images(image_paths, ".")

for ref in refs:
    if ref.placeholder_used:
        print(f"Placeholder created for: {ref.original_path}")
        print(f"  Alt text: {ref.alt_text}")
        print(f"  Placeholder path: {ref.resolved_path}")
```

---

### Example 3: Configuration Override

```python
from src import ConfigManager

# Load base config
config = ConfigManager()

# Override specific values programmatically
config._config["questions"]["questions_per_section"] = 10
config._config["branding"]["colors"]["accent_blue"] = "#0000FF"

# Use modified config
from src import QuestionGenerator
generator = QuestionGenerator(config)
# Will use 10 questions per section
```

---

**API Reference version:** 1.0
**Last updated:** 2026-01-11
