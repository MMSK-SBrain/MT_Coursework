#!/usr/bin/env python3
"""
Module 5: Unsupervised Learning - Dataset Download Script

This script downloads or generates all datasets needed for Module 5.
Datasets include:
1. E-commerce customer data (synthetic)
2. Patient/healthcare data (synthetic)
3. News articles dataset (synthetic or real)
4. MNIST digits (built-in to sklearn)
5. Credit card fraud data (synthetic)

All datasets are generated synthetically to ensure reproducibility
and avoid external dependencies.
"""

import numpy as np
import pandas as pd
import os
from sklearn.datasets import load_digits
import warnings
warnings.filterwarnings('ignore')

# Create datasets directory if it doesn't exist
os.makedirs('data', exist_ok=True)

print("="*70)
print("MODULE 5: UNSUPERVISED LEARNING - DATASET GENERATOR")
print("="*70)

# ============================================================================
# Dataset 1: E-commerce Customer Data (for K-Means clustering)
# ============================================================================
print("\n[1/5] Generating E-commerce Customer Data...")
np.random.seed(42)
n_customers = 2000

# Create 5 distinct customer segments
segments = []

# Segment 1: High-Value Frequent Buyers (20%)
n1 = 400
seg1 = pd.DataFrame({
    'customer_id': range(1, n1+1),
    'recency': np.random.randint(1, 30, n1),
    'frequency': np.random.randint(20, 50, n1),
    'monetary': np.random.uniform(5000, 15000, n1),
    'avg_order_value': np.random.uniform(200, 500, n1),
    'age': np.random.randint(35, 55, n1),
    'web_visits_per_month': np.random.randint(15, 30, n1),
    'segment_true': 'High-Value Frequent'
})
segments.append(seg1)

# Segment 2: Loyal Regulars (25%)
n2 = 500
seg2 = pd.DataFrame({
    'customer_id': range(n1+1, n1+n2+1),
    'recency': np.random.randint(1, 60, n2),
    'frequency': np.random.randint(10, 25, n2),
    'monetary': np.random.uniform(2000, 6000, n2),
    'avg_order_value': np.random.uniform(100, 250, n2),
    'age': np.random.randint(25, 60, n2),
    'web_visits_per_month': np.random.randint(8, 18, n2),
    'segment_true': 'Loyal Regulars'
})
segments.append(seg2)

# Segment 3: At-Risk Customers (15%)
n3 = 300
seg3 = pd.DataFrame({
    'customer_id': range(n1+n2+1, n1+n2+n3+1),
    'recency': np.random.randint(90, 365, n3),
    'frequency': np.random.randint(5, 15, n3),
    'monetary': np.random.uniform(1000, 4000, n3),
    'avg_order_value': np.random.uniform(80, 200, n3),
    'age': np.random.randint(25, 65, n3),
    'web_visits_per_month': np.random.randint(1, 5, n3),
    'segment_true': 'At-Risk'
})
segments.append(seg3)

# Segment 4: New Customers (20%)
n4 = 400
seg4 = pd.DataFrame({
    'customer_id': range(n1+n2+n3+1, n1+n2+n3+n4+1),
    'recency': np.random.randint(1, 30, n4),
    'frequency': np.random.randint(1, 5, n4),
    'monetary': np.random.uniform(50, 1000, n4),
    'avg_order_value': np.random.uniform(50, 200, n4),
    'age': np.random.randint(18, 45, n4),
    'web_visits_per_month': np.random.randint(5, 15, n4),
    'segment_true': 'New Customers'
})
segments.append(seg4)

# Segment 5: Window Shoppers (20%)
n5 = 400
seg5 = pd.DataFrame({
    'customer_id': range(n1+n2+n3+n4+1, n1+n2+n3+n4+n5+1),
    'recency': np.random.randint(30, 180, n5),
    'frequency': np.random.randint(1, 3, n5),
    'monetary': np.random.uniform(20, 500, n5),
    'avg_order_value': np.random.uniform(20, 100, n5),
    'age': np.random.randint(18, 50, n5),
    'web_visits_per_month': np.random.randint(10, 25, n5),
    'segment_true': 'Window Shoppers'
})
segments.append(seg5)

# Combine and shuffle
customers = pd.concat(segments, ignore_index=True)
customers = customers.sample(frac=1, random_state=42).reset_index(drop=True)
customers.to_csv('data/ecommerce_customers.csv', index=False)
print(f"   ✓ Generated {len(customers)} customers with 5 distinct segments")
print(f"   ✓ Saved to: data/ecommerce_customers.csv")

# ============================================================================
# Dataset 2: Patient Healthcare Data (for hierarchical/DBSCAN clustering)
# ============================================================================
print("\n[2/5] Generating Patient Healthcare Data...")
np.random.seed(42)
n_patients = 800

# Create 4 patient groups with distinct health profiles
patient_groups = []

# Group 1: Healthy (40%)
n_p1 = 320
pg1 = pd.DataFrame({
    'patient_id': range(1, n_p1+1),
    'age': np.random.randint(20, 50, n_p1),
    'bmi': np.random.uniform(18.5, 25, n_p1),
    'blood_pressure_sys': np.random.randint(110, 130, n_p1),
    'blood_pressure_dia': np.random.randint(70, 85, n_p1),
    'glucose': np.random.uniform(70, 100, n_p1),
    'cholesterol': np.random.uniform(150, 200, n_p1),
    'heart_rate': np.random.randint(60, 80, n_p1),
    'group_true': 'Healthy'
})
patient_groups.append(pg1)

# Group 2: Pre-diabetic/At-risk (30%)
n_p2 = 240
pg2 = pd.DataFrame({
    'patient_id': range(n_p1+1, n_p1+n_p2+1),
    'age': np.random.randint(35, 65, n_p2),
    'bmi': np.random.uniform(25, 30, n_p2),
    'blood_pressure_sys': np.random.randint(130, 150, n_p2),
    'blood_pressure_dia': np.random.randint(85, 95, n_p2),
    'glucose': np.random.uniform(100, 125, n_p2),
    'cholesterol': np.random.uniform(200, 240, n_p2),
    'heart_rate': np.random.randint(75, 90, n_p2),
    'group_true': 'Pre-diabetic'
})
patient_groups.append(pg2)

# Group 3: High-risk/Chronic (20%)
n_p3 = 160
pg3 = pd.DataFrame({
    'patient_id': range(n_p1+n_p2+1, n_p1+n_p2+n_p3+1),
    'age': np.random.randint(50, 80, n_p3),
    'bmi': np.random.uniform(30, 40, n_p3),
    'blood_pressure_sys': np.random.randint(150, 180, n_p3),
    'blood_pressure_dia': np.random.randint(95, 115, n_p3),
    'glucose': np.random.uniform(126, 200, n_p3),
    'cholesterol': np.random.uniform(240, 300, n_p3),
    'heart_rate': np.random.randint(80, 100, n_p3),
    'group_true': 'High-risk'
})
patient_groups.append(pg3)

# Group 4: Elderly (10%)
n_p4 = 80
pg4 = pd.DataFrame({
    'patient_id': range(n_p1+n_p2+n_p3+1, n_p1+n_p2+n_p3+n_p4+1),
    'age': np.random.randint(70, 90, n_p4),
    'bmi': np.random.uniform(22, 28, n_p4),
    'blood_pressure_sys': np.random.randint(120, 160, n_p4),
    'blood_pressure_dia': np.random.randint(75, 95, n_p4),
    'glucose': np.random.uniform(90, 130, n_p4),
    'cholesterol': np.random.uniform(180, 240, n_p4),
    'heart_rate': np.random.randint(65, 85, n_p4),
    'group_true': 'Elderly'
})
patient_groups.append(pg4)

patients = pd.concat(patient_groups, ignore_index=True)
patients = patients.sample(frac=1, random_state=42).reset_index(drop=True)
patients.to_csv('data/patient_health_data.csv', index=False)
print(f"   ✓ Generated {len(patients)} patients with 4 health profiles")
print(f"   ✓ Saved to: data/patient_health_data.csv")

# ============================================================================
# Dataset 3: News Articles (for text clustering)
# ============================================================================
print("\n[3/5] Generating News Articles Dataset...")
np.random.seed(42)

# Create simple synthetic news articles with 3 topics
sports_keywords = ['football', 'soccer', 'basketball', 'player', 'team', 'game', 'match', 'championship', 'win', 'score']
tech_keywords = ['technology', 'AI', 'artificial intelligence', 'machine learning', 'smartphone', 'app', 'software', 'innovation', 'data', 'cybersecurity']
business_keywords = ['stock', 'market', 'investment', 'company', 'profit', 'revenue', 'business', 'economy', 'finance', 'trading']

def generate_article(keywords, num_words=30):
    return ' '.join(np.random.choice(keywords, size=num_words, replace=True))

articles = []
n_per_category = 400

for _ in range(n_per_category):
    articles.append({'text': generate_article(sports_keywords), 'category': 'Sports'})
    articles.append({'text': generate_article(tech_keywords), 'category': 'Technology'})
    articles.append({'text': generate_article(business_keywords), 'category': 'Business'})

news_df = pd.DataFrame(articles)
news_df = news_df.sample(frac=1, random_state=42).reset_index(drop=True)
news_df.insert(0, 'article_id', range(1, len(news_df)+1))
news_df.to_csv('data/news_articles.csv', index=False)
print(f"   ✓ Generated {len(news_df)} news articles in 3 categories")
print(f"   ✓ Saved to: data/news_articles.csv")

# ============================================================================
# Dataset 4: MNIST Digits (built-in to sklearn)
# ============================================================================
print("\n[4/5] Loading MNIST Digits Dataset...")
digits = load_digits()
print(f"   ✓ MNIST Digits available via sklearn.datasets.load_digits()")
print(f"   ✓ {digits.data.shape[0]} samples, {digits.data.shape[1]} features (8x8 images)")
print(f"   ✓ 10 digit classes (0-9)")
print(f"   ✓ No download needed - built into scikit-learn!")

# ============================================================================
# Dataset 5: Credit Card Fraud Data (for anomaly detection)
# ============================================================================
print("\n[5/5] Generating Credit Card Fraud Dataset...")
np.random.seed(42)
n_normal = 9500
n_fraud = 500

# Normal transactions
normal = pd.DataFrame({
    'transaction_id': range(1, n_normal+1),
    'amount': np.random.gamma(2, 50, n_normal),
    'time_of_day': np.random.uniform(6, 23, n_normal),
    'distance_from_home': np.random.exponential(5, n_normal),
    'num_transactions_24h': np.random.poisson(3, n_normal),
    'merchant_risk_score': np.random.uniform(0, 0.3, n_normal),
    'is_fraud': 0
})

# Fraudulent transactions (anomalous patterns)
fraud = pd.DataFrame({
    'transaction_id': range(n_normal+1, n_normal+n_fraud+1),
    'amount': np.random.uniform(500, 5000, n_fraud),
    'time_of_day': np.random.choice([2, 3, 4, 5], n_fraud),
    'distance_from_home': np.random.uniform(100, 500, n_fraud),
    'num_transactions_24h': np.random.poisson(15, n_fraud),
    'merchant_risk_score': np.random.uniform(0.7, 1.0, n_fraud),
    'is_fraud': 1
})

fraud_data = pd.concat([normal, fraud], ignore_index=True)
fraud_data = fraud_data.sample(frac=1, random_state=42).reset_index(drop=True)
fraud_data.to_csv('data/credit_card_fraud.csv', index=False)
print(f"   ✓ Generated {len(fraud_data)} transactions")
print(f"   ✓ Normal: {n_normal} ({n_normal/len(fraud_data)*100:.1f}%)")
print(f"   ✓ Fraud: {n_fraud} ({n_fraud/len(fraud_data)*100:.1f}%)")
print(f"   ✓ Saved to: data/credit_card_fraud.csv")

# ============================================================================
# Summary
# ============================================================================
print("\n" + "="*70)
print("DATASET GENERATION COMPLETE!")
print("="*70)
print("\nGenerated Datasets:")
print("  1. data/ecommerce_customers.csv       - 2,000 customers, 5 segments")
print("  2. data/patient_health_data.csv       - 800 patients, 4 health groups")
print("  3. data/news_articles.csv             - 1,200 articles, 3 topics")
print("  4. MNIST Digits (sklearn built-in)    - 1,797 images, 10 digits")
print("  5. data/credit_card_fraud.csv         - 10,000 transactions, 5% fraud")
print("\nAll datasets are synthetic and reproducible (seed=42)")
print("Ready for Module 5 unsupervised learning exercises!")
print("="*70)
