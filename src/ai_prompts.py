"""
AI Prompt Templates for Question Generation

This module contains prompt templates for the Claude API to generate
different types of self-study questions based on course content.

Based on PRD Section 12.3
"""

from typing import Dict, Any
from src.models import QuestionType


# System prompt for question generation (PRD Section 12.3)
SYSTEM_PROMPT = """You are an expert instructional designer creating self-study questions for a machine learning course.

Your role is to generate high-quality assessment questions that:
1. Test genuine understanding, not just memorization
2. Are appropriate for beginners (clear language, minimal jargon)
3. Align with stated learning outcomes
4. Include helpful explanations for answers
5. Cover different cognitive levels (recall, understanding, application)

Always output valid JSON matching the specified schema."""


def get_question_generation_prompt(
    course_name: str,
    module_title: str,
    section_title: str,
    section_content: str,
    learning_outcome: str,
    question_count: int,
    question_distribution: Dict[str, int]
) -> str:
    """
    Generate user prompt for question generation.

    Args:
        course_name: Name of the course
        module_title: Title of the module
        section_title: Title of the section being assessed
        section_content: The actual content to generate questions from
        learning_outcome: Associated learning outcome
        question_count: Total number of questions to generate
        question_distribution: Dict mapping question type to count
            e.g., {"multiple_choice": 3, "true_false": 2, "short_answer": 1, "reflection": 1}

    Returns:
        Formatted prompt string
    """
    # Build distribution text
    distribution_lines = []
    for q_type, count in question_distribution.items():
        if count > 0:
            type_name = q_type.replace('_', ' ')
            if q_type == "multiple_choice":
                distribution_lines.append(f"- {count} multiple choice (4 options each)")
            elif q_type == "true_false":
                distribution_lines.append(f"- {count} true/false")
            else:
                distribution_lines.append(f"- {count} {type_name}")

    distribution_text = "\n".join(distribution_lines)

    # Get schema
    schema = get_question_schema()

    prompt = f"""Context:
- Course: {course_name}
- Module: {module_title}
- Section: {section_title}
- Learning Outcome: {learning_outcome}
- Target Audience: Beginner-level engineering students with no prior ML experience

Content to assess:
---
{section_content}
---

Task:
Generate {question_count} questions with the following distribution:
{distribution_text}

Requirements:
1. Each multiple choice question must have plausible distractors
2. Include explanations that teach, not just confirm correctness
3. Vary difficulty: 40% easy, 40% medium, 20% hard
4. Questions should be self-contained (student can answer without re-reading)
5. Avoid trick questions or ambiguous wording

Output format: JSON array of question objects matching this schema:
{schema}"""

    return prompt


def get_question_schema() -> str:
    """
    Get the JSON schema for question objects.

    Returns:
        JSON schema as string
    """
    return """{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "question_text": {
        "type": "string",
        "description": "The question text"
      },
      "type": {
        "type": "string",
        "enum": ["multiple_choice", "true_false", "short_answer", "reflection", "application"],
        "description": "Question type"
      },
      "options": {
        "type": ["array", "null"],
        "items": {"type": "string"},
        "description": "Answer options (for multiple_choice and true_false only)"
      },
      "correct_answer": {
        "type": ["string", "null"],
        "description": "Correct answer (null for reflection questions)"
      },
      "explanation": {
        "type": "string",
        "description": "Explanation of the correct answer or learning point"
      },
      "difficulty": {
        "type": "string",
        "enum": ["easy", "medium", "hard"],
        "description": "Question difficulty level"
      },
      "points": {
        "type": "integer",
        "description": "Point value (1-3)"
      },
      "learning_outcome": {
        "type": "string",
        "description": "Associated learning outcome"
      }
    },
    "required": ["question_text", "type", "explanation", "difficulty", "points"]
  }
}"""


def calculate_question_distribution(
    total_questions: int,
    enabled_types: list
) -> Dict[str, int]:
    """
    Calculate distribution of question types.

    Distribution strategy:
    - 40% multiple choice
    - 20% true/false
    - 20% short answer
    - 10% reflection
    - 10% application

    Args:
        total_questions: Total number of questions to generate
        enabled_types: List of enabled question types

    Returns:
        Dict mapping question type to count
    """
    # Default distribution percentages
    default_distribution = {
        "multiple_choice": 0.40,
        "true_false": 0.20,
        "short_answer": 0.20,
        "reflection": 0.10,
        "application": 0.10
    }

    # Filter to only enabled types
    enabled_distribution = {
        k: v for k, v in default_distribution.items()
        if k in enabled_types
    }

    # Normalize to sum to 1.0
    total_pct = sum(enabled_distribution.values())
    if total_pct > 0:
        enabled_distribution = {
            k: v / total_pct for k, v in enabled_distribution.items()
        }

    # Calculate counts (ensure at least 1 for each enabled type if total > len(enabled))
    distribution = {}
    remaining = total_questions

    # Sort by percentage descending
    sorted_types = sorted(
        enabled_distribution.items(),
        key=lambda x: x[1],
        reverse=True
    )

    for i, (q_type, pct) in enumerate(sorted_types):
        if i == len(sorted_types) - 1:
            # Last type gets remaining
            distribution[q_type] = remaining
        else:
            count = max(1, int(total_questions * pct))
            distribution[q_type] = min(count, remaining - (len(sorted_types) - i - 1))
            remaining -= distribution[q_type]

    return distribution


def get_example_questions_by_type() -> Dict[str, str]:
    """
    Get example questions for each type (for documentation/testing).

    Returns:
        Dict mapping question type to example JSON
    """
    return {
        "multiple_choice": """{
  "question_text": "What is Google Colab?",
  "type": "multiple_choice",
  "options": [
    "A graphics editing tool",
    "A cloud-based Jupyter notebook with free GPU",
    "A Google Meet alternative",
    "A data storage service"
  ],
  "correct_answer": "B",
  "explanation": "Google Colab provides free cloud-based Jupyter notebooks with GPU access, making it ideal for ML learning.",
  "difficulty": "easy",
  "points": 1,
  "learning_outcome": "Understand cloud computing tools for ML"
}""",
        "true_false": """{
  "question_text": "You need to install Python before using Colab.",
  "type": "true_false",
  "options": ["True", "False"],
  "correct_answer": "False",
  "explanation": "Colab runs entirely in the browser with Python pre-installed.",
  "difficulty": "easy",
  "points": 1,
  "learning_outcome": "Understand Colab setup requirements"
}""",
        "short_answer": """{
  "question_text": "Name 3 Python libraries that are pre-installed in Google Colab.",
  "type": "short_answer",
  "options": null,
  "correct_answer": "pandas, numpy, scikit-learn (or matplotlib, tensorflow, etc.)",
  "explanation": "Colab comes with most popular data science libraries pre-installed.",
  "difficulty": "medium",
  "points": 2,
  "learning_outcome": "Recognize common ML libraries"
}""",
        "reflection": """{
  "question_text": "Which of the 5 ML demos (stock predictor, cricket predictor, face detection, sentiment analyzer, chatbot) relates most to your industry or interests? Why?",
  "type": "reflection",
  "options": null,
  "correct_answer": null,
  "explanation": "There is no single correct answer. Reflect on your own context and interests.",
  "difficulty": "easy",
  "points": 2,
  "learning_outcome": "Connect ML concepts to personal context"
}""",
        "application": """{
  "question_text": "You need to train a complex deep learning model on a large dataset. Your laptop has only a CPU. What are three solutions you learned in this module to address this problem?",
  "type": "application",
  "options": null,
  "correct_answer": "1) Use Google Colab with free GPU, 2) Enable GPU runtime in Colab settings, 3) Use cloud computing services like AWS/GCP with GPU instances",
  "explanation": "This module introduced cloud-based solutions for GPU access.",
  "difficulty": "medium",
  "points": 3,
  "learning_outcome": "Apply cloud computing knowledge to solve practical problems"
}"""
    }
