# Module 4: Fraud Detection Capstone Project Rubric
## Production-Quality Machine Learning System

**Total Points:** 200
**Passing Grade:** 140 points (70%)
**Excellent Grade:** 180+ points (90%)
**Version:** 1.0
**Created:** 2026-01-06

---

## Project Overview

### Objective
Build a complete fraud detection system for credit card transactions using all Module 4 optimization techniques. This is a **showcase project** that demonstrates production-ready ML skills.

### Dataset
- **Source:** Credit Card Fraud Detection (Kaggle) or synthetic equivalent
- **Size:** ~284,807 transactions
- **Features:** 30 features (Time, Amount, V1-V28 from PCA)
- **Target:** Class (0 = legitimate, 1 = fraud)
- **Imbalance:** 0.172% fraud rate (492 frauds out of 284,807)

### Why This Project Matters
This simulates a real-world high-stakes scenario where:
- False positives cost customer satisfaction
- False negatives cost money from fraud losses
- Class imbalance is severe
- Model must generalize to future fraud patterns
- Business impact must be quantified

---

## Grading Breakdown (200 Points Total)

| Category | Points | Focus |
|----------|--------|-------|
| 1. Data Preparation | 30 | Loading, EDA, feature engineering, imbalance handling |
| 2. Model Training & Comparison | 60 | Multiple algorithms, proper training, baseline comparison |
| 3. Evaluation & Metrics | 40 | Comprehensive evaluation, all Module 4 metrics |
| 4. Optimization | 35 | Cross-validation, hyperparameter tuning, feature selection |
| 5. Visualizations | 20 | 33+ professional visualizations showing insights |
| 6. Documentation & Code Quality | 10 | Clean code, markdown documentation, reproducibility |
| 7. Business Value & Recommendations | 5 | Cost-benefit analysis, deployment considerations |

---

## Category 1: Data Preparation (30 points)

### 1.1 Data Loading & Verification (8 points)

| Score | Description | Requirements Met |
|-------|-------------|------------------|
| **8 pts (Excellent)** | Professional data loading | ✓ Data loaded successfully<br>✓ Shape verified (284,807 × 31)<br>✓ Data types checked<br>✓ Date/Time feature understood<br>✓ Initial data summary provided |
| **6 pts (Good)** | Complete loading | ✓ Data loaded<br>✓ Shape verified<br>✓ Basic checking |
| **4 pts (Adequate)** | Basic loading | ✓ Data loaded<br>✓ Minimal verification |
| **0-2 pts (Poor)** | Incomplete | ✗ Loading errors or no verification |

**Evidence Required:**
```python
# Must demonstrate:
- df.shape confirmation: (284807, 31)
- df.info() showing data types
- df.describe() for all features
- Class distribution: print(df['Class'].value_counts())
- Verification of fraud rate: ~0.172%
```

---

### 1.2 Exploratory Data Analysis (12 points)

| Score | Description | Requirements Met |
|-------|-------------|------------------|
| **12 pts (Excellent)** | Comprehensive EDA | ✓ Class distribution visualized<br>✓ Feature distributions for fraud vs legitimate<br>✓ Correlation analysis (heatmap)<br>✓ Outlier detection<br>✓ Amount distribution analysis<br>✓ Time pattern analysis<br>✓ At least 5 insights documented |
| **9 pts (Good)** | Thorough EDA | ✓ Class distribution<br>✓ Feature distributions<br>✓ Correlation analysis<br>✓ 3-4 insights |
| **6 pts (Adequate)** | Basic EDA | ✓ Class distribution<br>✓ Basic feature analysis<br>✓ 1-2 insights |
| **0-3 pts (Poor)** | Minimal EDA | ✗ Incomplete or no analysis |

**Required Visualizations (at least 5 of these 8):**
1. Class distribution pie chart or bar chart
2. Amount distribution: fraud vs legitimate (histogram or boxplot)
3. Time distribution: when fraud occurs
4. Correlation heatmap for V1-V28 features
5. Feature distribution comparison (fraud vs normal) for top 5 important features
6. Outlier detection visualization
7. PCA feature importance if analyzing V1-V28
8. Class balance visualization showing severe imbalance

**Sample Insights to Document:**
- "Fraud transactions have lower average amount ($122) than legitimate ($88)"
- "Fraud occurs more frequently during certain hours (time pattern identified)"
- "Features V14, V12, V10 show strong separation between classes"
- "99.828% of transactions are legitimate - severe class imbalance"

---

### 1.3 Feature Engineering (5 points)

| Score | Description | Requirements Met |
|-------|-------------|------------------|
| **5 pts (Excellent)** | Advanced feature engineering | ✓ Amount scaling/normalization<br>✓ Time feature engineering (hour, day)<br>✓ Creates derived features (e.g., amount_per_hour)<br>✓ Documents new features created |
| **4 pts (Good)** | Good feature engineering | ✓ Amount scaling<br>✓ Time features<br>✓ Basic derived features |
| **2-3 pts (Adequate)** | Basic feature engineering | ✓ Amount scaling only or minimal engineering |
| **0-1 pts (Poor)** | No feature engineering | ✗ Uses raw features only |

**Recommended Feature Engineering:**
```python
# Amount scaling
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
df['Amount_scaled'] = scaler.fit_transform(df[['Amount']])

# Time features (if Time is seconds from first transaction)
df['Hour'] = (df['Time'] / 3600) % 24
df['Day'] = (df['Time'] / 86400).astype(int)

# Derived features
df['Amount_per_hour'] = df['Amount'] / (df['Hour'] + 1)  # Avoid div by 0
```

---

### 1.4 Handling Class Imbalance (5 points)

| Score | Description | Requirements Met |
|-------|-------------|------------------|
| **5 pts (Excellent)** | Multiple imbalance strategies | ✓ Tries SMOTE or similar oversampling<br>✓ Tries class weights<br>✓ Compares both approaches<br>✓ Selects best method with justification<br>✓ ONLY applies to training data, NOT test |
| **4 pts (Good)** | Good imbalance handling | ✓ Uses one method (SMOTE or class weights)<br>✓ Correctly applied to training only<br>✓ Basic justification |
| **2-3 pts (Adequate)** | Basic handling | ✓ Uses class weights or basic oversampling |
| **0-1 pts (Poor)** | Incorrect or none | ✗ No imbalance handling or applies to test data (CRITICAL ERROR) |

**CRITICAL RULE:** **NEVER** apply SMOTE or oversampling to test data. This would be data leakage.

**Example Implementation:**
```python
# Option 1: SMOTE (apply to X_train, y_train only)
from imblearn.over_sampling import SMOTE
smote = SMOTE(random_state=42)
X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)

# Option 2: Class weights (built into model)
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(class_weight='balanced')

# CRITICAL: Test set remains untouched!
```

---

## Category 2: Model Training & Comparison (60 points)

### 2.1 Baseline Model (10 points)

| Score | Description | Requirements Met |
|-------|-------------|------------------|
| **10 pts (Excellent)** | Professional baseline | ✓ Simple baseline model (Logistic Regression or Decision Tree)<br>✓ Trained with default parameters<br>✓ Evaluated with all metrics<br>✓ Results documented as benchmark<br>✓ Weaknesses identified |
| **8 pts (Good)** | Good baseline | ✓ Baseline model trained<br>✓ Basic evaluation<br>✓ Results documented |
| **5 pts (Adequate)** | Basic baseline | ✓ Simple model trained<br>✓ Minimal evaluation |
| **0-3 pts (Poor)** | No baseline | ✗ No baseline or incomplete |

**Purpose:** Baseline establishes minimum performance. All other models must beat this.

**Recommended Baseline:**
```python
from sklearn.linear_model import LogisticRegression
baseline = LogisticRegression(max_iter=1000, random_state=42)
baseline.fit(X_train, y_train)
y_pred_baseline = baseline.predict(X_test)

# Document performance
baseline_precision = precision_score(y_test, y_pred_baseline)
baseline_recall = recall_score(y_test, y_pred_baseline)
baseline_f1 = f1_score(y_test, y_pred_baseline)

print(f"Baseline: Precision={baseline_precision:.3f}, "
      f"Recall={baseline_recall:.3f}, F1={baseline_f1:.3f}")
```

---

### 2.2 Multiple Algorithm Implementation (30 points)

**Requirement:** Train at least 4 different algorithms

| Score | Description | Algorithms Trained |
|-------|-------------|-------------------|
| **30 pts (Excellent)** | Comprehensive comparison | ✓ Logistic Regression (baseline)<br>✓ Random Forest<br>✓ Gradient Boosting or XGBoost<br>✓ Support Vector Machine (SVM)<br>✓ At least 1 more (LightGBM, Neural Network, etc.) |
| **24 pts (Good)** | Good comparison | ✓ 4 different algorithms trained |
| **18 pts (Adequate)** | Basic comparison | ✓ 3 algorithms trained |
| **0-12 pts (Poor)** | Minimal effort | ✗ Fewer than 3 algorithms |

**For EACH Algorithm (6 points each, up to 30 total):**

| Points | Requirements Per Algorithm |
|--------|---------------------------|
| **6 pts** | ✓ Correctly implemented<br>✓ Trained on training data<br>✓ Predictions on test data<br>✓ All metrics calculated (precision, recall, F1, AUC)<br>✓ Confusion matrix generated<br>✓ ROC curve created |
| **4-5 pts** | ✓ Implemented and trained<br>✓ Basic metrics calculated<br>✓ Confusion matrix or ROC curve |
| **2-3 pts** | ✓ Implemented but incomplete evaluation |
| **0-1 pts** | ✗ Incorrect implementation or doesn't run |

**Required Algorithms:**

**1. Random Forest (6 points)**
```python
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(n_estimators=100, random_state=42,
                             class_weight='balanced')
rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)
y_proba_rf = rf.predict_proba(X_test)[:, 1]
```

**2. Gradient Boosting / XGBoost (6 points)**
```python
from xgboost import XGBClassifier
xgb = XGBClassifier(scale_pos_weight=99.828/0.172,  # Class imbalance ratio
                    random_state=42)
xgb.fit(X_train, y_train)
y_pred_xgb = xgb.predict(X_test)
y_proba_xgb = xgb.predict_proba(X_test)[:, 1]
```

**3. Support Vector Machine (6 points)**
```python
from sklearn.svm import SVC
svm = SVC(kernel='rbf', probability=True, class_weight='balanced',
          random_state=42)
svm.fit(X_train, y_train)  # May be slow on full dataset
y_pred_svm = svm.predict(X_test)
y_proba_svm = svm.predict_proba(X_test)[:, 1]
```

**4. Additional Algorithm (6 points) - Student's Choice**
Options: LightGBM, CatBoost, Neural Network, Naive Bayes, etc.

---

### 2.3 Model Comparison Table (10 points)

| Score | Description | Requirements Met |
|-------|-------------|------------------|
| **10 pts (Excellent)** | Comprehensive comparison | ✓ Table with all models<br>✓ All metrics (Accuracy, Precision, Recall, F1, AUC)<br>✓ Training time included<br>✓ Best model per metric highlighted<br>✓ Clear winner identified with justification |
| **8 pts (Good)** | Good comparison | ✓ Table with 4+ metrics<br>✓ All models included<br>✓ Winner identified |
| **5 pts (Adequate)** | Basic comparison | ✓ Table with 2-3 metrics<br>✓ All models listed |
| **0-3 pts (Poor)** | Incomplete | ✗ No comparison table or missing models |

**Example Comparison Table:**

| Model | Accuracy | Precision | Recall | F1-Score | AUC | Training Time (s) |
|-------|----------|-----------|--------|----------|-----|-------------------|
| Baseline (LogReg) | 0.9985 | 0.75 | 0.62 | 0.68 | 0.92 | 2.3 |
| Random Forest | 0.9992 | 0.88 | 0.75 | 0.81 | 0.96 | 45.2 |
| **XGBoost** | **0.9994** | **0.92** | **0.78** | **0.84** | **0.98** | 28.5 |
| SVM | 0.9990 | 0.85 | 0.71 | 0.77 | 0.95 | 180.4 |
| LightGBM | 0.9993 | 0.90 | 0.76 | 0.82 | 0.97 | 15.8 |

**Winner:** XGBoost achieves best precision (92%) and AUC (0.98) while maintaining good recall (78%). This balance is ideal for fraud detection where precision matters most.

---

### 2.4 Time-Aware Train/Test Split (10 points)

| Score | Description | Requirements Met |
|-------|-------------|------------------|
| **10 pts (Excellent)** | Correct time-aware split | ✓ Splits data chronologically (by Time column)<br>✓ Training data from earlier period<br>✓ Test data from later period<br>✓ NO random shuffling<br>✓ Explains why this matters for fraud detection<br>✓ Shows data leakage would occur with random split |
| **8 pts (Good)** | Correct split | ✓ Chronological split<br>✓ No shuffling<br>✓ Basic explanation |
| **5 pts (Adequate)** | Attempted time-aware | ✓ Some chronological consideration |
| **0-3 pts (Poor)** | Wrong split | ✗ Uses random train_test_split (data leakage!) |

**CRITICAL:** Fraud detection uses time-series data. Random splitting would train on future fraud to predict past fraud - unrealistic data leakage!

**Correct Implementation:**
```python
# Sort by time
df_sorted = df.sort_values('Time')

# Split chronologically (e.g., 80% train, 20% test)
split_idx = int(len(df_sorted) * 0.8)
train = df_sorted[:split_idx]
test = df_sorted[split_idx:]

X_train = train.drop('Class', axis=1)
y_train = train['Class']
X_test = test.drop('Class', axis=1)
y_test = test['Class']

print(f"Train time range: {train['Time'].min():.0f} to {train['Time'].max():.0f}")
print(f"Test time range: {test['Time'].min():.0f} to {test['Time'].max():.0f}")
# Verify: Test time should start AFTER train time ends
```

---

## Category 3: Evaluation & Metrics (40 points)

### 3.1 Comprehensive Metrics Calculation (15 points)

| Score | Description | Requirements Met |
|-------|-------------|------------------|
| **15 pts (Excellent)** | All metrics calculated | ✓ Accuracy<br>✓ Precision<br>✓ Recall<br>✓ F1-Score<br>✓ AUC-ROC<br>✓ Precision-Recall AUC<br>✓ All for each model<br>✓ Correctly interpreted |
| **12 pts (Good)** | Most metrics | ✓ 5 of 6 metrics for all models<br>✓ Basic interpretation |
| **8 pts (Adequate)** | Basic metrics | ✓ 3-4 metrics for all models |
| **0-5 pts (Poor)** | Minimal metrics | ✗ Fewer than 3 metrics or incomplete |

**Why Each Metric Matters:**
- **Accuracy:** Misleading for imbalanced data (99.8% by always predicting "not fraud")
- **Precision:** Critical for fraud detection - minimizes false positives (blocking legitimate transactions)
- **Recall:** Important - catch as much fraud as possible
- **F1-Score:** Balances precision and recall
- **AUC-ROC:** Model's ability to discriminate across all thresholds
- **PR-AUC:** Better than ROC for imbalanced data

---

### 3.2 Confusion Matrix Analysis (10 points)

| Score | Description | Requirements Met |
|-------|-------------|------------------|
| **10 pts (Excellent)** | Deep confusion matrix analysis | ✓ Confusion matrix for best model<br>✓ Heatmap visualization with annotations<br>✓ Calculates: TP, TN, FP, FN<br>✓ Interprets each quadrant for business<br>✓ Discusses cost of FP vs FN |
| **8 pts (Good)** | Good analysis | ✓ Confusion matrix visualized<br>✓ TP, TN, FP, FN identified<br>✓ Basic business interpretation |
| **5 pts (Adequate)** | Basic matrix | ✓ Confusion matrix created<br>✓ Minimal interpretation |
| **0-3 pts (Poor)** | Incomplete | ✗ No confusion matrix or no interpretation |

**Example Analysis:**
```
Confusion Matrix for XGBoost:
              Predicted: Not Fraud    Predicted: Fraud
Actual: Not Fraud    56,850 (TN)          12 (FP)
Actual: Fraud            22 (FN)          78 (TP)

Interpretation:
- True Negatives (56,850): Correctly identified legitimate transactions
- False Positives (12): Legitimate transactions flagged as fraud
  → Customer frustration, need manual review
- False Negatives (22): Fraud missed by model
  → Direct financial loss
- True Positives (78): Fraud correctly caught
  → Prevented fraud losses

Business Impact:
- FP Rate: 12/56,862 = 0.02% (very low customer friction)
- Recall: 78/100 = 78% (catching most fraud)
- This balance is acceptable for production
```

---

### 3.3 ROC and Precision-Recall Curves (10 points)

| Score | Description | Requirements Met |
|-------|-------------|------------------|
| **10 pts (Excellent)** | Professional curve analysis | ✓ ROC curve for all models on one plot<br>✓ Precision-Recall curve for all models<br>✓ AUC scores annotated on curves<br>✓ Diagonal reference line (ROC)<br>✓ Threshold analysis<br>✓ Discusses why PR curve better for imbalanced data |
| **8 pts (Good)** | Good curves | ✓ Both curves created<br>✓ AUC scores shown<br>✓ Basic comparison |
| **5 pts (Adequate)** | Basic curves | ✓ One curve type created<br>✓ AUC calculated |
| **0-3 pts (Poor)** | Incomplete | ✗ No curves or incorrect implementation |

**ROC Curve Code:**
```python
from sklearn.metrics import roc_curve, roc_auc_score
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 8))
for model_name, y_proba in models_proba.items():
    fpr, tpr, _ = roc_curve(y_test, y_proba)
    auc = roc_auc_score(y_test, y_proba)
    plt.plot(fpr, tpr, label=f'{model_name} (AUC={auc:.3f})')

plt.plot([0, 1], [0, 1], 'k--', label='Random (AUC=0.5)')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curves - All Models')
plt.legend()
plt.grid(True)
plt.show()
```

---

### 3.4 Cross-Validation Results (5 points)

| Score | Description | Requirements Met |
|-------|-------------|------------------|
| **5 pts (Excellent)** | Proper CV implementation | ✓ Uses TimeSeriesSplit (no data leakage!)<br>✓ 5 folds minimum<br>✓ Reports mean ± std for precision, recall, F1<br>✓ Shows consistency across folds |
| **4 pts (Good)** | Good CV | ✓ TimeSeriesSplit used<br>✓ Mean ± std reported |
| **2-3 pts (Adequate)** | Basic CV | ✓ Some form of CV attempted |
| **0-1 pts (Poor)** | Wrong CV | ✗ Uses regular K-Fold (data leakage!) or no CV |

**CRITICAL:** Must use TimeSeriesSplit for time-series data to prevent data leakage.

---

## Category 4: Optimization (35 points)

### 4.1 Hyperparameter Tuning (20 points)

| Score | Description | Requirements Met |
|-------|-------------|------------------|
| **20 pts (Excellent)** | Comprehensive tuning | ✓ Grid Search or Random Search with TimeSeriesSplit CV<br>✓ Tunes 3+ hyperparameters<br>✓ Shows parameter grid<br>✓ Reports best parameters<br>✓ Documents improvement over default<br>✓ Shows optimization history |
| **16 pts (Good)** | Good tuning | ✓ Tunes 2-3 hyperparameters with CV<br>✓ Best parameters reported<br>✓ Improvement shown |
| **10 pts (Adequate)** | Basic tuning | ✓ Tunes 1-2 hyperparameters<br>✓ Some improvement |
| **0-7 pts (Poor)** | Minimal tuning | ✗ No tuning or incorrect implementation |

**Example for XGBoost:**
```python
from sklearn.model_selection import GridSearchCV, TimeSeriesSplit

param_grid = {
    'max_depth': [3, 5, 7],
    'learning_rate': [0.01, 0.1, 0.3],
    'n_estimators': [100, 200, 300],
    'scale_pos_weight': [100, 200, 500]  # For class imbalance
}

tscv = TimeSeriesSplit(n_splits=5)

grid_search = GridSearchCV(
    XGBClassifier(random_state=42),
    param_grid,
    scoring='f1',  # Or 'precision' depending on priority
    cv=tscv,
    n_jobs=-1,
    verbose=1
)

grid_search.fit(X_train, y_train)
best_model = grid_search.best_estimator_

print(f"Best parameters: {grid_search.best_params_}")
print(f"Best CV F1 score: {grid_search.best_score_:.4f}")

# Compare to default
default_f1 = f1_score(y_test, y_pred_default)
tuned_f1 = f1_score(y_test, grid_search.predict(X_test))
print(f"Improvement: {(tuned_f1 - default_f1)*100:.1f}% increase in F1")
```

**Performance Target:** At least 5% improvement in primary metric (precision or F1)

---

### 4.2 Feature Selection (10 points)

| Score | Description | Requirements Met |
|-------|-------------|------------------|
| **10 pts (Excellent)** | Comprehensive feature selection | ✓ Feature importance analysis (bar plot of top 20)<br>✓ Removes low-importance features<br>✓ Compares full vs reduced feature set performance<br>✓ Documents speed vs accuracy tradeoff |
| **8 pts (Good)** | Good feature selection | ✓ Feature importance calculated<br>✓ Reduced feature set created<br>✓ Basic comparison |
| **5 pts (Adequate)** | Basic selection | ✓ Feature importance shown<br>✓ Minimal reduction |
| **0-3 pts (Poor)** | No selection | ✗ No feature selection performed |

**Example:**
```python
# Get feature importances from best model
importances = best_model.feature_importances_
feature_names = X_train.columns

# Create DataFrame and sort
feat_imp_df = pd.DataFrame({
    'feature': feature_names,
    'importance': importances
}).sort_values('importance', ascending=False)

# Plot top 20
plt.figure(figsize=(10, 8))
plt.barh(feat_imp_df['feature'][:20], feat_imp_df['importance'][:20])
plt.xlabel('Importance')
plt.title('Top 20 Feature Importances')
plt.gca().invert_yaxis()
plt.show()

# Select top features (e.g., top 15)
top_features = feat_imp_df['feature'][:15].tolist()
X_train_reduced = X_train[top_features]
X_test_reduced = X_test[top_features]

# Retrain and compare
model_reduced = XGBClassifier(**best_params)
model_reduced.fit(X_train_reduced, y_train)
# Compare performance and training time
```

---

### 4.3 Threshold Optimization (5 points)

| Score | Description | Requirements Met |
|-------|-------------|------------------|
| **5 pts (Excellent)** | Optimal threshold selection | ✓ Tests multiple thresholds (0.3, 0.5, 0.7, 0.9)<br>✓ Plots precision-recall vs threshold<br>✓ Selects optimal threshold for business needs<br>✓ Justifies choice (e.g., prioritize precision) |
| **4 pts (Good)** | Good threshold analysis | ✓ Tests 2-3 thresholds<br>✓ Selects one with justification |
| **2-3 pts (Adequate)** | Basic threshold work | ✓ Tests one alternative threshold |
| **0-1 pts (Poor)** | No threshold work | ✗ Uses default 0.5 only |

**Example:**
```python
thresholds = [0.3, 0.5, 0.7, 0.9]
results = []

for thresh in thresholds:
    y_pred_thresh = (y_proba_best >= thresh).astype(int)
    precision = precision_score(y_test, y_pred_thresh)
    recall = recall_score(y_test, y_pred_thresh)
    f1 = f1_score(y_test, y_pred_thresh)
    results.append({
        'threshold': thresh,
        'precision': precision,
        'recall': recall,
        'f1': f1
    })

results_df = pd.DataFrame(results)
print(results_df)

# Visualization
plt.figure(figsize=(10, 6))
plt.plot(results_df['threshold'], results_df['precision'], label='Precision', marker='o')
plt.plot(results_df['threshold'], results_df['recall'], label='Recall', marker='s')
plt.plot(results_df['threshold'], results_df['f1'], label='F1', marker='^')
plt.xlabel('Threshold')
plt.ylabel('Score')
plt.title('Metrics vs Classification Threshold')
plt.legend()
plt.grid(True)
plt.show()

# Selection: "Choose threshold=0.7 for precision=0.95, accepting recall=0.65
# because false positives are more costly in this business context"
```

---

## Category 5: Visualizations (20 points)

**Requirement:** Create at least 15 visualizations (20 points if 33+ as specified in framework)

| Score | Description | Visualizations Created |
|-------|-------------|----------------------|
| **20 pts (Excellent)** | Comprehensive visuals | ✓ 33+ professional visualizations covering all aspects<br>✓ Clear titles, labels, legends<br>✓ Insights annotated on charts<br>✓ Diverse chart types |
| **16 pts (Good)** | Many visualizations | ✓ 20-32 visualizations<br>✓ Good formatting<br>✓ Covers main topics |
| **12 pts (Adequate)** | Adequate visuals | ✓ 15-19 visualizations<br>✓ Basic formatting |
| **0-8 pts (Poor)** | Minimal visuals | ✗ Fewer than 15 visualizations or poor quality |

### Required Visualization Categories:

#### EDA Visualizations (8-10 required):
1. Class distribution (pie or bar chart)
2. Amount distribution: fraud vs legitimate
3. Time distribution of fraud
4. Correlation heatmap (V1-V28 features)
5. Top 5 feature distributions: fraud vs normal
6. Outlier detection plots
7. Feature importance from tree-based model
8. Box plots showing feature ranges
9. Scatter plot: Amount vs Time colored by class
10. Cumulative fraud over time

#### Model Evaluation Visualizations (10-12 required):
11. Confusion matrix heatmap (best model)
12. ROC curves (all models on one plot)
13. Precision-Recall curves (all models)
14. Model comparison bar chart (all metrics)
15. Training time comparison
16. Feature importance bar chart (top 20)
17. Precision/Recall/F1 vs Threshold
18. Learning curves (if applicable)
19. Cross-validation score distribution (box plot)
20. Actual vs Predicted (for probability scores)
21. False positive analysis (which transactions misclassified)
22. False negative analysis

#### Optimization Visualizations (8-10 required):
23. Hyperparameter tuning: Grid search heatmap
24. Optimization history (score over iterations)
25. Feature selection: Full vs reduced performance
26. Cross-validation fold performance
27. Threshold optimization curves
28. Precision-Recall tradeoff curve
29. Cost analysis visualization
30. Model comparison radar chart
31. Performance vs training time scatter
32. Feature correlation with target
33. (Bonus) Interactive dashboard elements

**Formatting Standards:**
- Figure size: (10, 6) minimum or appropriate for content
- Titles: Clear and descriptive
- Axis labels: Present with units
- Legends: When multiple series
- Grid: Enabled for readability
- Colors: Colorblind-friendly palette recommended
- Annotations: Key insights marked on plots

---

## Category 6: Documentation & Code Quality (10 points)

### 6.1 Code Organization (5 points)

| Score | Description | Requirements Met |
|-------|-------------|------------------|
| **5 pts (Excellent)** | Production-quality code | ✓ Well-organized notebook with clear sections<br>✓ Code cells logically ordered<br>✓ Comments for complex operations<br>✓ Functions for repeated operations<br>✓ Reproducible (set random seeds) |
| **4 pts (Good)** | Good code quality | ✓ Organized sections<br>✓ Some comments<br>✓ Mostly reproducible |
| **2-3 pts (Adequate)** | Acceptable code | ✓ Basic organization<br>✓ Minimal comments |
| **0-1 pts (Poor)** | Poor code quality | ✗ Disorganized, no comments, not reproducible |

**Required Sections:**
1. Introduction & Objectives
2. Data Loading & Verification
3. Exploratory Data Analysis
4. Data Preparation & Feature Engineering
5. Model Training & Comparison
6. Model Evaluation
7. Optimization
8. Results & Business Recommendations
9. Conclusions

---

### 6.2 Documentation & Markdown (5 points)

| Score | Description | Requirements Met |
|-------|-------------|------------------|
| **5 pts (Excellent)** | Professional documentation | ✓ Markdown cells explaining each section<br>✓ Results interpreted in context<br>✓ Insights documented throughout<br>✓ README with project overview<br>✓ Conclusions section with recommendations |
| **4 pts (Good)** | Good documentation | ✓ Markdown explanations present<br>✓ Results interpreted<br>✓ Conclusions section |
| **2-3 pts (Adequate)** | Basic documentation | ✓ Some markdown cells<br>✓ Basic explanations |
| **0-1 pts (Poor)** | Minimal documentation | ✗ Little or no markdown, code only |

**Sample Documentation Structure:**
```markdown
# 1. Introduction

## Project Objective
Build a fraud detection system for credit card transactions...

## Success Criteria
- Precision > 90% (minimize false positives)
- Recall > 70% (catch most fraud)
- AUC > 0.95 (excellent discrimination)

## Approach
- Handle severe class imbalance (0.172% fraud)
- Compare multiple algorithms
- Optimize using Module 4 techniques
- Provide business recommendations

---

# 2. Data Loading & Verification
[Code cells with results]

## Findings:
- Dataset: 284,807 transactions
- Fraud rate: 0.172% (492 fraud cases)
- 30 features (Time, Amount, V1-V28 from PCA)
- No missing values detected

---
[Continue for each section]
```

---

## Category 7: Business Value & Recommendations (5 points)

### 7.1 Cost-Benefit Analysis (3 points)

| Score | Description | Requirements Met |
|-------|-------------|------------------|
| **3 pts (Excellent)** | Comprehensive business analysis | ✓ Estimates cost of false positives (customer friction)<br>✓ Estimates cost of false negatives (fraud losses)<br>✓ Calculates total business impact<br>✓ Compares to baseline/current system<br>✓ ROI projection |
| **2 pts (Good)** | Good analysis | ✓ Cost estimates for FP and FN<br>✓ Business impact calculated |
| **1 pt (Adequate)** | Basic analysis | ✓ Acknowledges business tradeoffs |
| **0 pts (Poor)** | No analysis | ✗ No business consideration |

**Example Analysis:**
```
Assumptions:
- Average fraud transaction: $100
- Cost to manually review flagged transaction: $1
- Customer friction from false positive: $10 (in goodwill)

Current System (Baseline Logistic Regression):
- FP: 25 × $10 = $250 customer friction
- FN: 38 × $100 = $3,800 fraud losses
- Manual reviews: 25 × $1 = $25
- Total cost: $4,075

Optimized System (Tuned XGBoost):
- FP: 12 × $10 = $120 customer friction
- FN: 22 × $100 = $2,200 fraud losses
- Manual reviews: 12 × $1 = $12
- Total cost: $2,332

Savings: $1,743 per 100 fraud cases
Annual savings (projected): ~$200,000 based on transaction volume
ROI: Model development cost recovered in < 1 month
```

---

### 7.2 Deployment Recommendations (2 points)

| Score | Description | Requirements Met |
|-------|-------------|------------------|
| **2 pts (Excellent)** | Actionable recommendations | ✓ Two-tier flagging system proposed (auto-block high-confidence, manual-review medium)<br>✓ Threshold recommendations with justification<br>✓ Monitoring plan (metrics to track)<br>✓ Retraining frequency suggested<br>✓ Model drift detection strategy |
| **1 pt (Good)** | Basic recommendations | ✓ Deployment strategy outlined<br>✓ Some monitoring considerations |
| **0 pts (Poor)** | No recommendations | ✗ No deployment considerations |

**Example Recommendations:**
```
Deployment Strategy:

1. Two-Tier System:
   - Auto-block: Fraud probability > 0.90 (high confidence)
     → Prevents ~60% of fraud automatically
   - Manual review: Fraud probability 0.50-0.90 (medium confidence)
     → Human analyst reviews ~30% of flagged transactions
   - Allow: Fraud probability < 0.50 (low confidence)
     → Normal processing for >99% of transactions

2. Threshold: Use 0.70 for initial deployment
   - Balances precision (92%) and recall (78%)
   - Can adjust based on first month results

3. Monitoring Metrics:
   - Track daily: precision, recall, fraud rate
   - Alert if recall drops below 70% (fraud pattern shift)
   - Alert if FP rate exceeds 0.05% (customer friction)

4. Retraining Schedule:
   - Retrain monthly with latest fraud data
   - Fraudsters adapt tactics - model must evolve
   - Monitor for model drift weekly

5. A/B Testing:
   - Deploy to 20% of traffic initially
   - Compare to current system for 2 weeks
   - Full rollout if metrics meet targets

6. Risk Mitigation:
   - Maintain current system as fallback
   - Gradual rollout by customer segment
   - Manual override capability for analysts
```

---

## Performance Targets

### Minimum Requirements (70% = 140 points):
- ✅ Precision > 85%
- ✅ Recall > 65%
- ✅ AUC > 0.90
- ✅ At least 3 algorithms trained
- ✅ Hyperparameter tuning performed
- ✅ Time-aware cross-validation used
- ✅ 15+ visualizations
- ✅ Code runs without errors
- ✅ Basic documentation

### Excellent Performance (90% = 180 points):
- ✅ Precision > 90%
- ✅ Recall > 75%
- ✅ AUC > 0.95
- ✅ 5+ algorithms compared
- ✅ Comprehensive optimization
- ✅ 33+ professional visualizations
- ✅ Production-quality code
- ✅ Complete business analysis
- ✅ Actionable recommendations

---

## Common Mistakes to Avoid

### Critical Errors (0 points in category):
1. **Data Leakage:** Applying SMOTE to test data or using random CV on time series
2. **No Imbalance Handling:** Ignoring the 0.172% fraud rate
3. **Wrong Metrics:** Relying only on accuracy for evaluation
4. **Missing Baseline:** No comparison to show improvement
5. **Code Doesn't Run:** Notebook has errors or missing files

### Significant Issues (50% penalty):
6. **Incomplete Evaluation:** Missing key metrics (precision, recall, or AUC)
7. **No Optimization:** Default hyperparameters only
8. **Poor Documentation:** Code-only notebook with no explanations
9. **Single Algorithm:** No model comparison
10. **No Business Context:** Technical only, no business recommendations

### Minor Issues (10-20% penalty):
11. **Few Visualizations:** <15 charts when 33+ requested
12. **Basic Analysis:** Minimal insights or shallow EDA
13. **Messy Code:** Disorganized, hard to follow
14. **Incomplete Optimization:** Only one technique applied

---

## Grading Checklist

### Data Preparation (30 pts)
- [ ] Data loaded and verified (8 pts)
- [ ] Comprehensive EDA with 5+ insights (12 pts)
- [ ] Feature engineering performed (5 pts)
- [ ] Class imbalance handled correctly (5 pts)

### Model Training (60 pts)
- [ ] Baseline model established (10 pts)
- [ ] 4+ algorithms trained correctly (30 pts)
- [ ] Comparison table with all metrics (10 pts)
- [ ] Time-aware train/test split (10 pts)

### Evaluation (40 pts)
- [ ] All 6 metrics calculated (15 pts)
- [ ] Confusion matrix analysis (10 pts)
- [ ] ROC & PR curves (10 pts)
- [ ] Cross-validation with TimeSeriesSplit (5 pts)

### Optimization (35 pts)
- [ ] Hyperparameter tuning with CV (20 pts)
- [ ] Feature selection analysis (10 pts)
- [ ] Threshold optimization (5 pts)

### Visualizations (20 pts)
- [ ] 15+ visualizations minimum
- [ ] 33+ for full points
- [ ] Professional formatting
- [ ] Covers all categories (EDA, evaluation, optimization)

### Documentation (10 pts)
- [ ] Code organized and commented (5 pts)
- [ ] Markdown documentation throughout (5 pts)

### Business Value (5 pts)
- [ ] Cost-benefit analysis (3 pts)
- [ ] Deployment recommendations (2 pts)

**Total:** _____ / 200 points

**Grade:** _____ %

**Pass/Fail:** [ ] PASS (140+) [ ] NEEDS REVISION (<140)

---

## Submission Requirements

### File Format:
- **Primary:** Jupyter Notebook (.ipynb)
- **Optional:** HTML export with outputs visible

### File Naming:
`Module4-Fraud-Detection-Capstone-[YourName].ipynb`

### Required Files:
1. Main notebook with all code and results
2. README.md with project overview
3. requirements.txt with package versions (optional but recommended)

### Size Limits:
- Notebook should run in <30 minutes
- File size <50MB (use sample if full dataset too large)

### Reproducibility:
- Set random seeds: `random_state=42`
- Document package versions
- Include data source/download instructions

---

## Timeline & Milestones

**Recommended Schedule (2-3 weeks):**

### Week 1: Data & EDA
- Days 1-2: Load data, initial EDA
- Days 3-4: Feature engineering, handle imbalance
- Day 5: Complete EDA visualizations

### Week 2: Modeling & Evaluation
- Days 1-2: Train baseline + 3 additional models
- Days 3-4: Comprehensive evaluation
- Day 5: Cross-validation analysis

### Week 3: Optimization & Polish
- Days 1-2: Hyperparameter tuning
- Day 3: Feature selection
- Day 4: Visualizations and documentation
- Day 5: Business analysis and final review

---

## Support & Resources

### Getting Help:
- **Technical Issues:** Office hours, discussion forum
- **Data Issues:** Alternative synthetic dataset available
- **Compute Issues:** Reduce dataset size (random sample of 50k transactions acceptable with note)

### Reference Materials:
- Module 4 session notebooks (all techniques covered)
- sklearn documentation for metrics
- XGBoost documentation for parameters
- Imbalanced-learn documentation for SMOTE

### Example Structure:
A reference notebook structure is available showing organization and documentation standards (without solutions).

---

## Frequently Asked Questions

### Q: Can I use a subset of the data due to compute limits?
**A:** Yes, but document this. Random sample of 50,000 transactions is acceptable. Maintain fraud rate (~0.172%) when sampling.

### Q: What if my precision/recall don't meet targets?
**A:** Document why. Some datasets are inherently harder. Full credit if methodology is correct and you explain challenges. Target is improvement over baseline, not absolute numbers.

### Q: Can I use algorithms not covered in the course?
**A:** Yes! Trying new algorithms (LightGBM, CatBoost, Neural Networks) can earn bonus points if properly implemented and documented.

### Q: How important are the 33+ visualizations?
**A:** Quality > quantity. 20 excellent visualizations better than 35 basic charts. Aim for comprehensive coverage of: EDA, model comparison, and optimization process.

### Q: Should I include failed experiments?
**A:** Yes! Professional ML work includes experiments that don't work. Document what you tried and why it didn't help. Shows thorough investigation.

### Q: What if Grid Search takes too long?
**A:** Use Random Search with fewer iterations. Or reduce parameter grid size. Document computational constraints. Full credit if approach is correct.

---

## Final Notes

This capstone integrates **all Module 4 skills**:
- ✅ Session 4.1: Classification metrics (precision, recall, F1, ROC)
- ✅ Session 4.2: Not applicable (regression metrics)
- ✅ Session 4.3: Cross-validation (TimeSeriesSplit critical!)
- ✅ Session 4.4: Overfitting diagnosis (learning curves if used)
- ✅ Session 4.5: Hyperparameter tuning (Grid/Random Search)
- ✅ Session 4.6: Feature selection (importance analysis)

**Success Strategy:**
1. Start early - this is a 20-30 hour project
2. Follow the structure in this rubric
3. Focus on methodology correctness over perfect results
4. Document everything - show your thinking
5. Ask for help when stuck - this is challenging work!

**Remember:** In real ML work, 90% of effort is data preparation and evaluation. Only 10% is model training. This project reflects that reality.

---

**Version:** 1.0
**Created:** 2026-01-06
**Module:** 4 - Model Evaluation & Optimization
**Points:** 200 (separate from session points)
**Weight:** Major capstone project demonstrating Module 4 mastery
