"""
Question Reviewer for Student Handout Generator

Interactive terminal interface for reviewing AI-generated questions before approval.
Uses the rich library for beautiful terminal UI.

Author: Course Generator Team
Date: 2026-01-11
"""

import json
import logging
from datetime import datetime
from pathlib import Path
from typing import List, Optional, Dict, Any

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, Confirm
from rich.table import Table
from rich import box
from rich.text import Text

from src.models import (
    Question,
    QuestionBank,
    QuestionType,
    QuestionStatus,
    QuestionDifficulty,
    QuestionSource,
    ReviewSession
)

logger = logging.getLogger(__name__)
console = Console()


class QuestionReviewer:
    """
    Interactive terminal interface for reviewing AI-generated questions.

    Responsibilities:
    - Load questions from staging files: question_banks/staging/{module_id}-staging.json
    - Display questions in interactive terminal UI (rich library)
    - Support review actions: [A]pprove, [E]dit, [R]eject, [S]kip, [Q]uit
    - Allow editing of question text, options, correct answer
    - Save approved questions to question_banks/approved/{module_id}.json
    - Save rejected questions to question_banks/rejected/{module_id}-rejected.json
    - Track review statistics (approved, edited, rejected, skipped)
    - Support resuming interrupted sessions (skipped questions remain pending)
    - Generate summary report after review

    Usage:
        reviewer = QuestionReviewer(
            staging_dir="question_banks/staging",
            approved_dir="question_banks/approved",
            rejected_dir="question_banks/rejected"
        )
        session = reviewer.start_session("module-0")
    """

    def __init__(
        self,
        staging_dir: str = "question_banks/staging",
        approved_dir: str = "question_banks/approved",
        rejected_dir: str = "question_banks/rejected"
    ):
        """
        Initialize QuestionReviewer.

        Args:
            staging_dir: Directory containing staging question files
            approved_dir: Directory for approved questions
            rejected_dir: Directory for rejected questions
        """
        self.staging_dir = Path(staging_dir)
        self.approved_dir = Path(approved_dir)
        self.rejected_dir = Path(rejected_dir)

        # Ensure directories exist
        self.staging_dir.mkdir(parents=True, exist_ok=True)
        self.approved_dir.mkdir(parents=True, exist_ok=True)
        self.rejected_dir.mkdir(parents=True, exist_ok=True)

    def start_session(self, module_id: str) -> ReviewSession:
        """
        Start an interactive review session for a module.

        Args:
            module_id: Module identifier (e.g., "module-0")

        Returns:
            ReviewSession with statistics

        Error Handling:
            - Staging file not found → log error, return empty session
            - Invalid JSON → log error, return empty session
            - No pending questions → log info, return completed session
        """
        # Load staging questions
        staging_file = self.staging_dir / f"{module_id}-staging.json"

        if not staging_file.exists():
            console.print(f"[red]Error:[/red] Staging file not found: {staging_file}")
            logger.error(f"Staging file not found: {staging_file}")
            return ReviewSession(
                module_id=module_id,
                started_at=datetime.now(),
                completed_at=datetime.now()
            )

        try:
            with open(staging_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            question_bank = QuestionBank.from_dict(data)
        except json.JSONDecodeError as e:
            console.print(f"[red]Error:[/red] Invalid JSON in staging file: {e}")
            logger.error(f"Invalid JSON in {staging_file}: {e}")
            return ReviewSession(
                module_id=module_id,
                started_at=datetime.now(),
                completed_at=datetime.now()
            )
        except Exception as e:
            console.print(f"[red]Error:[/red] Failed to load staging file: {e}")
            logger.error(f"Error loading {staging_file}: {e}")
            return ReviewSession(
                module_id=module_id,
                started_at=datetime.now(),
                completed_at=datetime.now()
            )

        # Filter pending questions
        pending_questions = question_bank.get_pending_questions()

        if not pending_questions:
            console.print(f"[green]✓[/green] No pending questions for {module_id}")
            logger.info(f"No pending questions for {module_id}")
            return ReviewSession(
                module_id=module_id,
                started_at=datetime.now(),
                completed_at=datetime.now()
            )

        # Initialize session
        session = ReviewSession(
            module_id=module_id,
            started_at=datetime.now(),
            questions_total=len(pending_questions)
        )

        # Start interactive review
        console.clear()
        self._display_welcome(question_bank, len(pending_questions))

        # Review each question
        for i, question in enumerate(pending_questions):
            action = self._review_question(
                question,
                i + 1,
                len(pending_questions),
                question_bank
            )

            if action == "approve":
                session.questions_approved += 1
                question.status = QuestionStatus.APPROVED
                question.reviewed_at = datetime.now()
            elif action == "edit":
                session.questions_edited += 1
                question.status = QuestionStatus.APPROVED
                question.reviewed_at = datetime.now()
            elif action == "reject":
                session.questions_rejected += 1
                question.status = QuestionStatus.REJECTED
                question.reviewed_at = datetime.now()
            elif action == "skip":
                session.questions_skipped += 1
                # Keep status as pending_review
            elif action == "quit":
                session.questions_skipped += len(pending_questions) - i - 1
                break

        # Mark session complete
        session.mark_complete()

        # Save results
        self._save_results(question_bank, session)

        # Display summary
        self._display_summary(session, question_bank)

        return session

    def _display_welcome(self, question_bank: QuestionBank, pending_count: int) -> None:
        """Display welcome banner."""
        panel = Panel(
            f"[bold]Question Review: {question_bank.module_title}[/bold]\n"
            f"Pending Questions: {pending_count}",
            border_style="blue",
            box=box.ROUNDED
        )
        console.print(panel)
        console.print()

    def _review_question(
        self,
        question: Question,
        current: int,
        total: int,
        question_bank: QuestionBank
    ) -> str:
        """
        Review a single question interactively.

        Args:
            question: Question to review
            current: Current question number (1-indexed)
            total: Total number of questions
            question_bank: QuestionBank containing this question

        Returns:
            Action taken: "approve", "edit", "reject", "skip", "quit"
        """
        # Display header
        console.rule(f"[bold blue]Question {current} of {total}[/bold blue]", style="blue")
        console.print()

        # Display question details
        self._display_question(question)

        # Get user action
        while True:
            console.print()
            choice = Prompt.ask(
                "[bold]Your choice[/bold]",
                choices=["A", "E", "R", "S", "Q", "a", "e", "r", "s", "q"],
                default="A"
            ).upper()

            if choice == "A":
                console.print("[green]✓ Question approved[/green]")
                return "approve"

            elif choice == "E":
                self._edit_question(question)
                console.print("[green]✓ Question updated and approved[/green]")
                return "edit"

            elif choice == "R":
                reason = Prompt.ask(
                    "[yellow]Rejection reason[/yellow] (optional)",
                    default=""
                )
                if reason:
                    question.reviewer_notes = f"REJECTED: {reason}"
                console.print("[red]✗ Question rejected[/red]")
                return "reject"

            elif choice == "S":
                console.print("[yellow]⏭ Question skipped[/yellow]")
                return "skip"

            elif choice == "Q":
                if Confirm.ask("[yellow]Quit review session?[/yellow]", default=False):
                    console.print("[yellow]Session saved. You can resume later.[/yellow]")
                    return "quit"
                # Continue if user cancels quit

    def _display_question(self, question: Question) -> None:
        """Display question details in formatted panel."""
        # Build question content
        content_lines = []

        # Question text
        content_lines.append(f"[bold white]{question.question_text}[/bold white]")
        content_lines.append("")

        # Options (if applicable)
        if question.options:
            for i, option in enumerate(question.options):
                label = chr(65 + i) if question.type == QuestionType.MULTIPLE_CHOICE else option
                content_lines.append(f"  {label}) {option}")
            content_lines.append("")

        # Metadata
        if question.correct_answer:
            content_lines.append(f"[cyan]Suggested Answer:[/cyan] {question.correct_answer}")
        content_lines.append(f"[cyan]Difficulty:[/cyan] {question.difficulty.value}")
        content_lines.append(f"[cyan]Points:[/cyan] {question.points}")

        # Separator
        content_lines.append("")
        content_lines.append("─" * 60)

        # Context
        if question.source_section:
            content_lines.append(f"[dim]Source Section:[/dim] {question.source_section}")
        if question.learning_outcome:
            content_lines.append(f"[dim]Learning Outcome:[/dim] {question.learning_outcome}")

        content_lines.append("─" * 60)
        content_lines.append("")

        # Action buttons
        content_lines.append("[green][A][/green] Approve    [cyan][E][/cyan] Edit    "
                           "[red][R][/red] Reject    [yellow][S][/yellow] Skip    "
                           "[dim][Q][/dim] Quit")

        # Create panel with type-specific color
        border_color = self._get_border_color_name(question.type)
        type_label = question.type.value.replace("_", " ").title()

        panel = Panel(
            "\n".join(content_lines),
            title=f"[{border_color}]{type_label}[/{border_color}]",
            border_style=border_color,
            box=box.ROUNDED
        )
        console.print(panel)

    def _get_border_color_name(self, question_type: QuestionType) -> str:
        """Get rich color name for question type border."""
        color_map = {
            QuestionType.MULTIPLE_CHOICE: "blue",
            QuestionType.TRUE_FALSE: "blue",
            QuestionType.SHORT_ANSWER: "green",
            QuestionType.REFLECTION: "magenta",
            QuestionType.APPLICATION: "green"
        }
        return color_map.get(question_type, "blue")

    def _edit_question(self, question: Question) -> None:
        """
        Interactive editing workflow for a question.

        Allows editing:
        - Question text
        - Options (for MCQ/T-F)
        - Correct answer
        - Reviewer notes
        """
        console.print()
        console.print("[bold cyan]Edit Question[/bold cyan]")
        console.print()

        # Edit question text
        new_text = Prompt.ask(
            "[cyan]Question text[/cyan] (or press Enter to keep)",
            default=""
        )
        if new_text.strip():
            question.question_text = new_text.strip()

        # Edit options (if applicable)
        if question.options:
            console.print()
            console.print(f"[dim]Current options: {', '.join(question.options)}[/dim]")
            new_options = Prompt.ask(
                "[cyan]Edit options[/cyan] (comma-separated, or Enter to keep)",
                default=""
            )
            if new_options.strip():
                question.options = [opt.strip() for opt in new_options.split(",")]

        # Edit correct answer
        if question.type in [QuestionType.MULTIPLE_CHOICE, QuestionType.TRUE_FALSE,
                            QuestionType.SHORT_ANSWER, QuestionType.APPLICATION]:
            console.print()
            current_answer = question.correct_answer or "(none)"
            new_answer = Prompt.ask(
                f"[cyan]Correct answer[/cyan] (current: {current_answer}, or Enter to keep)",
                default=""
            )
            if new_answer.strip():
                question.correct_answer = new_answer.strip()

        # Add reviewer notes
        console.print()
        notes = Prompt.ask(
            "[cyan]Review notes[/cyan] (optional)",
            default=""
        )
        if notes.strip():
            question.reviewer_notes = notes.strip()

    def _save_results(self, question_bank: QuestionBank, session: ReviewSession) -> None:
        """
        Save approved and rejected questions to appropriate files.

        Args:
            question_bank: QuestionBank with updated question statuses
            session: ReviewSession with statistics
        """
        module_id = question_bank.module_id

        # Get questions by status
        approved = question_bank.get_approved_questions()
        rejected = question_bank.get_rejected_questions()
        pending = question_bank.get_pending_questions()

        # Save approved questions
        if approved:
            approved_file = self.approved_dir / f"{module_id}.json"
            approved_bank = QuestionBank(
                module_id=module_id,
                module_title=question_bank.module_title,
                version=question_bank.version,
                last_reviewed=datetime.now(),
                questions=approved
            )

            # Merge with existing approved questions if file exists
            if approved_file.exists():
                try:
                    with open(approved_file, 'r', encoding='utf-8') as f:
                        existing_data = json.load(f)
                    existing_bank = QuestionBank.from_dict(existing_data)

                    # Merge questions (avoid duplicates by ID)
                    existing_ids = {q.id for q in existing_bank.questions}
                    for q in approved:
                        if q.id not in existing_ids:
                            existing_bank.add_question(q)
                        else:
                            # Update existing question
                            idx = next(i for i, eq in enumerate(existing_bank.questions) if eq.id == q.id)
                            existing_bank.questions[idx] = q

                    existing_bank.last_reviewed = datetime.now()
                    approved_bank = existing_bank
                except Exception as e:
                    logger.warning(f"Could not merge with existing approved file: {e}")

            with open(approved_file, 'w', encoding='utf-8') as f:
                json.dump(approved_bank.to_dict(), f, indent=2, ensure_ascii=False)

            logger.info(f"Saved {len(approved)} approved questions to {approved_file}")

        # Save rejected questions
        if rejected:
            rejected_file = self.rejected_dir / f"{module_id}-rejected.json"
            rejected_bank = QuestionBank(
                module_id=module_id,
                module_title=question_bank.module_title,
                version=question_bank.version,
                last_reviewed=datetime.now(),
                questions=rejected
            )

            # Append to existing rejected questions if file exists
            if rejected_file.exists():
                try:
                    with open(rejected_file, 'r', encoding='utf-8') as f:
                        existing_data = json.load(f)
                    existing_bank = QuestionBank.from_dict(existing_data)

                    # Add new rejected questions
                    existing_ids = {q.id for q in existing_bank.questions}
                    for q in rejected:
                        if q.id not in existing_ids:
                            existing_bank.add_question(q)

                    existing_bank.last_reviewed = datetime.now()
                    rejected_bank = existing_bank
                except Exception as e:
                    logger.warning(f"Could not merge with existing rejected file: {e}")

            with open(rejected_file, 'w', encoding='utf-8') as f:
                json.dump(rejected_bank.to_dict(), f, indent=2, ensure_ascii=False)

            logger.info(f"Saved {len(rejected)} rejected questions to {rejected_file}")

        # Update staging file (remove approved/rejected, keep pending)
        if pending:
            staging_file = self.staging_dir / f"{module_id}-staging.json"
            pending_bank = QuestionBank(
                module_id=module_id,
                module_title=question_bank.module_title,
                version=question_bank.version,
                generated_at=question_bank.generated_at,
                model_used=question_bank.model_used,
                questions=pending,
                questions_pending=len(pending)
            )

            with open(staging_file, 'w', encoding='utf-8') as f:
                json.dump(pending_bank.to_dict(), f, indent=2, ensure_ascii=False)

            logger.info(f"Updated staging file with {len(pending)} pending questions")
        else:
            # No pending questions - remove staging file
            staging_file = self.staging_dir / f"{module_id}-staging.json"
            if staging_file.exists():
                staging_file.unlink()
                logger.info(f"Removed staging file (all questions reviewed)")

    def _display_summary(self, session: ReviewSession, question_bank: QuestionBank) -> None:
        """Display review session summary."""
        console.print()
        console.rule("[bold green]Review Session Complete[/bold green]", style="green")
        console.print()

        # Calculate duration
        duration = session.completed_at - session.started_at if session.completed_at else None
        duration_str = f"{int(duration.total_seconds() // 60)} minutes {int(duration.total_seconds() % 60)} seconds" if duration else "N/A"

        # Create summary table
        table = Table(show_header=False, box=box.SIMPLE)
        table.add_column("Label", style="dim")
        table.add_column("Value", style="bold")

        table.add_row("Module", session.module_id)
        table.add_row("Duration", duration_str)
        table.add_row("", "")
        table.add_row("[green]✓ Approved[/green]", f"{session.questions_approved} questions")
        table.add_row("[cyan]✏ Edited[/cyan]", f"{session.questions_edited} questions")
        table.add_row("[red]✗ Rejected[/red]", f"{session.questions_rejected} questions")
        table.add_row("[yellow]⏭ Skipped[/yellow]", f"{session.questions_skipped} questions")

        console.print(table)
        console.print()

        # Show file paths
        if session.questions_approved > 0 or session.questions_edited > 0:
            approved_file = self.approved_dir / f"{session.module_id}.json"
            console.print(f"[green]Approved questions saved to:[/green]")
            console.print(f"  {approved_file}")
            console.print()

        if session.questions_rejected > 0:
            rejected_file = self.rejected_dir / f"{session.module_id}-rejected.json"
            console.print(f"[red]Rejected questions saved to:[/red]")
            console.print(f"  {rejected_file}")
            console.print()

        if session.questions_skipped > 0:
            console.print(f"[yellow]Note: {session.questions_skipped} questions remain pending review.[/yellow]")
            console.print(f"[yellow]Run the review command again to continue.[/yellow]")
            console.print()

    def get_review_status(self, module_id: str) -> Dict[str, Any]:
        """
        Get review status for a module.

        Args:
            module_id: Module identifier

        Returns:
            Dictionary with status information:
            {
                "status": "no_questions" | "pending_review" | "all_reviewed",
                "pending_count": int,
                "approved_count": int,
                "staging_exists": bool,
                "approved_exists": bool
            }
        """
        staging_file = self.staging_dir / f"{module_id}-staging.json"
        approved_file = self.approved_dir / f"{module_id}.json"

        result = {
            "status": "no_questions",
            "pending_count": 0,
            "approved_count": 0,
            "staging_exists": staging_file.exists(),
            "approved_exists": approved_file.exists()
        }

        # Check staging file
        if staging_file.exists():
            try:
                with open(staging_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                question_bank = QuestionBank.from_dict(data)
                pending = question_bank.get_pending_questions()
                result["pending_count"] = len(pending)

                if pending:
                    result["status"] = "pending_review"
            except Exception as e:
                logger.error(f"Error reading staging file {staging_file}: {e}")

        # Check approved file
        if approved_file.exists():
            try:
                with open(approved_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                question_bank = QuestionBank.from_dict(data)
                result["approved_count"] = len(question_bank.questions)

                if result["pending_count"] == 0:
                    result["status"] = "all_reviewed"
            except Exception as e:
                logger.error(f"Error reading approved file {approved_file}: {e}")

        return result


def get_review_status(module_id: str, staging_dir: str = "question_banks/staging",
                     approved_dir: str = "question_banks/approved") -> Dict[str, Any]:
    """
    Convenience function to get review status for a module.

    Args:
        module_id: Module identifier
        staging_dir: Path to staging directory
        approved_dir: Path to approved directory

    Returns:
        Dictionary with status information

    Example:
        status = get_review_status("module-0")
        if status["status"] == "pending_review":
            print(f"{status['pending_count']} questions need review")
    """
    reviewer = QuestionReviewer(staging_dir=staging_dir, approved_dir=approved_dir)
    return reviewer.get_review_status(module_id)
