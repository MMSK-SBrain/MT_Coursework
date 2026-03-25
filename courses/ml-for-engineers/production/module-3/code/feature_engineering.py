"""
Feature Engineering Library for Stock Prediction
ML for Engineers - Module 3: Regression

This library provides functions to calculate technical indicators
for stock price prediction using machine learning.

Created: 2026-01-05
"""

import pandas as pd
import numpy as np


def calculate_moving_average(data, column='Close', window=10):
    """
    Calculate Simple Moving Average (SMA)

    Parameters:
    -----------
    data : pd.DataFrame
        Stock price data
    column : str
        Column name to calculate MA on (default: 'Close')
    window : int
        Number of periods for moving average

    Returns:
    --------
    pd.Series
        Moving average values

    Example:
    --------
    >>> data['MA_10'] = calculate_moving_average(data, window=10)
    >>> data['MA_50'] = calculate_moving_average(data, window=50)
    """
    return data[column].rolling(window=window).mean()


def calculate_exponential_moving_average(data, column='Close', span=12):
    """
    Calculate Exponential Moving Average (EMA)

    Parameters:
    -----------
    data : pd.DataFrame
        Stock price data
    column : str
        Column name to calculate EMA on
    span : int
        Span for exponential weighting

    Returns:
    --------
    pd.Series
        Exponential moving average values
    """
    return data[column].ewm(span=span, adjust=False).mean()


def calculate_rsi(data, column='Close', window=14):
    """
    Calculate Relative Strength Index (RSI)

    RSI measures momentum and indicates overbought/oversold conditions.
    - RSI > 70: Overbought (might go down)
    - RSI < 30: Oversold (might go up)

    Parameters:
    -----------
    data : pd.DataFrame
        Stock price data
    column : str
        Column name to calculate RSI on
    window : int
        Number of periods for RSI calculation (default: 14)

    Returns:
    --------
    pd.Series
        RSI values (0-100)

    Example:
    --------
    >>> data['RSI'] = calculate_rsi(data, window=14)
    """
    # Calculate price changes
    delta = data[column].diff()

    # Separate gains and losses
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    # Calculate average gain and loss
    avg_gain = gain.rolling(window=window).mean()
    avg_loss = loss.rolling(window=window).mean()

    # Calculate relative strength
    rs = avg_gain / avg_loss

    # Calculate RSI
    rsi = 100 - (100 / (1 + rs))

    return rsi


def calculate_macd(data, column='Close', fast=12, slow=26, signal=9):
    """
    Calculate MACD (Moving Average Convergence Divergence)

    MACD shows the relationship between two moving averages.
    - MACD > Signal: Bullish (upward momentum)
    - MACD < Signal: Bearish (downward momentum)

    Parameters:
    -----------
    data : pd.DataFrame
        Stock price data
    column : str
        Column name to calculate MACD on
    fast : int
        Fast EMA period (default: 12)
    slow : int
        Slow EMA period (default: 26)
    signal : int
        Signal line period (default: 9)

    Returns:
    --------
    dict
        Dictionary with 'macd', 'signal', and 'histogram' Series

    Example:
    --------
    >>> macd_data = calculate_macd(data)
    >>> data['MACD'] = macd_data['macd']
    >>> data['MACD_Signal'] = macd_data['signal']
    >>> data['MACD_Histogram'] = macd_data['histogram']
    """
    # Calculate fast and slow EMAs
    ema_fast = data[column].ewm(span=fast, adjust=False).mean()
    ema_slow = data[column].ewm(span=slow, adjust=False).mean()

    # Calculate MACD line
    macd_line = ema_fast - ema_slow

    # Calculate signal line
    signal_line = macd_line.ewm(span=signal, adjust=False).mean()

    # Calculate histogram
    histogram = macd_line - signal_line

    return {
        'macd': macd_line,
        'signal': signal_line,
        'histogram': histogram
    }


def calculate_bollinger_bands(data, column='Close', window=20, num_std=2):
    """
    Calculate Bollinger Bands

    Bollinger Bands show volatility and potential price boundaries.
    - Price near upper band: Potentially overbought
    - Price near lower band: Potentially oversold

    Parameters:
    -----------
    data : pd.DataFrame
        Stock price data
    column : str
        Column name to calculate bands on
    window : int
        Moving average period (default: 20)
    num_std : int
        Number of standard deviations (default: 2)

    Returns:
    --------
    dict
        Dictionary with 'middle', 'upper', and 'lower' band Series

    Example:
    --------
    >>> bb = calculate_bollinger_bands(data, window=20)
    >>> data['BB_Middle'] = bb['middle']
    >>> data['BB_Upper'] = bb['upper']
    >>> data['BB_Lower'] = bb['lower']
    """
    # Calculate middle band (SMA)
    middle_band = data[column].rolling(window=window).mean()

    # Calculate standard deviation
    std = data[column].rolling(window=window).std()

    # Calculate upper and lower bands
    upper_band = middle_band + (std * num_std)
    lower_band = middle_band - (std * num_std)

    return {
        'middle': middle_band,
        'upper': upper_band,
        'lower': lower_band
    }


def calculate_volatility(data, column='Close', window=10):
    """
    Calculate price volatility (rolling standard deviation of returns)

    Parameters:
    -----------
    data : pd.DataFrame
        Stock price data
    column : str
        Column name to calculate volatility on
    window : int
        Number of periods for rolling calculation

    Returns:
    --------
    pd.Series
        Volatility values

    Example:
    --------
    >>> data['Volatility_10'] = calculate_volatility(data, window=10)
    """
    returns = data[column].pct_change()
    volatility = returns.rolling(window=window).std()
    return volatility


def calculate_daily_returns(data, column='Close'):
    """
    Calculate daily percentage returns

    Parameters:
    -----------
    data : pd.DataFrame
        Stock price data
    column : str
        Column name to calculate returns on

    Returns:
    --------
    pd.Series
        Daily returns as percentages

    Example:
    --------
    >>> data['Returns'] = calculate_daily_returns(data)
    """
    return data[column].pct_change()


def calculate_rate_of_change(data, column='Close', window=10):
    """
    Calculate Rate of Change (ROC)

    ROC measures the percentage change over a period.

    Parameters:
    -----------
    data : pd.DataFrame
        Stock price data
    column : str
        Column name to calculate ROC on
    window : int
        Number of periods to look back

    Returns:
    --------
    pd.Series
        Rate of change values

    Example:
    --------
    >>> data['ROC_10'] = calculate_rate_of_change(data, window=10)
    """
    return ((data[column] - data[column].shift(window)) / data[column].shift(window)) * 100


def calculate_momentum(data, column='Close', window=10):
    """
    Calculate Momentum indicator

    Momentum is the difference between current price and price N periods ago.

    Parameters:
    -----------
    data : pd.DataFrame
        Stock price data
    column : str
        Column name to calculate momentum on
    window : int
        Number of periods to look back

    Returns:
    --------
    pd.Series
        Momentum values

    Example:
    --------
    >>> data['Momentum_10'] = calculate_momentum(data, window=10)
    """
    return data[column] - data[column].shift(window)


def calculate_volume_sma(data, column='Volume', window=10):
    """
    Calculate Simple Moving Average of Volume

    Parameters:
    -----------
    data : pd.DataFrame
        Stock price data
    column : str
        Volume column name
    window : int
        Number of periods for moving average

    Returns:
    --------
    pd.Series
        Volume moving average

    Example:
    --------
    >>> data['Volume_MA_10'] = calculate_volume_sma(data, window=10)
    """
    return data[column].rolling(window=window).mean()


def calculate_price_position(data, column='Close', window=20):
    """
    Calculate price position within range (0 = lowest, 1 = highest)

    This shows where the current price sits relative to recent high/low.

    Parameters:
    -----------
    data : pd.DataFrame
        Stock price data
    column : str
        Column name to calculate position for
    window : int
        Number of periods for range calculation

    Returns:
    --------
    pd.Series
        Price position (0-1)

    Example:
    --------
    >>> data['Price_Position'] = calculate_price_position(data, window=20)
    """
    rolling_min = data[column].rolling(window=window).min()
    rolling_max = data[column].rolling(window=window).max()

    position = (data[column] - rolling_min) / (rolling_max - rolling_min)

    return position


def add_all_features(data, windows=[10, 20, 50]):
    """
    Add all technical indicators to dataset at once

    This is a convenience function that adds all major technical indicators
    with common parameter values. Great for quick feature engineering!

    Parameters:
    -----------
    data : pd.DataFrame
        Stock price data (must have OHLCV columns)
    windows : list
        List of window sizes for moving averages

    Returns:
    --------
    pd.DataFrame
        Data with all features added

    Features Added:
    ---------------
    - Moving averages (multiple windows)
    - RSI
    - MACD (all components)
    - Bollinger Bands (all components)
    - Volatility
    - Daily returns
    - Rate of change
    - Momentum
    - Volume MA
    - Price position

    Example:
    --------
    >>> # Load stock data
    >>> import yfinance as yf
    >>> data = yf.download('AAPL', start='2020-01-01', end='2024-01-01')
    >>>
    >>> # Add all features at once
    >>> data = add_all_features(data)
    >>>
    >>> # Check the new features
    >>> print(data.columns.tolist())
    """
    # Make a copy to avoid modifying original
    df = data.copy()

    print("Adding technical indicators...")

    # 1. Moving Averages
    for window in windows:
        df[f'MA_{window}'] = calculate_moving_average(df, window=window)
        print(f"  - Added MA_{window}")

    # 2. RSI
    df['RSI'] = calculate_rsi(df, window=14)
    print("  - Added RSI")

    # 3. MACD
    macd_data = calculate_macd(df)
    df['MACD'] = macd_data['macd']
    df['MACD_Signal'] = macd_data['signal']
    df['MACD_Histogram'] = macd_data['histogram']
    print("  - Added MACD (with signal and histogram)")

    # 4. Bollinger Bands
    bb = calculate_bollinger_bands(df, window=20)
    df['BB_Middle'] = bb['middle']
    df['BB_Upper'] = bb['upper']
    df['BB_Lower'] = bb['lower']
    print("  - Added Bollinger Bands")

    # 5. Volatility
    df['Volatility_10'] = calculate_volatility(df, window=10)
    df['Volatility_30'] = calculate_volatility(df, window=30)
    print("  - Added Volatility (10 and 30 day)")

    # 6. Returns
    df['Returns'] = calculate_daily_returns(df)
    print("  - Added Daily Returns")

    # 7. Rate of Change
    df['ROC_10'] = calculate_rate_of_change(df, window=10)
    print("  - Added Rate of Change (10 day)")

    # 8. Momentum
    df['Momentum_10'] = calculate_momentum(df, window=10)
    print("  - Added Momentum (10 day)")

    # 9. Volume indicators
    df['Volume_MA_10'] = calculate_volume_sma(df, window=10)
    print("  - Added Volume MA (10 day)")

    # 10. Price Position
    df['Price_Position_20'] = calculate_price_position(df, window=20)
    print("  - Added Price Position (20 day)")

    print(f"\nTotal features added: {len(df.columns) - len(data.columns)}")
    print(f"Original columns: {len(data.columns)}")
    print(f"New columns: {len(df.columns)}")

    return df


def prepare_regression_data(data, target_column='Close', drop_na=True):
    """
    Prepare data for regression modeling

    Creates target variable (next day's price) and separates features.

    Parameters:
    -----------
    data : pd.DataFrame
        Stock data with technical indicators
    target_column : str
        Column to predict (default: 'Close')
    drop_na : bool
        Whether to drop NaN values (default: True)

    Returns:
    --------
    tuple
        (X, y) where X is features DataFrame and y is target Series

    Example:
    --------
    >>> # After adding features
    >>> X, y = prepare_regression_data(data)
    >>> print(f"Features shape: {X.shape}")
    >>> print(f"Target shape: {y.shape}")
    """
    df = data.copy()

    # Create target: Tomorrow's closing price
    df['Target'] = df[target_column].shift(-1)

    # Drop the last row (no target available)
    df = df[:-1]

    # Drop NaN values if requested
    if drop_na:
        df = df.dropna()

    # Separate features and target
    # Exclude the target and the original close price
    feature_cols = [col for col in df.columns if col not in ['Target', target_column]]

    X = df[feature_cols]
    y = df['Target']

    return X, y


def time_series_split(X, y, train_size=0.8):
    """
    Split time series data for training and testing

    IMPORTANT: For time series, we don't shuffle!
    Train on old data, test on recent data.

    Parameters:
    -----------
    X : pd.DataFrame
        Features
    y : pd.Series
        Target variable
    train_size : float
        Proportion of data for training (default: 0.8)

    Returns:
    --------
    tuple
        (X_train, X_test, y_train, y_test)

    Example:
    --------
    >>> X_train, X_test, y_train, y_test = time_series_split(X, y, train_size=0.8)
    >>> print(f"Training: {X_train.index[0]} to {X_train.index[-1]}")
    >>> print(f"Testing: {X_test.index[0]} to {X_test.index[-1]}")
    """
    # Calculate split point
    split_idx = int(len(X) * train_size)

    # Split without shuffling
    X_train = X.iloc[:split_idx]
    X_test = X.iloc[split_idx:]
    y_train = y.iloc[:split_idx]
    y_test = y.iloc[split_idx:]

    print(f"Train set: {len(X_train)} samples ({X_train.index[0]} to {X_train.index[-1]})")
    print(f"Test set: {len(X_test)} samples ({X_test.index[0]} to {X_test.index[-1]})")

    return X_train, X_test, y_train, y_test


# Quick reference guide
INDICATOR_REFERENCE = {
    'Moving Average (MA)': 'Smooths price data to identify trends. Higher MA = longer-term trend.',
    'RSI': 'Momentum oscillator (0-100). >70 = overbought, <30 = oversold.',
    'MACD': 'Trend-following momentum. MACD > Signal = bullish, < Signal = bearish.',
    'Bollinger Bands': 'Volatility bands. Price near upper = overbought, near lower = oversold.',
    'Volatility': 'Measures price fluctuation. Higher = more risk/opportunity.',
    'Returns': 'Daily percentage price change.',
    'ROC': 'Rate of change over N periods.',
    'Momentum': 'Difference between current and past price.',
    'Volume MA': 'Average trading volume. Higher = more activity.',
    'Price Position': 'Where price sits in recent range (0 = low, 1 = high).'
}


if __name__ == "__main__":
    print("Feature Engineering Library for Stock Prediction")
    print("=" * 60)
    print("\nAvailable Functions:")
    print("  - calculate_moving_average()")
    print("  - calculate_rsi()")
    print("  - calculate_macd()")
    print("  - calculate_bollinger_bands()")
    print("  - calculate_volatility()")
    print("  - calculate_daily_returns()")
    print("  - calculate_rate_of_change()")
    print("  - calculate_momentum()")
    print("  - add_all_features()  <- Use this for quick setup!")
    print("  - prepare_regression_data()")
    print("  - time_series_split()")
    print("\nFor detailed usage, see: feature-engineering-guide.ipynb")
