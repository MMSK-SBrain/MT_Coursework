# User Stories: ML for Engineers Course Production
## Complete Backlog for All Modules

**Created:** 2026-01-05
**Total Stories:** 55
**Estimated Total Effort:** 615-910 hours
**Approach:** Sequential by module (0 → 1 → 2 → 3 → 4-10)

---

## Story Numbering Convention
`M[Module]-[Category]-[Number]`

**Categories:**
- **DEMO:** Demo application development
- **DATA:** Dataset sourcing and preparation
- **CODE:** Code examples and projects
- **VIZ:** Visual assets (diagrams, graphics)
- **ASSESS:** Assessment materials (quizzes, rubrics)
- **SETUP:** Setup and configuration guides
- **EXPAND:** Module framework expansion

---

# MODULE 0: THE HOOK

## M0-DEMO-01: Stock Predictor Demo App

**As an instructor**
I need a deployed stock price predictor web application
So that learners can see a working ML application in the first session

### Acceptance Criteria
- [ ] Web app built using Streamlit or Flask
- [ ] Predicts stock prices for AAPL, GOOGL, TSLA (minimum)
- [ ] Takes stock ticker and date range as input
- [ ] Shows prediction, direction (up/down), confidence level
- [ ] Displays historical accuracy chart
- [ ] Deployed to public URL (Heroku/Streamlit Cloud)
- [ ] Loads in < 3 seconds
- [ ] Works on mobile and desktop
- [ ] Source code documented and in repository
- [ ] Includes simple ML model (Random Forest or LSTM)

### Technical Specifications
- **Frontend:** Streamlit (easier) or Flask + HTML/CSS
- **Backend:** Python, scikit-learn or TensorFlow
- **Data Source:** yfinance library for real-time stock data
- **Model:** Pre-trained Random Forest or LSTM saved as pickle
- **Hosting:** Streamlit Cloud (free) or Heroku (paid)
- **Features to show:**
  - Stock selection dropdown
  - Date range picker
  - Prediction button
  - Results display (price, direction, confidence)
  - Historical chart
  - Accuracy metrics display

### Estimated Effort
**10-12 hours**
- Design: 2 hours
- Model training: 3-4 hours
- Frontend development: 3-4 hours
- Deployment: 2 hours
- Testing: 1 hour

### Priority
**CRITICAL** - Blocks Module 0 video recording

### Dependencies
None - can start immediately

---

## M0-DEMO-02: Cricket Match Predictor Demo App

**As an instructor**
I need a deployed cricket match outcome predictor
So that learners (especially in India) see ML applied to sports

### Acceptance Criteria
- [ ] Web app predicts cricket match outcomes
- [ ] Takes team names, venue, toss winner as input
- [ ] Shows win probability for both teams
- [ ] Displays key factors influencing prediction
- [ ] Deployed to public URL
- [ ] Works across devices
- [ ] Source code documented

### Technical Specifications
- **Frontend:** Streamlit
- **Model:** Logistic Regression or Random Forest
- **Data Source:** Kaggle cricket dataset or ESPN Cricinfo
- **Features:** Team names, venue, toss, recent form
- **Output:** Win probabilities, key factors

### Estimated Effort
**8-10 hours**

### Priority
**HIGH** - Needed for Module 0, appeals to target audience

### Dependencies
- Cricket match dataset (Kaggle)

---

## M0-DEMO-03: Face Detection & Recognition Demo App

**As an instructor**
I need a face detection/recognition demo
So that learners see computer vision in action

### Acceptance Criteria
- [ ] Web app detects faces in uploaded images
- [ ] Draws bounding boxes around faces
- [ ] Optionally recognizes known faces (if trained)
- [ ] Shows confidence scores
- [ ] Real-time webcam option (bonus)
- [ ] Deployed to public URL
- [ ] Source code documented

### Technical Specifications
- **Frontend:** Streamlit with file uploader
- **Model:** OpenCV Haar Cascades or MTCNN
- **Libraries:** OpenCV, face_recognition
- **Features:** Image upload, face detection, bounding boxes
- **Optional:** Face recognition for demo celebrities

### Estimated Effort
**6-8 hours**

### Priority
**HIGH** - Visual "wow" factor

### Dependencies
None - pre-trained models available

---

## M0-DEMO-04: Sentiment Analyzer Demo App

**As an instructor**
I need a sentiment analysis demo
So that learners see NLP application in social media context

### Acceptance Criteria
- [ ] Web app analyzes text sentiment
- [ ] Takes user input text or tweet
- [ ] Shows sentiment (Positive/Negative/Neutral)
- [ ] Shows confidence score
- [ ] Highlights key words
- [ ] Works with social media text (emojis, slang)
- [ ] Deployed to public URL

### Technical Specifications
- **Frontend:** Streamlit with text input
- **Model:** Pre-trained BERT or VADER
- **Libraries:** transformers, nltk
- **Features:** Text input, sentiment classification, word highlighting

### Estimated Effort
**6-8 hours**

### Priority
**MEDIUM** - Good for NLP introduction

### Dependencies
Pre-trained BERT model (Hugging Face)

---

## M0-DEMO-05: Customer Support Chatbot Demo App

**As an instructor**
I need a simple chatbot demo
So that learners see conversational AI in action

### Acceptance Criteria
- [ ] Web app with chat interface
- [ ] Responds to common customer queries
- [ ] Shows typing indicator
- [ ] Maintains conversation history
- [ ] Falls back gracefully for unknown queries
- [ ] Deployed to public URL

### Technical Specifications
- **Frontend:** Streamlit or Gradio
- **Backend:** Rule-based + simple NLP or OpenAI API (limited)
- **Features:** Chat interface, intent recognition, canned responses
- **Optional:** Integration with real LLM API for demo purposes

### Estimated Effort
**8-10 hours**

### Priority
**MEDIUM** - Shows conversational AI

### Dependencies
None (can use rule-based initially)

---

## M0-SETUP-01: LLM Account Setup Guides

**As an instructor**
I need detailed setup guides for ChatGPT, Gemini, and Claude
So that learners can create accounts without assistance

### Acceptance Criteria
- [ ] ChatGPT setup guide (step-by-step with screenshots)
- [ ] Google Gemini setup guide
- [ ] Claude setup guide
- [ ] Account creation process documented
- [ ] Free vs paid tier comparison
- [ ] API access overview (for later modules)
- [ ] Troubleshooting common issues
- [ ] All guides in PDF and/or markdown format

### Deliverables
1. `ChatGPT-Setup-Guide.pdf`
2. `Gemini-Setup-Guide.pdf`
3. `Claude-Setup-Guide.pdf`
4. `LLM-Comparison-Chart.pdf`
5. Screenshots folder (20-30 images)

### Estimated Effort
**8-10 hours**

### Priority
**CRITICAL** - Blocks learner progress in Module 0

---

## M0-SETUP-02: Google Colab & GPU Setup Guide

**As an instructor**
I need a comprehensive Google Colab setup guide
So that learners can run ML code in the cloud

### Acceptance Criteria
- [ ] Google account creation (if needed)
- [ ] Accessing Google Colab
- [ ] Creating first notebook
- [ ] Enabling GPU (step-by-step)
- [ ] Verifying GPU access (code snippet)
- [ ] Installing libraries (pip install)
- [ ] Uploading files to Colab
- [ ] Mounting Google Drive
- [ ] Saving work
- [ ] Common errors and solutions
- [ ] Screenshots for every step

### Deliverables
1. `Google-Colab-Setup-Guide.pdf`
2. `colab-verification.ipynb` (template notebook)
3. Screenshots folder

### Estimated Effort
**6-8 hours**

### Priority
**CRITICAL** - Blocks hands-on work

---

## M0-CODE-01: Iris Classifier Complete Code

**As an instructor**
I need a complete, tested Iris classifier notebook
So that learners can run their first ML code successfully

### Acceptance Criteria
- [ ] Complete Jupyter notebook
- [ ] Loads Iris dataset
- [ ] Exploratory data analysis
- [ ] Train/test split
- [ ] Model training (Decision Tree)
- [ ] Predictions and evaluation
- [ ] Clear comments explaining each step
- [ ] Visual outputs (plots)
- [ ] Runs without errors on Google Colab
- [ ] Takes < 1 minute to execute
- [ ] Includes prompts used to generate code

### Deliverables
1. `iris-classifier-complete.ipynb`
2. `prompts-used.md` (AI prompts for generating code)

### Technical Specifications
```python
# Key components:
- Load dataset: sklearn.datasets.load_iris()
- EDA: df.describe(), df.info(), pair plots
- Visualization: seaborn pair plot, feature distributions
- Model: DecisionTreeClassifier
- Metrics: accuracy, confusion matrix
- Output: Model achieves >90% accuracy
```

### Estimated Effort
**4-5 hours**

### Priority
**HIGH** - First hands-on ML experience

---

## M0-VIZ-01: Module 0 Visual Assets

**As an instructor**
I need visual assets for Module 0 videos
So that learners have clear, professional learning materials

### Acceptance Criteria
- [ ] Course roadmap graphic (all 11 modules)
- [ ] Module 0 session structure diagram
- [ ] The 5 demos overview infographic
- [ ] CPU vs GPU comparison diagram
- [ ] LLM comparison chart
- [ ] ML workflow diagram (simple)
- [ ] Welcome slide deck (10-15 slides)
- [ ] Demo app screenshots (high-res)
- [ ] Setup process flowcharts
- [ ] All assets in editable format (Figma/Canva) and export (PNG/SVG)

### Deliverables
- 15-20 visual assets
- Editable source files
- Exported PNGs (1920x1080 for videos)
- Brand style guide (colors, fonts)

### Estimated Effort
**12-15 hours**

### Priority
**HIGH** - Needed for video production

---

## M0-ASSESS-01: Module 0 Quiz Questions

**As an instructor**
I need complete quiz questions for Module 0
So that learners can be assessed on setup and basic understanding

### Acceptance Criteria
- [ ] Session 1 Quiz: 8-10 questions (demo understanding)
- [ ] Session 2 Quiz: 8-10 questions (LLM setup, tool comparison)
- [ ] Session 3 Quiz: 8-10 questions (Colab, GPU, first code)
- [ ] Each question has:
  - Question text
  - 4 multiple choice options
  - Correct answer marked
  - Explanation for correct answer
  - Difficulty level
  - Estimated time (30-60 sec/question)
- [ ] Mix of question types (recall, understanding, application)
- [ ] Questions in JSON/CSV format for LMS import

### Deliverables
1. `module-0-quizzes.json`
2. `module-0-quizzes.csv` (backup format)
3. Answer key with explanations

### Sample Question Structure
```json
{
  "quiz_id": "M0-S1-Q01",
  "session": 1,
  "question": "What was the primary purpose of showing you the 5 demos in Session 1?",
  "options": [
    "To teach you how ML algorithms work",
    "To motivate you and show what you'll build",
    "To test your existing knowledge",
    "To explain neural networks"
  ],
  "correct_answer": 1,
  "explanation": "Module 0 is about creating excitement...",
  "difficulty": "easy",
  "estimated_time_seconds": 30,
  "bloom_level": "understand"
}
```

### Estimated Effort
**6-8 hours**

### Priority
**MEDIUM** - Needed before Module 0 launch

---

**MODULE 0 TOTAL STORIES: 10**
**MODULE 0 ESTIMATED EFFORT: 75-115 hours**

---

# MODULE 1: FOUNDATIONS

## M1-DATA-01: Source and Prepare Stock Datasets

**As an instructor**
I need clean, ready-to-use stock price datasets
So that learners can focus on exploration without data cleaning issues

### Acceptance Criteria
- [ ] Stock data for: AAPL, GOOGL, TSLA, MSFT (US stocks)
- [ ] Stock data for: INFY, TCS, RELIANCE (Indian stocks)
- [ ] Date range: 5 years of historical data
- [ ] OHLCV format (Open, High, Low, Close, Volume)
- [ ] Clean data (no missing values or handled appropriately)
- [ ] CSV format for easy loading
- [ ] Hosted on accessible location (GitHub, Google Drive)
- [ ] Download instructions provided
- [ ] Data dictionary explaining each column
- [ ] License information included

### Technical Specifications
- **Source:** yfinance library OR Alpha Vantage API
- **Format:** CSV files (one per stock)
- **Columns:** Date, Open, High, Low, Close, Volume, Adj Close
- **Size:** ~1250 rows each (5 years of trading days)
- **Storage:** GitHub repository or Google Drive folder

### Script to Generate
```python
import yfinance as yf
import pandas as pd

tickers = ['AAPL', 'GOOGL', 'TSLA', 'MSFT', 'INFY.NS', 'TCS.NS', 'RELIANCE.NS']
for ticker in tickers:
    data = yf.download(ticker, period='5y')
    data.to_csv(f'{ticker}_5y.csv')
```

### Deliverables
1. 7 CSV files (one per stock)
2. `dataset-readme.md` (data dictionary, sources)
3. `download-instructions.md`
4. Data generation script

### Estimated Effort
**6-8 hours** (including documentation and testing)

### Priority
**CRITICAL** - Blocks all Module 1 hands-on activities

---

## M1-CODE-01: Complete Pandas Exploration Code

**As an instructor**
I need complete Pandas code examples
So that learners can explore stock data systematically

### Acceptance Criteria
- [ ] Jupyter notebook with all Pandas operations
- [ ] Loading CSV files
- [ ] Basic operations: head(), tail(), info(), describe()
- [ ] Filtering rows (date ranges, conditions)
- [ ] Selecting columns
- [ ] Calculating statistics (mean, median, std)
- [ ] Creating new columns (returns, moving averages)
- [ ] Grouping and aggregation
- [ ] Comparing multiple stocks
- [ ] Data quality checks (missing values, duplicates)
- [ ] All code tested and works
- [ ] Clear comments and explanations
- [ ] AI prompts used documented

### Deliverables
1. `pandas-stock-exploration.ipynb`
2. `prompts-pandas.md`
3. Expected output examples

### Estimated Effort
**10-12 hours**

### Priority
**CRITICAL** - Core of Module 1 Session 2

---

## M1-CODE-02: Complete Visualization Code

**As an instructor**
I need complete visualization code for all chart types
So that learners can create insightful stock visualizations

### Acceptance Criteria
- [ ] Line charts (price over time)
- [ ] Bar charts (volume)
- [ ] Histograms (price distributions)
- [ ] Scatter plots (correlations)
- [ ] Candlestick charts (OHLC data)
- [ ] Multiple stocks comparison (subplots)
- [ ] Moving averages overlay
- [ ] All using matplotlib and/or plotly
- [ ] Clear, professional-looking charts
- [ ] Customization examples (colors, labels, legends)
- [ ] Interactive charts (plotly)
- [ ] All code tested

### Deliverables
1. `stock-visualization-complete.ipynb`
2. Example output images (10-15 charts)

### Technical Specifications
```python
# Libraries:
- matplotlib.pyplot
- seaborn
- plotly.graph_objects (for candlestick)
- mplfinance (for advanced stock charts)

# Chart types to include:
1. Simple line chart (closing prices)
2. Multi-line chart (compare stocks)
3. Bar chart (volume)
4. Histogram (daily returns)
5. Scatter plot (volume vs price change)
6. Candlestick chart (OHLC)
7. Moving averages (10-day, 50-day)
8. Subplots (price + volume)
```

### Estimated Effort
**12-15 hours**

### Priority
**CRITICAL** - Core of Module 1 Session 3

---

## M1-CODE-03: Data Quality Checking Scripts

**As an instructor**
I need data quality checking code
So that learners understand data validation

### Acceptance Criteria
- [ ] Check for missing values
- [ ] Check for duplicates
- [ ] Check data types
- [ ] Check date ranges
- [ ] Check for outliers
- [ ] Validation report generation
- [ ] Cleaning recommendations
- [ ] Before/after comparison

### Deliverables
1. `data-quality-check.ipynb`
2. Sample quality report

### Estimated Effort
**4-6 hours**

### Priority
**MEDIUM**

---

## M1-SETUP-01: Prompt Library Template

**As an instructor**
I need a prompt library template
So that learners can organize their AI prompts effectively

### Acceptance Criteria
- [ ] Excel or Google Sheets template
- [ ] Categories: Data Loading, Exploration, Visualization, Debugging, etc.
- [ ] Columns: Prompt, Context, Output Type, Rating, Notes
- [ ] Example prompts filled in (20-30 examples)
- [ ] Instructions for use
- [ ] Tips for prompt engineering
- [ ] Downloadable and editable

### Deliverables
1. `prompt-library-template.xlsx`
2. `prompt-library-template.gsheet` (Google Sheets link)
3. `prompt-engineering-tips.pdf`

### Estimated Effort
**6-8 hours**

### Priority
**HIGH** - Core tool for AI-assisted learning

---

## M1-VIZ-01: Module 1 Visual Assets

**As an instructor**
I need visual assets for Module 1 videos
So that concepts are clearly explained

### Acceptance Criteria
- [ ] ML types diagram (Supervised, Unsupervised, Reinforcement)
- [ ] Classification vs Regression visual
- [ ] ML pipeline flowchart (5 steps)
- [ ] Data structure diagram (rows, columns, features, labels)
- [ ] Traditional programming vs ML comparison
- [ ] OHLCV data explanation graphic
- [ ] Pandas operations cheat sheet
- [ ] Chart types comparison
- [ ] All assets professional quality

### Deliverables
- 15-20 visual assets
- Editable source files
- Exported PNGs

### Estimated Effort
**12-15 hours**

### Priority
**HIGH**

---

## M1-ASSESS-01: Module 1 Quizzes

**As an instructor**
I need complete quiz questions for Module 1
So that conceptual understanding can be assessed

### Acceptance Criteria
- [ ] Session 1 Quiz: 10-12 questions (ML concepts)
- [ ] Session 2 Quiz: 8-10 questions (data operations)
- [ ] Session 3 Quiz: 8-10 questions (visualization)
- [ ] Session 4 Quiz: 8-10 questions (AI tools)
- [ ] Same format as Module 0 (JSON/CSV)
- [ ] Mix of difficulty levels
- [ ] Explanations included

### Deliverables
1. `module-1-quizzes.json`
2. Answer key with explanations

### Estimated Effort
**8-10 hours**

### Priority
**MEDIUM**

---

## M1-ASSESS-02: Stock Exploration Project Rubric

**As an instructor**
I need a detailed grading rubric
So that learners know expectations and grading is consistent

### Acceptance Criteria
- [ ] Clear criteria for stock data exploration project
- [ ] Point allocation (100 points total)
- [ ] Categories:
  - Data loading (10 points)
  - Exploration completeness (20 points)
  - Visualization quality (30 points)
  - Insights identified (20 points)
  - Code quality (10 points)
  - Documentation (10 points)
- [ ] Performance levels (Excellent, Good, Satisfactory, Needs Improvement)
- [ ] Example submissions (good, average, poor)
- [ ] Self-assessment checklist

### Deliverables
1. `module-1-project-rubric.pdf`
2. `module-1-self-assessment.pdf`
3. Example submissions (3 notebooks)

### Estimated Effort
**6-8 hours**

### Priority
**MEDIUM**

---

**MODULE 1 TOTAL STORIES: 8**
**MODULE 1 ESTIMATED EFFORT: 55-80 hours**

---

# MODULE 2: CLASSIFICATION

## M2-DATA-01: Source All Classification Datasets

**As an instructor**
I need all datasets for classification projects
So that learners can build 6 different classifiers

### Acceptance Criteria
- [ ] Iris dataset (sourced and documented)
- [ ] Spam email dataset (labeled emails)
- [ ] Customer churn dataset (business metrics)
- [ ] Heart disease dataset (UCI repository)
- [ ] MNIST dataset (handwritten digits)
- [ ] Cricket match dataset (match outcomes)
- [ ] All datasets cleaned and ready to use
- [ ] Data dictionaries provided
- [ ] Hosted accessibly (GitHub/Google Drive)
- [ ] License information included

### Dataset Sources
1. **Iris:** sklearn.datasets
2. **Spam:** Kaggle / UCI ML Repository
3. **Churn:** Kaggle (Telco churn dataset)
4. **Heart Disease:** UCI ML Repository
5. **MNIST:** tensorflow.keras.datasets
6. **Cricket:** Kaggle (IPL/International matches)

### Deliverables
- 6 datasets (CSV or direct loading code)
- Data dictionaries (6 files)
- Download/access instructions

### Estimated Effort
**10-12 hours**

### Priority
**CRITICAL**

---

## M2-CODE-01: Iris Classifier Complete Project

**As an instructor**
I need a complete Iris classification project
So that learners experience their first model building

### Acceptance Criteria
- [ ] Complete Jupyter notebook
- [ ] Data loading and EDA
- [ ] Train/test split
- [ ] Decision Tree model training
- [ ] Predictions and evaluation
- [ ] Accuracy, precision, recall calculated
- [ ] Confusion matrix visualization
- [ ] Feature importance analysis
- [ ] All code tested (achieves >90% accuracy)
- [ ] Clear documentation
- [ ] AI prompts documented

### Deliverables
1. `iris-classifier-complete.ipynb`
2. `prompts-iris.md`

### Estimated Effort
**6-8 hours**

### Priority
**CRITICAL** - First real ML model

---

## M2-CODE-02: Spam Email Classifier

**As an instructor**
I need a complete spam detection project
So that learners see NLP + classification

### Acceptance Criteria
- [ ] Complete notebook with spam classifier
- [ ] Text preprocessing (TF-IDF or Count Vectorizer)
- [ ] Multiple models (Naive Bayes, Logistic Regression)
- [ ] Model comparison
- [ ] Achieves >90% accuracy
- [ ] Can classify new emails
- [ ] All code tested

### Deliverables
1. `spam-classifier-complete.ipynb`

### Estimated Effort
**8-10 hours**

### Priority
**HIGH**

---

## M2-CODE-03: Customer Churn Predictor

**As an instructor**
I need a complete churn prediction project
So that learners see business application

### Acceptance Criteria
- [ ] Complete notebook
- [ ] Feature engineering for business data
- [ ] Handling categorical variables (encoding)
- [ ] Class imbalance handling
- [ ] Random Forest or Gradient Boosting model
- [ ] Business metrics (revenue impact)
- [ ] Feature importance
- [ ] All code tested

### Deliverables
1. `churn-predictor-complete.ipynb`

### Estimated Effort
**8-10 hours**

### Priority
**HIGH**

---

## M2-CODE-04: Heart Disease Predictor

**As an instructor**
I need a healthcare classification project
So that learners see medical AI application

### Acceptance Criteria
- [ ] Complete notebook
- [ ] Medical data EDA
- [ ] Feature scaling
- [ ] Multiple classification algorithms
- [ ] ROC curve and AUC
- [ ] Precision-recall tradeoff for medical context
- [ ] All code tested

### Deliverables
1. `heart-disease-predictor.ipynb`

### Estimated Effort
**8-10 hours**

### Priority
**HIGH**

---

## M2-CODE-05: MNIST Image Classifier

**As an instructor**
I need a simple image classification project
So that learners see computer vision basics

### Acceptance Criteria
- [ ] Complete notebook
- [ ] MNIST data loading
- [ ] Image visualization
- [ ] Neural network (simple, fully connected)
- [ ] Training with progress monitoring
- [ ] Achieves >95% accuracy
- [ ] Visualizes predictions
- [ ] All code tested

### Deliverables
1. `mnist-classifier.ipynb`

### Estimated Effort
**6-8 hours**

### Priority
**MEDIUM**

---

## M2-CODE-06: Cricket Match Outcome Predictor

**As an instructor**
I need a cricket prediction project
So that sports enthusiasts stay engaged

### Acceptance Criteria
- [ ] Complete notebook
- [ ] Cricket data EDA
- [ ] Feature engineering (team strength, venue, etc.)
- [ ] Classification model
- [ ] Win probability predictions
- [ ] All code tested

### Deliverables
1. `cricket-match-predictor.ipynb`

### Estimated Effort
**8-10 hours**

### Priority
**MEDIUM** - Engagement hook

---

## M2-CODE-07: Classification Metrics & Evaluation

**As an instructor**
I need comprehensive evaluation code
So that learners understand all classification metrics

### Acceptance Criteria
- [ ] Confusion matrix code and visualization
- [ ] Accuracy, Precision, Recall, F1-score calculation
- [ ] ROC curve and AUC
- [ ] Precision-Recall curve
- [ ] Classification report
- [ ] Cross-validation implementation
- [ ] Metric comparison across models
- [ ] When to use which metric (guide)

### Deliverables
1. `classification-metrics-complete.ipynb`
2. `metrics-guide.md`

### Estimated Effort
**8-10 hours**

### Priority
**HIGH** - Core understanding

---

## M2-VIZ-01: Module 2 Visual Assets

**As an instructor**
I need visual assets for Module 2
So that classification concepts are clear

### Acceptance Criteria
- [ ] Decision tree visualization
- [ ] Confusion matrix explained graphic
- [ ] ROC curve explanation
- [ ] Precision vs Recall tradeoff diagram
- [ ] Classification workflow diagram
- [ ] Train/test split visualization
- [ ] Overfitting vs underfitting graphic
- [ ] All 6 project overview infographic

### Deliverables
- 15-20 visual assets

### Estimated Effort
**12-15 hours**

### Priority
**HIGH**

---

## M2-ASSESS-01: Module 2 Quizzes & Rubrics

**As an instructor**
I need complete assessment materials for Module 2
So that learning can be properly evaluated

### Acceptance Criteria
- [ ] 6 session quizzes (8-10 questions each)
- [ ] Project rubrics for all 6 projects
- [ ] Model comparison rubric
- [ ] Final classification project rubric
- [ ] Self-assessment checklists
- [ ] Example submissions

### Deliverables
1. `module-2-quizzes.json`
2. `module-2-rubrics.pdf`
3. Example project submissions

### Estimated Effort
**10-12 hours**

### Priority
**MEDIUM**

---

**MODULE 2 TOTAL STORIES: 10**
**MODULE 2 ESTIMATED EFFORT: 90-130 hours**

---

# MODULE 3: REGRESSION

## M3-DATA-01: Source All Regression Datasets

**As an instructor**
I need all datasets for regression projects
So that learners can build 6 different regressors

### Acceptance Criteria
- [ ] House price dataset (Boston/California housing)
- [ ] Stock price data (reuse from Module 1, but extended)
- [ ] Sales forecasting dataset (retail/e-commerce)
- [ ] Cricket score dataset (ball-by-ball data)
- [ ] Energy consumption dataset (time series)
- [ ] Salary dataset (job/experience data)
- [ ] All cleaned and documented
- [ ] Data dictionaries provided

### Deliverables
- 6 datasets
- Data dictionaries
- Access instructions

### Estimated Effort
**12-15 hours**

### Priority
**CRITICAL**

---

## M3-CODE-01: Feature Engineering Library

**As an instructor**
I need a complete feature engineering code library
So that learners can create powerful stock prediction features

### Acceptance Criteria
- [ ] Moving averages (10, 20, 50, 200 day)
- [ ] RSI (Relative Strength Index) calculation
- [ ] MACD (Moving Average Convergence Divergence)
- [ ] Bollinger Bands
- [ ] Volatility metrics
- [ ] Rate of change
- [ ] Volume indicators
- [ ] Momentum indicators
- [ ] All functions tested and documented
- [ ] Example usage notebook

### Deliverables
1. `feature_engineering.py` (Python module)
2. `feature-engineering-guide.ipynb` (usage examples)

### Technical Specifications
```python
def calculate_rsi(data, window=14):
    """Calculate RSI indicator"""
    # Implementation

def calculate_macd(data):
    """Calculate MACD"""
    # Implementation

def add_moving_averages(data, windows=[10, 20, 50]):
    """Add multiple moving averages"""
    # Implementation
```

### Estimated Effort
**15-20 hours**

### Priority
**CRITICAL** - Core of stock prediction

---

## M3-CODE-02: Stock Predictor Complete Project

**As an instructor**
I need THE complete stock prediction project
So that learners achieve the Module 0 payoff

### Acceptance Criteria
- [ ] Complete end-to-end notebook
- [ ] Data loading (5 years of stock data)
- [ ] Feature engineering (10+ features)
- [ ] Train/test split (time-aware)
- [ ] Multiple models (Linear, RF, Gradient Boosting)
- [ ] Model comparison
- [ ] Prediction visualization
- [ ] Achieves reasonable accuracy (R² > 0.7)
- [ ] Deployment-ready code
- [ ] THE PAYOFF MOMENT clearly highlighted

### Deliverables
1. `stock-predictor-COMPLETE.ipynb`
2. Trained model file (pickle)
3. Prediction examples

### Estimated Effort
**15-20 hours** (most important project!)

### Priority
**CRITICAL** - THE PAYOFF

---

## M3-CODE-03: House Price Predictor

**As an instructor**
I need a house price prediction project
So that learners see classic regression application

### Acceptance Criteria
- [ ] Complete notebook
- [ ] Feature engineering for housing data
- [ ] Linear Regression baseline
- [ ] Advanced models (RF, Gradient Boosting)
- [ ] Feature importance analysis
- [ ] Prediction examples
- [ ] All tested

### Deliverables
1. `house-price-predictor.ipynb`

### Estimated Effort
**8-10 hours**

### Priority
**HIGH**

---

## M3-CODE-04: Sales Forecasting Project

**As an instructor**
I need a sales forecasting project
So that learners see business forecasting

### Acceptance Criteria
- [ ] Complete notebook
- [ ] Time series feature engineering
- [ ] Seasonal decomposition
- [ ] Regression for forecasting
- [ ] Business metrics (MAE, MAPE)
- [ ] Forecast visualization
- [ ] All tested

### Deliverables
1. `sales-forecasting.ipynb`

### Estimated Effort
**8-10 hours**

### Priority
**HIGH**

---

## M3-CODE-05: Cricket Score Predictor

**As an instructor**
I need a cricket score prediction project
So that sports fans achieve their payoff too

### Acceptance Criteria
- [ ] Complete notebook
- [ ] Ball-by-ball data processing
- [ ] Feature engineering (run rate, wickets, overs, etc.)
- [ ] Score prediction model
- [ ] Live prediction simulation
- [ ] All tested

### Deliverables
1. `cricket-score-predictor.ipynb`

### Estimated Effort
**10-12 hours**

### Priority
**MEDIUM** - Engagement

---

## M3-CODE-06: Regression Evaluation Code

**As an instructor**
I need comprehensive regression evaluation code
So that learners understand regression metrics

### Acceptance Criteria
- [ ] MAE, MSE, RMSE, R² calculations
- [ ] Residual plots
- [ ] Actual vs Predicted plots
- [ ] Cross-validation for time series
- [ ] Data leakage prevention examples
- [ ] Backtesting framework
- [ ] All tested

### Deliverables
1. `regression-metrics-complete.ipynb`
2. `backtesting-framework.py`

### Estimated Effort
**10-12 hours**

### Priority
**HIGH**

---

## M3-VIZ-01: Module 3 Visual Assets

**As an instructor**
I need visual assets for Module 3
So that regression concepts are clear

### Acceptance Criteria
- [ ] Linear regression visualization
- [ ] Residual plots explained
- [ ] Feature importance charts
- [ ] Time series decomposition graphic
- [ ] Overfitting in regression visual
- [ ] Stock prediction workflow diagram
- [ ] Technical indicators explained (RSI, MACD, etc.)

### Deliverables
- 15-20 visual assets

### Estimated Effort
**12-15 hours**

### Priority
**HIGH**

---

## M3-ASSESS-01: Module 3 Quizzes & Rubrics

**As an instructor**
I need complete assessment materials for Module 3
So that regression mastery can be evaluated

### Acceptance Criteria
- [ ] 6 session quizzes
- [ ] Project rubrics for all 6 projects
- [ ] Stock predictor rubric (detailed!)
- [ ] Final regression project rubric
- [ ] Self-assessment materials
- [ ] Example submissions

### Deliverables
1. `module-3-quizzes.json`
2. `module-3-rubrics.pdf`
3. Example submissions

### Estimated Effort
**10-12 hours**

### Priority
**MEDIUM**

---

**MODULE 3 TOTAL STORIES: 10**
**MODULE 3 ESTIMATED EFFORT: 115-165 hours**

---

# MODULES 4-10: EXPANSION STORIES

## M4-EXPAND-01: Expand Module 4 to Production Detail

**As an instructor**
I need Module 4 expanded to full production detail
So that video recording can proceed

### Acceptance Criteria
- [ ] Session-by-session breakdown (6 sessions)
- [ ] Video outlines with timing
- [ ] All code examples identified
- [ ] All datasets sourced
- [ ] All projects detailed
- [ ] Quiz questions created
- [ ] Visual assets identified
- [ ] Same detail level as Modules 0-3

### Estimated Effort
**40-50 hours**

### Priority
**MEDIUM** (after Modules 0-3)

---

## M5-EXPAND-01: Expand Module 5 to Production Detail
## M6-EXPAND-01: Expand Module 6 to Production Detail
## M7-EXPAND-01: Expand Module 7 to Production Detail
## M8-EXPAND-01: Expand Module 8 to Production Detail
## M9-EXPAND-01: Expand Module 9 to Production Detail
## M10-EXPAND-01: Expand Module 10 to Production Detail

**Same structure as M4-EXPAND-01**

**Estimated Effort per module:** 40-60 hours
**Total for Modules 5-10:** 240-360 hours

---

**MODULES 4-10 TOTAL STORIES: 7**
**MODULES 4-10 ESTIMATED EFFORT: 280-420 hours**

---

# BACKLOG SUMMARY

## Total Statistics
- **Total User Stories:** 55
- **Module 0:** 10 stories, 75-115 hours
- **Module 1:** 8 stories, 55-80 hours
- **Module 2:** 10 stories, 90-130 hours
- **Module 3:** 10 stories, 115-165 hours
- **Modules 4-10:** 7 stories, 280-420 hours
- **GRAND TOTAL:** 615-910 hours

## Priority Breakdown
- **CRITICAL:** 15 stories (blocks production)
- **HIGH:** 18 stories (needed soon)
- **MEDIUM:** 22 stories (needed before launch)

## Recommended Sequence
1. ✅ Start with Module 0 (10 stories)
2. ✅ Complete all Module 0 before moving on
3. ✅ Then Module 1 (8 stories)
4. ✅ Then Module 2 (10 stories)
5. ✅ Then Module 3 (10 stories)
6. ✅ Finally Modules 4-10 (7 expansion stories)

## Sprint Planning Suggestion
- **Sprint 1 (2 weeks):** M0-DEMO-01, M0-DEMO-02, M0-SETUP-01
- **Sprint 2 (2 weeks):** M0-DEMO-03, M0-DEMO-04, M0-DEMO-05, M0-SETUP-02
- **Sprint 3 (2 weeks):** M0-CODE-01, M0-VIZ-01, M0-ASSESS-01
- **Sprint 4 (2 weeks):** M1-DATA-01, M1-CODE-01, M1-CODE-02
- **And so on...**

---

**Status:** READY TO START
**First Story:** M0-DEMO-01 (Stock Predictor Demo App)
**Approval Needed:** YES - confirm approach before starting work

**Created:** 2026-01-05
**Version:** 1.0
