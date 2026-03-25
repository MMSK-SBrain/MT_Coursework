#!/usr/bin/env python3
"""
Demo Script for PDF Renderer

Demonstrates the PDF Renderer functionality with a sample dark-themed handout.

Usage:
    python3 demo_pdf_renderer.py

Output:
    - Generates demo_handout.pdf in the current directory
    - Shows font status and PDF validation
"""

from pathlib import Path
from src.pdf_renderer import PDFRenderer
from src.config_manager import ConfigManager


def main():
    print("=" * 70)
    print(" PDF Renderer Demo - Dark Theme Student Handout")
    print("=" * 70)

    try:
        # 1. Load configuration
        print("\n[1/5] Loading configuration...")
        config_manager = ConfigManager()
        config = config_manager.load_config()
        config["global"]["output_directory"] = "."  # Output to current directory
        print("      ✓ Configuration loaded")

        # 2. Initialize renderer
        print("\n[2/5] Initializing PDFRenderer...")
        renderer = PDFRenderer(config)
        print("      ✓ PDFRenderer initialized")
        print(f"      ✓ WeasyPrint available")

        # 3. Check font status
        print("\n[3/5] Checking font availability...")
        font_status = renderer.get_font_status()
        print(f"      - Inter font: {'✓ Available' if font_status['inter']['available'] else '✗ Not found (will use fallback)'}")
        if font_status['inter']['available']:
            print(f"        Path: {font_status['inter']['path']}")
        print(f"      - JetBrains Mono: {'✓ Available' if font_status['jetbrains_mono']['available'] else '✗ Not found (will use fallback)'}")
        if font_status['jetbrains_mono']['available']:
            print(f"        Path: {font_status['jetbrains_mono']['path']}")

        # 4. Generate PDF
        print("\n[4/5] Generating PDF...")

        html_content = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Demo Handout - ML for Engineers</title>
    <style>
        /* Page setup */
        @page {
            size: A4;
            margin: 20mm 25mm;
            background: #0D1117;

            @top-center {
                content: "Module 0: The Hook - Welcome to Machine Learning";
                font-family: Inter, -apple-system, sans-serif;
                font-size: 10pt;
                color: #8B949E;
                padding-bottom: 8mm;
                border-bottom: 1px solid #30363D;
            }

            @bottom-center {
                content: "Page " counter(page);
                font-family: Inter, -apple-system, sans-serif;
                font-size: 9pt;
                color: #484F58;
            }
        }

        /* Base styles */
        body {
            font-family: Inter, -apple-system, BlinkMacSystemFont, sans-serif;
            font-size: 11pt;
            line-height: 1.6;
            color: #E6EDF3;
            background: #0D1117;
        }

        /* Typography */
        h1 {
            font-size: 28pt;
            font-weight: 600;
            color: #E6EDF3;
            margin: 0 0 24px 0;
        }

        h2 {
            font-size: 22pt;
            font-weight: 600;
            color: #E6EDF3;
            margin: 32px 0 16px 0;
            page-break-after: avoid;
        }

        h3 {
            font-size: 16pt;
            font-weight: 600;
            color: #E6EDF3;
            margin: 24px 0 12px 0;
        }

        p {
            margin: 0 0 12pt 0;
        }

        strong {
            font-weight: 600;
            color: #E6EDF3;
        }

        /* Lists */
        ul, ol {
            margin: 12px 0;
            padding-left: 24px;
        }

        li {
            margin: 4px 0;
        }

        /* Code */
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
            line-height: 1.4;
        }

        /* Question boxes */
        .question-box {
            background: #161B22;
            border-left: 3px solid #58A6FF;
            border-radius: 6px;
            padding: 16px 20px;
            margin: 24px 0;
            page-break-inside: avoid;
        }

        .question-box.reflection {
            border-left-color: #A371F7;
        }

        .question-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
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

        .question-box.reflection .question-number {
            background: #A371F7;
        }

        .question-type {
            color: #8B949E;
            font-size: 9pt;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        .question-text {
            color: #E6EDF3;
            font-weight: 500;
            margin-bottom: 12px;
        }

        .answer-box {
            border: 1px solid #30363D;
            border-radius: 4px;
            min-height: 60px;
            margin-top: 12px;
            background: #0D1117;
        }

        /* Note box */
        .note-box {
            background: #161B22;
            border-left: 3px solid #D29922;
            border-radius: 6px;
            padding: 12px 16px;
            margin: 16px 0;
        }

        .note-label {
            color: #D29922;
            font-size: 10pt;
            font-weight: 600;
            text-transform: uppercase;
            margin-bottom: 4px;
        }
    </style>
</head>
<body>
    <h1>Module 0: The Hook</h1>
    <h2>Welcome to Machine Learning for Engineers</h2>

    <p>Welcome to the exciting world of <strong>Machine Learning</strong>! This demo handout showcases the dark theme PDF renderer built for the Student Handout Generator system.</p>

    <h3>Key Features Demonstrated</h3>

    <ul>
        <li>Dark background (#0D1117) with high-contrast text (#E6EDF3)</li>
        <li>Custom fonts: Inter for body text, JetBrains Mono for code</li>
        <li>Headers and footers with module title and page numbers</li>
        <li>Color-coded question boxes by type</li>
        <li>Code blocks with syntax highlighting</li>
        <li>Professional typography and spacing</li>
    </ul>

    <h2>Code Example: Your First ML Model</h2>

    <p>Here's a simple example of building a machine learning model with TensorFlow:</p>

    <pre><code>import tensorflow as tf
import numpy as np

# Create sample data
X = np.array([[1], [2], [3], [4]])
y = np.array([[2], [4], [6], [8]])

# Build model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation='relu', input_shape=(1,)),
    tf.keras.layers.Dense(1)
])

# Compile model
model.compile(optimizer='adam', loss='mse')

# Train model
model.fit(X, y, epochs=100, verbose=0)

# Make prediction
prediction = model.predict([[5]])
print(f'Prediction for 5: {prediction[0][0]:.2f}')
# Expected output: ~10.0
</code></pre>

    <div class="note-box">
        <div class="note-label">Important Note</div>
        <p>This example demonstrates a simple linear relationship (y = 2x). In practice, ML models tackle far more complex patterns!</p>
    </div>

    <h2>Self-Study Questions</h2>

    <div class="question-box">
        <div class="question-header">
            <span class="question-number">Q1</span>
            <span class="question-type">Multiple Choice</span>
        </div>
        <div class="question-text">
            <strong>What is the primary benefit of using Google Colab for ML beginners?</strong>
        </div>
        <p>
            A) Best code editor available<br/>
            B) Free GPU access in the cloud<br/>
            C) Required for Python programming<br/>
            D) Faster than all local setups
        </p>
        <div class="answer-box"></div>
    </div>

    <div class="question-box reflection">
        <div class="question-header">
            <span class="question-number">Q2</span>
            <span class="question-type">Reflection</span>
        </div>
        <div class="question-text">
            <strong>How might machine learning apply to your engineering field? Describe one potential use case.</strong>
        </div>
        <div class="answer-box"></div>
    </div>

    <h2>What's Next?</h2>

    <p>In the upcoming modules, you'll learn:</p>

    <ol>
        <li>Data exploration and visualization with Pandas</li>
        <li>Building classification models</li>
        <li>Understanding neural networks</li>
        <li>Working with image and text data</li>
        <li>Deploying ML models to production</li>
    </ol>

    <p>This handout was generated by the <strong>PDF Renderer</strong> component of the Student Handout Generator system, demonstrating professional dark-themed PDF output optimized for both screen reading and printing.</p>

</body>
</html>
        """

        output_path = renderer.render_handout(
            html_content=html_content,
            course_code="DEMO",
            module_number=0,
            module_title="The Hook - Welcome to ML",
            output_dir=Path(".")
        )

        print(f"      ✓ PDF generated successfully")
        print(f"      ✓ Output: {output_path}")
        print(f"      ✓ File size: {output_path.stat().st_size / 1024:.2f} KB")

        # 5. Validate PDF
        print("\n[5/5] Validating PDF...")
        with open(output_path, 'rb') as f:
            header = f.read(5)
            if header == b'%PDF-':
                print("      ✓ Valid PDF header")
            else:
                print("      ✗ Invalid PDF header!")

        # Success summary
        print("\n" + "=" * 70)
        print(" ✓ PDF Renderer Demo Complete!")
        print("=" * 70)
        print(f"\n Generated: {output_path.absolute()}")
        print(f" File name: {output_path.name}")
        print(f" File size: {output_path.stat().st_size / 1024:.2f} KB")
        print("\n Open the PDF to see the dark theme rendering!")
        print("\n Features demonstrated:")
        print("  • Dark background (#0D1117) with light text (#E6EDF3)")
        print("  • Inter font for body, JetBrains Mono for code")
        print("  • Headers with module title, footers with page numbers")
        print("  • Color-coded question boxes (blue, purple)")
        print("  • Code blocks with dark background")
        print("  • Professional typography and spacing")
        print("=" * 70)

    except ImportError as e:
        print(f"\n✗ Import Error: {e}")
        print("\n  WeasyPrint is not installed. Please install it:")
        print("    pip install weasyprint")
        print("\n  On macOS, you may also need:")
        print("    brew install pango gdk-pixbuf libffi")

    except Exception as e:
        print(f"\n✗ Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
