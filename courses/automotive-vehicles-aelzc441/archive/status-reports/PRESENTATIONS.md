# Presentations - Automotive Vehicles (AEL ZC441)

This document explains how to generate and manage PowerPoint presentations for this course.

## Directory Structure

```
automotive-vehicles-aelzc441/
├── lecture-frameworks/           # Source markdown lecture frameworks
├── presentations/
│   └── pptx/                    # Final PowerPoint presentations (19 files)
└── PRESENTATIONS.md             # This file
```

## Generated Presentations

All 19 PowerPoint presentations have been generated from the lecture frameworks:

- **Sessions 1-10**: Module 1-3 (Forces, Tires, Power, IC Engines, Cooling/Lubrication, Fuel Systems, Transmission 1 & 2, Vehicle Dynamics, Braking Systems)
- **Sessions 11-15**: Module 4 (Steering Systems, Suspension Systems, Electrical Architecture, Vehicle Control Systems, Communication Networks)
- **Sessions 16-18**: Module 5 (Chassis & Body Architecture, HVAC Systems, Passive Safety Systems Part 1 & 2)

**Format**: 16:9 widescreen
**Total Slides**: 673 slides across all sessions
**Text**: Fully editable native PowerPoint text boxes
**Styling**: Professional engineering theme (blue #4472C4, gray #333)

## How to Regenerate Presentations

If you need to regenerate presentations after updating the lecture frameworks, use the shared tools:

### Prerequisites

```bash
# Install Python dependencies
pip install python-pptx
```

### Step 1: Preprocess Framework Markdown

From the course directory:

```bash
python3 ../../tools/presentation-tools/preprocess-framework.py \
    lecture-frameworks/SESSION-XX-Topic-Framework.md \
    presentations/preprocessed/
```

### Step 2: Convert to PowerPoint

```bash
python3 ../../tools/presentation-tools/markdown-to-pptx.py \
    presentations/preprocessed/SESSION-XX-Topic-Framework.md \
    presentations/pptx/
```

### Batch Processing

To regenerate all presentations:

```bash
# From the course directory
mkdir -p presentations/preprocessed

# Preprocess all frameworks
for file in lecture-frameworks/SESSION-*.md; do
    python3 ../../tools/presentation-tools/preprocess-framework.py \
        "$file" \
        presentations/preprocessed/
done

# Convert all to PowerPoint
for file in presentations/preprocessed/SESSION-*.md; do
    python3 ../../tools/presentation-tools/markdown-to-pptx.py \
        "$file" \
        presentations/pptx/
done

# Clean up intermediate files (optional)
rm -rf presentations/preprocessed/
```

## Presentation Features

### Professional Styling
- Title slides with blue background (#4472C4)
- Content slides with clean white background
- Consistent typography with Calibri font
- Professional color scheme throughout

### Fully Editable
- All text is native PowerPoint text boxes (not images)
- Bullet points are properly formatted
- Easy to customize and update

### Content Structure
- Each session starts with a title slide
- Content organized into logical slide sections
- Code blocks formatted with monospace font
- Proper slide breaks and spacing

## Tools Location

The shared presentation tools are located at:
```
/Volumes/Dev/Course_Generator/tools/presentation-tools/
```

These tools are generic and can be used for any course. See the README in that directory for detailed documentation.

## Need Help?

For questions about:
- **Content**: Refer to the lecture frameworks in `lecture-frameworks/`
- **Presentation Generation**: See `/Volumes/Dev/Course_Generator/tools/presentation-tools/README.md`
- **Course Structure**: See the main `README.md` in this directory
