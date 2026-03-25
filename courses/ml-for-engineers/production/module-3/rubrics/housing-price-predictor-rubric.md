# Housing Price Predictor Rubric

**Total Points:** 50
**Module:** 3 - Regression
**Session:** 3.1 - Introduction to Regression
**Project:** California Housing Price Prediction
**Difficulty:** ⭐⭐ Beginner-Intermediate
**Purpose:** Introduction to regression concepts and evaluation

---

## Project Overview

This is the foundational regression project where students learn:
- Basic regression concepts
- Feature scaling and preprocessing
- Multiple regression with several features
- Regression evaluation metrics (MAE, MSE, RMSE, R²)
- Model comparison

**Dataset:** California Housing (sklearn.datasets)
- 20,640 samples
- 8 features (income, house age, rooms, location, etc.)
- Target: Median house value

**Expected Time:** 2-3 hours

---

## Grading Criteria

### 1. Data Loading & Exploration (10 points)

#### 1.1 Data Loading (3 points)
- **3 points:** Loads California Housing dataset correctly, displays first few rows, shows dataset shape and column names
- **2 points:** Loads dataset, displays basic info
- **1 point:** Loads dataset but minimal exploration
- **0 points:** Cannot load data

#### 1.2 Exploratory Data Analysis (7 points)
- **6-7 points:** Comprehensive EDA: summary statistics (describe), checks for missing values, identifies data types, creates 2+ visualizations (histograms, scatter plots, correlation heatmap), analyzes feature-target relationships, documents insights
- **4-5 points:** Good EDA: summary stats, checks missing values, 1-2 visualizations, basic insights
- **2-3 points:** Basic EDA: summary stats, checks data, minimal visualization
- **0-1 points:** Minimal or no exploration

**Key Requirements:**
- Check for missing values
- Summary statistics (mean, std, min, max)
- At least one visualization
- Brief interpretation of data

---

### 2. Data Preprocessing (12 points)

#### 2.1 Feature Scaling (6 points)
- **6 points:** Applies StandardScaler or MinMaxScaler correctly, fits on training data only, transforms both train and test, explains why scaling is important for regression, documents scaler choice
- **4-5 points:** Applies scaling correctly, fits on training data only, basic explanation
- **2-3 points:** Applies scaling but with minor issues (e.g., fits on all data)
- **0-1 points:** No scaling or fundamentally incorrect

**Critical:** Must fit scaler on training data only, then transform test data!

#### 2.2 Train-Test Split (6 points)
- **6 points:** Creates proper 80/20 or 70/30 split using train_test_split, sets random_state for reproducibility, validates split sizes, checks for data leakage
- **4-5 points:** Proper split, sets random_state, validates sizes
- **2-3 points:** Basic split with minor issues
- **0-1 points:** No split or incorrect implementation

**Key Requirements:**
- Use sklearn.model_selection.train_test_split
- Test size: 20-30%
- Random state set
- Validates X_train, X_test, y_train, y_test shapes

---

### 3. Model Implementation (15 points)

#### 3.1 Linear Regression Model (8 points)
- **7-8 points:** Implements Linear Regression from sklearn, trains on training data, makes predictions on test data, code is clean and well-commented, uses proper sklearn syntax
- **5-6 points:** Implements and trains Linear Regression successfully, makes predictions
- **3-4 points:** Basic implementation with minor issues
- **0-2 points:** Model doesn't run or major errors

#### 3.2 Model Comparison (7 points)
- **6-7 points:** Implements and compares 2+ algorithms (e.g., Linear Regression, Ridge, Lasso, Decision Tree, Random Forest), creates comparison table with metrics, discusses which performs best and why
- **4-5 points:** Implements 2 models, basic comparison
- **2-3 points:** Attempts second model but limited comparison
- **0-1 points:** Only one model or no comparison

**Suggested Models:**
- Linear Regression (baseline)
- Ridge Regression (with regularization)
- Random Forest Regressor
- Decision Tree Regressor

---

### 4. Model Evaluation (10 points)

#### 4.1 Metrics Calculation (6 points)
- **5-6 points:** Calculates all four metrics: MAE, MSE, RMSE, R², interprets each metric correctly, provides context (e.g., "RMSE of $68K on houses averaging $200K = 34% error"), explains what each metric tells us
- **3-4 points:** Calculates 3 metrics, basic interpretation
- **1-2 points:** Calculates 1-2 metrics, minimal interpretation
- **0 points:** No metrics or incorrect calculations

**Required Metrics:**
- MAE (Mean Absolute Error) - in dollars
- MSE (Mean Squared Error)
- RMSE (Root Mean Squared Error) - in dollars
- R² Score (Coefficient of Determination)

**Target Performance:**
- R² > 0.60 (good)
- RMSE < $80,000

#### 4.2 Results Visualization (4 points)
- **4 points:** Creates actual vs predicted scatter plot with diagonal reference line, residual plot, both plots well-labeled with titles and axis labels
- **3 points:** Creates actual vs predicted plot, adequate labeling
- **2 points:** Basic visualization, minimal labeling
- **0-1 points:** No visualization or poor quality

**Key Visualizations:**
- Actual vs Predicted scatter plot
- Ideally: Residual plot to check for patterns

---

### 5. Analysis & Documentation (3 points)

#### 5.1 Code Comments (1 point)
- **1 point:** Code has clear comments explaining key steps
- **0 points:** No comments or minimal comments

#### 5.2 Results Interpretation (2 points)
- **2 points:** Provides thoughtful analysis: discusses model performance, identifies which features might be important, suggests potential improvements, realistic assessment
- **1 point:** Basic interpretation of results
- **0 points:** No interpretation

---

## Bonus Points (5 points available)

### Feature Engineering (+2 points)
- Creates new features (e.g., rooms per household, bedrooms per room, population density)
- Tests impact on model performance

### Hyperparameter Tuning (+2 points)
- Uses GridSearchCV or RandomizedSearchCV
- Tests different regularization strengths for Ridge/Lasso
- Documents optimal hyperparameters

### Advanced Visualization (+1 point)
- Creates feature importance plot (for tree-based models)
- Geographic visualization of predictions
- Multiple insightful charts

---

## Score Interpretation

| Points | Grade | Interpretation |
|--------|-------|----------------|
| 45-55 | A | Excellent - comprehensive analysis and implementation |
| 40-44 | B | Good - solid understanding with minor gaps |
| 35-39 | C | Adequate - meets basic requirements |
| 30-34 | D | Below expectations - significant gaps |
| <30 | F | Incomplete or fundamentally flawed |

**Minimum Passing:** 35 points (70%)

---

## Common Issues and Deductions

### Critical Errors
- **Fits scaler on entire dataset:** -3 points (data leakage)
- **No train-test split:** -6 points
- **Model doesn't run:** -8 points

### Moderate Issues
- **No feature scaling:** -6 points
- **Missing evaluation metrics:** -2 points per metric
- **No visualization:** -4 points

### Minor Issues
- **No random state set:** -1 point
- **Poor code comments:** -1 point
- **No result interpretation:** -2 points

---

## Sample Successful Submission

**Score: 48/50 (A)**

**Strengths:**
- Excellent EDA with correlation heatmap showing MedInc is strongest predictor (9/10)
- Perfect preprocessing: StandardScaler fitted on training data only (12/12)
- Compared Linear, Ridge, and Random Forest - great comparison table (15/15)
- All metrics calculated with thoughtful interpretation: "R²=0.64 means model explains 64% of variance" (9/10)
- Clean code with good comments (3/3)
- **Bonus:** Created rooms_per_household feature (+2)

**Areas for Improvement:**
- Residual plot would strengthen analysis (-1)

**Feedback:**
Great foundational regression work! Your feature engineering (rooms per household) showed creativity. Consider adding residual plots to check for patterns in errors. This demonstrates solid understanding of regression basics.

---

## Learning Objectives Assessed

Students demonstrate ability to:
- ✅ Load and explore tabular datasets
- ✅ Apply feature scaling appropriately
- ✅ Create proper train-test splits
- ✅ Implement regression models
- ✅ Calculate and interpret regression metrics
- ✅ Compare model performance
- ✅ Visualize results effectively
- ✅ Document code and findings

---

## Next Steps

After completing this project, students should:
1. Understand regression fundamentals
2. Be comfortable with sklearn API
3. Know how to evaluate regression models
4. Be ready for time series regression (Session 3.3)
5. Have a working example for their portfolio

---

**Last Updated:** 2026-01-06
**Version:** 1.0
**Session:** 3.1 - Introduction to Regression
