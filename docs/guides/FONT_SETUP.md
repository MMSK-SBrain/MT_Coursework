# Font Setup for PDF Generation

## Overview

The Student Handout Generator uses custom fonts for professional dark-themed PDF output:
- **Inter**: Modern sans-serif font for body text and headings
- **JetBrains Mono**: Monospace font for code blocks

## Required Fonts

### Inter Font Family
- **Font**: Inter
- **Weights needed**: Regular (400), Bold (600)
- **Source**: [Google Fonts - Inter](https://fonts.google.com/specimen/Inter)
- **Files needed**:
  - `Inter-Regular.ttf`
  - `Inter-Bold.ttf` (or `Inter-SemiBold.ttf`)

### JetBrains Mono
- **Font**: JetBrains Mono
- **Weight needed**: Regular (400)
- **Source**: [Google Fonts - JetBrains Mono](https://fonts.google.com/specimen/JetBrains+Mono)
- **File needed**:
  - `JetBrainsMono-Regular.ttf`

---

## Installation Methods

### Method 1: Download from Google Fonts (Recommended)

#### Step 1: Download Inter

1. Visit https://fonts.google.com/specimen/Inter
2. Click "Download family" button
3. Extract the ZIP file
4. Locate the TTF files in the `static` folder:
   - `Inter-Regular.ttf` (or weight 400)
   - `Inter-Bold.ttf` (or weight 600, or `Inter-SemiBold.ttf`)

#### Step 2: Download JetBrains Mono

1. Visit https://fonts.google.com/specimen/JetBrains+Mono
2. Click "Download family" button
3. Extract the ZIP file
4. Locate in the `static` folder:
   - `JetBrainsMono-Regular.ttf` (or weight 400)

#### Step 3: Copy to Project

```bash
# From the project root directory
mkdir -p assets/fonts

# Copy the font files (adjust paths to where you extracted them)
cp ~/Downloads/Inter/static/Inter-Regular.ttf assets/fonts/
cp ~/Downloads/Inter/static/Inter-SemiBold.ttf assets/fonts/Inter-Bold.ttf
cp ~/Downloads/JetBrains_Mono/static/JetBrainsMono-Regular.ttf assets/fonts/
```

### Method 2: Download with curl/wget

```bash
# Create fonts directory
mkdir -p assets/fonts

# Download Inter (GitHub release)
curl -L https://github.com/rsms/inter/releases/download/v4.0/Inter-4.0.zip -o /tmp/Inter.zip
unzip /tmp/Inter.zip -d /tmp/Inter
cp /tmp/Inter/Inter\ Desktop/Inter-Regular.otf assets/fonts/Inter-Regular.ttf
cp /tmp/Inter/Inter\ Desktop/Inter-SemiBold.otf assets/fonts/Inter-Bold.ttf

# Download JetBrains Mono (GitHub release)
curl -L https://github.com/JetBrains/JetBrainsMono/releases/download/v2.304/JetBrainsMono-2.304.zip -o /tmp/JBM.zip
unzip /tmp/JBM.zip -d /tmp/JBM
cp /tmp/JBM/fonts/ttf/JetBrainsMono-Regular.ttf assets/fonts/
```

### Method 3: Use System Fonts (Fallback)

If you don't install custom fonts, WeasyPrint will fall back to system fonts:
- **macOS**: Helvetica (body), Courier (code)
- **Linux**: Liberation Sans (body), Liberation Mono (code)
- **Windows**: Arial (body), Courier New (code)

The PDFs will still generate but may not match the intended dark theme aesthetic.

---

## Verification

### Check Font Installation

Run this Python script to verify fonts are properly installed:

```python
from pathlib import Path

fonts_dir = Path("assets/fonts")
required_fonts = [
    "Inter-Regular.ttf",
    "Inter-Bold.ttf",
    "JetBrainsMono-Regular.ttf"
]

print("Checking font installation...")
all_found = True

for font in required_fonts:
    font_path = fonts_dir / font
    if font_path.exists():
        size_kb = font_path.stat().st_size / 1024
        print(f"✓ {font} ({size_kb:.1f} KB)")
    else:
        print(f"✗ {font} - NOT FOUND")
        all_found = False

if all_found:
    print("\n✓ All fonts installed correctly!")
else:
    print("\n✗ Some fonts are missing. Please install them.")
```

Or use the PDFRenderer's built-in check:

```python
from src.pdf_renderer import PDFRenderer
from src.config_manager import ConfigManager

config_manager = ConfigManager()
config = config_manager.load_config()
renderer = PDFRenderer(config)

status = renderer.get_font_status()
print(f"Inter: {status['inter']['available']}")
print(f"JetBrains Mono: {status['jetbrains_mono']['available']}")
```

### Test PDF Generation

Generate a test PDF to verify font embedding:

```bash
python -c "
from src.pdf_renderer import PDFRenderer
from src.config_manager import ConfigManager

config_manager = ConfigManager()
config = config_manager.load_config()
renderer = PDFRenderer(config)

html = '''
<html>
<head>
    <style>
        body { font-family: Inter, sans-serif; background: #0D1117; color: #E6EDF3; padding: 40px; }
        h1 { font-weight: 600; }
        code { font-family: 'JetBrains Mono', monospace; background: #161B22; padding: 2px 6px; }
    </style>
</head>
<body>
    <h1>Font Test</h1>
    <p>This is Inter Regular text.</p>
    <p><strong>This is Inter Bold text.</strong></p>
    <p>Code example: <code>print('Hello, World!')</code></p>
</body>
</html>
'''

output = renderer.render_to_pdf(html, output_path='test_fonts.pdf')
print(f'Test PDF generated: {output}')
"
```

Open `test_fonts.pdf` and verify:
- Body text uses Inter font
- Bold text uses Inter Bold
- Code uses JetBrains Mono

---

## Troubleshooting

### Font Not Embedding in PDF

**Problem**: PDFs use fallback fonts instead of custom fonts.

**Solutions**:
1. **Check file paths**: Ensure fonts are in `assets/fonts/` directory
2. **Check CSS paths**: The `dark_theme.css` uses relative paths: `url('../assets/fonts/...')`
3. **Verify base_url**: When calling `render_to_pdf()`, ensure `base_url` is set correctly:
   ```python
   renderer.render_to_pdf(html, base_url=str(Path.cwd()))
   ```
4. **Check file names**: Font files must match exactly:
   - `Inter-Regular.ttf` (not `Inter_Regular.ttf` or `InterRegular.ttf`)
   - `Inter-Bold.ttf` (not `Inter-SemiBold.ttf` unless you rename it)
   - `JetBrainsMono-Regular.ttf`

### OTF vs TTF Fonts

If you downloaded OTF (OpenType) fonts instead of TTF (TrueType):
- WeasyPrint supports both OTF and TTF
- Update `@font-face` in `dark_theme.css` to use `.otf` extension
- Or convert OTF to TTF using online tools or `fontforge`

### Font File Too Large

If fonts are very large (>1MB each):
- **Inter**: Download the "variable" version for smaller file size
- **JetBrains Mono**: Use only Regular weight (400) to save space
- Fonts will be embedded in each PDF, so smaller fonts = smaller PDFs

### WeasyPrint Cannot Find Fonts

**Error**: `WARNING: @font-face failed to load`

**Solutions**:
1. Check WeasyPrint logs for the exact path it's trying to load
2. Use absolute paths in CSS temporarily for debugging:
   ```css
   @font-face {
     font-family: 'Inter';
     src: url('/absolute/path/to/Course_Generator/assets/fonts/Inter-Regular.ttf') format('truetype');
   }
   ```
3. Ensure fonts are readable (check file permissions):
   ```bash
   chmod 644 assets/fonts/*.ttf
   ```

---

## Alternative Font Sources

### Inter Font
- **Official**: https://rsms.me/inter/
- **GitHub**: https://github.com/rsms/inter/releases
- **Google Fonts**: https://fonts.google.com/specimen/Inter
- **CDN**: https://fonts.googleapis.com/css2?family=Inter:wght@400;600

### JetBrains Mono
- **Official**: https://www.jetbrains.com/lp/mono/
- **GitHub**: https://github.com/JetBrains/JetBrainsMono/releases
- **Google Fonts**: https://fonts.google.com/specimen/JetBrains+Mono

---

## Font Licensing

Both fonts are free and open source:

- **Inter**: [SIL Open Font License 1.1](https://github.com/rsms/inter/blob/master/LICENSE.txt)
- **JetBrains Mono**: [OFL-1.1 License](https://github.com/JetBrains/JetBrainsMono/blob/master/OFL.txt)

You can:
- Use them for personal and commercial projects
- Embed them in PDFs
- Distribute PDFs with embedded fonts

---

## Quick Setup Script

Save this as `setup_fonts.sh`:

```bash
#!/bin/bash
set -e

echo "Setting up fonts for Student Handout Generator..."

# Create fonts directory
mkdir -p assets/fonts

# Download Inter
echo "Downloading Inter font..."
curl -L https://github.com/rsms/inter/releases/download/v4.0/Inter-4.0.zip -o /tmp/Inter.zip
unzip -q /tmp/Inter.zip -d /tmp/Inter

# Copy Inter fonts (convert OTF to TTF naming)
cp "/tmp/Inter/Inter Desktop/Inter-Regular.otf" assets/fonts/Inter-Regular.ttf
cp "/tmp/Inter/Inter Desktop/Inter-SemiBold.otf" assets/fonts/Inter-Bold.ttf

# Download JetBrains Mono
echo "Downloading JetBrains Mono font..."
curl -L https://github.com/JetBrains/JetBrainsMono/releases/download/v2.304/JetBrainsMono-2.304.zip -o /tmp/JBM.zip
unzip -q /tmp/JBM.zip -d /tmp/JBM

# Copy JetBrains Mono
cp /tmp/JBM/fonts/ttf/JetBrainsMono-Regular.ttf assets/fonts/

# Cleanup
rm -rf /tmp/Inter.zip /tmp/Inter /tmp/JBM.zip /tmp/JBM

echo "✓ Fonts installed successfully!"
echo ""
echo "Installed fonts:"
ls -lh assets/fonts/
```

Make it executable and run:

```bash
chmod +x setup_fonts.sh
./setup_fonts.sh
```

---

## Summary

1. **Download fonts** from Google Fonts or GitHub
2. **Copy to** `assets/fonts/` directory
3. **Required files**:
   - `Inter-Regular.ttf`
   - `Inter-Bold.ttf`
   - `JetBrainsMono-Regular.ttf`
4. **Verify** with `PDFRenderer.get_font_status()`
5. **Test** by generating a sample PDF

For questions or issues, check the troubleshooting section above.
