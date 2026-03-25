# AI Prompts Used - Pandas Stock Exploration
## Module 1: Foundations - ML for Engineers

---

## Overview

This document contains all the AI prompts that can be used to generate and understand the pandas stock exploration code. These prompts follow the **TASK + CONTEXT + FORMAT + CONSTRAINTS** formula taught in the course.

---

## Category 1: Data Loading Prompts

### Prompt 1.1: Basic CSV Loading
```
TASK: Write Python code to load a CSV file into a pandas DataFrame
CONTEXT: The file is stock price data with columns Date, Open, High, Low, Close, Volume
FORMAT: Python code with comments
CONSTRAINTS: Use pandas library, include error handling
```

**Expected Output**: Code using `pd.read_csv()` with error handling

---

### Prompt 1.2: Loading with Date Index
```
TASK: Load stock data CSV and set Date as the index
CONTEXT: CSV file has Date column in YYYY-MM-DD format
FORMAT: Python pandas code
CONSTRAINTS: Parse dates automatically, handle missing dates
```

**Expected Output**: Code using `parse_dates=True` and `index_col='Date'`

---

## Category 2: Data Exploration Prompts

### Prompt 2.1: View Dataset Structure
```
TASK: Show me code to explore the structure of a pandas DataFrame
CONTEXT: I want to see first few rows, last few rows, and overall information
FORMAT: Python code with print statements
CONSTRAINTS: Use head(), tail(), info(), describe()
```

**Expected Output**: Comprehensive exploration code

---

### Prompt 2.2: Get Summary Statistics
```
TASK: Calculate summary statistics for stock price data
CONTEXT: DataFrame has columns: Open, High, Low, Close, Volume
FORMAT: Python code that prints statistics in a readable format
CONSTRAINTS: Include mean, median, std dev, min, max for Close price
```

**Expected Output**: Code using `.describe()` and individual stat functions

---

## Category 3: Data Filtering Prompts

### Prompt 3.1: Filter by Price Condition
```
TASK: Filter stock data to show only days where closing price was above $200
CONTEXT: Working with pandas DataFrame with 'Adj Close' column
FORMAT: Python code with explanation
CONSTRAINTS: Use boolean indexing, show count of matching rows
```

**Expected Output**: `df[df['Adj Close'] > 200]`

---

### Prompt 3.2: Multiple Conditions
```
TASK: Filter stock data using multiple conditions
CONTEXT: Find days with both high price (>$200) AND high volume (>100M shares)
FORMAT: Python pandas code
CONSTRAINTS: Use & operator, show both conditions clearly
```

**Expected Output**: `df[(df['Adj Close'] > 200) & (df['Volume'] > 100000000)]`

---

### Prompt 3.3: Date Range Filter
```
TASK: Filter DataFrame to show only data from year 2023
CONTEXT: DataFrame has Date column as datetime type
FORMAT: Python code
CONSTRAINTS: Use datetime indexing, handle as string or datetime object
```

**Expected Output**: Date filtering code using string slicing or boolean indexing

---

## Category 4: Column Creation Prompts

### Prompt 4.1: Calculate Daily Returns
```
TASK: Create a new column with daily percentage returns
CONTEXT: Stock DataFrame with 'Adj Close' column
FORMAT: Python pandas code with explanation
CONSTRAINTS: Use pct_change(), multiply by 100 for percentage, handle first row (NaN)
```

**Expected Output**: `df['Daily_Return'] = df['Adj Close'].pct_change() * 100`

---

### Prompt 4.2: Moving Average
```
TASK: Add a 50-day moving average column
CONTEXT: Stock price DataFrame with 'Adj Close' column
FORMAT: Python code
CONSTRAINTS: Use rolling window, explain what moving average means
```

**Expected Output**: `df['MA_50'] = df['Adj Close'].rolling(window=50).mean()`

---

### Prompt 4.3: Price Range
```
TASK: Calculate daily price range (High - Low) as a new column
CONTEXT: DataFrame has 'High' and 'Low' columns for each trading day
FORMAT: Python pandas code
CONSTRAINTS: Create new column called 'Price_Range'
```

**Expected Output**: `df['Price_Range'] = df['High'] - df['Low']`

---

## Category 5: Finding Extremes Prompts

### Prompt 5.1: Find Maximum Value Day
```
TASK: Find the day with the highest closing price
CONTEXT: Stock DataFrame with 'Adj Close' column and Date index
FORMAT: Python code that prints the date and price
CONSTRAINTS: Use idxmax() to find index, then loc to get full row
```

**Expected Output**: Code using `idxmax()` and `.loc[]`

---

### Prompt 5.2: Top N Days
```
TASK: Find the top 10 days with highest trading volume
CONTEXT: DataFrame with 'Volume' column
FORMAT: Python code showing Date, Close price, and Volume for top 10
CONSTRAINTS: Use sort_values(), head(), select specific columns
```

**Expected Output**: `df.nlargest(10, 'Volume')[['Date', 'Adj Close', 'Volume']]`

---

## Category 6: Grouping and Aggregation Prompts

### Prompt 6.1: Yearly Statistics
```
TASK: Group stock data by year and calculate average price for each year
CONTEXT: DataFrame with Date column (datetime type) and Adj Close
FORMAT: Python pandas code with clear output
CONSTRAINTS: Extract year from date, group by year, show mean, min, max
```

**Expected Output**: Code using `dt.year` and `groupby()`

---

### Prompt 6.2: Multiple Aggregations
```
TASK: For each year, calculate: starting price, ending price, min, max, and average
CONTEXT: Stock price DataFrame with Date and Adj Close columns
FORMAT: Python pandas code creating a summary table
CONSTRAINTS: Use agg() with multiple functions (first, last, min, max, mean)
```

**Expected Output**: `groupby().agg()` with named aggregations

---

### Prompt 6.3: Monthly Average Volume
```
TASK: Calculate average trading volume for each month across all years
CONTEXT: DataFrame with Date (datetime) and Volume columns
FORMAT: Python code showing monthly averages
CONSTRAINTS: Group by year-month combination using dt.to_period('M')
```

**Expected Output**: Code using `to_period('M')` and `groupby()`

---

## Category 7: Data Quality Prompts

### Prompt 7.1: Check Missing Values
```
TASK: Check for missing values in a DataFrame
CONTEXT: Stock price DataFrame with multiple columns
FORMAT: Python code showing count of missing values per column
CONSTRAINTS: Use isnull().sum(), show total missing values
```

**Expected Output**: Code using `df.isnull().sum()`

---

### Prompt 7.2: Find Duplicates
```
TASK: Check for duplicate dates in stock data
CONTEXT: DataFrame with Date column that should be unique
FORMAT: Python code that counts and optionally shows duplicate dates
CONSTRAINTS: Use duplicated(), show count and actual duplicate rows if any
```

**Expected Output**: `df['Date'].duplicated().sum()`

---

### Prompt 7.3: Data Type Verification
```
TASK: Verify that all columns have correct data types
CONTEXT: Stock DataFrame where Date should be datetime, prices should be float
FORMAT: Python code showing current data types and how to convert if needed
CONSTRAINTS: Use dtypes, show conversion examples with to_datetime() and astype()
```

**Expected Output**: Code checking `df.dtypes` and conversion methods

---

## Category 8: Multi-Stock Comparison Prompts

### Prompt 8.1: Load Multiple Stocks
```
TASK: Load stock data for multiple tickers (AAPL, GOOGL, MSFT) into separate DataFrames
CONTEXT: CSV files named like 'AAPL_5y.csv' in the datasets folder
FORMAT: Python code using loop or dictionary
CONSTRAINTS: Store in dictionary with ticker as key, handle file not found errors
```

**Expected Output**: Loop creating dictionary of DataFrames

---

### Prompt 8.2: Create Comparison Table
```
TASK: Create a comparison table showing key statistics for multiple stocks
CONTEXT: Dictionary of stock DataFrames (multiple tickers)
FORMAT: Python code creating a summary DataFrame
CONSTRAINTS: For each stock show: avg price, min, max, volatility, avg volume
```

**Expected Output**: Loop creating list of dicts, converted to DataFrame

---

### Prompt 8.3: Calculate Relative Returns
```
TASK: Compare total percentage returns for multiple stocks over same period
CONTEXT: Multiple stock DataFrames covering same date range
FORMAT: Python code creating sorted comparison table
CONSTRAINTS: Calculate (end_price - start_price) / start_price * 100 for each
```

**Expected Output**: Return calculation and comparison table

---

## Category 9: Advanced Operations Prompts

### Prompt 9.1: Correlation Analysis
```
TASK: Calculate correlation between price and volume
CONTEXT: Stock DataFrame with Adj Close and Volume columns
FORMAT: Python code showing correlation coefficient
CONSTRAINTS: Use corr() method, explain what the result means
```

**Expected Output**: `df[['Adj Close', 'Volume']].corr()`

---

### Prompt 9.2: Streaks Analysis
```
TASK: Find the longest streak of consecutive days with price increases
CONTEXT: Stock DataFrame with daily prices
FORMAT: Python code that calculates and displays longest winning streak
CONSTRAINTS: Compare each day to previous day, count consecutive gains
```

**Expected Output**: Code using diff(), comparison, and streak counting logic

---

### Prompt 9.3: Percentile Analysis
```
TASK: Find which days had closing prices in the top 10% of all prices
CONTEXT: Stock DataFrame with Adj Close column
FORMAT: Python code filtering and showing these days
CONSTRAINTS: Use quantile(0.9) to find 90th percentile threshold
```

**Expected Output**: `df[df['Adj Close'] > df['Adj Close'].quantile(0.9)]`

---

## Category 10: Debugging Prompts

### Prompt 10.1: Fix KeyError
```
I got this error: KeyError: 'Adj Close'

Here's my code:
df = pd.read_csv('stock.csv')
print(df['Adj Close'])

What's wrong and how do I fix it?
```

**Expected Response**: Check column names with `df.columns`, likely has different spacing or capitalization

---

### Prompt 10.2: Fix Date Parsing
```
My dates are showing as strings instead of datetime. How do I convert them?

Current output: df['Date'] shows '2023-01-05' as object type

What code do I need?
```

**Expected Response**: `df['Date'] = pd.to_datetime(df['Date'])` or use `parse_dates` in `read_csv()`

---

### Prompt 10.3: Handle NaN in Calculations
```
I get NaN values when calculating daily returns. Is this normal?

Code: df['Return'] = df['Close'].pct_change()

First row shows NaN. Should I drop it?
```

**Expected Response**: NaN in first row is normal (no previous day), can use `fillna(0)` or `dropna()`

---

## Prompt Engineering Tips for Data Analysis

### 1. **Be Specific About Input**
❌ Bad: "Load stock data"
✅ Good: "Load stock data from CSV file with columns Date, Open, High, Low, Close, Volume"

### 2. **Specify Output Format**
❌ Bad: "Show me the statistics"
✅ Good: "Calculate and print mean, median, std dev for Adj Close in a formatted table"

### 3. **Include Context**
❌ Bad: "Filter the data"
✅ Good: "Filter stock DataFrame to show only days in 2023 where volume > 100M"

### 4. **Request Explanations**
❌ Bad: "Give me the code"
✅ Good: "Give me the code and explain what each line does"

### 5. **Iterate on Responses**
- Start simple: "Calculate daily returns"
- Then refine: "Add a column for 7-day moving average of returns"
- Then enhance: "Now compare this to the 30-day moving average"

### 6. **Ask for Multiple Approaches**
"Show me 3 different ways to filter data by date range in pandas"

### 7. **Request Best Practices**
"What's the most efficient way to calculate rolling statistics on large DataFrames?"

---

## Progressive Prompting Example

Here's how to build up from simple to complex:

**Level 1 - Basic**:
```
Load stock data from CSV file and show first 5 rows
```

**Level 2 - Add Details**:
```
Load stock data from CSV, parse dates, set Date as index, and show first 5 rows with summary statistics
```

**Level 3 - Add Calculations**:
```
Load stock data, parse dates, calculate daily returns and 50-day moving average, then show statistics for each column
```

**Level 4 - Add Analysis**:
```
Load stock data, calculate returns and moving averages, find days where price crossed above the 50-day MA, and calculate the average return on those days
```

---

## Verification Prompts

Use these to verify your understanding:

### Verification 1: Explain Code
```
Explain this code line by line:
df['MA_50'] = df['Adj Close'].rolling(window=50).mean()
```

### Verification 2: Predict Output
```
What will this code output if df has 100 rows?
print(df.tail(10).head(5))
```

### Verification 3: Find Issues
```
What's wrong with this code?
high_volume = df[df'Volume' > 100000000]
```

---

## Next Steps

1. Try each prompt in ChatGPT/Claude/Gemini
2. Compare outputs from different AI tools
3. Modify prompts to fit your specific needs
4. Build your personal prompt library
5. Practice iterative refinement

---

**Module**: Module 1: Foundations
**Course**: ML for Engineers
**Created**: 2026-01-05
**Version**: 1.0
