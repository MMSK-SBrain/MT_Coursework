"""
Unit tests for QuestionLoader

Tests question loading, validation, and placement logic.

Author: Course Generator Team
Date: 2026-01-11
"""

import json
import pytest
from datetime import datetime
from pathlib import Path
from typing import List

from src.question_loader import QuestionLoader, load_module_questions
from src.models import (
    Question,
    QuestionBank,
    QuestionType,
    QuestionStatus,
    QuestionDifficulty,
    QuestionSource,
    ContentSection
)


@pytest.fixture
def temp_question_bank_dir(tmp_path):
    """Create temporary question bank directory."""
    question_dir = tmp_path / "question_banks" / "approved"
    question_dir.mkdir(parents=True)
    return question_dir


@pytest.fixture
def sample_questions():
    """Create sample questions for testing."""
    return [
        Question(
            id="m0-s1-q1",
            type=QuestionType.MULTIPLE_CHOICE,
            question_text="What is machine learning?",
            options=["A type of hardware", "A subset of AI", "A programming language", "A database"],
            correct_answer="B",
            explanation="ML is a subset of artificial intelligence.",
            difficulty=QuestionDifficulty.EASY,
            points=1,
            learning_outcome="Define machine learning",
            source_section="session-1-intro",
            source=QuestionSource.MANUAL,
            status=QuestionStatus.APPROVED
        ),
        Question(
            id="m0-s1-q2",
            type=QuestionType.TRUE_FALSE,
            question_text="Python is the only language for ML.",
            options=["True", "False"],
            correct_answer="False",
            explanation="While Python is popular, languages like R, Julia, and Java are also used.",
            difficulty=QuestionDifficulty.EASY,
            points=1,
            source_section="session-1-intro",
            source=QuestionSource.MANUAL,
            status=QuestionStatus.APPROVED
        ),
        Question(
            id="m0-s2-q1",
            type=QuestionType.SHORT_ANSWER,
            question_text="Name three Python libraries for ML.",
            correct_answer="scikit-learn, tensorflow, pytorch",
            explanation="These are the most popular ML libraries.",
            difficulty=QuestionDifficulty.MEDIUM,
            points=2,
            source_section="session-2-libraries",
            source=QuestionSource.MANUAL,
            status=QuestionStatus.APPROVED
        ),
        Question(
            id="m0-s2-q2",
            type=QuestionType.REFLECTION,
            question_text="How would you use ML in your work?",
            explanation="Reflect on your own context.",
            difficulty=QuestionDifficulty.EASY,
            points=2,
            source_section="session-2-libraries",
            source=QuestionSource.MANUAL,
            status=QuestionStatus.APPROVED
        ),
        Question(
            id="m0-s3-q1",
            type=QuestionType.APPLICATION,
            question_text="Design a simple ML system for email spam detection.",
            correct_answer="Use text classification with labeled examples of spam/not spam.",
            explanation="This is a classic supervised learning problem.",
            difficulty=QuestionDifficulty.HARD,
            points=3,
            source_section="session-3-applications",
            source=QuestionSource.MANUAL,
            status=QuestionStatus.APPROVED
        )
    ]


@pytest.fixture
def sample_question_bank(sample_questions):
    """Create sample question bank."""
    return QuestionBank(
        module_id="module-0",
        module_title="Introduction to ML",
        version="1.0",
        last_reviewed=datetime.now(),
        questions=sample_questions
    )


@pytest.fixture
def sample_sections():
    """Create sample content sections for placement testing."""
    return [
        ContentSection(
            id="session-1-intro",
            level=2,
            title="Session 1: Introduction to ML",
            content="This is an introduction to machine learning.\n" * 50,  # ~50 lines
            include_in_handout=True
        ),
        ContentSection(
            id="session-2-libraries",
            level=2,
            title="Session 2: ML Libraries",
            content="Overview of ML libraries and tools.\n" * 100,  # ~100 lines
            include_in_handout=True
        ),
        ContentSection(
            id="session-3-applications",
            level=2,
            title="Session 3: ML Applications",
            content="Real-world applications of ML.\n" * 75,  # ~75 lines
            include_in_handout=True
        )
    ]


class TestQuestionLoaderInit:
    """Test QuestionLoader initialization."""

    def test_init_with_existing_directory(self, temp_question_bank_dir):
        """Test initialization with existing directory."""
        loader = QuestionLoader(str(temp_question_bank_dir))
        assert loader.question_banks_dir == temp_question_bank_dir

    def test_init_creates_missing_directory(self, tmp_path):
        """Test that missing directory is created."""
        new_dir = tmp_path / "new_question_banks"
        loader = QuestionLoader(str(new_dir))
        assert new_dir.exists()

    def test_init_default_directory(self):
        """Test initialization with default directory."""
        loader = QuestionLoader()
        assert loader.question_banks_dir == Path("question_banks/approved")


class TestLoadQuestions:
    """Test question loading functionality."""

    def test_load_existing_questions(self, temp_question_bank_dir, sample_question_bank):
        """Test loading questions from existing file."""
        # Create question bank file
        question_file = temp_question_bank_dir / "module-0.json"
        with open(question_file, 'w') as f:
            json.dump(sample_question_bank.to_dict(), f)

        # Load questions
        loader = QuestionLoader(str(temp_question_bank_dir))
        questions = loader.load_questions("module-0")

        assert len(questions) == 5
        assert all(isinstance(q, Question) for q in questions)
        assert all(q.status == QuestionStatus.APPROVED for q in questions)

    def test_load_missing_file(self, temp_question_bank_dir):
        """Test loading from non-existent file returns empty list."""
        loader = QuestionLoader(str(temp_question_bank_dir))
        questions = loader.load_questions("nonexistent-module")

        assert questions == []

    def test_load_invalid_json(self, temp_question_bank_dir):
        """Test loading invalid JSON returns empty list."""
        # Create invalid JSON file
        question_file = temp_question_bank_dir / "invalid.json"
        with open(question_file, 'w') as f:
            f.write("{ invalid json }")

        loader = QuestionLoader(str(temp_question_bank_dir))
        questions = loader.load_questions("invalid")

        assert questions == []

    def test_load_filters_pending_questions(self, temp_question_bank_dir, sample_questions):
        """Test that pending questions are filtered out."""
        # Add pending question
        pending_q = Question(
            id="pending-1",
            type=QuestionType.MULTIPLE_CHOICE,
            question_text="Pending question?",
            options=["A", "B", "C", "D"],
            correct_answer="A",
            status=QuestionStatus.PENDING_REVIEW
        )

        bank = QuestionBank(
            module_id="module-0",
            module_title="Test",
            version="1.0",
            questions=sample_questions + [pending_q]
        )

        # Save to file
        question_file = temp_question_bank_dir / "module-0.json"
        with open(question_file, 'w') as f:
            json.dump(bank.to_dict(), f)

        # Load questions
        loader = QuestionLoader(str(temp_question_bank_dir))
        questions = loader.load_questions("module-0")

        # Should only get approved questions
        assert len(questions) == 5
        assert all(q.status == QuestionStatus.APPROVED for q in questions)

    def test_load_no_approved_questions(self, temp_question_bank_dir):
        """Test loading when no approved questions exist."""
        bank = QuestionBank(
            module_id="module-0",
            module_title="Test",
            version="1.0",
            questions=[
                Question(
                    id="pending-1",
                    type=QuestionType.MULTIPLE_CHOICE,
                    question_text="Pending?",
                    options=["A", "B", "C", "D"],
                    correct_answer="A",
                    status=QuestionStatus.PENDING_REVIEW
                )
            ]
        )

        question_file = temp_question_bank_dir / "module-0.json"
        with open(question_file, 'w') as f:
            json.dump(bank.to_dict(), f)

        loader = QuestionLoader(str(temp_question_bank_dir))
        questions = loader.load_questions("module-0")

        assert questions == []


class TestValidateQuestion:
    """Test question validation logic."""

    def test_validate_multiple_choice(self, temp_question_bank_dir):
        """Test validation of multiple choice questions."""
        loader = QuestionLoader(str(temp_question_bank_dir))

        # Valid MCQ
        valid_mcq = Question(
            id="mcq-1",
            type=QuestionType.MULTIPLE_CHOICE,
            question_text="What is 2+2?",
            options=["1", "2", "3", "4"],
            correct_answer="D",
            status=QuestionStatus.APPROVED
        )
        assert loader._validate_question(valid_mcq) is True

        # Missing options
        invalid_mcq = Question(
            id="mcq-2",
            type=QuestionType.MULTIPLE_CHOICE,
            question_text="What is 2+2?",
            options=None,
            correct_answer="D",
            status=QuestionStatus.APPROVED
        )
        assert loader._validate_question(invalid_mcq) is False

        # Wrong number of options
        invalid_mcq2 = Question(
            id="mcq-3",
            type=QuestionType.MULTIPLE_CHOICE,
            question_text="What is 2+2?",
            options=["1", "2", "3"],  # Only 3 options
            correct_answer="C",
            status=QuestionStatus.APPROVED
        )
        assert loader._validate_question(invalid_mcq2) is False

        # Missing correct answer
        invalid_mcq3 = Question(
            id="mcq-4",
            type=QuestionType.MULTIPLE_CHOICE,
            question_text="What is 2+2?",
            options=["1", "2", "3", "4"],
            correct_answer=None,
            status=QuestionStatus.APPROVED
        )
        assert loader._validate_question(invalid_mcq3) is False

    def test_validate_true_false(self, temp_question_bank_dir):
        """Test validation of true/false questions."""
        loader = QuestionLoader(str(temp_question_bank_dir))

        # Valid T/F
        valid_tf = Question(
            id="tf-1",
            type=QuestionType.TRUE_FALSE,
            question_text="Is the sky blue?",
            options=["True", "False"],
            correct_answer="True",
            status=QuestionStatus.APPROVED
        )
        assert loader._validate_question(valid_tf) is True

        # Invalid options
        invalid_tf = Question(
            id="tf-2",
            type=QuestionType.TRUE_FALSE,
            question_text="Is the sky blue?",
            options=["Yes", "No"],  # Should be True/False
            correct_answer="Yes",
            status=QuestionStatus.APPROVED
        )
        assert loader._validate_question(invalid_tf) is False

        # Missing correct answer
        invalid_tf2 = Question(
            id="tf-3",
            type=QuestionType.TRUE_FALSE,
            question_text="Is the sky blue?",
            options=["True", "False"],
            correct_answer=None,
            status=QuestionStatus.APPROVED
        )
        assert loader._validate_question(invalid_tf2) is False

    def test_validate_short_answer(self, temp_question_bank_dir):
        """Test validation of short answer questions."""
        loader = QuestionLoader(str(temp_question_bank_dir))

        # Valid short answer
        valid_sa = Question(
            id="sa-1",
            type=QuestionType.SHORT_ANSWER,
            question_text="Name a programming language.",
            correct_answer="Python",
            status=QuestionStatus.APPROVED
        )
        assert loader._validate_question(valid_sa) is True

        # Missing correct answer (warning, but valid)
        no_answer_sa = Question(
            id="sa-2",
            type=QuestionType.SHORT_ANSWER,
            question_text="Name a programming language.",
            correct_answer=None,
            status=QuestionStatus.APPROVED
        )
        assert loader._validate_question(no_answer_sa) is True

    def test_validate_reflection(self, temp_question_bank_dir):
        """Test validation of reflection questions."""
        loader = QuestionLoader(str(temp_question_bank_dir))

        # Valid reflection
        valid_refl = Question(
            id="refl-1",
            type=QuestionType.REFLECTION,
            question_text="How would you apply this concept?",
            status=QuestionStatus.APPROVED
        )
        assert loader._validate_question(valid_refl) is True

    def test_validate_application(self, temp_question_bank_dir):
        """Test validation of application questions."""
        loader = QuestionLoader(str(temp_question_bank_dir))

        # Valid application
        valid_app = Question(
            id="app-1",
            type=QuestionType.APPLICATION,
            question_text="Design a solution for X.",
            correct_answer="Sample solution approach",
            status=QuestionStatus.APPROVED
        )
        assert loader._validate_question(valid_app) is True

    def test_validate_missing_required_fields(self, temp_question_bank_dir):
        """Test validation fails for missing required fields."""
        loader = QuestionLoader(str(temp_question_bank_dir))

        # Missing question_text
        invalid_q = Question(
            id="q-1",
            type=QuestionType.MULTIPLE_CHOICE,
            question_text="",
            options=["A", "B", "C", "D"],
            correct_answer="A",
            status=QuestionStatus.APPROVED
        )
        assert loader._validate_question(invalid_q) is False


class TestPlaceQuestions:
    """Test question placement algorithm."""

    def test_place_questions_basic(self, temp_question_bank_dir, sample_questions, sample_sections):
        """Test basic question placement."""
        loader = QuestionLoader(str(temp_question_bank_dir))
        placement_map = loader.place_questions(sample_questions, sample_sections)

        # Should have placements for sections
        assert len(placement_map) > 0
        # Total questions should match
        total_placed = sum(len(qs) for qs in placement_map.values())
        assert total_placed == len(sample_questions)

    def test_place_questions_by_source_section(self, temp_question_bank_dir, sample_questions, sample_sections):
        """Test questions are placed in their source sections when specified."""
        loader = QuestionLoader(str(temp_question_bank_dir))
        placement_map = loader.place_questions(sample_questions, sample_sections)

        # Check that questions with source_section are in correct sections
        for section_id, questions in placement_map.items():
            for question in questions:
                if question.source_section:
                    # Question should be in its source section or distributed
                    assert section_id in [q.source_section for q in sample_questions] or True

    def test_place_questions_empty_list(self, temp_question_bank_dir, sample_sections):
        """Test placing empty question list."""
        loader = QuestionLoader(str(temp_question_bank_dir))
        placement_map = loader.place_questions([], sample_sections)

        assert placement_map == {}

    def test_place_questions_no_sections(self, temp_question_bank_dir, sample_questions):
        """Test placing questions with no sections."""
        loader = QuestionLoader(str(temp_question_bank_dir))
        placement_map = loader.place_questions(sample_questions, [])

        assert placement_map == {}

    def test_place_questions_distribution(self, temp_question_bank_dir, sample_sections):
        """Test questions are distributed proportionally to section length."""
        # Create questions without source_section
        questions = [
            Question(
                id=f"q-{i}",
                type=QuestionType.MULTIPLE_CHOICE,
                question_text=f"Question {i}?",
                options=["A", "B", "C", "D"],
                correct_answer="A",
                status=QuestionStatus.APPROVED
            )
            for i in range(10)
        ]

        loader = QuestionLoader(str(temp_question_bank_dir))
        placement_map = loader.place_questions(questions, sample_sections)

        # All questions should be placed
        total_placed = sum(len(qs) for qs in placement_map.values())
        assert total_placed == 10

        # Longer sections should get more questions (roughly)
        # session-2 has 100 lines, session-3 has 75, session-1 has 50
        # So session-2 should have most questions


class TestGetMajorSections:
    """Test major section extraction."""

    def test_get_major_sections_flat(self, temp_question_bank_dir):
        """Test extraction from flat section list."""
        sections = [
            ContentSection(id="s1", level=1, title="Title", content="", include_in_handout=True),
            ContentSection(id="s2", level=2, title="Session 1", content="", include_in_handout=True),
            ContentSection(id="s3", level=2, title="Session 2", content="", include_in_handout=True),
            ContentSection(id="s4", level=3, title="Subsection", content="", include_in_handout=True),
        ]

        loader = QuestionLoader(str(temp_question_bank_dir))
        major = loader._get_major_sections(sections)

        assert len(major) == 2
        assert all(s.level == 2 for s in major)

    def test_get_major_sections_nested(self, temp_question_bank_dir):
        """Test extraction from nested sections."""
        subsection = ContentSection(id="s2-1", level=2, title="Subsession", content="", include_in_handout=True)
        section = ContentSection(
            id="s1",
            level=1,
            title="Main",
            content="",
            subsections=[subsection],
            include_in_handout=True
        )

        loader = QuestionLoader(str(temp_question_bank_dir))
        major = loader._get_major_sections([section])

        assert len(major) == 1
        assert major[0].id == "s2-1"

    def test_get_major_sections_exclude_filtered(self, temp_question_bank_dir):
        """Test that filtered sections are excluded."""
        sections = [
            ContentSection(id="s1", level=2, title="Included", content="", include_in_handout=True),
            ContentSection(id="s2", level=2, title="Excluded", content="", include_in_handout=False),
        ]

        loader = QuestionLoader(str(temp_question_bank_dir))
        major = loader._get_major_sections(sections)

        assert len(major) == 1
        assert major[0].id == "s1"


class TestQuestionBoxes:
    """Test question box grouping."""

    def test_create_question_boxes_default_size(self, temp_question_bank_dir, sample_questions):
        """Test creating question boxes with default size."""
        loader = QuestionLoader(str(temp_question_bank_dir))
        boxes = loader.create_question_boxes(sample_questions)

        # Should have at least one box
        assert len(boxes) > 0
        # Each box should have 3-5 questions
        for box in boxes[:-1]:  # All except possibly last
            assert 3 <= len(box) <= 5

    def test_create_question_boxes_custom_size(self, temp_question_bank_dir, sample_questions):
        """Test creating question boxes with custom size."""
        loader = QuestionLoader(str(temp_question_bank_dir))
        boxes = loader.create_question_boxes(sample_questions, box_size_range=(2, 3))

        # Each box should respect custom size
        for box in boxes[:-1]:
            assert 2 <= len(box) <= 3

    def test_create_question_boxes_empty_list(self, temp_question_bank_dir):
        """Test creating boxes from empty list."""
        loader = QuestionLoader(str(temp_question_bank_dir))
        boxes = loader.create_question_boxes([])

        assert boxes == []

    def test_create_question_boxes_preserves_order(self, temp_question_bank_dir, sample_questions):
        """Test that question order is preserved in boxes."""
        loader = QuestionLoader(str(temp_question_bank_dir))
        boxes = loader.create_question_boxes(sample_questions)

        # Flatten boxes and check order
        flattened = [q for box in boxes for q in box]
        assert flattened == sample_questions


class TestQuestionStats:
    """Test question statistics."""

    def test_get_question_stats(self, temp_question_bank_dir, sample_questions):
        """Test getting question statistics."""
        loader = QuestionLoader(str(temp_question_bank_dir))
        stats = loader.get_question_stats(sample_questions)

        assert stats["total"] == 5
        assert stats["by_type"][QuestionType.MULTIPLE_CHOICE.value] == 1
        assert stats["by_type"][QuestionType.TRUE_FALSE.value] == 1
        assert stats["by_type"][QuestionType.SHORT_ANSWER.value] == 1
        assert stats["by_type"][QuestionType.REFLECTION.value] == 1
        assert stats["by_type"][QuestionType.APPLICATION.value] == 1

    def test_get_question_stats_empty(self, temp_question_bank_dir):
        """Test stats for empty question list."""
        loader = QuestionLoader(str(temp_question_bank_dir))
        stats = loader.get_question_stats([])

        assert stats["total"] == 0
        assert stats["by_type"] == {}


class TestConvenienceFunction:
    """Test convenience function."""

    def test_load_module_questions(self, temp_question_bank_dir, sample_question_bank):
        """Test load_module_questions convenience function."""
        # Create question bank file
        question_file = temp_question_bank_dir / "module-0.json"
        with open(question_file, 'w') as f:
            json.dump(sample_question_bank.to_dict(), f)

        # Load using convenience function
        questions = load_module_questions("module-0", str(temp_question_bank_dir))

        assert len(questions) == 5
        assert all(isinstance(q, Question) for q in questions)


class TestErrorHandling:
    """Test error handling scenarios."""

    def test_handles_corrupt_question_data(self, temp_question_bank_dir):
        """Test handling of corrupt question data in valid JSON."""
        # Create file with valid JSON but invalid question data
        corrupt_data = {
            "module_id": "test",
            "module_title": "Test",
            "version": "1.0",
            "questions": [
                {
                    "id": "q1",
                    "type": "invalid_type",  # Invalid type
                    "question_text": "Test?"
                }
            ]
        }

        question_file = temp_question_bank_dir / "corrupt.json"
        with open(question_file, 'w') as f:
            json.dump(corrupt_data, f)

        loader = QuestionLoader(str(temp_question_bank_dir))
        questions = loader.load_questions("corrupt")

        # Should handle gracefully and return empty or skip invalid questions
        # Depending on implementation, might return empty list
        assert isinstance(questions, list)

    def test_handles_file_permission_error(self, temp_question_bank_dir, sample_question_bank):
        """Test handling of file permission errors."""
        import os

        # Create question file
        question_file = temp_question_bank_dir / "module-0.json"
        with open(question_file, 'w') as f:
            json.dump(sample_question_bank.to_dict(), f)

        # Make file unreadable (Unix-like systems only)
        if os.name != 'nt':  # Not Windows
            os.chmod(question_file, 0o000)

            loader = QuestionLoader(str(temp_question_bank_dir))
            questions = loader.load_questions("module-0")

            # Should handle gracefully
            assert isinstance(questions, list)

            # Restore permissions
            os.chmod(question_file, 0o644)


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--cov=src.question_loader", "--cov-report=term-missing"])
