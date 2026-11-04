"""
Automated dataset downloader for Module 7: Computer Vision
Downloads all required datasets for sessions 7.1-7.6
"""

import os
import sys
import requests
from pathlib import Path
import gzip
import shutil
import zipfile
import tarfile
from tqdm import tqdm

# Base directory for datasets
BASE_DIR = Path(__file__).parent / "data"
BASE_DIR.mkdir(exist_ok=True)

def download_file(url, destination):
    """Download file with progress bar"""
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))

    with open(destination, 'wb') as file, tqdm(
        desc=destination.name,
        total=total_size,
        unit='B',
        unit_scale=True,
        unit_divisor=1024,
    ) as progress_bar:
        for data in response.iter_content(chunk_size=1024):
            size = file.write(data)
            progress_bar.update(size)

def extract_archive(archive_path, extract_to):
    """Extract zip, tar, or gz archives"""
    print(f"Extracting {archive_path.name}...")

    if archive_path.suffix == '.zip':
        with zipfile.ZipFile(archive_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
    elif archive_path.suffix in ['.tar', '.gz', '.tgz']:
        with tarfile.open(archive_path, 'r:*') as tar_ref:
            tar_ref.extractall(extract_to)
    elif archive_path.suffix == '.gz':
        with gzip.open(archive_path, 'rb') as f_in:
            with open(extract_to / archive_path.stem, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)

    print(f"✓ Extracted to {extract_to}")

def download_mnist():
    """Download MNIST dataset (Session 7.1)"""
    print("\n" + "="*60)
    print("DOWNLOADING MNIST DATASET (Session 7.1)")
    print("="*60)

    # MNIST is built into Keras - no download needed
    print("✓ MNIST is built into TensorFlow/Keras")
    print("  Access with: tf.keras.datasets.mnist.load_data()")
    return True

def download_cifar10():
    """Download CIFAR-10 dataset (Session 7.2)"""
    print("\n" + "="*60)
    print("DOWNLOADING CIFAR-10 DATASET (Session 7.2)")
    print("="*60)

    # CIFAR-10 is built into Keras
    print("✓ CIFAR-10 is built into TensorFlow/Keras")
    print("  Access with: tf.keras.datasets.cifar10.load_data()")
    return True

def download_cats_vs_dogs():
    """Download Cats vs Dogs dataset (Session 7.3)"""
    print("\n" + "="*60)
    print("DOWNLOADING CATS VS DOGS DATASET (Session 7.3)")
    print("="*60)

    cats_dogs_dir = BASE_DIR / "cats_vs_dogs"

    if cats_dogs_dir.exists():
        print("✓ Cats vs Dogs dataset already exists")
        return True

    print("Option 1: Download via TensorFlow Datasets")
    print("  pip install tensorflow-datasets")
    print("  import tensorflow_datasets as tfds")
    print("  ds = tfds.load('cats_vs_dogs', split='train')")

    print("\nOption 2: Manual Download from Kaggle")
    print("  1. Install Kaggle CLI: pip install kaggle")
    print("  2. Configure Kaggle API (download kaggle.json from kaggle.com/account)")
    print("  3. Run: kaggle datasets download -d salader/dogs-vs-cats")

    print("\nOption 3: Use subset from Microsoft")
    url = "https://download.microsoft.com/download/3/E/1/3E1C3F21-ECDB-4869-8368-6DEBA77B919F/kagglecatsanddogs_5340.zip"

    try:
        cats_dogs_zip = BASE_DIR / "cats_vs_dogs.zip"
        print(f"\nDownloading from Microsoft... (800MB)")
        download_file(url, cats_dogs_zip)
        extract_archive(cats_dogs_zip, cats_dogs_dir)
        cats_dogs_zip.unlink()  # Remove zip file
        print("✓ Cats vs Dogs dataset downloaded successfully")
        return True
    except Exception as e:
        print(f"⚠ Automatic download failed: {e}")
        print("Please download manually from the links above.")
        return False

def download_chest_xray():
    """Download Chest X-Ray dataset (Session 7.5)"""
    print("\n" + "="*60)
    print("DOWNLOADING CHEST X-RAY DATASET (Session 7.5)")
    print("="*60)

    print("⚠ This dataset requires manual download from Kaggle")
    print("\nSteps:")
    print("1. Go to: https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia")
    print("2. Download the dataset (1.2GB)")
    print("3. Extract to:", BASE_DIR / "chest_xray")
    print("\nOR use Kaggle API:")
    print("  kaggle datasets download -d paultimothymooney/chest-xray-pneumonia")
    print("  unzip chest-xray-pneumonia.zip -d", BASE_DIR / "chest_xray")

    return False  # Requires manual download

def download_casting_defects():
    """Download manufacturing defect dataset (Session 7.6)"""
    print("\n" + "="*60)
    print("DOWNLOADING CASTING DEFECT DATASET (Session 7.6)")
    print("="*60)

    print("⚠ This dataset requires manual download from Kaggle")
    print("\nSteps:")
    print("1. Go to: https://www.kaggle.com/datasets/ravirajsinh45/real-life-industrial-dataset-of-casting-product")
    print("2. Download the dataset")
    print("3. Extract to:", BASE_DIR / "casting_defects")
    print("\nOR use Kaggle API:")
    print("  kaggle datasets download -d ravirajsinh45/real-life-industrial-dataset-of-casting-product")

    return False

def download_cricket_shots():
    """Instructions for cricket shot dataset (Capstone)"""
    print("\n" + "="*60)
    print("CRICKET SHOT DATASET (Capstone Project)")
    print("="*60)

    print("⚠ This dataset needs to be collected manually")
    print("\nOptions:")
    print("1. Collect images from cricket match videos")
    print("2. Use cricket photo galleries (with proper licensing)")
    print("3. Generate synthetic data")
    print("\nRequired structure:")
    print("  data/cricket_shots/")
    print("    train/")
    print("      cover_drive/ (200-300 images)")
    print("      straight_drive/ (200-300 images)")
    print("      pull/ (200-300 images)")
    print("      hook/ (200-300 images)")
    print("      sweep/ (200-300 images)")
    print("      defensive/ (200-300 images)")
    print("    test/ (same structure)")

    print("\nRecommended sources:")
    print("- ICC/ESPN Cricinfo image galleries")
    print("- YouTube cricket highlight videos (screenshot)")
    print("- Pexels/Unsplash (free cricket images)")

    return False

def setup_kaggle_api():
    """Helper to setup Kaggle API"""
    print("\n" + "="*60)
    print("KAGGLE API SETUP")
    print("="*60)

    print("To download datasets from Kaggle:")
    print("\n1. Install Kaggle CLI:")
    print("   pip install kaggle")

    print("\n2. Get API credentials:")
    print("   - Go to https://www.kaggle.com/account")
    print("   - Click 'Create New API Token'")
    print("   - Download kaggle.json")

    print("\n3. Place credentials:")
    print("   - Linux/Mac: ~/.kaggle/kaggle.json")
    print("   - Windows: C:\\Users\\<Username>\\.kaggle\\kaggle.json")

    print("\n4. Set permissions (Linux/Mac):")
    print("   chmod 600 ~/.kaggle/kaggle.json")

    print("\n5. Test:")
    print("   kaggle datasets list")

def main():
    """Main download function"""
    print("="*60)
    print("MODULE 7: COMPUTER VISION - DATASET DOWNLOADER")
    print("="*60)

    print(f"\nDatasets will be downloaded to: {BASE_DIR.absolute()}")

    # Download datasets
    datasets = {
        "MNIST": download_mnist,
        "CIFAR-10": download_cifar10,
        "Cats vs Dogs": download_cats_vs_dogs,
        "Chest X-Ray": download_chest_xray,
        "Casting Defects": download_casting_defects,
        "Cricket Shots": download_cricket_shots
    }

    results = {}

    for name, download_func in datasets.items():
        try:
            success = download_func()
            results[name] = "✓ Ready" if success else "⚠ Manual required"
        except Exception as e:
            results[name] = f"✗ Error: {str(e)}"

    # Summary
    print("\n" + "="*60)
    print("DOWNLOAD SUMMARY")
    print("="*60)

    for name, status in results.items():
        print(f"{name:20s}: {status}")

    print("\n" + "="*60)
    print("NEXT STEPS")
    print("="*60)
    print("1. For manual downloads, follow the instructions above")
    print("2. Organize datasets in the specified directory structure")
    print("3. Run dataset_info.py to verify all datasets")

    # Kaggle setup info
    setup_kaggle_api()

if __name__ == "__main__":
    main()
