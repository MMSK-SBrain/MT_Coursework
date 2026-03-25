# Module 3: Regression - Stock Prediction & Beyond
## The Moment You've Been Waiting For!

**Course Code:** ML-ENG-M3
**Duration:** 2 weeks (self-paced)
**Total Video Content:** ~8-10 hours
**Hands-on Time:** ~14-16 hours
**Theory/Practice Ratio:** 25% / 75%
**Pedagogy:** BUILD + CELEBRATE (The Payoff!)

---

## 🎯 Module Purpose

**THE PAYOFF MOMENT:** Build the stock predictor from Module 0!

**The Journey:**
- Module 0: "Wow, a stock predictor!" (Demo)
- Module 1: "Let me understand stock DATA" (Exploration)
- Module 2: "First, learn classification" (Building skills)
- **Module 3: "NOW I BUILD THAT STOCK PREDICTOR!"** ← **YOU ARE HERE!**

**Emotional Arc:**
- Week 0: Curiosity ("Can I really predict stocks?")
- Weeks 1-4: Learning and building
- **Week 5-6: ACHIEVEMENT** ("I built what I saw in Module 0!")

**What They Build:**
1. **Week 1:**
   - House price predictor (regression fundamentals)
   - Sales forecaster (time series intro)
   - **STOCK PRICE PREDICTOR** (the big one!)

2. **Week 2:**
   - Energy consumption predictor (manufacturing)
   - Patient readmission timing (healthcare)
   - Capstone: Advanced stock predictor + deployment

**What They Learn:**
- ✅ Regression vs classification
- ✅ Linear and non-linear regression
- ✅ Feature engineering for time series
- ✅ Technical indicators (RSI, MACD, Moving Averages)
- ✅ Model evaluation for regression (MSE, RMSE, R²)
- ✅ Real-world stock prediction

---

## 📅 Two-Week Structure

### Week 1: Regression Fundamentals + Stock Prediction
```
Day 1 (2.5 hrs): Session 1 - Regression Basics (House Prices)
Day 2 (2.5 hrs): Session 2 - Time Series Intro (Sales Forecasting)
Day 3 (3 hrs):   Session 3 - 🎉 STOCK PRICE PREDICTOR! 🎉
Day 4-7: Stock predictor refinement, practice
```

### Week 2: Advanced Regression + Applications
```
Day 8 (2.5 hrs):  Session 4 - Feature Engineering (Energy)
Day 9 (2.5 hrs):  Session 5 - Real-World Applications (Healthcare)
Day 10 (3 hrs):   Session 6 - Capstone: Complete Stock Predictor
Day 11-14: Final project, portfolio development
```

---

## 📹 Session 3: STOCK PRICE PREDICTOR (The Main Event!)

**Duration:** ~3 hours video + 4-5 hours hands-on
**Day:** Day 3 (Week 1)
**Goal:** BUILD THE STOCK PREDICTOR FROM MODULE 0!
**Hands-on:** 80%
**Difficulty:** ⭐⭐⭐ Challenging but achievable!

### The Epic Moment

**Opening Video (5 min):**
```
"Remember Day 1, Module 0?
You saw this working stock predictor.
You were amazed.
You wondered 'Can I build that?'

Today... YOU BUILD IT.

Everything you've learned:
- Module 1: Understanding stock data ✓
- Module 2: Building ML models ✓
- Session 1-2: Regression basics ✓

It all leads to THIS moment.
Let's build your stock predictor!"
```

### Video Breakdown

#### Video 1: Welcome to Stock Prediction! (8 min)
**Type:** Talking head + energy + callback

**Content:**
1. **The Callback** (3 min):
   - Show Module 0 stock predictor demo again
   - "This is what you saw"
   - "This is what you're building TODAY"
   - Emotional connection

2. **What We're Building** (3 min):
   - Predict Apple stock price (or any stock)
   - Input: Historical prices + technical indicators
   - Output: Tomorrow's predicted price
   - Regression problem (predicting number, not category)

3. **The Plan** (2 min):
   - Load historical stock data (Module 1 skills!)
   - Engineer features (new!)
   - Train regression model
   - Make predictions
   - Evaluate accuracy
   - Deploy (preview of Module 9!)

**Learning Outcome:** Feel the significance of this moment

---

#### Video 2: Loading Stock Data Revisited (10 min)
**Type:** Screen recording

**Content:**
1. **Get the Data** (5 min):
   ```python
   import yfinance as yf
   import pandas as pd
   import numpy as np

   # Download 5 years of Apple stock data
   ticker = "AAPL"
   data = yf.download(ticker, start="2019-01-01", end="2024-01-01")

   print(data.head())
   print(f"Total days: {len(data)}")
   ```

2. **Quick Exploration** (5 min):
   - Review from Module 1
   - Visualize closing price over time
   - Identify trends
   - Any obvious patterns?

**Hands-on During Video:**
- Load data for YOUR favorite stock
- Visualize it
- Excited to predict it!

**Learning Outcome:** Prepare stock data for modeling

---

#### Video 3: Feature Engineering for Stocks (15 min)
**Type:** Screen recording + explanation

**Content:**
1. **What Features Do We Need?** (3 min):
   - Raw data: OHLCV
   - But ML needs MORE signals
   - Technical indicators help!

2. **Creating Features** (12 min):

   **Moving Averages:**
   ```python
   # 10-day moving average
   data['MA_10'] = data['Close'].rolling(window=10).mean()

   # 50-day moving average
   data['MA_50'] = data['Close'].rolling(window=50).mean()
   ```

   **Daily Returns:**
   ```python
   data['Returns'] = data['Close'].pct_change()
   ```

   **Volatility:**
   ```python
   data['Volatility'] = data['Returns'].rolling(window=10).std()
   ```

   **RSI (Relative Strength Index):**
   ```python
   def calculate_rsi(data, window=14):
       delta = data['Close'].diff()
       gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
       loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
       rs = gain / loss
       rsi = 100 - (100 / (1 + rs))
       return rsi

   data['RSI'] = calculate_rsi(data)
   ```

   **MACD:**
   ```python
   exp1 = data['Close'].ewm(span=12).mean()
   exp2 = data['Close'].ewm(span=26).mean()
   data['MACD'] = exp1 - exp2
   ```

**Hands-on During Video:**
- Create all 5 features
- Visualize them alongside price
- See how they correlate

**Learning Outcome:** Engineer technical indicators for stock prediction

---

#### Video 4: Creating the Target Variable (12 min)
**Type:** Screen recording

**Content:**
1. **What Are We Predicting?** (4 min):
   - Tomorrow's closing price
   - Shift data to create target

   ```python
   # Create target: Tomorrow's price
   data['Target'] = data['Close'].shift(-1)

   # Drop last row (no target available)
   data = data.dropna()
   ```

2. **Features vs Target** (4 min):
   ```python
   # Features (X): Everything except Target
   feature_columns = ['Open', 'High', 'Low', 'Close', 'Volume',
                      'MA_10', 'MA_50', 'Returns', 'Volatility',
                      'RSI', 'MACD']

   X = data[feature_columns]
   y = data['Target']

   print(f"Features shape: {X.shape}")
   print(f"Target shape: {y.shape}")
   ```

3. **Train/Test Split for Time Series** (4 min):
   ```python
   # IMPORTANT: For time series, don't shuffle!
   # Train on old data, test on recent data

   split_point = int(len(data) * 0.8)

   X_train = X[:split_point]
   X_test = X[split_point:]
   y_train = y[:split_point]
   y_test = y[split_point:]

   print(f"Training on: {X_train.index[0]} to {X_train.index[-1]}")
   print(f"Testing on: {X_test.index[0]} to {X_test.index[-1]}")
   ```

**Hands-on During Video:**
- Create target variable
- Split data
- Verify split makes sense

**Learning Outcome:** Prepare data for time series prediction

---

#### Video 5: Training the Stock Predictor! (15 min)
**Type:** Screen recording + celebration!

**Content:**
1. **Start Simple: Linear Regression** (6 min):
   ```python
   from sklearn.linear_model import LinearRegression
   from sklearn.metrics import mean_squared_error, r2_score

   # Create and train model
   model = LinearRegression()
   model.fit(X_train, y_train)

   print("✅ Stock predictor trained!")
   ```

2. **Make Predictions** (5 min):
   ```python
   # Predict on test set
   predictions = model.predict(X_test)

   # Create results dataframe
   results = pd.DataFrame({
       'Actual': y_test.values,
       'Predicted': predictions,
       'Date': y_test.index
   })

   print(results.head(10))
   ```

3. **Visualize Results** (4 min):
   ```python
   import matplotlib.pyplot as plt

   plt.figure(figsize=(15,6))
   plt.plot(results['Date'], results['Actual'], label='Actual Price', linewidth=2)
   plt.plot(results['Date'], results['Predicted'], label='Predicted Price', linewidth=2, alpha=0.7)
   plt.title(f'{ticker} Stock Price: Actual vs Predicted')
   plt.xlabel('Date')
   plt.ylabel('Price ($)')
   plt.legend()
   plt.grid(True)
   plt.show()
   ```

**Hands-on During Video:**
- Train your stock predictor!
- See predictions!
- Visualize actual vs predicted!
- **CELEBRATE:** This is huge!

**Learning Outcome:** Train and visualize stock price predictions

---

#### Video 6: Evaluating the Predictor (12 min)
**Type:** Screen recording + interpretation

**Content:**
1. **Regression Metrics** (6 min):
   ```python
   from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

   mae = mean_absolute_error(y_test, predictions)
   mse = mean_squared_error(y_test, predictions)
   rmse = np.sqrt(mse)
   r2 = r2_score(y_test, predictions)

   print(f"Mean Absolute Error: ${mae:.2f}")
   print(f"Root Mean Squared Error: ${rmse:.2f}")
   print(f"R² Score: {r2:.4f}")
   ```

   - **MAE:** Average prediction error in dollars
   - **RMSE:** Penalizes larger errors more
   - **R²:** How well model explains variance (0-1, higher better)

2. **What's "Good"?** (6 min):
   - For stocks: Perfect prediction is impossible
   - RMSE of $2-5 on a $150 stock = Pretty good!
   - R² > 0.7 = Decent model
   - Compare to baseline (predict yesterday's price)

   ```python
   # Baseline: Predict yesterday's price
   baseline_pred = X_test['Close'].values
   baseline_rmse = np.sqrt(mean_squared_error(y_test, baseline_pred))

   print(f"Our Model RMSE: ${rmse:.2f}")
   print(f"Baseline RMSE: ${baseline_rmse:.2f}")

   if rmse < baseline_rmse:
       print("🎉 Our model beats the baseline!")
   ```

**Hands-on During Video:**
- Calculate all metrics
- Compare to baseline
- Interpret results

**Learning Outcome:** Evaluate regression model performance

---

#### Video 7: Improving the Predictor (15 min)
**Type:** Screen recording

**Content:**
1. **Try Advanced Algorithms** (8 min):

   **Random Forest Regressor:**
   ```python
   from sklearn.ensemble import RandomForestRegressor

   rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
   rf_model.fit(X_train, y_train)
   rf_pred = rf_model.predict(X_test)
   rf_rmse = np.sqrt(mean_squared_error(y_test, rf_pred))

   print(f"Random Forest RMSE: ${rf_rmse:.2f}")
   ```

   **Gradient Boosting:**
   ```python
   from sklearn.ensemble import GradientBoostingRegressor

   gb_model = GradientBoostingRegressor(n_estimators=100, random_state=42)
   gb_model.fit(X_train, y_train)
   gb_pred = gb_model.predict(X_test)
   gb_rmse = np.sqrt(mean_squared_error(y_test, gb_pred))

   print(f"Gradient Boosting RMSE: ${gb_rmse:.2f}")
   ```

2. **Feature Importance** (7 min):
   ```python
   # Which features matter most?
   importances = rf_model.feature_importances_
   feature_imp = pd.DataFrame({
       'Feature': feature_columns,
       'Importance': importances
   }).sort_values('Importance', ascending=False)

   print(feature_imp)

   # Plot
   plt.figure(figsize=(10,6))
   plt.barh(feature_imp['Feature'], feature_imp['Importance'])
   plt.xlabel('Importance')
   plt.title('Feature Importance in Stock Prediction')
   plt.show()
   ```

**Hands-on During Video:**
- Train 3 models
- Compare RMSE
- See which features matter most

**Learning Outcome:** Optimize stock predictor

---

#### Video 8: Predicting Tomorrow's Price! (10 min)
**Type:** Screen recording + excitement!

**Content:**
1. **The Ultimate Test** (8 min):
   ```python
   # Get latest data (today)
   latest_data = yf.download(ticker, period="1d")

   # Calculate features for today
   # (Use last 50+ days to calculate MAs, RSI, etc.)
   recent_data = yf.download(ticker, period="60d")
   # ... calculate all features ...

   # Prepare features for prediction
   latest_features = [...] # Feature vector for today

   # Predict tomorrow's price!
   tomorrow_prediction = best_model.predict([latest_features])[0]

   print(f"🔮 Predicted price for tomorrow: ${tomorrow_prediction:.2f}")
   print(f"📊 Today's closing price: ${latest_data['Close'].values[0]:.2f}")

   change = tomorrow_prediction - latest_data['Close'].values[0]
   pct_change = (change / latest_data['Close'].values[0]) * 100

   if change > 0:
       print(f"📈 Prediction: UP by ${change:.2f} ({pct_change:.2f}%)")
   else:
       print(f"📉 Prediction: DOWN by ${abs(change):.2f} ({abs(pct_change):.2f}%)")
   ```

2. **Reality Check** (2 min):
   - This is a prediction, not a guarantee!
   - Stock markets are unpredictable
   - Many factors affect prices
   - Use for learning, not actual trading (yet!)
   - You built what you saw in Module 0! 🎉

**Hands-on During Video:**
- Predict tomorrow for YOUR stock
- See the prediction!
- **CELEBRATE THE ACHIEVEMENT!**

**Learning Outcome:** Make real-world stock predictions

---

### Session 3 Activities

#### Activity 1: Complete Stock Predictor (2 hours)
**Objective:** Build end-to-end stock price predictor

**Task:**
1. Choose your stock
2. Load 5 years of data
3. Engineer 6+ features
4. Train 3 different regression models
5. Compare performance
6. Choose best model
7. Predict next day
8. Document everything

**Deliverable:**
- Complete Colab notebook
- Comparison table (3 models)
- Tomorrow's prediction
- Reflection: Accuracy and limitations

**Success Criteria:**
- RMSE better than baseline
- Clear documentation
- Working predictions

---

#### Activity 2: Multi-Stock Comparison (90 min)
**Objective:** Compare prediction difficulty across stocks

**Task:**
1. Build predictors for 3 different stocks:
   - One stable (e.g., JNJ, KO)
   - One volatile (e.g., TSLA, GME)
   - One of your choice
2. Compare RMSE across all three
3. Insights: Which is easier to predict? Why?

**Deliverable:**
- 3 stock predictors
- Comparison analysis
- Hypothesis: What makes stocks predictable?

---

#### Activity 3: Feature Engineering Experiment (60 min)
**Objective:** Test impact of different features

**Task:**
1. Baseline: Use only OHLCV
2. Add moving averages → Measure RMSE
3. Add RSI → Measure RMSE
4. Add MACD → Measure RMSE
5. Add all features → Measure RMSE

Which features help most?

**Deliverable:**
- Table showing RMSE with different feature combinations
- Conclusion about most important features

---

### Session 3 Quiz (15 questions)

**Multiple Choice (8):**
1. Regression predicts:
   - a) Categories
   - b) Continuous numbers
   - c) True/False values
   - d) Images

2. In stock prediction, what is the target variable?
   - a) Today's price
   - b) Tomorrow's price (what we're predicting)
   - c) Volume
   - d) Company name

3. Why is train/test split for time series different?
   - a) It's not different
   - b) We don't shuffle - train on old, test on recent
   - c) We need more data
   - d) Time series can't be split

4. What does RSI measure?
   - a) Price volatility
   - b) Momentum/overbought-oversold conditions
   - c) Trading volume
   - d) Company revenue

5. RMSE stands for:
   - a) Really Mean Squared Error
   - b) Root Mean Squared Error
   - c) Random Mean Standard Error
   - d) Regression Model Standard Estimate

6. A lower RMSE means:
   - a) Worse predictions
   - b) Better predictions (closer to actual)
   - c) More training time
   - d) Nothing useful

7. Feature engineering means:
   - a) Deleting features
   - b) Creating new useful features from existing data
   - c) Copying features
   - d) Renaming features

8. R² score of 0.8 means:
   - a) Model explains 80% of variance (pretty good!)
   - b) Model is 80% broken
   - c) 80 seconds of training
   - d) 80% accuracy

**True/False (4):**
9. Stock prediction with ML is 100% accurate. (False - impossible!)
10. Moving averages smooth out short-term fluctuations. (True)
11. More features always means better predictions. (False - can overfit)
12. You built the stock predictor from Module 0! (True - CELEBRATE!)

**Short Answer (3):**
13. Explain why we don't shuffle time series data when splitting.
14. What's the difference between MAE and RMSE?
15. Name 3 features you engineered for stock prediction.

**Passing Score:** 70% (11/15 correct)

---

## 📊 Module 3 Key Highlights

### Sessions 1-2 (Not detailed here, but include):

**Session 1: Regression Basics - House Prices**
- Linear regression fundamentals
- Feature scaling and normalization
- Polynomial regression intro
- Classic ML problem to build skills

**Session 2: Time Series Intro - Sales Forecasting**
- Time-based features
- Lag features
- Trend and seasonality
- Business forecasting application

**Sessions 4-6:**

**Session 4: Feature Engineering - Energy Consumption**
- Advanced feature creation
- Handling outliers
- Data transformation
- Manufacturing application

**Session 5: Healthcare Application - Patient Readmission**
- Medical data handling
- Ethical considerations
- Evaluation metrics for healthcare
- Real-world impact

**Session 6: Capstone - Advanced Stock Predictor**
- Combine everything learned
- Add sentiment analysis (preview of NLP)
- Deploy as simple web app (preview of Module 9)
- Portfolio-worthy project

---

## 📈 Module 3 Assessment Summary

### Completion Criteria

To pass Module 3:
- ✅ Complete all 6 sessions
- ✅ Build 6 different regression models
- ✅ Pass all 6 quizzes (70%+ each)
- ✅ Submit working stock predictor
- ✅ Submit capstone project
- ✅ Achieve RMSE better than baseline

### Grading Breakdown

| Component | Weight | Description |
|-----------|--------|-------------|
| Session Quizzes (6) | 25% | ~4% each |
| Session Projects (5) | 40% | Sessions 1-5, 8% each |
| Stock Predictor | 20% | Session 3 main project |
| Capstone Project | 15% | Session 6 comprehensive |

**Pass Threshold:** 70% overall + Stock predictor working

---

## 🎯 Learning Outcomes Achieved

By end of Module 3:

**Technical Skills:**
- ✅ Build regression models
- ✅ Engineer time-series features
- ✅ Calculate technical indicators
- ✅ Evaluate with MSE, RMSE, R², MAE
- ✅ Compare regression algorithms
- ✅ Handle time-series data properly

**Industry Applications:**
- ✅ Stock price prediction (Finance) ← **THE BIG ONE!**
- ✅ House pricing (Real Estate)
- ✅ Sales forecasting (Business)
- ✅ Energy prediction (Manufacturing)
- ✅ Patient readmission (Healthcare)

**The Achievement:**
- ✅ **BUILT THE STOCK PREDICTOR FROM MODULE 0!**
- ✅ "I predicted stock prices with ML!"
- ✅ Portfolio-worthy project
- ✅ Can apply to any regression problem

---

## 🔗 Connection to Module 4

### The Bridge

**Module 3 Ending:**
- "You built amazing predictors!"
- "Stock prices, house prices, sales..."
- "But how GOOD are they really?"
- "How do we make them BETTER?"
- "Module 4: Model Evaluation & Optimization!"

**Module 4 Opening:**
- "You can build models ✓"
- "Now: Make them production-quality!"
- "Learn to evaluate properly"
- "Optimize for best performance"
- "Prevent overfitting"
- "Tune hyperparameters"

---

**Module 3 Status:** Framework Complete ✅
**Estimated Learner Time:** 30-35 hours over 2 weeks
**Highlight:** 🎉 Stock Predictor Achievement! 🎉
**Next:** Module 4 Framework (Evaluation & Optimization)

---

**Last Updated:** 2026-01-05
**Version:** 1.0
**Special Note:** Session 3 is the HERO session - give it extra production value!
