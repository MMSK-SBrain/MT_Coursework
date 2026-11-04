# Stock Data Download Instructions
## Module 1: Foundations - ML for Engineers

---

## Overview

For Module 1, you'll need historical stock price data for **7 stocks**:

### US Stocks:
- **AAPL** - Apple Inc.
- **GOOGL** - Alphabet Inc. (Google)
- **TSLA** - Tesla Inc.
- **MSFT** - Microsoft Corporation

### Indian Stocks:
- **INFY.NS** - Infosys Limited
- **TCS.NS** - Tata Consultancy Services
- **RELIANCE.NS** - Reliance Industries Limited

**Data Format:** OHLCV (Open, High, Low, Close, Volume, Adjusted Close)
**Date Range:** 5 years of historical data
**Source:** Yahoo Finance

---

## Method 1: Using the Automated Script (Recommended)

### Prerequisites

1. **Python 3.7 or higher** installed
2. **Required libraries:**
   ```bash
   pip install yfinance pandas
   ```

### Steps

1. **Navigate to the datasets directory:**
   ```bash
   cd production/module-1/datasets/
   ```

2. **Run the download script:**
   ```bash
   python download_stock_data.py
   ```

3. **Expected output:**
   - 7 CSV files (one per stock)
   - `dataset_summary.csv` with overview statistics
   - Console output showing download progress

4. **Verify downloads:**
   - Each CSV should have ~1,250 rows (5 years of trading days)
   - Columns: Date, Open, High, Low, Close, Volume, Adj Close

---

## Method 2: Manual Download via Python/Jupyter

If the automated script doesn't work, you can download data manually using this code:

### In Jupyter Notebook or Python Script:

```python
import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

# Configuration
tickers = ['AAPL', 'GOOGL', 'TSLA', 'MSFT', 'INFY.NS', 'TCS.NS', 'RELIANCE.NS']
end_date = datetime.now()
start_date = end_date - timedelta(days=5*365)

# Download each stock
for ticker in tickers:
    print(f"Downloading {ticker}...")
    data = yf.download(ticker, start=start_date, end=end_date)

    # Save to CSV
    filename = f"{ticker.replace('.', '_')}_5y.csv"
    data.to_csv(filename)
    print(f"Saved {filename} - {len(data)} days of data")

print("All downloads complete!")
```

---

## Method 3: Using Google Colab (Cloud-based, No Installation)

1. **Open Google Colab:** https://colab.research.google.com/

2. **Create a new notebook**

3. **Install yfinance:**
   ```python
   !pip install yfinance
   ```

4. **Run the download code** (from Method 2)

5. **Download files to your computer:**
   ```python
   from google.colab import files

   # Download each CSV
   files.download('AAPL_5y.csv')
   files.download('GOOGL_5y.csv')
   # ... repeat for all stocks
   ```

---

## Method 4: Direct from Yahoo Finance Website

If Python isn't working, you can manually download from Yahoo Finance:

1. Go to: https://finance.yahoo.com/
2. Search for stock ticker (e.g., "AAPL")
3. Click "Historical Data" tab
4. Set date range: 5 years
5. Click "Download" button
6. Save as: `AAPL_5y.csv`
7. Repeat for all 7 stocks

**Note:** For Indian stocks, use full ticker symbol:
- INFY.NS
- TCS.NS
- RELIANCE.NS

---

## Data Structure

Each CSV file will have the following columns:

| Column | Description | Example |
|--------|-------------|---------|
| **Date** | Trading date | 2019-01-05 |
| **Open** | Opening price of the day | $150.25 |
| **High** | Highest price during the day | $152.80 |
| **Low** | Lowest price during the day | $149.50 |
| **Close** | Closing price of the day | $151.75 |
| **Adj Close** | Adjusted closing price (accounts for splits, dividends) | $151.75 |
| **Volume** | Number of shares traded | 35,250,000 |

---

## Expected File Sizes

| Stock | Approximate Rows | File Size |
|-------|-----------------|-----------|
| AAPL | ~1,250 | ~120 KB |
| GOOGL | ~1,250 | ~120 KB |
| TSLA | ~1,250 | ~120 KB |
| MSFT | ~1,250 | ~120 KB |
| INFY.NS | ~1,250 | ~120 KB |
| TCS.NS | ~1,250 | ~120 KB |
| RELIANCE.NS | ~1,250 | ~120 KB |

**Total Size:** ~850 KB (all 7 files)

---

## Verification Checklist

After downloading, verify your data:

- [ ] All 7 CSV files are present
- [ ] Each file has 6-7 columns (Date, Open, High, Low, Close, Volume, Adj Close)
- [ ] Each file has ~1,250 rows (5 years ≈ 1,260 trading days)
- [ ] No missing dates (check with `data.isnull().sum()`)
- [ ] Date range spans approximately 5 years
- [ ] Files can be loaded with pandas: `pd.read_csv('AAPL_5y.csv')`

### Quick Verification Code:

```python
import pandas as pd

# Check one file
data = pd.read_csv('AAPL_5y.csv')
print(f"Rows: {len(data)}")
print(f"Columns: {list(data.columns)}")
print(f"Date range: {data['Date'].iloc[0]} to {data['Date'].iloc[-1]}")
print(f"Missing values: {data.isnull().sum().sum()}")
```

---

## Troubleshooting

### Problem: "Module 'yfinance' not found"
**Solution:** Install yfinance: `pip install yfinance`

### Problem: "No data downloaded for ticker"
**Solution:**
- Check internet connection
- Verify ticker symbol is correct
- Try downloading just one stock first
- For Indian stocks, make sure to include `.NS` suffix

### Problem: "Permission denied" when saving files
**Solution:**
- Check you have write permissions in the directory
- Run script from a directory you own
- Try saving to a different directory

### Problem: "SSL Certificate Error"
**Solution:**
- Update Python: `pip install --upgrade certifi`
- Or use Method 4 (manual download)

### Problem: Data seems incomplete or incorrect
**Solution:**
- Re-download the data
- Check Yahoo Finance website to verify data availability
- Some stocks may have splits/dividends affecting historical data

---

## Data Quality Notes

### Trading Days vs Calendar Days
- Stock markets are closed on weekends and holidays
- 5 years ≈ 1,260 trading days (not 1,825 calendar days)
- Expect some gaps in dates (normal)

### Indian Market Hours
- Indian stocks (NSE) trade Monday-Friday
- Different holidays than US markets
- Data will reflect Indian time zone

### Adjusted Close Price
- **Use 'Adj Close' for analysis** (not 'Close')
- Accounts for stock splits and dividends
- Gives accurate historical returns

---

## Alternative Data Sources

If Yahoo Finance doesn't work, try these alternatives:

1. **Alpha Vantage** (requires free API key)
   - https://www.alphavantage.co/
   - 500 requests/day (free tier)

2. **Quandl** (requires account)
   - https://www.quandl.com/
   - Large financial dataset repository

3. **pandas_datareader** (uses multiple sources)
   ```python
   from pandas_datareader import data as pdr
   import yfinance as yf
   yf.pdr_override()

   data = pdr.get_data_yahoo('AAPL', start='2019-01-01', end='2024-01-01')
   ```

---

## License & Usage

**Data Source:** Yahoo Finance
**Terms of Use:** Educational and personal use
**Commercial Use:** Check Yahoo Finance Terms of Service

**Note:** This data is provided for educational purposes in the ML for Engineers course. Always verify data accuracy before making investment decisions.

---

## Support

**Issues with downloads?**
- Check the troubleshooting section above
- Verify your Python version: `python --version` (should be 3.7+)
- Post questions in the course forum
- Email instructor: [course-support@example.com]

---

**Last Updated:** 2026-01-05
**Course:** ML for Engineers - Module 1: Foundations
**Version:** 1.0
