"""
Unit tests for PDFRenderer

Tests cover:
- PDF generation with HTML and CSS
- Font embedding and fallback
- Output directory creation
- Error handling (WeasyPrint not installed, write errors)
- PDF validation (file exists, size > 0, valid header)
- Archive functionality
- Standard handout naming convention
"""

import pytest
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock
import tempfile
import shutil

from src.pdf_renderer import PDFRenderer, PDFRendererError
from src.error_handler import ErrorSeverity, FatalError


@pytest.fixture
def temp_dir():
    """Create temporary directory for test outputs"""
    temp_path = Path(tempfile.mkdtemp())
    yield temp_path
    # Cleanup
    if temp_path.exists():
        shutil.rmtree(temp_path)


@pytest.fixture
def sample_config(temp_dir):
    """Sample configuration for PDF renderer"""
    return {
        "global": {
            "output_directory": str(temp_dir / "handouts"),
            "archive_old_versions": True,
            "page_size": "A4"
        },
        "pdf": {
            "margins": {
                "top": "20mm",
                "bottom": "20mm",
                "left": "25mm",
                "right": "25mm"
            },
            "header": {
                "enabled": True,
                "format": "{module_title}",
                "color": "#8B949E"
            },
            "footer": {
                "enabled": True,
                "format": "Page {page_number}",
                "color": "#484F58"
            }
        },
        "branding": {
            "theme": "dark",
            "colors": {
                "background_primary": "#0D1117",
                "text_primary": "#E6EDF3"
            }
        }
    }


@pytest.fixture
def sample_html():
    """Sample HTML content for testing"""
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Test Handout</title>
    </head>
    <body>
        <h1>Module 0: The Hook</h1>
        <p>This is a test handout with <strong>dark theme</strong> styling.</p>
        <pre><code>print("Hello, World!")</code></pre>
    </body>
    </html>
    """


@pytest.fixture
def sample_css():
    """Sample CSS for testing"""
    return """
    @page {
        size: A4;
        margin: 20mm 25mm;
        background: #0D1117;
    }
    body {
        font-family: Inter, sans-serif;
        color: #E6EDF3;
        background: #0D1117;
    }
    h1 {
        color: #E6EDF3;
        font-size: 28pt;
    }
    code {
        font-family: 'JetBrains Mono', monospace;
        background: #161B22;
    }
    """


class TestPDFRendererInitialization:
    """Test PDFRenderer initialization"""

    def test_initialization_success(self, sample_config):
        """Test successful initialization with WeasyPrint available (actual import)"""
        # Use sys.modules mock
        mock_weasyprint = MagicMock()
        mock_weasyprint.__version__ = "60.0"
        with patch.dict('sys.modules', {'weasyprint': mock_weasyprint}):
            renderer = PDFRenderer(sample_config)
            assert renderer.config == sample_config
            assert renderer.pdf_config == sample_config["pdf"]
            assert renderer.global_config == sample_config["global"]

    def test_initialization_without_weasyprint(self, sample_config):
        """Test initialization fails when WeasyPrint is not installed"""
        # Mock ImportError during import
        import_error = ImportError("No module named 'weasyprint'")
        with patch.dict('sys.modules', {'weasyprint': None}):
            # Need to simulate import failure
            original_import = __builtins__.__import__
            def mock_import(name, *args, **kwargs):
                if name == 'weasyprint':
                    raise import_error
                return original_import(name, *args, **kwargs)

            with patch('builtins.__import__', side_effect=mock_import):
                with pytest.raises(FatalError) as exc_info:
                    PDFRenderer(sample_config)
                assert "WeasyPrint" in str(exc_info.value)


class TestPDFGeneration:
    """Test PDF generation functionality"""

    def test_render_to_pdf_basic(self, sample_config, sample_html, temp_dir):
        """Test basic PDF generation"""
        # Mock WeasyPrint
        mock_html = MagicMock()
        mock_html.write_pdf.return_value = b'%PDF-1.4\nFake PDF content'
        mock_weasyprint.HTML.return_value = mock_html

        renderer = PDFRenderer(sample_config)
        output_path = temp_dir / "test.pdf"

        result = renderer.render_to_pdf(
            html_content=sample_html,
            output_path=output_path
        )

        assert result == output_path
        assert output_path.exists()
        assert output_path.stat().st_size > 0

    @patch('src.pdf_renderer.weasyprint')
    def test_render_to_pdf_with_css(self, mock_weasyprint, sample_config, sample_html, sample_css, temp_dir):
        """Test PDF generation with CSS"""
        mock_html = MagicMock()
        mock_html.write_pdf.return_value = b'%PDF-1.4\nFake PDF content'
        mock_weasyprint.HTML.return_value = mock_html
        mock_weasyprint.CSS.return_value = MagicMock()

        renderer = PDFRenderer(sample_config)
        output_path = temp_dir / "test_with_css.pdf"

        result = renderer.render_to_pdf(
            html_content=sample_html,
            css_content=sample_css,
            output_path=output_path
        )

        assert result == output_path
        assert mock_weasyprint.CSS.called

    @patch('src.pdf_renderer.weasyprint')
    def test_render_to_pdf_auto_path(self, mock_weasyprint, sample_config, sample_html):
        """Test PDF generation with auto-generated output path"""
        mock_html = MagicMock()
        mock_html.write_pdf.return_value = b'%PDF-1.4\nFake PDF content'
        mock_weasyprint.HTML.return_value = mock_html

        renderer = PDFRenderer(sample_config)

        result = renderer.render_to_pdf(
            html_content=sample_html,
            module_title="Module 0: The Hook"
        )

        assert result.exists()
        assert "module-0" in result.name

    @patch('src.pdf_renderer.weasyprint')
    def test_render_handout_standard_naming(self, mock_weasyprint, sample_config, sample_html, temp_dir):
        """Test render_handout with standard naming convention"""
        mock_html = MagicMock()
        mock_html.write_pdf.return_value = b'%PDF-1.4\nFake PDF content'
        mock_weasyprint.HTML.return_value = mock_html

        renderer = PDFRenderer(sample_config)

        result = renderer.render_handout(
            html_content=sample_html,
            course_code="ML-ENG",
            module_number=0,
            module_title="The Hook",
            output_dir=temp_dir
        )

        assert result.name == "ML-ENG-module-0-handout.pdf"
        assert result.exists()

    @patch('src.pdf_renderer.weasyprint')
    def test_render_with_base_url(self, mock_weasyprint, sample_config, sample_html, temp_dir):
        """Test PDF generation with custom base URL for resolving paths"""
        mock_html = MagicMock()
        mock_html.write_pdf.return_value = b'%PDF-1.4\nFake PDF content'
        mock_weasyprint.HTML.return_value = mock_html

        renderer = PDFRenderer(sample_config)
        output_path = temp_dir / "test.pdf"
        base_url = "/custom/base/path"

        renderer.render_to_pdf(
            html_content=sample_html,
            output_path=output_path,
            base_url=base_url
        )

        # Verify base_url was passed to HTML()
        call_kwargs = mock_weasyprint.HTML.call_args[1]
        assert call_kwargs['base_url'] == base_url


class TestPDFValidation:
    """Test PDF validation functionality"""

    @patch('src.pdf_renderer.weasyprint')
    def test_validate_pdf_success(self, mock_weasyprint, sample_config, sample_html, temp_dir):
        """Test successful PDF validation"""
        # Create a valid PDF file
        pdf_content = b'%PDF-1.4\nFake PDF content with some data'
        mock_html = MagicMock()
        mock_html.write_pdf.return_value = pdf_content
        mock_weasyprint.HTML.return_value = mock_html

        renderer = PDFRenderer(sample_config)
        output_path = temp_dir / "valid.pdf"

        renderer.render_to_pdf(sample_html, output_path=output_path)
        assert output_path.exists()

    @patch('src.pdf_renderer.weasyprint')
    def test_validate_pdf_empty_file(self, mock_weasyprint, sample_config, sample_html, temp_dir):
        """Test validation fails for empty PDF"""
        mock_html = MagicMock()
        mock_html.write_pdf.return_value = b''  # Empty file
        mock_weasyprint.HTML.return_value = mock_html

        renderer = PDFRenderer(sample_config)
        output_path = temp_dir / "empty.pdf"

        with pytest.raises(PDFRendererError) as exc_info:
            renderer.render_to_pdf(sample_html, output_path=output_path)
        assert "empty" in str(exc_info.value).lower()

    @patch('src.pdf_renderer.weasyprint')
    def test_validate_pdf_invalid_header(self, mock_weasyprint, sample_config, sample_html, temp_dir):
        """Test validation fails for invalid PDF header"""
        mock_html = MagicMock()
        mock_html.write_pdf.return_value = b'Invalid PDF content'  # No %PDF- header
        mock_weasyprint.HTML.return_value = mock_html

        renderer = PDFRenderer(sample_config)
        output_path = temp_dir / "invalid.pdf"

        with pytest.raises(PDFRendererError) as exc_info:
            renderer.render_to_pdf(sample_html, output_path=output_path)
        assert "invalid" in str(exc_info.value).lower() or "header" in str(exc_info.value).lower()

    @patch('src.pdf_renderer.weasyprint')
    def test_validate_pdf_large_file_warning(self, mock_weasyprint, sample_config, sample_html, temp_dir):
        """Test warning for PDF files exceeding size limit"""
        # Create a large PDF (>10MB)
        large_content = b'%PDF-1.4\n' + b'X' * (11 * 1024 * 1024)  # 11MB
        mock_html = MagicMock()
        mock_html.write_pdf.return_value = large_content
        mock_weasyprint.HTML.return_value = mock_html

        renderer = PDFRenderer(sample_config)
        output_path = temp_dir / "large.pdf"

        # Should succeed but log warning
        result = renderer.render_to_pdf(sample_html, output_path=output_path)
        assert result.exists()
        # Warning should be logged (check via error_handler if needed)


class TestArchiveFunctionality:
    """Test archive old versions functionality"""

    @patch('src.pdf_renderer.weasyprint')
    def test_archive_old_version(self, mock_weasyprint, sample_config, sample_html, temp_dir):
        """Test archiving old PDF before overwriting"""
        mock_html = MagicMock()
        mock_html.write_pdf.return_value = b'%PDF-1.4\nVersion 1'
        mock_weasyprint.HTML.return_value = mock_html

        renderer = PDFRenderer(sample_config)
        output_path = temp_dir / "test.pdf"

        # Generate first version
        renderer.render_to_pdf(sample_html, output_path=output_path)
        assert output_path.exists()
        first_content = output_path.read_bytes()

        # Generate second version (should archive first)
        mock_html.write_pdf.return_value = b'%PDF-1.4\nVersion 2'
        renderer.render_to_pdf(sample_html, output_path=output_path)

        # Check archive directory exists
        archive_dir = output_path.parent / "archive"
        assert archive_dir.exists()

        # Check archived file exists
        archived_files = list(archive_dir.glob("test_*.pdf"))
        assert len(archived_files) >= 1

        # Check current file has new content
        assert output_path.read_bytes() != first_content

    @patch('src.pdf_renderer.weasyprint')
    def test_no_archive_when_disabled(self, mock_weasyprint, sample_config, sample_html, temp_dir):
        """Test no archiving when archive_old_versions is False"""
        sample_config["global"]["archive_old_versions"] = False

        mock_html = MagicMock()
        mock_html.write_pdf.return_value = b'%PDF-1.4\nContent'
        mock_weasyprint.HTML.return_value = mock_html

        renderer = PDFRenderer(sample_config)
        output_path = temp_dir / "test.pdf"

        # Generate first version
        renderer.render_to_pdf(sample_html, output_path=output_path)

        # Generate second version
        renderer.render_to_pdf(sample_html, output_path=output_path)

        # Archive directory should not exist
        archive_dir = output_path.parent / "archive"
        assert not archive_dir.exists()


class TestErrorHandling:
    """Test error handling scenarios"""

    @patch('src.pdf_renderer.weasyprint')
    def test_pdf_generation_failure(self, mock_weasyprint, sample_config, sample_html, temp_dir):
        """Test handling of PDF generation failure"""
        mock_html = MagicMock()
        mock_html.write_pdf.side_effect = Exception("WeasyPrint rendering failed")
        mock_weasyprint.HTML.return_value = mock_html

        renderer = PDFRenderer(sample_config)
        output_path = temp_dir / "test.pdf"

        with pytest.raises(PDFRendererError) as exc_info:
            renderer.render_to_pdf(sample_html, output_path=output_path)
        assert "PDF generation failed" in str(exc_info.value)

    @patch('src.pdf_renderer.weasyprint')
    def test_output_directory_creation(self, mock_weasyprint, sample_config, sample_html, temp_dir):
        """Test automatic creation of output directory"""
        mock_html = MagicMock()
        mock_html.write_pdf.return_value = b'%PDF-1.4\nContent'
        mock_weasyprint.HTML.return_value = mock_html

        renderer = PDFRenderer(sample_config)
        # Deep nested path that doesn't exist
        output_path = temp_dir / "deep" / "nested" / "path" / "test.pdf"

        result = renderer.render_to_pdf(sample_html, output_path=output_path)

        assert result.exists()
        assert output_path.parent.exists()

    def test_check_write_permissions_success(self, sample_config, temp_dir):
        """Test write permissions check succeeds for writable directory"""
        with patch('src.pdf_renderer.weasyprint'):
            renderer = PDFRenderer(sample_config)
            test_path = temp_dir / "test.pdf"

            assert renderer.check_write_permissions(test_path) is True

    def test_check_write_permissions_failure(self, sample_config, temp_dir):
        """Test write permissions check fails for read-only directory"""
        with patch('src.pdf_renderer.weasyprint'):
            renderer = PDFRenderer(sample_config)

            # Make directory read-only
            temp_dir.chmod(0o444)
            test_path = temp_dir / "subdir" / "test.pdf"

            try:
                result = renderer.check_write_permissions(test_path)
                assert result is False
            finally:
                # Restore permissions for cleanup
                temp_dir.chmod(0o755)


class TestFontHandling:
    """Test font embedding and fallback"""

    def test_get_font_status_fonts_available(self, sample_config, temp_dir):
        """Test font status check when fonts are available"""
        # Create mock font files
        fonts_dir = Path("assets/fonts")
        fonts_dir.mkdir(parents=True, exist_ok=True)

        try:
            (fonts_dir / "Inter-Regular.ttf").write_text("fake font")
            (fonts_dir / "Inter-Bold.ttf").write_text("fake font")
            (fonts_dir / "JetBrainsMono-Regular.ttf").write_text("fake font")

            with patch('src.pdf_renderer.weasyprint'):
                renderer = PDFRenderer(sample_config)
                status = renderer.get_font_status()

                assert status["inter"]["available"] is True
                assert status["jetbrains_mono"]["available"] is True
                assert len(status["fallback_fonts"]) > 0

        finally:
            # Cleanup
            if fonts_dir.exists():
                shutil.rmtree(fonts_dir)

    def test_get_font_status_fonts_missing(self, sample_config):
        """Test font status check when fonts are missing"""
        with patch('src.pdf_renderer.weasyprint'):
            renderer = PDFRenderer(sample_config)
            status = renderer.get_font_status()

            # Should report fonts as unavailable but have fallbacks
            assert status["inter"]["available"] is False or status["inter"]["path"] is None
            assert len(status["fallback_fonts"]) > 0


class TestOutputPathGeneration:
    """Test output path generation logic"""

    @patch('src.pdf_renderer.weasyprint')
    def test_generate_output_path_with_module_number(self, mock_weasyprint, sample_config):
        """Test output path generation extracts module number"""
        renderer = PDFRenderer(sample_config)

        path = renderer._generate_output_path("Module 0: The Hook")
        assert "module-0" in path.name

        path = renderer._generate_output_path("Module 10: Capstone")
        assert "module-10" in path.name

    @patch('src.pdf_renderer.weasyprint')
    def test_generate_output_path_without_module_number(self, mock_weasyprint, sample_config):
        """Test output path generation with non-standard title"""
        renderer = PDFRenderer(sample_config)

        path = renderer._generate_output_path("Introduction to ML")
        assert "introduction-to-ml" in path.name
        assert path.suffix == ".pdf"


class TestIntegration:
    """Integration tests with minimal mocking"""

    @patch('src.pdf_renderer.weasyprint')
    def test_full_workflow(self, mock_weasyprint, sample_config, sample_html, sample_css, temp_dir):
        """Test complete workflow from HTML to PDF"""
        # Setup mocks
        mock_html = MagicMock()
        mock_html.write_pdf.return_value = b'%PDF-1.4\n' + b'X' * 1000
        mock_weasyprint.HTML.return_value = mock_html
        mock_weasyprint.CSS.return_value = MagicMock()

        # Initialize renderer
        renderer = PDFRenderer(sample_config)

        # Render handout
        result = renderer.render_handout(
            html_content=sample_html,
            course_code="ML-ENG",
            module_number=0,
            module_title="The Hook",
            output_dir=temp_dir
        )

        # Verify results
        assert result.exists()
        assert result.name == "ML-ENG-module-0-handout.pdf"
        assert result.stat().st_size > 0
        assert result.parent == temp_dir

    @patch('src.pdf_renderer.weasyprint')
    def test_render_multiple_handouts(self, mock_weasyprint, sample_config, sample_html, temp_dir):
        """Test rendering multiple handouts sequentially"""
        mock_html = MagicMock()
        mock_html.write_pdf.return_value = b'%PDF-1.4\nContent'
        mock_weasyprint.HTML.return_value = mock_html

        renderer = PDFRenderer(sample_config)

        # Render multiple modules
        results = []
        for i in range(3):
            result = renderer.render_handout(
                html_content=sample_html,
                course_code="TEST",
                module_number=i,
                module_title=f"Module {i}",
                output_dir=temp_dir
            )
            results.append(result)

        # Verify all were created
        assert len(results) == 3
        for i, result in enumerate(results):
            assert result.exists()
            assert f"module-{i}" in result.name


class TestConfigurationHandling:
    """Test configuration handling"""

    @patch('src.pdf_renderer.weasyprint')
    def test_missing_config_sections(self, mock_weasyprint):
        """Test handling of missing config sections"""
        minimal_config = {
            "global": {},
            "pdf": {},
            "branding": {}
        }

        renderer = PDFRenderer(minimal_config)
        assert renderer.config == minimal_config

    @patch('src.pdf_renderer.weasyprint')
    def test_custom_page_size(self, mock_weasyprint, sample_config, sample_html, temp_dir):
        """Test custom page size configuration"""
        sample_config["global"]["page_size"] = "Letter"

        mock_html = MagicMock()
        mock_html.write_pdf.return_value = b'%PDF-1.4\nContent'
        mock_weasyprint.HTML.return_value = mock_html

        renderer = PDFRenderer(sample_config)
        output_path = temp_dir / "test.pdf"

        renderer.render_to_pdf(sample_html, output_path=output_path)
        assert output_path.exists()
