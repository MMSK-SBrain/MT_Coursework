# Presentation Tools - Framework to Slides Converter

This folder contains tools to convert the markdown lecture frameworks into presentation formats for teaching and video creation.

## Two-Step Workflow

### **Step 1: Marp → PowerPoint** (for editing & distribution)
Convert frameworks to editable PowerPoint presentations with professional engineering theme.

### **Step 2: reveal.js → HTML** (for video recording)
Convert frameworks to interactive HTML presentations optimized for screen capture.

---

## Quick Start

### Prerequisites

**Install Node.js dependencies:**
```bash
cd presentation-tools
npm install
```

This installs:
- `@marp-team/marp-cli` - Markdown to PowerPoint converter
- `reveal-md` - Markdown to HTML presentation converter

### Basic Usage

**Convert single session to PowerPoint:**
```bash
npm run convert:pptx SESSION-01
```

**Convert single session to HTML:**
```bash
npm run convert:html SESSION-01
```

**Convert all sessions (batch):**
```bash
npm run convert:all
```

**Preview session in browser:**
```bash
npm run preview SESSION-01
```

---

## Detailed Instructions

### Step 1: PowerPoint Conversion (Marp)

**Convert one session:**
```bash
./convert-to-pptx.sh SESSION-01-Forces-Framework.md
```

**Batch convert all sessions:**
```bash
./convert-to-pptx.sh --all
```

**Output location:**
```
../presentations/pptx/
├── Session-01-Forces.pptx
├── Session-02-Tires.pptx
├── Session-03-Power.pptx
...
```

**Features:**
- ✅ Professional engineering theme (blue/gray color scheme)
- ✅ Math equation support (LaTeX/KaTeX)
- ✅ Code syntax highlighting
- ✅ Auto-numbered slides with pagination
- ✅ Title slides, content slides, summary slides

### Step 2: HTML Conversion (reveal.js)

**Convert one session:**
```bash
./convert-to-html.sh SESSION-01-Forces-Framework.md
```

**Batch convert all sessions:**
```bash
./convert-to-html.sh --all
```

**Start live preview server:**
```bash
npm run preview SESSION-01
# Opens browser at http://localhost:1948
```

**Output location:**
```
../presentations/html/
├── Session-01-Forces/
│   ├── index.html
│   ├── css/
│   └── js/
├── Session-02-Tires/
...
```

**Features:**
- ✅ Interactive web presentations
- ✅ Keyboard navigation (arrows, space)
- ✅ Speaker notes view (press 'S')
- ✅ Overview mode (press 'O')
- ✅ Perfect for screen recording
- ✅ Mobile-responsive

---

## Framework Preprocessing

Your existing frameworks need minor modifications for optimal conversion:

### Required Changes

**1. Add Marp frontmatter** (for PowerPoint):
```markdown
---
marp: true
theme: engineering
paginate: true
math: katex
---

# Session 1: Forces Acting on a Moving Vehicle
...
```

**2. Add slide breaks:**
Replace your current structure:
```markdown
### SLIDE 1: Title Slide
**Visual:** ...
**Timing:** 1 minute
**Instructor Narrative:**
...
**PPT Content:**
...
```

With simplified Marp format:
```markdown
---

# Forces Acting on a Moving Vehicle
**Session 1 | Module 1: Vehicle Motion Fundamentals**

---

## Newton's Laws Applied to Vehicles

**Instructor Notes:** (in speaker notes)
Today we start with familiar physics...

**Content:**
- First Law: Inertia (object in motion stays in motion)
- Second Law: F = ma
- Third Law: Action-Reaction

---
```

### Automated Preprocessing

Use the provided Python script to automatically convert your frameworks:

```bash
python preprocess-frameworks.py ../lecture-frameworks/SESSION-01-Forces-Framework.md
```

This script:
- ✅ Adds Marp/reveal.js frontmatter
- ✅ Converts `### SLIDE X` to `---` breaks
- ✅ Extracts instructor narratives to speaker notes
- ✅ Preserves formulas, code blocks, tables
- ✅ Outputs to `../presentations/preprocessed/`

---

## Customization

### Marp Theme (PowerPoint styling)

Edit `themes/engineering.css`:

```css
/* Engineering Theme - Professional Blue/Gray */
section {
  background-color: #ffffff;
  color: #333333;
  font-family: 'Segoe UI', Arial, sans-serif;
}

h1 {
  color: #4472C4;
  border-bottom: 3px solid #4472C4;
}

/* Math equations */
.katex {
  font-size: 1.2em;
}

/* Code blocks */
code {
  background-color: #f0f0f0;
  color: #d14;
  padding: 2px 6px;
}
```

### reveal.js Theme (HTML styling)

Edit `themes/reveal-engineering.css`:

```css
.reveal {
  font-family: 'Segoe UI', sans-serif;
  font-size: 38px;
}

.reveal h1 {
  color: #4472C4;
  text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
}

.reveal .slides section {
  text-align: left;
}
```

---

## Video Recording Workflow

### Best Practice for Video Creation

**1. Start reveal.js server:**
```bash
npm run preview SESSION-01
```

**2. Open browser:** `http://localhost:1948`

**3. Enter fullscreen:** Press `F` key

**4. Enable speaker notes:** Press `S` key (opens second window)
   - Main window: Presentation view (for recording)
   - Second window: Speaker notes + timer + preview

**5. Use OBS Studio or similar:**
   - Capture browser window
   - Set resolution: 1920×1080 (Full HD)
   - Frame rate: 30 fps
   - Include audio (microphone)

**6. Navigate slides:**
   - Arrow keys: Next/previous slide
   - Space bar: Next slide
   - Overview: Press `O` to see all slides

**7. Recording tips:**
   - Read speaker notes from second window
   - Pause between slides (edit later)
   - Use laser pointer plugin (press `Q`)

### Example Recording Setup

```bash
# Terminal 1: Start presentation server
cd presentation-tools
npm run preview SESSION-01

# Terminal 2: Monitor (optional)
# Watch for file changes and auto-reload
npm run watch SESSION-01

# Browser:
# Main display → http://localhost:1948 (fullscreen for recording)
# Second display → http://localhost:1948/?print-pdf (speaker notes)
```

---

## Advanced Features

### Mathematical Equations

Both Marp and reveal.js support LaTeX math via KaTeX:

**Inline math:**
```markdown
The force is calculated as $F = m \times a$
```

**Display math:**
```markdown
$$
F_{\text{rolling}} = C_r \times m \times g
$$

$$
F_{\text{drag}} = \frac{1}{2} \rho C_d A v^2
$$
```

### Code Blocks with Syntax Highlighting

```markdown
```python
def calculate_force(mass, acceleration):
    """Calculate force using F = ma"""
    return mass * acceleration

force = calculate_force(1500, 2.5)  # 3750 N
```
```

### Tables

```markdown
| Parameter | Value | Unit |
|-----------|-------|------|
| Mass (m) | 1500 | kg |
| Acceleration (a) | 2.5 | m/s² |
| Force (F) | 3750 | N |
```

### Images

```markdown
![Force Diagram](../assets/force-diagram.png)
```

### Two-Column Layouts (reveal.js)

```html
<div class="columns">
<div class="column">

**Left Column:**
- Point 1
- Point 2

</div>
<div class="column">

**Right Column:**
- Point A
- Point B

</div>
</div>
```

---

## Troubleshooting

### Common Issues

**1. Marp not converting math equations:**
```bash
# Ensure KaTeX is enabled in frontmatter
---
marp: true
math: katex
---
```

**2. reveal.js slides not breaking correctly:**
```markdown
# Use triple-dash for horizontal breaks
---

# Use double-dash for vertical breaks (subsections)
--
```

**3. Images not loading:**
```bash
# Use relative paths from framework location
![Diagram](../assets/diagrams/force-body-diagram.png)

# Or copy images to output folder
cp -r ../assets output/html/Session-01/
```

**4. Theme not applying:**
```bash
# Verify theme file exists
ls themes/engineering.css

# Specify theme explicitly
marp --theme themes/engineering.css SESSION-01.md
```

### Getting Help

**Marp Documentation:** https://marpit.marp.app/
**reveal.js Documentation:** https://revealjs.com/
**KaTeX Math:** https://katex.org/docs/supported.html

---

## File Structure

```
automotive-vehicles-aelzc441/          # Course root
│
├── lecture-frameworks/                # Original frameworks (18 sessions)
│   ├── SESSION-01-Forces-Framework.md
│   ├── SESSION-02-Tires-Framework.md
│   └── ... (all 18 sessions)
│
├── presentations/                     # Generated presentations (OUTPUT)
│   ├── pptx/                         # PowerPoint files
│   │   ├── Session-01-Forces.pptx
│   │   ├── Session-02-Tires.pptx
│   │   └── ... (all sessions)
│   ├── html/                         # HTML presentations (for video)
│   │   ├── Session-01-Forces/
│   │   │   ├── index.html
│   │   │   ├── css/
│   │   │   └── js/
│   │   └── ... (all sessions)
│   └── preprocessed/                 # Intermediate markdown
│       └── ... (preprocessed files)
│
└── presentation-tools/               # Conversion scripts (THIS FOLDER)
    ├── README.md                     # This file
    ├── package.json                  # Node.js dependencies
    ├── package-lock.json             # Dependency lock file
    │
    ├── convert-to-pptx.sh           # Marp conversion script
    ├── convert-to-html.sh           # reveal.js conversion script
    ├── convert-all.py               # Master conversion script
    │
    ├── themes/
    │   ├── engineering.css          # Marp theme (PowerPoint styling)
    │   └── reveal-engineering.css   # reveal.js theme (HTML styling)
    │
    ├── templates/
    │   └── marp-template.md         # Example Marp slide structure
    │
    └── examples/
        └── SESSION-01-preprocessed.md # Example preprocessed framework
```

---

## Batch Conversion

### Convert All 18 Sessions

**Full automation:**
```bash
# 1. Preprocess all frameworks
python convert-all.py --preprocess

# 2. Convert to PowerPoint
npm run convert:all:pptx

# 3. Convert to HTML
npm run convert:all:html

# Or all in one command:
npm run convert:all
```

**Expected output:**
```
✅ Preprocessing complete: 18 sessions
✅ PowerPoint conversion: 18/18 sessions
✅ HTML conversion: 18/18 sessions

Output files:
- output/pptx/*.pptx (18 files)
- output/html/Session-*/ (18 folders)

Total time: ~5-10 minutes
```

---

## Quality Checklist

Before using presentations, verify:

### PowerPoint (PPTX)
- [ ] All slides render correctly
- [ ] Math equations display properly
- [ ] Images are embedded (not broken links)
- [ ] Code blocks have syntax highlighting
- [ ] Page numbers appear on all slides
- [ ] Theme colors are consistent (blue/gray)
- [ ] Font sizes are readable (minimum 18pt)

### HTML (reveal.js)
- [ ] Navigation works (arrow keys)
- [ ] Speaker notes accessible (press 'S')
- [ ] Math equations render (KaTeX loaded)
- [ ] Images load correctly
- [ ] Overview mode works (press 'O')
- [ ] Fullscreen works (press 'F')
- [ ] Responsive on different screen sizes

### Content
- [ ] All 6 learning outcomes covered
- [ ] Instructor narratives converted to speaker notes
- [ ] Formulas and calculations accurate
- [ ] Examples and practice problems included
- [ ] Connections to previous/next sessions mentioned

---

## Performance Tips

**Speed up conversions:**
- Use `--parallel` flag for batch processing
- Cache processed images in `output/assets/`
- Use lightweight theme (fewer CSS rules)

**Optimize for file size:**
- Compress images before including: `pngquant`, `jpegoptim`
- Use vector graphics (SVG) where possible
- Remove unused theme assets

**Improve rendering:**
- Pre-render math equations for PowerPoint
- Use web fonts (Google Fonts) for consistency
- Test on target display resolution (1920×1080)

---

## Next Steps

1. **Install dependencies:**
   ```bash
   cd presentation-tools
   npm install
   ```

2. **Test with one session:**
   ```bash
   npm run convert:pptx SESSION-01
   npm run preview SESSION-01
   ```

3. **Review output quality:**
   - Open `output/pptx/Session-01-Forces.pptx`
   - Browse to `http://localhost:1948` (if preview running)

4. **Customize themes:**
   - Edit `themes/engineering.css`
   - Edit `themes/reveal-engineering.css`

5. **Batch convert all sessions:**
   ```bash
   npm run convert:all
   ```

6. **Start recording videos:**
   - Use reveal.js HTML output
   - OBS Studio or Camtasia
   - Follow video recording workflow above

---

## License & Credits

**Tools Used:**
- Marp: https://marp.app/ (MIT License)
- reveal.js: https://revealjs.com/ (MIT License)
- KaTeX: https://katex.org/ (MIT License)

**Frameworks Created By:**
Course: Automotive Vehicles (AEL ZC441)
Institution: [Your Institution]
Date: 2026-01-03

---

**Questions or issues?**
Check the troubleshooting section or consult tool documentation.

**Happy presenting! 🚗📊**
