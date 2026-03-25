# Module 5: Unsupervised Learning - Datasets Documentation

## Overview

This directory contains all datasets and data generation scripts for Module 5: Unsupervised Learning. All datasets are either synthetic (generated) or built into scikit-learn to ensure reproducibility and eliminate external dependencies.

---

## Quick Start

### Generate All Datasets

```bash
python download_unsupervised_datasets.py
```

This will create a `data/` subdirectory with all required CSV files.

**Expected Output:**
```
data/
├── ecommerce_customers.csv       (2,000 rows)
├── patient_health_data.csv       (800 rows)
├── news_articles.csv             (1,200 rows)
└── credit_card_fraud.csv         (10,000 rows)
```

**MNIST Digits dataset** is built into scikit-learn and requires no download.

---

## Dataset Specifications

### 1. E-commerce Customer Data
**File:** `data/ecommerce_customers.csv`
**Purpose:** Session 1 - K-Means Customer Segmentation

#### Description
Synthetic e-commerce customer data with 2,000 customers across 5 distinct behavioral segments.

#### Features
| Column | Type | Range | Description |
|--------|------|-------|-------------|
| `customer_id` | int | 1-2000 | Unique customer identifier |
| `recency` | int | 1-365 | Days since last purchase |
| `frequency` | int | 1-50 | Number of purchases in period |
| `monetary` | float | $20-$15,000 | Total spending |
| `avg_order_value` | float | $20-$500 | Average order amount |
| `age` | int | 18-65 | Customer age |
| `web_visits_per_month` | int | 1-30 | Monthly website visits |
| `segment_true` | string | - | True segment label (for validation) |

#### True Segments
1. **High-Value Frequent** (20%, n=400)
   - Recent purchases (1-30 days)
   - High frequency (20-50 purchases)
   - High spending ($5,000-$15,000)
   - Older customers (35-55 years)

2. **Loyal Regulars** (25%, n=500)
   - Moderately recent (1-60 days)
   - Medium frequency (10-25 purchases)
   - Medium spending ($2,000-$6,000)
   - Mixed ages (25-60 years)

3. **At-Risk** (15%, n=300)
   - Not recent (90-365 days)
   - Had moderate frequency (5-15 purchases)
   - Medium spending ($1,000-$4,000)
   - Low engagement (1-5 web visits)

4. **New Customers** (20%, n=400)
   - Recent (1-30 days)
   - Low frequency (1-5 purchases)
   - Low total spending ($50-$1,000)
   - Younger (18-45 years)

5. **Window Shoppers** (20%, n=400)
   - Not very recent (30-180 days)
   - Very low frequency (1-3 purchases)
   - Very low spending ($20-$500)
   - High browsing, low buying

#### Usage Example
```python
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Load data
customers = pd.read_csv('data/ecommerce_customers.csv')

# Select features for clustering
features = ['recency', 'frequency', 'monetary', 'avg_order_value', 'age', 'web_visits_per_month']
X = customers[features]

# Scale features (CRITICAL for K-Means!)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply K-Means
kmeans = KMeans(n_clusters=5, random_state=42)
customers['cluster'] = kmeans.fit_predict(X_scaled)
```

---

### 2. Patient Health Data
**File:** `data/patient_health_data.csv`
**Purpose:** Session 2 - Hierarchical & DBSCAN Clustering Comparison

#### Description
Synthetic patient medical data with 800 patients across 4 health profiles.

#### Features
| Column | Type | Range | Description |
|--------|------|-------|-------------|
| `patient_id` | int | 1-800 | Unique patient identifier |
| `age` | int | 20-90 | Patient age in years |
| `bmi` | float | 18.5-40 | Body Mass Index |
| `blood_pressure_sys` | int | 110-180 | Systolic blood pressure (mmHg) |
| `blood_pressure_dia` | int | 70-115 | Diastolic blood pressure (mmHg) |
| `glucose` | float | 70-200 | Blood glucose level (mg/dL) |
| `cholesterol` | float | 150-300 | Total cholesterol (mg/dL) |
| `heart_rate` | int | 60-100 | Resting heart rate (bpm) |
| `group_true` | string | - | True health group (for validation) |

#### True Health Groups
1. **Healthy** (40%, n=320)
   - Younger (20-50 years)
   - Normal BMI (18.5-25)
   - Normal vitals across all metrics

2. **Pre-diabetic** (30%, n=240)
   - Middle-aged (35-65 years)
   - Overweight (BMI 25-30)
   - Elevated glucose (100-125 mg/dL)
   - Slightly elevated BP

3. **High-risk** (20%, n=160)
   - Older (50-80 years)
   - Obese (BMI 30-40)
   - High BP, high glucose, high cholesterol
   - Multiple risk factors

4. **Elderly** (10%, n=80)
   - Very old (70-90 years)
   - Variable health metrics
   - Age-related considerations

#### Usage Example
```python
import pandas as pd
from sklearn.cluster import DBSCAN, AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt

# Load data
patients = pd.read_csv('data/patient_health_data.csv')

# Select features
features = ['age', 'bmi', 'blood_pressure_sys', 'blood_pressure_dia',
            'glucose', 'cholesterol', 'heart_rate']
X = patients[features]

# Scale
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Hierarchical clustering with dendrogram
linkage_matrix = linkage(X_scaled[:200], method='ward')
plt.figure(figsize=(12, 6))
dendrogram(linkage_matrix)
plt.show()

# DBSCAN for outlier detection
dbscan = DBSCAN(eps=1.5, min_samples=10)
patients['cluster'] = dbscan.fit_predict(X_scaled)
print(f"Outliers: {(patients['cluster'] == -1).sum()} patients")
```

---

### 3. News Articles Dataset
**File:** `data/news_articles.csv`
**Purpose:** Session 3 - Document Clustering and Topic Discovery

#### Description
Synthetic news articles with 1,200 articles across 3 topics (Sports, Technology, Business).

#### Features
| Column | Type | Description |
|--------|------|-------------|
| `article_id` | int | Unique article identifier (1-1200) |
| `text` | string | Article text content (~30 words) |
| `category` | string | True category (Sports/Technology/Business) |

#### Categories
- **Sports** (400 articles): Football, basketball, tennis, championships, players
- **Technology** (400 articles): AI, machine learning, smartphones, innovation, cybersecurity
- **Business** (400 articles): Stocks, investments, companies, economy, finance

#### Usage Example
```python
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Load data
news = pd.read_csv('data/news_articles.csv')

# TF-IDF vectorization
vectorizer = TfidfVectorizer(max_features=100, stop_words='english')
X_tfidf = vectorizer.fit_transform(news['text'])

# K-Means clustering
kmeans = KMeans(n_clusters=3, random_state=42)
news['cluster'] = kmeans.fit_predict(X_tfidf)

# Extract top terms per cluster
terms = vectorizer.get_feature_names_out()
order_centroids = kmeans.cluster_centers_.argsort()[:, ::-1]

for i in range(3):
    print(f"Cluster {i} top terms:")
    top_terms = [terms[ind] for ind in order_centroids[i, :10]]
    print(', '.join(top_terms))

    # Generate word cloud
    cluster_text = ' '.join(news[news['cluster'] == i]['text'])
    wordcloud = WordCloud(width=800, height=400).generate(cluster_text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(f'Cluster {i} Word Cloud')
    plt.show()
```

---

### 4. MNIST Digits Dataset
**Source:** Built into scikit-learn
**Purpose:** Sessions 4 & 5 - PCA and t-SNE Dimensionality Reduction

#### Description
Handwritten digit images (0-9) in 8×8 grayscale format. This is a smaller version of the famous MNIST dataset.

#### Specifications
- **Samples:** 1,797 images
- **Features:** 64 (8×8 pixels)
- **Classes:** 10 (digits 0-9)
- **Format:** Each pixel value 0-16 (grayscale intensity)

#### Loading
```python
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt

# Load dataset
digits = load_digits()
X = digits.data        # Shape: (1797, 64)
y = digits.target      # Shape: (1797,)

print(f"Samples: {X.shape[0]}")
print(f"Features: {X.shape[1]}")
print(f"Classes: {len(np.unique(y))}")

# Visualize samples
fig, axes = plt.subplots(2, 5, figsize=(10, 4))
for idx, ax in enumerate(axes.ravel()):
    ax.imshow(X[idx].reshape(8, 8), cmap='gray')
    ax.set_title(f'Label: {y[idx]}')
    ax.axis('off')
plt.show()
```

#### Usage for PCA
```python
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Standardize
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# PCA to 2D
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

print(f"Explained variance: {pca.explained_variance_ratio_}")
print(f"Total: {sum(pca.explained_variance_ratio_):.2%}")

# Visualize
plt.figure(figsize=(10, 8))
scatter = plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='tab10', alpha=0.6)
plt.colorbar(scatter, label='Digit')
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.title('MNIST Digits in 2D (PCA)')
plt.show()
```

#### Usage for t-SNE
```python
from sklearn.manifold import TSNE

# t-SNE to 2D (slower but better visualization)
tsne = TSNE(n_components=2, random_state=42, perplexity=30)
X_tsne = tsne.fit_transform(X_scaled)

plt.figure(figsize=(10, 8))
scatter = plt.scatter(X_tsne[:, 0], X_tsne[:, 1], c=y, cmap='tab10', alpha=0.6)
plt.colorbar(scatter, label='Digit')
plt.title('MNIST Digits in 2D (t-SNE)')
plt.show()
```

---

### 5. Credit Card Fraud Dataset
**File:** `data/credit_card_fraud.csv`
**Purpose:** Session 6 - Unsupervised Anomaly Detection (Capstone)

#### Description
Synthetic credit card transaction data with 10,000 transactions, including 5% fraudulent transactions with anomalous patterns.

#### Features
| Column | Type | Range | Description |
|--------|------|-------|-------------|
| `transaction_id` | int | 1-10000 | Unique transaction identifier |
| `amount` | float | $20-$5,000 | Transaction amount |
| `time_of_day` | float | 0-24 | Hour of transaction (24-hour format) |
| `distance_from_home` | float | 0-500 | Distance from home location (km) |
| `num_transactions_24h` | int | 1-20 | Number of transactions in last 24h |
| `merchant_risk_score` | float | 0-1 | Merchant risk assessment (0=safe, 1=risky) |
| `is_fraud` | int | 0/1 | True fraud label (0=normal, 1=fraud) |

#### Patterns
**Normal Transactions (95%, n=9,500):**
- Moderate amounts ($50-$300)
- Normal hours (6 AM - 11 PM)
- Close to home (<50 km)
- Few daily transactions (1-5)
- Low-risk merchants (0-0.3 risk score)

**Fraudulent Transactions (5%, n=500):**
- High amounts ($500-$5,000)
- Unusual hours (2-5 AM)
- Far from home (100-500 km)
- Many transactions (10-20 in 24h)
- High-risk merchants (0.7-1.0 risk score)

#### Usage Example (Isolation Forest)
```python
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix

# Load data
fraud = pd.read_csv('data/credit_card_fraud.csv')

# Features (pretend we don't know is_fraud!)
features = ['amount', 'time_of_day', 'distance_from_home',
            'num_transactions_24h', 'merchant_risk_score']
X = fraud[features]
y_true = fraud['is_fraud']  # For evaluation only!

# Scale
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Isolation Forest
iso_forest = IsolationForest(contamination=0.05, random_state=42)
y_pred = iso_forest.fit_predict(X_scaled)
y_pred = (y_pred == -1).astype(int)  # Convert -1/1 to 0/1

# Evaluate
print("Performance:")
print(classification_report(y_true, y_pred, target_names=['Normal', 'Fraud']))
print("\nConfusion Matrix:")
print(confusion_matrix(y_true, y_pred))
```

---

## Data Generation Details

### Reproducibility
- All synthetic datasets use `random_seed=42` for reproducibility
- Running the script multiple times produces identical data
- Ensures consistent results across all learners

### Quality Assurance
- Realistic distributions and ranges
- Clear separation between segments/groups
- Sufficient sample sizes for stable clustering
- Balanced representation of patterns

### Modifications
To modify data generation parameters, edit `download_unsupervised_datasets.py`:
- Change `n_customers`, `n_patients`, etc. for different sample sizes
- Adjust feature ranges for different scales
- Modify segment proportions

---

## Troubleshooting

### Issue: Script fails with ModuleNotFoundError
**Solution:** Install required packages
```bash
pip install numpy pandas scikit-learn
```

### Issue: Data files already exist
**Solution:** Script will overwrite. To backup:
```bash
cp data/ecommerce_customers.csv data/ecommerce_customers_backup.csv
```

### Issue: MNIST digits not found
**Solution:** No download needed - use scikit-learn directly:
```python
from sklearn.datasets import load_digits
digits = load_digits()
```

### Issue: Datasets too large/small
**Solution:** Edit `download_unsupervised_datasets.py` to adjust sample sizes

---

## Data Privacy & Ethics

### Synthetic Data Advantages
- No real customer/patient data exposed
- No privacy concerns
- No GDPR/HIPAA compliance needed
- Safe for educational sharing

### Real-World Considerations
When working with real data:
- Obtain proper consent and permissions
- Anonymize/pseudonymize sensitive data
- Follow data protection regulations
- Consider ethical implications of clustering (e.g., customer profiling)
- Avoid discriminatory groupings

---

## Additional Datasets (Optional)

For learners wanting to explore further:

### Real Datasets for Practice
1. **UCI Machine Learning Repository**
   - Online Retail: https://archive.ics.uci.edu/ml/datasets/Online+Retail
   - Wholesale customers: https://archive.ics.uci.edu/ml/datasets/Wholesale+customers

2. **Kaggle Datasets**
   - Mall Customer Segmentation: https://www.kaggle.com/vjchoudhary7/customer-segmentation-tutorial-in-python
   - BBC News: https://www.kaggle.com/c/learn-ai-bbc/data

3. **scikit-learn Built-in**
   - Iris (simple clustering)
   - Wine (quality clustering)
   - Breast Cancer (outlier detection)

---

## License & Attribution

All synthetic datasets in this module are generated specifically for educational purposes and are freely available for use in this course.

For real-world datasets, always check and comply with their respective licenses and terms of use.

---

## Summary

| Dataset | File | Samples | Features | Purpose |
|---------|------|---------|----------|---------|
| E-commerce Customers | `ecommerce_customers.csv` | 2,000 | 7 + label | K-Means segmentation |
| Patient Health | `patient_health_data.csv` | 800 | 7 + label | Hierarchical/DBSCAN |
| News Articles | `news_articles.csv` | 1,200 | text + label | Document clustering |
| MNIST Digits | sklearn built-in | 1,797 | 64 (8×8) | PCA/t-SNE visualization |
| Credit Card Fraud | `credit_card_fraud.csv` | 10,000 | 5 + label | Anomaly detection |

**Total:** ~15,000 samples across 5 datasets covering all major unsupervised learning techniques!

---

**Need help?** Check the main module README or reach out to instructors.
