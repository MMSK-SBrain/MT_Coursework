# Week 2: Implementation Guide

## Overview

**Duration:** 18-22 hours across 3 sessions
**Goal:** Build, optimize, and deploy your ML system
**Mindset:** "Ship working code, iterate to improve" - Done is better than perfect!

---

## Week 2 Philosophy

This week is about **execution**. You have your plan from Week 1 - now it's time to build!

**Key Principles:**
- Start with baseline, iterate to excellence
- Deploy early, debug early
- Test continuously
- Document as you code
- Ask for help when stuck > 30 minutes

---

## Session 4: Model Development (6-8 hours)

### Goals
- Build data preprocessing pipeline
- Train multiple ML models
- Compare performance
- Select best model(s)
- Achieve target metrics

---

### Step 1: Environment Setup (30 minutes)

**Create clean development environment:**

```bash
# Create project structure (if not done)
mkdir -p data/{raw,processed}
mkdir -p notebooks models src/{data,features,models,utils} deployment tests docs

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install pandas numpy scikit-learn matplotlib seaborn jupyter

# Create requirements.txt
pip freeze > requirements.txt

# Initialize Git (if not done)
git init
git add .
git commit -m "Initial project structure"
```

**`.gitignore`:**
```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
ENV/

# Jupyter
.ipynb_checkpoints

# Data (large files)
data/raw/*
data/processed/*
!data/raw/.gitkeep
!data/processed/.gitkeep

# Models
models/*.pkl
models/*.h5
models/*.pt

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Secrets
.env
config.ini
credentials.json
```

---

### Step 2: Data Preprocessing Pipeline (90-120 minutes)

**Create:** `notebooks/02_preprocessing.ipynb`

**Build systematic preprocessing:**

#### A. Load Data

```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# Load raw data
df = pd.read_csv('data/raw/your_data.csv')
print(f"Original shape: {df.shape}")
```

#### B. Handle Missing Values

```python
# Strategy depends on your data (from EDA)

# Option 1: Drop rows with missing values
df_clean = df.dropna()

# Option 2: Drop columns with too many missing
threshold = 0.5  # Drop if > 50% missing
df_clean = df.dropna(thresh=len(df) * threshold, axis=1)

# Option 3: Impute missing values
from sklearn.impute import SimpleImputer

# Numerical: mean, median, or most frequent
imputer_num = SimpleImputer(strategy='median')
df[numerical_cols] = imputer_num.fit_transform(df[numerical_cols])

# Categorical: most frequent or constant
imputer_cat = SimpleImputer(strategy='most_frequent')
df[categorical_cols] = imputer_cat.fit_transform(df[categorical_cols])

print(f"After handling missing: {df.shape}")
print(f"Remaining missing: {df.isnull().sum().sum()}")
```

#### C. Handle Outliers

```python
# Option 1: Remove extreme outliers (use IQR method)
def remove_outliers(df, column, factor=1.5):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - factor * IQR
    upper_bound = Q3 + factor * IQR
    return df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]

# Option 2: Cap outliers (winsorization)
def cap_outliers(df, column, lower_percentile=1, upper_percentile=99):
    lower = df[column].quantile(lower_percentile / 100)
    upper = df[column].quantile(upper_percentile / 100)
    df[column] = df[column].clip(lower, upper)
    return df

# Apply to specific columns
for col in ['price', 'volume']:
    df = cap_outliers(df, col)

print(f"After outlier handling: {df.shape}")
```

#### D. Feature Engineering

```python
# Apply techniques learned in the course!

# Time-based features (if datetime column)
if 'date' in df.columns:
    df['date'] = pd.to_datetime(df['date'])
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df['day_of_week'] = df['date'].dt.dayofweek
    df['quarter'] = df['date'].dt.quarter

# Domain-specific features (examples)
# Stock data:
df['price_change'] = df['close'] - df['open']
df['price_range'] = df['high'] - df['low']
df['return'] = df['close'].pct_change()

# Rolling statistics
df['ma_7'] = df['close'].rolling(window=7).mean()
df['ma_30'] = df['close'].rolling(window=30).mean()
df['volatility_7'] = df['close'].rolling(window=7).std()

# Interaction features
df['feature_interaction'] = df['feature1'] * df['feature2']

# Polynomial features (use carefully!)
from sklearn.preprocessing import PolynomialFeatures
# poly = PolynomialFeatures(degree=2, include_bias=False)
# poly_features = poly.fit_transform(df[['feature1', 'feature2']])

print(f"After feature engineering: {df.shape}")
print(f"New features: {df.columns.tolist()}")
```

#### E. Encode Categorical Variables

```python
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

# Label Encoding (for ordinal categorical)
le = LabelEncoder()
df['category_encoded'] = le.fit_transform(df['category'])

# One-Hot Encoding (for nominal categorical)
df = pd.get_dummies(df, columns=['categorical_col'], drop_first=True)

# Or use sklearn OneHotEncoder for more control
from sklearn.preprocessing import OneHotEncoder
ohe = OneHotEncoder(sparse=False, drop='first')
encoded = ohe.fit_transform(df[['categorical_col']])
encoded_df = pd.DataFrame(encoded, columns=ohe.get_feature_names_out())
df = pd.concat([df, encoded_df], axis=1)

print(f"After encoding: {df.shape}")
```

#### F. Feature Scaling

```python
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler

# Choose based on your data distribution

# StandardScaler: mean=0, std=1 (assumes normal distribution)
scaler = StandardScaler()

# MinMaxScaler: scales to [0, 1] range
# scaler = MinMaxScaler()

# RobustScaler: robust to outliers (uses median, IQR)
# scaler = RobustScaler()

# Fit on training data only (don't fit on test!)
# We'll do this after train/test split
```

#### G. Train/Test Split

```python
# Define features and target
X = df.drop(['target', 'date', 'id'], axis=1)  # Remove target and non-feature cols
y = df['target']

# Split strategies

# Option 1: Random split (for most cases)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y  # stratify for classification
)

# Option 2: Time-based split (for time series)
# train_size = int(len(df) * 0.8)
# X_train, X_test = X[:train_size], X[train_size:]
# y_train, y_test = y[:train_size], y[train_size:]

print(f"Training set: {X_train.shape}")
print(f"Test set: {X_test.shape}")
print(f"Target distribution (train): {y_train.value_counts()}")
```

#### H. Apply Scaling

```python
# Fit scaler on training data only
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)  # Use same scaler!

# Convert back to DataFrame (optional, for readability)
X_train_scaled = pd.DataFrame(X_train_scaled, columns=X_train.columns)
X_test_scaled = pd.DataFrame(X_test_scaled, columns=X_test.columns)
```

#### I. Save Processed Data

```python
# Save for modeling
X_train_scaled.to_csv('data/processed/X_train.csv', index=False)
X_test_scaled.to_csv('data/processed/X_test.csv', index=False)
y_train.to_csv('data/processed/y_train.csv', index=False)
y_test.to_csv('data/processed/y_test.csv', index=False)

# Save preprocessor objects
import joblib
joblib.dump(scaler, 'models/scaler.pkl')
joblib.dump(imputer_num, 'models/imputer_num.pkl')
# Save any other transformers

print("Preprocessing complete! Data saved.")
```

---

### Step 3: Baseline Model (60-90 minutes)

**Create:** `notebooks/03_modeling.ipynb`

**Always start simple!**

```python
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import matplotlib.pyplot as plt
import seaborn as sns

# Load processed data
X_train = pd.read_csv('data/processed/X_train.csv')
X_test = pd.read_csv('data/processed/X_test.csv')
y_train = pd.read_csv('data/processed/y_train.csv').values.ravel()
y_test = pd.read_csv('data/processed/y_test.csv').values.ravel()

print(f"Training set: {X_train.shape}")
print(f"Test set: {X_test.shape}")
```

#### For Classification:

```python
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Train baseline model
baseline = LogisticRegression(random_state=42, max_iter=1000)
baseline.fit(X_train, y_train)

# Predictions
y_pred_train = baseline.predict(X_train)
y_pred_test = baseline.predict(X_test)

# Evaluation
print("Baseline Model (Logistic Regression)")
print(f"Training Accuracy: {accuracy_score(y_train, y_pred_train):.4f}")
print(f"Test Accuracy: {accuracy_score(y_test, y_pred_test):.4f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred_test))

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred_test)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title('Baseline Model - Confusion Matrix')
plt.ylabel('True Label')
plt.xlabel('Predicted Label')
plt.show()
```

#### For Regression:

```python
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

# Train baseline model
baseline = LinearRegression()
baseline.fit(X_train, y_train)

# Predictions
y_pred_train = baseline.predict(X_train)
y_pred_test = baseline.predict(X_test)

# Evaluation
print("Baseline Model (Linear Regression)")
print(f"Training R²: {r2_score(y_train, y_pred_train):.4f}")
print(f"Test R²: {r2_score(y_test, y_pred_test):.4f}")
print(f"Test RMSE: {np.sqrt(mean_squared_error(y_test, y_pred_test)):.4f}")
print(f"Test MAE: {mean_absolute_error(y_test, y_pred_test):.4f}")

# Residuals plot
residuals = y_test - y_pred_test
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.scatter(y_pred_test, residuals, alpha=0.5)
plt.axhline(y=0, color='r', linestyle='--')
plt.xlabel('Predicted Values')
plt.ylabel('Residuals')
plt.title('Residual Plot')

plt.subplot(1, 2, 2)
plt.scatter(y_test, y_pred_test, alpha=0.5)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
plt.xlabel('True Values')
plt.ylabel('Predicted Values')
plt.title('Predictions vs True Values')
plt.tight_layout()
plt.show()
```

**Baseline establishes minimum acceptable performance!**

---

### Step 4: Advanced Models (120-180 minutes)

**Try at least 3 different algorithms:**

```python
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from xgboost import XGBClassifier
from sklearn.neural_network import MLPClassifier

# Dictionary to store results
results = {}

# Model 1: Random Forest
print("\n" + "="*50)
print("Training Random Forest...")
rf = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)
acc_rf = accuracy_score(y_test, y_pred_rf)
results['Random Forest'] = acc_rf
print(f"Random Forest Test Accuracy: {acc_rf:.4f}")

# Model 2: Gradient Boosting
print("\n" + "="*50)
print("Training Gradient Boosting...")
gb = GradientBoostingClassifier(n_estimators=100, random_state=42)
gb.fit(X_train, y_train)
y_pred_gb = gb.predict(X_test)
acc_gb = accuracy_score(y_test, y_pred_gb)
results['Gradient Boosting'] = acc_gb
print(f"Gradient Boosting Test Accuracy: {acc_gb:.4f}")

# Model 3: XGBoost
print("\n" + "="*50)
print("Training XGBoost...")
xgb = XGBClassifier(n_estimators=100, random_state=42, use_label_encoder=False, eval_metric='logloss')
xgb.fit(X_train, y_train)
y_pred_xgb = xgb.predict(X_test)
acc_xgb = accuracy_score(y_test, y_pred_xgb)
results['XGBoost'] = acc_xgb
print(f"XGBoost Test Accuracy: {acc_xgb:.4f}")

# Model 4: Neural Network (optional)
print("\n" + "="*50)
print("Training Neural Network...")
nn = MLPClassifier(hidden_layer_sizes=(100, 50), max_iter=500, random_state=42)
nn.fit(X_train, y_train)
y_pred_nn = nn.predict(X_test)
acc_nn = accuracy_score(y_test, y_pred_nn)
results['Neural Network'] = acc_nn
print(f"Neural Network Test Accuracy: {acc_nn:.4f}")

# Compare all models
print("\n" + "="*50)
print("MODEL COMPARISON")
print("="*50)
results_df = pd.DataFrame(list(results.items()), columns=['Model', 'Test Accuracy'])
results_df = results_df.sort_values('Test Accuracy', ascending=False)
print(results_df.to_string(index=False))

# Visualization
plt.figure(figsize=(10, 6))
plt.barh(results_df['Model'], results_df['Test Accuracy'])
plt.xlabel('Test Accuracy')
plt.title('Model Comparison')
plt.xlim([0, 1])
for i, v in enumerate(results_df['Test Accuracy']):
    plt.text(v + 0.01, i, f'{v:.4f}', va='center')
plt.tight_layout()
plt.show()
```

---

### Step 5: Feature Importance Analysis (30 minutes)

**Understand what drives predictions:**

```python
# For tree-based models (RF, GB, XGB)
feature_importance = rf.feature_importances_
feature_names = X_train.columns

# Create DataFrame
importance_df = pd.DataFrame({
    'Feature': feature_names,
    'Importance': feature_importance
}).sort_values('Importance', ascending=False)

print("Top 10 Most Important Features:")
print(importance_df.head(10))

# Visualization
plt.figure(figsize=(10, 8))
plt.barh(importance_df['Feature'].head(15), importance_df['Importance'].head(15))
plt.xlabel('Importance')
plt.title('Top 15 Feature Importances')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()
```

---

### Step 6: Select Best Model (20 minutes)

**Decision criteria:**
- Test performance (primary)
- Training time
- Inference speed
- Interpretability needs
- Deployment constraints

```python
# Select best model
best_model_name = results_df.iloc[0]['Model']
print(f"\nBest Model: {best_model_name}")

# Save best model
if best_model_name == 'Random Forest':
    best_model = rf
elif best_model_name == 'XGBoost':
    best_model = xgb
elif best_model_name == 'Gradient Boosting':
    best_model = gb
else:
    best_model = nn

# Save model
import joblib
joblib.dump(best_model, 'models/best_model_v1.pkl')
print("Best model saved as 'models/best_model_v1.pkl'")

# Save model metadata
import json
metadata = {
    'model_name': best_model_name,
    'test_accuracy': float(results_df.iloc[0]['Test Accuracy']),
    'training_date': str(pd.Timestamp.now()),
    'features': X_train.columns.tolist(),
    'n_samples_train': len(X_train),
    'n_samples_test': len(X_test)
}

with open('models/model_metadata_v1.json', 'w') as f:
    json.dump(metadata, f, indent=2)
print("Model metadata saved")
```

---

## Session 5: Optimization & Testing (4-6 hours)

### Goals
- Hyperparameter tuning
- Error analysis
- Improve model performance
- Handle edge cases
- Validate robustness

---

### Step 1: Hyperparameter Tuning (90-120 minutes)

**Use Grid Search or Random Search:**

```python
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier

# Define parameter grid
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [10, 20, 30, None],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'max_features': ['auto', 'sqrt', 'log2']
}

# Grid Search (exhaustive but slow)
grid_search = GridSearchCV(
    RandomForestClassifier(random_state=42),
    param_grid,
    cv=5,
    scoring='accuracy',
    n_jobs=-1,
    verbose=2
)

# Or Random Search (faster, often as good)
from scipy.stats import randint
random_search = RandomizedSearchCV(
    RandomForestClassifier(random_state=42),
    param_distributions={
        'n_estimators': randint(100, 500),
        'max_depth': [10, 20, 30, 40, None],
        'min_samples_split': randint(2, 20),
        'min_samples_leaf': randint(1, 10),
    },
    n_iter=50,
    cv=5,
    scoring='accuracy',
    n_jobs=-1,
    verbose=2,
    random_state=42
)

print("Starting hyperparameter tuning...")
random_search.fit(X_train, y_train)

print(f"\nBest parameters: {random_search.best_params_}")
print(f"Best CV score: {random_search.best_score_:.4f}")

# Evaluate tuned model
best_tuned_model = random_search.best_estimator_
y_pred_tuned = best_tuned_model.predict(X_test)
acc_tuned = accuracy_score(y_test, y_pred_tuned)
print(f"Tuned model test accuracy: {acc_tuned:.4f}")

# Compare to original
print(f"Original model test accuracy: {acc_rf:.4f}")
print(f"Improvement: {(acc_tuned - acc_rf):.4f} ({(acc_tuned - acc_rf)/acc_rf*100:.2f}%)")
```

---

### Step 2: Error Analysis (60-90 minutes)

**Understand where model fails:**

```python
# Get predictions and probabilities
y_pred = best_tuned_model.predict(X_test)
y_proba = best_tuned_model.predict_proba(X_test)

# Create results DataFrame
results_df = pd.DataFrame({
    'True': y_test,
    'Predicted': y_pred,
    'Correct': y_test == y_pred,
    'Confidence': y_proba.max(axis=1)
})

# Add original features for analysis
results_df = pd.concat([results_df, X_test.reset_index(drop=True)], axis=1)

print("Error Analysis")
print("="*50)
print(f"Total samples: {len(results_df)}")
print(f"Correct predictions: {results_df['Correct'].sum()} ({results_df['Correct'].mean()*100:.2f}%)")
print(f"Incorrect predictions: {(~results_df['Correct']).sum()} ({(~results_df['Correct']).mean()*100:.2f}%)")

# Analyze incorrect predictions
incorrect = results_df[~results_df['Correct']]
print(f"\nIncorrect Predictions Analysis:")
print(f"Average confidence on errors: {incorrect['Confidence'].mean():.4f}")
print(f"Min confidence on errors: {incorrect['Confidence'].min():.4f}")
print(f"Max confidence on errors: {incorrect['Confidence'].max():.4f}")

# Low confidence predictions (might be uncertain)
low_confidence = results_df[results_df['Confidence'] < 0.6]
print(f"\nLow confidence predictions (< 0.6): {len(low_confidence)}")
print(f"Accuracy on low confidence: {low_confidence['Correct'].mean():.4f}")

# Analyze by class
for class_label in results_df['True'].unique():
    class_data = results_df[results_df['True'] == class_label]
    class_acc = class_data['Correct'].mean()
    print(f"\nClass {class_label}:")
    print(f"  Samples: {len(class_data)}")
    print(f"  Accuracy: {class_acc:.4f}")
    print(f"  Avg Confidence: {class_data['Confidence'].mean():.4f}")

# Visualize errors
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
results_df.groupby('True')['Correct'].mean().plot(kind='bar')
plt.title('Accuracy by Class')
plt.ylabel('Accuracy')
plt.xlabel('Class')
plt.ylim([0, 1])

plt.subplot(1, 2, 2)
plt.hist([results_df[results_df['Correct']]['Confidence'],
          results_df[~results_df['Correct']]['Confidence']],
         bins=20, label=['Correct', 'Incorrect'], alpha=0.7)
plt.xlabel('Confidence')
plt.ylabel('Count')
plt.title('Confidence Distribution')
plt.legend()
plt.tight_layout()
plt.show()

# Sample of worst predictions (lowest confidence errors)
worst_predictions = incorrect.nsmallest(10, 'Confidence')
print("\nWorst 10 Predictions:")
print(worst_predictions[['True', 'Predicted', 'Confidence']].to_string())
```

---

### Step 3: Cross-Validation (30 minutes)

**Ensure model generalizes:**

```python
from sklearn.model_selection import cross_val_score, cross_validate

# K-fold cross-validation
cv_scores = cross_val_score(best_tuned_model, X_train, y_train, cv=5, scoring='accuracy')

print("5-Fold Cross-Validation Results:")
print(f"Scores: {cv_scores}")
print(f"Mean: {cv_scores.mean():.4f}")
print(f"Std Dev: {cv_scores.std():.4f}")
print(f"Range: [{cv_scores.min():.4f}, {cv_scores.max():.4f}]")

# Get more metrics
scoring = ['accuracy', 'precision_macro', 'recall_macro', 'f1_macro']
cv_results = cross_validate(best_tuned_model, X_train, y_train, cv=5, scoring=scoring)

print("\nDetailed Cross-Validation:")
for metric in scoring:
    scores = cv_results[f'test_{metric}']
    print(f"{metric.capitalize()}: {scores.mean():.4f} (+/- {scores.std():.4f})")
```

---

### Step 4: Edge Case Testing (45-60 minutes)

**Test robustness:**

```python
# Test Case 1: Missing values in new data
print("Test 1: Handling missing values")
X_test_missing = X_test.copy()
X_test_missing.iloc[0, 0] = np.nan
try:
    pred_missing = best_tuned_model.predict(X_test_missing.fillna(X_test_missing.median()))
    print("✓ Handles missing values")
except Exception as e:
    print(f"✗ Error with missing values: {e}")

# Test Case 2: Out-of-range values
print("\nTest 2: Out-of-range values")
X_test_extreme = X_test.copy()
X_test_extreme.iloc[0, 0] = X_test_extreme.iloc[:, 0].max() * 10
try:
    pred_extreme = best_tuned_model.predict(X_test_extreme)
    print("✓ Handles extreme values")
except Exception as e:
    print(f"✗ Error with extreme values: {e}")

# Test Case 3: Single sample prediction
print("\nTest 3: Single sample prediction")
try:
    single_sample = X_test.iloc[0:1]
    pred_single = best_tuned_model.predict(single_sample)
    proba_single = best_tuned_model.predict_proba(single_sample)
    print(f"✓ Single prediction works: {pred_single[0]} (confidence: {proba_single.max():.4f})")
except Exception as e:
    print(f"✗ Error with single sample: {e}")

# Test Case 4: Batch prediction speed
print("\nTest 4: Prediction speed")
import time
start = time.time()
preds = best_tuned_model.predict(X_test)
end = time.time()
time_per_sample = (end - start) / len(X_test) * 1000
print(f"✓ Speed: {time_per_sample:.4f} ms per sample")
print(f"  Total time for {len(X_test)} samples: {end - start:.4f} seconds")
```

---

### Step 5: Final Model Save (20 minutes)

**Save optimized model:**

```python
import joblib
import json
from datetime import datetime

# Save tuned model
joblib.dump(best_tuned_model, 'models/final_model_v1.pkl')
print("Final model saved: models/final_model_v1.pkl")

# Save complete preprocessing pipeline
preprocessing_pipeline = {
    'scaler': scaler,
    'imputer_num': imputer_num,
    # Add any other preprocessors
}
joblib.dump(preprocessing_pipeline, 'models/preprocessing_pipeline_v1.pkl')
print("Preprocessing pipeline saved")

# Comprehensive metadata
final_metadata = {
    'model': {
        'name': type(best_tuned_model).__name__,
        'version': '1.0',
        'created_date': datetime.now().isoformat(),
        'hyperparameters': best_tuned_model.get_params()
    },
    'performance': {
        'test_accuracy': float(acc_tuned),
        'cv_accuracy_mean': float(cv_scores.mean()),
        'cv_accuracy_std': float(cv_scores.std()),
    },
    'data': {
        'n_features': len(X_train.columns),
        'features': X_train.columns.tolist(),
        'n_train_samples': len(X_train),
        'n_test_samples': len(X_test),
        'target_classes': list(map(int, np.unique(y_train)))
    },
    'preprocessing': {
        'scaler': type(scaler).__name__,
        'imputation': 'median for numerical features',
    }
}

with open('models/final_model_metadata_v1.json', 'w') as f:
    json.dump(final_metadata, f, indent=2)
print("Metadata saved")

print("\n" + "="*50)
print("MODEL READY FOR DEPLOYMENT!")
print("="*50)
```

---

## Session 6: Deployment (6-8 hours)

### Goals
- Build Flask/FastAPI API
- Create Streamlit UI
- Deploy to cloud
- Test end-to-end
- Obtain public URLs

---

### Step 1: Create API (120-180 minutes)

**Create:** `deployment/api/app.py`

```python
from flask import Flask, request, jsonify
import joblib
import numpy as np
import pandas as pd
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)

# Load model and preprocessors at startup
print("Loading model and preprocessors...")
model = joblib.load('../../models/final_model_v1.pkl')
preprocessing = joblib.load('../../models/preprocessing_pipeline_v1.pkl')
scaler = preprocessing['scaler']

print("Model loaded successfully!")

# Load metadata
import json
with open('../../models/final_model_metadata_v1.json', 'r') as f:
    metadata = json.load(f)

@app.route('/')
def home():
    """Home endpoint"""
    return jsonify({
        'message': 'ML Model API',
        'version': metadata['model']['version'],
        'endpoints': ['/health', '/predict', '/model/info']
    })

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat()
    })

@app.route('/model/info', methods=['GET'])
def model_info():
    """Get model information"""
    return jsonify(metadata)

@app.route('/predict', methods=['POST'])
def predict():
    """
    Make prediction

    Expected JSON format:
    {
        "features": {
            "feature1": value1,
            "feature2": value2,
            ...
        }
    }
    """
    try:
        # Get JSON data
        data = request.get_json()

        if not data or 'features' not in data:
            return jsonify({
                'error': 'No features provided',
                'format': 'Expected {"features": {...}}'
            }), 400

        # Convert to DataFrame
        features_dict = data['features']
        features_df = pd.DataFrame([features_dict])

        # Validate features
        expected_features = metadata['data']['features']
        if list(features_df.columns) != expected_features:
            return jsonify({
                'error': 'Invalid features',
                'expected': expected_features,
                'received': list(features_df.columns)
            }), 400

        # Preprocess
        features_scaled = scaler.transform(features_df)

        # Predict
        prediction = model.predict(features_scaled)[0]
        probability = model.predict_proba(features_scaled)[0]
        confidence = float(probability.max())

        # Response
        return jsonify({
            'prediction': int(prediction),
            'confidence': confidence,
            'probabilities': probability.tolist(),
            'timestamp': datetime.now().isoformat()
        })

    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```

**Create:** `deployment/api/requirements.txt`
```
flask==2.3.0
scikit-learn==1.3.0
numpy==1.24.0
pandas==2.0.0
joblib==1.3.0
gunicorn==21.2.0
```

**Create:** `deployment/api/Procfile`
```
web: gunicorn app:app
```

**Test locally:**
```bash
cd deployment/api
pip install -r requirements.txt
python app.py

# In another terminal, test:
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"features": {"feature1": 1.0, "feature2": 2.0, ...}}'
```

---

### Step 2: Create Streamlit UI (90-120 minutes)

**Create:** `deployment/ui/streamlit_app.py`

```python
import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import json

# Page config
st.set_page_config(
    page_title="ML Prediction App",
    page_icon="🤖",
    layout="wide"
)

# API URL (update after deployment)
API_URL = "http://localhost:5000"  # Local testing
# API_URL = "https://your-api.herokuapp.com"  # After deployment

# Title and description
st.title("🤖 ML Prediction Application")
st.markdown("""
This application uses machine learning to predict [YOUR TASK].
Enter the required information below to get a prediction.
""")

# Sidebar for navigation
page = st.sidebar.radio("Navigate", ["Prediction", "Model Info", "About"])

if page == "Prediction":
    st.header("Make a Prediction")

    # Input form
    with st.form("prediction_form"):
        st.subheader("Enter Features:")

        # Create input fields for each feature
        # Replace with your actual features
        feature1 = st.number_input("Feature 1", value=0.0)
        feature2 = st.number_input("Feature 2", value=0.0)
        feature3 = st.selectbox("Feature 3", ["Option 1", "Option 2", "Option 3"])
        # Add more features as needed

        submitted = st.form_submit_button("Predict")

    if submitted:
        # Prepare data
        features = {
            "feature1": feature1,
            "feature2": feature2,
            "feature3": feature3,
            # Add more features
        }

        # Make API request
        with st.spinner("Making prediction..."):
            try:
                response = requests.post(
                    f"{API_URL}/predict",
                    json={"features": features},
                    timeout=10
                )

                if response.status_code == 200:
                    result = response.json()

                    # Display results
                    st.success("Prediction completed!")

                    col1, col2 = st.columns(2)
                    with col1:
                        st.metric("Prediction", result['prediction'])
                    with col2:
                        st.metric("Confidence", f"{result['confidence']*100:.2f}%")

                    # Probability chart
                    if 'probabilities' in result:
                        prob_df = pd.DataFrame({
                            'Class': range(len(result['probabilities'])),
                            'Probability': result['probabilities']
                        })
                        fig = px.bar(prob_df, x='Class', y='Probability',
                                    title='Prediction Probabilities')
                        st.plotly_chart(fig)

                    # Show full response
                    with st.expander("View full response"):
                        st.json(result)
                else:
                    st.error(f"Error: {response.json().get('error', 'Unknown error')}")

            except requests.exceptions.RequestException as e:
                st.error(f"Could not connect to API: {e}")

elif page == "Model Info":
    st.header("Model Information")

    try:
        response = requests.get(f"{API_URL}/model/info")
        if response.status_code == 200:
            info = response.json()

            st.subheader("Model Details")
            st.write(f"**Name:** {info['model']['name']}")
            st.write(f"**Version:** {info['model']['version']}")
            st.write(f"**Created:** {info['model']['created_date']}")

            st.subheader("Performance Metrics")
            st.write(f"**Test Accuracy:** {info['performance']['test_accuracy']:.4f}")
            st.write(f"**CV Accuracy:** {info['performance']['cv_accuracy_mean']:.4f} ± {info['performance']['cv_accuracy_std']:.4f}")

            st.subheader("Data Information")
            st.write(f"**Number of Features:** {info['data']['n_features']}")
            st.write(f"**Training Samples:** {info['data']['n_train_samples']}")

            with st.expander("View all features"):
                st.write(info['data']['features'])

    except requests.exceptions.RequestException as e:
        st.error(f"Could not fetch model info: {e}")

elif page == "About":
    st.header("About This Project")
    st.markdown("""
    ### Project Description
    [Describe your project here]

    ### How It Works
    1. User enters feature values
    2. Data is sent to ML API
    3. Model makes prediction
    4. Results are displayed

    ### Technologies Used
    - **ML Framework:** scikit-learn
    - **API:** Flask
    - **UI:** Streamlit
    - **Deployment:** Heroku + Streamlit Cloud

    ### Contact
    - GitHub: [your-github]
    - LinkedIn: [your-linkedin]
    - Email: [your-email]
    """)
```

**Create:** `deployment/ui/requirements.txt`
```
streamlit==1.28.0
requests==2.31.0
pandas==2.0.0
plotly==5.17.0
```

**Test locally:**
```bash
cd deployment/ui
pip install -r requirements.txt
streamlit run streamlit_app.py
```

---

### Step 3: Deploy API to Heroku (60-90 minutes)

**Prerequisites:**
- Heroku account created
- Heroku CLI installed

**Steps:**

```bash
# Navigate to API directory
cd deployment/api

# Copy model files to API directory
cp ../../models/*.pkl .
cp ../../models/*.json .

# Initialize git (if not already)
git init

# Create .gitignore
echo "*.pkl" >> .gitignore
echo "__pycache__/" >> .gitignore
echo "venv/" >> .gitignore

# Login to Heroku
heroku login

# Create Heroku app
heroku create your-ml-api

# Add Python buildpack
heroku buildpacks:set heroku/python

# Deploy
git add .
git commit -m "Initial API deployment"
git push heroku main

# Check logs
heroku logs --tail

# Test deployed API
curl https://your-ml-api.herokuapp.com/health
```

**Get your API URL:** `https://your-ml-api.herokuapp.com`

---

### Step 4: Deploy UI to Streamlit Cloud (30-45 minutes)

**Steps:**

1. **Push code to GitHub:**
```bash
cd deployment/ui
git add .
git commit -m "Streamlit UI for deployment"
git push origin main
```

2. **Deploy on Streamlit Cloud:**
- Go to share.streamlit.io
- Click "New app"
- Select your GitHub repo
- Set main file path: `deployment/ui/streamlit_app.py`
- Click "Deploy"

3. **Update API URL in streamlit_app.py:**
```python
API_URL = "https://your-ml-api.herokuapp.com"
```

4. **Get your UI URL:** `https://your-app.streamlit.app`

---

### Step 5: End-to-End Testing (30-45 minutes)

**Test complete workflow:**

1. **Test API directly:**
```bash
curl -X GET https://your-ml-api.herokuapp.com/health
curl -X GET https://your-ml-api.herokuapp.com/model/info
curl -X POST https://your-ml-api.herokuapp.com/predict \
  -H "Content-Type: application/json" \
  -d '{"features": {...}}'
```

2. **Test UI:**
- Visit your Streamlit app URL
- Navigate through all pages
- Make test predictions
- Verify results display correctly

3. **Integration test:**
- UI → API → Model → Response → UI display
- Test with various inputs
- Test edge cases
- Verify error handling

4. **Document URLs:**
```markdown
## Deployed Application

- **API:** https://your-ml-api.herokuapp.com
- **UI:** https://your-app.streamlit.app
- **GitHub:** https://github.com/yourusername/your-repo
```

---

## Week 2 Deliverables Checklist

### Session 4: Model Development ✓
- [ ] Preprocessing pipeline complete
- [ ] Baseline model trained
- [ ] 3+ advanced models trained
- [ ] Models compared systematically
- [ ] Best model selected and saved
- [ ] Feature importance analyzed
- [ ] Model metadata saved

### Session 5: Optimization ✓
- [ ] Hyperparameter tuning complete
- [ ] Error analysis performed
- [ ] Cross-validation done
- [ ] Edge cases tested
- [ ] Final optimized model saved
- [ ] Performance meets targets

### Session 6: Deployment ✓
- [ ] Flask/FastAPI API built
- [ ] API tested locally
- [ ] Streamlit UI built
- [ ] UI tested locally
- [ ] API deployed to Heroku (or similar)
- [ ] UI deployed to Streamlit Cloud
- [ ] End-to-end integration working
- [ ] Public URLs obtained and documented

---

## Submit Week 2 Checkpoint

**Package and submit:**
1. Model development notebook (`notebooks/03_modeling.ipynb`)
2. Model evaluation report (metrics, comparisons)
3. Deployed API URL (working!)
4. Deployed UI URL (working!)
5. GitHub repository link (updated)

**Demo to instructor:**
- Show deployed application working
- Make live prediction
- Explain model choice

---

## Tips for Week 2 Success

### Do's ✅
- Start simple, iterate
- Test frequently
- Deploy early (don't wait until last day!)
- Document as you code
- Commit often to Git
- Ask for help when stuck

### Don'ts ❌
- Don't skip baseline model
- Don't over-optimize (good enough is good enough)
- Don't leave deployment for last day
- Don't ignore test errors
- Don't forget to save models!
- Don't hardcode credentials

---

## Troubleshooting

**Model not improving?**
- Check for data leakage
- Try different features
- Tune hyperparameters
- Consider ensemble methods

**API deployment fails?**
- Check Heroku logs
- Verify all dependencies in requirements.txt
- Test locally first
- Check model file sizes (<500MB for Heroku)

**UI not connecting to API?**
- Verify API URL is correct
- Check CORS settings
- Test API endpoint directly
- Check network/firewall

---

## Ready for Week 3?

If Week 2 is complete:
- ✅ You have working ML models
- ✅ You have deployed API
- ✅ You have deployed UI
- ✅ Everything works end-to-end
- ✅ You're ready to polish and present!

**Next:** `guides/week-3-polish-guide.md`

---

*You've built something real. Now let's make it shine!* 🌟
