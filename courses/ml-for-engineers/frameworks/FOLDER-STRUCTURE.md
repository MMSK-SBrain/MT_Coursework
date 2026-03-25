# Production Folder Structure
## ML for Engineers Course Materials Organization

**Created:** 2026-01-05
**Purpose:** Organize all production materials for course development

---

## Complete Folder Structure

```
courses/ml-for-engineers/
├── frameworks/                          # Course planning documents
│   ├── MASTER-COURSE-PLAN.md
│   ├── COURSE-PROGRESSION-ANALYSIS.md
│   ├── IMPLEMENTATION-SUMMARY.md
│   ├── COMPLETE-COURSE-SUMMARY.md
│   ├── PRODUCTION-READINESS-ASSESSMENT.md
│   ├── USER-STORIES-ALL-MODULES.md
│   ├── FOLDER-STRUCTURE.md
│   ├── module-0-framework-REVISED.md
│   ├── module-1-framework-REVISED.md
│   ├── module-2-framework-classification.md
│   ├── module-3-framework-regression.md
│   ├── modules-4-10-frameworks.md
│   ├── learning-outcomes.json
│   └── assessment-and-activities-COMPLETE.json
│
├── production/                          # All production-ready materials
│   │
│   ├── module-0/                        # Module 0: The Hook
│   │   ├── demo-apps/                   # 5 demo applications
│   │   │   ├── stock-predictor/
│   │   │   │   ├── app.py               # Streamlit/Flask app
│   │   │   │   ├── model.pkl            # Trained model
│   │   │   │   ├── requirements.txt
│   │   │   │   ├── README.md            # Deployment instructions
│   │   │   │   └── data/                # Sample data
│   │   │   ├── cricket-predictor/
│   │   │   │   ├── app.py
│   │   │   │   ├── model.pkl
│   │   │   │   ├── requirements.txt
│   │   │   │   └── README.md
│   │   │   ├── face-detection/
│   │   │   │   ├── app.py
│   │   │   │   ├── requirements.txt
│   │   │   │   └── README.md
│   │   │   ├── sentiment-analyzer/
│   │   │   │   ├── app.py
│   │   │   │   ├── model.pkl
│   │   │   │   ├── requirements.txt
│   │   │   │   └── README.md
│   │   │   └── chatbot/
│   │   │       ├── app.py
│   │   │       ├── intents.json         # Chatbot intents
│   │   │       ├── requirements.txt
│   │   │       └── README.md
│   │   │
│   │   ├── code/                        # Code examples
│   │   │   ├── iris-classifier-complete.ipynb
│   │   │   └── library-verification.ipynb
│   │   │
│   │   ├── setup-guides/                # Setup documentation
│   │   │   ├── ChatGPT-Setup-Guide.md
│   │   │   ├── Gemini-Setup-Guide.md
│   │   │   ├── Claude-Setup-Guide.md
│   │   │   ├── Google-Colab-Setup-Guide.md
│   │   │   ├── LLM-Comparison.md
│   │   │   └── screenshots/             # Setup screenshots
│   │   │
│   │   ├── visual-assets/               # Graphics and diagrams
│   │   │   ├── course-roadmap.png
│   │   │   ├── module-0-overview.png
│   │   │   ├── cpu-vs-gpu.png
│   │   │   ├── llm-comparison-chart.png
│   │   │   ├── welcome-slides.pdf
│   │   │   └── source/                  # Editable files (Figma/Canva)
│   │   │
│   │   ├── quizzes/                     # Quiz questions
│   │   │   ├── session-1-quiz.json
│   │   │   ├── session-2-quiz.json
│   │   │   ├── session-3-quiz.json
│   │   │   └── module-0-quizzes.csv
│   │   │
│   │   ├── video-scripts/               # Video scripts
│   │   │   ├── session-1/
│   │   │   ├── session-2/
│   │   │   └── session-3/
│   │   │
│   │   └── README.md                    # Module 0 production overview
│   │
│   ├── module-1/                        # Module 1: Foundations
│   │   ├── datasets/                    # Stock datasets
│   │   │   ├── AAPL_5y.csv
│   │   │   ├── GOOGL_5y.csv
│   │   │   ├── TSLA_5y.csv
│   │   │   ├── MSFT_5y.csv
│   │   │   ├── INFY_5y.csv
│   │   │   ├── TCS_5y.csv
│   │   │   ├── RELIANCE_5y.csv
│   │   │   ├── dataset-readme.md        # Data dictionary
│   │   │   └── download-script.py       # Auto-download script
│   │   │
│   │   ├── code/                        # Code examples
│   │   │   ├── pandas-stock-exploration.ipynb
│   │   │   ├── stock-visualization-complete.ipynb
│   │   │   ├── data-quality-check.ipynb
│   │   │   └── prompts-used.md          # AI prompts used
│   │   │
│   │   ├── templates/                   # Templates for learners
│   │   │   ├── prompt-library-template.xlsx
│   │   │   ├── stock-exploration-template.ipynb
│   │   │   └── prompt-engineering-tips.md
│   │   │
│   │   ├── visual-assets/               # Graphics
│   │   │   ├── ml-types-diagram.png
│   │   │   ├── classification-vs-regression.png
│   │   │   ├── ml-pipeline.png
│   │   │   ├── data-structure.png
│   │   │   ├── pandas-cheatsheet.png
│   │   │   └── source/
│   │   │
│   │   ├── quizzes/                     # Assessments
│   │   │   ├── session-1-quiz.json
│   │   │   ├── session-2-quiz.json
│   │   │   ├── session-3-quiz.json
│   │   │   ├── session-4-quiz.json
│   │   │   └── module-1-quizzes.csv
│   │   │
│   │   ├── rubrics/                     # Grading rubrics
│   │   │   ├── stock-exploration-rubric.pdf
│   │   │   ├── self-assessment.pdf
│   │   │   └── example-submissions/
│   │   │
│   │   ├── video-scripts/
│   │   │   ├── session-1/
│   │   │   ├── session-2/
│   │   │   ├── session-3/
│   │   │   └── session-4/
│   │   │
│   │   └── README.md
│   │
│   ├── module-2/                        # Module 2: Classification
│   │   ├── datasets/                    # All classification datasets
│   │   │   ├── iris/
│   │   │   ├── spam-emails/
│   │   │   ├── customer-churn/
│   │   │   ├── heart-disease/
│   │   │   ├── mnist/
│   │   │   ├── cricket-matches/
│   │   │   └── datasets-readme.md
│   │   │
│   │   ├── projects/                    # Complete projects
│   │   │   ├── 01-iris-classifier/
│   │   │   │   ├── iris-classifier-complete.ipynb
│   │   │   │   ├── prompts-used.md
│   │   │   │   └── README.md
│   │   │   ├── 02-spam-detector/
│   │   │   │   ├── spam-classifier-complete.ipynb
│   │   │   │   └── README.md
│   │   │   ├── 03-churn-predictor/
│   │   │   │   ├── churn-predictor-complete.ipynb
│   │   │   │   └── README.md
│   │   │   ├── 04-heart-disease/
│   │   │   │   ├── heart-disease-predictor.ipynb
│   │   │   │   └── README.md
│   │   │   ├── 05-mnist-classifier/
│   │   │   │   ├── mnist-classifier.ipynb
│   │   │   │   └── README.md
│   │   │   ├── 06-cricket-predictor/
│   │   │   │   ├── cricket-match-predictor.ipynb
│   │   │   │   └── README.md
│   │   │   └── classification-metrics-complete.ipynb
│   │   │
│   │   ├── visual-assets/
│   │   │   ├── decision-tree-viz.png
│   │   │   ├── confusion-matrix-explained.png
│   │   │   ├── roc-curve-explained.png
│   │   │   ├── precision-recall-tradeoff.png
│   │   │   └── source/
│   │   │
│   │   ├── quizzes/
│   │   │   ├── session-*.json
│   │   │   └── module-2-quizzes.csv
│   │   │
│   │   ├── rubrics/
│   │   │   ├── project-rubrics.pdf
│   │   │   └── example-submissions/
│   │   │
│   │   ├── video-scripts/
│   │   │   └── session-*/
│   │   │
│   │   └── README.md
│   │
│   ├── module-3/                        # Module 3: Regression
│   │   ├── datasets/
│   │   │   ├── house-prices/
│   │   │   ├── stock-data/              # Extended from Module 1
│   │   │   ├── sales-forecasting/
│   │   │   ├── cricket-scores/
│   │   │   ├── energy-consumption/
│   │   │   ├── salary-data/
│   │   │   └── datasets-readme.md
│   │   │
│   │   ├── feature-engineering/         # Feature engineering library
│   │   │   ├── feature_engineering.py   # Python module
│   │   │   ├── feature-engineering-guide.ipynb
│   │   │   ├── technical-indicators.md
│   │   │   └── README.md
│   │   │
│   │   ├── projects/
│   │   │   ├── 01-house-price-predictor/
│   │   │   ├── 02-stock-predictor-PAYOFF/    # THE MAIN PROJECT
│   │   │   │   ├── stock-predictor-COMPLETE.ipynb
│   │   │   │   ├── model.pkl
│   │   │   │   ├── deployment-ready/
│   │   │   │   └── README.md
│   │   │   ├── 03-sales-forecasting/
│   │   │   ├── 04-cricket-score-predictor/
│   │   │   ├── 05-energy-predictor/
│   │   │   ├── 06-salary-predictor/
│   │   │   ├── regression-metrics-complete.ipynb
│   │   │   └── backtesting-framework.py
│   │   │
│   │   ├── visual-assets/
│   │   │   ├── linear-regression-viz.png
│   │   │   ├── residual-plots.png
│   │   │   ├── technical-indicators-explained.png
│   │   │   └── source/
│   │   │
│   │   ├── quizzes/
│   │   │   └── *.json
│   │   │
│   │   ├── rubrics/
│   │   │   ├── stock-predictor-rubric.pdf    # Detailed!
│   │   │   └── example-submissions/
│   │   │
│   │   ├── video-scripts/
│   │   │   └── session-*/
│   │   │
│   │   └── README.md
│   │
│   ├── module-4/                        # To be created
│   ├── module-5/
│   ├── module-6/
│   ├── module-7/
│   ├── module-8/
│   ├── module-9/
│   ├── module-10/
│   │
│   └── shared/                          # Shared resources
│       ├── templates/                   # Reusable templates
│       │   ├── notebook-template.ipynb
│       │   ├── project-readme-template.md
│       │   └── quiz-template.json
│       │
│       ├── utilities/                   # Helper scripts
│       │   ├── dataset-downloader.py
│       │   ├── quiz-converter.py
│       │   └── model-evaluator.py
│       │
│       └── brand-assets/               # Brand materials
│           ├── logo.png
│           ├── colors.md
│           └── fonts/
│
└── deliverables/                        # Final course deliverables
    ├── videos/                          # Rendered videos
    │   ├── module-0/
    │   ├── module-1/
    │   └── ...
    │
    ├── lms-import/                      # LMS-ready files
    │   ├── quizzes/
    │   ├── assignments/
    │   └── course-structure.xml
    │
    └── student-materials/               # Student download packages
        ├── module-0-materials.zip
        ├── module-1-materials.zip
        └── ...
```

---

## Folder Naming Conventions

### Files
- Notebooks: `lowercase-with-hyphens.ipynb`
- Python modules: `snake_case.py`
- Markdown docs: `Title-Case-With-Hyphens.md`
- Data files: `UPPERCASE-ticker_period.csv`
- Quizzes: `session-N-quiz.json`

### Directories
- Lowercase with hyphens: `demo-apps/`, `visual-assets/`
- Module folders: `module-N/`
- Project folders: `01-project-name/`, `02-project-name/`

---

## File Size Guidelines

### To Prevent Context Issues
- **Notebooks:** Keep under 500 lines; split if larger
- **Markdown:** Keep under 1000 lines; split into sections
- **Data files:** Provide download scripts for files > 10MB
- **Images:** Optimize PNGs (< 2MB each)

### Splitting Strategy
If a notebook/file gets too large:
```
original-notebook.ipynb
→ Split into:
  - part-1-data-loading.ipynb
  - part-2-exploration.ipynb
  - part-3-modeling.ipynb
```

---

## README.md Structure

Each module folder should have:

```markdown
# Module N: Title

## Overview
Brief description

## Contents
- List of all materials
- What's included
- What's production-ready

## User Stories Completed
- [x] Story 1
- [x] Story 2
- [ ] Story 3 (in progress)

## Quick Start
How to use these materials

## Dependencies
Software/library requirements

## Status
Current completion status
```

---

## Usage Instructions

### For Instructors
1. Navigate to `production/module-N/`
2. Review README.md for overview
3. Access materials by category (code/, datasets/, etc.)
4. Use video-scripts/ for recording
5. Use quizzes/ for LMS import

### For Developers (Creating Materials)
1. Work in `production/module-N/` appropriate subfolder
2. Follow naming conventions
3. Update README.md when adding materials
4. Test all code before committing
5. Document AI prompts used

### For Students (After Launch)
Materials will be packaged from:
- `production/module-N/code/` → Student downloads
- `production/module-N/datasets/` → Student downloads
- `deliverables/student-materials/` → Final packages

---

## Git Ignore Recommendations

```gitignore
# Large files
*.pkl
*.h5
*.model
datasets/*.csv (if >10MB)

# Temporary files
*.tmp
.ipynb_checkpoints/
__pycache__/

# Environment
.env
venv/
```

---

## Backup Strategy

### Critical Files (Daily Backup)
- All code notebooks
- All datasets (or download scripts)
- All quizzes
- All rubrics

### Important Files (Weekly Backup)
- Visual assets (source files)
- Video scripts
- Documentation

---

## Status Tracking

### Module 0
- [ ] demo-apps/ (0/5 complete)
- [ ] code/ (0/2 complete)
- [ ] setup-guides/ (0/5 complete)
- [ ] visual-assets/ (0% complete)
- [ ] quizzes/ (0/3 complete)
- [ ] video-scripts/ (not started)

### Module 1
- [ ] datasets/ (0/7 complete)
- [ ] code/ (0/3 complete)
- [ ] templates/ (0/3 complete)
- [ ] visual-assets/ (0% complete)
- [ ] quizzes/ (0/4 complete)
- [ ] rubrics/ (0/1 complete)
- [ ] video-scripts/ (not started)

### Module 2
- [ ] datasets/ (0/6 complete)
- [ ] projects/ (0/7 complete)
- [ ] visual-assets/ (0% complete)
- [ ] quizzes/ (0/6 complete)
- [ ] rubrics/ (0/1 complete)
- [ ] video-scripts/ (not started)

### Module 3
- [ ] datasets/ (0/6 complete)
- [ ] feature-engineering/ (0% complete)
- [ ] projects/ (0/8 complete)
- [ ] visual-assets/ (0% complete)
- [ ] quizzes/ (0/6 complete)
- [ ] rubrics/ (0/1 complete)
- [ ] video-scripts/ (not started)

---

**Created:** 2026-01-05
**Version:** 1.0
**Status:** STRUCTURE DEFINED, READY TO CREATE FOLDERS
