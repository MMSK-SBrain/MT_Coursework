#!/usr/bin/env python3
"""
Demo script to show QuestionReviewer capabilities without interactive input.
This demonstrates the review workflow programmatically.
"""

import sys
import json
from pathlib import Path

# Add project to path
sys.path.insert(0, str(Path(__file__).parent))

from src.question_reviewer import QuestionReviewer, get_review_status
from src.models import QuestionBank, Question, QuestionStatus
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()


def demo_status_check():
    """Demonstrate status checking."""
    console.print(Panel.fit(
        "[bold cyan]Demo: Question Review Status Check[/bold cyan]",
        border_style="cyan"
    ))
    console.print()

    # Check status for module-0
    status = get_review_status("module-0")

    console.print(f"[cyan]Module:[/cyan] module-0")
    console.print(f"[cyan]Status:[/cyan] {status['status']}")
    console.print(f"[cyan]Pending Questions:[/cyan] {status['pending_count']}")
    console.print(f"[cyan]Approved Questions:[/cyan] {status['approved_count']}")
    console.print(f"[cyan]Staging File Exists:[/cyan] {status['staging_exists']}")
    console.print(f"[cyan]Approved File Exists:[/cyan] {status['approved_exists']}")
    console.print()


def demo_programmatic_approval():
    """Demonstrate programmatic question approval (non-interactive)."""
    console.print(Panel.fit(
        "[bold cyan]Demo: Programmatic Question Approval[/bold cyan]",
        border_style="cyan"
    ))
    console.print()

    # Load staging file
    staging_file = Path("question_banks/staging/module-0-staging.json")

    if not staging_file.exists():
        console.print("[red]Error: Staging file not found[/red]")
        return

    with open(staging_file) as f:
        data = json.load(f)

    question_bank = QuestionBank.from_dict(data)
    pending_questions = question_bank.get_pending_questions()

    console.print(f"[green]Loaded {len(pending_questions)} pending questions[/green]")
    console.print()

    # Show first 3 questions
    console.print("[bold]Sample Questions:[/bold]")
    for i, q in enumerate(pending_questions[:3], 1):
        console.print(f"\n[cyan]Question {i}:[/cyan] {q.question_text}")
        console.print(f"[dim]Type:[/dim] {q.type.value}")
        console.print(f"[dim]Difficulty:[/dim] {q.difficulty.value}")
        if q.options:
            console.print(f"[dim]Options:[/dim] {', '.join(q.options[:2])}...")

    console.print()


def demo_question_types():
    """Show different question types in the staging file."""
    console.print(Panel.fit(
        "[bold cyan]Demo: Question Types Distribution[/bold cyan]",
        border_style="cyan"
    ))
    console.print()

    staging_file = Path("question_banks/staging/module-0-staging.json")

    if not staging_file.exists():
        console.print("[red]Error: Staging file not found[/red]")
        return

    with open(staging_file) as f:
        data = json.load(f)

    question_bank = QuestionBank.from_dict(data)

    # Count by type
    type_counts = {}
    difficulty_counts = {}

    for q in question_bank.questions:
        q_type = q.type.value
        difficulty = q.difficulty.value

        type_counts[q_type] = type_counts.get(q_type, 0) + 1
        difficulty_counts[difficulty] = difficulty_counts.get(difficulty, 0) + 1

    # Display type distribution
    type_table = Table(title="Question Types")
    type_table.add_column("Type", style="cyan")
    type_table.add_column("Count", justify="right", style="green")

    for q_type, count in sorted(type_counts.items()):
        type_table.add_row(q_type.replace("_", " ").title(), str(count))

    console.print(type_table)
    console.print()

    # Display difficulty distribution
    diff_table = Table(title="Question Difficulty")
    diff_table.add_column("Difficulty", style="cyan")
    diff_table.add_column("Count", justify="right", style="yellow")

    for difficulty, count in sorted(difficulty_counts.items()):
        diff_table.add_row(difficulty.title(), str(count))

    console.print(diff_table)
    console.print()


def demo_cli_usage():
    """Show CLI usage examples."""
    console.print(Panel.fit(
        "[bold cyan]Demo: CLI Usage Examples[/bold cyan]",
        border_style="cyan"
    ))
    console.print()

    examples = [
        ("Review questions for module-0",
         "python generate_handout.py --review-questions module-0"),

        ("Check review status for all modules",
         "python generate_handout.py --review-status --course ml-for-engineers"),

        ("Review questions with custom config",
         "python generate_handout.py --review-questions module-0 --config custom_config.yaml"),
    ]

    for description, command in examples:
        console.print(f"[cyan]# {description}[/cyan]")
        console.print(f"[green]$ {command}[/green]")
        console.print()


def main():
    """Run all demos."""
    console.clear()

    console.print("[bold green]Question Reviewer - Feature Demonstration[/bold green]")
    console.print("[dim]This demo shows the QuestionReviewer capabilities[/dim]")
    console.print()

    # Run demos
    demo_status_check()
    input("Press Enter to continue...")
    console.print()

    demo_question_types()
    input("Press Enter to continue...")
    console.print()

    demo_programmatic_approval()
    input("Press Enter to continue...")
    console.print()

    demo_cli_usage()

    console.print("[bold green]✓ Demo complete![/bold green]")
    console.print()
    console.print("[yellow]To try interactive review, run:[/yellow]")
    console.print("[green]python generate_handout.py --review-questions module-0[/green]")
    console.print()


if __name__ == "__main__":
    main()
