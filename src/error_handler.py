"""
Error Handling Framework for Student Handout Generator

Defines custom exception classes for each error category (Fatal, Blocking,
Recoverable, Informational) with proper error message formatting and context.
"""

from typing import Optional, Dict, Any
from enum import Enum


class ErrorSeverity(Enum):
    """Error severity levels."""
    FATAL = "FATAL"           # Critical - stop immediately, exit code 1
    BLOCKING = "BLOCKING"     # High - stop current module, continue batch
    RECOVERABLE = "RECOVERABLE"  # Medium - log warning, use fallback, continue
    INFORMATIONAL = "INFO"    # Low - log info, continue normally


class HandoutGeneratorError(Exception):
    """
    Base exception class for all handout generator errors.

    All error messages follow the format:
    [SEVERITY] [MODULE] Error description
      → Context: Additional details
      → Action: What the system did or what user should do
    """

    def __init__(
        self,
        message: str,
        severity: ErrorSeverity,
        module: str,
        context: Optional[str] = None,
        action: Optional[str] = None,
        original_error: Optional[Exception] = None
    ):
        """
        Initialize error.

        Args:
            message: Error description
            severity: Error severity level
            module: Module/component where error occurred
            context: Additional context details
            action: What system did or what user should do
            original_error: Original exception if this wraps another error
        """
        self.message = message
        self.severity = severity
        self.module = module
        self.context = context
        self.action = action
        self.original_error = original_error

        # Format full error message
        self.formatted_message = self._format_message()
        super().__init__(self.formatted_message)

    def _format_message(self) -> str:
        """Format error message according to PRD specification."""
        parts = [f"[{self.severity.value}] [{self.module}] {self.message}"]

        if self.context:
            parts.append(f"  → Context: {self.context}")

        if self.action:
            parts.append(f"  → Action: {self.action}")

        if self.original_error:
            parts.append(f"  → Original Error: {str(self.original_error)}")

        return "\n".join(parts)

    def to_dict(self) -> Dict[str, Any]:
        """Convert error to dictionary for logging/serialization."""
        return {
            "severity": self.severity.value,
            "module": self.module,
            "message": self.message,
            "context": self.context,
            "action": self.action,
            "original_error": str(self.original_error) if self.original_error else None
        }


# ============================================================================
# FATAL ERRORS - Stop immediately, exit code 1
# ============================================================================

class FatalError(HandoutGeneratorError):
    """Base class for fatal errors that stop execution immediately."""

    def __init__(
        self,
        message: str,
        module: str,
        context: Optional[str] = None,
        action: Optional[str] = None,
        original_error: Optional[Exception] = None
    ):
        super().__init__(
            message=message,
            severity=ErrorSeverity.FATAL,
            module=module,
            context=context,
            action=action,
            original_error=original_error
        )


class ConfigurationError(FatalError):
    """Missing or invalid configuration."""

    def __init__(self, message: str, context: Optional[str] = None, action: Optional[str] = None):
        super().__init__(
            message=message,
            module="ConfigManager",
            context=context,
            action=action or "Fix configuration file and try again"
        )


class APIAuthenticationError(FatalError):
    """API authentication failed."""

    def __init__(self, api_provider: str, context: Optional[str] = None):
        super().__init__(
            message=f"API authentication failed for {api_provider}",
            module="QuestionGenerator",
            context=context or "Check API key is valid and not expired",
            action=f"Set valid API key in environment variable or configuration"
        )


class MissingAPIKeyError(FatalError):
    """API key not set in environment."""

    def __init__(self, env_var_name: str):
        super().__init__(
            message=f"API key environment variable not set: {env_var_name}",
            module="QuestionGenerator",
            context="AI question generation requires valid API credentials",
            action=f"Set environment variable: export {env_var_name}=your-api-key"
        )


class DependencyMissingError(FatalError):
    """Required dependency not installed."""

    def __init__(self, dependency: str, install_command: str):
        super().__init__(
            message=f"Required dependency not installed: {dependency}",
            module="System",
            context="This tool is required for PDF generation",
            action=f"Install dependency: {install_command}"
        )


class FileNotFoundError(FatalError):
    """Required file not found."""

    def __init__(self, file_path: str, file_type: str = "file"):
        super().__init__(
            message=f"{file_type.capitalize()} not found: {file_path}",
            module="FileSystem",
            context=f"The specified {file_type} does not exist",
            action=f"Check the path and ensure the {file_type} exists"
        )


class InvalidEncodingError(FatalError):
    """File has invalid UTF-8 encoding."""

    def __init__(self, file_path: str):
        super().__init__(
            message=f"Invalid UTF-8 encoding in file: {file_path}",
            module="FrameworkParser",
            context="File must be UTF-8 encoded",
            action="Convert file to UTF-8 encoding and try again"
        )


class OutputDirectoryError(FatalError):
    """Output directory not writable."""

    def __init__(self, directory: str):
        super().__init__(
            message=f"Output directory not writable: {directory}",
            module="PDFRenderer",
            context="Cannot write output files to the specified directory",
            action="Check directory exists and has write permissions"
        )


# ============================================================================
# BLOCKING ERRORS - Stop current module, continue batch
# ============================================================================

class BlockingError(HandoutGeneratorError):
    """Base class for errors that block current module but allow batch to continue."""

    def __init__(
        self,
        message: str,
        module: str,
        context: Optional[str] = None,
        action: Optional[str] = None,
        original_error: Optional[Exception] = None
    ):
        super().__init__(
            message=message,
            severity=ErrorSeverity.BLOCKING,
            module=module,
            context=context,
            action=action,
            original_error=original_error
        )


class UnreviewedQuestionsError(BlockingError):
    """Questions pending review - blocks generation."""

    def __init__(self, module_id: str, pending_count: int):
        super().__init__(
            message=f"Unreviewed questions exist for module: {module_id}",
            module="QuestionReviewer",
            context=f"{pending_count} questions pending review",
            action=f"Review questions: python generate_handout.py --review-questions {module_id}"
        )


class MissingMetadataError(BlockingError):
    """Required metadata missing from framework file."""

    def __init__(self, file_path: str, missing_fields: list):
        super().__init__(
            message=f"Missing required metadata fields",
            module="FrameworkParser",
            context=f"File: {file_path}, Missing: {', '.join(missing_fields)}",
            action="Add required metadata to framework file YAML frontmatter"
        )


class FileSizeExceededError(BlockingError):
    """File exceeds maximum size limit."""

    def __init__(self, file_path: str, size_mb: float, max_mb: float):
        super().__init__(
            message=f"File exceeds size limit: {size_mb:.1f}MB > {max_mb}MB",
            module="FrameworkParser",
            context=f"File: {file_path}",
            action="Split file into smaller modules or increase size limit in config"
        )


class PDFGenerationError(BlockingError):
    """PDF generation failed."""

    def __init__(self, module_id: str, context: Optional[str] = None, original_error: Optional[Exception] = None):
        super().__init__(
            message=f"PDF generation failed for module: {module_id}",
            module="PDFRenderer",
            context=context,
            action="Check logs for detailed error. Verify WeasyPrint installation.",
            original_error=original_error
        )


class CorruptedFrameworkError(BlockingError):
    """Framework file is corrupted or malformed."""

    def __init__(self, file_path: str, reason: str):
        super().__init__(
            message=f"Corrupted or malformed framework file",
            module="FrameworkParser",
            context=f"File: {file_path}, Reason: {reason}",
            action="Fix markdown syntax errors and try again"
        )


# ============================================================================
# RECOVERABLE ERRORS - Log warning, use fallback, continue
# ============================================================================

class RecoverableError(HandoutGeneratorError):
    """Base class for recoverable errors with fallback behavior."""

    def __init__(
        self,
        message: str,
        module: str,
        context: Optional[str] = None,
        action: Optional[str] = None,
        original_error: Optional[Exception] = None
    ):
        super().__init__(
            message=message,
            severity=ErrorSeverity.RECOVERABLE,
            module=module,
            context=context,
            action=action,
            original_error=original_error
        )


class ImageNotFoundError(RecoverableError):
    """Image file not found - use placeholder."""

    def __init__(self, image_path: str, section: str):
        super().__init__(
            message=f"Image not found: {image_path}",
            module="ImageProcessor",
            context=f"Section: {section}",
            action="Using placeholder image. Add image file or update markdown reference."
        )


class UnsupportedImageFormatError(RecoverableError):
    """Image format not supported."""

    def __init__(self, image_path: str, format: str):
        super().__init__(
            message=f"Unsupported image format: {format}",
            module="ImageProcessor",
            context=f"File: {image_path}",
            action="Skipping image. Convert to PNG, JPG, or SVG."
        )


class CorruptedImageError(RecoverableError):
    """Image file is corrupted."""

    def __init__(self, image_path: str):
        super().__init__(
            message=f"Corrupted image file: {image_path}",
            module="ImageProcessor",
            context="Cannot read or process image",
            action="Using placeholder. Replace with valid image file."
        )


class ImageTooLargeError(RecoverableError):
    """Image file exceeds size limit."""

    def __init__(self, image_path: str, size_mb: float, max_mb: float = 10):
        super().__init__(
            message=f"Image too large: {size_mb:.1f}MB > {max_mb}MB",
            module="ImageProcessor",
            context=f"File: {image_path}",
            action="Skipping image. Compress or resize image."
        )


class APITimeoutError(RecoverableError):
    """API request timed out."""

    def __init__(self, retry_count: int, max_retries: int):
        super().__init__(
            message=f"API request timed out (attempt {retry_count}/{max_retries})",
            module="QuestionGenerator",
            context="Network or API service issue",
            action="Retrying with exponential backoff" if retry_count < max_retries else "Using cached questions"
        )


class APIRateLimitError(RecoverableError):
    """API rate limit exceeded."""

    def __init__(self, retry_after: Optional[int] = None):
        super().__init__(
            message="API rate limit exceeded",
            module="QuestionGenerator",
            context=f"Retry after {retry_after} seconds" if retry_after else "Rate limit hit",
            action="Applying exponential backoff and retrying"
        )


class InvalidAPIResponseError(RecoverableError):
    """API returned invalid response."""

    def __init__(self, context: str):
        super().__init__(
            message="Invalid API response received",
            module="QuestionGenerator",
            context=context,
            action="Retrying once, then skipping section"
        )


class MalformedMarkdownError(RecoverableError):
    """Markdown syntax error - attempt best-effort parse."""

    def __init__(self, file_path: str, line_number: Optional[int] = None):
        super().__init__(
            message="Malformed markdown syntax detected",
            module="FrameworkParser",
            context=f"File: {file_path}" + (f", Line: {line_number}" if line_number else ""),
            action="Attempting best-effort parsing"
        )


class FontNotFoundError(RecoverableError):
    """Font file not found - fall back to system font."""

    def __init__(self, font_name: str):
        super().__init__(
            message=f"Font not found: {font_name}",
            module="PDFRenderer",
            context="Font file missing or not installed",
            action="Falling back to system default font"
        )


# ============================================================================
# INFORMATIONAL - Log info, continue normally
# ============================================================================

class InformationalError(HandoutGeneratorError):
    """Base class for informational messages."""

    def __init__(
        self,
        message: str,
        module: str,
        context: Optional[str] = None,
        action: Optional[str] = None
    ):
        super().__init__(
            message=message,
            severity=ErrorSeverity.INFORMATIONAL,
            module=module,
            context=context,
            action=action or "No action required"
        )


class EmptySectionWarning(InformationalError):
    """Section is empty - skipped."""

    def __init__(self, section_title: str):
        super().__init__(
            message=f"Empty section skipped: {section_title}",
            module="ContentTransformer",
            context="Section has no content",
            action="Continuing with next section"
        )


class UnusedConfigOptionWarning(InformationalError):
    """Configuration option not used."""

    def __init__(self, option_name: str):
        super().__init__(
            message=f"Unused configuration option: {option_name}",
            module="ConfigManager",
            context="This option has no effect in current version",
            action="Ignoring option and continuing"
        )


class CachedQuestionsUsedInfo(InformationalError):
    """Using cached questions instead of generating new ones."""

    def __init__(self, module_id: str, question_count: int):
        super().__init__(
            message=f"Using cached approved questions for module: {module_id}",
            module="QuestionGenerator",
            context=f"{question_count} questions loaded from approved bank",
            action="Continuing with cached questions"
        )


# ============================================================================
# EXIT CODES
# ============================================================================

class ExitCode:
    """Exit codes for the application."""
    SUCCESS = 0                # Success (all modules generated)
    FATAL_ERROR = 1           # Fatal error (system cannot proceed)
    PARTIAL_SUCCESS = 2       # Partial success (some modules failed in batch)
    BLOCKED_BY_REVIEW = 3     # Blocked by review (unreviewed questions)
    CONFIGURATION_ERROR = 4   # Configuration error
