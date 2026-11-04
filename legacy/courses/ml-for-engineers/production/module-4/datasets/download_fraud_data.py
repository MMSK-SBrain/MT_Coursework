"""
Credit Card Fraud Detection Dataset Downloader
Module 4 - Model Evaluation & Optimization

This script provides two options for obtaining fraud detection data:
1. Download from Kaggle (requires Kaggle API credentials)
2. Generate synthetic dataset that mimics real fraud detection characteristics

The synthetic option is production-ready and creates realistic data for learning purposes.
"""

import pandas as pd
import numpy as np
import os
import sys
from pathlib import Path

def generate_synthetic_fraud_dataset(
    n_samples=284807,
    fraud_rate=0.00172,
    random_state=42,
    save_path='data/creditcard.csv'
):
    """
    Generate synthetic credit card fraud dataset similar to the Kaggle dataset.

    This function creates a realistic dataset with:
    - PCA-transformed features (V1-V28)
    - Time feature (seconds from first transaction)
    - Amount feature (transaction amount)
    - Class label (0=normal, 1=fraud)
    - Realistic fraud patterns and distributions

    Parameters:
    -----------
    n_samples : int
        Total number of transactions (default: 284,807)
    fraud_rate : float
        Percentage of fraudulent transactions (default: 0.172%)
    random_state : int
        Random seed for reproducibility
    save_path : str
        Path to save the generated CSV file

    Returns:
    --------
    pd.DataFrame
        DataFrame with fraud detection data
    """

    print("="*70)
    print("GENERATING SYNTHETIC CREDIT CARD FRAUD DATASET")
    print("="*70)

    np.random.seed(random_state)

    # Calculate number of fraud and normal transactions
    n_fraud = int(n_samples * fraud_rate)
    n_normal = n_samples - n_fraud

    print(f"\nDataset Configuration:")
    print(f"  Total transactions: {n_samples:,}")
    print(f"  Normal transactions: {n_normal:,}")
    print(f"  Fraudulent transactions: {n_fraud:,}")
    print(f"  Fraud rate: {fraud_rate*100:.4f}%")
    print(f"  Imbalance ratio: 1:{int(n_normal/n_fraud)}")

    # Generate Time feature (seconds elapsed from first transaction)
    # Simulate 2 days of transactions (172,800 seconds)
    time = np.sort(np.random.uniform(0, 172800, n_samples))

    print(f"\n  Time range: 0 to {int(time.max())} seconds (~{time.max()/3600:.1f} hours)")

    # Generate V1-V28 features (PCA-transformed features)
    # Normal transactions: Standard normal distribution
    # Fraud transactions: Different distributions with specific patterns
    print("\n  Generating V1-V28 features (PCA components)...")

    features_normal = np.random.normal(0, 1, (n_normal, 28))
    features_fraud = np.random.normal(0, 1.5, (n_fraud, 28))  # Higher variance for fraud

    # Add specific patterns to certain features (based on real fraud patterns)
    # These features are known to be important fraud indicators
    important_features = {
        'V4': (2, 0.5, 'positive'),   # V5 in final (index 4)
        'V11': (2, 0.5, 'positive'),  # V12 in final
        'V14': (2, 0.5, 'positive'),  # V15 in final
        'V17': (2, 0.5, 'positive'),  # V18 in final
        'V10': (-2, 0.5, 'negative'), # V11 in final
        'V12': (-2, 0.5, 'negative'), # V13 in final
        'V16': (-2, 0.5, 'negative'), # V17 in final
    }

    for feature_idx, (mean, std, direction) in important_features.items():
        idx = int(feature_idx.replace('V', '')) if isinstance(feature_idx, str) else feature_idx
        if direction == 'positive':
            features_fraud[:, idx] += np.random.normal(mean, std, n_fraud)
        else:
            features_fraud[:, idx] -= np.random.normal(abs(mean), std, n_fraud)

    # Combine normal and fraud features
    V_features = np.vstack([features_normal, features_fraud])

    # Generate Amount feature
    # Normal transactions: Mostly small to medium amounts (lognormal distribution)
    # Fraud transactions: Mix of small and large amounts
    print("  Generating transaction amounts...")

    amount_normal = np.random.lognormal(mean=3.0, sigma=1.5, size=n_normal)

    # Fraud: 50% small amounts (testing stolen cards), 50% large amounts (maxing out cards)
    amount_fraud_small = np.random.lognormal(mean=2.0, sigma=1.0, size=n_fraud//2)
    amount_fraud_large = np.random.lognormal(mean=5.0, sigma=1.0, size=n_fraud - n_fraud//2)
    amount_fraud = np.concatenate([amount_fraud_small, amount_fraud_large])

    amount = np.concatenate([amount_normal, amount_fraud])

    # Cap amounts at realistic maximum (based on real data)
    amount = np.clip(amount, 0.01, 25691.16)

    # Create labels
    labels = np.concatenate([np.zeros(n_normal), np.ones(n_fraud)])

    # Shuffle all data together (maintaining correspondence)
    print("\n  Shuffling data...")
    shuffle_idx = np.random.permutation(n_samples)
    V_features = V_features[shuffle_idx]
    time = time[shuffle_idx]
    amount = amount[shuffle_idx]
    labels = labels[shuffle_idx]

    # Create DataFrame
    print("  Creating DataFrame...")
    data = pd.DataFrame(V_features, columns=[f'V{i}' for i in range(1, 29)])
    data['Time'] = time
    data['Amount'] = amount
    data['Class'] = labels.astype(int)

    # Reorder columns to match real dataset format
    cols = ['Time'] + [f'V{i}' for i in range(1, 29)] + ['Amount', 'Class']
    data = data[cols]

    # Save to CSV
    print(f"\n  Saving to {save_path}...")
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    data.to_csv(save_path, index=False)

    # Display statistics
    print("\n" + "="*70)
    print("DATASET GENERATED SUCCESSFULLY!")
    print("="*70)
    print(f"\nFile saved: {save_path}")
    print(f"File size: {os.path.getsize(save_path) / (1024*1024):.2f} MB")
    print(f"\nDataset shape: {data.shape}")
    print(f"Features: {data.shape[1] - 1} (30 features + 1 target)")

    print(f"\nClass distribution:")
    print(data['Class'].value_counts().to_string())
    print(f"\nActual fraud rate: {data['Class'].mean()*100:.4f}%")

    print(f"\nAmount statistics:")
    print(f"  Normal transactions:")
    print(f"    Mean: ${data[data['Class']==0]['Amount'].mean():.2f}")
    print(f"    Median: ${data[data['Class']==0]['Amount'].median():.2f}")
    print(f"    Max: ${data[data['Class']==0]['Amount'].max():.2f}")
    print(f"  Fraudulent transactions:")
    print(f"    Mean: ${data[data['Class']==1]['Amount'].mean():.2f}")
    print(f"    Median: ${data[data['Class']==1]['Amount'].median():.2f}")
    print(f"    Max: ${data[data['Class']==1]['Amount'].max():.2f}")

    print(f"\nTime span: {data['Time'].min():.0f} to {data['Time'].max():.0f} seconds")
    print(f"  (~{data['Time'].max()/3600:.1f} hours or ~{data['Time'].max()/86400:.1f} days)")

    return data


def download_from_kaggle(save_path='data/creditcard.csv'):
    """
    Download the real Credit Card Fraud Detection dataset from Kaggle.

    Requirements:
    - Kaggle account
    - Kaggle API credentials configured (~/.kaggle/kaggle.json)
    - Dataset: https://www.kaggle.com/mlg-ulb/creditcardfraud

    Parameters:
    -----------
    save_path : str
        Path to save the downloaded CSV file

    Returns:
    --------
    pd.DataFrame or None
        DataFrame with fraud detection data, or None if download failed
    """

    print("="*70)
    print("DOWNLOADING FROM KAGGLE")
    print("="*70)

    try:
        from kaggle.api.kaggle_api_extended import KaggleApi

        print("\nInitializing Kaggle API...")
        api = KaggleApi()
        api.authenticate()

        print("Downloading dataset: mlg-ulb/creditcardfraud")
        print("This may take a few minutes...")

        # Create data directory
        os.makedirs('data', exist_ok=True)

        # Download dataset
        api.dataset_download_files(
            'mlg-ulb/creditcardfraud',
            path='data',
            unzip=True,
            quiet=False
        )

        print("\n✅ Download complete!")

        # Load and return the data
        csv_path = 'data/creditcard.csv'
        if os.path.exists(csv_path):
            print(f"\nLoading data from {csv_path}...")
            data = pd.read_csv(csv_path)
            print(f"Dataset shape: {data.shape}")
            print(f"Fraud rate: {data['Class'].mean()*100:.4f}%")
            return data
        else:
            print("⚠️ Downloaded file not found. Check the data/ directory.")
            return None

    except ImportError:
        print("\n❌ ERROR: Kaggle package not installed.")
        print("Install it with: pip install kaggle")
        print("\nAlternatively, use the synthetic dataset generator.")
        return None

    except Exception as e:
        print(f"\n❌ ERROR downloading from Kaggle: {str(e)}")
        print("\nPossible issues:")
        print("  1. Kaggle API credentials not configured")
        print("     - Create an account at kaggle.com")
        print("     - Go to Account settings -> API -> Create New API Token")
        print("     - Place kaggle.json in ~/.kaggle/")
        print("  2. Dataset not accessible")
        print("     - Accept the competition rules at:")
        print("       https://www.kaggle.com/mlg-ulb/creditcardfraud")
        print("\nAlternatively, use the synthetic dataset generator.")
        return None


def main():
    """
    Main function to download or generate fraud detection dataset.
    """

    print("\n" + "="*70)
    print("CREDIT CARD FRAUD DETECTION DATASET")
    print("Module 4 - Model Evaluation & Optimization")
    print("="*70)

    print("\nOptions:")
    print("  1. Generate synthetic dataset (RECOMMENDED for learning)")
    print("  2. Download real dataset from Kaggle (requires API credentials)")
    print("  3. Generate larger synthetic dataset (500k transactions)")
    print("  4. Exit")

    while True:
        try:
            choice = input("\nEnter your choice (1-4): ").strip()

            if choice == '1':
                print("\nGenerating standard synthetic dataset (284,807 transactions)...")
                data = generate_synthetic_fraud_dataset()
                print("\n✅ Synthetic dataset ready for use!")
                break

            elif choice == '2':
                print("\nAttempting to download from Kaggle...")
                data = download_from_kaggle()
                if data is None:
                    print("\nFalling back to synthetic dataset...")
                    data = generate_synthetic_fraud_dataset()
                print("\n✅ Dataset ready for use!")
                break

            elif choice == '3':
                print("\nGenerating large synthetic dataset (500,000 transactions)...")
                data = generate_synthetic_fraud_dataset(
                    n_samples=500000,
                    fraud_rate=0.00172,
                    save_path='data/creditcard_large.csv'
                )
                print("\n✅ Large synthetic dataset ready for use!")
                break

            elif choice == '4':
                print("\nExiting without downloading/generating data.")
                sys.exit(0)

            else:
                print("❌ Invalid choice. Please enter 1, 2, 3, or 4.")

        except KeyboardInterrupt:
            print("\n\nOperation cancelled by user.")
            sys.exit(0)
        except Exception as e:
            print(f"\n❌ Error: {str(e)}")
            print("Please try again.")

    print("\n" + "="*70)
    print("DATASET READY FOR MODULE 4 PROJECTS")
    print("="*70)
    print("\nNext steps:")
    print("  1. Open fraud-detection-system.ipynb")
    print("  2. Run the notebook cells")
    print("  3. Build your production-quality fraud detection system!")
    print("\nHappy learning! 🚀")
    print("="*70)


if __name__ == "__main__":
    main()
