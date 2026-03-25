"""
Sample Stock Data Generator (Fallback)
========================================

This script generates realistic sample stock data if you can't download from Yahoo Finance.
The data mimics real stock price patterns but is synthetically generated.

WARNING: This is for educational/testing purposes only. Use real data when possible.
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_stock_data(ticker, start_price, volatility, trend, num_days=1260):
    """
    Generate realistic stock price data using geometric Brownian motion.

    Parameters:
    -----------
    ticker : str
        Stock ticker symbol
    start_price : float
        Starting price
    volatility : float
        Daily volatility (0.01 = 1% daily std dev)
    trend : float
        Annual trend (0.10 = 10% annual growth)
    num_days : int
        Number of trading days to generate (default 1260 = ~5 years)

    Returns:
    --------
    pandas.DataFrame with OHLCV data
    """

    # Generate dates (trading days only - exclude weekends)
    end_date = datetime.now()
    start_date = end_date - timedelta(days=int(num_days * 1.4))  # Extra days for weekends

    date_range = pd.bdate_range(start=start_date, end=end_date)
    dates = date_range[-num_days:]  # Take last num_days trading days

    # Geometric Brownian Motion for prices
    np.random.seed(hash(ticker) % 2**32)  # Seed based on ticker for reproducibility

    daily_drift = trend / 252  # Convert annual to daily
    daily_vol = volatility

    # Generate random returns
    returns = np.random.normal(daily_drift, daily_vol, num_days)

    # Calculate cumulative prices
    price_multiplier = np.exp(np.cumsum(returns))
    close_prices = start_price * price_multiplier

    # Generate OHLC from close
    # High: close + random amount
    high_factor = np.random.uniform(1.0, 1.02, num_days)
    high_prices = close_prices * high_factor

    # Low: close - random amount
    low_factor = np.random.uniform(0.98, 1.0, num_days)
    low_prices = close_prices * low_factor

    # Open: between low and high
    open_prices = np.random.uniform(low_prices, high_prices)

    # Ensure OHLC consistency
    for i in range(num_days):
        high_prices[i] = max(open_prices[i], close_prices[i], high_prices[i])
        low_prices[i] = min(open_prices[i], close_prices[i], low_prices[i])

    # Volume: log-normal distribution
    avg_volume = {
        'AAPL': 70_000_000,
        'GOOGL': 25_000_000,
        'TSLA': 100_000_000,
        'MSFT': 30_000_000,
        'INFY.NS': 15_000_000,
        'TCS.NS': 3_000_000,
        'RELIANCE.NS': 10_000_000
    }.get(ticker, 50_000_000)

    volume = np.random.lognormal(np.log(avg_volume), 0.5, num_days).astype(int)

    # Create DataFrame
    df = pd.DataFrame({
        'Date': dates,
        'Open': np.round(open_prices, 2),
        'High': np.round(high_prices, 2),
        'Low': np.round(low_prices, 2),
        'Close': np.round(close_prices, 2),
        'Adj Close': np.round(close_prices, 2),  # Same as close for simplicity
        'Volume': volume
    })

    df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')

    return df


def main():
    """Generate sample data for all stocks."""

    stocks = {
        # ticker: (start_price, volatility, annual_trend)
        'AAPL': (150.0, 0.015, 0.15),      # $150, 1.5% daily vol, 15% annual growth
        'GOOGL': (135.0, 0.018, 0.12),     # $135, 1.8% daily vol, 12% annual growth
        'TSLA': (250.0, 0.030, 0.20),      # $250, 3.0% daily vol, 20% annual growth (volatile!)
        'MSFT': (320.0, 0.014, 0.14),      # $320, 1.4% daily vol, 14% annual growth
        'INFY.NS': (1500.0, 0.020, 0.10),  # ₹1500, 2.0% daily vol, 10% annual growth
        'TCS.NS': (3500.0, 0.018, 0.11),   # ₹3500, 1.8% daily vol, 11% annual growth
        'RELIANCE.NS': (2400.0, 0.022, 0.09)  # ₹2400, 2.2% daily vol, 9% annual growth
    }

    print("="*70)
    print("Sample Stock Data Generator")
    print("="*70)
    print("WARNING: This generates SYNTHETIC data for testing/education.")
    print("Use real data from Yahoo Finance when possible!")
    print("="*70)
    print()

    for ticker, (start_price, volatility, trend) in stocks.items():
        print(f"Generating {ticker}...")

        df = generate_stock_data(ticker, start_price, volatility, trend)

        # Save to CSV
        filename = f"{ticker.replace('.', '_')}_5y_SAMPLE.csv"
        df.to_csv(filename, index=False)

        print(f"  ✓ Created {filename}")
        print(f"    - Rows: {len(df)}")
        print(f"    - Date range: {df['Date'].iloc[0]} to {df['Date'].iloc[-1]}")
        print(f"    - Price range: ${df['Close'].min():.2f} - ${df['Close'].max():.2f}")
        print()

    print("="*70)
    print("✓ Sample data generation complete!")
    print("="*70)
    print()
    print("NOTE: These files are marked with '_SAMPLE' suffix.")
    print("Replace with real data from Yahoo Finance for production use.")


if __name__ == "__main__":
    main()
