# Stock Price Predictor Demo App

## Overview

This is a production-ready stock price prediction web application built with Streamlit and Machine Learning. It's Demo #1 from Module 0 (The Hook) of the ML for Engineers course.

## Features

- **Real-time Stock Data**: Fetches live data from Yahoo Finance
- **8 Stock Options**: AAPL, GOOGL, TSLA, MSFT, AMZN, INFY, TCS.NS, RELIANCE.NS
- **Technical Indicators**: Calculates MA, RSI, Volatility, Momentum
- **ML Prediction**: Uses Random Forest Regressor
- **Interactive Visualizations**: Historical prices, predictions, accuracy charts
- **Feature Importance**: Shows which factors drive predictions
- **Responsive Design**: Works on desktop and mobile

## How It Works

1. **Data Collection**: Fetches 1 year of historical stock data
2. **Feature Engineering**: Calculates 12 technical indicators
3. **Model Training**: Trains Random Forest on 80% of data
4. **Prediction**: Forecasts next 1-30 days
5. **Visualization**: Displays predictions with confidence metrics

## Installation

### Local Setup

```bash
# Clone or download the files
cd stock-predictor

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## Deployment

### Deploy to Streamlit Cloud (Free)

1. **Push to GitHub**:
   ```bash
   git init
   git add .
   git commit -m "Stock predictor demo"
   git remote add origin YOUR_GITHUB_REPO
   git push -u origin main
   ```

2. **Deploy**:
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with GitHub
   - Click "New app"
   - Select your repository and branch
   - Set main file path: `app.py`
   - Click "Deploy"

3. **Done!** Your app will be live in 2-3 minutes at:
   `https://YOUR_APP_NAME.streamlit.app`

### Deploy to Heroku

```bash
# Add Procfile
echo "web: streamlit run app.py --server.port=$PORT" > Procfile

# Add setup.sh
cat > setup.sh << EOF
mkdir -p ~/.streamlit/
echo "[server]
headless = true
port = \$PORT
enableCORS = false
" > ~/.streamlit/config.toml
EOF

# Deploy
heroku create your-app-name
git push heroku main
```

## Usage

1. **Select Stock**: Choose from dropdown (e.g., AAPL)
2. **Set Prediction Days**: Use slider (1-30 days)
3. **Click "Predict"**: Wait 5-10 seconds
4. **View Results**:
   - Current vs predicted price
   - Direction (UP/DOWN)
   - Model confidence
   - Historical accuracy
   - Feature importance

## Technical Details

### ML Model
- **Algorithm**: Random Forest Regressor
- **Features**: 12 technical indicators
- **Training**: 80-20 train-test split
- **Metrics**: R² score, MAE

### Features Used
1. Open, High, Low, Volume
2. Moving Averages (10, 20, 50-day)
3. RSI (Relative Strength Index)
4. Volatility (rolling std)
5. Momentum (10-day)
6. Volume change
7. Day of week

### Tech Stack
- **Frontend**: Streamlit
- **ML**: scikit-learn
- **Data**: yfinance
- **Viz**: Plotly
- **Python**: 3.8+

## Testing

Test locally before deploying:

```bash
# Run the app
streamlit run app.py

# Test with different stocks
# Test with different prediction days
# Verify all visualizations load
# Check mobile responsiveness
```

## Expected Performance

- **Load Time**: < 3 seconds
- **Prediction Time**: 5-10 seconds
- **Accuracy**: R² ~0.7-0.9 (varies by stock)
- **MAE**: Typically $5-20 per stock

## Troubleshooting

### Data Fetch Fails
```python
# Error: No data found
# Solution: Check internet connection, try different stock
```

### Model Training Slow
```python
# Reduce n_estimators in RandomForestRegressor
model = RandomForestRegressor(n_estimators=50)  # Instead of 100
```

### Deployment Issues
```bash
# Streamlit Cloud: Check logs in dashboard
# Heroku: heroku logs --tail
```

## Customization

### Add More Stocks
```python
AVAILABLE_STOCKS = {
    'AAPL': 'Apple Inc.',
    'YOUR_TICKER': 'Your Company',
    # Add more...
}
```

### Change Model
```python
# Use different algorithm
from sklearn.ensemble import GradientBoostingRegressor
model = GradientBoostingRegressor()
```

### Adjust Features
```python
# Add more technical indicators in calculate_technical_indicators()
data['MACD'] = calculate_macd(data)
```

## AI Prompts Used

This app was generated using ChatGPT/Claude with these prompts:

1. **Initial structure**:
   ```
   Create a Streamlit app for stock price prediction using Random Forest.
   Include technical indicators, visualizations, and deployment-ready code.
   ```

2. **Feature engineering**:
   ```
   Add technical indicators: MA (10, 20, 50), RSI, Volatility, Momentum.
   Explain each indicator in comments.
   ```

3. **Visualization**:
   ```
   Create interactive Plotly charts showing:
   - Historical prices
   - Predictions
   - Actual vs predicted
   - Feature importance
   ```

4. **Deployment**:
   ```
   Make the app deployment-ready for Streamlit Cloud.
   Add error handling, caching, and mobile responsiveness.
   ```

## Course Integration

**Module 0 - Session 1**: Students see this running demo
**Module 1**: Students learn data exploration with stock data
**Module 2**: Students learn classification basics
**Module 3**: **Students build this from scratch!**

## License

MIT License - Free for educational use

## Support

For issues or questions:
- Course forum: [Link to course forum]
- GitHub issues: [Link to repo issues]
- Email: support@mlforengineers.com

## Credits

Built for **ML for Engineers Course**
Created by: [Your Name]
Date: January 2026

---

**🎓 Ready to learn how to build this?**
Enroll in the ML for Engineers course and build this (and 9 more projects) from scratch!
