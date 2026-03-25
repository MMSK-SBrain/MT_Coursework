"""
Pytest Configuration and Shared Fixtures for Student Handout Generator

This module provides shared fixtures across all test files for:
- Test configuration
- Sample framework files
- Sample questions
- Mock API responses
- Temporary directories
- Test data cleanup
"""

import json
import pytest
import tempfile
import shutil
from pathlib import Path
from datetime import datetime
from unittest.mock import Mock, MagicMock
from typing import Dict, Any, List

from src.config_manager import ConfigManager
from src.models import (
    Question, QuestionType, QuestionStatus, QuestionDifficulty, QuestionSource,
    FrameworkMetadata, ContentSection, ImageReference, HandoutDocument, TOCEntry
)


# ============================================================================
# CONFIGURATION FIXTURES
# ============================================================================

@pytest.fixture
def test_config() -> ConfigManager:
    """Load test configuration with safe defaults"""
    config_dict = {
        "global": {
            "output_directory": "./test_output",
            "archive_old_versions": False,
            "page_size": "A4"
        },
        "branding": {
            "theme": "dark",
            "colors": {
                "background_primary": "#0D1117",
                "background_secondary": "#161B22",
                "background_tertiary": "#21262D",
                "text_primary": "#E6EDF3",
                "text_secondary": "#8B949E",
                "text_muted": "#484F58",
                "accent_blue": "#58A6FF",
                "accent_green": "#3FB950",
                "accent_orange": "#D29922",
                "accent_red": "#F85149",
                "accent_purple": "#A371F7",
                "border_default": "#30363D"
            }
        },
        "questions": {
            "enabled": True,
            "questions_per_section": 5,
            "require_review": True,
            "types": ["multiple_choice", "true_false", "short_answer", "reflection", "application"],
            "ai_generation": {
                "enabled": True,
                "provider": "anthropic",
                "api_key_env_var": "ANTHROPIC_API_KEY",
                "model": "claude-sonnet-4-20250514",
                "max_retries": 3,
                "timeout_seconds": 60
            },
            "staging_directory": "./test_question_banks/staging",
            "approved_directory": "./test_question_banks/approved",
            "rejected_directory": "./test_question_banks/rejected"
        },
        "content": {
            "exclude_patterns": [
                "## Video Production Notes",
                "### For Instructors",
                "<!-- INSTRUCTOR ONLY -->"
            ],
            "include_toc": True,
            "include_learning_outcomes": True,
            "include_assessments": True
        },
        "images": {
            "base_directory": "./test_images",
            "max_width": 500,
            "placeholder_on_missing": True,
            "placeholder_color": "#21262D",
            "formats_supported": ["png", "jpg", "jpeg", "svg"]
        },
        "pdf": {
            "margins": {
                "top": "20mm",
                "bottom": "20mm",
                "left": "25mm",
                "right": "25mm"
            },
            "header": {
                "enabled": True,
                "format": "{module_title}",
                "color": "#8B949E"
            },
            "footer": {
                "enabled": True,
                "format": "Page {page_number}",
                "color": "#484F58"
            },
            "page_break_before_sections": True
        }
    }

    return ConfigManager(config_dict)


@pytest.fixture
def minimal_config() -> Dict[str, Any]:
    """Minimal configuration for testing edge cases"""
    return {
        "global": {
            "output_directory": "./test_output"
        },
        "questions": {
            "enabled": False,
            "require_review": True
        }
    }


# ============================================================================
# FRAMEWORK FILE FIXTURES
# ============================================================================

@pytest.fixture
def fixtures_dir() -> Path:
    """Get the fixtures directory path"""
    return Path(__file__).parent / "fixtures"


@pytest.fixture
def sample_framework_small(fixtures_dir) -> Path:
    """Path to small sample framework file"""
    return fixtures_dir / "sample_framework_small.md"


@pytest.fixture
def sample_framework_malformed(fixtures_dir) -> Path:
    """Path to malformed framework file"""
    return fixtures_dir / "sample_framework_malformed.md"


@pytest.fixture
def sample_framework_content() -> str:
    """Complete sample framework markdown content"""
    return """---
course_code: TEST-M0
module_number: 0
module_title: "Test Module - Introduction"
duration: "1 week"
video_content: "~2 hours"
hands_on_time: "~1 hour"
theory_practice_ratio: "60% / 40%"
version: "1.0"
---

# Test Module - Introduction

## Session 1: Getting Started

This is the introduction session content.

### Learning Outcomes

- Understand basic concepts
- Apply fundamental principles
- Practice with examples

### Key Concepts

Machine learning is the science of getting computers to learn without being explicitly programmed.

```python
# Example code
import numpy as np
data = np.array([1, 2, 3, 4, 5])
print(data.mean())
```

### Demo Applications

Here are some demo applications:
- Stock predictor
- Face detection
- Sentiment analyzer

![Demo Application](../images/demo-app.png)

## Session 2: Deep Dive

This section goes deeper into the concepts.

### Advanced Topics

More advanced content here with mathematical formulas and detailed explanations.

### Practice Exercise

Try building your own application using the concepts learned.
"""


# ============================================================================
# QUESTION FIXTURES
# ============================================================================

@pytest.fixture
def sample_questions() -> List[Question]:
    """Sample question bank for testing"""
    return [
        Question(
            id="test-q1",
            type=QuestionType.MULTIPLE_CHOICE,
            question_text="What is machine learning?",
            options=[
                "A type of database",
                "A programming language",
                "Getting computers to learn without explicit programming",
                "A cloud computing service"
            ],
            correct_answer="C",
            explanation="Machine learning is the science of getting computers to learn without being explicitly programmed.",
            points=1,
            difficulty=QuestionDifficulty.EASY,
            learning_outcome="Understand basic ML concepts",
            source_section="session-1-introduction",
            source=QuestionSource.AI_GENERATED,
            status=QuestionStatus.APPROVED,
            reviewed_at=datetime.now(),
            reviewer_notes=None
        ),
        Question(
            id="test-q2",
            type=QuestionType.TRUE_FALSE,
            question_text="Python is commonly used for machine learning.",
            options=["True", "False"],
            correct_answer="True",
            explanation="Python is one of the most popular languages for ML due to its rich ecosystem.",
            points=1,
            difficulty=QuestionDifficulty.EASY,
            learning_outcome="Recognize ML tools",
            source_section="session-1-introduction",
            source=QuestionSource.AI_GENERATED,
            status=QuestionStatus.APPROVED,
            reviewed_at=datetime.now(),
            reviewer_notes=None
        ),
        Question(
            id="test-q3",
            type=QuestionType.SHORT_ANSWER,
            question_text="Name two popular Python libraries for machine learning.",
            options=None,
            correct_answer="NumPy, scikit-learn (or TensorFlow, PyTorch, etc.)",
            explanation="Common ML libraries include NumPy, scikit-learn, TensorFlow, and PyTorch.",
            points=2,
            difficulty=QuestionDifficulty.MEDIUM,
            learning_outcome="Identify ML tools",
            source_section="session-1-introduction",
            source=QuestionSource.AI_GENERATED,
            status=QuestionStatus.APPROVED,
            reviewed_at=datetime.now(),
            reviewer_notes=None
        ),
        Question(
            id="test-q4",
            type=QuestionType.REFLECTION,
            question_text="How might machine learning apply to your industry or work?",
            options=None,
            correct_answer=None,
            explanation="Reflect on practical applications in your context.",
            points=2,
            difficulty=QuestionDifficulty.EASY,
            learning_outcome="Connect ML to personal context",
            source_section="session-2-deep-dive",
            source=QuestionSource.AI_GENERATED,
            status=QuestionStatus.APPROVED,
            reviewed_at=datetime.now(),
            reviewer_notes=None
        ),
        Question(
            id="test-q5",
            type=QuestionType.APPLICATION,
            question_text="You need to predict house prices. What type of ML problem is this?",
            options=None,
            correct_answer="Regression problem - predicting continuous numerical values",
            explanation="Predicting prices is a regression task since we're predicting continuous values.",
            points=3,
            difficulty=QuestionDifficulty.MEDIUM,
            learning_outcome="Apply ML concepts",
            source_section="session-2-deep-dive",
            source=QuestionSource.AI_GENERATED,
            status=QuestionStatus.APPROVED,
            reviewed_at=datetime.now(),
            reviewer_notes=None
        )
    ]


@pytest.fixture
def pending_questions() -> List[Question]:
    """Questions pending review for testing"""
    return [
        Question(
            id="pending-q1",
            type=QuestionType.MULTIPLE_CHOICE,
            question_text="What is supervised learning?",
            options=["Learning with labeled data", "Learning without labels", "Reinforcement learning", "None of above"],
            correct_answer="A",
            explanation="Supervised learning uses labeled training data.",
            points=1,
            difficulty=QuestionDifficulty.EASY,
            learning_outcome="Understand ML types",
            source_section="session-1",
            source=QuestionSource.AI_GENERATED,
            status=QuestionStatus.PENDING_REVIEW,
            reviewed_at=None,
            reviewer_notes=None
        )
    ]


@pytest.fixture
def sample_questions_json(sample_questions) -> str:
    """JSON representation of sample questions"""
    questions_dict = {
        "module_id": "test-module-0",
        "module_title": "Test Module - Introduction",
        "version": "1.0",
        "last_reviewed": datetime.now().isoformat(),
        "questions": [q.to_dict() for q in sample_questions]
    }
    return json.dumps(questions_dict, indent=2)


# ============================================================================
# METADATA & CONTENT FIXTURES
# ============================================================================

@pytest.fixture
def sample_metadata() -> FrameworkMetadata:
    """Sample framework metadata"""
    return FrameworkMetadata(
        course_code="TEST-M0",
        module_number=0,
        module_title="Test Module - Introduction",
        duration="1 week",
        video_content="~2 hours",
        hands_on_time="~1 hour",
        theory_practice_ratio="60% / 40%",
        file_path=Path("/test/framework.md"),
        last_updated=datetime.now(),
        version="1.0"
    )


@pytest.fixture
def sample_sections() -> List[ContentSection]:
    """Sample content sections hierarchy"""
    return [
        ContentSection(
            id="session-1",
            level=2,
            title="Session 1: Getting Started",
            content="This is the introduction session content.",
            subsections=[
                ContentSection(
                    id="session-1-learning",
                    level=3,
                    title="Learning Outcomes",
                    content="- Understand basic concepts\n- Apply fundamental principles",
                    subsections=[],
                    metadata={},
                    include_in_handout=True,
                    question_count=2
                ),
                ContentSection(
                    id="session-1-concepts",
                    level=3,
                    title="Key Concepts",
                    content="Machine learning is the science of getting computers to learn.",
                    subsections=[],
                    metadata={},
                    include_in_handout=True,
                    question_count=1
                )
            ],
            metadata={},
            include_in_handout=True,
            question_count=3
        ),
        ContentSection(
            id="session-2",
            level=2,
            title="Session 2: Deep Dive",
            content="This section goes deeper into the concepts.",
            subsections=[],
            metadata={},
            include_in_handout=True,
            question_count=2
        )
    ]


@pytest.fixture
def sample_images() -> List[ImageReference]:
    """Sample image references"""
    return [
        ImageReference(
            id="img-1",
            original_path="../images/demo-app.png",
            resolved_path=Path("/test/images/demo-app.png"),
            alt_text="Demo Application",
            caption="Figure 1: Demo Application",
            width=500,
            height=300,
            exists=True,
            placeholder_used=False
        ),
        ImageReference(
            id="img-2",
            original_path="../images/missing.png",
            resolved_path=None,
            alt_text="Missing Image",
            caption="Figure 2: Missing Image",
            width=500,
            height=300,
            exists=False,
            placeholder_used=True
        )
    ]


# ============================================================================
# TEMPORARY DIRECTORY FIXTURES
# ============================================================================

@pytest.fixture
def temp_output_dir(tmp_path):
    """Create temporary output directory"""
    output_dir = tmp_path / "output"
    output_dir.mkdir()
    return output_dir


@pytest.fixture
def temp_question_bank_dir(tmp_path):
    """Create temporary question bank directory structure"""
    base = tmp_path / "question_banks"
    staging = base / "staging"
    approved = base / "approved"
    rejected = base / "rejected"

    staging.mkdir(parents=True)
    approved.mkdir(parents=True)
    rejected.mkdir(parents=True)

    return {
        "base": base,
        "staging": staging,
        "approved": approved,
        "rejected": rejected
    }


@pytest.fixture
def temp_images_dir(tmp_path, fixtures_dir):
    """Create temporary images directory with test images"""
    images_dir = tmp_path / "images"
    images_dir.mkdir()

    # Copy test images from fixtures
    test_images = ["test_image.png", "test_image.jpg", "test_image.svg"]
    for img_name in test_images:
        src = fixtures_dir / img_name
        if src.exists():
            shutil.copy(src, images_dir / img_name)

    return images_dir


@pytest.fixture
def temp_frameworks_dir(tmp_path, sample_framework_content):
    """Create temporary frameworks directory with sample files"""
    frameworks_dir = tmp_path / "frameworks"
    frameworks_dir.mkdir()

    # Create sample framework file
    framework_file = frameworks_dir / "test-framework.md"
    framework_file.write_text(sample_framework_content)

    return frameworks_dir


# ============================================================================
# MOCK API FIXTURES
# ============================================================================

@pytest.fixture
def mock_anthropic_client():
    """Mock Anthropic API client for testing"""
    mock_client = MagicMock()

    # Mock successful API response
    mock_response = MagicMock()
    mock_response.content = [
        MagicMock(text=json.dumps({
            "questions": [
                {
                    "id": "ai-q1",
                    "type": "multiple_choice",
                    "question_text": "What is AI?",
                    "options": ["A", "B", "C", "D"],
                    "correct_answer": "A",
                    "explanation": "AI explanation",
                    "difficulty": "easy",
                    "points": 1,
                    "learning_outcome": "Understand AI",
                    "source_section": "intro"
                }
            ]
        }))
    ]

    mock_client.messages.create.return_value = mock_response

    return mock_client


@pytest.fixture
def mock_anthropic_error():
    """Mock Anthropic API client that raises errors"""
    mock_client = MagicMock()
    mock_client.messages.create.side_effect = Exception("API Error: Rate limit exceeded")
    return mock_client


# ============================================================================
# CLEANUP FIXTURES
# ============================================================================

@pytest.fixture(autouse=True)
def cleanup_temp_files():
    """Cleanup temporary files after tests (autouse - runs for every test)"""
    # Setup phase (before test)
    temp_dirs = []

    yield temp_dirs  # Test runs here

    # Teardown phase (after test)
    for temp_dir in temp_dirs:
        if temp_dir.exists():
            shutil.rmtree(temp_dir)


@pytest.fixture
def register_temp_dir(cleanup_temp_files):
    """Register temporary directories for cleanup"""
    def _register(path: Path):
        cleanup_temp_files.append(path)
    return _register


# ============================================================================
# HANDOUT DOCUMENT FIXTURE
# ============================================================================

@pytest.fixture
def sample_handout_document(sample_metadata, sample_sections, sample_questions, sample_images) -> HandoutDocument:
    """Complete handout document for testing"""
    toc = [
        TOCEntry(level=2, title="Session 1: Getting Started", page_number=2, anchor="session-1"),
        TOCEntry(level=3, title="Learning Outcomes", page_number=2, anchor="session-1-learning"),
        TOCEntry(level=3, title="Key Concepts", page_number=3, anchor="session-1-concepts"),
        TOCEntry(level=2, title="Session 2: Deep Dive", page_number=5, anchor="session-2")
    ]

    return HandoutDocument(
        metadata=sample_metadata,
        sections=sample_sections,
        questions=sample_questions,
        images=sample_images,
        toc=toc,
        generation_timestamp=datetime.now(),
        config_used={"theme": "dark"},
        output_path=Path("/test/output/handout.pdf"),
        warnings=["Missing image: demo-app.png"],
        question_review_complete=True
    )


# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def create_test_question_file(path: Path, questions: List[Question], module_id: str = "test-module"):
    """Helper to create a question bank JSON file"""
    questions_dict = {
        "module_id": module_id,
        "module_title": "Test Module",
        "version": "1.0",
        "last_reviewed": datetime.now().isoformat(),
        "questions": [q.to_dict() for q in questions]
    }

    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, 'w') as f:
        json.dump(questions_dict, f, indent=2)


def create_test_framework_file(path: Path, content: str):
    """Helper to create a framework markdown file"""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)


# Make helper functions available as fixtures
@pytest.fixture
def create_question_file():
    return create_test_question_file


@pytest.fixture
def create_framework_file():
    return create_test_framework_file
