"""
Unit tests for Security Utilities

Tests input validation, path security, and sanitization functions.
"""

import pytest
from pathlib import Path
import tempfile
import os

# Add parent directory to path to import src modules
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.security import SecurityValidator


class TestSecurityValidator:
    """Test suite for SecurityValidator"""

    # ========================================================================
    # File Path Validation Tests
    # ========================================================================

    def test_validate_simple_file_path(self, tmp_path):
        """Test validating a simple file path"""
        test_file = tmp_path / "test.md"
        test_file.write_text("content")

        validated_path = SecurityValidator.validate_file_path(
            str(test_file),
            base_directory=str(tmp_path),
            must_exist=True
        )

        assert validated_path.exists()
        assert validated_path.is_file()

    def test_validate_file_path_prevents_traversal(self, tmp_path):
        """Test that path traversal is prevented"""
        with pytest.raises(ValueError) as exc_info:
            SecurityValidator.validate_file_path(
                "../../../etc/passwd",
                base_directory=str(tmp_path)
            )
        # Can detect either via suspicious pattern or path traversal check
        assert ("Path traversal detected" in str(exc_info.value) or
                "Suspicious pattern detected" in str(exc_info.value))

    def test_validate_file_path_suspicious_patterns(self):
        """Test detection of suspicious patterns"""
        suspicious_paths = [
            "../../../etc/passwd",
            "/proc/self/environ",
            "file:///etc/passwd",
            "javascript:alert('xss')"
        ]

        for path in suspicious_paths:
            with pytest.raises(ValueError) as exc_info:
                SecurityValidator.validate_file_path(path)
            assert "Suspicious pattern detected" in str(exc_info.value)

    def test_validate_file_path_empty(self):
        """Test error for empty file path"""
        with pytest.raises(ValueError) as exc_info:
            SecurityValidator.validate_file_path("")
        assert "File path cannot be empty" in str(exc_info.value)

    def test_validate_file_must_exist(self, tmp_path):
        """Test error when file must exist but doesn't"""
        with pytest.raises(ValueError) as exc_info:
            SecurityValidator.validate_file_path(
                "nonexistent.txt",
                base_directory=str(tmp_path),
                must_exist=True
            )
        assert "File does not exist" in str(exc_info.value)

    def test_validate_file_path_relative(self, tmp_path):
        """Test validating relative file path"""
        test_file = tmp_path / "subdir" / "test.md"
        test_file.parent.mkdir(parents=True)
        test_file.write_text("content")

        validated_path = SecurityValidator.validate_file_path(
            "subdir/test.md",
            base_directory=str(tmp_path),
            must_exist=True
        )

        assert validated_path.exists()

    # ========================================================================
    # Directory Path Validation Tests
    # ========================================================================

    def test_validate_directory_path(self, tmp_path):
        """Test validating a directory path"""
        test_dir = tmp_path / "testdir"
        test_dir.mkdir()

        validated_path = SecurityValidator.validate_directory_path(
            str(test_dir),
            must_exist=True
        )

        assert validated_path.exists()
        assert validated_path.is_dir()

    def test_validate_directory_create_if_missing(self, tmp_path):
        """Test creating directory if it doesn't exist"""
        test_dir = tmp_path / "newdir"

        validated_path = SecurityValidator.validate_directory_path(
            str(test_dir),
            create_if_missing=True
        )

        assert validated_path.exists()
        assert validated_path.is_dir()

    def test_validate_directory_empty_path(self):
        """Test error for empty directory path"""
        with pytest.raises(ValueError) as exc_info:
            SecurityValidator.validate_directory_path("")
        assert "Directory path cannot be empty" in str(exc_info.value)

    def test_validate_directory_not_a_directory(self, tmp_path):
        """Test error when path is not a directory"""
        test_file = tmp_path / "file.txt"
        test_file.write_text("content")

        with pytest.raises(ValueError) as exc_info:
            SecurityValidator.validate_directory_path(str(test_file))
        assert "Path is not a directory" in str(exc_info.value)

    # ========================================================================
    # Image Path Validation Tests
    # ========================================================================

    def test_validate_image_path_valid(self, tmp_path):
        """Test validating a valid image path"""
        test_image = tmp_path / "test.png"
        test_image.write_bytes(b"fake png data")

        validated_path, exists = SecurityValidator.validate_image_path(
            str(test_image),
            base_directory=str(tmp_path)
        )

        assert validated_path.suffix == ".png"
        assert exists is True

    def test_validate_image_path_nonexistent(self, tmp_path):
        """Test validating nonexistent image"""
        validated_path, exists = SecurityValidator.validate_image_path(
            "nonexistent.jpg",
            base_directory=str(tmp_path)
        )

        assert validated_path.suffix == ".jpg"
        assert exists is False

    def test_validate_image_path_invalid_extension(self, tmp_path):
        """Test error for invalid image extension"""
        with pytest.raises(ValueError) as exc_info:
            SecurityValidator.validate_image_path(
                "file.exe",
                base_directory=str(tmp_path)
            )
        assert "Image extension not allowed" in str(exc_info.value)

    def test_validate_image_path_empty(self):
        """Test error for empty image path"""
        with pytest.raises(ValueError) as exc_info:
            SecurityValidator.validate_image_path("")
        assert "Image path cannot be empty" in str(exc_info.value)

    def test_validate_image_path_all_extensions(self, tmp_path):
        """Test all allowed image extensions"""
        allowed_extensions = ['.png', '.jpg', '.jpeg', '.svg', '.gif']

        for ext in allowed_extensions:
            test_image = tmp_path / f"image{ext}"
            test_image.write_bytes(b"fake image data")

            validated_path, exists = SecurityValidator.validate_image_path(
                str(test_image),
                base_directory=str(tmp_path)
            )

            assert validated_path.suffix == ext
            assert exists is True

    # ========================================================================
    # Markdown Sanitization Tests
    # ========================================================================

    def test_sanitize_markdown_script_tags(self):
        """Test removal of script tags"""
        markdown = "# Title\n<script>alert('xss')</script>\nContent"
        sanitized = SecurityValidator.sanitize_markdown(markdown)

        assert "<script" not in sanitized
        assert "alert" not in sanitized
        assert "REMOVED: script" in sanitized
        assert "# Title" in sanitized
        assert "Content" in sanitized

    def test_sanitize_markdown_event_handlers(self):
        """Test removal of event handlers"""
        markdown = '<img src="image.png" onclick="alert(\'xss\')" />'
        sanitized = SecurityValidator.sanitize_markdown(markdown)

        assert "onclick" not in sanitized

    def test_sanitize_markdown_javascript_urls(self):
        """Test removal of javascript: URLs"""
        markdown = '[Click](javascript:alert("xss"))'
        sanitized = SecurityValidator.sanitize_markdown(markdown)

        # javascript: should be replaced with removed-javascript:
        assert markdown != sanitized  # Content changed
        assert "removed-javascript:" in sanitized
        # Original javascript: URL should not work
        assert '[Click](javascript:' not in sanitized

    def test_sanitize_markdown_data_urls(self):
        """Test removal of data: URLs"""
        markdown = '<img src="data:text/html,<script>alert(\'xss\')</script>" />'
        sanitized = SecurityValidator.sanitize_markdown(markdown)

        assert "data:text/html" not in sanitized
        assert "removed-data-url" in sanitized

    def test_sanitize_markdown_empty(self):
        """Test sanitizing empty markdown"""
        assert SecurityValidator.sanitize_markdown("") == ""
        assert SecurityValidator.sanitize_markdown(None) is None

    def test_sanitize_markdown_safe_content(self):
        """Test that safe content is not modified"""
        markdown = "# Title\n\nSafe **bold** and *italic* text.\n\n- List item"
        sanitized = SecurityValidator.sanitize_markdown(markdown)

        assert sanitized == markdown

    # ========================================================================
    # File Size Validation Tests
    # ========================================================================

    def test_validate_markdown_file_size_valid(self, tmp_path):
        """Test validating file size within limit"""
        test_file = tmp_path / "test.md"
        test_file.write_text("x" * 1000)  # 1KB file

        # Should not raise
        SecurityValidator.validate_markdown_file_size(test_file)

    def test_validate_markdown_file_size_too_large(self, tmp_path):
        """Test error for file exceeding size limit"""
        test_file = tmp_path / "large.md"
        # Create file larger than 5MB
        test_file.write_bytes(b"x" * (6 * 1024 * 1024))

        with pytest.raises(ValueError) as exc_info:
            SecurityValidator.validate_markdown_file_size(test_file)
        assert "Markdown file too large" in str(exc_info.value)

    def test_validate_markdown_file_size_nonexistent(self, tmp_path):
        """Test error for nonexistent file"""
        with pytest.raises(ValueError) as exc_info:
            SecurityValidator.validate_markdown_file_size(tmp_path / "nonexistent.md")
        assert "File does not exist" in str(exc_info.value)

    # ========================================================================
    # Filename Sanitization Tests
    # ========================================================================

    def test_sanitize_filename_basic(self):
        """Test basic filename sanitization"""
        filename = "module-0-framework.md"
        sanitized = SecurityValidator.sanitize_filename(filename)
        assert sanitized == filename

    def test_sanitize_filename_path_separators(self):
        """Test removal of path separators"""
        filename = "path/to/file.md"
        sanitized = SecurityValidator.sanitize_filename(filename)
        assert "/" not in sanitized
        assert sanitized == "path-to-file.md"

    def test_sanitize_filename_traversal(self):
        """Test sanitization of path traversal attempts"""
        filename = "../../../etc/passwd"
        sanitized = SecurityValidator.sanitize_filename(filename)
        assert ".." not in sanitized
        assert "/" not in sanitized

    def test_sanitize_filename_dangerous_characters(self):
        """Test removal of dangerous characters"""
        filename = 'file<>:"|?*.txt'
        sanitized = SecurityValidator.sanitize_filename(filename)
        assert "<" not in sanitized
        assert ">" not in sanitized
        assert "|" not in sanitized
        assert "?" not in sanitized

    def test_sanitize_filename_empty(self):
        """Test error for empty filename"""
        with pytest.raises(ValueError) as exc_info:
            SecurityValidator.sanitize_filename("")
        assert "Filename cannot be empty" in str(exc_info.value)

    def test_sanitize_filename_null_bytes(self):
        """Test removal of null bytes"""
        filename = "file\x00name.txt"
        sanitized = SecurityValidator.sanitize_filename(filename)
        assert "\x00" not in sanitized

    def test_sanitize_filename_length_limit(self):
        """Test filename length limiting"""
        filename = "a" * 300 + ".txt"
        sanitized = SecurityValidator.sanitize_filename(filename)
        assert len(sanitized) <= 255

    # ========================================================================
    # Module ID Validation Tests
    # ========================================================================

    def test_validate_module_id_valid(self):
        """Test validating valid module IDs"""
        valid_ids = ["module-0", "module-1", "module-10", "module-99"]

        for module_id in valid_ids:
            validated = SecurityValidator.validate_module_id(module_id)
            assert validated == module_id

    def test_validate_module_id_invalid(self):
        """Test error for invalid module IDs"""
        invalid_ids = ["module", "module-", "module-abc", "mod-0"]

        for module_id in invalid_ids:
            with pytest.raises(ValueError) as exc_info:
                SecurityValidator.validate_module_id(module_id)
            assert "Invalid module ID format" in str(exc_info.value)

        # Empty string has different error message
        with pytest.raises(ValueError) as exc_info:
            SecurityValidator.validate_module_id("")
        assert "Module ID cannot be empty" in str(exc_info.value)

    # ========================================================================
    # URL Validation Tests
    # ========================================================================

    def test_validate_url_valid(self):
        """Test validating valid URLs"""
        valid_urls = [
            "https://example.com",
            "http://example.com/path",
            "https://example.com/path?query=value"
        ]

        for url in valid_urls:
            validated = SecurityValidator.validate_url(url)
            assert validated == url

    def test_validate_url_invalid_scheme(self):
        """Test error for invalid URL scheme"""
        with pytest.raises(ValueError) as exc_info:
            SecurityValidator.validate_url("ftp://example.com")
        assert "URL scheme not allowed" in str(exc_info.value)

    def test_validate_url_javascript(self):
        """Test error for javascript: URLs"""
        with pytest.raises(ValueError) as exc_info:
            SecurityValidator.validate_url("javascript:alert('xss')")
        assert "URL scheme not allowed" in str(exc_info.value)

    def test_validate_url_empty(self):
        """Test error for empty URL"""
        with pytest.raises(ValueError) as exc_info:
            SecurityValidator.validate_url("")
        assert "URL cannot be empty" in str(exc_info.value)

    # ========================================================================
    # Color Hex Validation Tests
    # ========================================================================

    def test_validate_color_hex_valid(self):
        """Test validating valid hex colors"""
        valid_colors = ["#0D1117", "#E6EDF3", "#58A6FF", "#000000", "#FFFFFF"]

        for color in valid_colors:
            validated = SecurityValidator.validate_color_hex(color)
            assert validated == color.upper()

    def test_validate_color_hex_invalid(self):
        """Test error for invalid hex colors"""
        invalid_colors = ["#ZZZ", "0D1117", "#12", "#1234567", "red"]

        for color in invalid_colors:
            with pytest.raises(ValueError) as exc_info:
                SecurityValidator.validate_color_hex(color)
            assert "Invalid hex color code" in str(exc_info.value)

    def test_validate_color_hex_empty(self):
        """Test error for empty color"""
        with pytest.raises(ValueError) as exc_info:
            SecurityValidator.validate_color_hex("")
        assert "Color code cannot be empty" in str(exc_info.value)

    # ========================================================================
    # Safe Path Checking Tests
    # ========================================================================

    def test_is_safe_path_valid(self, tmp_path):
        """Test checking if path is safe"""
        test_file = tmp_path / "safe.txt"
        assert SecurityValidator.is_safe_path(str(test_file), str(tmp_path)) is True

    def test_is_safe_path_traversal(self, tmp_path):
        """Test that path traversal is not safe"""
        assert SecurityValidator.is_safe_path("../../etc/passwd", str(tmp_path)) is False

    # ========================================================================
    # Safe Output Path Tests
    # ========================================================================

    def test_get_safe_output_path(self, tmp_path):
        """Test getting safe output path"""
        output_path = SecurityValidator.get_safe_output_path(
            str(tmp_path),
            "module-0-handout",
            ".pdf"
        )

        assert output_path.parent == tmp_path
        assert output_path.name == "module-0-handout.pdf"

    def test_get_safe_output_path_sanitizes_filename(self, tmp_path):
        """Test that output filename is sanitized"""
        output_path = SecurityValidator.get_safe_output_path(
            str(tmp_path),
            "../../../dangerous",
            ".pdf"
        )

        assert ".." not in str(output_path.name)
        assert output_path.parent == tmp_path

    def test_get_safe_output_path_creates_directory(self, tmp_path):
        """Test that output directory is created if missing"""
        new_dir = tmp_path / "output"

        output_path = SecurityValidator.get_safe_output_path(
            str(new_dir),
            "test",
            ".pdf"
        )

        assert new_dir.exists()
        assert output_path.parent == new_dir


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
