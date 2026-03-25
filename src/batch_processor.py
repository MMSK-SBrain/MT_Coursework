"""
Batch Processor for Student Handout Generator

Processes multiple modules in a course with review status checking,
progress tracking, and error handling.

Author: Course Generator Team
Date: 2026-01-11
"""

import re
import shutil
import time
import logging
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple

from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn, TimeElapsedColumn
from rich.panel import Panel
from rich.table import Table
from rich import box

from src.config_manager import ConfigManager
from src.framework_parser import FrameworkParser
from src.content_transformer import ContentTransformer
from src.question_loader import QuestionLoader
from src.question_reviewer import QuestionReviewer
from src.image_processor import ImageProcessor
from src.layout_engine import LayoutEngine
from src.pdf_renderer import PDFRenderer
from src.models import HandoutDocument

logger = logging.getLogger(__name__)
console = Console()


class BatchProcessResult:
    """Result of processing a single module in batch mode."""

    def __init__(
        self,
        module_id: str,
        success: bool,
        output_path: Optional[Path] = None,
        error: Optional[str] = None,
        blocked_by_review: bool = False,
        processing_time: float = 0.0
    ):
        self.module_id = module_id
        self.success = success
        self.output_path = output_path
        self.error = error
        self.blocked_by_review = blocked_by_review
        self.processing_time = processing_time


class BatchProcessor:
    """
    Batch processor for generating handouts for all modules in a course.

    Responsibilities:
    - Discover framework files in course directory
    - Check question review status for all modules
    - Block generation if any questions pending review (unless --force-unreviewed)
    - Process modules sequentially (one at a time to avoid resource issues)
    - Show progress indication (current module, ETA)
    - Continue on individual failures (log error, continue to next)
    - Generate summary report (successful/failed/blocked)
    - Support selective module processing (e.g., --modules 0,1,2)
    - Archive old versions before regenerating

    Usage:
        processor = BatchProcessor(config)
        results = processor.process_course("ml-for-engineers")
        results = processor.process_course("ml-for-engineers", module_numbers=[0, 1, 2])
    """

    def __init__(self, config: ConfigManager):
        """
        Initialize BatchProcessor.

        Args:
            config: ConfigManager instance with loaded configuration
        """
        self.config = config
        self.course_base_dir = Path("courses")

    def discover_frameworks(self, course_dir: Path) -> List[Tuple[Path, str]]:
        """
        Discover all framework files in course directory.

        Expected structure:
        courses/ml-for-engineers/
          ├── frameworks/
          │   ├── module-0-framework-REVISED.md
          │   ├── module-1-framework-REVISED.md
          │   └── ...

        Args:
            course_dir: Path to course directory (e.g., courses/ml-for-engineers)

        Returns:
            List of tuples: (framework_path, module_id)
            Sorted by module number

        Example:
            [(Path("module-0-framework-REVISED.md"), "module-0"),
             (Path("module-1-framework-REVISED.md"), "module-1")]
        """
        frameworks_dir = course_dir / "frameworks"

        if not frameworks_dir.exists():
            logger.warning(f"Frameworks directory not found: {frameworks_dir}")
            return []

        # Find all .md files matching pattern
        pattern = "*-framework*.md"
        files = list(frameworks_dir.glob(pattern))

        # Extract module ID and create tuples
        results = []
        for file_path in files:
            try:
                module_id = self._extract_module_id(file_path)
                if module_id:
                    results.append((file_path, module_id))
            except ValueError as e:
                logger.warning(f"Could not extract module ID from {file_path.name}: {e}")

        # Sort by module number
        results.sort(key=lambda x: self._get_module_number(x[1]))

        logger.info(f"Discovered {len(results)} framework files in {frameworks_dir}")
        return results

    def _extract_module_id(self, framework_path: Path) -> str:
        """
        Extract module ID from framework filename.

        Examples:
        - "module-0-framework-REVISED.md" -> "module-0"
        - "module-10-framework.md" -> "module-10"
        - "module-1-learning-framework.md" -> "module-1"

        Args:
            framework_path: Path to framework file

        Returns:
            Module ID (e.g., "module-0")

        Raises:
            ValueError: If module ID cannot be extracted
        """
        match = re.search(r'module-(\d+)', framework_path.name)
        if match:
            return f"module-{match.group(1)}"
        raise ValueError(f"Cannot extract module ID from: {framework_path.name}")

    def _get_module_number(self, module_id: str) -> int:
        """
        Extract numeric module number from module ID.

        Args:
            module_id: Module identifier (e.g., "module-0")

        Returns:
            Module number as integer
        """
        match = re.search(r'module-(\d+)', module_id)
        if match:
            return int(match.group(1))
        return 999  # Put unmatched items at end

    def check_review_status(
        self,
        frameworks: List[Tuple[Path, str]]
    ) -> Tuple[List[str], List[str], List[str]]:
        """
        Check question review status for all modules.

        Args:
            frameworks: List of (framework_path, module_id) tuples

        Returns:
            Tuple of (pending_modules, reviewed_modules, no_questions_modules)
            - pending_modules: Modules with questions needing review
            - reviewed_modules: Modules with all questions reviewed
            - no_questions_modules: Modules with no questions
        """
        reviewer = QuestionReviewer(
            staging_dir=self.config.get("questions.staging_directory", "question_banks/staging"),
            approved_dir=self.config.get("questions.approved_directory", "question_banks/approved"),
            rejected_dir=self.config.get("questions.rejected_directory", "question_banks/rejected")
        )

        pending_modules = []
        reviewed_modules = []
        no_questions_modules = []

        for _, module_id in frameworks:
            status = reviewer.get_review_status(module_id)

            if status["status"] == "pending_review":
                pending_modules.append(module_id)
            elif status["status"] == "all_reviewed":
                reviewed_modules.append(module_id)
            else:
                no_questions_modules.append(module_id)

        logger.info(f"Review status: {len(reviewed_modules)} reviewed, "
                   f"{len(pending_modules)} pending, {len(no_questions_modules)} no questions")

        return pending_modules, reviewed_modules, no_questions_modules

    def archive_old_handout(
        self,
        course_code: str,
        module_number: int,
        output_dir: Path
    ) -> Optional[Path]:
        """
        Archive existing handout before regenerating.

        Moves existing PDF to archive/ subdirectory with timestamp.

        Args:
            course_code: Course code (e.g., "ML-ENG")
            module_number: Module number
            output_dir: Output directory

        Returns:
            Path to archived file if archived, None if no existing file
        """
        if not self.config.get("global.archive_old_versions", True):
            return None

        # Find existing PDF
        old_pdf = output_dir / f"{course_code}-module-{module_number}-handout.pdf"

        if not old_pdf.exists():
            return None

        # Create archive directory
        archive_dir = output_dir / "archive"
        archive_dir.mkdir(parents=True, exist_ok=True)

        # Generate archive filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        archived_name = f"{course_code}-module-{module_number}-handout-{timestamp}.pdf"
        archived_path = archive_dir / archived_name

        # Move file
        try:
            shutil.move(str(old_pdf), str(archived_path))
            logger.info(f"Archived old handout to {archived_path}")
            return archived_path
        except Exception as e:
            logger.error(f"Failed to archive {old_pdf}: {e}")
            return None

    def process_single_module(
        self,
        framework_path: Path,
        module_id: str,
        output_dir: Path,
        force_unreviewed: bool = False
    ) -> BatchProcessResult:
        """
        Process a single module (generate handout).

        This reuses the pipeline from generate_handout.py but returns
        a BatchProcessResult for summary reporting.

        Args:
            framework_path: Path to framework markdown file
            module_id: Module identifier
            output_dir: Output directory for PDF
            force_unreviewed: Generate even if questions pending review

        Returns:
            BatchProcessResult with success/error information
        """
        start_time = time.time()

        try:
            # Parse framework file
            parser = FrameworkParser()
            parse_result = parser.parse_file(framework_path)

            if not parse_result.success:
                error_msg = "; ".join(parse_result.errors)
                return BatchProcessResult(
                    module_id=module_id,
                    success=False,
                    error=f"Parse error: {error_msg}",
                    processing_time=time.time() - start_time
                )

            # Check review status (unless forced)
            if not force_unreviewed:
                reviewer = QuestionReviewer(
                    staging_dir=self.config.get("questions.staging_directory", "question_banks/staging"),
                    approved_dir=self.config.get("questions.approved_directory", "question_banks/approved")
                )
                status = reviewer.get_review_status(module_id)

                if status["status"] == "pending_review":
                    return BatchProcessResult(
                        module_id=module_id,
                        success=False,
                        blocked_by_review=True,
                        error=f"{status['pending_count']} questions pending review",
                        processing_time=time.time() - start_time
                    )

            # Archive old version
            self.archive_old_handout(
                course_code=parse_result.metadata.course_code,
                module_number=parse_result.metadata.module_number,
                output_dir=output_dir
            )

            # Transform content
            transformer = ContentTransformer(self.config)
            transformed_sections = transformer.transform(parse_result.sections)

            # Load questions
            question_loader = QuestionLoader(
                question_banks_dir=self.config.get("questions.approved_directory", "question_banks/approved")
            )
            questions = question_loader.load_questions(module_id)

            # Process images
            image_processor = ImageProcessor(self.config)
            processed_images = image_processor.process_images(
                parse_result.images,
                framework_path.parent
            )

            # Create handout document
            handout_doc = HandoutDocument(
                metadata=parse_result.metadata,
                sections=transformed_sections,
                questions=questions,
                images=processed_images,
                generation_timestamp=datetime.now(),
                config_used=self.config.to_dict(),
                question_review_complete=(len(questions) > 0)
            )

            # Add warnings from parse result
            for warning in parse_result.warnings:
                handout_doc.add_warning(warning)

            # Generate layout
            layout_engine = LayoutEngine(self.config)
            html_content = layout_engine.render(handout_doc)

            # Render PDF
            pdf_renderer = PDFRenderer(self.config)
            pdf_path = pdf_renderer.render_handout(
                html_content=html_content,
                course_code=parse_result.metadata.course_code,
                module_number=parse_result.metadata.module_number,
                module_title=parse_result.metadata.module_title,
                output_dir=output_dir
            )

            processing_time = time.time() - start_time

            logger.info(f"Successfully generated handout for {module_id} in {processing_time:.1f}s")

            return BatchProcessResult(
                module_id=module_id,
                success=True,
                output_path=pdf_path,
                processing_time=processing_time
            )

        except Exception as e:
            processing_time = time.time() - start_time
            error_msg = str(e)
            logger.error(f"Error processing {module_id}: {error_msg}", exc_info=True)

            return BatchProcessResult(
                module_id=module_id,
                success=False,
                error=error_msg,
                processing_time=processing_time
            )

    def process_course(
        self,
        course_name: str,
        module_numbers: Optional[List[int]] = None,
        force_unreviewed: bool = False
    ) -> Dict[str, BatchProcessResult]:
        """
        Batch process all modules (or selected modules) in a course.

        Workflow:
        1. Discover framework files
        2. Check review status for ALL modules
        3. Block if any pending reviews (unless force_unreviewed)
        4. Process modules sequentially with progress tracking
        5. Continue on individual failures
        6. Generate summary report

        Args:
            course_name: Course name (e.g., "ml-for-engineers")
            module_numbers: Optional list of module numbers to process (e.g., [0, 1, 2])
                           If None, process all modules
            force_unreviewed: Generate even if questions pending review

        Returns:
            Dictionary of {module_id: BatchProcessResult}
        """
        start_time = time.time()

        # Display header
        console.print(Panel.fit(
            f"[bold cyan]Batch Processing: {course_name}[/bold cyan]\n"
            f"Mode: {'Selective modules' if module_numbers else 'All modules'}",
            border_style="cyan"
        ))
        console.print()

        # Step 1: Discover framework files
        course_dir = self.course_base_dir / course_name
        if not course_dir.exists():
            console.print(f"[red]Error:[/red] Course directory not found: {course_dir}")
            return {}

        frameworks = self.discover_frameworks(course_dir)

        if not frameworks:
            console.print(f"[red]Error:[/red] No framework files found in {course_dir / 'frameworks'}")
            return {}

        # Filter by module numbers if specified
        if module_numbers is not None:
            module_ids = {f"module-{n}" for n in module_numbers}
            frameworks = [(path, mid) for path, mid in frameworks if mid in module_ids]

            if not frameworks:
                console.print(f"[red]Error:[/red] No frameworks found for specified modules: {module_numbers}")
                return {}

        console.print(f"[cyan]Found {len(frameworks)} framework file(s)[/cyan]")
        for path, module_id in frameworks:
            console.print(f"  • {module_id}: {path.name}")
        console.print()

        # Step 2: Check review status
        console.print("[cyan]Checking question review status...[/cyan]")
        pending_modules, reviewed_modules, no_questions_modules = self.check_review_status(frameworks)

        # Display review status table
        if pending_modules or reviewed_modules or no_questions_modules:
            status_table = Table(title="Review Status", box=box.SIMPLE)
            status_table.add_column("Status", style="bold")
            status_table.add_column("Count", justify="right")
            status_table.add_column("Modules")

            if reviewed_modules:
                status_table.add_row(
                    "[green]✓ Reviewed[/green]",
                    str(len(reviewed_modules)),
                    ", ".join(reviewed_modules)
                )

            if no_questions_modules:
                status_table.add_row(
                    "[dim]○ No Questions[/dim]",
                    str(len(no_questions_modules)),
                    ", ".join(no_questions_modules)
                )

            if pending_modules:
                status_table.add_row(
                    "[yellow]⚠ Pending Review[/yellow]",
                    str(len(pending_modules)),
                    ", ".join(pending_modules)
                )

            console.print(status_table)
            console.print()

        # Step 3: Block if any pending reviews (unless forced)
        if pending_modules and not force_unreviewed:
            console.print(Panel(
                f"[bold yellow]Cannot batch generate - {len(pending_modules)} module(s) have pending reviews[/bold yellow]\n\n"
                f"Pending modules: {', '.join(pending_modules)}\n\n"
                f"Options:\n"
                f"  1. Review questions: python generate_handout.py --review-questions <module-id>\n"
                f"  2. Force generation: python generate_handout.py --batch --course {course_name} --force-unreviewed",
                title="[yellow]Blocked by Review[/yellow]",
                border_style="yellow"
            ))
            logger.warning(f"Batch processing blocked: {len(pending_modules)} modules need review")

            # Return blocked results
            results = {}
            for _, module_id in frameworks:
                if module_id in pending_modules:
                    results[module_id] = BatchProcessResult(
                        module_id=module_id,
                        success=False,
                        blocked_by_review=True,
                        error="Questions pending review"
                    )
            return results

        # Step 4: Process modules sequentially with progress tracking
        output_dir = Path(self.config.get("global.output_directory", "./handouts"))
        results = {}

        console.print(f"[bold cyan]Processing {len(frameworks)} module(s)...[/bold cyan]\n")

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TaskProgressColumn(),
            TimeElapsedColumn(),
            console=console
        ) as progress:

            overall_task = progress.add_task(
                "[cyan]Overall progress",
                total=len(frameworks)
            )

            for framework_path, module_id in frameworks:
                # Update progress description
                progress.update(
                    overall_task,
                    description=f"[cyan]Processing {module_id}..."
                )

                # Process module
                result = self.process_single_module(
                    framework_path=framework_path,
                    module_id=module_id,
                    output_dir=output_dir,
                    force_unreviewed=force_unreviewed
                )

                results[module_id] = result

                # Update progress
                progress.update(overall_task, advance=1)

                # Log result
                if result.success:
                    logger.info(f"✓ {module_id}: Success ({result.processing_time:.1f}s)")
                elif result.blocked_by_review:
                    logger.warning(f"⏸ {module_id}: Blocked by review")
                else:
                    logger.error(f"✗ {module_id}: {result.error}")

        # Step 5: Generate summary report
        console.print()
        self._display_summary(results, course_name, time.time() - start_time, output_dir)

        return results

    def _display_summary(
        self,
        results: Dict[str, BatchProcessResult],
        course_name: str,
        total_time: float,
        output_dir: Path
    ) -> None:
        """
        Display batch processing summary report.

        Args:
            results: Dictionary of {module_id: BatchProcessResult}
            course_name: Course name
            total_time: Total processing time in seconds
            output_dir: Output directory path
        """
        console.rule("[bold green]Batch Processing Complete[/bold green]", style="green")
        console.print()

        # Count results by status
        successful = [r for r in results.values() if r.success]
        failed = [r for r in results.values() if not r.success and not r.blocked_by_review]
        blocked = [r for r in results.values() if r.blocked_by_review]

        # Summary panel
        duration_mins = int(total_time // 60)
        duration_secs = int(total_time % 60)

        summary_table = Table(show_header=False, box=None, padding=(0, 2))
        summary_table.add_row("[cyan]Course:[/cyan]", course_name)
        summary_table.add_row("[cyan]Duration:[/cyan]", f"{duration_mins} minutes {duration_secs} seconds")
        summary_table.add_row("", "")
        summary_table.add_row("[green]✓ Successful:[/green]", f"{len(successful)} modules")
        summary_table.add_row("[red]✗ Failed:[/red]", f"{len(failed)} modules")
        summary_table.add_row("[yellow]⏭ Blocked:[/yellow]", f"{len(blocked)} modules")

        console.print(summary_table)
        console.print()

        # Successful modules
        if successful:
            console.print("[bold green]Successful modules:[/bold green]")
            for result in successful:
                try:
                    file_size = result.output_path.stat().st_size / (1024 * 1024) if result.output_path and result.output_path.exists() else 0
                except (FileNotFoundError, AttributeError):
                    file_size = 0
                console.print(
                    f"  [green]✓[/green] {result.module_id}: "
                    f"{result.output_path.name if result.output_path else 'N/A'} "
                    f"({file_size:.1f} MB, {result.processing_time:.1f}s)"
                )
            console.print()

        # Failed modules
        if failed:
            console.print("[bold red]Failed modules:[/bold red]")
            for result in failed:
                console.print(f"  [red]✗[/red] {result.module_id}: {result.error}")
            console.print()

        # Blocked modules
        if blocked:
            console.print("[bold yellow]Blocked modules (pending review):[/bold yellow]")
            for result in blocked:
                console.print(f"  [yellow]⏭[/yellow] {result.module_id}: {result.error}")
            console.print()

        # Output directory
        console.print(f"[cyan]Output directory:[/cyan] {output_dir}")
        console.print()

        # Performance stats
        if successful:
            avg_time = sum(r.processing_time for r in successful) / len(successful)
            console.print(f"[dim]Average processing time: {avg_time:.1f}s per module[/dim]")
            console.print()
