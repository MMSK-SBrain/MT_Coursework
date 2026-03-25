# Troubleshooting Guide

Common issues and solutions for the Student Handout Generator.

---

## Table of Contents

- [Installation Issues](#installation-issues)
- [Configuration Issues](#configuration-issues)
- [API & Question Generation Issues](#api--question-generation-issues)
- [PDF Generation Issues](#pdf-generation-issues)
- [Image Processing Issues](#image-processing-issues)
- [Performance Issues](#performance-issues)
- [General Errors](#general-errors)

---

## Installation Issues

### WeasyPrint Installation Fails

**Symptom:**
```
ERROR: Failed building wheel for weasyprint
```

**Cause:** Missing system dependencies or incompatible architecture.

**Solution for macOS (Apple Silicon):**

```bash
# Install system dependencies with ARM support
brew install pango gdk-pixbuf cairo libffi

# Set compilation flags
export PKG_CONFIG_PATH="/opt/homebrew/lib/pkgconfig"
export LDFLAGS="-L/opt/homebrew/lib"
export CPPFLAGS="-I/opt/homebrew/include"

# Reinstall WeasyPrint
pip install --force-reinstall weasyprint

# Verify installation
python3 -c "import weasyprint; print(weasyprint.__version__)"
```

**Solution for macOS (Intel):**

```bash
# Install dependencies
brew install pango gdk-pixbuf cairo libffi

# Set compilation flags
export PKG_CONFIG_PATH="/usr/local/lib/pkgconfig"
export LDFLAGS="-L/usr/local/lib"
export CPPFLAGS="-I/usr/local/include"

# Install WeasyPrint
pip install weasyprint
```

---

### Pandoc Not Found

**Symptom:**
```
RuntimeError: Pandoc not found. Please install Pandoc.
```

**Solution:**

```bash
# Install via Homebrew
brew install pandoc

# Verify installation
pandoc --version

# If still not found, check PATH
echo $PATH

# Add Homebrew bin to PATH if needed
export PATH="/opt/homebrew/bin:$PATH"  # Apple Silicon
# or
export PATH="/usr/local/bin:$PATH"      # Intel
```

---

### Python Version Too Old

**Symptom:**
```
ERROR: This package requires Python 3.11+
```

**Solution:**

```bash
# Check current version
python3 --version

# Install Python 3.11+ via Homebrew
brew install python@3.11

# Create virtual environment with specific version
python3.11 -m venv venv
source venv/bin/activate

# Verify
python --version
```

---

### Missing System Libraries

**Symptom:**
```
ImportError: libpango-1.0.dylib not found
```

**Solution:**

```bash
# Reinstall Pango and dependencies
brew reinstall pango gdk-pixbuf cairo

# Link libraries (if needed)
brew link --overwrite pango

# Set library path
export DYLD_LIBRARY_PATH="/opt/homebrew/lib:$DYLD_LIBRARY_PATH"
```

---

## Configuration Issues

### Config File Not Found

**Symptom:**
```
[ERROR] Configuration file not found: handout_config.yaml
```

**Solution:**

```bash
# Check if file exists
ls -la handout_config.yaml

# Create from template if missing
cat > handout_config.yaml << 'EOF'
global:
  output_directory: "./handouts"
  archive_old_versions: true
  page_size: "A4"
  fonts:
    body: "Inter"
    heading: "Inter"
    code: "JetBrains Mono"

branding:
  theme: "dark"

questions:
  enabled: true
  questions_per_section: 7
  require_review: true
  ai_generation:
    enabled: true
    provider: "anthropic"
    api_key_env_var: "ANTHROPIC_API_KEY"
    model: "claude-sonnet-4-20250514"

content:
  exclude_patterns:
    - "## Video Production Notes"
    - "### For Instructors"

images:
  base_directory: "./images"
  max_width: 500

pdf:
  margins:
    top: 20mm
    bottom: 20mm
    left: 25mm
    right: 25mm
EOF
```

---

### Invalid Configuration

**Symptom:**
```
[ERROR] Invalid configuration: 'questions.enabled' must be boolean
```

**Solution:**

```bash
# Validate YAML syntax
python3 -c "import yaml; yaml.safe_load(open('handout_config.yaml'))"

# Common issues:
# - Missing quotes around strings
# - Incorrect indentation (use 2 spaces)
# - Mixed tabs and spaces
# - Invalid color codes (must be #RRGGBB)

# Check specific values
python3 -c "
from src.config_manager import ConfigManager
config = ConfigManager()
config.validate()
print('Configuration valid!')
"
```

---

### Environment Variables Not Loaded

**Symptom:**
```
[ERROR] ANTHROPIC_API_KEY environment variable not set
```

**Solution:**

```bash
# Check if .env file exists
ls -la .env

# Create if missing
cp .env.example .env

# Edit .env
nano .env
# Add: ANTHROPIC_API_KEY=sk-ant-your-key-here

# Verify environment variable
python3 -c "
import os
from dotenv import load_dotenv
load_dotenv()
print('API Key:', 'SET' if os.getenv('ANTHROPIC_API_KEY') else 'NOT SET')
"

# If still not working, set directly in shell
export ANTHROPIC_API_KEY=sk-ant-your-key-here
```

---

## API & Question Generation Issues

### API Key Invalid

**Symptom:**
```
[ERROR] API authentication failed: Invalid API key
```

**Solution:**

```bash
# Check API key format (should start with sk-ant-)
echo $ANTHROPIC_API_KEY

# Get new API key
# 1. Visit https://console.anthropic.com/
# 2. Navigate to API Keys
# 3. Create new key
# 4. Update .env file

# Test API key
python3 -c "
import anthropic
client = anthropic.Anthropic()
print('API key valid!')
"
```

---

### API Rate Limited

**Symptom:**
```
[ERROR] API rate limited: Too many requests
```

**Solution:**

The system automatically retries with exponential backoff. If rate limiting persists:

```bash
# Wait a few minutes and retry
sleep 300  # Wait 5 minutes

# Process modules individually instead of batch
python3 generate_handout.py --input frameworks/module-0.md

# Use approved questions to skip API calls
python3 generate_handout.py \
  --input frameworks/module-0.md \
  --use-approved-questions
```

---

### API Timeout

**Symptom:**
```
[WARNING] API timeout after 60 seconds, retrying (attempt 1/3)
```

**Solution:**

```bash
# Increase timeout in config
# Edit handout_config.yaml:
questions:
  ai_generation:
    timeout_seconds: 120  # Increase from 60

# Check network connection
ping anthropic.com

# Use smaller sections
# Break large framework files into smaller modules
```

---

### Poor Quality Questions Generated

**Symptom:** AI generates irrelevant or low-quality questions.

**Solution:**

1. **Improve framework content:**
   - Ensure learning outcomes are clearly stated
   - Add more context to sections
   - Include concrete examples

2. **Adjust prompts:**
   - Edit `src/ai_prompts.py`
   - Provide better context in prompts
   - Specify question characteristics

3. **Use manual question banks:**
   - Create custom questions
   - Place in `question_banks/approved/`
   - Use `--use-approved-questions` flag

4. **Review and edit:**
   - Use review interface to edit questions
   - Reject low-quality questions
   - Add reviewer notes for future reference

---

### Questions Not Saved After Review

**Symptom:** Reviewed questions don't appear in approved bank.

**Solution:**

```bash
# Check permissions
chmod 755 question_banks/approved
ls -la question_banks/approved/

# Check for error messages in logs
tail -n 50 logs/handout_generation.log

# Manually verify saved file
cat question_banks/approved/module-0.json

# If file is corrupted, restore from staging
cp question_banks/staging/module-0-staging.json \
   question_banks/approved/module-0.json

# Re-run review
python3 generate_handout.py --review-questions module-0
```

---

## PDF Generation Issues

### Font Not Found Warnings

**Symptom:**
```
[WARNING] Font 'Inter' not found, using fallback
```

**Solution:**

```bash
# Install Inter font
# Download from: https://rsms.me/inter/
# Install TTF files to: /Library/Fonts/ or ~/Library/Fonts/

# Install JetBrains Mono
# Download from: https://www.jetbrains.com/lp/mono/
# Install TTF files to: /Library/Fonts/ or ~/Library/Fonts/

# Verify fonts installed
fc-list | grep -i inter
fc-list | grep -i jetbrains

# Clear font cache (if needed)
fc-cache -f -v

# Restart Python process
```

**Alternative - Use System Fonts:**

Edit `handout_config.yaml`:
```yaml
global:
  fonts:
    body: "Arial"
    heading: "Arial"
    code: "Courier New"
```

---

### PDF Generation Fails

**Symptom:**
```
[ERROR] PDF generation failed: WeasyPrint error
```

**Solution:**

```bash
# Check WeasyPrint directly
python3 -c "
from weasyprint import HTML, CSS
HTML(string='<h1>Test</h1>').write_pdf('/tmp/test.pdf')
print('WeasyPrint working!')
"

# Check for malformed HTML
python3 generate_handout.py \
  --input framework.md \
  --formats html \
  --verbose

# Open generated HTML in browser to check for issues
open handouts/module-0/handout.html

# Check logs for detailed error
tail -n 100 logs/handout_generation.log
```

---

### Dark Theme Not Rendering Correctly

**Symptom:** PDF has light background or incorrect colors.

**Solution:**

1. **Check PDF viewer:**
   - Try different PDF viewers (Preview, Adobe Reader, Chrome)
   - Some viewers don't support all CSS features

2. **Verify colors in config:**
   ```yaml
   branding:
     colors:
       background_primary: "#0D1117"  # Must include #
       text_primary: "#E6EDF3"
   ```

3. **Test with HTML output:**
   ```bash
   python3 generate_handout.py \
     --input framework.md \
     --formats html

   # Open in browser to verify colors
   open handouts/module-0/handout.html
   ```

4. **Check CSS template:**
   ```bash
   # Verify dark theme CSS
   cat templates/dark_theme.css | grep background-color
   ```

---

### Page Breaks in Wrong Places

**Symptom:** Headings appear at bottom of page, or content split incorrectly.

**Solution:**

Edit `handout_config.yaml`:
```yaml
pdf:
  page_break_before_sections: true  # Enable page breaks before H2
```

Or manually adjust CSS:
```css
/* In templates/dark_theme.css */
h2 {
  page-break-before: always;
  page-break-after: avoid;
}

.question-box {
  page-break-inside: avoid;
}
```

---

### PDF File Size Too Large

**Symptom:** PDF exceeds 10MB.

**Solution:**

```bash
# Reduce image sizes
# Edit handout_config.yaml:
images:
  max_width: 400  # Reduce from 500

# Compress images before processing
for img in images/*.png; do
  pngquant --quality=65-80 --ext .png --force "$img"
done

# Use JPG instead of PNG for photos
# Convert images:
for img in images/*.png; do
  convert "$img" "${img%.png}.jpg"
done
```

---

## Image Processing Issues

### Images Not Appearing in PDF

**Symptom:** Image placeholders shown instead of actual images.

**Solution:**

```bash
# Check image paths in markdown
grep -n "!\[.*\]" frameworks/module-0.md

# Verify images exist
ls -la images/module-0/

# Check image path resolution
python3 -c "
from src import ConfigManager, ImageProcessor
config = ConfigManager()
processor = ImageProcessor(config)
refs = processor.process_images(
    ['../images/module-0/demo.png'],
    'courses/ml-for-engineers'
)
for ref in refs:
    print(f'{ref.original_path}: exists={ref.exists}')
"

# Fix image paths in markdown
# Use relative paths from framework file location
# Example: ![Demo](../images/module-0/demo.png)
```

---

### Image Format Not Supported

**Symptom:**
```
[WARNING] Unsupported image format: .gif
```

**Solution:**

```bash
# Convert to supported format (PNG, JPG, SVG)
convert image.gif image.png

# Or use online converter

# Update markdown reference
# Change: ![](image.gif)
# To: ![](image.png)
```

---

### Images Too Large to Process

**Symptom:**
```
[WARNING] Image exceeds size limit (>10MB): large.png
```

**Solution:**

```bash
# Compress image before processing
# For PNG:
pngquant --quality=65-80 large.png -o compressed.png

# For JPG:
convert large.jpg -quality 75 compressed.jpg

# Or use ImageMagick to resize
convert large.png -resize 1920x1080 resized.png

# Update image reference in markdown
```

---

### Placeholder Images Appear

**Symptom:** Dark grey placeholders instead of images.

**Cause:** Image files not found.

**Solution:**

```bash
# List missing images from log
grep "Image not found" logs/handout_generation.log

# Check expected image locations
ls -la images/module-0/

# Fix paths in markdown or copy images to correct location
cp ~/Downloads/demo.png images/module-0/

# Disable placeholders (show nothing instead)
# Edit handout_config.yaml:
images:
  placeholder_on_missing: false
```

---

## Performance Issues

### Generation Takes Too Long

**Symptom:** Single module takes >10 minutes to process.

**Solutions:**

1. **Use approved questions:**
   ```bash
   python3 generate_handout.py \
     --input framework.md \
     --use-approved-questions
   ```
   Reduces 3-5 min to ~30 sec.

2. **Reduce questions per section:**
   ```yaml
   # Edit handout_config.yaml:
   questions:
     questions_per_section: 5  # Reduce from 7
   ```

3. **Check API response time:**
   ```bash
   python3 generate_handout.py \
     --input framework.md \
     --verbose | grep "API"
   ```

4. **Process smaller sections:**
   - Break large framework files into multiple modules
   - Process individually

---

### Batch Processing Hangs

**Symptom:** Batch processing stops responding.

**Solution:**

```bash
# Check which module is processing
tail -f logs/handout_generation.log

# Process modules individually to isolate issue
for i in {0..10}; do
  python3 generate_handout.py \
    --input frameworks/module-${i}.md
done

# Increase timeouts
# Edit handout_config.yaml:
questions:
  ai_generation:
    timeout_seconds: 180

# Check system resources
top
```

---

### Memory Errors

**Symptom:**
```
MemoryError: Unable to allocate array
```

**Solution:**

```bash
# Check available memory
top

# Process modules individually instead of batch
python3 generate_handout.py --input framework.md

# Reduce image sizes
# Edit handout_config.yaml:
images:
  max_width: 300

# Close other applications
# Restart Python process periodically

# For very large files, split into multiple modules
```

---

## General Errors

### Permission Denied Errors

**Symptom:**
```
PermissionError: [Errno 13] Permission denied: './handouts/'
```

**Solution:**

```bash
# Create output directory with proper permissions
mkdir -p handouts
chmod 755 handouts

# Check ownership
ls -ld handouts

# Change ownership if needed
sudo chown -R $USER:staff handouts

# Use different output directory
python3 generate_handout.py \
  --input framework.md \
  --output ~/Documents/handouts
```

---

### Module Not Found Errors

**Symptom:**
```
ModuleNotFoundError: No module named 'src'
```

**Solution:**

```bash
# Ensure you're in project root
pwd
# Should be: /Volumes/Dev/Course_Generator

# Activate virtual environment
source venv/bin/activate

# Verify virtual environment
which python
# Should show: .../venv/bin/python

# Reinstall dependencies
pip install -r requirements.txt

# Check Python path
python3 -c "import sys; print('\n'.join(sys.path))"
```

---

### Unicode/Encoding Errors

**Symptom:**
```
UnicodeDecodeError: 'utf-8' codec can't decode byte
```

**Solution:**

```bash
# Check file encoding
file -I frameworks/module-0.md

# Convert to UTF-8 if needed
iconv -f ISO-8859-1 -t UTF-8 framework.md > framework_utf8.md

# Or use dos2unix for line endings
dos2unix framework.md

# Specify encoding explicitly in Python
# (Add to src/framework_parser.py if needed)
with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()
```

---

### Dry Run Fails Validation

**Symptom:**
```
[ERROR] Dry run validation failed: Missing required metadata
```

**Solution:**

```bash
# Check framework file has YAML frontmatter
head -n 20 frameworks/module-0.md

# Required frontmatter:
# ---
# course_code: ML-ENG-M0
# module_number: 0
# module_title: "Module Title"
# ---

# Add missing metadata
# Edit framework file and add YAML frontmatter at top
```

---

### Log File Errors

**Symptom:**
```
[ERROR] Cannot write to log file: logs/handout_generation.log
```

**Solution:**

```bash
# Create logs directory
mkdir -p logs
chmod 755 logs

# Check disk space
df -h

# Clear old logs if needed
rm logs/*.log

# Disable file logging temporarily
# Edit handout_config.yaml:
logging:
  file: null  # Disable file logging
  console: true
```

---

## Getting More Help

### Enable Verbose Mode

```bash
python3 generate_handout.py \
  --input framework.md \
  --verbose 2>&1 | tee output.log
```

### Check Logs

```bash
# View latest log entries
tail -n 100 logs/handout_generation.log

# Search for errors
grep ERROR logs/handout_generation.log

# Watch logs in real-time
tail -f logs/handout_generation.log
```

### Run Tests

```bash
# Run full test suite
pytest -v

# Run specific test
pytest tests/test_framework_parser.py -v

# Run with coverage
pytest --cov=src --cov-report=term-missing
```

### Collect Debug Information

```bash
# System info
uname -a
python3 --version
pandoc --version
brew --version

# Python packages
pip list

# Configuration
python3 -c "
from src.config_manager import ConfigManager
config = ConfigManager()
print(config._config)
"

# Test components
python3 -c "
from src import (
    FrameworkParser, ContentTransformer,
    QuestionGenerator, ImageProcessor,
    LayoutEngine, PDFRenderer
)
print('All imports successful!')
"
```

---

## Still Having Issues?

1. **Check documentation:**
   - [INSTALLATION.md](INSTALLATION.md)
   - [USAGE_GUIDE.md](USAGE_GUIDE.md)
   - [API_REFERENCE.md](API_REFERENCE.md)

2. **Review PRD:**
   - [PRD-Student-Handout-Generator-v2.md](PRD-Student-Handout-Generator-v2.md)

3. **Check architecture:**
   - [ARCHITECTURE.md](ARCHITECTURE.md)

4. **Run diagnostics:**
   ```bash
   # Full system check
   python3 -c "
   print('Python:', __import__('sys').version)
   print('WeasyPrint:', __import__('weasyprint').__version__)
   print('Anthropic:', __import__('anthropic').__version__)
   print('PyYAML:', __import__('yaml').__version__)
   print('Rich:', __import__('rich').__version__)
   print('All dependencies OK!')
   "
   ```

---

**Troubleshooting guide version:** 1.0
**Last updated:** 2026-01-11
