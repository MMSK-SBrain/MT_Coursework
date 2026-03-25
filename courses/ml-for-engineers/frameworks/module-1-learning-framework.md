# Module 1: Getting Started with AI-Assisted Learning
## Learning Framework & Implementation Guide

**Course Code:** ML-ENG-M1
**Duration:** 1 week (self-paced)
**Total Video Content:** ~6-7 hours
**Total Hands-on Time:** ~8-10 hours
**Theory/Practice Ratio:** 20% / 80%

---

## 📋 Module Overview

### Module Outcomes
By the end of Module 1, learners will be able to:
1. **MO-1-1:** Apply prompt engineering techniques to elicit high-quality ML code and explanations from LLMs
2. **MO-1-2:** Analyze ML problem statements and decompose them into AI-actionable prompts
3. **MO-1-3:** Build a simple ML prediction model using AI-generated code and execute it successfully

### Prerequisites
- Laptop with internet connection
- Willingness to learn
- Basic computer skills (can browse web, download files)

### What Learners Will Build
- **Primary Project:** Stock price prediction model (Sessions 1-2)
- **Secondary Project:** Cricket match outcome predictor (Session 3)
- **Mini Projects:** 9 progressive challenges (3 per session)

---

## 🎯 Module Structure

```
Module 1 (1 Week)
│
├── Setup Session (Day 1: ~1.5 hours)
│   └── Get accounts, tools, and environment ready
│
├── Session 1: Introduction to ML (Day 2: ~2 hours)
│   └── What is ML? Why does it matter? [Hook: Stock prediction]
│
├── Session 2: Prompt Engineering (Day 3-4: ~2 hours)
│   └── Mastering AI communication [Continue: Stock prediction]
│
└── Session 3: Your First Model (Day 5-7: ~2 hours)
    └── Build and run a real ML model [Switch: Cricket prediction]
```

---

## 📹 Setup Session: Getting Ready for ML

**Duration:** ~1.5 hours video + 1 hour practice
**Day:** Day 1
**Goal:** Set up all tools and accounts needed for Module 2 onwards

### Video Breakdown

#### Video 1: Welcome & Course Overview (10 min)
**Type:** Talking head + graphics
**Content:**
- Welcome to the course
- What you'll achieve by end of Module 1
- Course philosophy: AI as your coding partner
- Overview of the week ahead
- Motivational hook: Show final projects (stock predictor, cricket predictor)

**Learning Outcome:** SO-1-0-1 - Understand course structure and AI-assisted learning philosophy

---

#### Video 2: Creating Your LLM Accounts (10 min)
**Type:** Screen recording + talking head
**Content:**
- Why we need multiple LLM platforms
- Step-by-step: Create ChatGPT account
- Step-by-step: Create Gemini account
- Step-by-step: Create Claude account (optional)
- Verify all accounts with test prompts
- Free vs paid tiers explanation

**Hands-on During Video:**
- Pause and create accounts alongside the video
- Send test message to each platform

**Learning Outcome:** SO-1-0-2 - Create and verify LLM platform accounts

---

#### Video 3: LLM Access Methods - Web, IDE, API (10 min)
**Type:** Screen recording + graphics
**Content:**
- Three ways to use LLMs:
  1. Web interface (what we'll use most)
  2. IDE integration (GitHub Copilot demo)
  3. API access (brief overview for later)
- When to use each method
- Demo: Same prompt on web vs IDE

**Learning Outcome:** SO-1-0-3 - Identify different LLM access methods

---

#### Video 4: Understanding CPU vs GPU (8 min)
**Type:** Talking head + animations
**Content:**
- What is CPU and GPU?
- Real-world analogy: Chef vs Kitchen assembly line
- Why ML needs GPUs (parallel processing)
- When do you need a GPU? (small models = CPU ok, large models = GPU needed)
- Local GPU vs Cloud GPU

**Learning Outcome:** SO-1-0-4 - Explain CPU vs GPU differences for ML

---

#### Video 5: Setting Up Google Colab (10 min)
**Type:** Screen recording + talking head
**Content:**
- What is Google Colab and why use it?
- Creating a Google Colab account
- Interface tour: Cells, runtime, GPU setting
- Enabling GPU: Runtime → Change runtime type → GPU
- Running your first Python cell
- Saving and organizing notebooks

**Hands-on During Video:**
- Open Google Colab
- Create first notebook
- Enable GPU
- Run: `print("Hello ML!")`
- Check GPU: `!nvidia-smi`

**Learning Outcome:** SO-1-0-5 - Set up and configure Google Colab with GPU

---

#### Video 6: Installing Essential ML Libraries (10 min)
**Type:** Screen recording + talking head
**Content:**
- Libraries we'll use: numpy, pandas, scikit-learn, matplotlib
- Using AI to help with installation
- Prompt: "How do I install ML libraries in Google Colab?"
- Running installation commands
- Testing imports
- Troubleshooting common errors with AI help

**Hands-on During Video:**
```python
# Install and test libraries
import numpy as np
import pandas as pd
import sklearn
import matplotlib.pyplot as plt
print("All libraries installed successfully!")
```

**Learning Outcome:** SO-1-0-6 - Install and verify ML libraries

---

### Setup Session Mini Projects (Progressive)

#### Mini Project 1: LLM Comparison Challenge (Easy) - 20 min
**Objective:** Test the same prompt across 3 LLMs and compare responses

**Task:**
- Send this prompt to ChatGPT, Gemini, and Claude:
  "Explain what machine learning is in simple terms, then give me a real-world example."
- Create a comparison table in a Google Doc
- Rate each response: Clarity (1-5), Examples (1-5), Helpfulness (1-5)
- Which one do you prefer and why?

**Deliverable:** Comparison table with ratings and your recommendation

---

#### Mini Project 2: Colab GPU Speed Test (Medium) - 25 min
**Objective:** Experience CPU vs GPU performance difference

**Task:**
- In Google Colab, ask ChatGPT: "Give me Python code to compare CPU vs GPU performance for matrix multiplication"
- Run the code on CPU (Runtime → Change runtime type → None)
- Run the same code on GPU (Runtime → Change runtime type → GPU)
- Record execution times
- Calculate speedup: (CPU time / GPU time)

**Deliverable:** Screenshot showing execution times for both runs

---

#### Mini Project 3: Environment Setup Verification (Challenge) - 30 min
**Objective:** Create a comprehensive setup check notebook

**Task:**
- Create a new Colab notebook called "My_ML_Setup_Check"
- Use ChatGPT to help you create a script that:
  1. Checks if GPU is available
  2. Prints GPU name and memory
  3. Tests all ML libraries (numpy, pandas, sklearn, matplotlib)
  4. Prints library versions
  5. Creates a simple plot to test visualization
- Run the entire notebook successfully
- Add markdown cells explaining what each section does

**Deliverable:** Complete setup check notebook (submit link)

---

### Setup Session Quiz (10 questions, Mixed Format)

**Quiz 1: Environment Setup & LLM Basics**

**Multiple Choice Questions (5):**
1. Which of the following is NOT a way to access LLMs?
   - a) Web browser interface
   - b) IDE plugins
   - c) Email
   - d) API calls

2. What is the main advantage of using GPU for ML?
   - a) Cheaper than CPU
   - b) Parallel processing capability
   - c) Easier to program
   - d) Uses less electricity

3. Which platform provides free GPU access for ML learning?
   - a) Microsoft Word
   - b) Google Colab
   - c) Gmail
   - d) YouTube

4. When should you use ChatGPT/Gemini for coding help?
   - a) Only after you've learned to code
   - b) Never, it's cheating
   - c) Throughout learning as a coding assistant
   - d) Only for debugging

5. What does 'Runtime → Change runtime type → GPU' do in Colab?
   - a) Deletes your notebook
   - b) Enables GPU acceleration
   - c) Closes the browser
   - d) Installs Python

**True/False (3):**
6. You need to install Python on your computer to use Google Colab. (False)
7. Free tier of ChatGPT is sufficient for this course. (True)
8. GPU is always faster than CPU for all tasks. (False)

**Short Answer (2):**
9. Name two LLM platforms you set up in this session.
10. What command checks if GPU is available in Colab? (`!nvidia-smi` or checking tensorflow/pytorch)

**Passing Score:** 70% (7/10 correct)

---

## 📹 Session 1: Introduction to Machine Learning

**Duration:** ~2 hours video + 2-3 hours practice
**Day:** Day 2
**Hook:** "Can you predict tomorrow's stock price and make money?"
**Storytelling Theme:** Stock Market Prediction

### The Story Arc
**Problem:** Meet Raj, an engineer who wants to predict stock prices to make better investment decisions. He knows companies release financial data, news affects stocks, and historical patterns exist - but how do you turn this data into predictions? Enter Machine Learning...

---

### Video Breakdown

#### Video 1: The Stock Prediction Challenge (10 min)
**Type:** Talking head + graphics/stock charts
**Content:**
- Raj's problem: "How do I predict if a stock will go up or down?"
- Traditional approach: Manual analysis, spreadsheets, gut feeling
- The ML approach: Let data reveal patterns
- Preview: By end of this module, you'll build a stock predictor
- Key question: What IS machine learning?

**Learning Outcome:** SO-1-1-1 - Identify real-world ML problems (stock prediction)

---

#### Video 2: What is Machine Learning? (10 min)
**Type:** Talking head + animations
**Content:**
- Definition: Teaching computers to learn from data
- Traditional programming vs ML (flowchart comparison)
- Key ingredients: Data + Algorithm = Predictions
- Three types of ML (brief intro):
  - Supervised (we teach with examples) ← Focus for stock prediction
  - Unsupervised (finds patterns itself)
  - Reinforcement (learns by trial and error)
- For stock prediction: We'll use supervised learning

**Learning Outcome:** SO-1-1-1 - Define ML and distinguish from traditional programming

---

#### Video 3: How ML Predicts Stocks (10 min)
**Type:** Screen recording + talking head + graphics
**Content:**
- The ML pipeline for stock prediction:
  1. Collect historical data (prices, volume, indicators)
  2. Prepare data (clean, organize)
  3. Train ML model (teach it patterns)
  4. Test predictions (how accurate?)
  5. Use for future predictions
- Real example: Show a dataset (simple CSV)
- What patterns might ML find? (price trends, volume correlations)
- Demo: Ask ChatGPT "How does ML predict stock prices?"

**Hands-on During Video:**
- Open ChatGPT
- Ask: "Explain how machine learning can predict stock prices in simple terms"
- Ask follow-up: "What data would I need?"

**Learning Outcome:** SO-1-1-2 - Understand ML pipeline for prediction tasks

---

#### Video 4: AI as Your Learning Partner (10 min)
**Type:** Talking head + screen recording
**Content:**
- Philosophy: You don't need to code from scratch
- AI will be your:
  - Code generator
  - Tutor
  - Debugger
  - Project assistant
- Demo: Live interaction with ChatGPT
  - Ask vague question → Get vague answer
  - Ask specific question → Get useful answer
- The skill: Learning to communicate with AI effectively
- Show: Same question asked 3 different ways → 3 different quality answers

**Learning Outcome:** SO-1-1-3 - Understand AI-assisted learning approach

---

#### Video 5: Different Types of ML Problems (10 min)
**Type:** Screen recording + graphics
**Content:**
- Classification: Categorizing (Is stock up or down? Will team win or lose?)
- Regression: Predicting numbers (Exact stock price? Run score?)
- Clustering: Grouping similar things
- Stock prediction can be both:
  - Regression: Predict exact price (harder)
  - Classification: Predict up/down (easier, we'll do this)
- Other examples:
  - Email spam detection (Classification)
  - House price prediction (Regression)
  - Customer segmentation (Clustering)

**Learning Outcome:** SO-1-1-4 - Distinguish between classification and regression

---

#### Video 6: Using AI to Explain ML Concepts (10 min)
**Type:** Screen recording + talking head
**Content:**
- Technique: Ask AI to explain in multiple ways
- Demo: Ask ChatGPT to explain "supervised learning":
  - To a 10-year-old
  - To a college student
  - To a business executive
- Compare explanations
- When to use which level?
- Practice: You try with "what is a neural network?"
- Power tip: "Explain like I'm 5, then give technical details"

**Hands-on During Video:**
- Open ChatGPT/Gemini
- Try the 3-level explanation technique
- Find which explanation style helps you most

**Learning Outcome:** SO-1-1-3 - Use LLMs to explain concepts at different levels

---

### Session 1 Mini Projects (Progressive)

#### Mini Project 1: ML Problem Identifier (Easy) - 25 min
**Objective:** Identify ML vs non-ML problems

**Task:**
- Use ChatGPT to help you create a list of 10 problems
- Prompt: "Give me 10 problems - 5 that need ML and 5 that don't need ML"
- For each ML problem, identify: Classification or Regression?
- Add 2 of your own industry-specific problems
- Ask AI to verify your classifications

**Deliverable:** Google Doc with 12 problems, each labeled: ML/Non-ML and Classification/Regression

---

#### Mini Project 2: Stock Prediction Data Explorer (Medium) - 35 min
**Objective:** Understand what data is needed for stock prediction

**Task:**
- Ask ChatGPT: "What data do I need to predict stock prices with ML? Give me a detailed list."
- Research (using AI):
  - What is "historical price data"?
  - What are "technical indicators" (RSI, MACD, Moving Average)?
  - What is "volume" and why does it matter?
- Find a free source of stock data (ask AI: "Where can I get free stock data?")
- Create a mind map or document explaining the data pipeline

**Deliverable:** Document explaining 5 types of data needed for stock prediction with examples

---

#### Mini Project 3: Your First AI-Assisted Code (Challenge) - 45 min
**Objective:** Generate and understand code for loading stock data

**Task:**
- In Google Colab, use ChatGPT to generate code for:
  "Write Python code to download stock data for Apple (AAPL) for the last 6 months and display the first 10 rows"
- Steps:
  1. Get the code from ChatGPT
  2. Copy to Colab
  3. Run it (might need to install libraries)
  4. If errors, copy error back to ChatGPT and ask for fix
  5. Once working, ask ChatGPT: "Explain this code line by line"
  6. Add comments to each line explaining what it does (in your own words)
- Experiment: Change stock ticker to another company

**Deliverable:** Colab notebook with working code, line-by-line comments, and data displayed

---

### Session 1 Quiz (12 questions, Mixed Format)

**Quiz 2: Introduction to Machine Learning**

**Multiple Choice (6):**
1. What is machine learning?
   - a) Teaching computers to learn from data
   - b) Computer graphics programming
   - c) Building websites
   - d) Database management

2. Which type of ML would you use for stock price prediction?
   - a) Unsupervised learning
   - b) Supervised learning
   - c) Reinforcement learning
   - d) None of the above

3. What's the difference between classification and regression?
   - a) Classification predicts categories, regression predicts numbers
   - b) They are the same thing
   - c) Classification is easier than regression
   - d) Regression doesn't use data

4. In the ML pipeline, what comes first?
   - a) Make predictions
   - b) Test the model
   - c) Collect and prepare data
   - d) Deploy to production

5. For predicting if a stock will go UP or DOWN, which ML type is best?
   - a) Regression
   - b) Classification
   - c) Clustering
   - d) None

6. Traditional programming vs ML - key difference?
   - a) ML learns patterns from data, traditional follows explicit rules
   - b) ML is always faster
   - c) Traditional programming is newer
   - d) They are exactly the same

**True/False (3):**
7. You need to be an expert coder to use ML with AI assistance. (False)
8. Supervised learning needs labeled training data. (True)
9. Stock prediction using ML is 100% accurate. (False)

**Short Answer (3):**
10. Name two types of data needed for stock prediction.
11. What does "supervised learning" mean?
12. Give one example of a classification problem (other than stocks).

**Passing Score:** 70% (9/12 correct)

---

## 📹 Session 2: Effective Prompt Engineering for ML

**Duration:** ~2 hours video + 2-3 hours practice
**Day:** Day 3-4
**Hook:** "The difference between 'write ML code' and getting exactly what you need"
**Storytelling Theme:** Continue Stock Prediction - Mastering AI Communication

### The Story Arc
**Problem:** Raj tried asking ChatGPT "make a stock predictor" but got generic code that didn't work for his needs. He's frustrated. Then he learns: AI is powerful, but you need to speak its language. The skill isn't coding - it's asking the RIGHT questions...

---

### Video Breakdown

#### Video 1: Why Prompt Engineering Matters (10 min)
**Type:** Talking head + screen recording demos
**Content:**
- Raj's failed attempt: Vague prompt = Vague result
- Show live: Bad prompt vs Good prompt (same goal, different outcomes)
- Bad: "Write stock prediction code"
- Good: "Write Python code using scikit-learn to predict stock direction (up/down) using pandas dataframe with columns: Open, High, Low, Close, Volume. Use logistic regression."
- The difference: Specificity, context, constraints
- You're not just asking questions - you're collaborating with AI

**Learning Outcome:** SO-1-2-1 - Understand importance of prompt quality

---

#### Video 2: The Prompt Engineering Formula (10 min)
**Type:** Screen recording + graphics
**Content:**
- **The Formula:**
  ```
  [TASK] + [CONTEXT] + [FORMAT] + [CONSTRAINTS] = Great Prompt
  ```
- Breaking it down for stock prediction:
  - TASK: "Create a stock direction classifier"
  - CONTEXT: "Using historical price data with OHLCV features"
  - FORMAT: "Python code using pandas and scikit-learn"
  - CONSTRAINTS: "For beginners, add comments, handle missing data"
- Demo: Build a prompt step by step
- Practice together: Build prompt for "loading stock data"

**Hands-on During Video:**
- Follow along building prompts in a text editor
- Test your prompt in ChatGPT

**Learning Outcome:** SO-1-2-1 - Construct effective prompts using the formula

---

#### Video 3: Iterative Prompting - The Conversation Method (10 min)
**Type:** Screen recording + talking head
**Content:**
- You don't get perfect code on first try - that's OK!
- The iteration cycle:
  1. Start with basic prompt
  2. Review AI's response
  3. Ask for specific improvements
  4. Refine until perfect
- Live demo: Start with basic stock code, iterate 4 times:
  - "Add error handling"
  - "Add data visualization"
  - "Make it work with any stock ticker"
  - "Add comments for beginners"
- Key: Each prompt builds on previous response
- Power tip: "Improve this code to..."

**Hands-on During Video:**
- Try the iteration cycle with your own prompt
- Document each iteration

**Learning Outcome:** SO-1-2-2 - Iterate on AI-generated code with follow-up prompts

---

#### Video 4: Asking for Explanations (10 min)
**Type:** Screen recording
**Content:**
- Getting code is step 1, understanding it is step 2
- Prompt patterns for explanations:
  - "Explain this code line by line"
  - "What does [specific part] do?"
  - "Why did you use [library/method]?"
  - "Explain like I'm a beginner"
  - "What are alternative approaches?"
- Demo: Get complex ML code, then:
  - Ask for high-level overview
  - Ask for line-by-line breakdown
  - Ask for concept explanations
  - Ask for alternatives
- Practice: Use code from previous session

**Hands-on During Video:**
- Take code from Session 1 Mini Project 3
- Ask AI for detailed explanation
- Rewrite comments in your own words

**Learning Outcome:** SO-1-2-3 - Request code explanations at different depths

---

#### Video 5: Debugging with AI (10 min)
**Type:** Screen recording + talking head
**Content:**
- Errors are learning opportunities
- The debug prompt pattern:
  ```
  "I got this error: [paste error message]
   Here's my code: [paste code]
   What's wrong and how do I fix it?"
  ```
- Common ML errors and how to prompt for solutions:
  - ImportError: Library not installed
  - ValueError: Data shape mismatch
  - KeyError: Missing column
  - TypeError: Wrong data type
- Live demo: Intentionally break code, debug with AI
- Power tip: Include error message + surrounding code

**Hands-on During Video:**
- Intentionally create an error in your stock data code
- Use AI to debug
- Document the fix

**Learning Outcome:** SO-1-2-2 - Debug code errors using AI assistance

---

#### Video 6: Stock Predictor - Phase 1 (Building Together) (10 min)
**Type:** Screen recording + talking head
**Content:**
- Bringing it together: Build stock predictor (Phase 1)
- Using proper prompts, create code that:
  1. Loads stock data for any ticker
  2. Calculates basic features (moving averages)
  3. Creates target variable (up/down next day)
  4. Displays sample of prepared data
- Walk through: Prompt → Code → Test → Iterate
- Save this notebook - we'll continue in Session 3

**Hands-on During Video:**
- Code along in Google Colab
- Use the prompt formula
- Iterate until working

**Learning Outcome:** SO-1-2-1, SO-1-2-2 - Apply prompt engineering to build ML pipeline

---

### Session 2 Mini Projects (Progressive)

#### Mini Project 1: Prompt Improvement Challenge (Easy) - 20 min
**Objective:** Transform bad prompts into good ones

**Bad Prompts Given:**
1. "Make ML code"
2. "Stock stuff"
3. "Fix this"

**Task:**
- Rewrite each using the Prompt Formula (Task + Context + Format + Constraints)
- Test improved prompts in ChatGPT
- Compare outputs: Bad prompt result vs Good prompt result
- Document the difference in quality

**Deliverable:** Document showing bad → good prompt transformations with output comparison

---

#### Mini Project 2: Iterative Code Enhancement (Medium) - 35 min
**Objective:** Practice the iteration cycle

**Task:**
- Start with this basic prompt: "Write code to load stock data"
- Get initial code from ChatGPT
- Iterate 5 times, each time adding:
  1. Error handling
  2. Support for date range selection
  3. Data visualization (price chart)
  4. Calculate daily returns
  5. Add descriptive comments
- Document each iteration: Prompt used + Code improvement gained

**Deliverable:** Colab notebook with 5 versions showing progressive enhancement + iteration log

---

#### Mini Project 3: Stock Feature Engineering with AI (Challenge) - 45 min
**Objective:** Create advanced features for stock prediction

**Task:**
- Research: Ask AI "What are the best technical indicators for stock prediction?"
- Pick 3 indicators (e.g., RSI, MACD, Moving Average)
- For each indicator:
  - Ask AI to explain what it is and why it's useful
  - Ask AI to generate code to calculate it
  - Add to your stock data notebook
- Create a visualization showing the indicators
- Save this enhanced dataset - you'll use it in Session 3!

**Deliverable:** Colab notebook with 3 technical indicators calculated and visualized

---

### Session 2 Quiz (12 questions, Mixed Format)

**Quiz 3: Prompt Engineering for ML**

**Multiple Choice (5):**
1. What makes a good prompt for generating ML code?
   - a) As short as possible
   - b) Specific with context and constraints
   - c) Using complex vocabulary
   - d) Writing it in all caps

2. What's the first step when debugging code with AI?
   - a) Delete everything and start over
   - b) Paste error message and code, ask for fix
   - c) Give up
   - d) Ask AI to explain quantum physics

3. The Prompt Formula is: Task + Context + ___ + Constraints
   - a) Time
   - b) Money
   - c) Format
   - d) Weather

4. How many iterations is normal to get good ML code?
   - a) Always first try
   - b) 3-5 iterations is common
   - c) 100+ iterations
   - d) It's impossible to get working code

5. When asking for code explanation, you should:
   - a) Never ask, just copy-paste
   - b) Only ask once
   - c) Specify the depth level you need
   - d) Ask in a different language

**True/False (4):**
6. Prompt engineering is a skill that improves with practice. (True)
7. You should never iterate on AI-generated code. (False)
8. Including error messages helps AI debug better. (True)
9. All prompts work the same on all LLMs. (False)

**Short Answer (3):**
10. What are the 4 components of the Prompt Formula?
11. How would you ask AI to explain code to a beginner?
12. Write a prompt to generate code for calculating a 20-day moving average for stock data.

**Passing Score:** 70% (9/12 correct)

---

## 📹 Session 3: Your First ML Model

**Duration:** ~2 hours video + 3-4 hours practice
**Day:** Day 5-7
**Hook:** "You're about to build a real ML model - and it will make predictions!"
**Storytelling Theme:** Switch to Cricket Match Prediction (keep it fresh!)

### The Story Arc
**Problem:** Meet Priya, a cricket fanatic who wants to predict match outcomes before they happen. She has historical match data - team stats, player performance, venue info. Can ML help her become a prediction champion? Let's build her cricket match predictor...

---

### Video Breakdown

#### Video 1: Welcome to Cricket Prediction (8 min)
**Type:** Talking head + cricket clips/graphics
**Content:**
- Why switch from stocks to cricket? (Show ML applies everywhere!)
- Priya's challenge: Predict match winner before first ball
- What data matters? Team rankings, player form, venue, toss, weather
- Preview: You'll build a working cricket predictor today
- Comparison: Stock prediction (regression/classification) vs Cricket (classification)
- Both use same ML principles, different data!

**Learning Outcome:** Understand ML generalizes across domains

---

#### Video 2: The Complete ML Pipeline (10 min)
**Type:** Screen recording + graphics
**Content:**
- Review: The 5-step ML pipeline
  1. **Get Data** → Cricket match history
  2. **Prepare Data** → Clean, features, train/test split
  3. **Choose Model** → Classification algorithm
  4. **Train Model** → Learn from past matches
  5. **Make Predictions** → Predict future matches
- Visual diagram showing data flow
- What we'll build: Simple classifier (Logistic Regression or Decision Tree)
- Use AI to help with every step

**Learning Outcome:** SO-1-3-1 - Understand complete ML workflow

---

#### Video 3: Setting Up Your ML Environment (10 min)
**Type:** Screen recording + talking head
**Content:**
- Prompt AI: "Help me set up a Python environment for ML in Google Colab"
- Install necessary libraries (pandas, numpy, sklearn, matplotlib)
- Test imports
- Download sample cricket dataset (we'll provide simplified CSV)
- Load data and inspect:
  ```python
  import pandas as pd
  data = pd.read_csv('cricket_matches.csv')
  print(data.head())
  print(data.info())
  ```
- Understanding your data: Features vs Target

**Hands-on During Video:**
- Follow along setting up your notebook
- Load the cricket dataset
- Display first 10 rows

**Learning Outcome:** SO-1-3-1 - Set up ML environment with AI guidance

---

#### Video 4: Data Preparation with AI (10 min)
**Type:** Screen recording
**Content:**
- Prompt: "I have cricket match data with these columns: [list columns]. Help me prepare it for ML classification. I want to predict match winner."
- AI guides you to:
  - Handle missing values
  - Convert categorical (team names) to numerical
  - Select relevant features
  - Create train/test split (80/20)
- Code walkthrough with explanations
- Check: X_train, X_test, y_train, y_test

**Hands-on During Video:**
- Run data preparation code
- Verify train/test split
- Check shapes: `X_train.shape`

**Learning Outcome:** SO-1-3-2 - Prepare data for ML with AI assistance

---

#### Video 5: Training Your First Model (10 min)
**Type:** Screen recording + talking head
**Content:**
- The magic moment: Training!
- Prompt: "Write code to train a classification model for this prepared cricket data"
- AI generates model training code:
  ```python
  from sklearn.linear_model import LogisticRegression
  model = LogisticRegression()
  model.fit(X_train, y_train)
  ```
- Explain what's happening (in simple terms)
- Make predictions: `predictions = model.predict(X_test)`
- Calculate accuracy: `accuracy_score(y_test, predictions)`
- Celebrate: You just trained an ML model!

**Hands-on During Video:**
- Train your model
- Make predictions
- Calculate accuracy
- Screenshot your results!

**Learning Outcome:** SO-1-3-2 - Train and evaluate an ML model

---

#### Video 6: Understanding Your Model's Code (10 min)
**Type:** Screen recording + talking head
**Content:**
- Now that it works, let's understand it deeply
- Prompt: "Explain this ML code line by line for a beginner"
- Go through each section:
  - Why import these libraries?
  - What does `.fit()` do?
  - What does `.predict()` do?
  - How is accuracy calculated?
- Add detailed comments to your notebook
- Experiment: What if you change the model? (Decision Tree instead)
- Prompt: "How do I change this to use a Decision Tree classifier?"

**Hands-on During Video:**
- Add line-by-line comments
- Try Decision Tree model
- Compare accuracies

**Learning Outcome:** SO-1-3-3 - Explain ML code with AI assistance

---

#### Video 7: Making Real Predictions (10 min)
**Type:** Screen recording + talking head
**Content:**
- Now the fun part: Predict new matches!
- Create new match scenario (manual input):
  ```python
  new_match = {
    'team_a_rank': 2,
    'team_b_rank': 5,
    'venue': 'home',
    'toss_won': 'team_a',
    ...
  }
  ```
- Convert to proper format
- Make prediction: `model.predict([new_match])`
- Interpret result: Team A or Team B wins?
- Try multiple scenarios
- Challenge: How confident is the model? (prediction probabilities)

**Hands-on During Video:**
- Create 3 different match scenarios
- Get predictions for each
- Check prediction probabilities

**Learning Outcome:** SO-1-3-2 - Use trained model for new predictions

---

#### Video 8: Next Steps & Module Wrap-up (8 min)
**Type:** Talking head + screen recording
**Content:**
- What you've achieved:
  ✓ Set up ML environment
  ✓ Prepared data
  ✓ Trained model
  ✓ Made predictions
  ✓ All using AI assistance!
- Limitations of this simple model (it's not perfect!)
- What's coming in Module 2: Better models, more data, real accuracy
- Teaser: Module 2-10 will cover advanced techniques
- Final challenge: Try improving your model with AI's help

**Learning Outcome:** Reflect on learning journey

---

### Session 3 Mini Projects (Progressive)

#### Mini Project 1: Model Comparison (Easy) - 25 min
**Objective:** Compare different classification algorithms

**Task:**
- You've used Logistic Regression for cricket prediction
- Ask AI: "What are 2 other classification algorithms I can try?"
- Implement 2 other algorithms (Decision Tree, Random Forest)
- Compare accuracy of all 3 models
- Create a comparison table:
  | Model | Accuracy | Speed | Complexity |

**Deliverable:** Colab notebook with 3 models trained and comparison table

---

#### Mini Project 2: Feature Importance (Medium) - 35 min
**Objective:** Understand what features matter most

**Task:**
- Prompt AI: "How can I see which features are most important for my cricket predictions?"
- Implement feature importance visualization
- Analyze: Which features matter most? (team rank? venue? toss?)
- Experiment: Remove the least important feature and retrain
- Did accuracy change?
- Document findings

**Deliverable:** Notebook with feature importance chart and analysis

---

#### Mini Project 3: Build Your Own Predictor (Challenge) - 60 min
**Objective:** End-to-end project from scratch

**Choose ONE:**
- **Option A:** Movie Success Predictor (Will a movie be hit or flop?)
- **Option B:** Exam Pass/Fail Predictor (Based on study hours, attendance, etc.)
- **Option C:** Your own idea (get approval from AI if feasible!)

**Requirements:**
1. Create or find simple dataset (can be synthetic - ask AI to generate)
2. Prepare data (with AI help)
3. Train classification model
4. Make predictions
5. Achieve >60% accuracy
6. Document entire process with markdown explanations
7. Add visualizations

**Deliverable:** Complete Colab notebook with end-to-end ML project + short writeup explaining your approach

---

### Session 3 Quiz (15 questions, Mixed Format)

**Quiz 4: Building Your First ML Model**

**Multiple Choice (7):**
1. What is the first step in the ML pipeline?
   - a) Train the model
   - b) Get and prepare data
   - c) Make predictions
   - d) Deploy to production

2. What does `model.fit(X_train, y_train)` do?
   - a) Deletes the data
   - b) Trains the model on training data
   - c) Makes predictions
   - d) Visualizes results

3. Why do we split data into train and test sets?
   - a) To confuse the model
   - b) To evaluate model on unseen data
   - c) It's required by Python
   - d) To make more data

4. What does an accuracy of 75% mean?
   - a) Model is 75% broken
   - b) Model predicts correctly 75% of the time
   - c) Model is perfect
   - d) Model takes 75 seconds

5. Which is a classification problem?
   - a) Predicting exact stock price
   - b) Predicting match winner (Team A or B)
   - c) Predicting house price
   - d) Predicting temperature

6. What does `.predict()` do?
   - a) Trains the model
   - b) Makes predictions on new data
   - c) Loads the dataset
   - d) Calculates accuracy

7. If your model gets 100% accuracy on training data, is that good?
   - a) Yes, always perfect
   - b) Maybe, but might be overfitting - check test accuracy
   - c) No, it's impossible
   - d) Doesn't matter

**True/False (5):**
8. You always need a GPU to train ML models. (False)
9. More data usually leads to better models. (True)
10. You can use the same trained model to make predictions many times. (True)
11. Classification predicts categories, regression predicts numbers. (True)
12. AI can help you debug ML code. (True)

**Short Answer (3):**
13. What are the 5 steps in the ML pipeline?
14. Explain what "training a model" means.
15. Name two classification algorithms you learned about.

**Passing Score:** 70% (11/15 correct)

---

## 📊 Module 1 Assessment Summary

### Overall Module Completion Criteria

To pass Module 1, learners must:
- ✅ Complete ALL setup steps (accounts, Colab, libraries)
- ✅ Pass all 3 quizzes with 70% or higher
- ✅ Submit 9 mini projects (3 per session)
- ✅ Complete final challenge project (Session 3 - Mini Project 3)
- ✅ Submit setup verification notebook

### Grading Breakdown
| Component | Weight | Description |
|-----------|--------|-------------|
| Quizzes (3) | 30% | 10% each (Setup, Session 1, Session 2-3 combined) |
| Mini Projects (9) | 40% | Evaluated on completeness and effort |
| Final Challenge | 25% | Session 3 Mini Project 3 - full ML project |
| Participation | 5% | Engagement tracking (video completion) |

**Pass Threshold:** 70% overall

---

## 🎯 Learning Outcome Mapping

### Session Outcomes Achieved

**Setup Session:**
- SO-1-0-1: Understand AI-assisted learning philosophy ✓
- SO-1-0-2: Create LLM accounts ✓
- SO-1-0-3: Identify LLM access methods ✓
- SO-1-0-4: Explain CPU vs GPU ✓
- SO-1-0-5: Set up Google Colab with GPU ✓
- SO-1-0-6: Install ML libraries ✓

**Session 1:**
- SO-1-1-1: Define ML and distinguish from traditional programming ✓
- SO-1-1-2: Identify real-world ML problems ✓
- SO-1-1-3: Use LLMs to explain concepts at multiple levels ✓

**Session 2:**
- SO-1-2-1: Construct effective prompts for ML tasks ✓
- SO-1-2-2: Iterate on AI-generated code ✓
- SO-1-2-3: Request code explanations at different depths ✓

**Session 3:**
- SO-1-3-1: Set up ML environment with AI guidance ✓
- SO-1-3-2: Train and evaluate ML model ✓
- SO-1-3-3: Explain ML code with AI assistance ✓

---

## 📚 Resources & Materials Needed

### For Instructors
- **Datasets:**
  - Stock price data (AAPL, GOOGL sample CSVs)
  - Cricket match data (simplified CSV with 500 matches)
  - Sample datasets for mini projects
- **Video Recording:**
  - Screen recording software (OBS, Camtasia)
  - Graphics/animations for concepts
  - Cricket clips / stock charts (licensed)
- **Colab Notebooks:**
  - Template notebooks for each session
  - Solution notebooks for mini projects
  - Auto-grading scripts

### For Learners
**Required:**
- Laptop with internet
- Google account (for Colab)
- ChatGPT/Gemini/Claude accounts

**Optional:**
- Dual monitors (easier for video + coding)
- Headphones
- Note-taking app

### Downloadable Resources
- Module 1 Quick Reference Guide (PDF)
- Prompt Engineering Cheat Sheet (PDF)
- Common ML Errors & Fixes Guide (PDF)
- Cricket Dataset (CSV)
- Stock Dataset (CSV)
- Setup Checklist (PDF)

---

## 🎬 Video Production Notes

### Filming Setup
- **Talking Head:** Clean background, good lighting, eye-level camera
- **Screen Recording:** 1920x1080, clear font size (14pt+), hide distractions
- **Graphics:** Simple animations, consistent color scheme
- **Pacing:** Speak clearly, pause after key concepts

### Editing Guidelines
- Add timestamps in description
- Include subtitles/captions
- Insert callout boxes for key points
- Background music (subtle, not distracting)
- Include "Pause & Practice" slides between sections

### Engagement Features
- Progress bars showing module completion
- "Quick Win" badges for completing mini projects
- Interactive polls in platform
- Discussion prompts after each session

---

## 🔄 Continuous Improvement

### Feedback Collection Points
- After each quiz: "What was confusing?"
- After mini projects: Difficulty rating (1-5)
- End of module survey
- Track: Video completion rates, rewind/fast-forward patterns

### Iteration Plan
- **Week 2:** Review quiz results, identify difficult concepts
- **Week 4:** Update videos based on common questions
- **Month 2:** Add bonus content for advanced learners
- **Month 3:** Refresh datasets, examples

---

## 📈 Success Metrics

### Module 1 Goals
- **Completion Rate:** >85% of enrolled learners
- **Quiz Pass Rate:** >90% pass all 3 quizzes (with retakes)
- **Engagement:** >80% watch time for videos
- **Satisfaction:** >4.0/5.0 learner rating

### Leading Indicators
- Setup completion rate (Day 1-2)
- First quiz pass rate (indicator of clarity)
- Mini project submission rate
- Forum/discussion activity

---

## 🚀 Next Steps After Module 1

### Prerequisites Check for Module 2
By end of Module 1, learners should have:
- ✅ Working Google Colab setup
- ✅ Understanding of ML basics
- ✅ Prompt engineering skills
- ✅ Built and trained at least 2 models (stock + cricket)
- ✅ Comfort with AI-assisted coding

### Module 2 Preview
**"Supervised Learning - Classification Deep Dive"**
- Advanced classification algorithms
- Real datasets (spam detection, customer churn)
- Feature engineering techniques
- Model evaluation metrics (confusion matrix, precision, recall)
- Deploy a classifier as simple web app

---

## 📞 Support & Help

### For Learners
- **Stuck on setup?** Check Setup Troubleshooting Guide
- **Code not working?** Post in Discussion Forum with:
  - Error message
  - Your code
  - What you've tried
- **Concept unclear?** Rewatch video, try different LLM explanation

### For Instructors
- Weekly instructor sync meetings
- Shared repository of improved prompts
- Learner question database
- Content update requests via GitHub

---

**Last Updated:** 2026-01-05
**Version:** 1.0
**Total Learner Time:** 15-20 hours (video + practice)
**Module Code:** ML-ENG-M1
