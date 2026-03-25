"""
Stock Price Predictor - ML for Engineers Course Demo
Module 0: The Hook - Demo #1

This is a production-ready stock price prediction application using
Random Forest regression. Built to wow learners in their first session!

Features:
- Real-time stock data fetching
- Technical indicators calculation
- Price prediction with confidence
- Historical accuracy visualization
- Mobile-responsive interface

Author: ML for Engineers Course
License: MIT
"""

import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
import plotly.graph_objects as go
import plotly.express as px
import warnings
warnings.filterwarnings('ignore')

# Page configuration
st.set_page_config(
    page_title="Stock Price Predictor",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better UI
st.markdown("""
    <style>
    .main {
        padding: 0rem 1rem;
    }
    .stAlert {
        margin-top: 1rem;
    }
    h1 {
        color: #1E88E5;
        padding-bottom: 1rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# Title and introduction
st.title("📈 Stock Price Predictor")
st.markdown("""
Welcome to the **Stock Price Predictor**! This ML-powered app predicts stock prices using
historical data and technical indicators.

**How it works:** The app uses a Random Forest model trained on 1 year of historical data,
including features like moving averages, RSI, and volatility metrics.
""")

# Sidebar for user inputs
st.sidebar.header("🎯 Configuration")
st.sidebar.markdown("Select your stock and date range below:")

# Stock selection
AVAILABLE_STOCKS = {
    'AAPL': 'Apple Inc.',
    'GOOGL': 'Alphabet Inc.',
    'TSLA': 'Tesla Inc.',
    'MSFT': 'Microsoft Corporation',
    'AMZN': 'Amazon.com Inc.',
    'INFY': 'Infosys Limited',
    'TCS.NS': 'Tata Consultancy Services',
    'RELIANCE.NS': 'Reliance Industries'
}

selected_ticker = st.sidebar.selectbox(
    "Select Stock Ticker",
    options=list(AVAILABLE_STOCKS.keys()),
    format_func=lambda x: f"{x} - {AVAILABLE_STOCKS[x]}"
)

# Date range (using last 1 year for training)
st.sidebar.markdown("---")
st.sidebar.markdown("**Prediction Settings**")
prediction_days = st.sidebar.slider("Predict next N days", 1, 30, 5)

# Helper functions
@st.cache_data(ttl=3600)
def fetch_stock_data(ticker, period='1y'):
    """Fetch stock data from Yahoo Finance"""
    try:
        stock = yf.Ticker(ticker)
        df = stock.history(period=period)
        if df.empty:
            return None
        return df
    except Exception as e:
        st.error(f"Error fetching data: {str(e)}")
        return None

def calculate_technical_indicators(df):
    """Calculate technical indicators for ML features"""
    # Make a copy to avoid modifying original
    data = df.copy()

    # Moving Averages
    data['MA_10'] = data['Close'].rolling(window=10).mean()
    data['MA_20'] = data['Close'].rolling(window=20).mean()
    data['MA_50'] = data['Close'].rolling(window=50).mean()

    # Relative Strength Index (RSI)
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    data['RSI'] = 100 - (100 / (1 + rs))

    # Volatility (standard deviation of returns)
    data['Volatility'] = data['Close'].pct_change().rolling(window=10).std()

    # Price momentum
    data['Momentum'] = data['Close'] - data['Close'].shift(10)

    # Volume change
    data['Volume_Change'] = data['Volume'].pct_change()

    # Day of week (cyclical feature)
    data['DayOfWeek'] = pd.to_datetime(data.index).dayofweek

    # Drop NaN values
    data = data.dropna()

    return data

def prepare_features(df):
    """Prepare feature matrix and target variable"""
    features = ['Open', 'High', 'Low', 'Volume', 'MA_10', 'MA_20', 'MA_50',
                'RSI', 'Volatility', 'Momentum', 'Volume_Change', 'DayOfWeek']

    X = df[features]
    y = df['Close']

    return X, y

def train_model(X, y):
    """Train Random Forest model"""
    # Split data (80-20)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, shuffle=False
    )

    # Train Random Forest
    model = RandomForestRegressor(
        n_estimators=100,
        max_depth=10,
        random_state=42,
        n_jobs=-1
    )

    model.fit(X_train, y_train)

    # Calculate metrics
    train_pred = model.predict(X_train)
    test_pred = model.predict(X_test)

    train_mae = mean_absolute_error(y_train, train_pred)
    test_mae = mean_absolute_error(y_test, test_pred)
    train_r2 = r2_score(y_train, train_pred)
    test_r2 = r2_score(y_test, test_pred)

    return model, {
        'train_mae': train_mae,
        'test_mae': test_mae,
        'train_r2': train_r2,
        'test_r2': test_r2,
        'X_test': X_test,
        'y_test': y_test,
        'test_pred': test_pred
    }

def predict_future(model, df, days=5):
    """Predict future prices"""
    predictions = []
    last_row = df.iloc[-1:].copy()

    for i in range(days):
        # Prepare features
        features = ['Open', 'High', 'Low', 'Volume', 'MA_10', 'MA_20', 'MA_50',
                    'RSI', 'Volatility', 'Momentum', 'Volume_Change', 'DayOfWeek']

        X_pred = last_row[features]

        # Make prediction
        pred_price = model.predict(X_pred)[0]
        predictions.append(pred_price)

        # Update for next iteration (simplified - using predicted price)
        # In production, you'd want more sophisticated feature updates
        last_row['Close'] = pred_price
        last_row['Open'] = pred_price
        last_row['High'] = pred_price * 1.02
        last_row['Low'] = pred_price * 0.98

    return predictions

# Main application
if st.sidebar.button("🚀 Predict Stock Price", type="primary"):
    with st.spinner(f"Fetching data for {selected_ticker}..."):
        # Fetch data
        raw_data = fetch_stock_data(selected_ticker)

        if raw_data is not None and len(raw_data) > 60:
            # Calculate technical indicators
            data_with_features = calculate_technical_indicators(raw_data)

            # Prepare features
            X, y = prepare_features(data_with_features)

            # Train model
            with st.spinner("Training ML model..."):
                model, metrics = train_model(X, y)

            # Make predictions
            future_predictions = predict_future(model, data_with_features, prediction_days)

            # Display results
            st.success("✅ Prediction Complete!")

            # Create two columns for metrics
            col1, col2, col3, col4 = st.columns(4)

            current_price = raw_data['Close'].iloc[-1]
            predicted_price = future_predictions[-1]
            price_change = predicted_price - current_price
            price_change_pct = (price_change / current_price) * 100

            with col1:
                st.metric(
                    "Current Price",
                    f"${current_price:.2f}",
                    delta=None
                )

            with col2:
                st.metric(
                    f"Predicted Price (Day {prediction_days})",
                    f"${predicted_price:.2f}",
                    delta=f"{price_change_pct:+.2f}%"
                )

            with col3:
                direction = "📈 UP" if price_change > 0 else "📉 DOWN"
                st.metric(
                    "Direction",
                    direction,
                    delta=f"${price_change:+.2f}"
                )

            with col4:
                confidence = min(metrics['test_r2'] * 100, 99)
                st.metric(
                    "Model Confidence",
                    f"{confidence:.1f}%",
                    delta=None
                )

            # Historical accuracy section
            st.markdown("---")
            st.subheader("📊 Model Performance")

            perf_col1, perf_col2 = st.columns(2)

            with perf_col1:
                st.markdown("**Training Metrics:**")
                st.write(f"- R² Score: {metrics['train_r2']:.4f}")
                st.write(f"- Mean Absolute Error: ${metrics['train_mae']:.2f}")

            with perf_col2:
                st.markdown("**Testing Metrics:**")
                st.write(f"- R² Score: {metrics['test_r2']:.4f}")
                st.write(f"- Mean Absolute Error: ${metrics['test_mae']:.2f}")

            # Historical price chart with predictions
            st.markdown("---")
            st.subheader("📈 Price History & Predictions")

            # Create figure
            fig = go.Figure()

            # Historical prices
            fig.add_trace(go.Scatter(
                x=raw_data.index,
                y=raw_data['Close'],
                mode='lines',
                name='Historical Price',
                line=dict(color='#1E88E5', width=2)
            ))

            # Create future dates
            last_date = raw_data.index[-1]
            future_dates = pd.date_range(
                start=last_date + timedelta(days=1),
                periods=prediction_days,
                freq='D'
            )

            # Predicted prices
            fig.add_trace(go.Scatter(
                x=future_dates,
                y=future_predictions,
                mode='lines+markers',
                name='Predicted Price',
                line=dict(color='#FF6B6B', width=2, dash='dash'),
                marker=dict(size=8)
            ))

            fig.update_layout(
                title=f"{selected_ticker} - Historical & Predicted Prices",
                xaxis_title="Date",
                yaxis_title="Price (USD)",
                hovermode='x unified',
                height=500
            )

            st.plotly_chart(fig, use_container_width=True)

            # Actual vs Predicted on test set
            st.markdown("---")
            st.subheader("🎯 Model Accuracy Visualization")

            fig2 = go.Figure()

            test_dates = data_with_features.iloc[-len(metrics['y_test']):].index

            fig2.add_trace(go.Scatter(
                x=test_dates,
                y=metrics['y_test'],
                mode='lines',
                name='Actual Price',
                line=dict(color='#1E88E5', width=2)
            ))

            fig2.add_trace(go.Scatter(
                x=test_dates,
                y=metrics['test_pred'],
                mode='lines',
                name='Model Prediction',
                line=dict(color='#4CAF50', width=2)
            ))

            fig2.update_layout(
                title="Actual vs Predicted Prices (Test Set)",
                xaxis_title="Date",
                yaxis_title="Price (USD)",
                hovermode='x unified',
                height=400
            )

            st.plotly_chart(fig2, use_container_width=True)

            # Feature importance
            st.markdown("---")
            st.subheader("🔍 What Drives the Prediction?")

            feature_importance = pd.DataFrame({
                'Feature': X.columns,
                'Importance': model.feature_importances_
            }).sort_values('Importance', ascending=False)

            fig3 = px.bar(
                feature_importance,
                x='Importance',
                y='Feature',
                orientation='h',
                title='Feature Importance in Prediction Model'
            )

            fig3.update_layout(height=400)
            st.plotly_chart(fig3, use_container_width=True)

            # Disclaimer
            st.markdown("---")
            st.warning("""
            **⚠️ Disclaimer:** This is an educational demo for the ML for Engineers course.
            Do NOT use these predictions for actual trading decisions. Stock markets are
            unpredictable, and past performance does not guarantee future results.
            Always consult with financial advisors before making investment decisions.
            """)

        else:
            st.error("❌ Insufficient data available. Please try a different stock or date range.")

else:
    # Show welcome message and sample data
    st.info("👈 Select a stock ticker and click 'Predict Stock Price' to see ML in action!")

    # Show sample stock info
    st.markdown("---")
    st.subheader("📋 Available Stocks")

    stocks_df = pd.DataFrame([
        {'Ticker': ticker, 'Company': name}
        for ticker, name in AVAILABLE_STOCKS.items()
    ])

    st.dataframe(stocks_df, use_container_width=True)

    st.markdown("---")
    st.markdown("""
    ### 🎓 About This Demo

    This stock price predictor is Demo #1 from **Module 0** of the ML for Engineers course.

    **What you'll learn by building this:**
    - Data fetching and preprocessing
    - Feature engineering (technical indicators)
    - Random Forest regression
    - Model evaluation and visualization
    - Deployment with Streamlit

    **Technologies used:**
    - Python 3.8+
    - scikit-learn (ML)
    - yfinance (Data)
    - Streamlit (Web app)
    - Plotly (Visualizations)

    **By Module 3 of this course, YOU will build this from scratch!**
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 2rem 0;'>
    <p>Built with ❤️ for ML for Engineers Course | Module 0: The Hook</p>
    <p><small>Powered by Streamlit, scikit-learn, and yfinance</small></p>
</div>
""", unsafe_allow_html=True)
