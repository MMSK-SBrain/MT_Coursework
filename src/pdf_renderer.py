"""
PDF Renderer for Student Handout Generator

Converts HTML with dark theme CSS to professional PDF using WeasyPrint.
Handles font embedding, image embedding, page setup, headers/footers, and validation.

Story 7: PDF Renderer
Components: PDFRenderer, WeasyPrint integration
"""

import logging
from pathlib import Path
from typing import Optional, Dict, Any, List
import shutil
from datetime import datetime

from src.models import HandoutDocument
from src.error_handler import (
    ErrorSeverity,
    HandoutGeneratorError,
    FatalError,
    RecoverableError,
    FontNotFoundError
)

logger = logging.getLogger(__name__)


class PDFRendererError(HandoutGeneratorError):
    """PDF renderer specific errors"""
    def __init__(self, message: str, context: Optional[str] = None, action: Optional[str] = None):
        super().__init__(
            message=message,
            severity=ErrorSeverity.BLOCKING,
            module="PDFRenderer",
            context=context,
            action=action
        )


class PDFRenderer:
    """
    Renders HTML content to PDF using WeasyPrint with dark theme styling.

    Features:
    - Dark theme PDF generation
    - Font embedding (Inter, JetBrains Mono)
    - Image embedding
    - A4 page setup with configurable margins
    - Headers and footers with page numbers
    - PDF validation
    - Output directory management
    - Archive old versions

    Example:
        >>> config = {"pdf": {"margins": {"top": "20mm", ...}}, ...}
        >>> renderer = PDFRenderer(config)
        >>> pdf_path = renderer.render_to_pdf(
        ...     html_content="<html>...</html>",
        ...     css_content="body { background: #0D1117; }",
        ...     output_path=Path("handouts/module-0.pdf"),
        ...     module_title="Module 0: The Hook"
        ... )
    """

    def __init__(self, config: Dict[str, Any]):
        """
        Initialize PDF renderer with configuration.

        Args:
            config: Configuration dictionary with pdf, branding, global sections

        Raises:
            PDFRendererError: If WeasyPrint is not installed
        """
        self.config = config
        self.pdf_config = config.get("pdf", {})
        self.global_config = config.get("global", {})
        self.branding_config = config.get("branding", {})

        # Check WeasyPrint availability
        self._check_weasyprint()

        logger.info("PDFRenderer initialized")

    def _check_weasyprint(self) -> None:
        """
        Check if WeasyPrint is installed and importable.

        Raises:
            PDFRendererError: If WeasyPrint cannot be imported
        """
        try:
            import weasyprint
            logger.debug(f"WeasyPrint version: {weasyprint.__version__}")
        except ImportError as e:
            error_msg = (
                "WeasyPrint is not installed. Please install it using:\n"
                "  pip install weasyprint\n\n"
                "On macOS, you may also need system dependencies:\n"
                "  brew install pango gdk-pixbuf libffi"
            )
            logger.error(error_msg)
            raise FatalError(
                message="WeasyPrint is not installed",
                module="PDFRenderer",
                context=str(e),
                action="Install WeasyPrint: pip install weasyprint"
            ) from e

    def render_to_pdf(
        self,
        html_content: str,
        css_content: Optional[str] = None,
        output_path: Optional[Path] = None,
        module_title: str = "Student Handout",
        metadata: Optional[Dict[str, str]] = None,
        base_url: Optional[str] = None
    ) -> Path:
        """
        Render HTML content to PDF file.

        Args:
            html_content: Complete HTML content as string
            css_content: CSS stylesheet content (optional, can be embedded in HTML)
            output_path: Path for output PDF file (auto-generated if None)
            module_title: Module title for headers
            metadata: PDF metadata (title, author, subject, keywords)
            base_url: Base URL for resolving relative paths (default: current directory)

        Returns:
            Path to generated PDF file

        Raises:
            PDFRendererError: If PDF generation fails
        """
        try:
            from weasyprint import HTML, CSS

            # Generate output path if not provided
            if output_path is None:
                output_path = self._generate_output_path(module_title)
            else:
                output_path = Path(output_path)

            # Ensure output directory exists
            output_path.parent.mkdir(parents=True, exist_ok=True)

            # Archive old version if it exists
            if output_path.exists() and self.global_config.get("archive_old_versions", True):
                self._archive_old_version(output_path)

            # Prepare base URL for resolving relative paths (images, fonts)
            if base_url is None:
                base_url = str(Path.cwd())

            logger.info(f"Rendering PDF: {output_path}")
            logger.debug(f"HTML length: {len(html_content)} chars")
            logger.debug(f"CSS provided: {css_content is not None}")
            logger.debug(f"Base URL: {base_url}")

            # Create HTML object
            html_obj = HTML(string=html_content, base_url=base_url)

            # Prepare stylesheets
            stylesheets = []
            if css_content:
                stylesheets.append(CSS(string=css_content))

            # Generate PDF
            pdf_bytes = html_obj.write_pdf(
                stylesheets=stylesheets,
                **self._get_pdf_options(metadata)
            )

            # Write PDF to file
            output_path.write_bytes(pdf_bytes)

            # Validate PDF output
            self._validate_pdf(output_path)

            logger.info(f"PDF generated successfully: {output_path}")
            logger.info(f"PDF size: {output_path.stat().st_size / 1024:.2f} KB")

            return output_path

        except ImportError as e:
            # This shouldn't happen because we check in __init__, but just in case
            raise PDFRendererError("WeasyPrint is not available") from e
        except Exception as e:
            error_msg = f"PDF generation failed: {str(e)}"
            logger.error(error_msg, exc_info=True)
            raise PDFRendererError(
                message=error_msg,
                context=f"Output path: {output_path}, Error type: {type(e).__name__}",
                action="Check HTML/CSS syntax and file paths"
            ) from e

    def _get_pdf_options(self, metadata: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
        """
        Get PDF generation options including metadata.

        Args:
            metadata: PDF metadata dictionary

        Returns:
            Dictionary of options for WeasyPrint
        """
        options = {}

        # Add PDF metadata
        if metadata:
            # WeasyPrint accepts metadata in the HTML <meta> tags
            # So we don't need to pass it here separately
            pass

        return options

    def _generate_output_path(self, module_title: str) -> Path:
        """
        Generate output path based on module title and configuration.

        Args:
            module_title: Module title (e.g., "Module 0: The Hook")

        Returns:
            Generated output path
        """
        output_dir = Path(self.global_config.get("output_directory", "./handouts"))

        # Extract module number from title (e.g., "Module 0" -> "0")
        import re
        match = re.search(r'[Mm]odule[- ](\d+)', module_title)
        if match:
            module_num = match.group(1)
            # Format: {course-code}-module-{N}-handout.pdf
            # We don't have course code here, so use generic name
            filename = f"module-{module_num}-handout.pdf"
        else:
            # Fallback: sanitize title
            filename = re.sub(r'[^\w\s-]', '', module_title.lower())
            filename = re.sub(r'[-\s]+', '-', filename)
            filename = f"{filename}-handout.pdf"

        return output_dir / filename

    def _archive_old_version(self, pdf_path: Path) -> None:
        """
        Archive old version of PDF before overwriting.

        Args:
            pdf_path: Path to PDF file to archive
        """
        try:
            archive_dir = pdf_path.parent / "archive"
            archive_dir.mkdir(exist_ok=True)

            # Add timestamp to archived filename
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            archive_name = f"{pdf_path.stem}_{timestamp}{pdf_path.suffix}"
            archive_path = archive_dir / archive_name

            shutil.copy2(pdf_path, archive_path)
            logger.info(f"Archived old version: {archive_path}")

        except Exception as e:
            # Log warning but don't fail
            logger.warning(f"Failed to archive old version: {e}")
            logger.warning(f"Could not archive old PDF {pdf_path}: {str(e)}")

    def _validate_pdf(self, pdf_path: Path) -> None:
        """
        Validate generated PDF file.

        Args:
            pdf_path: Path to PDF file to validate

        Raises:
            PDFRendererError: If validation fails
        """
        # Check file exists
        if not pdf_path.exists():
            raise PDFRendererError(f"PDF file was not created: {pdf_path}")

        # Check file size
        file_size = pdf_path.stat().st_size
        if file_size == 0:
            raise PDFRendererError(f"PDF file is empty: {pdf_path}")

        # Check file size limit (10MB)
        max_size = 10 * 1024 * 1024  # 10MB in bytes
        if file_size > max_size:
            warning = f"PDF file exceeds recommended size: {file_size / 1024 / 1024:.2f}MB > 10MB"
            logger.warning(warning)

        # Try to read PDF header (basic validation)
        try:
            with open(pdf_path, 'rb') as f:
                header = f.read(5)
                if not header.startswith(b'%PDF-'):
                    raise PDFRendererError(f"Invalid PDF header in file: {pdf_path}")
        except Exception as e:
            raise PDFRendererError(f"Cannot read PDF file: {e}")

        logger.debug(f"PDF validation passed: {pdf_path}")

    def render_handout(
        self,
        html_content: str,
        css_path: Optional[Path] = None,
        course_code: str = "COURSE",
        module_number: int = 0,
        module_title: str = "Module",
        output_dir: Optional[Path] = None
    ) -> Path:
        """
        Render complete handout with standard naming convention.

        This is a convenience method that follows the naming convention:
        {course-code}-module-{N}-handout.pdf

        Args:
            html_content: Complete HTML content
            css_path: Path to CSS file (optional, can be embedded in HTML)
            course_code: Course code (e.g., "ML-ENG")
            module_number: Module number (e.g., 0)
            module_title: Module title for headers
            output_dir: Output directory (uses config default if None)

        Returns:
            Path to generated PDF file
        """
        # Load CSS if path provided
        css_content = None
        if css_path and css_path.exists():
            css_content = css_path.read_text(encoding='utf-8')
            logger.debug(f"Loaded CSS from: {css_path}")

        # Generate output path with standard naming
        if output_dir is None:
            output_dir = Path(self.global_config.get("output_directory", "./handouts"))

        filename = f"{course_code}-module-{module_number}-handout.pdf"
        output_path = output_dir / filename

        # Prepare metadata
        metadata = {
            "title": f"{course_code} - Module {module_number}: {module_title}",
            "author": "Course Generator",
            "subject": f"Student Handout - Module {module_number}",
            "keywords": f"{course_code}, Module {module_number}, Student Handout"
        }

        return self.render_to_pdf(
            html_content=html_content,
            css_content=css_content,
            output_path=output_path,
            module_title=module_title,
            metadata=metadata
        )

    def get_font_status(self) -> Dict[str, Any]:
        """
        Check font availability status.

        Returns:
            Dictionary with font status information:
            {
                "inter": {"available": bool, "path": str|None},
                "jetbrains_mono": {"available": bool, "path": str|None},
                "fallback_fonts": List[str]
            }
        """
        status = {
            "inter": {"available": False, "path": None},
            "jetbrains_mono": {"available": False, "path": None},
            "fallback_fonts": []
        }

        # Check for fonts in assets/fonts directory
        fonts_dir = Path("assets/fonts")
        if fonts_dir.exists():
            # Check for Inter
            inter_files = list(fonts_dir.glob("Inter*.ttf"))
            if inter_files:
                status["inter"]["available"] = True
                status["inter"]["path"] = str(inter_files[0])

            # Check for JetBrains Mono
            jetbrains_files = list(fonts_dir.glob("JetBrainsMono*.ttf"))
            if jetbrains_files:
                status["jetbrains_mono"]["available"] = True
                status["jetbrains_mono"]["path"] = str(jetbrains_files[0])

        # Check system fonts as fallback
        system_fonts = ["Arial", "Helvetica", "Courier", "monospace", "sans-serif"]
        status["fallback_fonts"] = system_fonts

        return status

    def check_write_permissions(self, output_path: Path) -> bool:
        """
        Check if output directory is writable.

        Args:
            output_path: Path to check for write permissions

        Returns:
            True if writable, False otherwise
        """
        try:
            output_dir = output_path.parent
            output_dir.mkdir(parents=True, exist_ok=True)

            # Try to create a test file
            test_file = output_dir / ".write_test"
            test_file.write_text("test")
            test_file.unlink()

            return True

        except Exception as e:
            logger.error(f"Output directory not writable: {e}")
            logger.error(f"Output directory is not writable: {output_dir}")
            return False
