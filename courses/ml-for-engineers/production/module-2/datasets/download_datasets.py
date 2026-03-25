"""
Module 2: Classification Datasets Download Script
Downloads and prepares all datasets for classification projects

Datasets:
1. Iris - sklearn built-in
2. Spam Email - SMS Spam Collection
3. Customer Churn - Telco Customer Churn
4. Heart Disease - UCI Heart Disease
5. MNIST - tensorflow/keras built-in
6. Cricket Matches - IPL dataset

Author: ML for Engineers Course
Date: 2026-01-05
"""

import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
import tensorflow as tf
import os
import urllib.request
import zipfile

# Create data directory if it doesn't exist
DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)

print("=" * 60)
print("MODULE 2: CLASSIFICATION DATASETS DOWNLOAD")
print("=" * 60)

# ================================================================
# DATASET 1: IRIS (Built-in)
# ================================================================
print("\n[1/6] Loading Iris Dataset...")
try:
    iris = load_iris()
    iris_df = pd.DataFrame(
        data=iris.data,
        columns=iris.feature_names
    )
    iris_df['species'] = iris.target
    iris_df['species_name'] = iris_df['species'].map({
        0: 'setosa',
        1: 'versicolor',
        2: 'virginica'
    })

    iris_df.to_csv(f"{DATA_DIR}/iris.csv", index=False)
    print(f"✓ Iris dataset saved: {len(iris_df)} samples")
    print(f"  Features: {iris.feature_names}")
    print(f"  Classes: {iris.target_names}")
except Exception as e:
    print(f"✗ Error loading Iris: {e}")

# ================================================================
# DATASET 2: SPAM EMAIL (SMS Spam Collection)
# ================================================================
print("\n[2/6] Downloading Spam Email Dataset...")
try:
    # UCI ML Repository - SMS Spam Collection
    spam_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00228/smsspamcollection.zip"
    spam_zip_path = f"{DATA_DIR}/spam.zip"

    print("  Downloading from UCI ML Repository...")
    urllib.request.urlretrieve(spam_url, spam_zip_path)

    # Extract
    with zipfile.ZipFile(spam_zip_path, 'r') as zip_ref:
        zip_ref.extractall(DATA_DIR)

    # Read and format
    spam_df = pd.read_csv(
        f"{DATA_DIR}/SMSSpamCollection",
        sep='\t',
        names=['label', 'message'],
        encoding='latin-1'
    )

    spam_df.to_csv(f"{DATA_DIR}/spam_email.csv", index=False)

    print(f"✓ Spam email dataset saved: {len(spam_df)} samples")
    print(f"  Spam: {len(spam_df[spam_df['label']=='spam'])}")
    print(f"  Ham: {len(spam_df[spam_df['label']=='ham'])}")

    # Cleanup
    os.remove(spam_zip_path)
    os.remove(f"{DATA_DIR}/SMSSpamCollection")
    if os.path.exists(f"{DATA_DIR}/readme"):
        os.remove(f"{DATA_DIR}/readme")

except Exception as e:
    print(f"✗ Error downloading Spam dataset: {e}")
    print("  Manual download: https://archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection")

# ================================================================
# DATASET 3: CUSTOMER CHURN (Telco)
# ================================================================
print("\n[3/6] Downloading Customer Churn Dataset...")
try:
    # Kaggle dataset - Telco Customer Churn
    churn_url = "https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/data/Telco-Customer-Churn.csv"

    print("  Downloading Telco Customer Churn dataset...")
    churn_df = pd.read_csv(churn_url)

    # Clean TotalCharges column (has some spaces)
    churn_df['TotalCharges'] = pd.to_numeric(churn_df['TotalCharges'], errors='coerce')
    churn_df = churn_df.dropna()

    churn_df.to_csv(f"{DATA_DIR}/customer_churn.csv", index=False)

    print(f"✓ Customer churn dataset saved: {len(churn_df)} samples")
    print(f"  Churned: {len(churn_df[churn_df['Churn']=='Yes'])}")
    print(f"  Retained: {len(churn_df[churn_df['Churn']=='No'])}")
    print(f"  Features: {len(churn_df.columns)} columns")

except Exception as e:
    print(f"✗ Error downloading Churn dataset: {e}")
    print("  Manual download: https://www.kaggle.com/blastchar/telco-customer-churn")

# ================================================================
# DATASET 4: HEART DISEASE (UCI)
# ================================================================
print("\n[4/6] Downloading Heart Disease Dataset...")
try:
    # UCI Heart Disease dataset
    heart_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.cleveland.data"

    print("  Downloading UCI Heart Disease dataset...")

    # Column names
    column_names = [
        'age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg',
        'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'target'
    ]

    heart_df = pd.read_csv(heart_url, names=column_names, na_values='?')

    # Binary classification: 0 = no disease, 1-4 = disease present
    heart_df['target'] = (heart_df['target'] > 0).astype(int)

    # Drop rows with missing values
    heart_df = heart_df.dropna()

    heart_df.to_csv(f"{DATA_DIR}/heart_disease.csv", index=False)

    print(f"✓ Heart disease dataset saved: {len(heart_df)} samples")
    print(f"  Disease: {len(heart_df[heart_df['target']==1])}")
    print(f"  No disease: {len(heart_df[heart_df['target']==0])}")
    print(f"  Features: {len(heart_df.columns)-1} columns")

except Exception as e:
    print(f"✗ Error downloading Heart Disease dataset: {e}")
    print("  Manual download: https://archive.ics.uci.edu/ml/datasets/Heart+Disease")

# ================================================================
# DATASET 5: MNIST (Built-in)
# ================================================================
print("\n[5/6] Loading MNIST Dataset...")
try:
    print("  Loading from TensorFlow/Keras...")
    (X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()

    # Save a subset for faster training (first 10000 samples)
    mnist_subset_size = 10000

    # Flatten images for CSV storage
    X_train_flat = X_train[:mnist_subset_size].reshape(mnist_subset_size, -1)
    y_train_subset = y_train[:mnist_subset_size]

    # Create DataFrame
    mnist_df = pd.DataFrame(X_train_flat)
    mnist_df['label'] = y_train_subset

    mnist_df.to_csv(f"{DATA_DIR}/mnist_subset.csv", index=False)

    print(f"✓ MNIST dataset saved: {mnist_subset_size} samples (subset)")
    print(f"  Original training: {len(X_train)} samples")
    print(f"  Original test: {len(X_test)} samples")
    print(f"  Image size: 28x28 pixels")
    print(f"  Classes: 0-9 (digits)")
    print("  Note: Use tf.keras.datasets.mnist.load_data() for full dataset")

except Exception as e:
    print(f"✗ Error loading MNIST: {e}")

# ================================================================
# DATASET 6: CRICKET MATCHES (IPL)
# ================================================================
print("\n[6/6] Downloading Cricket Match Dataset...")
try:
    # IPL matches dataset
    cricket_url = "https://raw.githubusercontent.com/codophilic/IPL-Data-Analysis/master/matches.csv"

    print("  Downloading IPL matches dataset...")
    cricket_df = pd.read_csv(cricket_url)

    # Keep relevant columns
    cricket_df = cricket_df[[
        'season', 'team1', 'team2', 'toss_winner', 'toss_decision',
        'winner', 'venue', 'result'
    ]].dropna()

    cricket_df.to_csv(f"{DATA_DIR}/cricket_matches.csv", index=False)

    print(f"✓ Cricket matches dataset saved: {len(cricket_df)} samples")
    print(f"  Seasons: {cricket_df['season'].min()} - {cricket_df['season'].max()}")
    print(f"  Unique teams: {cricket_df['team1'].nunique()}")
    print(f"  Venues: {cricket_df['venue'].nunique()}")

except Exception as e:
    print(f"✗ Error downloading Cricket dataset: {e}")
    print("  Manual download: https://www.kaggle.com/nowke9/ipldata")

# ================================================================
# SUMMARY
# ================================================================
print("\n" + "=" * 60)
print("DOWNLOAD COMPLETE")
print("=" * 60)

print("\nDatasets saved in:", os.path.abspath(DATA_DIR))
print("\nFiles created:")
for file in sorted(os.listdir(DATA_DIR)):
    if file.endswith('.csv'):
        filepath = os.path.join(DATA_DIR, file)
        size_mb = os.path.getsize(filepath) / (1024 * 1024)
        print(f"  • {file:<25} ({size_mb:.2f} MB)")

print("\n" + "=" * 60)
print("Next steps:")
print("1. Review data dictionaries in datasets-readme.md")
print("2. Load datasets in Jupyter notebooks")
print("3. Start building classification models!")
print("=" * 60)
