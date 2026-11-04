# Stock Price Dataset - Data Dictionary
## Module 1: Foundations - ML for Engineers

---

## Dataset Overview

This dataset collection contains **5 years of historical stock price data** for 7 publicly traded companies across US and Indian stock markets.

**Purpose:** Educational use for learning data exploration, visualization, and machine learning fundamentals

**Date Range:** Approximately 5 years (varies by download date)

**Update Frequency:** Historical data (static for course purposes)

**Format:** CSV (Comma-Separated Values)

---

## Stock List

### US Stocks (NYSE/NASDAQ)

| Ticker | Company Name | Sector | Exchange | Currency |
|--------|--------------|--------|----------|----------|
| **AAPL** | Apple Inc. | Technology | NASDAQ | USD |
| **GOOGL** | Alphabet Inc. (Google) | Technology | NASDAQ | USD |
| **TSLA** | Tesla Inc. | Automotive/Energy | NASDAQ | USD |
| **MSFT** | Microsoft Corporation | Technology | NASDAQ | USD |

### Indian Stocks (NSE - National Stock Exchange)

| Ticker | Company Name | Sector | Exchange | Currency |
|--------|--------------|--------|----------|----------|
| **INFY.NS** | Infosys Limited | IT Services | NSE | INR |
| **TCS.NS** | Tata Consultancy Services | IT Services | NSE | INR |
| **RELIANCE.NS** | Reliance Industries | Conglomerate | NSE | INR |

**Note:** `.NS` suffix indicates National Stock Exchange of India

---

## File Structure

### File Naming Convention
```
{TICKER}_5y.csv
```

**Examples:**
- `AAPL_5y.csv`
- `INFY_NS_5y.csv` (note: `.` replaced with `_`)

### File Count
- **Total Files:** 7 CSV files
- **Total Size:** ~850 KB (compressed: ~200 KB)

---

## Column Definitions

Each CSV file contains the following columns:

### 1. Date
- **Type:** Date (YYYY-MM-DD format)
- **Description:** Trading date
- **Example:** `2024-01-05`
- **Notes:**
  - Only trading days included (no weekends/holidays)
  - US and Indian markets have different holiday schedules
  - Set as index in pandas by default

### 2. Open
- **Type:** Float (decimal number)
- **Description:** Stock price at market open
- **Unit:** Currency (USD or INR)
- **Example:** `150.25`
- **Notes:**
  - Price at 9:30 AM EST (US markets)
  - Price at 9:15 AM IST (Indian markets)
  - First price of the trading day

### 3. High
- **Type:** Float (decimal number)
- **Description:** Highest price reached during the trading day
- **Unit:** Currency (USD or INR)
- **Example:** `152.80`
- **Notes:**
  - Intraday high
  - Always >= Open, Low, Close

### 4. Low
- **Type:** Float (decimal number)
- **Description:** Lowest price reached during the trading day
- **Unit:** Currency (USD or INR)
- **Example:** `149.50`
- **Notes:**
  - Intraday low
  - Always <= Open, High, Close

### 5. Close
- **Type:** Float (decimal number)
- **Description:** Stock price at market close
- **Unit:** Currency (USD or INR)
- **Example:** `151.75`
- **Notes:**
  - Price at 4:00 PM EST (US markets)
  - Price at 3:30 PM IST (Indian markets)
  - Last price of the trading day
  - **⚠️ Use 'Adj Close' for analysis, not this column**

### 6. Adj Close (Adjusted Close)
- **Type:** Float (decimal number)
- **Description:** Closing price adjusted for splits and dividends
- **Unit:** Currency (USD or INR)
- **Example:** `151.75`
- **Notes:**
  - **RECOMMENDED COLUMN FOR PRICE ANALYSIS**
  - Accounts for:
    - Stock splits (e.g., 2-for-1 split)
    - Dividend payments
    - Corporate actions
  - Provides accurate historical returns
  - If no splits/dividends, equals 'Close'

### 7. Volume
- **Type:** Integer (whole number)
- **Description:** Number of shares traded during the day
- **Unit:** Shares
- **Example:** `35250000` (35.25 million shares)
- **Notes:**
  - Indicates trading activity/liquidity
  - High volume = High interest/volatility
  - Low volume = Less trading activity

---

## Data Characteristics

### Temporal Coverage

| Characteristic | Value |
|----------------|-------|
| **Time Span** | ~5 years (1,825 calendar days) |
| **Trading Days** | ~1,250 rows per file |
| **Frequency** | Daily (business days only) |
| **Gaps** | Weekends and market holidays |

### Statistical Properties

**Typical Statistics (Example: AAPL)**

| Metric | Approximate Range |
|--------|------------------|
| Mean Price | $120 - $180 |
| Std Deviation | $20 - $40 |
| Min Price | $80 - $120 |
| Max Price | $180 - $200 |
| Mean Volume | 50M - 100M shares |

**Note:** Actual values vary by stock and time period

---

## Data Quality

### Completeness

| Quality Metric | Expected Value | Notes |
|----------------|----------------|-------|
| **Missing Values** | 0 (ideally) | Yahoo Finance data is generally clean |
| **Duplicate Dates** | 0 | Each date should appear once |
| **Date Gaps** | Yes (normal) | Weekends, holidays |
| **Outliers** | Possible | Stock splits, major news events |

### Known Issues

1. **Stock Splits:** Historical prices adjusted retrospectively
2. **Dividends:** Accounted for in 'Adj Close'
3. **Market Holidays:** Different for US vs Indian markets
4. **Currency:** Mixed (USD for US stocks, INR for Indian stocks)
5. **Trading Hours:** Different time zones

---

## Usage Examples

### Loading Data (Python/Pandas)

```python
import pandas as pd

# Load single stock
df = pd.read_csv('AAPL_5y.csv', index_col='Date', parse_dates=True)

# View first few rows
print(df.head())

# Basic info
print(df.info())

# Summary statistics
print(df.describe())
```

### Accessing Columns

```python
# Get closing prices
closing_prices = df['Adj Close']

# Get volume
volume = df['Volume']

# Get specific date range
recent_data = df['2023-01-01':'2023-12-31']
```

### Common Calculations

```python
# Daily returns (percentage change)
df['Daily_Return'] = df['Adj Close'].pct_change()

# Moving average (50 days)
df['MA_50'] = df['Adj Close'].rolling(window=50).mean()

# Price range (High - Low)
df['Range'] = df['High'] - df['Low']

# Average price
df['Average_Price'] = (df['High'] + df['Low']) / 2
```

---

## Suggested Features for ML

### Price-Based Features
- `Adj Close` - Adjusted closing price ⭐ PRIMARY
- `Daily Return` - Percentage change from previous day
- `Volatility` - Rolling standard deviation
- `Price Range` - High - Low

### Volume-Based Features
- `Volume` - Trading volume
- `Volume Change` - % change in volume
- `Volume MA` - Moving average of volume

### Technical Indicators
- `Moving Average` (MA) - 10, 20, 50, 200 days
- `RSI` - Relative Strength Index
- `MACD` - Moving Average Convergence Divergence
- `Bollinger Bands` - Price volatility bands

**Note:** Technical indicators covered in Module 3

---

## Important Considerations

### For Analysis

1. **Always use 'Adj Close' for price analysis**
   - Accounts for splits and dividends
   - Provides accurate historical performance

2. **Different currencies**
   - US stocks: USD
   - Indian stocks: INR
   - Don't directly compare absolute prices

3. **Different market hours**
   - US: 9:30 AM - 4:00 PM EST
   - India: 9:15 AM - 3:30 PM IST
   - Time zone differences matter for news events

4. **Trading days vary**
   - US and Indian holidays are different
   - Expect different gap patterns

### For Machine Learning

1. **Time-based split required**
   - Don't use random train/test split
   - Use chronological split (e.g., first 4 years = train, last year = test)

2. **Avoid data leakage**
   - Don't use future data to predict past
   - Be careful with moving averages at edges

3. **Stationarity concerns**
   - Stock prices are non-stationary
   - Consider using returns instead of prices

4. **Feature scaling**
   - Different stocks have different price ranges
   - Normalize/standardize for multi-stock models

---

## Data Lineage

**Original Source:** Yahoo Finance (https://finance.yahoo.com/)

**Collection Method:** yfinance Python library

**Collection Date:** Varies (downloaded by learner)

**Updates:** Not updated (static historical data for course)

**Transformations:**
- Downloaded as-is from Yahoo Finance
- Saved to CSV format
- No additional cleaning/processing

---

## Licensing & Attribution

**Data Provider:** Yahoo Finance

**Terms of Use:**
- Educational and personal use permitted
- Commercial use requires verification of Yahoo Finance ToS
- No warranty on data accuracy
- Not intended for actual trading decisions

**Attribution:**
- Data sourced from Yahoo Finance via yfinance library
- Course: ML for Engineers
- Module 1: Foundations

---

## Support & Documentation

**Questions about the data?**
- Review download-instructions.md
- Check Yahoo Finance website for stock information
- Consult course materials for usage examples

**Data quality issues?**
- Verify download completed successfully
- Re-download from Yahoo Finance
- Check for recent stock splits or corporate actions

**Technical issues?**
- Ensure pandas is installed: `pip install pandas`
- Verify CSV file is not corrupted
- Check file encoding (should be UTF-8)

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-01-05 | Initial dataset creation |

---

## Quick Reference Card

### Load Data
```python
import pandas as pd
df = pd.read_csv('AAPL_5y.csv', index_col='Date', parse_dates=True)
```

### Key Columns
- **Adj Close** ← Use this for price analysis
- **Volume** ← Use this for activity analysis
- **Date** ← Index (time series)

### Common Operations
```python
df.head()           # First 5 rows
df.describe()       # Statistics
df.info()           # Structure
df['Adj Close']     # Get column
df['2023']          # Filter year
```

### Data Quality Checks
```python
df.isnull().sum()       # Missing values
df.duplicated().sum()   # Duplicates
df['Adj Close'].plot()  # Visual check
```

---

**Last Updated:** 2026-01-05
**Module:** Module 1: Foundations
**Course:** ML for Engineers
