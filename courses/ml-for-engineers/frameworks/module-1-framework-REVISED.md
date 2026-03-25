# Module 1: Foundations - Understanding ML & Exploring Data
## Getting Ready to Build (Without Building Yet!)

**Course Code:** ML-ENG-M1
**Duration:** 1 week (self-paced)
**Total Video Content:** ~5-6 hours
**Hands-on Time:** ~4-5 hours (exploration only!)
**Theory/Practice Ratio:** 60% / 40%
**Pedagogy:** UNDERSTAND + EXPLORE (Light hands-on)

---

## 🎯 Module Purpose

**Primary Goal:** Understand ML concepts + Explore data + Master AI tools

**What Makes This Different from Module 0:**
- Module 0: "WOW!" (demos, no explanation)
- Module 1: "AH-HA!" (understanding concepts, exploring data)
- NOT YET: "I BUILT IT!" (that's Module 2+)

**Psychology:**
- Build conceptual foundation before hands-on building
- Explore before you create
- Understand the "why" before the "how"
- Master your AI tools (they'll be with you all course)

**What They Learn:**
- ✅ What is ML and when to use it
- ✅ Types of ML problems (conceptual)
- ✅ How to explore and visualize data
- ✅ Master prompt engineering
- ✅ Understand data structure and patterns

**What They DON'T Do (Yet):**
- ❌ Build ML models
- ❌ Train algorithms
- ❌ Make predictions
- ❌ That all starts Module 2!

**The Stock Data Journey Continues:**
- Module 0: "Wow, stock predictor!"
- Module 1: "Let me understand stock DATA" ← WE ARE HERE
- Module 3: "Now I'll BUILD the stock predictor!"

---

## 📅 Week Structure

```
Day 1 (2 hrs): Session 1 - Understanding Machine Learning
Day 2 (2 hrs): Session 2 - Working with Data
Day 3 (2 hrs): Session 3 - Data Visualization & Patterns
Day 4 (2 hrs): Session 4 - Mastering AI-Assisted Learning
Day 5-7: Practice projects and integration
```

---

## 📹 Session 1: Understanding Machine Learning

**Duration:** ~2 hours video + 1 hour practice
**Day:** Day 1
**Goal:** Conceptual understanding of ML
**Hands-on:** 20% (asking AI to explain concepts)

###  Video Breakdown

#### Video 1: What IS Machine Learning? (10 min)
**Type:** Talking head + animations
**The Hook:** "Remember Raj's stock predictor? Let's understand HOW it works"

**Content:**
1. **Definition** (3 min):
   - ML = Teaching computers to learn from data
   - Not: Explicit programming
   - Instead: Learn patterns from examples
   - Analogy: Teaching a child vs programming a robot

2. **Traditional Programming vs ML** (4 min):
   - Traditional: IF-THEN rules (you write all rules)
   - ML: Show examples, computer finds rules
   - Example comparison:
     - Spam filter (traditional): IF contains "free money" THEN spam
     - Spam filter (ML): Show 10,000 spam + 10,000 real emails → learns patterns

3. **The Key Insight** (3 min):
   - ML is for problems where rules are too complex to write
   - Or where patterns change over time
   - Perfect for: Stock prediction, face recognition, language understanding

**Learning Outcome:** Define ML and distinguish from traditional programming

---

#### Video 2: Types of ML - The Big Picture (10 min)
**Type:** Animated explanation + real examples

**Content:**
1. **Supervised Learning** (4 min):
   - You provide: Input + Correct answer
   - ML learns: Pattern from input to answer
   - Two types:
     - **Classification:** Predict category (Spam/Not spam, Win/Lose)
     - **Regression:** Predict number (Stock price, Temperature)
   - Examples: Stock predictor, Disease diagnosis

2. **Unsupervised Learning** (3 min):
   - You provide: Only input (no answers)
   - ML finds: Hidden patterns and groups
   - Example: Customer segmentation, Anomaly detection

3. **Reinforcement Learning** (2 min):
   - ML learns: By trial and error
   - Gets: Rewards for good actions
   - Example: Game playing AI, Robot control
   - Note: Not covered in this course (advanced topic)

4. **This Course Focus** (1 min):
   - Modules 2-4: Supervised learning (most common)
   - Module 5: Unsupervised learning
   - That's 90% of real-world ML!

**Learning Outcome:** Identify three types of ML and their use cases

---

#### Video 3: Classification vs Regression - Deep Dive (10 min)
**Type:** Screen recording + graphics

**Content:**
1. **Classification Explained** (4 min):
   - Predict: Category or class
   - Binary: Yes/No, Spam/Ham, Win/Lose
   - Multi-class: Type A/B/C, Species 1/2/3
   - Stock example: Will price go UP or DOWN tomorrow?
   - Output: Category label

2. **Regression Explained** (4 min):
   - Predict: Continuous number
   - Examples: Price ($150.25), Temperature (72.3°F), Age (45 years)
   - Stock example: What will the exact price be tomorrow? ($152.35)
   - Output: Number

3. **How to Choose?** (2 min):
   - Ask: "What am I predicting?"
   - Category → Classification
   - Number → Regression
   - Practice examples:
     - House price → Regression (number)
     - Email spam → Classification (category)
     - Disease diagnosis → Classification (which disease)
     - Patient recovery days → Regression (number of days)

**Hands-on During Video:**
- List 10 problems
- For each, identify: Classification or Regression?

**Learning Outcome:** Distinguish classification from regression

---

#### Video 4: The ML Pipeline (10 min)
**Type:** Animated flowchart + examples

**Content:**
1. **The 5 Steps** (5 min):
   ```
   DATA → PREPARE → TRAIN → TEST → DEPLOY
   ```

   **Step 1 - Get Data:**
   - Historical data with examples
   - For stocks: Past prices, volumes, indicators

   **Step 2 - Prepare Data:**
   - Clean (remove errors)
   - Format (make consistent)
   - Split (training vs testing)

   **Step 3 - Train Model:**
   - ML algorithm learns patterns
   - Uses training data

   **Step 4 - Test Model:**
   - Check accuracy on NEW data
   - Never seen before by model

   **Step 5 - Deploy:**
   - Use in real world
   - Make actual predictions

2. **Stock Predictor Example** (5 min):
   - Walk through each step for stock prediction
   - DATA: 5 years of Apple stock data
   - PREPARE: Calculate moving averages, indicators
   - TRAIN: Teach model to recognize patterns
   - TEST: Check predictions on last 6 months
   - DEPLOY: Use for tomorrow's prediction

**Learning Outcome:** Explain the 5-step ML pipeline

---

#### Video 5: When Should You Use ML? (10 min)
**Type:** Talking head + decision framework

**Content:**
1. **Good Use Cases** (4 min):
   - ✅ Pattern is complex (hard to write rules)
   - ✅ Pattern changes over time
   - ✅ Have lots of historical data
   - ✅ Don't need 100% accuracy
   - Examples: Image recognition, Recommendations, Fraud detection

2. **Bad Use Cases** (3 min):
   - ❌ Simple rule-based problem
   - ❌ No data available
   - ❌ Need perfect accuracy (life-critical)
   - ❌ Can't explain why (in some cases)
   - Examples: Calculator, Password validation, Flight control

3. **The Decision Framework** (3 min):
   - Decision tree to help choose
   - Exercise: 10 problems → Use ML or not?

**Hands-on During Video:**
- Think of 3 problems in your industry
- Should they use ML? Why or why not?

**Learning Outcome:** Evaluate when ML is appropriate

---

#### Video 6: AI as Your Learning Partner (8 min)
**Type:** Screen recording + philosophy

**Content:**
1. **The Learning Mindset** (3 min):
   - You don't need to memorize syntax
   - You DO need to understand concepts
   - AI handles code details
   - You handle strategy and understanding

2. **Live Demo** (5 min):
   - Ask ChatGPT: "Explain supervised learning"
   - Not clear? Ask: "Explain like I'm 10 years old"
   - Still confused? Ask: "Give me 3 real-world examples"
   - Want more? Ask: "What are common algorithms for this?"
   - This is your superpower!

**Learning Outcome:** Embrace AI-assisted learning mindset

---

### Session 1 Activities

#### Activity 1: ML Concept Mapping (30 min)
**Objective:** Solidify understanding through creation

**Task:**
- Create a concept map (mind map) of ML
- Center: "Machine Learning"
- Branches:
  - Types (Supervised, Unsupervised, Reinforcement)
  - Supervised splits: Classification, Regression
  - For each: 3 examples
- Use AI to help generate examples
- Make it visual (draw by hand or digital tool)

**Deliverable:** Concept map image + short explanation

---

#### Activity 2: Classification or Regression Game (20 min)
**Objective:** Practice identifying problem types

**Task:**
Given 20 problems, identify each as:
- Classification (Binary or Multi-class)
- Regression
- Not ML

Problems include:
1. Predicting diabetes risk (Yes/No)
2. Predicting patient blood pressure (number)
3. Calculating 2+2
4. Detecting credit card fraud
5. [16 more...]

**Deliverable:** Completed worksheet with reasoning

---

#### Activity 3: Industry Problem Analysis (40 min)
**Objective:** Apply ML thinking to your domain

**Task:**
- Identify 5 problems in your industry/interests
- For each, answer:
  1. Is this suitable for ML? Why/why not?
  2. If yes: Classification or Regression?
  3. What data would you need?
  4. What would "success" look like? (X% accuracy)
- Use AI to validate your thinking

**Deliverable:** Analysis document (5 problems analyzed)

---

### Session 1 Quiz (15 questions)

**Multiple Choice (8):**
1. Machine learning is best described as:
   - a) Writing rules for computers to follow
   - b) Teaching computers to learn patterns from data
   - c) A type of database
   - d) Advanced Excel formulas

2. Supervised learning requires:
   - a) Only input data
   - b) Input data and correct answers
   - c) No data
   - d) Only images

3. Predicting if an email is spam is:
   - a) Regression
   - b) Classification
   - c) Unsupervised learning
   - d) Not a ML problem

4. Predicting house prices ($) is:
   - a) Regression
   - b) Binary classification
   - c) Multi-class classification
   - d) Unsupervised learning

5. The first step in ML pipeline is:
   - a) Deploy the model
   - b) Train the model
   - c) Get and prepare data
   - d) Test the model

6. ML is NOT suitable for:
   - a) Complex pattern recognition
   - b) Simple calculator operations
   - c) Image classification
   - d) Text analysis

7. What's the difference between binary and multi-class classification?
   - a) Binary predicts 2 categories, multi-class predicts 3+
   - b) They're the same
   - c) Binary is harder
   - d) Multi-class doesn't use data

8. In the ML pipeline, why do we split data into train/test?
   - a) To make more data
   - b) To test model on data it hasn't seen
   - c) Because computers require it
   - d) To delete bad data

**True/False (4):**
9. ML can solve any problem if you have enough data. (False)
10. Classification predicts categories, regression predicts numbers. (True)
11. You always need labeled data for ML. (False - not for unsupervised)
12. The ML pipeline has 5 main steps. (True)

**Short Answer (3):**
13. Give 2 examples of classification problems.
14. Explain why stock prediction can be both classification AND regression.
15. Name the 5 steps in the ML pipeline.

**Passing Score:** 70% (11/15 correct)

---

## 📹 Session 2: Working with Data

**Duration:** ~2 hours video + 2 hours hands-on
**Day:** Day 2
**Goal:** Understand and explore data (STOCK DATA!)
**Hands-on:** 60% (this is where exploration starts!)

### Video Breakdown

#### Video 1: Data is Everything in ML (8 min)
**Type:** Talking head + graphics

**Content:**
1. **Why Data Matters** (3 min):
   - "Garbage in, garbage out"
   - Quality > Quantity (but need both)
   - ML models are only as good as their data

2. **Data for Stock Prediction** (5 min):
   - What data do we need to predict stocks?
   - Historical prices (OHLCV)
   - Volume patterns
   - Technical indicators
   - Maybe: News sentiment, economic indicators
   - Remember: We're EXPLORING today, not predicting yet!

**Learning Outcome:** Understand importance of data quality

---

#### Video 2: Understanding Data Structure (10 min)
**Type:** Screen recording in Colab

**Content:**
1. **Features vs Labels** (4 min):
   - **Features (X):** Input variables, what we know
   - **Labels (y):** Output variable, what we predict
   - Stock example:
     - Features: Yesterday's price, volume, moving average
     - Label: Tomorrow's price (or up/down direction)

2. **Rows vs Columns** (3 min):
   - Each row = one example/sample
   - Each column = one feature
   - Stock data: Each row = one day

3. **Data Types** (3 min):
   - Numerical: Numbers (price, volume)
   - Categorical: Categories (sector, exchange)
   - Date/Time: Temporal (trading date)
   - Text: Strings (company name)

**Hands-on During Video:**
- Look at sample stock data
- Identify: Which columns are features?
- Count: How many rows (days) of data?

**Learning Outcome:** Understand data structure terminology

---

#### Video 3: Loading Stock Data (10 min)
**Type:** Screen recording + AI assistance

**Content:**
1. **Using AI to Get Data Code** (4 min):
   - Prompt ChatGPT: "Write Python code to download stock data for Apple (AAPL) using yfinance library for the last 2 years"
   - Copy the code
   - Paste into Colab
   - Run!

2. **The Code Explained** (4 min):
   ```python
   import yfinance as yf
   import pandas as pd

   # Download data
   ticker = "AAPL"
   data = yf.download(ticker, start="2022-01-01", end="2024-01-01")

   # Display first rows
   print(data.head())
   ```
   - What each line does (AI explains)

3. **Exploring the Data** (2 min):
   ```python
   # See structure
   print(data.info())

   # See statistics
   print(data.describe())

   # Shape
   print(f"Rows: {data.shape[0]}, Columns: {data.shape[1]}")
   ```

**Hands-on During Video:**
- Run the code
- Load data for 3 different stocks (GOOGL, MSFT, TSLA)
- Compare the data structures

**Learning Outcome:** Load and inspect stock data

---

#### Video 4: Data Exploration Commands (10 min)
**Type:** Screen recording

**Content:**
1. **Essential Pandas Commands** (8 min):

   **View Data:**
   ```python
   data.head()        # First 5 rows
   data.tail()        # Last 5 rows
   data.sample(10)    # Random 10 rows
   ```

   **Understand Structure:**
   ```python
   data.info()        # Column types, null values
   data.describe()    # Statistics for each column
   data.columns       # Column names
   ```

   **Basic Calculations:**
   ```python
   data['Close'].mean()    # Average close price
   data['Volume'].max()    # Maximum volume
   data['Close'].std()     # Standard deviation
   ```

2. **Hands-on Practice** (2 min):
   - Try each command
   - What do you learn about the stock?

**Hands-on During Video:**
- Run all commands
- Answer: What's the average closing price?
- Answer: What's the highest volume day?

**Learning Outcome:** Use pandas for data exploration

---

#### Video 5: Understanding Stock Data Columns (10 min)
**Type:** Talking head + screen recording

**Content:**
1. **OHLCV Explained** (6 min):
   - **Open:** Price at market open (9:30 AM)
   - **High:** Highest price during the day
   - **Low:** Lowest price during the day
   - **Close:** Price at market close (4:00 PM)
   - **Volume:** Number of shares traded

   - Why each matters
   - Visual: Show daily candlestick

2. **Derived Features** (4 min):
   - We can calculate MORE features:
   - Daily return: (Today - Yesterday) / Yesterday
   - Moving average: Average of last N days
   - These help ML find patterns!
   - We'll create these next session

**Learning Outcome:** Understand stock data features

---

#### Video 6: Comparing Multiple Stocks (10 min)
**Type:** Screen recording

**Content:**
1. **Loading Multiple Stocks** (4 min):
   ```python
   tickers = ["AAPL", "GOOGL", "MSFT", "TSLA"]
   data_dict = {}

   for ticker in tickers:
       data_dict[ticker] = yf.download(ticker, start="2023-01-01")
   ```

2. **Comparing Statistics** (6 min):
   - Which had highest average price?
   - Which was most volatile? (std dev)
   - Which had highest trading volume?
   - Create comparison table

**Hands-on During Video:**
- Load 4-5 stocks of your choice
- Compare them
- Which would you invest in? (based on data only)

**Learning Outcome:** Compare datasets across multiple entities

---

### Session 2 Activities

#### Activity 1: Stock Data Explorer (45 min)
**Objective:** Deep exploration of stock data

**Task:**
1. Choose ONE stock (your favorite company)
2. Load 5 years of data
3. Answer these questions (using code):
   - What's the highest close price ever?
   - What's the lowest?
   - What's the average daily volume?
   - Which day had the biggest price jump?
   - Which day had the biggest price drop?
   - How many days did it close higher than $X? (you pick X)

4. Create a summary report

**Deliverable:**
- Colab notebook with code and answers
- Summary document with insights

---

#### Activity 2: Multi-Stock Comparison (40 min)
**Objective:** Compare 5 stocks from different sectors

**Task:**
1. Pick 5 stocks from different industries:
   - Tech (AAPL, GOOGL, MSFT)
   - Auto (TSLA, F, GM)
   - Retail (AMZN, WMT)
   - Finance (JPM, BAC)
   - Healthcare (JNJ, PFE)

2. For each, calculate:
   - Average close price (2023)
   - Total price change (%)
   - Average daily volume
   - Volatility (std deviation)

3. Create comparison table
4. Insights: Which sector performed best?

**Deliverable:**
- Comparison table
- 5 insights discovered

---

#### Activity 3: Data Quality Check (30 min)
**Objective:** Learn to identify data issues

**Task:**
1. Load stock data for any ticker
2. Check for:
   - Missing values: `data.isnull().sum()`
   - Duplicate dates: `data.index.duplicated().sum()`
   - Outliers: Any suspiciously high/low values?

3. Use AI to help:
   - Prompt: "How do I check for outliers in stock data?"
   - Prompt: "How do I handle missing values?"

4. Document findings

**Deliverable:**
- Data quality report
- Code used for checking

---

### Session 2 Quiz (12 questions)

**Multiple Choice (6):**
1. In stock data, what does OHLCV stand for?
   - a) Only High Low Close Volume
   - b) Open High Low Close Volume
   - c) Open Hour Low Close Value
   - d) Open High Late Close Volume

2. What does `data.head()` do?
   - a) Shows the first few rows of data
   - b) Deletes the data
   - c) Calculates the average
   - d) Sorts the data

3. Features in ML are:
   - a) The output we predict
   - b) The input variables we use to make predictions
   - c) Errors in the model
   - d) Data visualization

4. Which is NOT a good feature for stock prediction?
   - a) Previous day's closing price
   - b) Trading volume
   - c) The stock ticker symbol (just the letters)
   - d) Moving averages

5. `data.describe()` shows:
   - a) Only the first row
   - b) Statistical summary of numerical columns
   - c) All the data
   - d) Error messages

6. Why check for missing values?
   - a) It's not necessary
   - b) Missing values can cause errors in ML models
   - c) To delete all the data
   - d) Just for fun

**True/False (4):**
7. Each row in stock data typically represents one trading day. (True)
8. Volume tells you how many shares were traded. (True)
9. You can use AI to help you write data exploration code. (True)
10. More data is always better, even if it's low quality. (False)

**Short Answer (2):**
11. What's the difference between Features (X) and Labels (y)?
12. Why is it important to explore data before building ML models?

**Passing Score:** 70% (9/12 correct)

---

## 📹 Session 3: Data Visualization & Patterns

**Duration:** ~2 hours video + 2 hours hands-on
**Day:** Day 3
**Goal:** Visualize data and find patterns (Stock market!)
**Hands-on:** 70% (lots of charting!)

### Video Breakdown

#### Video 1: Why Visualize Data? (8 min)
**Type:** Talking head + examples

**Content:**
1. **Seeing is Understanding** (4 min):
   - Numbers in tables = Hard to see patterns
   - Graphs and charts = Instant insights
   - Example: Show table of 100 stock prices vs line chart
   - Which tells the story better?

2. **Types of Insights** (4 min):
   - Trends: Going up, down, sideways?
   - Seasonality: Repeating patterns?
   - Anomalies: Unusual spikes or drops?
   - Relationships: Do two things move together?

**Learning Outcome:** Understand value of visualization

---

#### Video 2: Stock Price Over Time (10 min)
**Type:** Screen recording

**Content:**
1. **Basic Line Chart** (5 min):
   ```python
   import matplotlib.pyplot as plt

   # Plot closing price
   plt.figure(figsize=(12,6))
   plt.plot(data.index, data['Close'])
   plt.title('Apple Stock Price Over Time')
   plt.xlabel('Date')
   plt.ylabel('Price ($)')
   plt.grid(True)
   plt.show()
   ```

2. **What Do We See?** (5 min):
   - Overall trend (up/down?)
   - Volatility (big swings?)
   - Key events (crashes, rallies?)
   - Using AI to enhance:
     - Prompt: "Add a 50-day moving average to this plot"
     - See trend more clearly!

**Hands-on During Video:**
- Create price chart for your chosen stock
- Identify: Uptrend or downtrend?
- Find: Biggest price jump

**Learning Outcome:** Create and interpret time series plots

---

#### Video 3: Volume Analysis (10 min)
**Type:** Screen recording

**Content:**
1. **Volume Bar Chart** (5 min):
   ```python
   plt.figure(figsize=(12,6))
   plt.bar(data.index, data['Volume'])
   plt.title('Trading Volume Over Time')
   plt.xlabel('Date')
   plt.ylabel('Volume')
   plt.show()
   ```

2. **Volume Insights** (5 min):
   - High volume = High interest (news event?)
   - Low volume = Quiet period
   - Volume + Price change = Signals
   - High volume + price up = Strong bullish signal
   - High volume + price down = Strong bearish signal

**Hands-on During Video:**
- Create volume chart
- Find day with highest volume
- Research: What happened that day? (news)

**Learning Outcome:** Visualize and interpret volume data

---

#### Video 4: Multiple Plot Types (10 min)
**Type:** Screen recording

**Content:**
1. **Histogram - Price Distribution** (3 min):
   ```python
   plt.hist(data['Close'], bins=50)
   plt.title('Distribution of Closing Prices')
   plt.xlabel('Price')
   plt.ylabel('Frequency')
   plt.show()
   ```
   - What it shows: Most common price ranges

2. **Scatter Plot - Price vs Volume** (3 min):
   ```python
   plt.scatter(data['Close'], data['Volume'])
   plt.title('Price vs Volume')
   plt.xlabel('Price')
   plt.ylabel('Volume')
   plt.show()
   ```
   - Any relationship between price and volume?

3. **Box Plot - Price Spread** (4 min):
   - Shows median, quartiles, outliers
   - Comparing multiple stocks side-by-side

**Hands-on During Video:**
- Create all 3 plot types
- Interpret each one

**Learning Outcome:** Use different visualization types appropriately

---

#### Video 5: Advanced Visualizations with AI (10 min)
**Type:** Screen recording + AI collaboration

**Content:**
1. **Candlestick Charts** (5 min):
   - Show OHLC in one visual
   - Prompt AI: "Create a candlestick chart for stock data using plotly"
   - Interactive chart!

2. **Multi-Line Comparison** (5 min):
   - Compare 3-4 stocks on one chart
   - Color-coded lines
   - Legend
   - Prompt AI: "Plot AAPL, GOOGL, MSFT on same chart, normalized to start at 100"

**Hands-on During Video:**
- Create candlestick chart
- Create comparison chart for 4 stocks

**Learning Outcome:** Create advanced visualizations with AI help

---

#### Video 6: Finding Patterns (10 min)
**Type:** Screen recording + analysis

**Content:**
1. **Pattern Recognition** (6 min):
   - **Trends:** Sustained movement (up/down)
   - **Support/Resistance:** Price levels that act as floors/ceilings
   - **Seasonality:** "Sell in May and go away"
   - **Volatility Clustering:** Big moves follow big moves

2. **Using Visualizations** (4 min):
   - How to spot each pattern visually
   - Example: Moving average crossovers
   - Note: These aren't ML yet - just exploration!
   - In Module 3, ML will find these patterns automatically

**Learning Outcome:** Identify visual patterns in financial data

---

### Session 3 Activities

#### Activity 1: 5-Chart Stock Analysis (60 min)
**Objective:** Complete visual analysis of one stock

**Task:**
For your chosen stock (2 years of data), create:
1. Line chart: Closing price over time
2. Bar chart: Volume over time
3. Histogram: Price distribution
4. Scatter plot: Price vs Volume
5. Candlestick chart (with AI help)

For each chart, write 2-3 sentences of insights

**Deliverable:**
- Notebook with all 5 charts
- Analysis document with insights for each

---

#### Activity 2: Multi-Stock Visual Comparison (50 min)
**Objective:** Compare stocks visually

**Task:**
1. Choose 3 stocks from same sector (e.g., 3 tech stocks)
2. Create normalized price comparison chart (all start at 100)
3. Which performed best?
4. Create 3 separate volume charts
5. Any correlation between their movements?

**Deliverable:**
- Comparison chart
- Analysis: Which stock would you pick and why?

---

#### Activity 3: Pattern Hunter (40 min)
**Objective:** Find and document patterns

**Task:**
1. Load 5 years of data for S&P 500 index (^GSPC)
2. Create visualizations to find:
   - 3 clear uptrends
   - 3 clear downtrends
   - 2 major crashes/rallies
   - 1 sideways (ranging) period

3. Mark dates on chart
4. Research: What caused each major movement?

**Deliverable:**
- Annotated chart with patterns marked
- Historical context for each pattern

---

### Session 3 Quiz (10 questions)

**Multiple Choice (5):**
1. Which chart is best for showing price movement over time?
   - a) Pie chart
   - b) Line chart
   - c) Donut chart
   - d) Word cloud

2. What does a histogram show?
   - a) Time series
   - b) Distribution/frequency of values
   - c) Correlation
   - d) Nothing useful

3. High trading volume usually indicates:
   - a) Low interest in the stock
   - b) High interest/activity in the stock
   - c) The stock is worthless
   - d) Data error

4. A candlestick chart shows:
   - a) Only closing price
   - b) Open, High, Low, Close in one visual
   - c) Only volume
   - d) Historical news

5. Normalizing prices to start at 100 helps:
   - a) Make data look better
   - b) Compare relative performance of different stocks
   - c) Delete unwanted data
   - d) Fix errors

**True/False (3):**
6. Visualizations help identify patterns that numbers alone might hide. (True)
7. You should only use one type of chart for all data. (False)
8. AI can help you create complex visualizations. (True)

**Short Answer (2):**
9. Why is it useful to plot both price AND volume together?
10. Name 3 types of charts/plots we learned in this session.

**Passing Score:** 70% (7/10 correct)

---

## 📹 Session 4: Mastering AI-Assisted Learning

**Duration:** ~1.5 hours video + 1.5 hours practice
**Day:** Day 4
**Goal:** Become expert at using AI for learning
**Hands-on:** 50%

### Video Breakdown

#### Video 1: The Prompt Engineering Formula Revisited (10 min)
**Type:** Screen recording + examples

**Content:**
1. **The Formula** (3 min):
   ```
   TASK + CONTEXT + FORMAT + CONSTRAINTS = Great Prompt
   ```

2. **For Data Work** (7 min):

   **Bad Prompt:**
   "Make a chart"

   **Good Prompt:**
   "Create a line chart showing Apple stock closing prices for the last year. Use matplotlib. Include title, axis labels, and grid. Make the figure 12x6 inches."

   TASK: Create a line chart
   CONTEXT: Apple stock closing prices, last year
   FORMAT: matplotlib
   CONSTRAINTS: Include labels, grid, specific size

**Hands-on During Video:**
- Transform 5 bad prompts to good prompts

**Learning Outcome:** Master prompt formula for data tasks

---

#### Video 2: Iterative Prompting for Data Analysis (10 min)
**Type:** Screen recording demonstration

**Content:**
1. **Starting Simple** (8 min):
   - Initial: "Load stock data"
   - Iterate 1: "Add error handling"
   - Iterate 2: "Add data validation"
   - Iterate 3: "Add comments for beginners"
   - Iterate 4: "Create summary statistics"

2. **Live Example** (2 min):
   - Show full conversation with ChatGPT
   - Each iteration improves the code
   - Final result: Production-quality script

**Hands-on During Video:**
- Try the iteration cycle yourself

**Learning Outcome:** Iterate effectively with AI

---

#### Video 3: Getting Explanations at Your Level (10 min)
**Type:** Screen recording

**Content:**
1. **Multi-Level Explanations** (8 min):
   - Same code, explained 3 ways:

   **Level 1 - Complete Beginner:**
   "Explain this data loading code like I've never programmed before"

   **Level 2 - Some Experience:**
   "Explain this code with moderate technical detail"

   **Level 3 - Want Deep Understanding:**
   "Explain this code including the underlying pandas mechanics"

2. **When to Use Each** (2 min):
   - Start with Level 1
   - Move to Level 2 once comfortable
   - Level 3 for deep learning

**Hands-on During Video:**
- Take one code snippet
- Get all 3 levels of explanation
- Compare understanding

**Learning Outcome:** Request appropriate explanation depth

---

#### Video 4: Debugging with AI (10 min)
**Type:** Screen recording + troubleshooting

**Content:**
1. **The Debug Prompt Pattern** (5 min):
   ```
   "I got this error: [full error message]

    Here's my code:
    [paste code]

    What's wrong and how do I fix it?"
   ```

2. **Common Data Errors** (5 min):
   - KeyError: Column doesn't exist
   - TypeError: Wrong data type
   - ValueError: Invalid value
   - For each: Example error → AI solution

**Hands-on During Video:**
- Intentionally create 3 errors
- Debug each with AI
- Document solutions

**Learning Outcome:** Debug efficiently with AI help

---

#### Video 5: Building Your Prompt Library (8 min)
**Type:** Talking head + examples

**Content:**
1. **Categories to Build** (4 min):
   - Data Loading
   - Data Exploration
   - Visualization
   - Debugging
   - Learning & Explanation

2. **Template Examples** (4 min):
   - "Load [data type] from [source]..."
   - "Create [chart type] showing [data] with [features]..."
   - "Explain [concept] at [level]..."
   - "Debug this error: [error]..."

**Learning Outcome:** Create reusable prompt templates

---

#### Video 6: Module 1 Wrap-Up & Looking Ahead (10 min)
**Type:** Talking head

**Content:**
1. **What You've Learned** (4 min):
   - ✅ What ML is and when to use it
   - ✅ Classification vs Regression
   - ✅ The ML pipeline
   - ✅ Data exploration and visualization
   - ✅ Prompt engineering mastery
   - ✅ You understand stock data deeply!

2. **What's Next** (3 min):
   - **Module 2:** Build your FIRST real ML models!
   - Classification: Spam detection, Churn prediction
   - Hands-on model building starts!
   - You're now ready because you understand:
     - What ML is
     - What data looks like
     - How to explore patterns
     - How to use AI effectively

3. **The Journey Continues** (3 min):
   - Module 0: Demos (WOW!)
   - Module 1: Understanding (AH-HA!) ← You are here
   - Module 2: Building (I DID IT!) ← Next week
   - "You have the foundation. Time to build!"

**Learning Outcome:** Ready for model building in Module 2

---

### Session 4 Activities

#### Activity 1: Prompt Engineering Challenge (40 min)
**Objective:** Create 15 excellent prompts

**Task:**
Create 3 prompts for each category:
1. Data Loading (3 prompts)
2. Data Cleaning (3 prompts)
3. Visualization (3 prompts)
4. Analysis (3 prompts)
5. Debugging (3 prompts)

Test each prompt with AI, keep the ones that work well

**Deliverable:**
- Prompt library document
- Rating (1-5) for each prompt's effectiveness

---

#### Activity 2: End-to-End Data Project (90 min)
**Objective:** Put everything together

**Task:**
"Complete Stock Analysis Report" - Choose any stock:

1. **Load Data** (15 min):
   - 3 years of historical data
   - Verify quality

2. **Explore Data** (20 min):
   - Summary statistics
   - Missing values check
   - Basic insights

3. **Visualize** (30 min):
   - 5 different charts
   - Each tells part of the story

4. **Analyze** (20 min):
   - Find 3 patterns/insights
   - Support with visualizations
   - Explain what you found

5. **Document** (15 min):
   - Professional notebook
   - Markdown cells explaining each step
   - Conclusions

**Deliverable:**
- Complete Colab notebook
- Professional report (can be in notebook)

---

### Session 4 Quiz (10 questions)

**Multiple Choice (5):**
1. The prompt formula is: TASK + CONTEXT + ___ + CONSTRAINTS
   - a) Time
   - b) Format
   - c) Money
   - d) Code

2. Iterative prompting means:
   - a) Asking the same question repeatedly
   - b) Refining prompts step-by-step to improve results
   - c) Using multiple LLMs
   - d) Deleting all prompts

3. When debugging, you should provide AI with:
   - a) Only the error message
   - b) Only your code
   - c) Both error message and relevant code
   - d) Nothing, AI knows automatically

4. Multi-level explanations help because:
   - a) They waste time
   - b) You can choose the depth that matches your understanding
   - c) They're required by Python
   - d) They make code run faster

5. A good prompt library includes:
   - a) Only one prompt type
   - b) Templates for common tasks across categories
   - c) Random prompts
   - d) Only debugging prompts

**True/False (3):**
6. Iterating on prompts usually gives better results than one-shot prompts. (True)
7. You should always ask for the most technical explanation possible. (False)
8. AI can help you learn faster by providing customized explanations. (True)

**Short Answer (2):**
9. Why is it useful to build a personal prompt library?
10. Describe the 4 components of the prompt formula.

**Passing Score:** 70% (7/10 correct)

---

## 📊 Module 1 Assessment Summary

### Completion Criteria

To pass Module 1:
- ✅ Watch all videos (~5-6 hours)
- ✅ Complete exploration activities (4-5 hours hands-on)
- ✅ Pass all 4 quizzes with 70%+ each
- ✅ Submit end-to-end stock analysis project
- ✅ Build personal prompt library

### Grading Breakdown

| Component | Weight | Description |
|-----------|--------|-------------|
| Quizzes (4) | 40% | 10% each session quiz |
| Session Activities | 30% | Hands-on exploration tasks |
| Final Stock Analysis | 25% | End-to-end project (Session 4) |
| Prompt Library | 5% | Quality and completeness |

**Pass Threshold:** 70% overall

---

## 🎯 Learning Outcomes Achieved

### By End of Module 1, Learners Can:

**Conceptual Understanding (Understand Level):**
- ✅ Define machine learning and distinguish from traditional programming
- ✅ Identify supervised, unsupervised, and reinforcement learning
- ✅ Distinguish classification from regression problems
- ✅ Explain the 5-step ML pipeline
- ✅ Evaluate when ML is appropriate for a problem

**Data Skills (Apply + Analyze Level):**
- ✅ Load stock data programmatically
- ✅ Explore datasets using pandas commands
- ✅ Identify features and labels in datasets
- ✅ Create multiple types of visualizations
- ✅ Interpret patterns in financial data
- ✅ Compare multiple stocks visually

**AI-Assisted Learning (Apply Level):**
- ✅ Construct effective prompts using formula
- ✅ Iterate on prompts to improve results
- ✅ Request explanations at appropriate levels
- ✅ Debug code errors with AI assistance
- ✅ Maintain a personal prompt library

**Critical Thinking:**
- ✅ Identify suitable ML problems in their industry
- ✅ Recognize data quality issues
- ✅ Interpret visualizations for insights
- ✅ Evaluate different approaches

---

## 🔗 Connection to Module 2

### The Bridge

**Module 1 Ending:**
- "You now understand what ML is"
- "You can explore data like a pro"
- "You've mastered AI-assisted learning"
- "You've explored stock data deeply"
- "But you haven't BUILT a model yet..."

**Module 2 Opening:**
- "Time to build your FIRST real ML model!"
- "Classification: Start with simple problems"
- "Remember the spam detector demo? You'll build it!"
- "Remember the cricket predictor? You'll build that too!"
- "We'll build skills with simple problems first..."

**Module 3 Connection:**
- "...THEN you'll build that stock predictor you've been exploring!"
- "Because you understand the data (Module 1)"
- "And you've built classifiers (Module 2)"
- "Stock prediction will be your Module 3 victory!"

---

## 📚 Resources Provided

### For Learners
- Stock data loading templates
- Visualization code templates
- Prompt library starter pack
- Pandas cheat sheet
- Data exploration checklist

### For Instructors
- All quiz questions (Google Forms ready)
- Grading rubrics
- Sample stock datasets (CSV backups)
- Video scripts
- Troubleshooting guide

---

**Module 1 Status:** COMPLETE ✅
**Ready for:** Module 2 (First Real ML!)
**Estimated Learner Time:** 9-11 hours total

---

**Last Updated:** 2026-01-05
**Version:** 2.0 (Revised - Exploration Focus, No Model Building)
