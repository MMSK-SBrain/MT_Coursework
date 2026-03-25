# Presentation Tools - Usage Guide

Generic tools for converting lecture framework markdown files into PowerPoint presentations.

## Overview

This toolset provides a two-step workflow:
1. **Preprocess**: Convert instructor-led story frameworks to clean slide markdown
2. **Convert**: Transform slide markdown into editable PowerPoint presentations

## Tools

### 1. preprocess-framework.py

Converts instructor-led story framework markdown to Marp-compatible slide format.

**What it does:**
- Extracts slide content from `## Slide X:`, `### SLIDE X:`, `#### Slide X:`, or `##### Slide X:` markers
- Removes instructor script markers and HTML comments
- Cleans up visual descriptions and formatting
- Adds Marp frontmatter
- Separates slides with `---` markers

**Usage:**
```bash
python3 preprocess-framework.py <input-framework.md> [output-dir]
```

**Arguments:**
- `input-framework.md` - Path to the lecture framework markdown file
- `output-dir` - (Optional) Output directory for preprocessed files. Defaults to `./preprocessed/`

**Example:**
```bash
# Use default output directory (./preprocessed/)
python3 preprocess-framework.py ../../courses/my-course/frameworks/SESSION-01.md

# Specify custom output directory
python3 preprocess-framework.py \
    ../../courses/my-course/frameworks/SESSION-01.md \
    ../../courses/my-course/presentations/preprocessed/
```

### 2. markdown-to-pptx.py

Converts preprocessed markdown slides into fully editable PowerPoint presentations.

**What it does:**
- Parses markdown slides separated by `---`
- Creates native PowerPoint text boxes (fully editable)
- Applies professional engineering theme styling
- Generates 16:9 widescreen presentations
- Handles title slides, content slides, bullet points, and code blocks

**Usage:**
```bash
python3 markdown-to-pptx.py <input-markdown.md> [output-dir]
```

**Arguments:**
- `input-markdown.md` - Path to the preprocessed markdown file
- `output-dir` - (Optional) Output directory for PowerPoint files. Defaults to `./pptx/`

**Example:**
```bash
# Use default output directory (./pptx/)
python3 markdown-to-pptx.py preprocessed/SESSION-01.md

# Specify custom output directory
python3 markdown-to-pptx.py \
    ../../courses/my-course/presentations/preprocessed/SESSION-01.md \
    ../../courses/my-course/presentations/pptx/
```

## Prerequisites

**Python Dependencies:**
```bash
pip install python-pptx
```

## Complete Workflow Example

### Single File Conversion

```bash
# Navigate to your course directory
cd /path/to/Course_Generator/courses/my-course/

# Step 1: Preprocess the framework
python3 ../../tools/presentation-tools/preprocess-framework.py \
    lecture-frameworks/SESSION-01-Topic-Framework.md \
    presentations/preprocessed/

# Step 2: Convert to PowerPoint
python3 ../../tools/presentation-tools/markdown-to-pptx.py \
    presentations/preprocessed/SESSION-01-Topic-Framework.md \
    presentations/pptx/
```

### Batch Processing All Sessions

```bash
# Navigate to your course directory
cd /path/to/Course_Generator/courses/my-course/

# Create output directories
mkdir -p presentations/preprocessed
mkdir -p presentations/pptx

# Preprocess all frameworks
for file in lecture-frameworks/SESSION-*.md; do
    echo "Preprocessing $(basename $file)..."
    python3 ../../tools/presentation-tools/preprocess-framework.py \
        "$file" \
        presentations/preprocessed/
done

# Convert all to PowerPoint
for file in presentations/preprocessed/SESSION-*.md; do
    echo "Converting $(basename $file)..."
    python3 ../../tools/presentation-tools/markdown-to-pptx.py \
        "$file" \
        presentations/pptx/
done

# Optional: Clean up intermediate files
rm -rf presentations/preprocessed/

echo "✓ All presentations generated in presentations/pptx/"
```

## Presentation Styling

### Color Scheme
- **Primary Blue**: #4472C4 (titles, accents)
- **Dark Blue**: #2E5090 (subtitles)
- **Text Gray**: #333333 (body text)
- **Light Gray**: #5A5A5A (secondary text)
- **Accent Orange**: #FF6600 (highlights, reserved for future use)
- **White**: #FFFFFF (backgrounds, title text)

### Slide Types

**Title Slide:**
- Blue background (#4472C4)
- Large white title text (44pt, bold)
- Subtitle text (24pt)
- Detected by markdown H1 headers on first slide

**Content Slide:**
- White background
- Subtitle in dark blue (24pt, bold)
- Bullet points in gray (18pt)
- Proper indentation for nested bullets
- Code blocks in monospace Consolas font (14pt)

### Typography
- **Headings**: Calibri Bold
- **Body Text**: Calibri Regular
- **Code**: Consolas

## Framework Markdown Requirements

For best results, your lecture framework markdown should follow this structure:

```markdown
# Session X: Topic Name

## Slide 1: Introduction
Content for first slide...

## Slide 2: Key Concepts
- Bullet point 1
- Bullet point 2
  - Nested bullet

## Slide 3: Code Example
```code
Example code here
```
```

**Supported slide markers:**
- `## Slide X: Title`
- `### SLIDE X: Title` (case-insensitive)
- `#### Slide X: Title`
- `##### Slide X: Title`

## Troubleshooting

**No slides generated:**
- Check that your markdown uses one of the supported slide marker formats
- Ensure slide content is not empty (minimum 10 characters)
- Verify the markdown file is properly formatted

**Text not appearing:**
- Check for excessive HTML comments that might be removing content
- Ensure content is not wrapped in unsupported markdown syntax

**Styling issues:**
- PowerPoint files are fully editable - you can adjust styling manually if needed
- Check that the python-pptx library is installed and up to date

## Integration with Other Courses

These tools are designed to be course-agnostic. To use them with a new course:

1. Organize your course in this structure:
   ```
   courses/my-new-course/
   ├── lecture-frameworks/      # Your markdown frameworks
   └── presentations/
       └── pptx/                # Generated PowerPoint files
   ```

2. Run the tools from your course directory using relative paths to `../../tools/presentation-tools/`

3. Customize the color scheme by editing `markdown-to-pptx.py` if needed

## Support

For issues or questions:
- Check the README in the main Course_Generator directory
- Review example frameworks in existing courses
- Ensure all prerequisites are installed

## Version History

- **v1.0** (2026-01-03): Initial modular release
  - Support for multiple markdown heading levels
  - Configurable output directories
  - Professional engineering theme
  - 16:9 widescreen format
