# AI Prompt Library Template
## Module 1: Foundations - ML for Engineers

---

## How to Use This Template

1. **Copy this template** to your own document (Google Docs, Notion, Excel, etc.)
2. **Fill in prompts** as you progress through the course
3. **Rate effectiveness** (1-5 stars) after using each prompt
4. **Add notes** about what worked and what didn't
5. **Build your collection** - aim for 50+ prompts by end of course

**Tip:** The best prompt library is personal to YOU!

---

## Prompt Template Format

For each prompt, record:
- **Prompt Text**: The exact prompt you used
- **Category**: Type of task (see categories below)
- **Context**: What you were trying to achieve
- **AI Tool**: ChatGPT, Claude, Gemini, etc.
- **Output Quality**: 1-5 stars
- **Notes**: What worked, what to improve
- **Date Used**: When you used it

---

## Categories

1. **Data Loading** - Loading CSV, handling dates, reading files
2. **Data Exploration** - head(), describe(), info(), statistics
3. **Data Filtering** - Conditional selection, date ranges
4. **Data Transformation** - Creating columns, calculations
5. **Visualization** - Charts, plots, graphs
6. **Data Quality** - Missing values, duplicates, outliers
7. **Debugging** - Error messages, fixing code
8. **Learning** - Explanations, concepts, theory
9. **Code Optimization** - Improving performance
10. **General** - Miscellaneous prompts

---

## Sample Prompts (Use as Examples)

### Category: Data Loading

| # | Prompt | Context | Tool | Rating | Notes |
|---|--------|---------|------|--------|-------|
| 1 | Write Python code to load a CSV file named 'stock_data.csv' into a pandas DataFrame. Include error handling for file not found. | Loading stock data | ChatGPT | ⭐⭐⭐⭐⭐ | Perfect code, worked first time |
| 2 | Load CSV with dates as index: Read 'AAPL.csv', parse 'Date' column as datetime, and set it as the index | Setting up time series data | Claude | ⭐⭐⭐⭐ | Needed to add parse_dates=True |
| 3 | Load multiple CSV files in a loop and store in a dictionary with ticker symbols as keys | Loading portfolio data | Gemini | ⭐⭐⭐⭐ | Good, added my own error handling |

### Category: Data Exploration

| # | Prompt | Context | Tool | Rating | Notes |
|---|--------|---------|------|--------|-------|
| 4 | Show me pandas code to explore a DataFrame: first/last rows, shape, column names, data types, and summary statistics | Initial data exploration | ChatGPT | ⭐⭐⭐⭐⭐ | Complete and clear |
| 5 | Calculate mean, median, std dev, min, and max for the 'Adj Close' column, formatted nicely | Stock price statistics | Claude | ⭐⭐⭐⭐ | Added formatted output |
| 6 | Write code to show the 10 rows with highest trading volume | Finding top volume days | ChatGPT | ⭐⭐⭐⭐⭐ | Used nlargest(), perfect |

### Category: Data Filtering

| # | Prompt | Context | Tool | Rating | Notes |
|---|--------|---------|------|--------|-------|
| 7 | Filter DataFrame to show only rows where 'Adj Close' > $200 and 'Volume' > 100 million | Finding high price/volume days | ChatGPT | ⭐⭐⭐⭐⭐ | Correct boolean indexing |
| 8 | Select data for year 2023 only from a DataFrame with datetime index | Year-based filtering | Claude | ⭐⭐⭐⭐ | Showed multiple methods |
| 9 | Find days where price increased by more than 5% | Identifying big gains | Gemini | ⭐⭐⭐ | Had to modify for pct_change |

### Category: Data Transformation

| # | Prompt | Context | Tool | Rating | Notes |
|---|--------|---------|------|--------|-------|
| 10 | Create a new column 'Daily_Return' with percentage change from previous day | Calculating returns | ChatGPT | ⭐⭐⭐⭐⭐ | Used pct_change() * 100 |
| 11 | Add a 50-day moving average column to my stock DataFrame | Adding technical indicator | Claude | ⭐⭐⭐⭐⭐ | rolling(50).mean(), perfect |
| 12 | Calculate cumulative return from start of period | Portfolio performance tracking | ChatGPT | ⭐⭐⭐⭐ | Needed to understand formula |

### Category: Visualization

| # | Prompt | Context | Tool | Rating | Notes |
|---|--------|---------|------|--------|-------|
| 13 | Create a line chart of stock price over time using matplotlib. Include title, axis labels, and grid | Basic time series plot | ChatGPT | ⭐⭐⭐⭐⭐ | Clean, professional code |
| 14 | Make a histogram of daily returns with 50 bins, add a vertical line at the mean | Returns distribution | Claude | ⭐⭐⭐⭐ | Good, I changed colors |
| 15 | Create an interactive candlestick chart using plotly for the last 100 days | OHLC visualization | ChatGPT | ⭐⭐⭐⭐⭐ | Interactive, impressive! |

### Category: Data Quality

| # | Prompt | Context | Tool | Rating | Notes |
|---|--------|---------|------|--------|-------|
| 16 | Check for missing values in all columns and show count and percentage | Data quality audit | ChatGPT | ⭐⭐⭐⭐⭐ | Comprehensive check |
| 17 | Find duplicate dates in my DataFrame and show them | Checking data integrity | Claude | ⭐⭐⭐⭐ | Used duplicated() method |
| 18 | Detect outliers in 'Volume' column using IQR method | Outlier detection | Gemini | ⭐⭐⭐⭐ | Explained IQR well |

### Category: Debugging

| # | Prompt | Context | Tool | Rating | Notes |
|---|--------|---------|------|--------|-------|
| 19 | I get KeyError: 'Adj Close'. My code: df['Adj Close'].mean(). What's wrong? | Column name error | ChatGPT | ⭐⭐⭐⭐⭐ | Check df.columns, found space |
| 20 | Fix this error: TypeError: unsupported operand type(s) for +: 'int' and 'str' | Type mismatch | Claude | ⭐⭐⭐⭐ | Explained type conversion |
| 21 | My plot shows dates as numbers, not formatted dates. How to fix? | Date formatting in matplotlib | ChatGPT | ⭐⭐⭐⭐ | Use date formatting |

### Category: Learning

| # | Prompt | Context | Tool | Rating | Notes |
|---|--------|---------|------|--------|-------|
| 22 | Explain what pct_change() does in pandas, with examples | Understanding method | ChatGPT | ⭐⭐⭐⭐⭐ | Clear explanation |
| 23 | What's the difference between 'Close' and 'Adj Close'? | Stock data concepts | Claude | ⭐⭐⭐⭐⭐ | Explained splits/dividends |
| 24 | Explain rolling windows in pandas like I'm a beginner | Learning concept | Gemini | ⭐⭐⭐⭐ | Good analogy |

---

## YOUR PROMPT LIBRARY

### Category: Data Loading

| # | Prompt | Context | Tool | Rating | Notes | Date |
|---|--------|---------|------|--------|-------|------|
| | | | | | | |
| | | | | | | |
| | | | | | | |

### Category: Data Exploration

| # | Prompt | Context | Tool | Rating | Notes | Date |
|---|--------|---------|------|--------|-------|------|
| | | | | | | |
| | | | | | | |
| | | | | | | |

### Category: Data Filtering

| # | Prompt | Context | Tool | Rating | Notes | Date |
|---|--------|---------|------|--------|-------|------|
| | | | | | | |
| | | | | | | |
| | | | | | | |

### Category: Data Transformation

| # | Prompt | Context | Tool | Rating | Notes | Date |
|---|--------|---------|------|--------|-------|------|
| | | | | | | |
| | | | | | | |
| | | | | | | |

### Category: Visualization

| # | Prompt | Context | Tool | Rating | Notes | Date |
|---|--------|---------|------|--------|-------|------|
| | | | | | | |
| | | | | | | |
| | | | | | | |

### Category: Data Quality

| # | Prompt | Context | Tool | Rating | Notes | Date |
|---|--------|---------|------|--------|-------|------|
| | | | | | | |
| | | | | | | |
| | | | | | | |

### Category: Debugging

| # | Prompt | Context | Tool | Rating | Notes | Date |
|---|--------|---------|------|--------|-------|------|
| | | | | | | |
| | | | | | | |
| | | | | | | |

### Category: Learning

| # | Prompt | Context | Tool | Rating | Notes | Date |
|---|--------|---------|------|--------|-------|------|
| | | | | | | |
| | | | | | | |
| | | | | | | |

### Category: Code Optimization

| # | Prompt | Context | Tool | Rating | Notes | Date |
|---|--------|---------|------|--------|-------|------|
| | | | | | | |
| | | | | | | |
| | | | | | | |

### Category: General

| # | Prompt | Context | Tool | Rating | Notes | Date |
|---|--------|---------|------|--------|-------|------|
| | | | | | | |
| | | | | | | |
| | | | | | | |

---

## Prompt Engineering Tips

### The TASK-CONTEXT-FORMAT-CONSTRAINTS Formula

**Good Prompt Structure:**
```
[TASK] + [CONTEXT] + [FORMAT] + [CONSTRAINTS]
```

**Example:**
```
TASK: Create a line chart
CONTEXT: Showing Apple stock price for the last year
FORMAT: Using matplotlib with title, labels, and grid
CONSTRAINTS: Figure size 12x6, blue line, 2px width
```

**Becomes:**
```
Create a line chart showing Apple stock price for the last year using matplotlib.
Include title, axis labels, and grid. Set figure size to 12x6 inches,
use blue color for the line, and set line width to 2 pixels.
```

### Tips for Better Prompts

1. **Be Specific**
   - ❌ "Make a chart"
   - ✅ "Create a line chart of stock closing prices using matplotlib"

2. **Provide Context**
   - ❌ "Filter the data"
   - ✅ "Filter stock DataFrame to show only 2023 data where volume > 100M"

3. **Specify Format**
   - ❌ "Show me the code"
   - ✅ "Show me Python pandas code with comments explaining each step"

4. **Add Constraints**
   - ❌ "Calculate statistics"
   - ✅ "Calculate mean, median, std dev for Close price, formatted to 2 decimal places"

5. **Iterate and Refine**
   - Start simple: "Load CSV file"
   - Refine: "Add error handling"
   - Enhance: "Add data validation"

### When to Use Which AI Tool

| Tool | Best For | Notes |
|------|----------|-------|
| **ChatGPT** | Code generation, debugging | Fast, reliable |
| **Claude** | Explanations, long responses | Great for learning |
| **Gemini** | Google ecosystem, data analysis | Good with sheets |
| **GitHub Copilot** | Real-time coding assistance | IDE integration |

### Prompt Templates

**Data Loading Template:**
```
Load [DATA_TYPE] from [SOURCE] into pandas DataFrame.
Include [FEATURES: error handling, date parsing, etc.].
Set [COLUMN_NAME] as the index.
```

**Visualization Template:**
```
Create a [CHART_TYPE] showing [DATA] over [TIME_PERIOD].
Use [LIBRARY: matplotlib/seaborn/plotly].
Include [FEATURES: title, labels, legend, grid].
Style: [COLORS, SIZE, etc.].
```

**Debugging Template:**
```
I got this error: [ERROR_MESSAGE]

Here's my code:
[CODE]

What's wrong and how do I fix it?
```

**Learning Template:**
```
Explain [CONCEPT] at a [LEVEL: beginner/intermediate/advanced] level.
Include [EXAMPLES, ANALOGIES, CODE SAMPLES].
Focus on [SPECIFIC_ASPECT] if applicable.
```

---

## Progress Tracking

### Module 1 Goals
- [ ] 50+ prompts collected
- [ ] All categories covered
- [ ] 3+ prompts per category
- [ ] At least 80% rated 4+ stars
- [ ] Notes added to all prompts

### Current Stats
- Total Prompts: _____
- Average Rating: _____
- Most Used Category: _____
- Favorite AI Tool: _____
- Top 3 Best Prompts: _____, _____, _____

---

## Advanced: Prompt Chains

Sometimes one prompt isn't enough. Chain prompts for complex tasks:

**Example: Stock Analysis Chain**

1. "Load Apple stock data from CSV and show summary statistics"
2. "Add a daily returns column and calculate volatility"
3. "Create a visualization with price and volume subplots"
4. "Add 20-day and 50-day moving averages to the price chart"
5. "Identify days where price crossed above the 50-day MA"

Each builds on the previous!

---

## Reflection Questions

Use these to improve your prompting:

1. **What made this prompt effective?**
2. **What would I change next time?**
3. **Did I get the result on first try?**
4. **How many iterations did it take?**
5. **Could I make it more specific?**
6. **Did I learn something new from the response?**

---

## Export & Share

**Ways to use this library:**

1. **Personal Reference** - Quick lookup during coding
2. **Team Sharing** - Share best prompts with classmates
3. **Progress Tracking** - See improvement over time
4. **Final Project** - Use as reference for capstone
5. **Job Interviews** - Show your AI collaboration skills

---

**Course**: ML for Engineers - Module 1: Foundations
**Created**: 2026-01-05
**Version**: 1.0

**Remember**: The best prompt library is one you actually USE and UPDATE regularly!
