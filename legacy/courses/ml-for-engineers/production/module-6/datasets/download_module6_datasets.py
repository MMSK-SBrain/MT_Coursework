#!/usr/bin/env python3
"""
Module 6 Dataset Download Script
Neural Networks & Deep Learning

Datasets needed:
1. MNIST - Built into Keras
2. Fashion MNIST - Built into Keras
3. Iris - Built into sklearn
4. Stock Data - Reuse from Module 3
5. Flowers/Cats vs Dogs - TensorFlow Datasets or Kaggle

Usage:
    python download_module6_datasets.py
"""

import os
import sys
import numpy as np
import tensorflow as tf
from tensorflow import keras
from sklearn.datasets import load_iris
import yfinance as yf
from datetime import datetime

print("="*70)
print("MODULE 6: DATASET DOWNLOAD AND VERIFICATION")
print("="*70)

# Create directories
os.makedirs('data', exist_ok=True)
os.makedirs('data/stock', exist_ok=True)

def download_mnist():
    """Download MNIST (built-in to Keras)"""
    print("\n1. MNIST Digits Dataset")
    print("-" * 70)
    try:
        from tensorflow.keras.datasets import mnist
        (X_train, y_train), (X_test, y_test) = mnist.load_data()
        print(f"✅ MNIST loaded successfully")
        print(f"   Training samples: {X_train.shape[0]}")
        print(f"   Test samples: {X_test.shape[0]}")
        print(f"   Image shape: {X_train.shape[1:]} ")
        print(f"   Classes: {np.unique(y_train)}")
        return True
    except Exception as e:
        print(f"❌ Error loading MNIST: {e}")
        return False

def download_fashion_mnist():
    """Download Fashion MNIST (built-in to Keras)"""
    print("\n2. Fashion MNIST Dataset")
    print("-" * 70)
    try:
        from tensorflow.keras.datasets import fashion_mnist
        (X_train, y_train), (X_test, y_test) = fashion_mnist.load_data()
        print(f"✅ Fashion MNIST loaded successfully")
        print(f"   Training samples: {X_train.shape[0]}")
        print(f"   Test samples: {X_test.shape[0]}")
        print(f"   Image shape: {X_train.shape[1:]}")
        print(f"   Classes: T-shirt, Trouser, Pullover, Dress, Coat,")
        print(f"            Sandal, Shirt, Sneaker, Bag, Ankle boot")
        return True
    except Exception as e:
        print(f"❌ Error loading Fashion MNIST: {e}")
        return False

def download_iris():
    """Download Iris (built-in to sklearn)"""
    print("\n3. Iris Dataset")
    print("-" * 70)
    try:
        iris = load_iris()
        print(f"✅ Iris loaded successfully")
        print(f"   Samples: {iris.data.shape[0]}")
        print(f"   Features: {iris.data.shape[1]}")
        print(f"   Classes: {iris.target_names.tolist()}")
        return True
    except Exception as e:
        print(f"❌ Error loading Iris: {e}")
        return False

def download_stock_data():
    """Download stock data for stock predictor"""
    print("\n4. Stock Data (for Stock Predictor Capstone)")
    print("-" * 70)

    tickers = ['AAPL', 'GOOGL', 'MSFT']
    success = True

    for ticker in tickers:
        try:
            print(f"   Downloading {ticker}...")
            df = yf.download(ticker, period='5y', progress=False)
            if len(df) > 0:
                filename = f"data/stock/{ticker}_5y.csv"
                df.to_csv(filename)
                print(f"   ✅ {ticker}: {len(df)} days → {filename}")
            else:
                print(f"   ⚠️ {ticker}: No data downloaded")
                success = False
        except Exception as e:
            print(f"   ❌ {ticker}: Error - {e}")
            success = False

    if success:
        print(f"\n✅ Stock data downloaded successfully")
        print(f"   Note: Can also reuse Module 3 stock data")

    return success

def download_transfer_learning_data():
    """Instructions for transfer learning dataset"""
    print("\n5. Transfer Learning Dataset (Flowers or Cats vs Dogs)")
    print("-" * 70)
    print("📋 Manual download required:")
    print()
    print("Option 1: TensorFlow Flowers Dataset")
    print("   import tensorflow_datasets as tfds")
    print("   tfds.load('tf_flowers', split='train', as_supervised=True)")
    print()
    print("Option 2: Kaggle Cats vs Dogs")
    print("   1. Install kaggle: pip install kaggle")
    print("   2. Setup API key: ~/.kaggle/kaggle.json")
    print("   3. Download: kaggle competitions download -c dogs-vs-cats")
    print()
    print("Option 3: Use ImageDataGenerator with local images")
    print("   Place images in: data/flowers/class1/, data/flowers/class2/, etc.")
    print()
    print("⚠️ This dataset is optional for transfer learning session")
    print("   Notebooks will work with any image dataset")
    return True

def verify_tensorflow():
    """Verify TensorFlow installation"""
    print("\n6. TensorFlow Verification")
    print("-" * 70)
    print(f"   TensorFlow version: {tf.__version__}")
    print(f"   Keras version: {keras.__version__}")

    # Check for GPU
    gpus = tf.config.list_physical_devices('GPU')
    if gpus:
        print(f"   ✅ GPU available: {len(gpus)} device(s)")
        for i, gpu in enumerate(gpus):
            print(f"      GPU {i}: {gpu.name}")
    else:
        print(f"   ⚠️ No GPU detected (CPU only)")
        print(f"      Neural networks will train slower but will work!")

    return True

def print_summary(results):
    """Print summary of downloads"""
    print("\n" + "="*70)
    print("DOWNLOAD SUMMARY")
    print("="*70)

    datasets = [
        ("MNIST Digits", results[0]),
        ("Fashion MNIST", results[1]),
        ("Iris", results[2]),
        ("Stock Data", results[3]),
        ("Transfer Learning (manual)", results[4]),
        ("TensorFlow Verified", results[5])
    ]

    success_count = sum(results)
    total_count = len(results)

    for name, status in datasets:
        status_symbol = "✅" if status else "❌"
        print(f"{status_symbol} {name}")

    print("="*70)
    print(f"\nSuccess Rate: {success_count}/{total_count} datasets ready")

    if success_count == total_count:
        print("\n🎉 All datasets ready! You can start Module 6!")
    elif success_count >= 4:
        print("\n✅ Core datasets ready! You can start most notebooks.")
        print("   Transfer learning dataset is optional.")
    else:
        print("\n⚠️ Some datasets failed to download.")
        print("   Check error messages above and try again.")

    print("\n📚 Next Steps:")
    print("   1. Start with Session 1: iris-neural-network.ipynb")
    print("   2. Progress to Session 2: mnist-digit-recognition.ipynb")
    print("   3. Build up to Capstone: stock-predictor-neural-network.ipynb")

def main():
    """Main download function"""
    print("\nStarting dataset downloads...")
    print("This may take a few minutes...\n")

    results = []

    # Download all datasets
    results.append(download_mnist())
    results.append(download_fashion_mnist())
    results.append(download_iris())
    results.append(download_stock_data())
    results.append(download_transfer_learning_data())
    results.append(verify_tensorflow())

    # Print summary
    print_summary(results)

    # Additional info
    print("\n" + "="*70)
    print("ADDITIONAL INFORMATION")
    print("="*70)
    print("\n📦 Dataset Sizes:")
    print("   MNIST: ~11 MB")
    print("   Fashion MNIST: ~25 MB")
    print("   Iris: <1 MB")
    print("   Stock Data: ~2 MB")
    print("   Flowers/Cats-Dogs: ~500 MB - 1 GB")
    print()
    print("💻 System Requirements:")
    print("   RAM: 8 GB minimum, 16 GB recommended")
    print("   Disk Space: 2 GB minimum (without transfer learning data)")
    print("   GPU: Optional but recommended for faster training")
    print()
    print("📖 Documentation:")
    print("   See datasets-readme.md for detailed information")
    print("   See each notebook for specific data preparation")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️ Download interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Unexpected error: {e}")
        sys.exit(1)
