# Installation Guide

Complete installation guide for the Student Handout Generator system.

---

## Table of Contents

- [Prerequisites](#prerequisites)
- [System Dependencies](#system-dependencies)
- [Python Package Installation](#python-package-installation)
- [Font Setup](#font-setup)
- [Environment Configuration](#environment-configuration)
- [Verification](#verification)
- [Troubleshooting](#troubleshooting)

---

## Prerequisites

### Required Software

- **Python 3.11 or higher**
  - Check your version: `python3 --version`
  - macOS typically includes Python 3, but you may need to upgrade
  - Download from: https://www.python.org/downloads/

- **Homebrew** (macOS package manager)
  - Check if installed: `brew --version`
  - Install if needed: `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`

### Hardware Requirements

- **Operating System:** macOS 12+ (optimized for Apple Silicon M1/M2/M3)
- **RAM:** 8GB minimum, 16GB recommended
- **Storage:** 1GB free space for dependencies and generated files
- **Network:** Required for AI-powered question generation (Claude API)

---

## System Dependencies

These dependencies are required for PDF generation and image processing.

### Install via Homebrew

```bash
brew install pandoc pango gdk-pixbuf libffi
```

### Dependency Details

| Package | Purpose | Version |
|---------|---------|---------|
| **pandoc** | Document conversion between formats | 3.0+ |
| **pango** | Text rendering for PDFs | Latest |
| **gdk-pixbuf** | Image loading and scaling | Latest |
| **libffi** | Foreign function interface library | Latest |

### Verify Installation

```bash
# Check Pandoc
pandoc --version

# Should output: pandoc 3.x.x or higher
```

---

## Python Package Installation

### Step 1: Navigate to Project Directory

```bash
cd /Volumes/Dev/Course_Generator
```

### Step 2: Create Virtual Environment (Recommended)

```bash
# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate

# You should see (venv) in your prompt
```

### Step 3: Install Python Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- **Document Processing:** mistune, pypandoc, markdown-it-py
- **PDF Generation:** weasyprint, Pillow
- **AI Integration:** anthropic (Claude API client)
- **Configuration:** PyYAML, Jinja2, python-dotenv
- **Terminal UI:** rich
- **Testing:** pytest, pytest-cov, pytest-mock

### Step 4: Verify Installation

```bash
# Check installed packages
pip list | grep -E "weasyprint|anthropic|rich|PyYAML"
```

Expected output:
```
anthropic         0.40.0
PyYAML           6.0.0
rich             13.7.0
weasyprint       60.2.0
```

---

## Font Setup

The system uses two professional fonts for optimal readability:

### Required Fonts

1. **Inter** - Body text and headings
2. **JetBrains Mono** - Code blocks

### Installation Methods

#### Option 1: Automatic (System Fonts)

If these fonts are already installed on your system, the PDF renderer will use them automatically.

Check if fonts are installed:
```bash
# macOS
fc-list | grep -i inter
fc-list | grep -i jetbrains
```

#### Option 2: Manual Installation

**Inter Font:**
1. Download from: https://rsms.me/inter/
2. Install all font files (TTF format)
3. Place in: `/Library/Fonts/` (system-wide) or `~/Library/Fonts/` (user)

**JetBrains Mono:**
1. Download from: https://www.jetbrains.com/lp/mono/
2. Install all font files (TTF format)
3. Place in: `/Library/Fonts/` or `~/Library/Fonts/`

#### Option 3: Embedded Fonts (Project Bundle)

If you have font files in the project:
```bash
# Copy fonts to assets directory
mkdir -p assets/fonts
cp ~/Downloads/Inter-*.ttf assets/fonts/
cp ~/Downloads/JetBrainsMono-*.ttf assets/fonts/
```

### Verify Fonts

```bash
# List available fonts
fc-list | grep -E "Inter|JetBrains"
```

Expected output:
```
/Library/Fonts/Inter-Regular.ttf: Inter:style=Regular
/Library/Fonts/Inter-Bold.ttf: Inter:style=Bold
/Library/Fonts/JetBrainsMono-Regular.ttf: JetBrains Mono:style=Regular
```

### Fallback Behavior

If fonts are not found, the system will:
1. Log a warning
2. Fall back to system fonts (Arial, Courier)
3. PDF will still generate, but with different typography

---

## Environment Configuration

### Step 1: Create Environment File

```bash
# Copy example file
cp .env.example .env
```

### Step 2: Configure API Key

Edit `.env` and add your Anthropic API key:

```bash
# Open in your preferred editor
nano .env
# or
code .env
```

Add the following:
```bash
# Anthropic API Key (required for AI question generation)
ANTHROPIC_API_KEY=sk-ant-xxxxxxxxxxxxxxxxxxxxx

# Optional: Override default config path
# HANDOUT_CONFIG_PATH=./custom_config.yaml

# Optional: Log level (DEBUG, INFO, WARNING, ERROR)
LOG_LEVEL=INFO
```

### Step 3: Get an Anthropic API Key

1. Sign up at: https://console.anthropic.com/
2. Navigate to: API Keys section
3. Create a new API key
4. Copy the key (starts with `sk-ant-`)
5. Paste into `.env` file

**Security Note:** Never commit the `.env` file to version control. It's already in `.gitignore`.

### Step 4: Verify Configuration

```bash
# Check if API key is set
python3 -c "import os; from dotenv import load_dotenv; load_dotenv(); print('API Key:', 'SET' if os.getenv('ANTHROPIC_API_KEY') else 'NOT SET')"
```

Expected output:
```
API Key: SET
```

---

## Verification

### Complete Installation Check

Run the following command to verify everything is working:

```bash
python3 generate_handout.py --help
```

Expected output:
```
usage: generate_handout.py [-h] [--input INPUT] [--batch] [--course COURSE] ...

Student Handout Generator - Transform framework files into professional PDFs

optional arguments:
  -h, --help           show this help message and exit
  --input INPUT, -i INPUT
                       Path to framework markdown file
  ...
```

### Test Generation (Dry Run)

Test the system without generating a PDF:

```bash
python3 generate_handout.py --input courses/ml-for-engineers/frameworks/module-0-framework-REVISED.md --dry-run
```

Expected output:
```
[INFO] Dry run mode enabled - no files will be generated
[INFO] Validating framework file...
[INFO] Framework file valid: module-0-framework-REVISED.md
[INFO] Metadata extracted: Module 0 - The Hook
[INFO] All checks passed!
```

### Run Full Test Suite

```bash
# Run all tests
pytest

# Run with coverage report
pytest --cov=src --cov-report=term-missing
```

Expected output:
```
============================= test session starts ==============================
...
collected 45 items

tests/test_framework_parser.py ........                                  [ 17%]
tests/test_content_transformer.py ......                                 [ 31%]
tests/test_question_loader.py .....                                      [ 42%]
...

============================== 45 passed in 12.34s =============================
```

---

## Troubleshooting

### Issue: "WeasyPrint not found"

**Error:**
```
ModuleNotFoundError: No module named 'weasyprint'
```

**Solution:**
```bash
# Ensure system dependencies are installed first
brew install pango gdk-pixbuf libffi

# Then reinstall WeasyPrint
pip install --force-reinstall weasyprint
```

---

### Issue: "Pandoc not found"

**Error:**
```
RuntimeError: Pandoc not found. Please install Pandoc.
```

**Solution:**
```bash
# Install Pandoc
brew install pandoc

# Verify installation
pandoc --version
```

---

### Issue: "Font not found"

**Warning:**
```
[WARNING] Font 'Inter' not found, using fallback
```

**Solution:**
1. Install Inter font (see [Font Setup](#font-setup))
2. Verify installation: `fc-list | grep Inter`
3. Restart terminal/Python session
4. If still not working, PDF will use system fonts (no critical error)

---

### Issue: "API Key not set"

**Error:**
```
[ERROR] ANTHROPIC_API_KEY environment variable not set
```

**Solution:**
```bash
# Check if .env file exists
ls -la .env

# If not, create it
cp .env.example .env

# Edit and add your API key
nano .env

# Verify
python3 -c "import os; from dotenv import load_dotenv; load_dotenv(); print(os.getenv('ANTHROPIC_API_KEY'))"
```

---

### Issue: "Permission denied" when generating PDFs

**Error:**
```
PermissionError: [Errno 13] Permission denied: './handouts/module-0/'
```

**Solution:**
```bash
# Create output directory with proper permissions
mkdir -p handouts
chmod 755 handouts

# Or specify a different output directory
python3 generate_handout.py --input framework.md --output ~/Documents/handouts
```

---

### Issue: "Module not found" errors

**Error:**
```
ModuleNotFoundError: No module named 'src'
```

**Solution:**
```bash
# Ensure you're in the project root directory
pwd
# Should be: /Volumes/Dev/Course_Generator

# Ensure virtual environment is activated
source venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

---

### Issue: WeasyPrint installation fails on Apple Silicon

**Error:**
```
ERROR: Failed building wheel for weasyprint
```

**Solution:**
```bash
# Install dependencies with ARM-optimized builds
brew install pango gdk-pixbuf cairo libffi

# Set environment variables for compilation
export PKG_CONFIG_PATH="/opt/homebrew/lib/pkgconfig"
export LDFLAGS="-L/opt/homebrew/lib"
export CPPFLAGS="-I/opt/homebrew/include"

# Install WeasyPrint
pip install weasyprint
```

---

### Issue: Large framework files cause memory errors

**Error:**
```
MemoryError: Unable to allocate array
```

**Solution:**
```bash
# Process modules individually instead of batch
python3 generate_handout.py --input frameworks/module-0.md

# Or increase Python memory limit (if using Docker/containers)
# Not typically needed on M1 MacBook Pro with 16GB RAM
```

---

### Getting Help

If you encounter issues not covered here:

1. **Check logs:** `logs/handout_generation.log`
2. **Run with verbose mode:** `python3 generate_handout.py --input file.md --verbose`
3. **Review [TROUBLESHOOTING.md](TROUBLESHOOTING.md)** for more solutions
4. **Check PRD:** `PRD-Student-Handout-Generator-v2.md` for architecture details
5. **Run tests:** `pytest -v` to identify specific component failures

---

## Next Steps

Once installation is complete:

1. **Review configuration:** Edit `handout_config.yaml` to customize settings
2. **Read usage guide:** See [USAGE_GUIDE.md](USAGE_GUIDE.md) for detailed usage instructions
3. **Generate your first handout:** Follow the Quick Start in the usage guide
4. **Review AI-generated questions:** Learn about the question review workflow

---

## Uninstallation

To remove the system:

```bash
# Deactivate virtual environment
deactivate

# Remove virtual environment
rm -rf venv

# Remove generated files
rm -rf handouts
rm -rf logs
rm -rf question_banks

# Remove system dependencies (optional)
brew uninstall pandoc pango gdk-pixbuf libffi
```

---

**Installation guide version:** 1.0
**Last updated:** 2026-01-11
