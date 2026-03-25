"""
Question Loader for Student Handout Generator

Loads and validates questions from JSON files in question_banks/approved/ directory.
Implements question placement algorithm to insert questions contextually after sections.

Author: Course Generator Team
Date: 2026-01-11
"""

import json
import logging
from pathlib import Path
from typing import List, Dict, Optional, Tuple

from src.models import (
    Question,
    QuestionBank,
    QuestionType,
    QuestionStatus,
    QuestionDifficulty,
    QuestionSource,
    ContentSection
)

logger = logging.getLogger(__name__)


class QuestionLoader:
    """
    Loads and validates questions from JSON question banks.

    Responsibilities:
    - Load questions from JSON files in question_banks/approved/
    - Validate question schema against Question dataclass
    - Support all 5 question types (multiple_choice, true_false, short_answer, reflection, application)
    - Filter questions by status (only use "approved" questions)
    - Handle missing/invalid question banks gracefully

    Usage:
        loader = QuestionLoader(question_banks_dir="./question_banks/approved")
        questions = loader.load_questions("module-0")
        if questions:
            placed = loader.place_questions(questions, sections)
    """

    def __init__(self, question_banks_dir: str = "question_banks/approved"):
        """
        Initialize QuestionLoader.

        Args:
            question_banks_dir: Path to directory containing approved question banks
        """
        self.question_banks_dir = Path(question_banks_dir)
        if not self.question_banks_dir.exists():
            logger.warning(f"Question banks directory not found: {self.question_banks_dir}")
            self.question_banks_dir.mkdir(parents=True, exist_ok=True)

    def load_questions(self, module_id: str) -> List[Question]:
        """
        Load questions from JSON file for a specific module.

        Args:
            module_id: Module identifier (e.g., "module-0")

        Returns:
            List of approved Question objects, or empty list if none found

        Error Handling:
            - File not found → log warning, return empty list
            - Invalid JSON → log error, return empty list
            - Missing required fields → log warning, skip question
            - Invalid question type → log warning, skip question
        """
        question_file = self.question_banks_dir / f"{module_id}.json"

        if not question_file.exists():
            logger.warning(f"Question bank not found for {module_id}: {question_file}")
            return []

        try:
            with open(question_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON in question bank {question_file}: {e}")
            return []
        except Exception as e:
            logger.error(f"Error reading question bank {question_file}: {e}")
            return []

        # Parse question bank
        try:
            question_bank = QuestionBank.from_dict(data)
        except Exception as e:
            logger.error(f"Error parsing question bank {question_file}: {e}")
            return []

        # Filter for approved questions only
        approved_questions = question_bank.get_approved_questions()

        if not approved_questions:
            logger.info(f"No approved questions found in {module_id}")
            return []

        # Validate each question
        valid_questions = []
        for question in approved_questions:
            if self._validate_question(question):
                valid_questions.append(question)
            else:
                logger.warning(f"Skipping invalid question {question.id} in {module_id}")

        logger.info(f"Loaded {len(valid_questions)} approved questions for {module_id}")
        return valid_questions

    def _validate_question(self, question: Question) -> bool:
        """
        Validate question has all required fields for its type.

        Args:
            question: Question to validate

        Returns:
            True if valid, False otherwise
        """
        # Check required base fields
        if not question.id or not question.question_text:
            logger.warning(f"Question {question.id} missing required fields (id or question_text)")
            return False

        # Type-specific validation
        if question.type == QuestionType.MULTIPLE_CHOICE:
            if not question.options or len(question.options) != 4:
                logger.warning(f"Multiple choice question {question.id} must have exactly 4 options")
                return False
            if not question.correct_answer:
                logger.warning(f"Multiple choice question {question.id} missing correct_answer")
                return False

        elif question.type == QuestionType.TRUE_FALSE:
            if not question.options or set(question.options) != {"True", "False"}:
                logger.warning(f"True/False question {question.id} must have options ['True', 'False']")
                return False
            if not question.correct_answer or question.correct_answer not in ["True", "False"]:
                logger.warning(f"True/False question {question.id} has invalid correct_answer")
                return False

        elif question.type == QuestionType.SHORT_ANSWER:
            # Short answer should have a reference answer
            if not question.correct_answer:
                logger.warning(f"Short answer question {question.id} missing reference answer")
                # Not fatal, continue with warning

        elif question.type == QuestionType.REFLECTION:
            # Reflection questions don't need correct_answer
            if question.correct_answer:
                logger.debug(f"Reflection question {question.id} has correct_answer (will be ignored)")

        elif question.type == QuestionType.APPLICATION:
            # Application questions should have a correct_answer as reference
            if not question.correct_answer:
                logger.warning(f"Application question {question.id} missing reference answer")
                # Not fatal, continue with warning

        else:
            logger.warning(f"Unknown question type: {question.type}")
            return False

        return True

    def place_questions(
        self,
        questions: List[Question],
        sections: List[ContentSection],
        target_frequency: int = 175
    ) -> Dict[str, List[Question]]:
        """
        Place questions contextually after major sections.

        Question Placement Logic:
        - Analyze ContentSection hierarchy from FrameworkParser
        - Identify major sections (level 2 headers / H2)
        - Insert question groups after section content
        - Maintain frequency: ~1 question per 150-200 lines of content (default: 175)
        - Group questions in "Self-Study Check" boxes (3-5 questions per box)

        Args:
            questions: List of questions to place
            sections: List of ContentSection objects from parser
            target_frequency: Target lines of content per question (default: 175)

        Returns:
            Dictionary mapping section_id to list of questions for that section

        Example:
            {
                "session-1-demos": [Question(...), Question(...)],
                "session-2-setup": [Question(...), Question(...), Question(...)]
            }
        """
        if not questions:
            logger.info("No questions to place")
            return {}

        # Find major sections (level 2 headers)
        major_sections = self._get_major_sections(sections)

        if not major_sections:
            logger.warning("No major sections found for question placement")
            return {}

        # Calculate content length for each section
        section_lengths = {}
        for section in major_sections:
            length = self._calculate_section_length(section)
            section_lengths[section.id] = length

        # Group questions by source_section if available
        questions_by_section = self._group_questions_by_section(questions)

        # Distribute remaining questions based on content length
        placement_map = {}

        # First, place questions that have explicit source_section
        for section in major_sections:
            if section.id in questions_by_section:
                placement_map[section.id] = questions_by_section[section.id]
                logger.debug(f"Placed {len(questions_by_section[section.id])} questions in {section.id} (source match)")

        # Then distribute remaining questions based on content length
        unplaced_questions = []
        for q in questions:
            placed = False
            for section_id, section_questions in placement_map.items():
                if q in section_questions:
                    placed = True
                    break
            if not placed:
                unplaced_questions.append(q)

        if unplaced_questions:
            logger.info(f"Distributing {len(unplaced_questions)} unplaced questions")
            self._distribute_questions(
                unplaced_questions,
                major_sections,
                section_lengths,
                placement_map,
                target_frequency
            )

        # Log placement summary
        total_placed = sum(len(qs) for qs in placement_map.values())
        logger.info(f"Placed {total_placed} questions across {len(placement_map)} sections")

        return placement_map

    def _get_major_sections(self, sections: List[ContentSection]) -> List[ContentSection]:
        """
        Extract major sections (level 2 headers) from section hierarchy.

        Args:
            sections: List of ContentSection objects

        Returns:
            List of major sections (level 2 headers)
        """
        major_sections = []

        for section in sections:
            if section.level == 2 and section.include_in_handout:
                major_sections.append(section)
            # Recursively check subsections
            if section.subsections:
                major_sections.extend(self._get_major_sections(section.subsections))

        return major_sections

    def _calculate_section_length(self, section: ContentSection) -> int:
        """
        Calculate total content length (in lines) for a section and its subsections.

        Args:
            section: ContentSection to measure

        Returns:
            Approximate number of lines in section
        """
        # Approximate lines: count newlines + rough estimate
        lines = section.content.count('\n') + 1

        # Add subsection lengths
        for subsection in section.subsections:
            lines += self._calculate_section_length(subsection)

        return lines

    def _group_questions_by_section(self, questions: List[Question]) -> Dict[str, List[Question]]:
        """
        Group questions by their source_section field.

        Args:
            questions: List of questions

        Returns:
            Dictionary mapping section_id to questions
        """
        grouped = {}
        for question in questions:
            if question.source_section:
                if question.source_section not in grouped:
                    grouped[question.source_section] = []
                grouped[question.source_section].append(question)

        return grouped

    def _distribute_questions(
        self,
        questions: List[Question],
        sections: List[ContentSection],
        section_lengths: Dict[str, int],
        placement_map: Dict[str, List[Question]],
        target_frequency: int
    ) -> None:
        """
        Distribute unplaced questions across sections based on content length.

        Args:
            questions: Questions to distribute
            sections: Major sections
            section_lengths: Map of section_id to content length
            placement_map: Map to update with placements (modified in place)
            target_frequency: Target lines per question
        """
        if not questions or not sections:
            return

        # Calculate how many questions each section should get based on length
        total_length = sum(section_lengths.values())

        if total_length == 0:
            # Equal distribution if no content length
            questions_per_section = len(questions) // len(sections)
            remaining = len(questions) % len(sections)

            idx = 0
            for i, section in enumerate(sections):
                count = questions_per_section + (1 if i < remaining else 0)
                if count > 0:
                    if section.id not in placement_map:
                        placement_map[section.id] = []
                    placement_map[section.id].extend(questions[idx:idx + count])
                    idx += count
        else:
            # Proportional distribution based on content length
            questions_allocated = 0

            for section in sections:
                # Calculate proportion
                proportion = section_lengths[section.id] / total_length
                count = int(len(questions) * proportion)

                if count > 0:
                    if section.id not in placement_map:
                        placement_map[section.id] = []

                    end_idx = min(questions_allocated + count, len(questions))
                    placement_map[section.id].extend(questions[questions_allocated:end_idx])
                    questions_allocated = end_idx

            # Place any remaining questions in the last section
            if questions_allocated < len(questions):
                last_section = sections[-1]
                if last_section.id not in placement_map:
                    placement_map[last_section.id] = []
                placement_map[last_section.id].extend(questions[questions_allocated:])

    def create_question_boxes(
        self,
        questions: List[Question],
        box_size_range: Tuple[int, int] = (3, 5)
    ) -> List[List[Question]]:
        """
        Group questions into "Self-Study Check" boxes for layout.

        Args:
            questions: Questions to group
            box_size_range: Tuple of (min, max) questions per box

        Returns:
            List of question groups (each group becomes one box)
        """
        if not questions:
            return []

        min_size, max_size = box_size_range
        boxes = []
        current_box = []

        for question in questions:
            current_box.append(question)

            # Create box when we reach max size or it's the last question
            if len(current_box) >= max_size or question == questions[-1]:
                # Don't create box if too small (unless it's the last one)
                if len(current_box) >= min_size or question == questions[-1]:
                    boxes.append(current_box)
                    current_box = []

        # Handle remaining questions
        if current_box:
            if boxes and len(current_box) < min_size:
                # Merge with last box if too small
                boxes[-1].extend(current_box)
            else:
                boxes.append(current_box)

        logger.debug(f"Created {len(boxes)} question boxes from {len(questions)} questions")
        return boxes

    def get_question_stats(self, questions: List[Question]) -> Dict[str, any]:
        """
        Get statistics about a list of questions.

        Args:
            questions: List of questions to analyze

        Returns:
            Dictionary with statistics (total, by_type, by_difficulty, by_source)
        """
        stats = {
            "total": len(questions),
            "by_type": {},
            "by_difficulty": {},
            "by_source": {},
            "by_status": {}
        }

        for q in questions:
            # Count by type
            type_name = q.type.value
            stats["by_type"][type_name] = stats["by_type"].get(type_name, 0) + 1

            # Count by difficulty
            difficulty = q.difficulty.value
            stats["by_difficulty"][difficulty] = stats["by_difficulty"].get(difficulty, 0) + 1

            # Count by source
            source = q.source.value
            stats["by_source"][source] = stats["by_source"].get(source, 0) + 1

            # Count by status
            status = q.status.value
            stats["by_status"][status] = stats["by_status"].get(status, 0) + 1

        return stats


def load_module_questions(module_id: str, question_banks_dir: str = "question_banks/approved") -> List[Question]:
    """
    Convenience function to load questions for a module.

    Args:
        module_id: Module identifier (e.g., "module-0")
        question_banks_dir: Path to question banks directory

    Returns:
        List of approved questions

    Example:
        questions = load_module_questions("module-0")
        if questions:
            print(f"Loaded {len(questions)} questions")
    """
    loader = QuestionLoader(question_banks_dir)
    return loader.load_questions(module_id)
