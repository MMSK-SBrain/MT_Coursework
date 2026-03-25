# Sales Forecast Rubric

**Total Points:** 50
**Module:** 3 - Regression
**Session:** 3.3 - Time Series Basics
**Project:** Monthly Sales Forecasting
**Difficulty:** ⭐⭐⭐ Intermediate
**Purpose:** Introduction to time series regression and temporal features

---

## Project Overview

This project bridges basic regression and stock prediction by introducing:
- Time series concepts (trend, seasonality)
- Chronological train-test splits
- Lag features and rolling statistics
- Business forecasting application
- Preventing data leakage in temporal data

**Dataset:** Monthly sales data (synthetic or real retail data)
- 60+ months of historical data
- Features: Marketing spend, seasonality, promotions
- Target: Monthly sales ($)

**Expected Time:** 2-3 hours

---

## Grading Criteria

### 1. Time Series Data Understanding (12 points)

#### 1.1 Data Loading & Temporal Setup (4 points)
- **4 points:** Loads data with proper datetime index, ensures chronological order, validates no missing months, displays date range, shows data structure
- **3 points:** Loads data with datetime index, checks chronological order
- **2 points:** Loads data but datetime handling has minor issues
- **0-1 points:** No proper datetime handling

**Key Requirements:**
- Datetime index (not just integer index)
- Data in chronological order
- No gaps in time series (or gaps handled)
- Date range documented

---

#### 1.2 Trend & Seasonality Analysis (8 points)
- **7-8 points:** Comprehensive analysis: visualizes sales over time, identifies trend (upward/downward/stable), detects seasonality patterns (monthly, quarterly, yearly), uses decomposition (seasonal_decompose) or rolling averages, documents findings with specific examples ("Sales spike in December, dip in February")
- **5-6 points:** Good analysis: visualizes time series, identifies trend and/or seasonality, basic decomposition
- **3-4 points:** Basic analysis: plots sales over time, mentions patterns
- **1-2 points:** Minimal analysis, plots only
- **0 points:** No temporal analysis

**Key Requirements:**
- Time series plot with clear date axis
- Identification of trend (even if "no clear trend")
- Discussion of seasonality (or lack thereof)
- At least one analytical technique (decomposition, moving average, or visual inspection)

---

### 2. Time Series Feature Engineering (15 points)

#### 2.1 Lag Features (6 points)
- **5-6 points:** Creates multiple lag features (lag_1, lag_3, lag_12), explains rationale (e.g., "lag_12 captures year-over-year comparison"), properly handles NaN values from lagging, validates no data leakage
- **3-4 points:** Creates 2+ lag features, handles NaN, basic explanation
- **1-2 points:** Creates 1 lag feature with issues
- **0 points:** No lag features

**Example Lag Features:**
- lag_1: Last month's sales
- lag_3: Sales from 3 months ago
- lag_12: Sales from same month last year

**Critical:** Lag features must use PAST data only!

---

#### 2.2 Rolling Statistics (6 points)
- **5-6 points:** Creates rolling mean and/or rolling std with appropriate windows (3-month, 6-month, 12-month), explains window choice, handles NaN at beginning of series, visualizes rolling stats with original data
- **3-4 points:** Creates rolling statistics, reasonable windows, handles NaN
- **1-2 points:** Basic rolling stats with issues
- **0 points:** No rolling statistics

**Example Rolling Features:**
- rolling_mean_3: 3-month moving average
- rolling_mean_12: 12-month moving average
- rolling_std_3: 3-month volatility

---

#### 2.3 Date/Time Features (3 points)
- **3 points:** Extracts temporal features: month (1-12), quarter (Q1-Q4), year, day of week (if applicable), creates one-hot encoding or cyclical encoding for month/quarter
- **2 points:** Extracts month and/or quarter
- **1 point:** Minimal date features
- **0 points:** No date features

**Useful Time Features:**
- Month number (for seasonality)
- Quarter (for quarterly patterns)
- Year (for long-term trend)
- Is_December (or other important months)

---

### 3. Proper Time Series Splitting (10 points)

#### 3.1 Chronological Split (7 points)
- **7 points:** PERFECT chronological split: train on older data (first 70-80%), test on recent data (last 20-30%), NO SHUFFLING, clearly documents split date, visualizes split on timeline, explains why chronological split is critical
- **5-6 points:** Correct chronological split, no shuffling, documents split
- **3-4 points:** Chronological split with minor issues
- **1-2 points:** Attempts chronological split but has problems
- **0 points:** Uses random split (WRONG for time series!)

**Critical Requirements:**
- MUST be chronological (zero points if shuffled)
- Train on old, test on recent
- Clear boundary (e.g., "Train: Jan 2018 - Dec 2021, Test: Jan 2022 - Dec 2022")

---

#### 3.2 Data Leakage Prevention (3 points)
- **3 points:** Demonstrates awareness of leakage risks, validates features use only past information, explains why future data cannot be in features, documents validation steps
- **2 points:** Shows awareness, basic validation
- **1 point:** Mentions data leakage concept
- **0 points:** No consideration of data leakage

**Common Leakage Issues to Avoid:**
- Using future sales in features
- Calculating statistics on entire dataset
- Forward-looking lag features

---

### 4. Model Training & Evaluation (10 points)

#### 4.1 Model Implementation (5 points)
- **5 points:** Trains 2+ regression models (Linear Regression, Random Forest, Gradient Boosting), appropriate hyperparameters, models trained only on training data, predictions on test data
- **3-4 points:** Trains 1-2 models successfully
- **1-2 points:** Basic model with issues
- **0 points:** Model doesn't run

---

#### 4.2 Time Series Evaluation (5 points)
- **5 points:** Calculates MAE, RMSE, R² on test data, compares to baseline (naive forecast: predict last month's sales), creates forecast vs actual plot with dates, interprets results in business context ("RMSE of $50K on average sales of $500K = 10% error")
- **3-4 points:** Calculates metrics, basic comparison, plots results
- **1-2 points:** Minimal evaluation
- **0 points:** No proper evaluation

**Required:**
- At least 2 metrics (RMSE, R²)
- Baseline comparison (naive forecast)
- Forecast visualization with dates

---

### 5. Business Insights & Documentation (3 points)

#### 5.1 Business Interpretation (2 points)
- **2 points:** Provides business-relevant insights: discusses forecasting accuracy in practical terms, identifies important factors (e.g., "December sales 2x average due to holidays"), suggests how forecast could inform business decisions (inventory, staffing, marketing)
- **1 point:** Basic business interpretation
- **0 points:** No business context

---

#### 5.2 Code Quality (1 point)
- **1 point:** Clean, well-commented code with clear structure
- **0 points:** Poor code quality

---

## Bonus Points (5 points available)

### Advanced Time Series Techniques (+3 points)
- **3 points:** Implements SARIMA, Prophet, or LSTM for time series, compares with traditional regression
- **2 points:** Attempts advanced method
- **1 point:** Research and documentation of advanced methods

### Rolling Window Validation (+2 points)
- **2 points:** Implements walk-forward validation or rolling window backtesting, documents performance over time
- **1 point:** Attempts cross-validation appropriate for time series

---

## Score Interpretation

| Points | Grade | Interpretation |
|--------|-------|----------------|
| 45-55 | A | Excellent - strong time series understanding |
| 40-44 | B | Good - solid time series concepts |
| 35-39 | C | Adequate - meets time series basics |
| 30-34 | D | Below expectations - gaps in time series understanding |
| <30 | F | Incomplete or fundamental time series errors |

**Minimum Passing:** 35 points (70%)

---

## Common Issues and Deductions

### Critical Errors (Major Deductions)
- **Random train-test split:** -7 points (fundamental time series error!)
- **Data leakage (future in features):** -5 points
- **No temporal features:** -9 points (defeats project purpose)

### Significant Issues (Medium Deductions)
- **No lag features:** -6 points
- **No trend/seasonality analysis:** -5 points
- **No baseline comparison:** -3 points

### Minor Issues (Small Deductions)
- **Poor datetime handling:** -2 points
- **No business interpretation:** -2 points
- **Inadequate visualization:** -2 points

---

## Sample Excellent Submission

**Score: 52/50 (A+)**

**Strengths:**
- Perfect datetime setup with proper indexing (12/12)
- Excellent feature engineering: lag_1, lag_3, lag_12, rolling_mean_3, rolling_mean_12, month, quarter (15/15)
- PERFECT chronological split with clear visualization (10/10)
- Trained Linear Regression, Random Forest, and Gradient Boosting - comprehensive comparison (10/10)
- Strong business insights: "Model forecasts Q4 sales $680K (RMSE $45K = 6.6% error), enabling early inventory planning" (3/3)
- **Bonus:** Implemented Facebook Prophet for comparison (+3)

**Feedback:**
Outstanding time series work! Your lag_12 feature captured year-over-year patterns perfectly (R² improved from 0.68 to 0.82). The business interpretation shows you understand forecasting's real-world value. The Prophet comparison was impressive - great initiative! This is portfolio-ready.

---

## Distinguishing Features from Housing Project

**Housing Price Predictor (Session 3.1):**
- Random train-test split (okay for independent samples)
- Cross-sectional data (no time dimension)
- Standard feature engineering

**Sales Forecast (Session 3.3):**
- ✅ Chronological split (critical difference!)
- ✅ Temporal features (lags, rolling stats)
- ✅ Trend and seasonality analysis
- ✅ Data leakage awareness
- ✅ Baseline comparison (naive forecast)

**Key Learning:** Time series requires different handling than cross-sectional data!

---

## Learning Objectives Assessed

Students demonstrate ability to:
- ✅ Handle datetime data correctly
- ✅ Identify trends and seasonality
- ✅ Create lag features and rolling statistics
- ✅ Implement chronological train-test splits
- ✅ Prevent data leakage in time series
- ✅ Evaluate time series forecasts
- ✅ Provide business context for predictions
- ✅ Prepare for stock prediction (Session 3.6)

---

## Connection to Stock Predictor

This project is **critical preparation** for the stock predictor:

| Concept | Sales Forecast | Stock Predictor |
|---------|---------------|-----------------|
| Chronological split | ✅ Required | ✅ Required |
| Lag features | Monthly sales lags | Price lags |
| Rolling stats | Rolling mean sales | Moving averages |
| Seasonality | Holiday patterns | Market cycles |
| No data leakage | ✅ Critical | ✅ Critical |

**Students who master this will succeed in Session 3.6!**

---

## Instructor Notes

### What to Emphasize
1. **Chronological splitting is NON-NEGOTIABLE** for time series
2. Data leakage is the #1 time series mistake
3. Baseline comparison provides context (forecasting is hard!)
4. Business interpretation matters (this is practical ML)

### What to Watch For
- Students using random_state with shuffle (wrong!)
- Lag features created incorrectly (leaking future)
- Rolling statistics calculated on entire dataset
- No awareness of why time series is different

### Teaching Moment
If student uses random split: "Imagine you're forecasting 2024 sales. Would you have access to June 2024 data in January 2024? Random split lets the model 'see the future' during training. In production, this fails completely."

---

**Last Updated:** 2026-01-06
**Version:** 1.0
**Session:** 3.3 - Time Series Basics
**Bridge to:** Session 3.6 - Stock Predictor PAYOFF
