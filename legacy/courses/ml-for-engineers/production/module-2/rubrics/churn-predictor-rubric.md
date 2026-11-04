# Customer Churn Prediction Project Rubric

**Total Points:** 75
**Module:** 2 - Classification
**Project:** Customer Churn Predictor
**Session:** 2.5
**Target Accuracy:** >80%
**Target Recall:** >75% (catching churners is valuable!)

---

## Project Overview

Predict which customers are likely to cancel their service (churn). This business-critical application introduces feature engineering, handling mixed data types (numerical and categorical), and translating ML results into business actions. You'll work with realistic messy data and learn to create features that improve model performance.

**Learning Objectives:**
- Engineer meaningful features from raw business data
- Handle categorical variables (Label Encoding, One-Hot Encoding)
- Work with mixed data types (numerical + categorical)
- Address class imbalance in real datasets
- Extract business insights from ML models
- Understand the business value of churn prediction
- Optimize for business metrics, not just accuracy

**Business Context:**
- Acquiring new customers costs 5-25x more than retaining existing ones
- Identifying at-risk customers enables proactive retention efforts
- Even small improvements in churn prediction can save millions in revenue

---

## Grading Criteria

### 1. Data Preprocessing & Exploration (10 points)

| Points | Criteria |
|--------|----------|
| 9-10 | **Excellent:** Loads data correctly, comprehensive EDA with summary statistics and visualizations, identifies data types (numerical vs categorical), checks for missing values and handles appropriately, analyzes class distribution (imbalance?), creates visualizations showing churn patterns (churn by tenure, by contract type, etc.), identifies potential feature engineering opportunities, documents data quality issues |
| 7-8 | **Good:** Loads data correctly, good EDA with statistics and 2-3 visualizations, identifies data types, handles missing values, checks class distribution, basic churn pattern analysis |
| 5-6 | **Adequate:** Loads data, basic EDA (head, info, describe), identifies some data types, basic missing value handling, checks class distribution |
| 3-4 | **Poor:** Loads data, minimal EDA, doesn't properly identify data types, poor missing value handling, ignores class distribution |
| 0-2 | **Failing:** Cannot load data or no meaningful exploration |

**Key Requirements:**
- ✅ Load customer churn dataset (Telco, Bank, or similar)
- ✅ Display shape, info(), describe()
- ✅ Check for missing values and handle them
- ✅ Analyze churn rate (class distribution)
- ✅ Create visualizations:
  - Churn distribution (pie chart or bar chart)
  - Churn by categorical features (contract type, payment method)
  - Churn by numerical features (tenure, monthly charges)
- ✅ Document observations and insights

**Expected Dataset Characteristics:**
- 5,000-10,000 customer records
- Mix of numerical (tenure, charges) and categorical (gender, contract type) features
- Binary target: Churned (Yes/No) or (1/0)
- Typically imbalanced (20-30% churn rate)

---

### 2. Feature Engineering (15 points)

| Points | Criteria |
|--------|----------|
| 14-15 | **Excellent:** Creates 5+ engineered features with clear business logic, examples: tenure categories (new/medium/loyal), average monthly charge (total/tenure), service combinations, contract value segments, explains rationale for each feature, tests feature importance, compares model performance with/without engineered features, demonstrates improvement from feature engineering, documents feature creation process |
| 11-13 | **Good:** Creates 3-4 engineered features with business logic, explains rationale, tests feature importance, shows some performance improvement, documents process |
| 8-10 | **Adequate:** Creates 1-2 engineered features, basic rationale, limited importance testing, minimal documentation |
| 5-7 | **Poor:** Creates arbitrary features without clear logic, no rationale, no testing, poor documentation |
| 0-4 | **Failing:** No feature engineering or creates features that break the model |

**Key Requirements:**
- ✅ Create at least 3 meaningful engineered features
- ✅ Justify each feature with business logic
- ✅ Test feature importance after training
- ✅ Compare performance with/without features
- ✅ Document feature creation code clearly

**Recommended Feature Engineering Examples:**
```python
# Tenure categories
df['tenure_category'] = pd.cut(df['tenure'],
                               bins=[0, 12, 24, 48, 72],
                               labels=['0-1yr', '1-2yr', '2-4yr', '4+yr'])

# Average monthly charge
df['avg_monthly_charge'] = df['TotalCharges'] / df['tenure']

# Service count (how many services customer uses)
service_cols = ['PhoneService', 'InternetService', 'OnlineSecurity', ...]
df['num_services'] = df[service_cols].apply(lambda x: x.str.contains('Yes').sum(), axis=1)

# Contract value segment
df['contract_value'] = pd.cut(df['MonthlyCharges'],
                              bins=[0, 30, 70, 100, 200],
                              labels=['Low', 'Medium', 'High', 'Premium'])

# Customer lifetime value (CLV)
df['estimated_clv'] = df['MonthlyCharges'] * df['tenure']
```

**Business Logic Examples:**
- Tenure categories: New customers (< 1 year) churn more
- Avg monthly charge: High spenders may be more/less loyal
- Service count: More services = more switching costs
- Contract type: Month-to-month = higher churn risk

---

### 3. Categorical Data Handling (10 points)

| Points | Criteria |
|--------|----------|
| 9-10 | **Excellent:** Correctly identifies all categorical variables, applies appropriate encoding (Label Encoding for ordinal, One-Hot for nominal), understands when to use each method, handles binary variables appropriately, avoids dummy variable trap, scales numerical features (StandardScaler), documents encoding choices with justification, all features properly encoded for ML |
| 7-8 | **Good:** Identifies most categorical variables, applies appropriate encoding for most, understands main differences, handles binary variables, applies scaling, documents choices |
| 5-6 | **Adequate:** Identifies some categorical variables, applies encoding (may mix up methods), basic understanding, minimal scaling, limited documentation |
| 3-4 | **Poor:** Misses categorical variables, incorrect encoding, doesn't understand differences, no scaling, no documentation |
| 0-2 | **Failing:** Cannot handle categorical variables or critical errors |

**Key Requirements:**
- ✅ Identify all categorical variables
- ✅ Apply Label Encoding for ordinal variables (if any)
- ✅ Apply One-Hot Encoding for nominal variables
- ✅ Handle binary variables (Yes/No, Male/Female) appropriately
- ✅ Avoid dummy variable trap (drop_first=True)
- ✅ Scale numerical features (StandardScaler or MinMaxScaler)
- ✅ Document encoding decisions

**Encoding Guidelines:**
```python
from sklearn.preprocessing import LabelEncoder, StandardScaler
import pandas as pd

# Binary variables (Yes/No) - Simple mapping
df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})

# Ordinal variables (if any) - Label Encoding
# Example: Contract: Month-to-month < One year < Two year
label_enc = LabelEncoder()
df['Contract_encoded'] = label_enc.fit_transform(df['Contract'])

# Nominal variables (no inherent order) - One-Hot Encoding
# Example: PaymentMethod, InternetService
df = pd.get_dummies(df,
                    columns=['PaymentMethod', 'InternetService'],
                    drop_first=True)

# Scale numerical features
scaler = StandardScaler()
numerical_cols = ['tenure', 'MonthlyCharges', 'TotalCharges']
df[numerical_cols] = scaler.fit_transform(df[numerical_cols])
```

**Important:** Fit encoders and scalers ONLY on training data, then transform both train and test!

---

### 4. Model Training & Class Imbalance Handling (20 points)

| Points | Criteria |
|--------|----------|
| 18-20 | **Excellent:** Trains 3+ algorithms, addresses class imbalance using appropriate techniques (class_weight, SMOTE, or threshold adjustment), achieves >80% accuracy AND >75% recall, implements cross-validation, compares algorithms with multiple metrics (accuracy, precision, recall, F1, AUC), creates ROC curves, tunes hyperparameters, documents approach, all code runs without errors |
| 15-17 | **Good:** Trains 3 algorithms, addresses imbalance (class weights or similar), achieves targets, uses cross-validation, compares with multiple metrics, basic tuning, good documentation |
| 11-14 | **Adequate:** Trains 2 algorithms, acknowledges imbalance, achieves 75-80% accuracy, basic comparison, minimal tuning, basic documentation |
| 6-10 | **Poor:** Trains 1-2 algorithms, ignores imbalance, below 75% accuracy, accuracy-only comparison, no tuning |
| 0-5 | **Failing:** Cannot train models, major errors, or far below target accuracy |

**Key Requirements:**
- ✅ Train at least 3 algorithms:
  - Logistic Regression
  - Random Forest
  - Gradient Boosting (XGBoost or LightGBM)
- ✅ Address class imbalance with at least one technique
- ✅ Achieve >80% accuracy target
- ✅ Achieve >75% recall target (catching churners)
- ✅ Use cross-validation (k-fold)
- ✅ Compare algorithms comprehensively
- ✅ Document best model and why

**Handling Class Imbalance:**
```python
from sklearn.ensemble import RandomForestClassifier
from imblearn.over_sampling import SMOTE

# Method 1: Class weights
rf_model = RandomForestClassifier(
    n_estimators=100,
    class_weight='balanced',  # Handles imbalance
    random_state=42
)

# Method 2: SMOTE (Synthetic Minority Over-sampling)
smote = SMOTE(random_state=42)
X_train_balanced, y_train_balanced = smote.fit_resample(X_train, y_train)

# Method 3: Adjust decision threshold
# Instead of 0.5, use lower threshold (0.3) to catch more churners
probs = model.predict_proba(X_test)[:, 1]
predictions = (probs > 0.3).astype(int)
```

**Recommended Algorithms:**
- Logistic Regression: Fast, interpretable baseline
- Random Forest: Good performance, feature importance
- Gradient Boosting: Often best performance for tabular data

---

### 5. Business Insights & Feature Importance (15 points)

| Points | Criteria |
|--------|----------|
| 14-15 | **Excellent:** Analyzes feature importance comprehensively, identifies top 10 churn drivers with business interpretation, creates professional visualizations (importance plots, SHAP values optional), provides specific, actionable business recommendations (e.g., "Focus retention offers on month-to-month customers with tenure < 1 year"), estimates business impact (cost savings, revenue retention), discusses precision vs recall tradeoff in business terms, segments customers by churn risk |
| 11-13 | **Good:** Analyzes feature importance, identifies top churn drivers, good visualizations, provides actionable recommendations, discusses business impact, considers metric tradeoffs |
| 8-10 | **Adequate:** Basic feature importance analysis, identifies some drivers, basic visualizations, general recommendations, limited business impact discussion |
| 5-7 | **Poor:** Minimal feature analysis, vague drivers, poor visualizations, generic recommendations, no business impact |
| 0-4 | **Failing:** No business analysis or purely technical focus |

**Key Requirements:**
- ✅ Extract and visualize feature importance
- ✅ Identify top 10 churn drivers
- ✅ Interpret findings in business terms
- ✅ Provide specific, actionable recommendations
- ✅ Estimate business impact (even rough estimates)
- ✅ Discuss false positive vs false negative costs
- ✅ Consider customer segmentation by risk

**Feature Importance Analysis:**
```python
# Extract importance from Random Forest
importances = rf_model.feature_importances_
feature_names = X_train.columns
importance_df = pd.DataFrame({
    'Feature': feature_names,
    'Importance': importances
}).sort_values('Importance', ascending=False)

# Visualize top 10
plt.figure(figsize=(10, 6))
top_10 = importance_df.head(10)
plt.barh(top_10['Feature'], top_10['Importance'])
plt.xlabel('Importance')
plt.title('Top 10 Churn Drivers')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()
```

**Business Recommendations Example:**
```
Top Churn Drivers Identified:
1. Contract Type (Month-to-month) - 23% importance
2. Tenure < 12 months - 18% importance
3. No Tech Support - 12% importance

Actionable Recommendations:
1. Offer contract upgrades (month→annual) with 10% discount to new customers
2. Implement onboarding program for customers in first 90 days
3. Proactive tech support outreach to high-value customers without support plans

Expected Impact:
- If we reduce churn by 5% (from 27% to 22%)
- 1,000 customers saved annually
- Avg customer value: $1,500/year
- Revenue impact: $1.5M annually
```

---

### 6. Model Evaluation & Documentation (5 points)

| Points | Criteria |
|--------|----------|
| 5 | **Excellent:** Comprehensive evaluation with confusion matrix, classification report, ROC curve, AUC score, analyzes false positives and false negatives, documents complete methodology, clear conclusions, professional presentation |
| 4 | **Good:** Good evaluation with confusion matrix, classification report, AUC, analyzes errors, documents methodology, clear conclusions |
| 3 | **Adequate:** Basic evaluation with confusion matrix, classification report, basic error analysis, minimal documentation |
| 2 | **Poor:** Minimal evaluation, incomplete analysis, poor documentation |
| 0-1 | **Failing:** No proper evaluation or documentation |

**Key Requirements:**
- ✅ Confusion matrix with heatmap
- ✅ Classification report (precision, recall, F1)
- ✅ ROC curve and AUC score
- ✅ Analysis of false positives vs false negatives
- ✅ Document complete approach
- ✅ Conclusions and recommendations

---

## Bonus Points (Optional - Up to +10 points)

### Customer Segmentation (+3 points)
- Segment customers by churn risk (high/medium/low)
- Analyze characteristics of each segment
- Recommend tailored retention strategies per segment

### SHAP Values for Interpretability (+4 points)
- Implement SHAP (SHapley Additive exPlanations)
- Show individual prediction explanations
- Create SHAP summary plots
- Explain predictions for specific high-risk customers

### Cost-Benefit Analysis (+3 points)
- Calculate cost of false positives (unnecessary retention offers)
- Calculate cost of false negatives (lost customers)
- Find optimal decision threshold based on costs
- Estimate ROI of churn prediction model

---

## Common Mistakes to Avoid

❌ **Fitting encoders/scalers on all data** - Only fit on training, transform test
❌ **Ignoring class imbalance** - Leads to model predicting all "No Churn"
❌ **Using accuracy alone** - Misleading for imbalanced data
❌ **Not handling categorical variables** - ML needs numbers
❌ **No feature engineering** - Raw features rarely optimal
❌ **Forgetting business context** - This is a business problem, not just ML
❌ **Data leakage** - Don't include information from the future
❌ **No cross-validation** - Single split may be misleading

---

## Grading Summary

| Category | Points | Your Score |
|----------|--------|------------|
| Data Preprocessing & Exploration | 10 | |
| Feature Engineering | 15 | |
| Categorical Data Handling | 10 | |
| Model Training & Imbalance Handling | 20 | |
| Business Insights & Feature Importance | 15 | |
| Model Evaluation & Documentation | 5 | |
| **Subtotal** | **75** | |
| Bonus (Optional) | +10 max | |
| Code Quality Deductions | Up to -10 | |
| **TOTAL** | **75** | |

**Passing Score:** 53/75 (70%)
**Target Score:** 60/75 (80%)
**Excellence Score:** 68+/75 (90%+)

---

## Dataset Information

**Recommended Dataset:** Telco Customer Churn
- Source: IBM Sample Datasets or Kaggle
- ~7,000 customers
- 19 features (numerical + categorical)
- 26.5% churn rate (imbalanced)
- Features include: tenure, contract type, monthly charges, services subscribed

**Download:**
- Kaggle: "Telco Customer Churn"
- UCI ML Repository: Customer Churn datasets
- IBM Community: Telco Sample Data

---

## Submission Requirements

### What to Submit:
1. **Jupyter Notebook (.ipynb)** with complete pipeline
2. **Business Report** (markdown in notebook):
   - Executive summary (2-3 paragraphs)
   - Key churn drivers identified
   - Model performance metrics
   - Actionable business recommendations
   - Estimated business impact

### Pre-Submission Checklist:
- [ ] All code runs without errors
- [ ] Achieves >80% accuracy and >75% recall
- [ ] 3+ engineered features created
- [ ] All categorical variables properly encoded
- [ ] Class imbalance addressed
- [ ] 3+ algorithms compared
- [ ] Feature importance analyzed
- [ ] Business recommendations provided
- [ ] Professional visualizations

---

## Resources

### Documentation:
- [Label Encoding](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html)
- [One-Hot Encoding](https://pandas.pydata.org/docs/reference/api/pandas.get_dummies.html)
- [SMOTE](https://imbalanced-learn.org/stable/references/generated/imblearn.over_sampling.SMOTE.html)
- [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html)

### Helpful Tutorials:
- Session 2.5 Video: "Customer Churn Prediction"
- Module 2 Framework: Feature Engineering section

---

**Created:** 2026-01-06
**Version:** 1.0
**Course:** ML for Engineers - Module 2
**Last Updated:** 2026-01-06
