# Module 1: Data Exploration Exercises Rubric
## Comprehensive Assessment Guide

**Module:** 1 - Foundations
**Focus:** Understanding ML & Exploring Data (NO model building yet)
**Total Points:** 60 (across 4 sessions)
**Passing Grade:** 42 points (70%)
**Version:** 1.0
**Created:** 2026-01-06

---

## Rubric Philosophy

Module 1 is about **exploration and understanding**, not technical mastery. Students should:
- ✅ Understand WHAT machine learning is and WHEN to use it
- ✅ Explore data deeply using pandas
- ✅ Create meaningful visualizations
- ✅ Master AI-assisted learning

Students should **NOT** yet:
- ❌ Build machine learning models (that's Module 2+)
- ❌ Train algorithms or make predictions
- ❌ Worry about model accuracy

---

## Session 1.1: Understanding Machine Learning (15 points)

### Exercise 1: ML Concept Map (5 points)

**Objective:** Create visual representation of ML concepts and relationships

| Score | Description | Requirements Met |
|-------|-------------|------------------|
| **5 pts (Excellent)** | Comprehensive, clear, insightful | ✓ ML at center with branches to 3 types<br>✓ Supervised splits into classification/regression<br>✓ 3+ real-world examples per type<br>✓ Relationships/connections shown<br>✓ Visually organized and easy to read |
| **4 pts (Good)** | Complete with all major concepts | ✓ All ML types present<br>✓ 2 examples per type<br>✓ Basic relationships shown<br>✓ Readable organization |
| **3 pts (Adequate)** | Basic but missing some elements | ✓ Main types present<br>✓ Some examples included<br>✓ Structure somewhat clear |
| **0-2 pts (Poor)** | Incomplete or unclear | ✗ Missing major concepts<br>✗ Few or no examples<br>✗ Disorganized |

**Evidence Required:**
- Image of concept map (photo of hand-drawn or digital file)
- Includes: Supervised, Unsupervised, Reinforcement Learning
- Classification and Regression distinguished
- Real-world examples labeled

---

### Exercise 2: Classification or Regression Game (6 points)

**Objective:** Identify problem types correctly and explain reasoning

| Score | Description | Accuracy Range |
|-------|-------------|----------------|
| **6 pts (Excellent)** | Mastery demonstrated | 18-20 correct (90-100%)<br>Clear reasoning for each<br>Distinguishes binary/multi-class |
| **4-5 pts (Good)** | Strong understanding | 14-17 correct (70-85%)<br>Reasoning provided for most<br>Mostly correct classifications |
| **2-3 pts (Adequate)** | Developing understanding | 10-13 correct (50-65%)<br>Basic reasoning<br>Some confusion evident |
| **0-1 pts (Poor)** | Major gaps | <10 correct (<50%)<br>Little or no reasoning<br>Fundamental misunderstandings |

**Example Problems to Classify:**
1. Predicting diabetes risk (Yes/No) → **Binary Classification**
2. Predicting patient blood pressure (number) → **Regression**
3. Calculating 2+2 → **Not ML**
4. Detecting credit card fraud → **Binary Classification**
5. Identifying flower species (3 types) → **Multi-class Classification**
6. Estimating house prices → **Regression**
7. Recommending products → **Multi-class Classification or Ranking**
8. Forecasting temperature → **Regression**

**Grading Notes:**
- Some problems may have multiple valid interpretations (e.g., stock prediction as regression OR classification)
- Award full credit if student provides reasonable justification
- Focus on understanding of "category vs number" distinction

---

### Exercise 3: Industry Problem Analysis (4 points)

**Objective:** Apply ML thinking to real-world domain problems

| Score | Description | Requirements Met |
|-------|-------------|------------------|
| **4 pts (Excellent)** | Thorough, thoughtful analysis | ✓ 5 domain-specific problems identified<br>✓ ML suitability clearly determined for each<br>✓ Classification vs Regression specified<br>✓ Required data listed<br>✓ Success metrics defined (e.g., "85% accuracy") |
| **3 pts (Good)** | Complete with good reasoning | ✓ 5 problems analyzed<br>✓ ML assessment provided<br>✓ Problem types identified<br>✓ Basic data requirements |
| **2 pts (Adequate)** | Basic effort shown | ✓ 3-4 problems analyzed<br>✓ Basic ML suitability assessment<br>✓ Some data considerations |
| **0-1 pts (Poor)** | Minimal effort | ✗ <3 problems<br>✗ Superficial analysis<br>✗ No clear reasoning |

**Example Industry Problem (Healthcare):**
```
Problem: Predicting patient readmission within 30 days

ML Suitable? YES
- Pattern is complex (multiple factors)
- Historical data available
- Doesn't need 100% accuracy
- Can improve over time

Type: Binary Classification (Readmitted: Yes/No)

Data Needed:
- Patient demographics (age, gender)
- Diagnosis codes
- Length of stay
- Medications prescribed
- Previous admissions
- Lab results

Success Criteria:
- 80% precision (avoid false alarms)
- 70% recall (catch most at-risk patients)
- Better than current manual system (50% accuracy)
```

---

## Session 1.2: Working with Data (15 points)

### Exercise 1: Stock Data Explorer (7 points)

**Objective:** Deep exploration of stock data using pandas

| Score | Description | Requirements Met |
|-------|-------------|------------------|
| **7 pts (Excellent)** | Comprehensive exploration | ✓ All 6 questions answered correctly<br>✓ Code is well-commented<br>✓ 5 years of data loaded<br>✓ Summary report with insights<br>✓ Proper pandas commands used |
| **5-6 pts (Good)** | Thorough work | ✓ 4-5 questions answered<br>✓ Code runs correctly<br>✓ Basic comments<br>✓ Summary provided |
| **3-4 pts (Adequate)** | Basic completion | ✓ 2-3 questions answered<br>✓ Code mostly works<br>✓ Minimal documentation |
| **0-2 pts (Poor)** | Incomplete | ✗ <2 questions answered<br>✗ Code errors<br>✗ No summary |

**Required Questions to Answer:**
1. What's the highest close price ever?
2. What's the lowest close price?
3. What's the average daily volume?
4. Which day had the biggest price jump? (day-to-day increase)
5. Which day had the biggest price drop?
6. How many days did it close higher than $[pick a threshold]?

**Code Quality Indicators:**
- Uses `.max()`, `.min()`, `.mean()` appropriately
- Proper filtering with boolean indexing
- Date handling (if finding specific days)
- Comments explain what each section does

---

### Exercise 2: Multi-Stock Comparison (5 points)

**Objective:** Compare stocks from different sectors systematically

| Score | Description | Requirements Met |
|-------|-------------|------------------|
| **5 pts (Excellent)** | Insightful comparison | ✓ 5 stocks from different sectors<br>✓ 4+ metrics calculated (avg price, %change, volume, volatility)<br>✓ Clear comparison table<br>✓ 5+ insights about sector performance |
| **4 pts (Good)** | Complete comparison | ✓ 5 stocks analyzed<br>✓ 3-4 metrics<br>✓ Table created<br>✓ 3-4 insights |
| **3 pts (Adequate)** | Basic comparison | ✓ 3-4 stocks<br>✓ 2 metrics<br>✓ Basic insights |
| **0-2 pts (Poor)** | Minimal effort | ✗ <3 stocks<br>✗ Incomplete analysis |

**Suggested Stock Selections:**
- **Tech:** AAPL, GOOGL, MSFT
- **Auto:** TSLA, F, GM
- **Retail:** AMZN, WMT
- **Finance:** JPM, BAC
- **Healthcare:** JNJ, PFE

**Metrics to Calculate:**
- Average close price (2023)
- Total % change (start to end of year)
- Average daily volume
- Volatility (standard deviation of daily returns)

**Sample Insight:**
"Tech sector (AAPL, GOOGL, MSFT) showed 25% average growth in 2023, outperforming auto sector (5% growth). Healthcare was most stable with lowest volatility."

---

### Exercise 3: Data Quality Check (3 points)

**Objective:** Identify and document data quality issues

| Score | Description | Requirements Met |
|-------|-------------|------------------|
| **3 pts (Excellent)** | Thorough quality check | ✓ Missing values checked (`.isnull().sum()`)<br>✓ Duplicates checked (`.duplicated()`)<br>✓ Outliers detected (statistical methods)<br>✓ Findings documented<br>✓ Handling strategies proposed |
| **2 pts (Good)** | Good effort | ✓ 2-3 quality checks performed<br>✓ Findings documented<br>✓ Basic handling approach |
| **1 pt (Adequate)** | Basic check | ✓ 1 quality check<br>✓ Minimal documentation |
| **0 pts (Poor)** | No checking | ✗ No quality assessment performed |

**Required Checks:**
```python
# 1. Missing Values
print(data.isnull().sum())

# 2. Duplicates
print(f"Duplicate dates: {data.index.duplicated().sum()}")

# 3. Outliers (example using IQR)
Q1 = data['Close'].quantile(0.25)
Q3 = data['Close'].quantile(0.75)
IQR = Q3 - Q1
outliers = data[(data['Close'] < Q1 - 1.5*IQR) | (data['Close'] > Q3 + 1.5*IQR)]
print(f"Potential outliers: {len(outliers)}")
```

---

## Session 1.3: Data Visualization & Patterns (15 points)

### Exercise 1: Five-Chart Stock Analysis (8 points)

**Objective:** Create diverse visualizations and extract insights

| Score | Description | Charts & Insights |
|-------|-------------|-------------------|
| **8 pts (Excellent)** | Professional analysis | ✓ All 5 charts created with proper formatting<br>✓ Titles, labels, grids present<br>✓ 2-3 insightful observations per chart<br>✓ Charts are readable and informative |
| **6-7 pts (Good)** | Complete work | ✓ All 5 charts present<br>✓ Proper formatting<br>✓ 1-2 observations per chart<br>✓ Basic insights |
| **4-5 pts (Adequate)** | Partial completion | ✓ 3-4 charts<br>✓ Basic formatting<br>✓ Minimal insights |
| **0-3 pts (Poor)** | Incomplete | ✗ <3 charts<br>✗ Poor formatting<br>✗ No insights |

**Required Charts:**

1. **Line Chart:** Closing price over time
   - **Insight Example:** "Strong uptrend from Jan 2022 to July 2023, then consolidation period"

2. **Bar Chart:** Volume over time
   - **Insight Example:** "Volume spikes correlate with major price movements (earnings reports)"

3. **Histogram:** Price distribution
   - **Insight Example:** "Stock spent most time in $140-$160 range, indicating support/resistance"

4. **Scatter Plot:** Price vs Volume
   - **Insight Example:** "Weak negative correlation - high volume often on down days (panic selling)"

5. **Candlestick Chart:** (with AI assistance)
   - **Insight Example:** "Multiple long green candles show strong buying pressure in Q2 2023"

**Formatting Requirements:**
- Figure size: (12, 6) or similar readable size
- Title present and descriptive
- Axis labels clear
- Grid enabled (helps readability)
- Colors appropriate

---

### Exercise 2: Multi-Stock Visual Comparison (4 points)

**Objective:** Compare stock performance visually

| Score | Description | Requirements Met |
|-------|-------------|------------------|
| **4 pts (Excellent)** | Excellent comparison | ✓ Normalized chart (all start at 100)<br>✓ 3 stocks from same sector<br>✓ Best performer identified with justification<br>✓ Volume charts for all 3<br>✓ Correlation observation |
| **3 pts (Good)** | Good comparison | ✓ Comparison chart created<br>✓ 3 stocks<br>✓ Best performer ID'd<br>✓ Volume charts |
| **2 pts (Adequate)** | Basic effort | ✓ Basic comparison<br>✓ 2 stocks<br>✓ Minimal analysis |
| **0-1 pts (Poor)** | Incomplete | ✗ No comparison or 1 stock only |

**Normalization Example:**
```python
# Normalize to 100 at start
normalized = (df / df.iloc[0]) * 100
plt.plot(normalized.index, normalized['AAPL'], label='AAPL')
plt.plot(normalized.index, normalized['GOOGL'], label='GOOGL')
plt.plot(normalized.index, normalized['MSFT'], label='MSFT')
plt.legend()
plt.title('Tech Stocks Normalized Performance (Base=100)')
```

---

### Exercise 3: Pattern Hunter (3 points)

**Objective:** Identify and document market patterns

| Score | Description | Requirements Met |
|-------|-------------|------------------|
| **3 pts (Excellent)** | Comprehensive pattern ID | ✓ 3 uptrends marked with dates<br>✓ 3 downtrends marked<br>✓ 2 crashes/rallies marked<br>✓ 1 sideways period<br>✓ Historical context researched<br>✓ 5 years of data |
| **2 pts (Good)** | Good effort | ✓ 4-6 patterns identified<br>✓ Dates provided<br>✓ Basic historical context |
| **1 pt (Adequate)** | Basic patterns | ✓ 2-3 patterns<br>✓ Some dates<br>✓ Minimal context |
| **0 pts (Poor)** | No patterns | ✗ No pattern identification |

**Pattern Types to Find:**

| Pattern | What to Look For | Example Date Range |
|---------|------------------|-------------------|
| **Uptrend** | Sustained price increase over weeks/months | "Mar 2023 - Aug 2023" |
| **Downtrend** | Sustained price decrease | "Jan 2022 - Jun 2022" |
| **Crash** | Sudden sharp drop | "March 2020 (COVID crash)" |
| **Rally** | Sudden sharp rise | "Nov 2020 (vaccine news)" |
| **Sideways** | Price consolidation, no clear direction | "Aug 2021 - Nov 2021" |

**Historical Context Example:**
"S&P 500 crash in March 2020 (28% drop) caused by COVID-19 pandemic and lockdown fears. Market recovered rapidly due to Fed intervention and stimulus packages."

---

## Session 1.4: Mastering AI-Assisted Learning (15 points)

### Exercise 1: Prompt Engineering Library (5 points)

**Objective:** Build reusable prompt collection

| Score | Description | Requirements Met |
|-------|-------------|------------------|
| **5 pts (Excellent)** | Comprehensive library | ✓ 15+ prompts (3 per category)<br>✓ 5 categories covered<br>✓ All tested with AI<br>✓ Rated 1-5 for effectiveness<br>✓ Notes on what works well |
| **4 pts (Good)** | Complete library | ✓ 12-14 prompts<br>✓ 5 categories<br>✓ Most tested<br>✓ Ratings included |
| **3 pts (Adequate)** | Basic library | ✓ 9-11 prompts<br>✓ Basic organization<br>✓ Some testing |
| **0-2 pts (Poor)** | Incomplete | ✗ <9 prompts<br>✗ Minimal effort |

**Required Categories & Examples:**

**1. Data Loading (3 prompts)**
```
Example Prompt (Rating: 5/5):
"Write Python code to download stock data for Apple (AAPL)
from 2020-01-01 to 2024-01-01 using yfinance library.
Include error handling for network issues.
Save to CSV as backup."

Why it works: Specific ticker, exact dates, library specified,
error handling requested, output format clear.
```

**2. Data Cleaning (3 prompts)**
```
Example Prompt (Rating: 4/5):
"I have a DataFrame with missing values in the 'Volume' column.
Write code to: 1) Check how many missing values exist,
2) Fill them with the median of the column,
3) Verify no missing values remain."

Why it works: Clear problem, specific steps, verification included.
```

**3. Visualization (3 prompts)**
```
Example Prompt (Rating: 5/5):
"Create a line chart showing AAPL closing prices over time using matplotlib.
Requirements: figure size 12x6, title 'Apple Stock Price 2020-2024',
axis labels, grid enabled, blue line color."

Why it works: Chart type clear, specific formatting, all requirements listed.
```

**4. Analysis (3 prompts)**
```
Example Prompt (Rating: 4/5):
"Given a stock DataFrame with columns Date, Open, High, Low, Close, Volume,
calculate: 1) Average daily return, 2) Total percentage change from start to end,
3) Days with volume above average. Explain the code."

Why it works: Data structure specified, multiple metrics clear,
explanation requested.
```

**5. Debugging (3 prompts)**
```
Example Prompt (Rating: 5/5):
"I got this error: 'KeyError: 'Adj Close'' when running:
df['Adj Close'].mean(). My DataFrame has columns:
['Date', 'Open', 'High', 'Low', 'Close', 'Volume'].
What's wrong and how do I fix it?"

Why it works: Exact error message, relevant code,
DataFrame structure provided.
```

---

### Exercise 2: End-to-End Stock Analysis (10 points)

**Objective:** Complete professional data analysis project

This is the **capstone project for Module 1**. It integrates all skills learned.

**Grading Breakdown (10 points total):**

| Section | Points | Excellent (Full Points) | Good (80%) | Adequate (60%) | Poor (<60%) |
|---------|--------|-------------------------|------------|----------------|-------------|
| **1. Load Data** | 2 | 3 years loaded, verified, correct range | 2 years, mostly verified | 1 year or basic loading | Incomplete or errors |
| **2. Explore** | 2 | Stats + missing check + 3 insights | Stats + 2 insights | Basic stats, 1 insight | Minimal exploration |
| **3. Visualize** | 2 | 5 different charts, clear purpose | 4 charts, basic purpose | 2-3 charts | <2 charts |
| **4. Analyze** | 2 | 3 patterns, visualizations, clear explanations | 2 patterns, supported | 1 pattern, basic support | No patterns |
| **5. Document** | 2 | Professional markdown, clear conclusions | Good documentation, basic conclusions | Minimal docs | No documentation |

**Detailed Requirements:**

#### Section 1: Load Data (2 points)
```python
# Required elements:
- Import yfinance and pandas
- Download 3 years of data for chosen stock
- Display first and last rows to verify date range
- Check data shape (should be ~750 trading days)
- Confirm no critical missing values

# Markdown explanation:
"I chose [STOCK] because [reason].
Loaded 3 years (2021-2024) with X trading days."
```

#### Section 2: Explore Data (2 points)
```python
# Required elements:
- df.describe() for all columns
- df.isnull().sum() to check missing values
- Calculate: max price, min price, average volume
- 3 insights discovered

# Markdown insights example:
"Insights:
1. Stock traded in $120-$180 range (50% spread)
2. Volume averages 50M shares/day, spikes to 200M on earnings
3. Price volatility (std dev) is $15, indicating moderate risk"
```

#### Section 3: Visualize (2 points)
```python
# Required elements:
- Chart 1: Price over time (line chart)
- Chart 2: Volume distribution (histogram)
- Chart 3: Price vs Volume (scatter)
- Chart 4: Moving average overlay (line chart)
- Chart 5: Student's choice (surprise me!)

# Each chart must have:
- Title, axis labels, grid
- Caption explaining what it shows
```

#### Section 4: Analyze & Find Patterns (2 points)
```python
# Required elements:
- Pattern 1: Uptrend or downtrend (with dates)
- Pattern 2: Volatility period or consolidation
- Pattern 3: Correlation observation or seasonal pattern

# Each pattern needs:
- Visualization support (marked on chart or separate chart)
- Date range specified
- Explanation of what it means

# Example:
"Pattern 1: Strong Uptrend (Jan 2023 - Aug 2023)
- Price increased from $130 to $175 (+34%)
- Driven by strong earnings reports and tech sector growth
- See Chart 6 for annotated trend line"
```

#### Section 5: Professional Documentation (2 points)
```
# Required elements:
- Markdown cells throughout explaining each step
- Clear section headers (## Section 1: Load Data)
- Code comments for complex operations
- Final conclusions section summarizing:
  * What you learned about this stock
  * Key patterns identified
  * What you'd want to know next
  * How this prepares you for Module 2 (building predictors)

# Professional touches:
- Table of contents (bonus)
- Consistent formatting
- No random print statements
- Clean, readable code
```

**Sample Conclusion:**
```markdown
## Conclusions

### What I Learned
This analysis of Apple stock (2021-2024) revealed moderate volatility
with strong long-term growth. The 3-year return was +45%, outpacing
the S&P 500.

### Key Patterns
1. Seasonal strength in Q4 (holiday sales)
2. Earnings reports drive 20%+ volume spikes
3. Strong correlation between volume and price movement direction

### Next Steps
For Module 2, I'm interested in building a classifier to predict
whether the stock will close up or down based on opening price,
volume, and moving averages. This exploration gave me the
foundational data understanding needed.

### Skills Demonstrated
- Pandas data manipulation (loading, filtering, aggregation)
- Matplotlib/seaborn visualization (5 chart types)
- Pattern recognition in time series
- AI-assisted code generation and debugging
- Professional analysis documentation
```

---

## Overall Module 1 Assessment Summary

### Total Points Distribution

| Session | Points | Focus Area |
|---------|--------|------------|
| 1.1 | 15 | Understanding ML Concepts |
| 1.2 | 15 | Working with Data |
| 1.3 | 15 | Data Visualization |
| 1.4 | 15 | AI-Assisted Learning + Capstone |
| **Total** | **60** | **Complete Module** |

### Passing Criteria

- **Minimum Points:** 42/60 (70%)
- **Required Elements:**
  - All 4 session quizzes passed (70%+ each)
  - End-to-end project completed
  - Prompt library with 12+ prompts
  - At least 3 visualizations in final project

### Bonus Points (max +5)

- Exceptional final project visualization: +2
- Discovers unique insight: +2
- Helps peer in forum: +1

**Maximum Total:** 65 points (60 base + 5 bonus)

---

## Grading Calibration Guide

### What "Excellent" Work Looks Like:
- Goes beyond minimum requirements
- Shows genuine curiosity (asks questions, explores deeper)
- Visualizations are clear and insightful
- Code is commented and organized
- Insights are specific, not generic
- Professional presentation
- Demonstrates growth from Session 1 to Session 4

### What "Good" Work Looks Like:
- Meets all requirements
- Shows solid understanding
- Visualizations are functional
- Code works correctly
- Basic insights provided
- Organized submission
- Steady progress through module

### What "Adequate" Work Looks Like:
- Meets most requirements (70%+)
- Shows developing understanding
- Visualizations present but basic
- Code has minor issues but mostly works
- Minimal insights
- Somewhat organized
- Completes tasks but doesn't elaborate

### What "Poor" Work (Needs Revision) Looks Like:
- Missing major requirements (<70%)
- Significant misunderstandings
- Code doesn't run or major errors
- No insights, just charts
- Disorganized submission
- Appears rushed or copy-pasted without understanding

---

## Common Student Questions & Grading Responses

### Q: "My stock data only goes back 2 years, not 3. Is that OK?"
**A:** Yes, 2 years is acceptable if that's all that's available for your chosen stock. Mention this limitation in your documentation. Full credit if properly documented.

### Q: "I used different chart types than suggested. Will I lose points?"
**A:** No! As long as you have 5 different chart types that are appropriate for the data and you provide insights for each, that's excellent. Creativity encouraged.

### Q: "My code works in Colab but the shared link doesn't show outputs. What do I do?"
**A:** Save outputs by: Runtime → Run all, then File → Save. Share the link again. Or export as HTML/PDF with outputs visible.

### Q: "I found a pattern that's not in the course materials. Is that OK?"
**A:** Absolutely! That's what exploration is about. Document what you found and explain it clearly. This may earn bonus points for unique insight.

### Q: "Can I use a different stock than the examples?"
**A:** Yes! Choose any stock with sufficient history. Just document why you chose it.

---

## Instructor Checklist for Grading

For each student submission, verify:

- [ ] All required evidence files submitted
- [ ] Code executes without critical errors
- [ ] Minimum requirements met for each exercise
- [ ] Quiz scores recorded (70%+ each)
- [ ] Insights go beyond surface observations
- [ ] AI tools used effectively (evident in prompt library)
- [ ] Professional documentation present
- [ ] Calculation of final score accurate
- [ ] Feedback provided (praise + specific improvements)
- [ ] Student ready for Module 2 (model building)

---

**Remember:** Module 1 is about building confidence with data and tools. Grade with encouragement. Students who complete all exercises thoughtfully are ready for Module 2's model building challenges.

**Version:** 1.0
**Last Updated:** 2026-01-06
**Next Review:** After first cohort completion
