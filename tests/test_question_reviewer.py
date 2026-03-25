"""
Unit tests for QuestionReviewer

Tests the interactive question review interface including:
- Loading staging questions
- Review actions (approve, edit, reject, skip)
- Saving approved/rejected questions
- Review session tracking
- Status checking
"""

import json
import pytest
from datetime import datetime
from pathlib import Path
from unittest.mock import MagicMock, patch, mock_open

from src.question_reviewer import QuestionReviewer, get_review_status
from src.models import (
    Question,
    QuestionBank,
    QuestionType,
    QuestionStatus,
    QuestionDifficulty,
    QuestionSource
)


@pytest.fixture
def temp_dirs(tmp_path):
    """Create temporary directories for testing."""
    staging_dir = tmp_path / "staging"
    approved_dir = tmp_path / "approved"
    rejected_dir = tmp_path / "rejected"

    staging_dir.mkdir()
    approved_dir.mkdir()
    rejected_dir.mkdir()

    return {
        "staging": staging_dir,
        "approved": approved_dir,
        "rejected": rejected_dir
    }


@pytest.fixture
def sample_question_bank():
    """Create sample question bank with pending questions."""
    return QuestionBank(
        module_id="module-0",
        module_title="Test Module",
        version="1.0",
        generated_at=datetime.now(),
        model_used="claude-sonnet-4",
        questions=[
            Question(
                id="m0-q1",
                type=QuestionType.MULTIPLE_CHOICE,
                question_text="What is machine learning?",
                options=["A type of database", "AI technique", "Programming language", "Operating system"],
                correct_answer="B",
                difficulty=QuestionDifficulty.EASY,
                points=1,
                source_section="session-1",
                status=QuestionStatus.PENDING_REVIEW
            ),
            Question(
                id="m0-q2",
                type=QuestionType.TRUE_FALSE,
                question_text="Python is required for ML.",
                options=["True", "False"],
                correct_answer="True",
                difficulty=QuestionDifficulty.EASY,
                points=1,
                source_section="session-1",
                status=QuestionStatus.PENDING_REVIEW
            ),
            Question(
                id="m0-q3",
                type=QuestionType.REFLECTION,
                question_text="How might ML apply to your work?",
                difficulty=QuestionDifficulty.EASY,
                points=2,
                source_section="session-2",
                status=QuestionStatus.PENDING_REVIEW
            )
        ],
        questions_pending=3
    )


@pytest.fixture
def reviewer(temp_dirs):
    """Create QuestionReviewer instance with temp directories."""
    return QuestionReviewer(
        staging_dir=str(temp_dirs["staging"]),
        approved_dir=str(temp_dirs["approved"]),
        rejected_dir=str(temp_dirs["rejected"])
    )


class TestQuestionReviewerInit:
    """Test QuestionReviewer initialization."""

    def test_init_creates_directories(self, tmp_path):
        """Test that directories are created if they don't exist."""
        staging = tmp_path / "staging"
        approved = tmp_path / "approved"
        rejected = tmp_path / "rejected"

        reviewer = QuestionReviewer(
            staging_dir=str(staging),
            approved_dir=str(approved),
            rejected_dir=str(rejected)
        )

        assert staging.exists()
        assert approved.exists()
        assert rejected.exists()

    def test_init_with_existing_directories(self, temp_dirs):
        """Test initialization with existing directories."""
        reviewer = QuestionReviewer(
            staging_dir=str(temp_dirs["staging"]),
            approved_dir=str(temp_dirs["approved"]),
            rejected_dir=str(temp_dirs["rejected"])
        )

        assert reviewer.staging_dir == temp_dirs["staging"]
        assert reviewer.approved_dir == temp_dirs["approved"]
        assert reviewer.rejected_dir == temp_dirs["rejected"]


class TestGetReviewStatus:
    """Test review status checking."""

    def test_status_no_questions(self, reviewer):
        """Test status when no staging or approved files exist."""
        status = reviewer.get_review_status("module-0")

        assert status["status"] == "no_questions"
        assert status["pending_count"] == 0
        assert status["approved_count"] == 0
        assert not status["staging_exists"]
        assert not status["approved_exists"]

    def test_status_pending_review(self, reviewer, sample_question_bank, temp_dirs):
        """Test status when staging file has pending questions."""
        staging_file = temp_dirs["staging"] / "module-0-staging.json"
        with open(staging_file, 'w') as f:
            json.dump(sample_question_bank.to_dict(), f)

        status = reviewer.get_review_status("module-0")

        assert status["status"] == "pending_review"
        assert status["pending_count"] == 3
        assert status["approved_count"] == 0
        assert status["staging_exists"]
        assert not status["approved_exists"]

    def test_status_all_reviewed(self, reviewer, sample_question_bank, temp_dirs):
        """Test status when all questions are approved."""
        # Mark all as approved
        for q in sample_question_bank.questions:
            q.status = QuestionStatus.APPROVED

        approved_file = temp_dirs["approved"] / "module-0.json"
        with open(approved_file, 'w') as f:
            json.dump(sample_question_bank.to_dict(), f)

        status = reviewer.get_review_status("module-0")

        assert status["status"] == "all_reviewed"
        assert status["pending_count"] == 0
        assert status["approved_count"] == 3
        assert not status["staging_exists"]
        assert status["approved_exists"]

    def test_status_invalid_json(self, reviewer, temp_dirs):
        """Test status with invalid JSON file."""
        staging_file = temp_dirs["staging"] / "module-0-staging.json"
        with open(staging_file, 'w') as f:
            f.write("invalid json{")

        status = reviewer.get_review_status("module-0")

        assert status["status"] == "no_questions"
        assert status["pending_count"] == 0


class TestStartSession:
    """Test interactive review session."""

    def test_start_session_no_staging_file(self, reviewer):
        """Test starting session when staging file doesn't exist."""
        with patch('src.question_reviewer.console'):
            session = reviewer.start_session("module-0")

        assert session.module_id == "module-0"
        assert session.questions_total == 0
        assert session.completed_at is not None

    def test_start_session_invalid_json(self, reviewer, temp_dirs):
        """Test starting session with invalid JSON."""
        staging_file = temp_dirs["staging"] / "module-0-staging.json"
        with open(staging_file, 'w') as f:
            f.write("invalid json")

        with patch('src.question_reviewer.console'):
            session = reviewer.start_session("module-0")

        assert session.questions_total == 0
        assert session.completed_at is not None

    def test_start_session_no_pending_questions(self, reviewer, sample_question_bank, temp_dirs):
        """Test starting session when all questions already reviewed."""
        # Mark all as approved
        for q in sample_question_bank.questions:
            q.status = QuestionStatus.APPROVED

        staging_file = temp_dirs["staging"] / "module-0-staging.json"
        with open(staging_file, 'w') as f:
            json.dump(sample_question_bank.to_dict(), f)

        with patch('src.question_reviewer.console'):
            session = reviewer.start_session("module-0")

        assert session.questions_total == 0
        assert session.completed_at is not None

    @patch('src.question_reviewer.console')
    @patch('src.question_reviewer.Prompt.ask')
    def test_start_session_approve_all(self, mock_prompt, mock_console, reviewer,
                                       sample_question_bank, temp_dirs):
        """Test session where all questions are approved."""
        staging_file = temp_dirs["staging"] / "module-0-staging.json"
        with open(staging_file, 'w') as f:
            json.dump(sample_question_bank.to_dict(), f)

        # Mock user always choosing "A" (approve)
        mock_prompt.return_value = "A"

        session = reviewer.start_session("module-0")

        assert session.questions_total == 3
        assert session.questions_approved == 3
        assert session.questions_edited == 0
        assert session.questions_rejected == 0
        assert session.questions_skipped == 0
        assert session.completed_at is not None

        # Check approved file was created
        approved_file = temp_dirs["approved"] / "module-0.json"
        assert approved_file.exists()

        with open(approved_file) as f:
            approved_data = json.load(f)
            assert len(approved_data["questions"]) == 3
            assert all(q["status"] == "approved" for q in approved_data["questions"])

        # Check staging file was removed
        assert not staging_file.exists()

    @patch('src.question_reviewer.console')
    @patch('src.question_reviewer.Prompt.ask')
    def test_start_session_reject_all(self, mock_prompt, mock_console, reviewer,
                                      sample_question_bank, temp_dirs):
        """Test session where all questions are rejected."""
        staging_file = temp_dirs["staging"] / "module-0-staging.json"
        with open(staging_file, 'w') as f:
            json.dump(sample_question_bank.to_dict(), f)

        # Mock user choosing "R" (reject) with no reason
        mock_prompt.side_effect = ["R", "", "R", "", "R", ""]

        session = reviewer.start_session("module-0")

        assert session.questions_total == 3
        assert session.questions_approved == 0
        assert session.questions_rejected == 3
        assert session.completed_at is not None

        # Check rejected file was created
        rejected_file = temp_dirs["rejected"] / "module-0-rejected.json"
        assert rejected_file.exists()

        with open(rejected_file) as f:
            rejected_data = json.load(f)
            assert len(rejected_data["questions"]) == 3

    @patch('src.question_reviewer.console')
    @patch('src.question_reviewer.Prompt.ask')
    def test_start_session_skip_all(self, mock_prompt, mock_console, reviewer,
                                    sample_question_bank, temp_dirs):
        """Test session where all questions are skipped."""
        staging_file = temp_dirs["staging"] / "module-0-staging.json"
        with open(staging_file, 'w') as f:
            json.dump(sample_question_bank.to_dict(), f)

        # Mock user choosing "S" (skip)
        mock_prompt.return_value = "S"

        session = reviewer.start_session("module-0")

        assert session.questions_total == 3
        assert session.questions_skipped == 3
        assert session.questions_approved == 0

        # Check staging file still exists with pending questions
        assert staging_file.exists()
        with open(staging_file) as f:
            staging_data = json.load(f)
            assert len(staging_data["questions"]) == 3
            assert all(q["status"] == "pending_review" for q in staging_data["questions"])

    @patch('src.question_reviewer.console')
    @patch('src.question_reviewer.Prompt.ask')
    @patch('src.question_reviewer.Confirm.ask')
    def test_start_session_quit(self, mock_confirm, mock_prompt, mock_console, reviewer,
                               sample_question_bank, temp_dirs):
        """Test quitting review session."""
        staging_file = temp_dirs["staging"] / "module-0-staging.json"
        with open(staging_file, 'w') as f:
            json.dump(sample_question_bank.to_dict(), f)

        # First question: approve, second question: quit
        mock_prompt.side_effect = ["A", "Q"]
        mock_confirm.return_value = True

        session = reviewer.start_session("module-0")

        assert session.questions_total == 3
        assert session.questions_approved == 1
        assert session.questions_skipped == 2  # Remaining questions counted as skipped

    @patch('src.question_reviewer.console')
    @patch('src.question_reviewer.Prompt.ask')
    def test_start_session_mixed_actions(self, mock_prompt, mock_console, reviewer,
                                        sample_question_bank, temp_dirs):
        """Test session with mixed review actions."""
        staging_file = temp_dirs["staging"] / "module-0-staging.json"
        with open(staging_file, 'w') as f:
            json.dump(sample_question_bank.to_dict(), f)

        # Q1: approve, Q2: reject with reason, Q3: skip
        mock_prompt.side_effect = ["A", "R", "Poor question", "S"]

        session = reviewer.start_session("module-0")

        assert session.questions_total == 3
        assert session.questions_approved == 1
        assert session.questions_rejected == 1
        assert session.questions_skipped == 1

        # Check files
        approved_file = temp_dirs["approved"] / "module-0.json"
        rejected_file = temp_dirs["rejected"] / "module-0-rejected.json"

        assert approved_file.exists()
        assert rejected_file.exists()
        assert staging_file.exists()  # Still has 1 pending

        # Verify rejected question has notes
        with open(rejected_file) as f:
            rejected_data = json.load(f)
            assert rejected_data["questions"][0]["reviewer_notes"] == "REJECTED: Poor question"


class TestEditQuestion:
    """Test question editing workflow."""

    @patch('src.question_reviewer.console')
    @patch('src.question_reviewer.Prompt.ask')
    def test_edit_question_text_only(self, mock_prompt, mock_console, reviewer,
                                     sample_question_bank, temp_dirs):
        """Test editing only question text."""
        staging_file = temp_dirs["staging"] / "module-0-staging.json"
        with open(staging_file, 'w') as f:
            json.dump(sample_question_bank.to_dict(), f)

        # Choose edit, change text, keep options, keep answer, no notes
        mock_prompt.side_effect = [
            "E",  # Choose edit
            "What is ML really?",  # New question text
            "",  # Keep options
            "",  # Keep answer
            ""   # No notes
        ]

        session = reviewer.start_session("module-0")

        # Load approved file and check
        approved_file = temp_dirs["approved"] / "module-0.json"
        with open(approved_file) as f:
            approved_data = json.load(f)
            # First question should have new text
            assert "What is ML really?" in approved_data["questions"][0]["question_text"]

    @patch('src.question_reviewer.console')
    @patch('src.question_reviewer.Prompt.ask')
    def test_edit_question_with_notes(self, mock_prompt, mock_console, reviewer,
                                     sample_question_bank, temp_dirs):
        """Test editing question with reviewer notes."""
        staging_file = temp_dirs["staging"] / "module-0-staging.json"
        # Use only first question
        sample_question_bank.questions = [sample_question_bank.questions[0]]
        sample_question_bank.questions_pending = 1

        with open(staging_file, 'w') as f:
            json.dump(sample_question_bank.to_dict(), f)

        # Edit with notes
        mock_prompt.side_effect = [
            "E",  # Choose edit
            "",  # Keep text
            "",  # Keep options
            "",  # Keep answer
            "Improved clarity"  # Notes
        ]

        session = reviewer.start_session("module-0")

        assert session.questions_edited == 1

        # Check reviewer notes were saved
        approved_file = temp_dirs["approved"] / "module-0.json"
        with open(approved_file) as f:
            approved_data = json.load(f)
            assert approved_data["questions"][0]["reviewer_notes"] == "Improved clarity"


class TestSaveResults:
    """Test saving review results."""

    def test_merge_with_existing_approved(self, reviewer, sample_question_bank, temp_dirs):
        """Test merging new approved questions with existing ones."""
        # Create existing approved file
        existing_question = Question(
            id="m0-q0",
            type=QuestionType.MULTIPLE_CHOICE,
            question_text="Existing question",
            options=["A", "B", "C", "D"],
            correct_answer="A",
            status=QuestionStatus.APPROVED
        )
        existing_bank = QuestionBank(
            module_id="module-0",
            module_title="Test Module",
            version="1.0",
            questions=[existing_question]
        )

        approved_file = temp_dirs["approved"] / "module-0.json"
        with open(approved_file, 'w') as f:
            json.dump(existing_bank.to_dict(), f)

        # Create staging file
        staging_file = temp_dirs["staging"] / "module-0-staging.json"
        with open(staging_file, 'w') as f:
            json.dump(sample_question_bank.to_dict(), f)

        # Approve all questions
        with patch('src.question_reviewer.console'), \
             patch('src.question_reviewer.Prompt.ask', return_value="A"):
            session = reviewer.start_session("module-0")

        # Check merged file
        with open(approved_file) as f:
            merged_data = json.load(f)
            assert len(merged_data["questions"]) == 4  # 1 existing + 3 new
            question_ids = [q["id"] for q in merged_data["questions"]]
            assert "m0-q0" in question_ids  # Existing
            assert "m0-q1" in question_ids  # New

    def test_append_to_existing_rejected(self, reviewer, sample_question_bank, temp_dirs):
        """Test appending to existing rejected file."""
        # Create existing rejected file
        existing_question = Question(
            id="m0-q-old",
            type=QuestionType.MULTIPLE_CHOICE,
            question_text="Old rejected question",
            options=["A", "B", "C", "D"],
            correct_answer="A",
            status=QuestionStatus.REJECTED
        )
        existing_bank = QuestionBank(
            module_id="module-0",
            module_title="Test Module",
            version="1.0",
            questions=[existing_question]
        )

        rejected_file = temp_dirs["rejected"] / "module-0-rejected.json"
        with open(rejected_file, 'w') as f:
            json.dump(existing_bank.to_dict(), f)

        # Create staging file
        staging_file = temp_dirs["staging"] / "module-0-staging.json"
        with open(staging_file, 'w') as f:
            json.dump(sample_question_bank.to_dict(), f)

        # Reject all questions
        with patch('src.question_reviewer.console'), \
             patch('src.question_reviewer.Prompt.ask', side_effect=["R", ""] * 3):
            session = reviewer.start_session("module-0")

        # Check merged rejected file
        with open(rejected_file) as f:
            merged_data = json.load(f)
            assert len(merged_data["questions"]) == 4  # 1 old + 3 new


class TestConvenienceFunction:
    """Test convenience function."""

    def test_get_review_status_function(self, temp_dirs, sample_question_bank):
        """Test get_review_status convenience function."""
        staging_file = temp_dirs["staging"] / "module-0-staging.json"
        with open(staging_file, 'w') as f:
            json.dump(sample_question_bank.to_dict(), f)

        status = get_review_status(
            "module-0",
            staging_dir=str(temp_dirs["staging"]),
            approved_dir=str(temp_dirs["approved"])
        )

        assert status["status"] == "pending_review"
        assert status["pending_count"] == 3


class TestBorderColors:
    """Test question type border colors."""

    def test_get_border_color_name(self, reviewer):
        """Test border color mapping for each question type."""
        assert reviewer._get_border_color_name(QuestionType.MULTIPLE_CHOICE) == "blue"
        assert reviewer._get_border_color_name(QuestionType.TRUE_FALSE) == "blue"
        assert reviewer._get_border_color_name(QuestionType.SHORT_ANSWER) == "green"
        assert reviewer._get_border_color_name(QuestionType.REFLECTION) == "magenta"
        assert reviewer._get_border_color_name(QuestionType.APPLICATION) == "green"


class TestEdgeCases:
    """Test edge cases and error handling."""

    def test_empty_question_bank(self, reviewer, temp_dirs):
        """Test with empty question bank."""
        empty_bank = QuestionBank(
            module_id="module-0",
            module_title="Empty Module",
            version="1.0",
            questions=[]
        )

        staging_file = temp_dirs["staging"] / "module-0-staging.json"
        with open(staging_file, 'w') as f:
            json.dump(empty_bank.to_dict(), f)

        with patch('src.question_reviewer.console'):
            session = reviewer.start_session("module-0")

        assert session.questions_total == 0

    def test_case_insensitive_choices(self, reviewer, sample_question_bank, temp_dirs):
        """Test that review choices are case-insensitive."""
        staging_file = temp_dirs["staging"] / "module-0-staging.json"
        # Use only one question
        sample_question_bank.questions = [sample_question_bank.questions[0]]
        sample_question_bank.questions_pending = 1

        with open(staging_file, 'w') as f:
            json.dump(sample_question_bank.to_dict(), f)

        # Test lowercase choice
        with patch('src.question_reviewer.console'), \
             patch('src.question_reviewer.Prompt.ask', return_value="a"):
            session = reviewer.start_session("module-0")

        assert session.questions_approved == 1
