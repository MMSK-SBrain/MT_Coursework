"""
Security Utilities for Student Handout Generator

Provides input validation, path security, and sanitization utilities
to prevent path traversal, malicious input, and other security issues.
"""

import re
import os
from pathlib import Path
from typing import Optional, List
from urllib.parse import urlparse


class SecurityValidator:
    """
    Security validation utilities for file paths, markdown content, and inputs.
    """

    # Suspicious patterns to reject
    SUSPICIOUS_PATTERNS = [
        r'\.\./\.\.',           # Path traversal
        r'\.\.',                # Double dots
        r'/etc/passwd',         # System files
        r'/proc/',              # System directories
        r'file://',             # File URLs
        r'javascript:',         # JavaScript URLs
        r'<script',             # Script tags
        r'eval\(',              # Eval calls
        r'exec\(',              # Exec calls
        r'__import__',          # Python imports
        r'subprocess',          # Subprocess calls
    ]

    # Allowed image extensions
    ALLOWED_IMAGE_EXTENSIONS = ['.png', '.jpg', '.jpeg', '.svg', '.gif']

    # Maximum file sizes (in bytes)
    MAX_MARKDOWN_SIZE = 5 * 1024 * 1024  # 5MB
    MAX_IMAGE_SIZE = 10 * 1024 * 1024     # 10MB

    @classmethod
    def validate_file_path(
        cls,
        file_path: str,
        base_directory: Optional[str] = None,
        must_exist: bool = False
    ) -> Path:
        """
        Validate file path and prevent path traversal attacks.

        Args:
            file_path: Path to validate
            base_directory: Base directory to restrict access to (optional)
            must_exist: Whether file must exist

        Returns:
            Validated Path object

        Raises:
            ValueError: If path is invalid or suspicious

        Example:
            >>> validator = SecurityValidator()
            >>> path = validator.validate_file_path("./frameworks/module-0.md", "/project")
            >>> print(path)
            /project/frameworks/module-0.md
        """
        if not file_path:
            raise ValueError("File path cannot be empty")

        # Convert to Path object
        path = Path(file_path).expanduser()

        # Check for suspicious patterns
        path_str = str(path)
        for pattern in cls.SUSPICIOUS_PATTERNS:
            if re.search(pattern, path_str, re.IGNORECASE):
                raise ValueError(
                    f"Suspicious pattern detected in path: {file_path}\n"
                    f"Pattern: {pattern}"
                )

        # Resolve to absolute path
        try:
            if base_directory:
                base = Path(base_directory).resolve()
                resolved_path = (base / path).resolve()
            else:
                resolved_path = path.resolve()
        except (OSError, RuntimeError) as e:
            raise ValueError(f"Cannot resolve path: {file_path}\nError: {str(e)}")

        # Verify path is within base directory (prevent traversal)
        if base_directory:
            base = Path(base_directory).resolve()
            try:
                resolved_path.relative_to(base)
            except ValueError:
                raise ValueError(
                    f"Path traversal detected: {file_path}\n"
                    f"Path must be within: {base_directory}\n"
                    f"Resolved to: {resolved_path}"
                )

        # Check if file exists (if required)
        if must_exist and not resolved_path.exists():
            raise ValueError(f"File does not exist: {resolved_path}")

        # Check if path points to a file (not directory) when it must exist
        if must_exist and resolved_path.exists() and not resolved_path.is_file():
            raise ValueError(f"Path is not a file: {resolved_path}")

        return resolved_path

    @classmethod
    def validate_directory_path(
        cls,
        directory_path: str,
        must_exist: bool = False,
        create_if_missing: bool = False
    ) -> Path:
        """
        Validate directory path.

        Args:
            directory_path: Directory path to validate
            must_exist: Whether directory must exist
            create_if_missing: Create directory if it doesn't exist

        Returns:
            Validated Path object

        Raises:
            ValueError: If path is invalid
        """
        if not directory_path:
            raise ValueError("Directory path cannot be empty")

        path = Path(directory_path).expanduser()

        # Check for suspicious patterns
        path_str = str(path)
        for pattern in cls.SUSPICIOUS_PATTERNS:
            if re.search(pattern, path_str, re.IGNORECASE):
                raise ValueError(f"Suspicious pattern detected in path: {directory_path}")

        # Resolve to absolute path
        try:
            resolved_path = path.resolve()
        except (OSError, RuntimeError) as e:
            raise ValueError(f"Cannot resolve directory path: {directory_path}\nError: {str(e)}")

        # Create if requested
        if create_if_missing and not resolved_path.exists():
            try:
                resolved_path.mkdir(parents=True, exist_ok=True)
            except OSError as e:
                raise ValueError(f"Cannot create directory: {resolved_path}\nError: {str(e)}")

        # Check if exists (if required)
        if must_exist and not resolved_path.exists():
            raise ValueError(f"Directory does not exist: {resolved_path}")

        # Verify it's a directory
        if resolved_path.exists() and not resolved_path.is_dir():
            raise ValueError(f"Path is not a directory: {resolved_path}")

        return resolved_path

    @classmethod
    def validate_image_path(
        cls,
        image_path: str,
        base_directory: Optional[str] = None
    ) -> tuple[Path, bool]:
        """
        Validate image file path and extension.

        Args:
            image_path: Image path to validate
            base_directory: Base directory to restrict access to

        Returns:
            Tuple of (validated path, exists flag)

        Raises:
            ValueError: If path is invalid or extension not allowed
        """
        if not image_path:
            raise ValueError("Image path cannot be empty")

        # Validate as file path
        try:
            path = cls.validate_file_path(image_path, base_directory, must_exist=False)
        except ValueError as e:
            raise ValueError(f"Invalid image path: {str(e)}")

        # Check extension
        extension = path.suffix.lower()
        if extension not in cls.ALLOWED_IMAGE_EXTENSIONS:
            raise ValueError(
                f"Image extension not allowed: {extension}\n"
                f"Allowed extensions: {', '.join(cls.ALLOWED_IMAGE_EXTENSIONS)}"
            )

        # Check if exists
        exists = path.exists()

        # If exists, validate size
        if exists:
            size = path.stat().st_size
            if size > cls.MAX_IMAGE_SIZE:
                raise ValueError(
                    f"Image too large: {size / (1024 * 1024):.1f}MB > "
                    f"{cls.MAX_IMAGE_SIZE / (1024 * 1024):.0f}MB\n"
                    f"File: {path}"
                )

        return path, exists

    @classmethod
    def sanitize_markdown(cls, markdown_content: str) -> str:
        """
        Sanitize markdown content by removing potentially dangerous HTML/JS.

        Args:
            markdown_content: Markdown content to sanitize

        Returns:
            Sanitized markdown content

        Example:
            >>> content = "# Title\\n<script>alert('xss')</script>\\nParagraph"
            >>> safe = SecurityValidator.sanitize_markdown(content)
            >>> print(safe)
            # Title
            <!-- REMOVED: script -->
            Paragraph
        """
        if not markdown_content:
            return markdown_content

        # Remove script tags
        sanitized = re.sub(
            r'<script[^>]*>.*?</script>',
            '<!-- REMOVED: script -->',
            markdown_content,
            flags=re.IGNORECASE | re.DOTALL
        )

        # Remove event handlers (onclick, onerror, etc.)
        sanitized = re.sub(
            r'\s+on\w+\s*=\s*["\'][^"\']*["\']',
            '',
            sanitized,
            flags=re.IGNORECASE
        )

        # Remove javascript: URLs
        sanitized = re.sub(
            r'javascript:',
            'removed-javascript:',
            sanitized,
            flags=re.IGNORECASE
        )

        # Remove data: URLs (can contain base64 encoded scripts)
        sanitized = re.sub(
            r'data:text/html[^"\')\s]*',
            'removed-data-url',
            sanitized,
            flags=re.IGNORECASE
        )

        return sanitized

    @classmethod
    def validate_markdown_file_size(cls, file_path: Path) -> None:
        """
        Validate markdown file size.

        Args:
            file_path: Path to markdown file

        Raises:
            ValueError: If file is too large
        """
        if not file_path.exists():
            raise ValueError(f"File does not exist: {file_path}")

        size = file_path.stat().st_size
        if size > cls.MAX_MARKDOWN_SIZE:
            raise ValueError(
                f"Markdown file too large: {size / (1024 * 1024):.1f}MB > "
                f"{cls.MAX_MARKDOWN_SIZE / (1024 * 1024):.0f}MB\n"
                f"File: {file_path}\n"
                f"Consider splitting into smaller modules"
            )

    @classmethod
    def sanitize_filename(cls, filename: str) -> str:
        """
        Sanitize filename by removing dangerous characters.

        Args:
            filename: Filename to sanitize

        Returns:
            Sanitized filename

        Example:
            >>> SecurityValidator.sanitize_filename("module-0../../etc/passwd.md")
            'module-0-etc-passwd.md'
        """
        if not filename:
            raise ValueError("Filename cannot be empty")

        # Remove path separators
        sanitized = filename.replace('/', '-').replace('\\', '-')

        # Remove null bytes
        sanitized = sanitized.replace('\x00', '')

        # Remove leading/trailing dots and spaces
        sanitized = sanitized.strip('. ')

        # Replace multiple dots with single dot
        sanitized = re.sub(r'\.{2,}', '.', sanitized)

        # Remove any remaining suspicious characters
        sanitized = re.sub(r'[<>:"|?*]', '', sanitized)

        # Ensure it's not empty after sanitization
        if not sanitized:
            raise ValueError("Filename becomes empty after sanitization")

        # Limit length
        if len(sanitized) > 255:
            name, ext = os.path.splitext(sanitized)
            sanitized = name[:255 - len(ext)] + ext

        return sanitized

    @classmethod
    def validate_module_id(cls, module_id: str) -> str:
        """
        Validate module ID format.

        Args:
            module_id: Module ID to validate (e.g., "module-0")

        Returns:
            Validated module ID

        Raises:
            ValueError: If module ID is invalid
        """
        if not module_id:
            raise ValueError("Module ID cannot be empty")

        # Check format: module-N or module-NN
        if not re.match(r'^module-\d{1,2}$', module_id):
            raise ValueError(
                f"Invalid module ID format: {module_id}\n"
                f"Expected format: 'module-N' (e.g., 'module-0', 'module-10')"
            )

        return module_id

    @classmethod
    def validate_url(cls, url: str, allowed_schemes: Optional[List[str]] = None) -> str:
        """
        Validate URL format and scheme.

        Args:
            url: URL to validate
            allowed_schemes: List of allowed URL schemes (default: ['http', 'https'])

        Returns:
            Validated URL

        Raises:
            ValueError: If URL is invalid or scheme not allowed
        """
        if not url:
            raise ValueError("URL cannot be empty")

        if allowed_schemes is None:
            allowed_schemes = ['http', 'https']

        try:
            parsed = urlparse(url)
        except Exception as e:
            raise ValueError(f"Invalid URL format: {url}\nError: {str(e)}")

        if parsed.scheme not in allowed_schemes:
            raise ValueError(
                f"URL scheme not allowed: {parsed.scheme}\n"
                f"Allowed schemes: {', '.join(allowed_schemes)}\n"
                f"URL: {url}"
            )

        return url

    @classmethod
    def validate_color_hex(cls, color: str) -> str:
        """
        Validate hex color code format.

        Args:
            color: Hex color code to validate (e.g., "#0D1117")

        Returns:
            Validated color code

        Raises:
            ValueError: If color code is invalid
        """
        if not color:
            raise ValueError("Color code cannot be empty")

        if not re.match(r'^#[0-9A-Fa-f]{6}$', color):
            raise ValueError(
                f"Invalid hex color code: {color}\n"
                f"Expected format: #RRGGBB (e.g., #0D1117)"
            )

        return color.upper()

    @classmethod
    def is_safe_path(cls, path: str, base_directory: str) -> bool:
        """
        Check if path is safe (within base directory).

        Args:
            path: Path to check
            base_directory: Base directory

        Returns:
            True if path is safe, False otherwise
        """
        try:
            cls.validate_file_path(path, base_directory, must_exist=False)
            return True
        except ValueError:
            return False

    @classmethod
    def get_safe_output_path(
        cls,
        output_dir: str,
        filename: str,
        extension: str = '.pdf'
    ) -> Path:
        """
        Get safe output file path.

        Args:
            output_dir: Output directory
            filename: Filename (will be sanitized)
            extension: File extension (default: .pdf)

        Returns:
            Safe output path

        Raises:
            ValueError: If paths are invalid
        """
        # Validate and create output directory
        output_path = cls.validate_directory_path(output_dir, create_if_missing=True)

        # Sanitize filename
        safe_filename = cls.sanitize_filename(filename)

        # Ensure extension
        if not safe_filename.endswith(extension):
            safe_filename += extension

        # Construct full path
        full_path = output_path / safe_filename

        return full_path
