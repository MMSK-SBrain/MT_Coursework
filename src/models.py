"""
Data Models for Student Handout Generator

All data models as dataclasses with type hints from PRD Sections 10.1-10.6
"""

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import Any, Dict, List, Optional


class QuestionType(Enum):
    """Question type enumeration."""
    MULTIPLE_CHOICE = "multiple_choice"
    TRUE_FALSE = "true_false"
    SHORT_ANSWER = "short_answer"
    REFLECTION = "reflection"
    APPLICATION = "application"


class QuestionStatus(Enum):
    """Question review status."""
    PENDING_REVIEW = "pending_review"
    APPROVED = "approved"
    REJECTED = "rejected"


class QuestionDifficulty(Enum):
    """Question difficulty level."""
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"


class QuestionSource(Enum):
    """Question source."""
    AI_GENERATED = "ai_generated"
    MANUAL = "manual"


@dataclass
class FrameworkMetadata:
    """Metadata extracted from framework markdown file (PRD Section 10.1)"""
    course_code: str
    module_number: int
    module_title: str
    duration: Optional[str] = None
    video_content: Optional[str] = None
    hands_on_time: Optional[str] = None
    theory_practice_ratio: Optional[str] = None
    file_path: Optional[Path] = None
    last_updated: Optional[datetime] = None
    version: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return {
            "course_code": self.course_code,
            "module_number": self.module_number,
            "module_title": self.module_title,
            "duration": self.duration,
            "video_content": self.video_content,
            "hands_on_time": self.hands_on_time,
            "theory_practice_ratio": self.theory_practice_ratio,
            "file_path": str(self.file_path),
            "last_updated": self.last_updated.isoformat(),
            "version": self.version
        }


@dataclass
class ContentSection:
    """A section of content from the framework (PRD Section 10.2)"""
    id: str
    level: int
    title: str
    content: str
    subsections: List['ContentSection'] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)
    include_in_handout: bool = True
    question_count: int = 0

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "level": self.level,
            "title": self.title,
            "content": self.content,
            "subsections": [s.to_dict() for s in self.subsections],
            "metadata": self.metadata,
            "include_in_handout": self.include_in_handout,
            "question_count": self.question_count
        }


@dataclass
class Question:
    """A self-study question (PRD Section 10.3)"""
    id: str
    type: QuestionType
    question_text: str
    options: Optional[List[str]] = None
    correct_answer: Optional[str] = None
    explanation: Optional[str] = None
    points: int = 1
    difficulty: QuestionDifficulty = QuestionDifficulty.EASY
    learning_outcome: Optional[str] = None
    source_section: str = ""
    source: QuestionSource = QuestionSource.AI_GENERATED
    status: QuestionStatus = QuestionStatus.PENDING_REVIEW
    reviewed_at: Optional[datetime] = None
    reviewer_notes: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "type": self.type.value,
            "question_text": self.question_text,
            "options": self.options,
            "correct_answer": self.correct_answer,
            "explanation": self.explanation,
            "points": self.points,
            "difficulty": self.difficulty.value,
            "learning_outcome": self.learning_outcome,
            "source_section": self.source_section,
            "source": self.source.value,
            "status": self.status.value,
            "reviewed_at": self.reviewed_at.isoformat() if self.reviewed_at else None,
            "reviewer_notes": self.reviewer_notes
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Question':
        return cls(
            id=data["id"],
            type=QuestionType(data["type"]),
            question_text=data["question_text"],
            options=data.get("options"),
            correct_answer=data.get("correct_answer"),
            explanation=data.get("explanation"),
            points=data.get("points", 1),
            difficulty=QuestionDifficulty(data.get("difficulty", "easy")),
            learning_outcome=data.get("learning_outcome"),
            source_section=data.get("source_section", ""),
            source=QuestionSource(data.get("source", "ai_generated")),
            status=QuestionStatus(data.get("status", "pending_review")),
            reviewed_at=datetime.fromisoformat(data["reviewed_at"]) if data.get("reviewed_at") else None,
            reviewer_notes=data.get("reviewer_notes")
        )

    def get_border_color(self) -> str:
        """Get border color for question type (dark theme)"""
        color_map = {
            QuestionType.MULTIPLE_CHOICE: "#58A6FF",
            QuestionType.TRUE_FALSE: "#58A6FF",
            QuestionType.SHORT_ANSWER: "#3FB950",
            QuestionType.REFLECTION: "#A371F7",
            QuestionType.APPLICATION: "#3FB950"
        }
        return color_map.get(self.type, "#58A6FF")


@dataclass
class ImageReference:
    """Reference to an image in the handout (PRD Section 10.4)"""
    id: str
    original_path: str
    resolved_path: Optional[Path] = None
    alt_text: str = ""
    caption: Optional[str] = None
    width: int = 500
    height: int = 0
    exists: bool = False
    placeholder_used: bool = False

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "original_path": self.original_path,
            "resolved_path": str(self.resolved_path) if self.resolved_path else None,
            "alt_text": self.alt_text,
            "caption": self.caption,
            "width": self.width,
            "height": self.height,
            "exists": self.exists,
            "placeholder_used": self.placeholder_used
        }


@dataclass
class TOCEntry:
    """Table of contents entry"""
    level: int
    title: str
    page_number: int
    anchor: str


@dataclass
class HandoutDocument:
    """Complete handout document (PRD Section 10.5)"""
    metadata: FrameworkMetadata
    sections: List[ContentSection]
    questions: List[Question]
    images: List[ImageReference]
    toc: List[TOCEntry] = field(default_factory=list)
    generation_timestamp: datetime = field(default_factory=datetime.now)
    config_used: Dict[str, Any] = field(default_factory=dict)
    output_path: Optional[Path] = None
    warnings: List[str] = field(default_factory=list)
    question_review_complete: bool = False

    def to_dict(self) -> Dict[str, Any]:
        return {
            "metadata": self.metadata.to_dict(),
            "sections": [s.to_dict() for s in self.sections],
            "questions": [q.to_dict() for q in self.questions],
            "images": [img.to_dict() for img in self.images],
            "toc": [{"level": e.level, "title": e.title, "page_number": e.page_number, "anchor": e.anchor} for e in self.toc],
            "generation_timestamp": self.generation_timestamp.isoformat(),
            "config_used": self.config_used,
            "output_path": str(self.output_path) if self.output_path else None,
            "warnings": self.warnings,
            "question_review_complete": self.question_review_complete
        }

    def add_warning(self, warning: str) -> None:
        self.warnings.append(warning)

    def get_question_stats(self) -> Dict[str, int]:
        stats = {"total": len(self.questions), "by_type": {}, "by_difficulty": {}, "by_status": {}}
        for q in self.questions:
            stats["by_type"][q.type.value] = stats["by_type"].get(q.type.value, 0) + 1
            stats["by_difficulty"][q.difficulty.value] = stats["by_difficulty"].get(q.difficulty.value, 0) + 1
            stats["by_status"][q.status.value] = stats["by_status"].get(q.status.value, 0) + 1
        return stats


@dataclass
class ReviewSession:
    """Question review session tracking (PRD Section 10.6)"""
    module_id: str
    started_at: datetime
    completed_at: Optional[datetime] = None
    questions_total: int = 0
    questions_approved: int = 0
    questions_edited: int = 0
    questions_rejected: int = 0
    questions_skipped: int = 0

    def to_dict(self) -> Dict[str, Any]:
        return {
            "module_id": self.module_id,
            "started_at": self.started_at.isoformat(),
            "completed_at": self.completed_at.isoformat() if self.completed_at else None,
            "questions_total": self.questions_total,
            "questions_approved": self.questions_approved,
            "questions_edited": self.questions_edited,
            "questions_rejected": self.questions_rejected,
            "questions_skipped": self.questions_skipped
        }

    def mark_complete(self) -> None:
        self.completed_at = datetime.now()

    def get_completion_percentage(self) -> float:
        reviewed = self.questions_approved + self.questions_edited + self.questions_rejected
        return (reviewed / self.questions_total * 100) if self.questions_total > 0 else 0.0

    def get_summary(self) -> str:
        return (f"Reviewed {self.questions_total} questions: {self.questions_approved} approved, "
                f"{self.questions_edited} edited, {self.questions_rejected} rejected, {self.questions_skipped} skipped")


@dataclass
class BatchResult:
    """Result from batch processing a single module"""
    module_id: str
    success: bool
    output_path: Optional[Path] = None
    error: Optional[str] = None
    blocked_by_review: bool = False
    processing_time_seconds: float = 0.0
    warnings: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "module_id": self.module_id,
            "success": self.success,
            "output_path": str(self.output_path) if self.output_path else None,
            "error": self.error,
            "blocked_by_review": self.blocked_by_review,
            "processing_time_seconds": self.processing_time_seconds,
            "warnings": self.warnings
        }


@dataclass
class QuestionBank:
    """Question bank for a module"""
    module_id: str
    module_title: str
    version: str
    last_reviewed: Optional[datetime] = None
    questions: List[Question] = field(default_factory=list)
    generated_at: Optional[datetime] = None
    model_used: Optional[str] = None
    questions_pending: int = 0
    questions_reviewed: int = 0

    def to_dict(self) -> Dict[str, Any]:
        return {
            "module_id": self.module_id,
            "module_title": self.module_title,
            "version": self.version,
            "last_reviewed": self.last_reviewed.isoformat() if self.last_reviewed else None,
            "questions": [q.to_dict() for q in self.questions],
            "generated_at": self.generated_at.isoformat() if self.generated_at else None,
            "model_used": self.model_used,
            "questions_pending": self.questions_pending,
            "questions_reviewed": self.questions_reviewed
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'QuestionBank':
        return cls(
            module_id=data["module_id"],
            module_title=data["module_title"],
            version=data["version"],
            last_reviewed=datetime.fromisoformat(data["last_reviewed"]) if data.get("last_reviewed") else None,
            questions=[Question.from_dict(q) for q in data.get("questions", [])],
            generated_at=datetime.fromisoformat(data["generated_at"]) if data.get("generated_at") else None,
            model_used=data.get("model_used"),
            questions_pending=data.get("questions_pending", 0),
            questions_reviewed=data.get("questions_reviewed", 0)
        )

    def add_question(self, question: Question) -> None:
        self.questions.append(question)
        if question.status == QuestionStatus.PENDING_REVIEW:
            self.questions_pending += 1
        else:
            self.questions_reviewed += 1

    def get_pending_questions(self) -> List[Question]:
        return [q for q in self.questions if q.status == QuestionStatus.PENDING_REVIEW]

    def get_approved_questions(self) -> List[Question]:
        return [q for q in self.questions if q.status == QuestionStatus.APPROVED]

    def get_rejected_questions(self) -> List[Question]:
        return [q for q in self.questions if q.status == QuestionStatus.REJECTED]


@dataclass
class ParseResult:
    """
    Result of parsing a framework file.

    Contains the parsed metadata and sections, along with any errors
    or warnings encountered during parsing.
    """
    metadata: Optional[FrameworkMetadata] = None
    sections: List[ContentSection] = field(default_factory=list)
    images: List[ImageReference] = field(default_factory=list)
    errors: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    success: bool = False
