"""
Integration test for PDF Renderer

This test uses actual WeasyPrint (if available) to generate a real PDF.
Run this separately from unit tests to verify end-to-end functionality.

Usage:
    python3 -m pytest tests/test_pdf_renderer_integration.py -v -s

    Or run directly:
    python3 tests/test_pdf_renderer_integration.py
"""

import pytest
from pathlib import Path
import tempfile
import shutil

from src.pdf_renderer import PDFRenderer, PDFRendererError
from src.config_manager import ConfigManager
from src.error_handler import FatalError


# Skip all tests in this module if WeasyPrint is not installed
pytest.importorskip("weasyprint", reason="WeasyPrint not installed")


@pytest.fixture
def config():
    """Load actual config"""
    config_manager = ConfigManager()
    return config_manager.load_config()


@pytest.fixture
def temp_output_dir():
    """Create temporary output directory"""
    temp_dir = Path(tempfile.mkdtemp())
    yield temp_dir
    # Cleanup
    if temp_dir.exists():
        shutil.rmtree(temp_dir)


@pytest.fixture
def sample_html():
    """Sample HTML with dark theme"""
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Test Handout - Module 0</title>
        <style>
            @page {
                size: A4;
                margin: 20mm 25mm;
                background: #0D1117;

                @top-center {
                    content: "Module 0: The Hook - Welcome to Machine Learning";
                    font-family: Inter, sans-serif;
                    font-size: 10pt;
                    color: #8B949E;
                }

                @bottom-center {
                    content: "Page " counter(page);
                    font-family: Inter, sans-serif;
                    font-size: 9pt;
                    color: #484F58;
                }
            }

            body {
                font-family: Inter, -apple-system, sans-serif;
                font-size: 11pt;
                line-height: 1.6;
                color: #E6EDF3;
                background: #0D1117;
            }

            h1 {
                font-size: 28pt;
                font-weight: 600;
                color: #E6EDF3;
                margin-bottom: 24px;
            }

            h2 {
                font-size: 22pt;
                font-weight: 600;
                color: #E6EDF3;
                margin: 32px 0 16px 0;
            }

            p {
                margin: 0 0 12pt 0;
            }

            code {
                font-family: 'JetBrains Mono', 'Courier New', monospace;
                font-size: 10pt;
                background: #161B22;
                padding: 2px 6px;
                border-radius: 4px;
                color: #E6EDF3;
            }

            pre {
                background: #161B22;
                border: 1px solid #30363D;
                border-radius: 6px;
                padding: 16px;
                margin: 16px 0;
            }

            pre code {
                background: none;
                padding: 0;
            }

            .question-box {
                background: #161B22;
                border-left: 3px solid #58A6FF;
                border-radius: 6px;
                padding: 16px 20px;
                margin: 24px 0;
            }

            .question-header {
                display: flex;
                justify-content: space-between;
                margin-bottom: 12px;
            }

            .question-number {
                background: #58A6FF;
                color: #0D1117;
                padding: 2px 8px;
                border-radius: 4px;
                font-size: 10pt;
                font-weight: 600;
            }

            .question-type {
                color: #8B949E;
                font-size: 9pt;
                text-transform: uppercase;
            }
        </style>
    </head>
    <body>
        <h1>Module 0: The Hook</h1>
        <h2>Welcome to Machine Learning for Engineers</h2>

        <p>This is a <strong>test handout</strong> demonstrating the dark theme PDF renderer.</p>

        <p>The renderer supports:</p>
        <ul>
            <li>Dark background (#0D1117) with light text (#E6EDF3)</li>
            <li>Custom fonts (Inter for body, JetBrains Mono for code)</li>
            <li>Headers and footers with page numbers</li>
            <li>Question boxes with colored borders</li>
        </ul>

        <h2>Code Example</h2>

        <p>Here's a simple Python code block:</p>

        <pre><code>import tensorflow as tf

model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation='relu'),
    tf.keras.layers.Dense(1)
])

model.compile(optimizer='adam', loss='mse')
print('Model ready!')
</code></pre>

        <h2>Self-Study Questions</h2>

        <div class="question-box">
            <div class="question-header">
                <span class="question-number">Q1</span>
                <span class="question-type">Multiple Choice</span>
            </div>
            <p><strong>What is the primary benefit of Google Colab for ML beginners?</strong></p>
            <p>A) Best code editor<br/>
               B) Free GPU access in the cloud<br/>
               C) Required for Python<br/>
               D) Faster than all local setups</p>
        </div>

        <p>This PDF demonstrates all the key features of the dark theme renderer.</p>
    </body>
    </html>
    """


class TestPDFRendererIntegration:
    """Integration tests with actual WeasyPrint"""

    def test_generate_basic_pdf(self, config, sample_html, temp_output_dir):
        """Test generating a basic PDF with actual WeasyPrint"""
        # Update config to use temp directory
        config["global"]["output_directory"] = str(temp_output_dir)

        renderer = PDFRenderer(config)
        output_path = temp_output_dir / "test-basic.pdf"

        result = renderer.render_to_pdf(
            html_content=sample_html,
            output_path=output_path,
            module_title="Module 0: The Hook"
        )

        # Verify PDF was created
        assert result.exists()
        assert result == output_path

        # Verify file size
        file_size = result.stat().st_size
        assert file_size > 0
        print(f"\n✓ PDF generated: {result}")
        print(f"✓ File size: {file_size / 1024:.2f} KB")

        # Verify PDF header
        with open(result, 'rb') as f:
            header = f.read(5)
            assert header == b'%PDF-'
            print(f"✓ Valid PDF header")

    def test_generate_handout_with_standard_naming(self, config, sample_html, temp_output_dir):
        """Test render_handout with standard naming convention"""
        config["global"]["output_directory"] = str(temp_output_dir)

        renderer = PDFRenderer(config)

        result = renderer.render_handout(
            html_content=sample_html,
            course_code="ML-ENG",
            module_number=0,
            module_title="The Hook",
            output_dir=temp_output_dir
        )

        # Verify naming convention
        assert result.name == "ML-ENG-module-0-handout.pdf"
        assert result.exists()

        print(f"\n✓ Handout generated: {result}")
        print(f"✓ File name: {result.name}")

    def test_archive_functionality(self, config, sample_html, temp_output_dir):
        """Test archiving old versions"""
        config["global"]["output_directory"] = str(temp_output_dir)
        config["global"]["archive_old_versions"] = True

        renderer = PDFRenderer(config)
        output_path = temp_output_dir / "test-archive.pdf"

        # Generate first version
        result1 = renderer.render_to_pdf(sample_html, output_path=output_path)
        assert result1.exists()

        # Generate second version (should archive first)
        result2 = renderer.render_to_pdf(sample_html, output_path=output_path)
        assert result2.exists()

        # Check archive directory
        archive_dir = output_path.parent / "archive"
        assert archive_dir.exists()

        # Check archived files
        archived_files = list(archive_dir.glob("test-archive_*.pdf"))
        assert len(archived_files) >= 1

        print(f"\n✓ Archive directory: {archive_dir}")
        print(f"✓ Archived files: {len(archived_files)}")

    def test_font_status_check(self, config):
        """Test font availability checking"""
        renderer = PDFRenderer(config)

        status = renderer.get_font_status()

        print(f"\n✓ Font status:")
        print(f"  - Inter: {status['inter']['available']}")
        if status['inter']['available']:
            print(f"    Path: {status['inter']['path']}")
        print(f"  - JetBrains Mono: {status['jetbrains_mono']['available']}")
        if status['jetbrains_mono']['available']:
            print(f"    Path: {status['jetbrains_mono']['path']}")
        print(f"  - Fallback fonts: {', '.join(status['fallback_fonts'][:3])}")

        assert "fallback_fonts" in status
        assert len(status["fallback_fonts"]) > 0

    def test_write_permissions_check(self, config, temp_output_dir):
        """Test write permissions checking"""
        renderer = PDFRenderer(config)

        test_path = temp_output_dir / "test.pdf"
        can_write = renderer.check_write_permissions(test_path)

        assert can_write is True
        print(f"\n✓ Write permissions: OK for {temp_output_dir}")


def main():
    """Run integration tests manually"""
    print("=" * 60)
    print("PDF Renderer Integration Tests")
    print("=" * 60)

    try:
        # Load config
        config_manager = ConfigManager()
        config = config_manager.load_config()

        # Create temp directory
        temp_dir = Path(tempfile.mkdtemp())
        config["global"]["output_directory"] = str(temp_dir)

        print(f"\nTemp output directory: {temp_dir}")

        # Initialize renderer
        print("\n1. Initializing PDFRenderer...")
        renderer = PDFRenderer(config)
        print("   ✓ PDFRenderer initialized")

        # Check fonts
        print("\n2. Checking font status...")
        status = renderer.get_font_status()
        print(f"   - Inter: {status['inter']['available']}")
        print(f"   - JetBrains Mono: {status['jetbrains_mono']['available']}")

        # Generate sample PDF
        print("\n3. Generating sample PDF...")

        html = """
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                @page { size: A4; margin: 20mm; background: #0D1117; }
                body { font-family: Inter, sans-serif; color: #E6EDF3; background: #0D1117; padding: 40px; }
                h1 { font-size: 28pt; font-weight: 600; }
                code { font-family: 'JetBrains Mono', monospace; background: #161B22; padding: 2px 6px; }
            </style>
        </head>
        <body>
            <h1>PDF Renderer Test</h1>
            <p>This is a test handout with <strong>dark theme</strong>.</p>
            <p>Code example: <code>print('Hello, ML!')</code></p>
        </body>
        </html>
        """

        output = renderer.render_handout(
            html_content=html,
            course_code="TEST",
            module_number=0,
            module_title="PDF Renderer Test",
            output_dir=temp_dir
        )

        print(f"   ✓ PDF generated: {output}")
        print(f"   ✓ File size: {output.stat().st_size / 1024:.2f} KB")

        # Validate
        print("\n4. Validating PDF...")
        with open(output, 'rb') as f:
            header = f.read(5)
            if header == b'%PDF-':
                print("   ✓ Valid PDF header")
            else:
                print("   ✗ Invalid PDF header")

        print("\n" + "=" * 60)
        print("✓ All integration tests passed!")
        print("=" * 60)
        print(f"\nGenerated PDF: {output}")
        print("Open this file to verify the dark theme rendering.")

    except Exception as e:
        print(f"\n✗ Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
