#!/usr/bin/env python3
"""
Student Handout Generator - CLI Interface

Main command-line interface for generating student handouts from framework markdown files.
Orchestrates the complete pipeline from parsing to PDF generation.

Usage:
    python generate_handout.py --input frameworks/module-0-framework-REVISED.md
    python generate_handout.py --input frameworks/module-0-framework-REVISED.md --dry-run
    python generate_handout.py --input frameworks/module-0-framework-REVISED.md --verbose

Author: Course Generator Team
Date: 2026-01-11
"""

import sys
import argparse
import logging
from pathlib import Path
from datetime import datetime
import time
from typing import Optional

from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn
from rich.panel import Panel
from rich.table import Table
from rich import print as rprint

from src.config_manager import ConfigManager, ConfigValidationError
from src.framework_parser import FrameworkParser, FrameworkParserError
from src.content_transformer import ContentTransformer
from src.question_loader import QuestionLoader
from src.question_reviewer import QuestionReviewer
from src.image_processor import ImageProcessor
from src.layout_engine import LayoutEngine
from src.pdf_renderer import PDFRenderer
from src.batch_processor import BatchProcessor
from src.models import HandoutDocument


# Exit codes (from PRD Section 7.5)
EXIT_SUCCESS = 0
EXIT_FATAL_ERROR = 1
EXIT_PARTIAL_SUCCESS = 2
EXIT_BLOCKED_BY_REVIEW = 3
EXIT_CONFIG_ERROR = 4

# Initialize rich console
console = Console()


def setup_logging(verbose: bool = False, log_file: Optional[str] = None) -> None:
    """
    Set up logging configuration.

    Args:
        verbose: Enable verbose (DEBUG) logging
        log_file: Path to log file (from config or default)
    """
    log_level = logging.DEBUG if verbose else logging.INFO

    # Create logs directory if it doesn't exist
    if log_file:
        log_path = Path(log_file)
        log_path.parent.mkdir(parents=True, exist_ok=True)

    # Configure logging format
    log_format = "[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s"

    handlers = []

    # Console handler (only WARNING and above unless verbose)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.WARNING if not verbose else logging.DEBUG)
    console_handler.setFormatter(logging.Formatter(log_format))
    handlers.append(console_handler)

    # File handler if specified
    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(logging.Formatter(log_format))
        handlers.append(file_handler)

    # Configure root logger
    logging.basicConfig(
        level=log_level,
        format=log_format,
        handlers=handlers
    )


def parse_arguments() -> argparse.Namespace:
    """
    Parse command-line arguments.

    Returns:
        Parsed arguments namespace
    """
    parser = argparse.ArgumentParser(
        description="Generate student handouts from framework markdown files",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate single handout
  python generate_handout.py --input frameworks/module-0-framework-REVISED.md

  # Batch process entire course
  python generate_handout.py --batch --course ml-for-engineers

  # Batch process specific modules only
  python generate_handout.py --batch --course ml-for-engineers --modules 0,1,2

  # Check review status
  python generate_handout.py --review-status --course ml-for-engineers

  # Review questions for a module
  python generate_handout.py --review-questions module-0

  # Dry run (validate without generating)
  python generate_handout.py --input frameworks/module-0-framework-REVISED.md --dry-run

  # Use approved questions (skip AI generation)
  python generate_handout.py --input frameworks/module-0-framework-REVISED.md --use-approved-questions

  # Force generation with unreviewed questions
  python generate_handout.py --batch --course ml-for-engineers --force-unreviewed

  # Verbose logging
  python generate_handout.py --input frameworks/module-0-framework-REVISED.md --verbose

For more information, see README.md
        """
    )

    # Input arguments
    parser.add_argument(
        '--input', '-i',
        type=str,
        help='Path to framework markdown file (required unless --batch/--review-questions/--review-status)'
    )

    # Configuration
    parser.add_argument(
        '--config',
        type=str,
        default='handout_config.yaml',
        help='Path to configuration file (default: handout_config.yaml)'
    )

    # Output
    parser.add_argument(
        '--output', '-o',
        type=str,
        help='Output directory (default: from config)'
    )

    # Mode flags
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Validate inputs without generating PDF'
    )

    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Enable verbose logging (DEBUG level)'
    )

    # Question handling
    parser.add_argument(
        '--use-approved-questions',
        action='store_true',
        help='Skip AI generation, use approved question bank only'
    )

    parser.add_argument(
        '--force-unreviewed',
        action='store_true',
        help='Generate with unreviewed questions (adds warning banner)'
    )

    # Batch processing
    parser.add_argument(
        '--batch', '-b',
        action='store_true',
        help='Batch process all modules in course'
    )

    parser.add_argument(
        '--review-questions',
        type=str,
        metavar='MODULE_ID',
        help='Review AI-generated questions for module interactively'
    )

    parser.add_argument(
        '--review-status',
        action='store_true',
        help='Show review status for all modules (requires --course)'
    )

    parser.add_argument(
        '--course', '-c',
        type=str,
        help='Course name for batch processing or review status'
    )

    parser.add_argument(
        '--modules', '-m',
        type=str,
        help='Comma-separated module numbers for selective batch processing (e.g., "0,1,2")'
    )

    args = parser.parse_args()

    # Validation
    if not args.input and not args.batch and not args.review_questions and not args.review_status:
        parser.error("--input is required unless using --batch, --review-questions, or --review-status")

    if args.batch and not args.course:
        parser.error("--batch requires --course to be specified")

    if args.review_status and not args.course:
        parser.error("--review-status requires --course to be specified")

    if args.modules and not args.batch:
        parser.error("--modules can only be used with --batch")

    return args


def validate_dry_run(args: argparse.Namespace, config: ConfigManager) -> bool:
    """
    Perform dry-run validation without generating PDF.

    Args:
        args: Parsed command-line arguments
        config: ConfigManager instance

    Returns:
        True if validation passes, False otherwise
    """
    console.print("\n[bold cyan]Dry Run Mode - Validation Only[/bold cyan]\n")

    validation_results = []
    all_valid = True

    # 1. Check input file exists
    input_path = Path(args.input)
    if input_path.exists():
        validation_results.append(("Input file", str(input_path), "✓", "green"))
    else:
        validation_results.append(("Input file", str(input_path), "✗ Not found", "red"))
        all_valid = False

    # 2. Check configuration
    try:
        config_dict = config.to_dict()
        validation_results.append(("Configuration", args.config, "✓", "green"))
    except Exception as e:
        validation_results.append(("Configuration", args.config, f"✗ {str(e)}", "red"))
        all_valid = False

    # 3. Check output directory
    output_dir = Path(args.output) if args.output else Path(config.get("global.output_directory", "./handouts"))
    if output_dir.parent.exists():
        validation_results.append(("Output directory", str(output_dir), "✓ (will create)", "green"))
    else:
        validation_results.append(("Output directory", str(output_dir), "✗ Parent does not exist", "red"))
        all_valid = False

    # 4. Check WeasyPrint availability
    try:
        from weasyprint import HTML
        validation_results.append(("WeasyPrint", "weasyprint", "✓ Installed", "green"))
    except ImportError:
        validation_results.append(("WeasyPrint", "weasyprint", "✗ Not installed", "red"))
        all_valid = False

    # 5. Check fonts
    fonts_dir = Path("assets/fonts")
    if fonts_dir.exists():
        validation_results.append(("Fonts", str(fonts_dir), "✓", "green"))
    else:
        validation_results.append(("Fonts", str(fonts_dir), "⚠ Missing (will use system fonts)", "yellow"))

    # 6. Check question bank if using approved questions
    if args.use_approved_questions:
        # Try to infer module ID from filename
        module_id = None
        if "module-" in input_path.name:
            match = input_path.name.split("module-")[1].split("-")[0]
            module_id = f"module-{match}"

        if module_id:
            question_file = Path(config.get("questions.approved_directory", "question_banks/approved")) / f"{module_id}.json"
            if question_file.exists():
                validation_results.append(("Question bank", str(question_file), "✓", "green"))
            else:
                validation_results.append(("Question bank", str(question_file), "✗ Not found", "red"))
                all_valid = False

    # Display results table
    table = Table(title="Validation Results")
    table.add_column("Component", style="cyan", no_wrap=True)
    table.add_column("Path/Value", style="white")
    table.add_column("Status", style="bold")

    for component, path, status, color in validation_results:
        table.add_row(component, path, f"[{color}]{status}[/{color}]")

    console.print(table)

    # Summary
    if all_valid:
        console.print("\n[bold green]✓ All validations passed[/bold green]")
        console.print("[dim]Ready to generate handout (remove --dry-run to proceed)[/dim]\n")
        return True
    else:
        console.print("\n[bold red]✗ Some validations failed[/bold red]")
        console.print("[dim]Fix the issues above before generating[/dim]\n")
        return False


def generate_handout(args: argparse.Namespace, config: ConfigManager) -> int:
    """
    Generate a single handout from framework file.

    Pipeline orchestration:
    1. Load configuration
    2. Parse framework file
    3. Transform content (remove instructor sections)
    4. Load/generate questions
    5. Process images
    6. Create HandoutDocument
    7. Generate layout (HTML)
    8. Render PDF

    Args:
        args: Parsed command-line arguments
        config: ConfigManager instance

    Returns:
        Exit code (0 = success, 1 = fatal error)
    """
    start_time = time.time()
    logger = logging.getLogger(__name__)

    try:
        # Display header
        console.print(Panel.fit(
            "[bold cyan]Student Handout Generator[/bold cyan]\n"
            f"Input: {args.input}",
            border_style="cyan"
        ))

        # Initialize components
        input_path = Path(args.input)
        output_dir = Path(args.output) if args.output else Path(config.get("global.output_directory", "./handouts"))

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TaskProgressColumn(),
            console=console
        ) as progress:

            # Step 1: Parse framework file
            parse_task = progress.add_task("[cyan]Parsing framework file...", total=1)
            logger.info(f"Parsing framework file: {input_path}")

            parser = FrameworkParser()
            parse_result = parser.parse_file(input_path)

            if not parse_result.success:
                console.print(f"\n[bold red]✗ Failed to parse framework file[/bold red]")
                for error in parse_result.errors:
                    console.print(f"  [red]• {error}[/red]")
                return EXIT_FATAL_ERROR

            progress.update(parse_task, completed=1)
            console.print(f"[green]✓[/green] Parsed {len(parse_result.sections)} sections")

            # Step 2: Transform content
            transform_task = progress.add_task("[cyan]Transforming content...", total=1)
            logger.info("Transforming content (removing instructor sections)")

            transformer = ContentTransformer(config)
            transformed_sections = transformer.transform(parse_result.sections)

            progress.update(transform_task, completed=1)
            console.print(f"[green]✓[/green] Transformed {len(transformed_sections)} sections")

            # Step 3: Load/generate questions
            question_task = progress.add_task("[cyan]Loading questions...", total=1)

            # Extract module ID from metadata
            module_id = f"module-{parse_result.metadata.module_number}"
            logger.info(f"Loading questions for {module_id}")

            # For now, always use manual question loading (Story 9 will add AI generation)
            if args.use_approved_questions or True:  # Force manual for now
                question_loader = QuestionLoader(
                    question_banks_dir=config.get("questions.approved_directory", "question_banks/approved")
                )
                questions = question_loader.load_questions(module_id)

                if not questions:
                    console.print(f"\n[yellow]⚠ No approved questions found for {module_id}[/yellow]")
                    console.print(f"[dim]Looking in: {config.get('questions.approved_directory')}[/dim]")

                    if not args.force_unreviewed:
                        console.print(f"\n[yellow]Continuing without questions. Use --force-unreviewed to suppress this check.[/yellow]")
            else:
                # This will be implemented in Story 9 (AI Question Generator)
                console.print("[yellow]Note: AI question generation not yet implemented (Story 9)[/yellow]")
                questions = []

            progress.update(question_task, completed=1)
            console.print(f"[green]✓[/green] Loaded {len(questions)} questions")

            # Step 4: Process images
            image_task = progress.add_task("[cyan]Processing images...", total=1)
            logger.info("Processing images")

            image_processor = ImageProcessor(config)
            processed_images = image_processor.process_images(parse_result.images)

            missing_count = sum(1 for img in processed_images if img.placeholder_used)

            progress.update(image_task, completed=1)
            if missing_count > 0:
                console.print(f"[yellow]⚠[/yellow] Processed {len(processed_images)} images ({missing_count} missing, using placeholders)")
            else:
                console.print(f"[green]✓[/green] Processed {len(processed_images)} images")

            # Step 5: Create HandoutDocument
            doc_task = progress.add_task("[cyan]Creating handout document...", total=1)
            logger.info("Creating handout document")

            handout_doc = HandoutDocument(
                metadata=parse_result.metadata,
                sections=transformed_sections,
                questions=questions,
                images=processed_images,
                generation_timestamp=datetime.now(),
                config_used=config.to_dict(),
                question_review_complete=(len(questions) > 0)
            )

            # Add warnings from parse result
            for warning in parse_result.warnings:
                handout_doc.add_warning(warning)

            progress.update(doc_task, completed=1)
            console.print(f"[green]✓[/green] Created handout document")

            # Step 6: Generate layout (HTML)
            layout_task = progress.add_task("[cyan]Generating layout...", total=1)
            logger.info("Generating HTML layout")

            layout_engine = LayoutEngine()  # Uses default templates directory
            html_content = layout_engine.generate_html(handout_doc)

            progress.update(layout_task, completed=1)
            console.print(f"[green]✓[/green] Generated HTML layout")

            # Step 7: Render PDF
            pdf_task = progress.add_task("[cyan]Rendering PDF...", total=1)
            logger.info("Rendering PDF")

            pdf_renderer = PDFRenderer(config)
            pdf_path = pdf_renderer.render_handout(
                html_content=html_content,
                course_code=parse_result.metadata.course_code,
                module_number=parse_result.metadata.module_number,
                module_title=parse_result.metadata.module_title,
                output_dir=output_dir
            )

            progress.update(pdf_task, completed=1)

        # Success summary
        elapsed_time = time.time() - start_time

        console.print(f"\n[bold green]✓ Handout generated successfully![/bold green]")
        console.print(f"\n[cyan]Output:[/cyan] {pdf_path}")
        console.print(f"[cyan]Processing time:[/cyan] {elapsed_time:.1f} seconds")

        # Statistics
        stats_table = Table(show_header=False, box=None, padding=(0, 2))
        stats_table.add_row("[cyan]Sections:[/cyan]", str(len(transformed_sections)))
        stats_table.add_row("[cyan]Questions:[/cyan]", str(len(questions)))
        stats_table.add_row("[cyan]Images:[/cyan]", str(len(processed_images)))

        if handout_doc.warnings:
            stats_table.add_row("[yellow]Warnings:[/yellow]", str(len(handout_doc.warnings)))

        console.print(stats_table)

        # Display warnings if any
        if handout_doc.warnings:
            console.print("\n[yellow]Warnings:[/yellow]")
            for warning in handout_doc.warnings:
                console.print(f"  [yellow]• {warning}[/yellow]")

        console.print()
        return EXIT_SUCCESS

    except ConfigValidationError as e:
        console.print(f"\n[bold red]✗ Configuration Error[/bold red]")
        console.print(f"[red]{str(e)}[/red]\n")
        logger.error(f"Configuration error: {e}")
        return EXIT_CONFIG_ERROR

    except FrameworkParserError as e:
        console.print(f"\n[bold red]✗ Parser Error[/bold red]")
        console.print(f"[red]{str(e)}[/red]\n")
        logger.error(f"Parser error: {e}")
        return EXIT_FATAL_ERROR

    except Exception as e:
        console.print(f"\n[bold red]✗ Unexpected Error[/bold red]")
        console.print(f"[red]{str(e)}[/red]\n")
        logger.exception(f"Unexpected error during generation")
        return EXIT_FATAL_ERROR


def review_questions(module_id: str, config: ConfigManager) -> int:
    """
    Start interactive question review session for a module.

    Args:
        module_id: Module identifier (e.g., "module-0")
        config: ConfigManager instance

    Returns:
        Exit code
    """
    logger = logging.getLogger(__name__)

    try:
        # Initialize reviewer
        reviewer = QuestionReviewer(
            staging_dir=config.get("questions.staging_directory", "question_banks/staging"),
            approved_dir=config.get("questions.approved_directory", "question_banks/approved"),
            rejected_dir=config.get("questions.rejected_directory", "question_banks/rejected")
        )

        # Start review session
        session = reviewer.start_session(module_id)

        # Exit code based on results
        if session.questions_total == 0:
            return EXIT_SUCCESS
        elif session.questions_skipped > 0:
            return EXIT_SUCCESS  # Can resume later
        else:
            return EXIT_SUCCESS

    except Exception as e:
        console.print(f"\n[bold red]✗ Review Error[/bold red]")
        console.print(f"[red]{str(e)}[/red]\n")
        logger.exception("Error during question review")
        return EXIT_FATAL_ERROR


def show_review_status(course_name: str, config: ConfigManager) -> int:
    """
    Show review status for all modules in a course.

    Args:
        course_name: Course name (e.g., "ml-for-engineers")
        config: ConfigManager instance

    Returns:
        Exit code
    """
    logger = logging.getLogger(__name__)

    try:
        # Initialize reviewer
        reviewer = QuestionReviewer(
            staging_dir=config.get("questions.staging_directory", "question_banks/staging"),
            approved_dir=config.get("questions.approved_directory", "question_banks/approved"),
            rejected_dir=config.get("questions.rejected_directory", "question_banks/rejected")
        )

        # Find all staging files
        staging_dir = Path(config.get("questions.staging_directory", "question_banks/staging"))
        staging_files = list(staging_dir.glob("*-staging.json"))

        if not staging_files:
            console.print(f"[yellow]No staging files found in {staging_dir}[/yellow]")
            return EXIT_SUCCESS

        # Display header
        console.print(Panel.fit(
            f"[bold cyan]Question Review Status: {course_name}[/bold cyan]",
            border_style="cyan"
        ))
        console.print()

        # Create status table
        table = Table(title="Module Review Status")
        table.add_column("Module", style="cyan", no_wrap=True)
        table.add_column("Status", style="bold")
        table.add_column("Pending", justify="right", style="yellow")
        table.add_column("Approved", justify="right", style="green")

        # Get status for each module
        for staging_file in sorted(staging_files):
            module_id = staging_file.stem.replace("-staging", "")
            status = reviewer.get_review_status(module_id)

            if status["status"] == "pending_review":
                status_str = "[yellow]Pending Review[/yellow]"
            elif status["status"] == "all_reviewed":
                status_str = "[green]All Reviewed[/green]"
            else:
                status_str = "[dim]No Questions[/dim]"

            table.add_row(
                module_id,
                status_str,
                str(status["pending_count"]),
                str(status["approved_count"])
            )

        console.print(table)
        console.print()

        # Summary
        total_pending = sum(
            reviewer.get_review_status(f.stem.replace("-staging", ""))["pending_count"]
            for f in staging_files
        )

        if total_pending > 0:
            console.print(f"[yellow]⚠ {total_pending} questions need review across all modules[/yellow]")
            console.print(f"[dim]Use: python generate_handout.py --review-questions <module-id>[/dim]")
        else:
            console.print("[green]✓ All questions reviewed[/green]")

        console.print()
        return EXIT_SUCCESS

    except Exception as e:
        console.print(f"\n[bold red]✗ Error[/bold red]")
        console.print(f"[red]{str(e)}[/red]\n")
        logger.exception("Error checking review status")
        return EXIT_FATAL_ERROR


def batch_process_course(args: argparse.Namespace, config: ConfigManager) -> int:
    """
    Batch process all modules (or selected modules) in a course.

    Args:
        args: Parsed command-line arguments
        config: ConfigManager instance

    Returns:
        Exit code (0 = all success, 2 = partial success, 3 = blocked by review)
    """
    logger = logging.getLogger(__name__)

    try:
        # Parse module numbers if specified
        module_numbers = None
        if args.modules:
            try:
                module_numbers = [int(n.strip()) for n in args.modules.split(",")]
                logger.info(f"Selective batch processing: modules {module_numbers}")
            except ValueError:
                console.print(f"[red]Error:[/red] Invalid module numbers format: {args.modules}")
                console.print("[dim]Expected format: --modules 0,1,2[/dim]")
                return EXIT_CONFIG_ERROR

        # Initialize batch processor
        processor = BatchProcessor(config)

        # Process course
        results = processor.process_course(
            course_name=args.course,
            module_numbers=module_numbers,
            force_unreviewed=args.force_unreviewed
        )

        # Determine exit code based on results
        if not results:
            return EXIT_FATAL_ERROR

        successful = sum(1 for r in results.values() if r.success)
        blocked = sum(1 for r in results.values() if r.blocked_by_review)
        failed = len(results) - successful - blocked

        # Exit codes:
        # 0 = all successful
        # 2 = partial success (some failures)
        # 3 = blocked by review
        if blocked > 0 and successful == 0:
            return EXIT_BLOCKED_BY_REVIEW
        elif failed > 0:
            return EXIT_PARTIAL_SUCCESS
        else:
            return EXIT_SUCCESS

    except Exception as e:
        console.print(f"\n[bold red]✗ Batch Processing Error[/bold red]")
        console.print(f"[red]{str(e)}[/red]\n")
        logger.exception("Error during batch processing")
        return EXIT_FATAL_ERROR


def main() -> int:
    """
    Main entry point for CLI.

    Returns:
        Exit code
    """
    # Parse arguments
    args = parse_arguments()

    # Load configuration
    try:
        if Path(args.config).exists():
            config = ConfigManager.from_file(args.config)
        else:
            console.print(f"[yellow]Warning: Config file not found ({args.config}), using defaults[/yellow]")
            config = ConfigManager.from_defaults()
    except ConfigValidationError as e:
        console.print(f"[bold red]✗ Configuration Error[/bold red]")
        console.print(f"[red]{str(e)}[/red]\n")
        return EXIT_CONFIG_ERROR

    # Set up logging
    log_file = config.get("logging.file", "./logs/handout_generation.log")
    setup_logging(verbose=args.verbose, log_file=log_file)

    # Question review mode
    if args.review_questions:
        return review_questions(args.review_questions, config)

    # Review status mode
    if args.review_status:
        return show_review_status(args.course, config)

    # Batch processing mode
    if args.batch:
        return batch_process_course(args, config)

    # Dry run mode
    if args.dry_run:
        if validate_dry_run(args, config):
            return EXIT_SUCCESS
        else:
            return EXIT_FATAL_ERROR

    # Generate handout (single module)
    return generate_handout(args, config)


if __name__ == "__main__":
    sys.exit(main())
