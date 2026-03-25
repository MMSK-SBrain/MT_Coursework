"""
Tests for Question Generator

Tests AI-powered question generation with mocked Anthropic API calls.
"""

import json
import pytest
import os
from pathlib import Path
from datetime import datetime
from unittest.mock import Mock, MagicMock, patch

from src.question_generator import QuestionGenerator
from src.models import (
    ContentSection,
    FrameworkMetadata,
    QuestionType,
    QuestionStatus,
    QuestionSource,
    QuestionDifficulty
)
from src.error_handler import FatalError, RecoverableError


@pytest.fixture
def config():
    """Test configuration."""
    return {
        "questions": {
            "enabled": True,
            "questions_per_section": 7,
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
            "staging_directory": "./test_staging"
        }
    }


@pytest.fixture
def mock_anthropic_client(mocker):
    """Mock Anthropic client."""
    # Mock the Anthropic class
    mock_client = mocker.patch('src.question_generator.Anthropic')

    # Create mock message response
    mock_message = Mock()
    mock_content = Mock()
    mock_content.text = json.dumps([
        {
            "question_text": "What is machine learning?",
            "type": "multiple_choice",
            "options": ["A type of database", "AI that learns from data", "A programming language", "A cloud service"],
            "correct_answer": "B",
            "explanation": "Machine learning is a subset of AI that learns patterns from data.",
            "difficulty": "easy",
            "points": 1,
            "learning_outcome": "Understand ML basics"
        },
        {
            "question_text": "Is Python required for machine learning?",
            "type": "true_false",
            "options": ["True", "False"],
            "correct_answer": "False",
            "explanation": "While Python is popular, ML can be done in other languages too.",
            "difficulty": "easy",
            "points": 1,
            "learning_outcome": "Understand ML tools"
        },
        {
            "question_text": "Name three common ML libraries.",
            "type": "short_answer",
            "options": None,
            "correct_answer": "scikit-learn, TensorFlow, PyTorch",
            "explanation": "These are the most popular ML libraries in Python.",
            "difficulty": "medium",
            "points": 2,
            "learning_outcome": "Recognize ML libraries"
        }
    ])
    mock_message.content = [mock_content]

    # Set up the mock client instance
    mock_instance = Mock()
    mock_instance.messages.create.return_value = mock_message
    mock_client.return_value = mock_instance

    return mock_client


@pytest.fixture
def sample_section():
    """Sample content section."""
    return ContentSection(
        id="session-1",
        level=2,
        title="Introduction to Machine Learning",
        content="""
# Introduction to Machine Learning

Machine learning is a subset of artificial intelligence that enables computers to learn from data.

## Key Concepts
- Supervised learning
- Unsupervised learning
- Reinforcement learning

ML uses algorithms to identify patterns in data and make predictions.
        """,
        include_in_handout=True,
        metadata={"learning_outcome": "Understand ML fundamentals"}
    )


@pytest.fixture
def sample_metadata():
    """Sample framework metadata."""
    return FrameworkMetadata(
        course_code="ML-ENG-M0",
        module_number=0,
        module_title="The Hook - Welcome to Machine Learning",
        duration="1 week",
        video_content="~4.5 hours"
    )


class TestQuestionGeneratorInit:
    """Test QuestionGenerator initialization."""

    def test_init_success(self, config, mock_anthropic_client, monkeypatch):
        """Test successful initialization."""
        monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-ant-test123")

        generator = QuestionGenerator(config)

        assert generator.model == "claude-sonnet-4-20250514"
        assert generator.max_retries == 3
        assert generator.timeout_seconds == 60
        assert generator.questions_per_section == 7
        assert len(generator.enabled_types) == 5

    def test_init_missing_api_key(self, config, monkeypatch):
        """Test initialization fails without API key."""
        monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
        # Make sure Anthropic SDK is marked as available
        monkeypatch.setattr('src.question_generator.ANTHROPIC_AVAILABLE', True)

        with pytest.raises(FatalError) as exc_info:
            QuestionGenerator(config)

        assert "ANTHROPIC_API_KEY" in str(exc_info.value)
        assert "not set" in str(exc_info.value)

    def test_init_questions_disabled(self, config, monkeypatch):
        """Test initialization fails when questions disabled."""
        monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-ant-test123")
        config["questions"]["enabled"] = False

        with pytest.raises(FatalError) as exc_info:
            QuestionGenerator(config)

        assert "disabled" in str(exc_info.value)

    def test_init_ai_disabled(self, config, monkeypatch):
        """Test initialization fails when AI generation disabled."""
        monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-ant-test123")
        config["questions"]["ai_generation"]["enabled"] = False

        with pytest.raises(FatalError) as exc_info:
            QuestionGenerator(config)

        assert "AI" in str(exc_info.value)


class TestQuestionGeneration:
    """Test question generation."""

    def test_generate_questions_for_section(self, config, mock_anthropic_client, sample_section, monkeypatch):
        """Test generating questions for a single section."""
        monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-ant-test123")

        generator = QuestionGenerator(config)
        questions = generator.generate_questions_for_section(
            section=sample_section,
            course_name="ML for Engineers",
            module_title="Module 0",
            question_count=3
        )

        assert len(questions) == 3
        assert all(q.status == QuestionStatus.PENDING_REVIEW for q in questions)
        assert all(q.source == QuestionSource.AI_GENERATED for q in questions)
        assert questions[0].type == QuestionType.MULTIPLE_CHOICE
        assert questions[1].type == QuestionType.TRUE_FALSE
        assert questions[2].type == QuestionType.SHORT_ANSWER

    def test_generate_questions_for_module(self, config, mock_anthropic_client, sample_metadata, sample_section, monkeypatch, tmp_path):
        """Test generating questions for entire module."""
        monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-ant-test123")
        config["questions"]["staging_directory"] = str(tmp_path / "staging")

        generator = QuestionGenerator(config)

        sections = [sample_section]
        question_bank = generator.generate_questions_for_module(
            metadata=sample_metadata,
            sections=sections,
            course_name="ML for Engineers"
        )

        assert question_bank.module_id == "module-0"
        assert question_bank.module_title == sample_metadata.module_title
        assert question_bank.model_used == "claude-sonnet-4-20250514"
        assert len(question_bank.questions) > 0
        assert question_bank.questions_pending > 0
        assert question_bank.questions_reviewed == 0

    def test_api_response_with_markdown(self, config, mocker, sample_section, monkeypatch):
        """Test parsing API response with markdown code blocks."""
        monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-ant-test123")

        # Mock response with markdown code blocks
        mock_client = mocker.patch('src.question_generator.Anthropic')
        mock_message = Mock()
        mock_content = Mock()
        mock_content.text = """```json
[
  {
    "question_text": "Test question",
    "type": "multiple_choice",
    "options": ["A", "B"],
    "correct_answer": "A",
    "explanation": "Test",
    "difficulty": "easy",
    "points": 1
  }
]
```"""
        mock_message.content = [mock_content]
        mock_instance = Mock()
        mock_instance.messages.create.return_value = mock_message
        mock_client.return_value = mock_instance

        generator = QuestionGenerator(config)
        questions = generator.generate_questions_for_section(
            section=sample_section,
            course_name="ML for Engineers",
            module_title="Module 0",
            question_count=1
        )

        assert len(questions) == 1
        assert questions[0].question_text == "Test question"


class TestAPIRetryLogic:
    """Test API retry logic with exponential backoff."""

    def test_rate_limit_retry(self, config, mocker, sample_section, monkeypatch):
        """Test retry on rate limit."""
        monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-ant-test123")

        # Mock to fail twice, then succeed
        mock_client = mocker.patch('src.question_generator.Anthropic')
        mock_instance = Mock()

        # Import the actual exception class
        from anthropic import RateLimitError

        # First two calls raise RateLimitError, third succeeds
        mock_message = Mock()
        mock_content = Mock()
        mock_content.text = json.dumps([{
            "question_text": "Test",
            "type": "multiple_choice",
            "options": ["A", "B"],
            "correct_answer": "A",
            "explanation": "Test",
            "difficulty": "easy",
            "points": 1
        }])
        mock_message.content = [mock_content]

        # Create mock response and body for exceptions
        mock_response = Mock()
        mock_response.status_code = 429
        mock_body = {"error": {"message": "Rate limit"}}

        mock_instance.messages.create.side_effect = [
            RateLimitError("Rate limit", response=mock_response, body=mock_body),
            RateLimitError("Rate limit", response=mock_response, body=mock_body),
            mock_message
        ]
        mock_client.return_value = mock_instance

        generator = QuestionGenerator(config)

        # Should succeed after retries
        questions = generator.generate_questions_for_section(
            section=sample_section,
            course_name="ML for Engineers",
            module_title="Module 0",
            question_count=1
        )

        assert len(questions) == 1
        assert mock_instance.messages.create.call_count == 3

    def test_timeout_retry(self, config, mocker, sample_section, monkeypatch):
        """Test retry on timeout."""
        monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-ant-test123")

        mock_client = mocker.patch('src.question_generator.Anthropic')
        mock_instance = Mock()

        from anthropic import APITimeoutError

        mock_message = Mock()
        mock_content = Mock()
        mock_content.text = json.dumps([{
            "question_text": "Test",
            "type": "multiple_choice",
            "options": ["A", "B"],
            "correct_answer": "A",
            "explanation": "Test",
            "difficulty": "easy",
            "points": 1
        }])
        mock_message.content = [mock_content]

        mock_instance.messages.create.side_effect = [
            APITimeoutError("Timeout"),
            mock_message
        ]
        mock_client.return_value = mock_instance

        generator = QuestionGenerator(config)
        questions = generator.generate_questions_for_section(
            section=sample_section,
            course_name="ML for Engineers",
            module_title="Module 0",
            question_count=1
        )

        assert len(questions) == 1
        assert mock_instance.messages.create.call_count == 2

    def test_authentication_error_no_retry(self, config, mocker, sample_section, monkeypatch):
        """Test authentication error causes immediate failure."""
        monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-ant-test123")

        mock_client = mocker.patch('src.question_generator.Anthropic')
        mock_instance = Mock()

        from anthropic import AuthenticationError

        # Create mock response and body for exception
        mock_response = Mock()
        mock_response.status_code = 401
        mock_body = {"error": {"message": "Invalid API key"}}

        mock_instance.messages.create.side_effect = AuthenticationError("Invalid API key", response=mock_response, body=mock_body)
        mock_client.return_value = mock_instance

        generator = QuestionGenerator(config)

        with pytest.raises(FatalError) as exc_info:
            generator.generate_questions_for_section(
                section=sample_section,
                course_name="ML for Engineers",
                module_title="Module 0",
                question_count=1
            )

        assert "authentication" in str(exc_info.value).lower()
        assert mock_instance.messages.create.call_count == 1  # No retry

    def test_max_retries_exceeded(self, config, mocker, sample_section, monkeypatch):
        """Test failure after max retries."""
        monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-ant-test123")

        mock_client = mocker.patch('src.question_generator.Anthropic')
        mock_instance = Mock()

        from anthropic import RateLimitError

        # Create mock response and body for exception
        mock_response = Mock()
        mock_response.status_code = 429
        mock_body = {"error": {"message": "Rate limit"}}

        # Always fail
        mock_instance.messages.create.side_effect = RateLimitError("Rate limit", response=mock_response, body=mock_body)
        mock_client.return_value = mock_instance

        generator = QuestionGenerator(config)

        with pytest.raises(RecoverableError) as exc_info:
            generator.generate_questions_for_section(
                section=sample_section,
                course_name="ML for Engineers",
                module_title="Module 0",
                question_count=1
            )

        assert "retries" in str(exc_info.value).lower()
        assert mock_instance.messages.create.call_count == 3  # max_retries


class TestStagingFiles:
    """Test staging file operations."""

    def test_save_staging_file(self, config, mock_anthropic_client, sample_metadata, sample_section, monkeypatch, tmp_path):
        """Test saving staging file."""
        monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-ant-test123")
        config["questions"]["staging_directory"] = str(tmp_path / "staging")

        generator = QuestionGenerator(config)
        question_bank = generator.generate_questions_for_module(
            metadata=sample_metadata,
            sections=[sample_section]
        )

        staging_file = tmp_path / "staging" / "module-0-staging.json"
        assert staging_file.exists()

        # Verify content
        with open(staging_file) as f:
            data = json.load(f)

        assert data["module_id"] == "module-0"
        assert "questions" in data
        assert len(data["questions"]) > 0
        assert data["model_used"] == "claude-sonnet-4-20250514"

    def test_load_staging_file(self, config, mock_anthropic_client, sample_metadata, sample_section, monkeypatch, tmp_path):
        """Test loading staging file."""
        monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-ant-test123")
        config["questions"]["staging_directory"] = str(tmp_path / "staging")

        generator = QuestionGenerator(config)

        # Generate and save
        original_bank = generator.generate_questions_for_module(
            metadata=sample_metadata,
            sections=[sample_section]
        )

        # Load
        loaded_bank = generator.load_staging_file("module-0")

        assert loaded_bank is not None
        assert loaded_bank.module_id == original_bank.module_id
        assert len(loaded_bank.questions) == len(original_bank.questions)

    def test_load_nonexistent_staging_file(self, config, mock_anthropic_client, monkeypatch, tmp_path):
        """Test loading non-existent staging file returns None."""
        monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-ant-test123")
        config["questions"]["staging_directory"] = str(tmp_path / "staging")

        generator = QuestionGenerator(config)
        loaded_bank = generator.load_staging_file("module-999")

        assert loaded_bank is None

    def test_has_pending_questions(self, config, mock_anthropic_client, sample_metadata, sample_section, monkeypatch, tmp_path):
        """Test checking for pending questions."""
        monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-ant-test123")
        config["questions"]["staging_directory"] = str(tmp_path / "staging")

        generator = QuestionGenerator(config)

        # No staging file yet
        assert not generator.has_pending_questions("module-0")

        # Generate questions
        generator.generate_questions_for_module(
            metadata=sample_metadata,
            sections=[sample_section]
        )

        # Now has pending questions
        assert generator.has_pending_questions("module-0")

    def test_get_staging_status(self, config, mock_anthropic_client, sample_metadata, sample_section, monkeypatch, tmp_path):
        """Test getting staging status."""
        monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-ant-test123")
        config["questions"]["staging_directory"] = str(tmp_path / "staging")

        generator = QuestionGenerator(config)

        # No staging file
        status = generator.get_staging_status("module-0")
        assert not status["exists"]
        assert status["pending"] == 0

        # Generate questions
        generator.generate_questions_for_module(
            metadata=sample_metadata,
            sections=[sample_section]
        )

        # Check status
        status = generator.get_staging_status("module-0")
        assert status["exists"]
        assert status["pending"] > 0
        assert status["total"] > 0
        assert status["model_used"] == "claude-sonnet-4-20250514"


class TestInvalidResponses:
    """Test handling of invalid API responses."""

    def test_invalid_json_response(self, config, mocker, sample_section, monkeypatch):
        """Test handling of invalid JSON."""
        monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-ant-test123")

        mock_client = mocker.patch('src.question_generator.Anthropic')
        mock_message = Mock()
        mock_content = Mock()
        mock_content.text = "This is not valid JSON"
        mock_message.content = [mock_content]
        mock_instance = Mock()
        mock_instance.messages.create.return_value = mock_message
        mock_client.return_value = mock_instance

        generator = QuestionGenerator(config)

        with pytest.raises(RecoverableError) as exc_info:
            generator.generate_questions_for_section(
                section=sample_section,
                course_name="ML for Engineers",
                module_title="Module 0",
                question_count=1
            )

        assert "JSON" in str(exc_info.value)

    def test_missing_required_fields(self, config, mocker, sample_section, monkeypatch):
        """Test handling of missing required fields in questions."""
        monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-ant-test123")

        mock_client = mocker.patch('src.question_generator.Anthropic')
        mock_message = Mock()
        mock_content = Mock()
        # Missing 'type' field
        mock_content.text = json.dumps([{
            "question_text": "Test question",
            "difficulty": "easy"
        }])
        mock_message.content = [mock_content]
        mock_instance = Mock()
        mock_instance.messages.create.return_value = mock_message
        mock_client.return_value = mock_instance

        generator = QuestionGenerator(config)

        with pytest.raises(RecoverableError) as exc_info:
            generator.generate_questions_for_section(
                section=sample_section,
                course_name="ML for Engineers",
                module_title="Module 0",
                question_count=1
            )

        assert "No valid questions" in str(exc_info.value)


class TestModuleSpecificConfig:
    """Test module-specific configuration overrides."""

    def test_module_specific_question_count(self, config, mock_anthropic_client, sample_metadata, sample_section, monkeypatch, tmp_path):
        """Test module-specific question count override."""
        monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-ant-test123")
        config["questions"]["staging_directory"] = str(tmp_path / "staging")

        # Add module-specific config
        config["modules"] = {
            "module-0": {
                "questions": {
                    "questions_per_section": 3  # Override default of 7
                }
            }
        }

        generator = QuestionGenerator(config)

        # The mock returns exactly 3 questions, so this should work
        question_bank = generator.generate_questions_for_module(
            metadata=sample_metadata,
            sections=[sample_section]
        )

        assert len(question_bank.questions) == 3  # Should use module-specific config


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
