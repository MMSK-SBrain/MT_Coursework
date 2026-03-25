"""
AI Question Generator

Generates self-study questions using the Anthropic Claude API.
Questions are saved to staging files for mandatory review.

Based on PRD Section 12 and Story 9 in ARCHITECTURE.md
"""

import os
import json
import time
import logging
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Optional

try:
    from anthropic import Anthropic
    import anthropic
    ANTHROPIC_AVAILABLE = True
except ImportError:
    ANTHROPIC_AVAILABLE = False
    # Create dummy classes for type hints
    class Anthropic:
        pass
    class anthropic:
        class RateLimitError(Exception):
            pass
        class APITimeoutError(Exception):
            pass
        class APIConnectionError(Exception):
            pass
        class AuthenticationError(Exception):
            pass

from src.models import (
    ContentSection,
    Question,
    QuestionType,
    QuestionDifficulty,
    QuestionSource,
    QuestionStatus,
    QuestionBank,
    FrameworkMetadata
)
from src.ai_prompts import (
    SYSTEM_PROMPT,
    get_question_generation_prompt,
    calculate_question_distribution
)
from src.error_handler import FatalError, RecoverableError


logger = logging.getLogger(__name__)


class QuestionGenerator:
    """
    Generates self-study questions using Claude API.

    Accepts ContentSection objects and generates contextual questions
    that are saved to staging files for mandatory review.
    """

    def __init__(self, config: Dict[str, Any]):
        """
        Initialize question generator.

        Args:
            config: Configuration dict from handout_config.yaml

        Raises:
            FatalError: If Anthropic SDK not installed or API key missing
        """
        self.config = config
        self.questions_config = config.get("questions", {})
        self.ai_config = self.questions_config.get("ai_generation", {})

        # Validate configuration
        if not self.questions_config.get("enabled", True):
            raise FatalError(
                message="Question generation is disabled in configuration",
                module="QuestionGenerator"
            )

        if not self.ai_config.get("enabled", True):
            raise FatalError(
                message="AI question generation is disabled in configuration",
                module="QuestionGenerator"
            )

        # Check if Anthropic SDK is installed
        if not ANTHROPIC_AVAILABLE:
            raise FatalError(
                message="Anthropic SDK not installed",
                module="QuestionGenerator",
                action="Run: pip install anthropic"
            )

        # Get API key from environment
        api_key_env_var = self.ai_config.get("api_key_env_var", "ANTHROPIC_API_KEY")
        self.api_key = os.environ.get(api_key_env_var)

        if not self.api_key:
            raise FatalError(
                message=f"{api_key_env_var} environment variable not set",
                module="QuestionGenerator",
                context="AI question generation requires valid API credentials",
                action=f"Set environment variable: export {api_key_env_var}=sk-ant-xxxxxxxxxxxxxxxxxxxxx"
            )

        # Initialize Anthropic client
        self.client = Anthropic(api_key=self.api_key)

        # Configuration parameters
        self.model = self.ai_config.get("model", "claude-sonnet-4-20250514")
        self.max_retries = self.ai_config.get("max_retries", 3)
        self.timeout_seconds = self.ai_config.get("timeout_seconds", 60)
        self.questions_per_section = self.questions_config.get("questions_per_section", 7)
        self.enabled_types = self.questions_config.get("types", [
            "multiple_choice", "true_false", "short_answer", "reflection", "application"
        ])

        # Staging directory
        self.staging_dir = Path(self.questions_config.get(
            "staging_directory", "./question_banks/staging"
        ))
        self.staging_dir.mkdir(parents=True, exist_ok=True)

        logger.info(f"QuestionGenerator initialized with model: {self.model}")

    def generate_questions_for_module(
        self,
        metadata: FrameworkMetadata,
        sections: List[ContentSection],
        course_name: str = "Machine Learning for Engineers"
    ) -> QuestionBank:
        """
        Generate questions for all major sections in a module.

        Args:
            metadata: Module metadata
            sections: List of content sections
            course_name: Name of the course

        Returns:
            QuestionBank with generated questions (status: pending_review)

        Raises:
            FatalError: If generation fails completely
        """
        logger.info(f"Generating questions for module: {metadata.module_title}")

        # Create question bank
        question_bank = QuestionBank(
            module_id=f"module-{metadata.module_number}",
            module_title=metadata.module_title,
            version="1.0",
            generated_at=datetime.now(),
            model_used=self.model
        )

        # Filter to major sections (level 2 headers - "##")
        major_sections = [s for s in sections if s.level == 2 and s.include_in_handout]

        logger.info(f"Found {len(major_sections)} major sections to generate questions for")

        # Generate questions for each major section
        for i, section in enumerate(major_sections, 1):
            logger.info(f"Processing section {i}/{len(major_sections)}: {section.title}")

            # Get module-specific question count if configured
            module_config = self.config.get("modules", {}).get(
                question_bank.module_id, {}
            )
            section_question_count = module_config.get(
                "questions", {}
            ).get("questions_per_section", self.questions_per_section)

            try:
                questions = self.generate_questions_for_section(
                    section=section,
                    course_name=course_name,
                    module_title=metadata.module_title,
                    question_count=section_question_count
                )

                # Add questions to bank
                for question in questions:
                    question_bank.add_question(question)

                logger.info(f"Generated {len(questions)} questions for section: {section.title}")

            except Exception as e:
                logger.error(f"Failed to generate questions for section '{section.title}': {e}")
                # Continue with other sections
                continue

        # Save to staging file
        self.save_staging_file(question_bank)

        logger.info(
            f"Question generation complete: {len(question_bank.questions)} questions generated, "
            f"{question_bank.questions_pending} pending review"
        )

        return question_bank

    def generate_questions_for_section(
        self,
        section: ContentSection,
        course_name: str,
        module_title: str,
        question_count: int
    ) -> List[Question]:
        """
        Generate questions for a single section using Claude API.

        Args:
            section: Content section to generate questions for
            course_name: Name of the course
            module_title: Title of the module
            question_count: Number of questions to generate

        Returns:
            List of Question objects (status: pending_review)

        Raises:
            RecoverableError: If generation fails after all retries
        """
        # Calculate question distribution
        distribution = calculate_question_distribution(
            total_questions=question_count,
            enabled_types=self.enabled_types
        )

        # Extract learning outcome from section metadata or use section title
        learning_outcome = section.metadata.get(
            "learning_outcome",
            f"Understand {section.title}"
        )

        # Build prompt
        user_prompt = get_question_generation_prompt(
            course_name=course_name,
            module_title=module_title,
            section_title=section.title,
            section_content=section.content[:2000],  # Limit content to avoid token limits
            learning_outcome=learning_outcome,
            question_count=question_count,
            question_distribution=distribution
        )

        # Call API with retry logic
        response_text = self._call_api_with_retry(user_prompt)

        # Parse response
        questions = self._parse_api_response(
            response_text=response_text,
            section=section,
            learning_outcome=learning_outcome
        )

        return questions

    def _call_api_with_retry(self, user_prompt: str) -> str:
        """
        Call Claude API with exponential backoff retry logic.

        Args:
            user_prompt: The user prompt to send

        Returns:
            API response text

        Raises:
            FatalError: If authentication fails
            RecoverableError: If all retries fail
        """
        last_error = None

        for attempt in range(self.max_retries):
            try:
                logger.debug(f"API call attempt {attempt + 1}/{self.max_retries}")

                message = self.client.messages.create(
                    model=self.model,
                    max_tokens=4000,
                    temperature=0.7,
                    system=SYSTEM_PROMPT,
                    messages=[{"role": "user", "content": user_prompt}],
                    timeout=self.timeout_seconds
                )

                # Extract response text
                response_text = message.content[0].text
                logger.debug(f"API call successful, received {len(response_text)} characters")
                return response_text

            except anthropic.RateLimitError as e:
                last_error = e
                wait_time = 2 ** attempt  # Exponential backoff: 1s, 2s, 4s
                logger.warning(
                    f"Rate limit hit, attempt {attempt + 1}/{self.max_retries}. "
                    f"Waiting {wait_time}s before retry..."
                )
                time.sleep(wait_time)

            except anthropic.APITimeoutError as e:
                last_error = e
                logger.warning(
                    f"API timeout, attempt {attempt + 1}/{self.max_retries}. "
                    f"Retrying..."
                )
                # Continue immediately for timeout (no wait)

            except anthropic.APIConnectionError as e:
                last_error = e
                wait_time = 2 ** attempt
                logger.warning(
                    f"API connection error, attempt {attempt + 1}/{self.max_retries}. "
                    f"Waiting {wait_time}s before retry..."
                )
                time.sleep(wait_time)

            except anthropic.AuthenticationError as e:
                # Authentication errors are fatal - don't retry
                raise FatalError(
                    message="API authentication failed",
                    module="QuestionGenerator",
                    context=str(e),
                    action="Verify ANTHROPIC_API_KEY is correct"
                )

            except Exception as e:
                # Unexpected errors
                logger.error(f"Unexpected API error: {type(e).__name__}: {e}")
                last_error = e
                # Don't retry on unexpected errors
                break

        # All retries failed
        raise RecoverableError(
            message=f"API request failed after {self.max_retries} retries",
            module="QuestionGenerator",
            context=f"Last error: {type(last_error).__name__}: {str(last_error)}",
            action="Check API status or try again later"
        )

    def _parse_api_response(
        self,
        response_text: str,
        section: ContentSection,
        learning_outcome: str
    ) -> List[Question]:
        """
        Parse API response JSON into Question objects.

        Args:
            response_text: Raw API response text
            section: The section these questions relate to
            learning_outcome: Associated learning outcome

        Returns:
            List of Question objects

        Raises:
            RecoverableError: If parsing fails
        """
        try:
            # Try to extract JSON from response (may have markdown code blocks)
            json_text = response_text.strip()

            # Remove markdown code blocks if present
            if json_text.startswith("```json"):
                json_text = json_text[7:]  # Remove ```json
            if json_text.startswith("```"):
                json_text = json_text[3:]  # Remove ```
            if json_text.endswith("```"):
                json_text = json_text[:-3]  # Remove ```

            json_text = json_text.strip()

            # Parse JSON
            questions_data = json.loads(json_text)

            if not isinstance(questions_data, list):
                raise ValueError("Response is not a JSON array")

            # Convert to Question objects
            questions = []
            for i, q_data in enumerate(questions_data, 1):
                try:
                    question = self._create_question_from_api_data(
                        q_data=q_data,
                        section=section,
                        learning_outcome=learning_outcome,
                        index=i
                    )
                    questions.append(question)
                except Exception as e:
                    logger.warning(f"Failed to parse question {i}: {e}")
                    # Continue with other questions
                    continue

            if not questions:
                raise ValueError("No valid questions parsed from response")

            return questions

        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse API response as JSON: {e}")
            logger.debug(f"Response text: {response_text[:500]}")
            raise RecoverableError(
                message="Invalid JSON response from API",
                module="QuestionGenerator",
                context=str(e),
                action="This may indicate a model issue. Try regenerating."
            )
        except Exception as e:
            logger.error(f"Failed to parse API response: {e}")
            raise RecoverableError(
                message="Failed to parse API response",
                module="QuestionGenerator",
                context=str(e),
                action="Check API response format"
            )

    def _create_question_from_api_data(
        self,
        q_data: Dict[str, Any],
        section: ContentSection,
        learning_outcome: str,
        index: int
    ) -> Question:
        """
        Create Question object from API response data.

        Args:
            q_data: Question data from API
            section: The section this question relates to
            learning_outcome: Associated learning outcome
            index: Question index for ID generation

        Returns:
            Question object

        Raises:
            ValueError: If required fields are missing
        """
        # Validate required fields
        required_fields = ["question_text", "type", "difficulty"]
        for field in required_fields:
            if field not in q_data:
                raise ValueError(f"Missing required field: {field}")

        # Generate unique ID
        question_id = f"{section.id}-q{index}"

        # Parse question type
        try:
            question_type = QuestionType(q_data["type"])
        except ValueError:
            raise ValueError(f"Invalid question type: {q_data['type']}")

        # Parse difficulty
        try:
            difficulty = QuestionDifficulty(q_data["difficulty"])
        except ValueError:
            # Default to medium if invalid
            difficulty = QuestionDifficulty.MEDIUM

        # Create question
        question = Question(
            id=question_id,
            type=question_type,
            question_text=q_data["question_text"],
            options=q_data.get("options"),
            correct_answer=q_data.get("correct_answer"),
            explanation=q_data.get("explanation"),
            points=q_data.get("points", 1),
            difficulty=difficulty,
            learning_outcome=q_data.get("learning_outcome", learning_outcome),
            source_section=section.id,
            source=QuestionSource.AI_GENERATED,
            status=QuestionStatus.PENDING_REVIEW
        )

        return question

    def save_staging_file(self, question_bank: QuestionBank) -> Path:
        """
        Save question bank to staging file.

        Args:
            question_bank: QuestionBank to save

        Returns:
            Path to staging file

        Raises:
            FatalError: If save fails
        """
        staging_file = self.staging_dir / f"{question_bank.module_id}-staging.json"

        try:
            # Convert to dict
            data = question_bank.to_dict()

            # Write to file
            with open(staging_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)

            logger.info(f"Saved staging file: {staging_file}")
            return staging_file

        except Exception as e:
            raise FatalError(
                message=f"Failed to save staging file: {staging_file}",
                module="QuestionGenerator",
                context=str(e),
                action="Check directory permissions and disk space"
            )

    def load_staging_file(self, module_id: str) -> Optional[QuestionBank]:
        """
        Load question bank from staging file.

        Args:
            module_id: Module ID (e.g., "module-0")

        Returns:
            QuestionBank if file exists, None otherwise
        """
        staging_file = self.staging_dir / f"{module_id}-staging.json"

        if not staging_file.exists():
            return None

        try:
            with open(staging_file, 'r', encoding='utf-8') as f:
                data = json.load(f)

            question_bank = QuestionBank.from_dict(data)
            logger.info(f"Loaded staging file: {staging_file}")
            return question_bank

        except Exception as e:
            logger.error(f"Failed to load staging file {staging_file}: {e}")
            return None

    def has_pending_questions(self, module_id: str) -> bool:
        """
        Check if module has pending questions in staging.

        Args:
            module_id: Module ID (e.g., "module-0")

        Returns:
            True if staging file exists with pending questions
        """
        question_bank = self.load_staging_file(module_id)
        if question_bank is None:
            return False

        return question_bank.questions_pending > 0

    def get_staging_status(self, module_id: str) -> Dict[str, Any]:
        """
        Get status of staging questions for a module.

        Args:
            module_id: Module ID (e.g., "module-0")

        Returns:
            Dict with staging status information
        """
        question_bank = self.load_staging_file(module_id)

        if question_bank is None:
            return {
                "exists": False,
                "pending": 0,
                "reviewed": 0,
                "total": 0
            }

        return {
            "exists": True,
            "pending": question_bank.questions_pending,
            "reviewed": question_bank.questions_reviewed,
            "total": len(question_bank.questions),
            "generated_at": question_bank.generated_at.isoformat() if question_bank.generated_at else None,
            "model_used": question_bank.model_used
        }
