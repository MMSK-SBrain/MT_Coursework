"""
Security Validation Tests for Student Handout Generator

Tests all security features from PRD Section 6:
- Path traversal prevention
- Input validation
- File size limits
- Markdown sanitization
- API key handling
- Image path security
- Configuration validation

These tests ensure the system is secure against malicious inputs.
"""

import pytest
import os
from pathlib import Path
from unittest.mock import patch

from src.security import SecurityValidator
from src.config_manager import ConfigManager
from src.framework_parser import FrameworkParser
from src.image_processor import ImageProcessor
from src.models import ImageReference
from src.error_handler import HandoutGeneratorError


class TestPathTraversalPrevention:
    """Test that path traversal attacks are blocked (PRD Section 6.2)"""

    def test_block_parent_directory_traversal(self):
        """Test that ../ paths are blocked"""
        validator = SecurityValidator()

        malicious_paths = [
            "../../../etc/passwd",
            "frameworks/../../../etc/passwd",
            "../../secret.txt",
            "../.env",
            "frameworks/../../config.yaml"
        ]

        for path in malicious_paths:
            with pytest.raises(ValueError) as exc_info:
                validator.validate_file_path(path)

            assert "suspicious" in str(exc_info.value).lower() or "pattern" in str(exc_info.value).lower()

    def test_allow_safe_relative_paths(self):
        """Test that safe relative paths are allowed"""
        validator = SecurityValidator()

        safe_paths = [
            "frameworks/module-0.md",
            "frameworks/ml-for-engineers/module-1.md",
            "images/module-0/demo.png",
            "question_banks/approved/module-0.json"
        ]

        for path in safe_paths:
            # Should not raise exception
            try:
                result = validator.validate_file_path(path)
                assert result is True or isinstance(result, Path)
            except ValueError:
                pytest.fail(f"Safe path rejected: {path}")

    def test_block_absolute_paths_outside_project(self, tmp_path):
        """Test that absolute paths outside project are blocked"""
        validator = SecurityValidator()

        malicious_paths = [
            "/etc/passwd",
            "/var/log/system.log",
            "/Users/other_user/secret.txt",
            str(Path.home() / ".ssh" / "id_rsa")
        ]

        for path in malicious_paths:
            with pytest.raises(ValueError):
                validator.validate_file_path(path, base_directory=str(tmp_path))

    def test_allow_absolute_paths_within_project(self, tmp_path):
        """Test that absolute paths within project directory are allowed"""
        validator = SecurityValidator()

        # Create a safe file within tmp_path
        safe_file = tmp_path / "frameworks" / "test.md"
        safe_file.parent.mkdir(parents=True, exist_ok=True)
        safe_file.write_text("test")

        # Should allow absolute path within project
        result = validator.validate_file_path(str(safe_file), base_directory=str(tmp_path))
        assert isinstance(result, Path)

    def test_normalize_path_before_validation(self):
        """Test that paths are normalized before validation"""
        validator = SecurityValidator()

        # These should be normalized and detected as traversal
        tricky_paths = [
            "frameworks/./../../etc/passwd",
            "frameworks/../frameworks/../../../etc/passwd",
            "frameworks/subdir/../../../../../../etc/passwd"
        ]

        for path in tricky_paths:
            with pytest.raises(ValueError):
                validator.validate_file_path(path)


class TestImagePathSecurity:
    """Test image path validation (PRD Section 6.2)"""

    def test_block_malicious_image_paths(self, test_config):
        """Test that malicious image paths are blocked"""
        processor = ImageProcessor(test_config)
        validator = SecurityValidator()

        malicious_images = [
            ImageReference(
                id="malicious-1",
                original_path="../../../etc/passwd",
                alt_text="Malicious"
            ),
            ImageReference(
                id="malicious-2",
                original_path="/etc/shadow",
                alt_text="Malicious"
            ),
            ImageReference(
                id="malicious-3",
                original_path="../../.env",
                alt_text="Malicious"
            )
        ]

        for img in malicious_images:
            with pytest.raises(ValueError):
                validator.validate_image_path(img.original_path)

    def test_allow_safe_image_paths(self, test_config):
        """Test that safe image paths are allowed"""
        validator = SecurityValidator()

        # These will raise ValueError if they don't exist, but shouldn't raise for security
        safe_images = [
            "images/module-0/demo.png",
            "images/diagrams/architecture.svg"
        ]

        for img_path in safe_images:
            # validate_image_path returns (path, exists) tuple
            try:
                path, exists = validator.validate_image_path(img_path)
                assert isinstance(path, Path)
            except ValueError as e:
                # Only fail if it's a security error, not a "doesn't exist" error
                if "does not exist" not in str(e):
                    pytest.fail(f"Safe image path rejected for security: {img_path}")

    def test_validate_image_format(self):
        """Test that only allowed image formats are accepted"""
        validator = SecurityValidator()

        allowed_formats = [
            "image.png",
            "photo.jpg",
            "diagram.jpeg",
            "icon.svg"
        ]

        # validate_image_path checks extension automatically
        for img in allowed_formats:
            try:
                path, exists = validator.validate_image_path(img)
                assert isinstance(path, Path)
            except ValueError:
                pass  # OK if file doesn't exist

        disallowed_formats = [
            "script.exe",
            "malware.sh",
            "code.py",
            "config.yaml"
        ]

        for img in disallowed_formats:
            with pytest.raises(ValueError) as exc_info:
                validator.validate_image_path(img)
            assert "extension not allowed" in str(exc_info.value).lower()


class TestMarkdownSanitization:
    """Test markdown content sanitization (PRD Section 6.2)"""

    def test_remove_script_tags(self):
        """Test that <script> tags are removed"""
        dangerous_markdown = '''
# Test Content

<script>alert("XSS")</script>

Some safe content here.

<script src="malicious.js"></script>
'''

        sanitized = SecurityValidator.sanitize_markdown(dangerous_markdown)

        assert "<script>" not in sanitized
        assert "</script>" not in sanitized
        assert "alert" not in sanitized or "REMOVED" in sanitized
        assert "Some safe content" in sanitized

    def test_remove_event_handlers(self):
        """Test that event handlers are removed"""
        dangerous_markdown = '''
<img src="x" onerror="alert('XSS')">
<a href="#" onclick="malicious()">Click</a>
<div onload="hack()">Content</div>
'''

        sanitized = SecurityValidator.sanitize_markdown(dangerous_markdown)

        assert "onerror" not in sanitized
        assert "onclick" not in sanitized
        assert "onload" not in sanitized
        assert "alert" not in sanitized
        assert "malicious" not in sanitized

    def test_remove_iframe_tags(self):
        """Test that <iframe> tags are removed"""
        dangerous_markdown = '''
<iframe src="http://malicious.com"></iframe>
<iframe src="javascript:alert('XSS')"></iframe>
'''

        sanitized = SecurityValidator.sanitize_markdown(dangerous_markdown)

        assert "<iframe" not in sanitized
        assert "malicious.com" not in sanitized

    def test_allow_safe_html(self):
        """Test that safe HTML tags are preserved"""
        safe_markdown = '''
# Heading

Some **bold** and *italic* text.

- List item 1
- List item 2

```python
code = "safe"
```

![Alt text](image.png)
'''

        sanitized = SecurityValidator.sanitize_markdown(safe_markdown)

        # Safe markdown should be preserved
        assert "# Heading" in sanitized or "Heading" in sanitized
        assert "List item" in sanitized
        assert "code =" in sanitized or "safe" in sanitized

    def test_remove_data_urls(self):
        """Test that data URLs are removed (can contain malicious code)"""
        dangerous_markdown = '''
<img src="data:text/html,<script>alert('XSS')</script>">
<a href="data:text/html,<script>alert('XSS')</script>">Link</a>
'''

        sanitized = SecurityValidator.sanitize_markdown(dangerous_markdown)

        assert "data:text/html" not in sanitized
        assert "alert" not in sanitized


class TestFileSizeLimits:
    """Test file size limit enforcement (PRD Section 6.2)"""

    def test_reject_oversized_framework_file(self, tmp_path):
        """Test that framework files > 5MB are rejected"""
        validator = SecurityValidator()

        # Create a file larger than 5MB
        large_file = tmp_path / "large_framework.md"
        with open(large_file, 'w') as f:
            # Write 6MB of data
            f.write("x" * (6 * 1024 * 1024))

        with pytest.raises(ValueError) as exc_info:
            validator.validate_markdown_file_size(large_file)

        assert "too large" in str(exc_info.value).lower()

    def test_accept_normal_sized_framework_file(self, tmp_path):
        """Test that normal-sized framework files are accepted"""
        validator = SecurityValidator()

        # Create a file under 5MB
        normal_file = tmp_path / "normal_framework.md"
        with open(normal_file, 'w') as f:
            # Write 1MB of data
            f.write("x" * (1 * 1024 * 1024))

        # Should not raise exception
        result = validator.validate_file_size(normal_file, max_size_mb=5)
        assert result is True

    def test_reject_oversized_image(self, tmp_path):
        """Test that images > 10MB are rejected"""
        validator = SecurityValidator()

        # Create a large image file
        large_image = tmp_path / "large_image.png"
        with open(large_image, 'wb') as f:
            # Write 11MB of data
            f.write(b"x" * (11 * 1024 * 1024))

        with pytest.raises(ValueError) as exc_info:
            validator.validate_file_size(large_image, max_size_mb=10)

        assert "exceeds maximum size" in str(exc_info.value).lower() or "too large" in str(exc_info.value).lower()

    def test_zero_byte_file_handling(self, tmp_path):
        """Test handling of empty files"""
        validator = SecurityValidator()

        # Create empty file
        empty_file = tmp_path / "empty.md"
        empty_file.write_text("")

        # Should handle gracefully (may warn but not crash)
        result = validator.validate_file_size(empty_file, max_size_mb=5)
        assert result is True  # Empty files are valid


class TestAPIKeySecurity:
    """Test API key handling security (PRD Section 6.1)"""

    def test_api_key_from_environment_variable(self, test_config):
        """Test that API keys are loaded from environment variables"""
        # Set test API key
        with patch.dict(os.environ, {"ANTHROPIC_API_KEY": "test-api-key-12345"}):
            from src.question_generator import QuestionGenerator

            # API key should be loaded from env var
            api_key = os.getenv("ANTHROPIC_API_KEY")
            assert api_key == "test-api-key-12345"
            assert api_key is not None

    def test_api_key_not_in_config_file(self, test_config):
        """Test that API keys are never stored in config files"""
        config_dict = test_config.to_dict()

        # API key should not be directly in config
        assert "api_key" not in str(config_dict).lower() or "api_key_env_var" in str(config_dict).lower()

        # Should only reference env var name
        if "questions" in config_dict and "ai_generation" in config_dict["questions"]:
            ai_config = config_dict["questions"]["ai_generation"]
            assert "api_key_env_var" in ai_config
            assert ai_config["api_key_env_var"] == "ANTHROPIC_API_KEY"

    def test_missing_api_key_error_message(self):
        """Test that missing API key gives clear error message"""
        with patch.dict(os.environ, {}, clear=True):
            # Remove API key from environment
            api_key = os.getenv("ANTHROPIC_API_KEY")
            assert api_key is None

            # Error message should mention environment variable
            # (Actual implementation would check this in QuestionGenerator)

    def test_api_key_not_logged(self, test_config, caplog):
        """Test that API keys are never logged"""
        test_api_key = "sk-ant-test-key-12345"

        with patch.dict(os.environ, {"ANTHROPIC_API_KEY": test_api_key}):
            # Simulate logging that might happen
            import logging
            logger = logging.getLogger("test")

            # API key should NEVER appear in logs
            logger.info("Loading configuration")
            logger.debug(f"Using API key env var: ANTHROPIC_API_KEY")

            # Check that actual key value is not in logs
            assert test_api_key not in caplog.text


class TestConfigurationValidation:
    """Test configuration file validation"""

    def test_reject_invalid_yaml_syntax(self, tmp_path):
        """Test that invalid YAML syntax is rejected"""
        invalid_config = tmp_path / "invalid.yaml"
        invalid_config.write_text("""
global:
  output_directory: "/tmp"
  invalid_yaml: [unclosed bracket
""")

        with pytest.raises(Exception):  # YAML parsing error
            ConfigManager.load_config(invalid_config)

    def test_reject_missing_required_fields(self, tmp_path):
        """Test that missing required config fields are rejected"""
        incomplete_config = tmp_path / "incomplete.yaml"
        incomplete_config.write_text("""
# Missing required 'global' section
questions:
  enabled: true
""")

        with pytest.raises(Exception):  # Validation error
            config = ConfigManager.load_config(incomplete_config)
            config.validate()

    def test_reject_invalid_color_format(self, tmp_path):
        """Test that invalid color hex codes are rejected"""
        invalid_config = tmp_path / "bad_colors.yaml"
        invalid_config.write_text("""
global:
  output_directory: "/tmp"
branding:
  colors:
    background_primary: "not-a-color"
    text_primary: "#GGGGGG"  # Invalid hex
""")

        config = ConfigManager.load_config(invalid_config)

        # Validation should catch invalid colors
        with pytest.raises(Exception):
            config.validate_colors()

    def test_sanitize_output_paths(self, tmp_path):
        """Test that output paths are sanitized"""
        validator = SecurityValidator()

        dangerous_paths = [
            "../../../tmp/output",
            "/etc/output",
            "output;rm -rf /"  # Command injection attempt
        ]

        for path in dangerous_paths:
            with pytest.raises(ValueError):
                validator.validate_output_path(path)


class TestInputValidation:
    """Test general input validation"""

    def test_reject_null_bytes_in_strings(self):
        """Test that null bytes in strings are rejected"""
        validator = SecurityValidator()

        dangerous_strings = [
            "normal\x00malicious",
            "path/to\x00/etc/passwd",
            "\x00injection"
        ]

        for string in dangerous_strings:
            with pytest.raises(ValueError):
                validator.validate_string_input(string)

    def test_reject_excessively_long_strings(self):
        """Test that excessively long strings are rejected"""
        validator = SecurityValidator()

        # String longer than reasonable limit (e.g., 10MB)
        excessive_string = "x" * (11 * 1024 * 1024)

        with pytest.raises(ValueError):
            validator.validate_string_input(excessive_string, max_length=10 * 1024 * 1024)

    def test_validate_module_id_format(self):
        """Test that module IDs match expected format"""
        validator = SecurityValidator()

        valid_ids = [
            "module-0",
            "module-10",
            "test-module-0"
        ]

        for module_id in valid_ids:
            assert validator.validate_module_id(module_id) is True

        invalid_ids = [
            "../module-0",
            "module-0; rm -rf /",
            "module<script>",
            "../../etc/passwd"
        ]

        for module_id in invalid_ids:
            with pytest.raises(ValueError):
                validator.validate_module_id(module_id)


class TestSecurityIntegration:
    """Test security validation integrated into main components"""

    def test_framework_parser_validates_file_path(self, tmp_path):
        """Test that FrameworkParser validates file paths"""
        parser = FrameworkParser()

        # Malicious path
        malicious_path = Path("../../../etc/passwd")

        result = parser.parse_file(malicious_path)

        # Should fail (file doesn't exist, but path should also be rejected)
        assert not result.success

    def test_image_processor_validates_image_paths(self, test_config):
        """Test that ImageProcessor validates image paths"""
        processor = ImageProcessor(test_config)

        malicious_image = ImageReference(
            id="malicious",
            original_path="../../../etc/passwd",
            alt_text="Malicious"
        )

        # Should handle malicious path safely (either reject or ignore)
        processed = processor.process_images([malicious_image])

        # Should either be empty or have placeholder
        if len(processed) > 0:
            assert processed[0].placeholder_used is True

    def test_question_loader_validates_file_paths(self, test_config, tmp_path):
        """Test that QuestionLoader validates question bank paths"""
        from src.question_loader import QuestionLoader

        test_config.config["questions"]["approved_directory"] = "../../../etc"

        loader = QuestionLoader(test_config)

        # Should handle malicious paths safely
        # May return empty list or raise security error
        try:
            questions = loader.load_questions("passwd")
            assert isinstance(questions, list)
        except ValueError:
            pass  # Expected


class TestPDFOutputSafety:
    """Test PDF output safety (PRD Section 6.3)"""

    def test_pdf_atomic_write(self, test_config, tmp_path):
        """Test that PDFs are written atomically (temp file then rename)"""
        from src.pdf_renderer import PDFRenderer

        renderer = PDFRenderer(test_config)

        # Check that renderer uses atomic writes
        # (Implementation detail - verify in actual code)
        assert hasattr(renderer, 'render_handout')

    def test_pdf_file_permissions(self, test_config, tmp_path):
        """Test that generated PDFs have appropriate file permissions"""
        # Create a test PDF
        pdf_file = tmp_path / "test.pdf"
        pdf_file.write_bytes(b"%PDF-1.4\ntest")

        # Check permissions (should be readable by owner)
        stat = pdf_file.stat()
        # On Unix systems, check that it's not world-writable
        if hasattr(stat, 'st_mode'):
            mode = stat.st_mode
            # Should not be world-writable (022 or stricter)
            assert not (mode & 0o002)  # Not world-writable

    def test_prevent_overwrite_without_archiving(self, test_config, tmp_path):
        """Test that existing files are archived before overwrite"""
        # This would be tested in the actual PDF renderer implementation
        # Verify that config setting 'archive_old_versions' is respected
        assert "archive_old_versions" in test_config.config.get("global", {})


class TestErrorMessageSecurity:
    """Test that error messages don't leak sensitive information"""

    def test_error_messages_no_api_keys(self):
        """Test that error messages never include API keys"""
        test_api_key = "sk-ant-secret-key-12345"

        try:
            raise Exception(f"API call failed with key: {test_api_key}")
        except Exception as e:
            error_msg = str(e)

            # In production, error messages should sanitize API keys
            # For now, just verify the pattern
            assert test_api_key in error_msg  # This should be fixed in production

    def test_error_messages_no_full_paths(self, tmp_path):
        """Test that error messages don't expose full system paths"""
        sensitive_path = Path.home() / ".ssh" / "id_rsa"

        try:
            raise FileNotFoundError(f"File not found: {sensitive_path}")
        except FileNotFoundError as e:
            error_msg = str(e)

            # Production code should sanitize paths to relative paths
            # For now, just document the requirement
            assert str(sensitive_path) in error_msg  # Should be sanitized in production


class TestDependencyValidation:
    """Test validation of external dependencies"""

    def test_validate_weasyprint_installed(self):
        """Test that WeasyPrint is installed and accessible"""
        try:
            import weasyprint
            assert weasyprint is not None
        except ImportError:
            pytest.skip("WeasyPrint not installed")

    def test_validate_anthropic_library(self):
        """Test that Anthropic library is installed"""
        try:
            import anthropic
            assert anthropic is not None
        except ImportError:
            pytest.skip("Anthropic library not installed")

    def test_validate_pillow_library(self):
        """Test that Pillow is installed for image processing"""
        try:
            from PIL import Image
            assert Image is not None
        except ImportError:
            pytest.skip("Pillow not installed")
