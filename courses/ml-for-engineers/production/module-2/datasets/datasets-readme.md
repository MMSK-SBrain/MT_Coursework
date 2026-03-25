# Module 2: Classification Datasets
## Complete Data Dictionary and Access Guide

**Module:** Classification (Module 2)
**Created:** 2026-01-05
**Total Datasets:** 6
**Purpose:** Support all 6 classification projects

---

## Quick Start

### Installation

```bash
pip install -r requirements.txt
```

### Download All Datasets

```bash
python3 download_datasets.py
```

This will create a `data/` directory with all datasets ready to use.

---

## Dataset 1: Iris Flower Classification

### Overview
- **Source:** Built-in with scikit-learn
- **Problem Type:** Multi-class classification (3 classes)
- **Samples:** 150 (50 per class)
- **Features:** 4 numerical features
- **Target:** Species (setosa, versicolor, virginica)
- **Difficulty:** ⭐ Beginner

### Dataset Details

| Column Name | Type | Description | Unit | Range |
|------------|------|-------------|------|-------|
| sepal length (cm) | float | Length of sepal | cm | 4.3 - 7.9 |
| sepal width (cm) | float | Width of sepal | cm | 2.0 - 4.4 |
| petal length (cm) | float | Length of petal | cm | 1.0 - 6.9 |
| petal width (cm) | float | Width of petal | cm | 0.1 - 2.5 |
| species | int | Target class (0, 1, 2) | - | 0-2 |
| species_name | string | Class label name | - | setosa/versicolor/virginica |

### Class Distribution
- Setosa (0): 50 samples (33.3%)
- Versicolor (1): 50 samples (33.3%)
- Virginica (2): 50 samples (33.3%)

**Perfectly balanced dataset!**

### Loading Code

```python
from sklearn.datasets import load_iris
import pandas as pd

# Load dataset
iris = load_iris()

# Convert to DataFrame
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = iris.target
df['species_name'] = iris.target_names[iris.target]

print(f"Shape: {df.shape}")
print(df.head())
```

### Project Goal
- Build Decision Tree classifier
- **Target Accuracy:** >90%
- Understand train/test split
- First successful ML model!

### Key Learning Points
- Basic classification workflow
- Multi-class classification
- Confusion matrix
- Model evaluation metrics

---

## Dataset 2: Spam Email Detection

### Overview
- **Source:** UCI Machine Learning Repository (SMS Spam Collection)
- **Problem Type:** Binary classification
- **Samples:** 5,574 SMS messages
- **Features:** Text (message content)
- **Target:** spam / ham (legitimate)
- **Difficulty:** ⭐⭐ Intermediate

### Dataset Details

| Column Name | Type | Description | Example |
|------------|------|-------------|---------|
| label | string | Class label | "spam" or "ham" |
| message | string | SMS text content | "Free entry in 2 a wkly..." |

### Class Distribution
- Ham (legitimate): 4,827 messages (86.6%)
- Spam: 747 messages (13.4%)

**Imbalanced dataset** - typical of real-world spam detection!

### Loading Code

```python
import pandas as pd

# Load dataset
df = pd.read_csv('data/spam_email.csv')

# Binary encoding
df['target'] = df['label'].map({'ham': 0, 'spam': 1})

print(f"Total messages: {len(df)}")
print(f"Spam: {(df['target']==1).sum()}")
print(f"Ham: {(df['target']==0).sum()}")
```

### Text Preprocessing Pipeline

```python
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

# Option 1: Bag of Words
vectorizer = CountVectorizer(max_features=3000)
X = vectorizer.fit_transform(df['message'])

# Option 2: TF-IDF (often better for spam)
tfidf = TfidfVectorizer(max_features=3000, stop_words='english')
X = tfidf.fit_transform(df['message'])
```

### Project Goal
- Build Naive Bayes or Logistic Regression classifier
- **Target Accuracy:** >90%
- Learn text preprocessing
- Handle imbalanced data

### Key Learning Points
- Text to numerical features (vectorization)
- Bag of Words vs TF-IDF
- Naive Bayes for text
- Precision vs Recall trade-off

### Source URL
https://archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection

---

## Dataset 3: Customer Churn Prediction

### Overview
- **Source:** IBM Telco Customer Churn Dataset
- **Problem Type:** Binary classification
- **Samples:** 7,043 customers
- **Features:** 19 features (numerical + categorical)
- **Target:** Churn (Yes/No)
- **Difficulty:** ⭐⭐⭐ Advanced

### Dataset Details

| Column Name | Type | Description | Values/Range |
|------------|------|-------------|--------------|
| customerID | string | Unique ID | - |
| gender | string | Gender | Male/Female |
| SeniorCitizen | int | Senior citizen flag | 0/1 |
| Partner | string | Has partner | Yes/No |
| Dependents | string | Has dependents | Yes/No |
| tenure | int | Months with company | 0-72 |
| PhoneService | string | Has phone service | Yes/No |
| MultipleLines | string | Multiple phone lines | Yes/No/No phone service |
| InternetService | string | Internet service type | DSL/Fiber optic/No |
| OnlineSecurity | string | Online security service | Yes/No/No internet |
| OnlineBackup | string | Online backup service | Yes/No/No internet |
| DeviceProtection | string | Device protection | Yes/No/No internet |
| TechSupport | string | Tech support | Yes/No/No internet |
| StreamingTV | string | Streaming TV | Yes/No/No internet |
| StreamingMovies | string | Streaming movies | Yes/No/No internet |
| Contract | string | Contract type | Month-to-month/One year/Two year |
| PaperlessBilling | string | Paperless billing | Yes/No |
| PaymentMethod | string | Payment method | 4 types |
| MonthlyCharges | float | Monthly charge | $18.25 - $118.75 |
| TotalCharges | float | Total charges | $18.80 - $8,684.80 |
| Churn | string | Customer churned | Yes/No |

### Class Distribution
- No Churn: 5,174 customers (73.5%)
- Churn: 1,869 customers (26.5%)

**Moderately imbalanced**

### Loading Code

```python
import pandas as pd

# Load dataset
df = pd.read_csv('data/customer_churn.csv')

# Binary target
df['Churn_Binary'] = df['Churn'].map({'No': 0, 'Yes': 1})

print(f"Total customers: {len(df)}")
print(f"Churn rate: {df['Churn_Binary'].mean():.2%}")
```

### Feature Engineering Ideas

```python
# Create new features
df['TenureGroup'] = pd.cut(df['tenure'], bins=[0, 12, 24, 48, 72],
                            labels=['0-1yr', '1-2yr', '2-4yr', '4-6yr'])

df['AvgMonthlyCharges'] = df['TotalCharges'] / (df['tenure'] + 1)

df['HasMultipleServices'] = (
    (df['OnlineSecurity'] == 'Yes').astype(int) +
    (df['OnlineBackup'] == 'Yes').astype(int) +
    (df['DeviceProtection'] == 'Yes').astype(int) +
    (df['TechSupport'] == 'Yes').astype(int)
)
```

### Project Goal
- Build Random Forest or Gradient Boosting classifier
- **Target Accuracy:** >80%
- Learn feature engineering
- Handle categorical variables
- Address class imbalance

### Key Learning Points
- Handling mixed data types
- Label encoding vs One-Hot encoding
- Feature engineering for business data
- Class imbalance techniques (SMOTE, class weights)
- Business impact (revenue retention)

### Source URL
https://github.com/IBM/telco-customer-churn-on-icp4d

---

## Dataset 4: Heart Disease Prediction

### Overview
- **Source:** UCI Machine Learning Repository (Cleveland Heart Disease)
- **Problem Type:** Binary classification
- **Samples:** 297 patients (after removing missing values)
- **Features:** 13 medical attributes
- **Target:** Disease presence (0/1)
- **Difficulty:** ⭐⭐⭐ Advanced

### Dataset Details

| Column Name | Type | Description | Values/Range |
|------------|------|-------------|--------------|
| age | int | Age in years | 29-77 |
| sex | int | Sex (1=male, 0=female) | 0/1 |
| cp | int | Chest pain type | 1-4 |
| trestbps | int | Resting blood pressure | 94-200 mm Hg |
| chol | int | Serum cholesterol | 126-564 mg/dl |
| fbs | int | Fasting blood sugar >120 | 0/1 |
| restecg | int | Resting ECG results | 0-2 |
| thalach | int | Max heart rate achieved | 71-202 |
| exang | int | Exercise induced angina | 0/1 |
| oldpeak | float | ST depression | 0-6.2 |
| slope | int | Slope of peak exercise ST | 1-3 |
| ca | int | Number of major vessels | 0-3 |
| thal | int | Thalassemia | 3, 6, 7 |
| target | int | Disease present | 0/1 |

### Medical Context

**Chest Pain Types (cp):**
1. Typical angina
2. Atypical angina
3. Non-anginal pain
4. Asymptomatic

**Resting ECG (restecg):**
0. Normal
1. ST-T wave abnormality
2. Left ventricular hypertrophy

### Class Distribution
- No disease (0): ~160 patients (54%)
- Disease present (1): ~137 patients (46%)

**Relatively balanced**

### Loading Code

```python
import pandas as pd

# Load dataset
df = pd.read_csv('data/heart_disease.csv')

print(f"Total patients: {len(df)}")
print(f"Disease present: {(df['target']==1).sum()}")
print(f"No disease: {(df['target']==0).sum()}")

# Check for missing values
print(f"Missing values:\n{df.isnull().sum()}")
```

### Project Goal
- Build classification model with **high recall** (minimize false negatives!)
- **Target AUC:** >0.85
- Learn ROC curve analysis
- Understand precision-recall trade-off in medical context

### Key Learning Points
- Medical AI ethics
- Cost of false negatives (missing disease) vs false positives
- ROC curve and AUC
- Feature importance for interpretability
- When to prioritize recall over precision

### Important Medical Note
⚠️ This is for educational purposes only. Real medical AI requires:
- Regulatory approval (FDA, etc.)
- Much larger datasets
- Clinical validation
- Explainable models
- Expert physician oversight

### Source URL
https://archive.ics.uci.edu/ml/datasets/Heart+Disease

---

## Dataset 5: MNIST Digit Classification

### Overview
- **Source:** Built-in with TensorFlow/Keras
- **Problem Type:** Multi-class classification (10 classes)
- **Samples:** 70,000 images (60,000 train + 10,000 test)
- **Features:** 784 pixels (28x28 grayscale images)
- **Target:** Digits 0-9
- **Difficulty:** ⭐⭐⭐ Advanced (large scale)

### Dataset Details

| Property | Value | Description |
|----------|-------|-------------|
| Image Size | 28 x 28 | Grayscale images |
| Pixel Values | 0-255 | Intensity (0=black, 255=white) |
| Training Set | 60,000 | For model training |
| Test Set | 10,000 | For evaluation |
| Classes | 10 | Digits 0-9 |
| File Format | NumPy arrays | Native to Keras |

### Class Distribution
Each digit (0-9) has approximately equal representation (~6,000 training images each).

**Perfectly balanced dataset!**

### Loading Code

```python
from tensorflow import keras
import matplotlib.pyplot as plt

# Load dataset
(X_train, y_train), (X_test, y_test) = keras.datasets.mnist.load_data()

print(f"Training images: {X_train.shape}")
print(f"Training labels: {y_train.shape}")
print(f"Test images: {X_test.shape}")
print(f"Test labels: {y_test.shape}")

# Visualize sample
plt.imshow(X_train[0], cmap='gray')
plt.title(f"Label: {y_train[0]}")
plt.show()
```

### Preprocessing Pipeline

```python
import numpy as np

# Normalize pixel values to [0, 1]
X_train_norm = X_train.astype('float32') / 255.0
X_test_norm = X_test.astype('float32') / 255.0

# Flatten for traditional ML (28x28 -> 784)
X_train_flat = X_train_norm.reshape(60000, -1)
X_test_flat = X_test_norm.reshape(10000, -1)

# For neural networks, reshape to (28, 28, 1)
X_train_cnn = X_train_norm.reshape(-1, 28, 28, 1)
X_test_cnn = X_test_norm.reshape(-1, 28, 28, 1)

# One-hot encode labels
y_train_onehot = keras.utils.to_categorical(y_train, 10)
y_test_onehot = keras.utils.to_categorical(y_test, 10)
```

### Project Goal
- Build simple neural network (fully connected)
- **Target Accuracy:** >95%
- Learn image classification basics
- Introduction to neural networks

### Model Options

**Option 1: Traditional ML (faster training)**
```python
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators=100)
model.fit(X_train_flat[:10000], y_train[:10000])  # Use subset
```

**Option 2: Simple Neural Network (better accuracy)**
```python
from tensorflow import keras

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(X_train_norm, y_train, epochs=5, validation_split=0.2)
```

### Key Learning Points
- Image data preprocessing
- Flattening images for ML
- Neural network basics
- Softmax for multi-class
- Large-scale classification

### Performance Benchmarks
- Random Forest: ~97% accuracy
- Simple Neural Network: ~98% accuracy
- CNN (out of scope): ~99% accuracy

---

## Dataset 6: Cricket Match Outcome Prediction

### Overview
- **Source:** IPL (Indian Premier League) match data
- **Problem Type:** Binary classification (Team 1 win / Team 2 win)
- **Samples:** ~600-800 matches
- **Features:** Team names, venue, toss winner, season
- **Target:** Match winner
- **Difficulty:** ⭐⭐ Intermediate

### Dataset Details

| Column Name | Type | Description | Example Values |
|------------|------|-------------|----------------|
| season | int | IPL season year | 2008-2020 |
| team1 | string | First team | Mumbai Indians, CSK, etc. |
| team2 | string | Second team | Royal Challengers, KKR, etc. |
| toss_winner | string | Team that won toss | Mumbai Indians |
| toss_decision | string | Bat or field | bat / field |
| winner | string | Match winner | Mumbai Indians |
| venue | string | Stadium | Wankhede Stadium, Eden Gardens |
| result | string | Result type | normal / tie / no result |

### Feature Engineering Opportunities

```python
# 1. Team strength (historical win rate)
team_wins = df.groupby('winner').size()

# 2. Venue advantage (home ground)
df['team1_home'] = df.apply(lambda x: 1 if 'home_ground_logic' else 0, axis=1)

# 3. Toss advantage
df['toss_match'] = (df['toss_winner'] == df['winner']).astype(int)

# 4. Head-to-head record
# Calculate win rate between specific teams

# 5. Recent form (last 5 matches)
# Rolling window of wins/losses
```

### Loading Code

```python
import pandas as pd

# Load dataset
df = pd.read_csv('data/cricket_matches.csv')

# Remove ties and no-results
df = df[df['result'] == 'normal'].copy()

# Create binary target (did team1 win?)
df['team1_win'] = (df['winner'] == df['team1']).astype(int)

print(f"Total matches: {len(df)}")
print(f"Team1 wins: {df['team1_win'].sum()}")
print(f"Team2 wins: {len(df) - df['team1_win'].sum()}")
```

### Project Goal
- Build match outcome predictor
- **Target Accuracy:** >60% (cricket is unpredictable!)
- Learn feature engineering from categorical data
- Understand sports analytics

### Key Learning Points
- Encoding categorical features
- Creating derived features (team strength, form)
- Handling temporal data (season trends)
- Understanding prediction limits (sports randomness)
- Engagement hook (callback to Module 0!)

### Business Applications
- Sports betting odds
- Fantasy cricket team selection
- Broadcasting insights
- Team strategy planning

### Source URL
https://www.kaggle.com/nowke9/ipldata
https://github.com/codophilic/IPL-Data-Analysis

---

## Installation & Setup

### Step 1: Install Dependencies

```bash
# Create virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install packages
pip install -r requirements.txt
```

### Step 2: Download Datasets

```bash
python3 download_datasets.py
```

### Step 3: Verify Installation

```python
import pandas as pd
import numpy as np
import sklearn
import tensorflow as tf

print("✓ All libraries imported successfully!")
print(f"Pandas: {pd.__version__}")
print(f"NumPy: {np.__version__}")
print(f"Scikit-learn: {sklearn.__version__}")
print(f"TensorFlow: {tf.__version__}")
```

---

## Dataset Summary Table

| # | Dataset | Samples | Features | Classes | Difficulty | Target Accuracy |
|---|---------|---------|----------|---------|------------|-----------------|
| 1 | Iris | 150 | 4 | 3 | ⭐ | >90% |
| 2 | Spam Email | 5,574 | Text | 2 | ⭐⭐ | >90% |
| 3 | Customer Churn | 7,043 | 19 | 2 | ⭐⭐⭐ | >80% |
| 4 | Heart Disease | 297 | 13 | 2 | ⭐⭐⭐ | AUC >0.85 |
| 5 | MNIST | 70,000 | 784 | 10 | ⭐⭐⭐ | >95% |
| 6 | Cricket Matches | ~700 | 7+ | 2 | ⭐⭐ | >60% |

---

## Troubleshooting

### Issue: Dataset download fails

**Solution:**
- Check internet connection
- Verify URLs are still active
- Try manual download from source URLs
- Check firewall/proxy settings

### Issue: Missing libraries

**Solution:**
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Issue: TensorFlow installation problems

**Solution (macOS with Apple Silicon):**
```bash
pip install tensorflow-macos
pip install tensorflow-metal  # For GPU acceleration
```

**Solution (Windows/Linux):**
```bash
pip install tensorflow
```

### Issue: Memory errors with MNIST

**Solution:**
- Use subset of data (first 10,000 samples)
- Increase system RAM allocation
- Use batch processing

---

## Next Steps

1. ✅ Datasets downloaded
2. ⏭️ Start with Iris Classifier (Session 1)
3. ⏭️ Build Spam Detector (Session 2)
4. ⏭️ Create Churn Predictor (Session 3)
5. ⏭️ Build Heart Disease Predictor (Session 4)
6. ⏭️ Optional: MNIST & Cricket projects

---

## License Information

- **Iris:** Public domain (UCI ML Repository)
- **SMS Spam Collection:** Public domain (UCI ML Repository)
- **Telco Churn:** IBM - Open data
- **Heart Disease:** Public domain (UCI ML Repository)
- **MNIST:** Yann LeCun - Publicly available
- **Cricket (IPL):** Public sports data

All datasets are used for educational purposes.

---

**Created:** 2026-01-05
**Last Updated:** 2026-01-05
**Version:** 1.0
**Status:** ✅ Ready for use
