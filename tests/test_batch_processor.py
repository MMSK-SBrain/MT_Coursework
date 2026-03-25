"""
Unit tests for BatchProcessor

Tests batch processing functionality including:
- Framework file discovery
- Module ID extraction
- Review status checking
- Sequential processing
- Archive functionality
- Summary reporting
- Selective module processing

Author: Course Generator Team
Date: 2026-01-11
"""

import pytest
import json
import shutil
from pathlib import Path
from datetime import datetime
from unittest.mock import Mock, MagicMock, patch

from src.batch_processor import BatchProcessor, BatchProcessResult
from src.config_manager import ConfigManager
from src.models import QuestionBank, Question, QuestionType, QuestionStatus, QuestionDifficulty


@pytest.fixture
def temp_course_dir(tmp_path):
    """Create temporary course directory structure."""
    course_dir = tmp_path / "courses" / "test-course"
    frameworks_dir = course_dir / "frameworks"
    frameworks_dir.mkdir(parents=True, exist_ok=True)

    # Create framework files
    (frameworks_dir / "module-0-framework-REVISED.md").write_text(
        "---\ncourse_code: TEST-M0\nmodule_number: 0\nmodule_title: Test Module 0\n---\n# Module 0"
    )
    (frameworks_dir / "module-1-framework-REVISED.md").write_text(
        "---\ncourse_code: TEST-M1\nmodule_number: 1\nmodule_title: Test Module 1\n---\n# Module 1"
    )
    (frameworks_dir / "module-2-framework.md").write_text(
        "---\ncourse_code: TEST-M2\nmodule_number: 2\nmodule_title: Test Module 2\n---\n# Module 2"
    )

    return course_dir


@pytest.fixture
def temp_question_banks(tmp_path):
    """Create temporary question bank directories."""
    staging_dir = tmp_path / "question_banks" / "staging"
    approved_dir = tmp_path / "question_banks" / "approved"
    rejected_dir = tmp_path / "question_banks" / "rejected"

    staging_dir.mkdir(parents=True, exist_ok=True)
    approved_dir.mkdir(parents=True, exist_ok=True)
    rejected_dir.mkdir(parents=True, exist_ok=True)

    # Create staging questions for module-0
    module_0_staging = QuestionBank(
        module_id="module-0",
        module_title="Test Module 0",
        version="1.0",
        generated_at=datetime.now(),
        questions=[
            Question(
                id="m0-q1",
                type=QuestionType.MULTIPLE_CHOICE,
                question_text="Test question 1?",
                options=["A", "B", "C", "D"],
                correct_answer="A",
                difficulty=QuestionDifficulty.EASY,
                points=1,
                source_section="section-1",
                status=QuestionStatus.PENDING_REVIEW
            )
        ],
        questions_pending=1
    )
    (staging_dir / "module-0-staging.json").write_text(
        json.dumps(module_0_staging.to_dict(), indent=2)
    )

    # Create approved questions for module-1
    module_1_approved = QuestionBank(
        module_id="module-1",
        module_title="Test Module 1",
        version="1.0",
        last_reviewed=datetime.now(),
        questions=[
            Question(
                id="m1-q1",
                type=QuestionType.TRUE_FALSE,
                question_text="Test question?",
                options=["True", "False"],
                correct_answer="True",
                difficulty=QuestionDifficulty.EASY,
                points=1,
                source_section="section-1",
                status=QuestionStatus.APPROVED
            )
        ]
    )
    (approved_dir / "module-1.json").write_text(
        json.dumps(module_1_approved.to_dict(), indent=2)
    )

    return {
        "staging_dir": staging_dir,
        "approved_dir": approved_dir,
        "rejected_dir": rejected_dir
    }


@pytest.fixture
def mock_config(temp_question_banks):
    """Create mock configuration."""
    config = Mock(spec=ConfigManager)
    config.get.side_effect = lambda key, default=None: {
        "questions.staging_directory": str(temp_question_banks["staging_dir"]),
        "questions.approved_directory": str(temp_question_banks["approved_dir"]),
        "questions.rejected_directory": str(temp_question_banks["rejected_dir"]),
        "global.output_directory": "./handouts",
        "global.archive_old_versions": True
    }.get(key, default)
    config.to_dict.return_value = {"test": "config"}
    return config


class TestBatchProcessResult:
    """Test BatchProcessResult data class."""

    def test_successful_result(self):
        """Test creating successful result."""
        result = BatchProcessResult(
            module_id="module-0",
            success=True,
            output_path=Path("test.pdf"),
            processing_time=10.5
        )

        assert result.module_id == "module-0"
        assert result.success is True
        assert result.output_path == Path("test.pdf")
        assert result.error is None
        assert result.blocked_by_review is False
        assert result.processing_time == 10.5

    def test_failed_result(self):
        """Test creating failed result."""
        result = BatchProcessResult(
            module_id="module-1",
            success=False,
            error="Parse error",
            processing_time=5.0
        )

        assert result.module_id == "module-1"
        assert result.success is False
        assert result.error == "Parse error"
        assert result.output_path is None
        assert result.blocked_by_review is False

    def test_blocked_result(self):
        """Test creating blocked result."""
        result = BatchProcessResult(
            module_id="module-2",
            success=False,
            blocked_by_review=True,
            error="Questions pending review"
        )

        assert result.module_id == "module-2"
        assert result.success is False
        assert result.blocked_by_review is True
        assert result.error == "Questions pending review"


class TestBatchProcessor:
    """Test BatchProcessor class."""

    def test_init(self, mock_config):
        """Test BatchProcessor initialization."""
        processor = BatchProcessor(mock_config)

        assert processor.config == mock_config
        assert processor.course_base_dir == Path("courses")

    def test_discover_frameworks(self, mock_config, temp_course_dir):
        """Test discovering framework files."""
        processor = BatchProcessor(mock_config)
        processor.course_base_dir = temp_course_dir.parent

        frameworks = processor.discover_frameworks(temp_course_dir)

        assert len(frameworks) == 3
        # Should be sorted by module number
        assert frameworks[0][1] == "module-0"
        assert frameworks[1][1] == "module-1"
        assert frameworks[2][1] == "module-2"

        # Check paths
        assert frameworks[0][0].name == "module-0-framework-REVISED.md"
        assert frameworks[1][0].name == "module-1-framework-REVISED.md"
        assert frameworks[2][0].name == "module-2-framework.md"

    def test_discover_frameworks_no_directory(self, mock_config, tmp_path):
        """Test discovering frameworks when directory doesn't exist."""
        processor = BatchProcessor(mock_config)
        course_dir = tmp_path / "nonexistent"

        frameworks = processor.discover_frameworks(course_dir)

        assert frameworks == []

    def test_extract_module_id(self, mock_config):
        """Test extracting module ID from various filename patterns."""
        processor = BatchProcessor(mock_config)

        # Standard patterns
        assert processor._extract_module_id(Path("module-0-framework-REVISED.md")) == "module-0"
        assert processor._extract_module_id(Path("module-10-framework.md")) == "module-10"
        assert processor._extract_module_id(Path("module-1-learning-framework.md")) == "module-1"

    def test_extract_module_id_invalid(self, mock_config):
        """Test extracting module ID from invalid filename."""
        processor = BatchProcessor(mock_config)

        with pytest.raises(ValueError, match="Cannot extract module ID"):
            processor._extract_module_id(Path("invalid-file.md"))

    def test_get_module_number(self, mock_config):
        """Test extracting numeric module number."""
        processor = BatchProcessor(mock_config)

        assert processor._get_module_number("module-0") == 0
        assert processor._get_module_number("module-10") == 10
        assert processor._get_module_number("invalid") == 999  # Default for unmatched

    def test_check_review_status(self, mock_config, temp_course_dir, temp_question_banks):
        """Test checking review status for all modules."""
        processor = BatchProcessor(mock_config)
        processor.course_base_dir = temp_course_dir.parent

        frameworks = processor.discover_frameworks(temp_course_dir)
        pending, reviewed, no_questions = processor.check_review_status(frameworks)

        # module-0 has pending questions
        assert "module-0" in pending
        # module-1 has approved questions
        assert "module-1" in reviewed
        # module-2 has no questions
        assert "module-2" in no_questions

    def test_archive_old_handout(self, mock_config, tmp_path):
        """Test archiving old handout before regeneration."""
        processor = BatchProcessor(mock_config)

        # Create existing handout
        output_dir = tmp_path / "handouts"
        output_dir.mkdir(parents=True, exist_ok=True)
        old_pdf = output_dir / "TEST-module-0-handout.pdf"
        old_pdf.write_text("old content")

        # Archive it
        archived_path = processor.archive_old_handout(
            course_code="TEST",
            module_number=0,
            output_dir=output_dir
        )

        # Old file should be moved
        assert not old_pdf.exists()
        # Archive should exist
        assert archived_path is not None
        assert archived_path.exists()
        assert "archive" in str(archived_path)
        assert "TEST-module-0-handout" in archived_path.name

    def test_archive_no_existing_handout(self, mock_config, tmp_path):
        """Test archiving when no existing handout."""
        processor = BatchProcessor(mock_config)

        output_dir = tmp_path / "handouts"
        output_dir.mkdir(parents=True, exist_ok=True)

        # No existing file
        archived_path = processor.archive_old_handout(
            course_code="TEST",
            module_number=0,
            output_dir=output_dir
        )

        assert archived_path is None

    def test_archive_disabled_in_config(self, tmp_path):
        """Test archiving when disabled in config."""
        config = Mock(spec=ConfigManager)
        config.get.side_effect = lambda key, default=None: {
            "global.archive_old_versions": False
        }.get(key, default)

        processor = BatchProcessor(config)

        output_dir = tmp_path / "handouts"
        output_dir.mkdir(parents=True, exist_ok=True)
        old_pdf = output_dir / "TEST-module-0-handout.pdf"
        old_pdf.write_text("old content")

        archived_path = processor.archive_old_handout(
            course_code="TEST",
            module_number=0,
            output_dir=output_dir
        )

        # Should not archive
        assert archived_path is None
        # Old file still exists
        assert old_pdf.exists()

    @patch('src.batch_processor.FrameworkParser')
    @patch('src.batch_processor.ContentTransformer')
    @patch('src.batch_processor.QuestionLoader')
    @patch('src.batch_processor.QuestionReviewer')
    @patch('src.batch_processor.ImageProcessor')
    @patch('src.batch_processor.LayoutEngine')
    @patch('src.batch_processor.PDFRenderer')
    def test_process_single_module_success(
        self,
        mock_pdf_renderer,
        mock_layout_engine,
        mock_image_processor,
        mock_question_reviewer,
        mock_question_loader,
        mock_content_transformer,
        mock_framework_parser,
        mock_config,
        tmp_path
    ):
        """Test processing a single module successfully."""
        # Setup mocks
        mock_parse_result = Mock()
        mock_parse_result.success = True
        mock_parse_result.errors = []
        mock_parse_result.warnings = []
        mock_parse_result.metadata.course_code = "TEST"
        mock_parse_result.metadata.module_number = 0
        mock_parse_result.metadata.module_title = "Test Module"
        mock_parse_result.sections = []
        mock_parse_result.images = []

        mock_framework_parser.return_value.parse_file.return_value = mock_parse_result
        mock_content_transformer.return_value.transform.return_value = []

        # Mock review status as "all reviewed" (not pending)
        mock_reviewer_instance = Mock()
        mock_reviewer_instance.get_review_status.return_value = {
            "status": "all_reviewed",
            "pending_count": 0
        }
        mock_question_reviewer.return_value = mock_reviewer_instance

        mock_question_loader.return_value.load_questions.return_value = []
        mock_image_processor.return_value.process_images.return_value = []
        mock_layout_engine.return_value.render.return_value = "<html></html>"
        mock_pdf_renderer.return_value.render_handout.return_value = Path("test.pdf")

        # Process
        processor = BatchProcessor(mock_config)
        result = processor.process_single_module(
            framework_path=Path("test.md"),
            module_id="module-0",
            output_dir=tmp_path,
            force_unreviewed=False
        )

        # Assertions
        assert result.success is True
        assert result.module_id == "module-0"
        assert result.output_path == Path("test.pdf")
        assert result.error is None
        assert result.processing_time > 0

    @patch('src.batch_processor.FrameworkParser')
    def test_process_single_module_parse_error(
        self,
        mock_framework_parser,
        mock_config,
        tmp_path
    ):
        """Test processing a module with parse error."""
        # Setup mock parse error
        mock_parse_result = Mock()
        mock_parse_result.success = False
        mock_parse_result.errors = ["Invalid YAML frontmatter"]

        mock_framework_parser.return_value.parse_file.return_value = mock_parse_result

        # Process
        processor = BatchProcessor(mock_config)
        result = processor.process_single_module(
            framework_path=Path("test.md"),
            module_id="module-0",
            output_dir=tmp_path,
            force_unreviewed=False
        )

        # Assertions
        assert result.success is False
        assert result.module_id == "module-0"
        assert "Parse error" in result.error
        assert result.blocked_by_review is False

    @patch('src.batch_processor.FrameworkParser')
    @patch('src.batch_processor.QuestionReviewer')
    def test_process_single_module_blocked_by_review(
        self,
        mock_question_reviewer,
        mock_framework_parser,
        mock_config,
        tmp_path
    ):
        """Test processing blocked by pending review."""
        # Setup mocks
        mock_parse_result = Mock()
        mock_parse_result.success = True
        mock_parse_result.metadata.course_code = "TEST"
        mock_parse_result.metadata.module_number = 0

        mock_framework_parser.return_value.parse_file.return_value = mock_parse_result

        # Mock pending review status
        mock_reviewer_instance = Mock()
        mock_reviewer_instance.get_review_status.return_value = {
            "status": "pending_review",
            "pending_count": 5
        }
        mock_question_reviewer.return_value = mock_reviewer_instance

        # Process (without force)
        processor = BatchProcessor(mock_config)
        result = processor.process_single_module(
            framework_path=Path("test.md"),
            module_id="module-0",
            output_dir=tmp_path,
            force_unreviewed=False
        )

        # Assertions
        assert result.success is False
        assert result.blocked_by_review is True
        assert "5 questions pending review" in result.error

    def test_process_course_no_frameworks(self, mock_config, tmp_path):
        """Test batch processing when no frameworks found."""
        processor = BatchProcessor(mock_config)
        processor.course_base_dir = tmp_path / "courses"

        results = processor.process_course(
            course_name="nonexistent-course",
            module_numbers=None,
            force_unreviewed=False
        )

        assert results == {}

    def test_process_course_selective_modules(
        self,
        mock_config,
        temp_course_dir,
        temp_question_banks
    ):
        """Test selective module processing."""
        processor = BatchProcessor(mock_config)
        processor.course_base_dir = temp_course_dir.parent

        # Mock process_single_module to avoid actual processing
        with patch.object(processor, 'process_single_module') as mock_process:
            mock_process.return_value = BatchProcessResult(
                module_id="module-0",
                success=True,
                output_path=Path("test.pdf"),
                processing_time=1.0
            )

            # Process only modules 0 and 1
            results = processor.process_course(
                course_name="test-course",
                module_numbers=[0, 1],
                force_unreviewed=True
            )

            # Should only process 2 modules
            assert len(results) == 2
            assert "module-0" in results
            assert "module-1" in results
            assert "module-2" not in results

    def test_process_course_blocked_by_review(
        self,
        mock_config,
        temp_course_dir,
        temp_question_banks
    ):
        """Test batch processing blocked by pending reviews."""
        processor = BatchProcessor(mock_config)
        processor.course_base_dir = temp_course_dir.parent

        # Process without force (module-0 has pending questions)
        results = processor.process_course(
            course_name="test-course",
            module_numbers=None,
            force_unreviewed=False
        )

        # Should be blocked
        assert "module-0" in results
        assert results["module-0"].blocked_by_review is True


class TestBatchProcessorIntegration:
    """Integration tests for batch processing."""

    def test_full_batch_workflow_simulation(
        self,
        mock_config,
        temp_course_dir,
        temp_question_banks
    ):
        """Simulate full batch processing workflow."""
        processor = BatchProcessor(mock_config)
        processor.course_base_dir = temp_course_dir.parent

        # Discover frameworks
        frameworks = processor.discover_frameworks(temp_course_dir)
        assert len(frameworks) == 3

        # Check review status
        pending, reviewed, no_questions = processor.check_review_status(frameworks)
        assert len(pending) == 1  # module-0
        assert len(reviewed) == 1  # module-1
        assert len(no_questions) == 1  # module-2

        # Verify specific modules
        assert "module-0" in pending
        assert "module-1" in reviewed
        assert "module-2" in no_questions


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
