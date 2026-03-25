"""
Stock Data Downloader for Module 1: Foundations
================================================

This script downloads 5 years of historical stock data for the following stocks:
- US Stocks: AAPL, GOOGL, TSLA, MSFT
- Indian Stocks: INFY.NS, TCS.NS, RELIANCE.NS

Data Format: OHLCV (Open, High, Low, Close, Volume)
Data Source: Yahoo Finance via yfinance library
Date Range: 5 years from today

Requirements:
- yfinance library: pip install yfinance
- pandas library: pip install pandas

Usage:
    python download_stock_data.py

Output:
    CSV files for each stock in the current directory
"""

import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import os

# Configuration
TICKERS = {
    'US_Stocks': ['AAPL', 'GOOGL', 'TSLA', 'MSFT'],
    'Indian_Stocks': ['INFY.NS', 'TCS.NS', 'RELIANCE.NS']
}

# Date range: 5 years
END_DATE = datetime.now()
START_DATE = END_DATE - timedelta(days=5*365)

# Output directory
OUTPUT_DIR = '.'

def download_stock_data(ticker, start_date, end_date):
    """
    Download historical stock data for a given ticker.

    Parameters:
    -----------
    ticker : str
        Stock ticker symbol (e.g., 'AAPL', 'INFY.NS')
    start_date : datetime
        Start date for historical data
    end_date : datetime
        End date for historical data

    Returns:
    --------
    pandas.DataFrame
        DataFrame containing OHLCV data
    """
    try:
        print(f"Downloading {ticker}...")
        data = yf.download(ticker, start=start_date, end=end_date, progress=False)

        if data.empty:
            print(f"  ⚠️  WARNING: No data retrieved for {ticker}")
            return None

        print(f"  ✓ Downloaded {len(data)} days of data for {ticker}")
        return data

    except Exception as e:
        print(f"  ✗ ERROR downloading {ticker}: {str(e)}")
        return None

def save_to_csv(data, ticker, output_dir):
    """
    Save stock data to CSV file.

    Parameters:
    -----------
    data : pandas.DataFrame
        Stock data to save
    ticker : str
        Stock ticker symbol
    output_dir : str
        Directory to save CSV file
    """
    if data is None or data.empty:
        return False

    # Clean ticker name for filename (replace . with _)
    clean_ticker = ticker.replace('.', '_')
    filename = f"{clean_ticker}_5y.csv"
    filepath = os.path.join(output_dir, filename)

    try:
        data.to_csv(filepath)
        print(f"  ✓ Saved to {filename}")
        return True
    except Exception as e:
        print(f"  ✗ ERROR saving {ticker}: {str(e)}")
        return False

def generate_summary_report(all_data):
    """
    Generate summary statistics for all downloaded datasets.

    Parameters:
    -----------
    all_data : dict
        Dictionary of ticker: DataFrame pairs

    Returns:
    --------
    pandas.DataFrame
        Summary statistics for all stocks
    """
    summary_data = []

    for ticker, data in all_data.items():
        if data is not None and not data.empty:
            summary = {
                'Ticker': ticker,
                'Start_Date': data.index[0].strftime('%Y-%m-%d'),
                'End_Date': data.index[-1].strftime('%Y-%m-%d'),
                'Total_Days': len(data),
                'Avg_Close': f"${data['Close'].mean():.2f}",
                'Min_Close': f"${data['Close'].min():.2f}",
                'Max_Close': f"${data['Close'].max():.2f}",
                'Avg_Volume': f"{data['Volume'].mean():,.0f}",
                'Missing_Values': data.isnull().sum().sum()
            }
            summary_data.append(summary)

    return pd.DataFrame(summary_data)

def main():
    """
    Main function to download all stock data.
    """
    print("="*70)
    print("Stock Data Downloader - Module 1: Foundations")
    print("="*70)
    print(f"Date Range: {START_DATE.strftime('%Y-%m-%d')} to {END_DATE.strftime('%Y-%m-%d')}")
    print(f"Output Directory: {os.path.abspath(OUTPUT_DIR)}")
    print("="*70)
    print()

    all_data = {}
    successful = 0
    failed = 0

    # Download US stocks
    print("📈 Downloading US Stocks...")
    print("-" * 70)
    for ticker in TICKERS['US_Stocks']:
        data = download_stock_data(ticker, START_DATE, END_DATE)
        if save_to_csv(data, ticker, OUTPUT_DIR):
            all_data[ticker] = data
            successful += 1
        else:
            failed += 1
        print()

    # Download Indian stocks
    print("📊 Downloading Indian Stocks...")
    print("-" * 70)
    for ticker in TICKERS['Indian_Stocks']:
        data = download_stock_data(ticker, START_DATE, END_DATE)
        if save_to_csv(data, ticker, OUTPUT_DIR):
            all_data[ticker] = data
            successful += 1
        else:
            failed += 1
        print()

    # Generate summary report
    print("="*70)
    print("📋 Summary Report")
    print("="*70)
    print(f"Successfully downloaded: {successful} stocks")
    print(f"Failed: {failed} stocks")
    print()

    if all_data:
        summary_df = generate_summary_report(all_data)
        print(summary_df.to_string(index=False))

        # Save summary to CSV
        summary_filepath = os.path.join(OUTPUT_DIR, 'dataset_summary.csv')
        summary_df.to_csv(summary_filepath, index=False)
        print()
        print(f"✓ Summary saved to: dataset_summary.csv")

    print()
    print("="*70)
    print("✓ Download complete!")
    print("="*70)

if __name__ == "__main__":
    main()
