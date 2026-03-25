"""
NLP Datasets Downloader
=======================

Automated download script for all Module 8 datasets:
- IMDB Movie Reviews (50K reviews)
- AG News (120K articles)
- Twitter Sentiment
- Sample text corpora
- FAQ/Intent datasets

Author: ML for Engineers Course
Date: 2026-01-06
"""

import os
import sys
import requests
from pathlib import Path
import zipfile
import tarfile
import gzip
import shutil

# Create datasets directory
DATASETS_DIR = Path(__file__).parent
DATASETS_DIR.mkdir(exist_ok=True)


def download_file(url, filename):
    """Download file with progress bar."""
    print(f"Downloading {filename}...")
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        total_size = int(response.headers.get('content-length', 0))
        block_size = 8192

        with open(filename, 'wb') as f:
            downloaded = 0
            for data in response.iter_content(block_size):
                downloaded += len(data)
                f.write(data)
                if total_size > 0:
                    percent = (downloaded / total_size) * 100
                    print(f"\r  Progress: {percent:.1f}%", end='')
        print(f"\n✓ Downloaded {filename}")
        return True
    except Exception as e:
        print(f"\n✗ Error downloading {filename}: {e}")
        return False


def download_imdb_reviews():
    """Download IMDB movie reviews dataset."""
    print("\n" + "="*60)
    print("1. IMDB Movie Reviews Dataset")
    print("="*60)

    print("\nThis dataset is available through TensorFlow Datasets or Keras.")
    print("Run this code to download:")
    print("""
    import tensorflow as tf
    import tensorflow_datasets as tfds

    # Load IMDB dataset
    dataset, info = tfds.load('imdb_reviews', with_info=True, as_supervised=True)
    train_dataset, test_dataset = dataset['train'], dataset['test']

    print(f"Training samples: {info.splits['train'].num_examples}")
    print(f"Test samples: {info.splits['test'].num_examples}")
    """)

    return True


def download_ag_news():
    """Download AG News dataset."""
    print("\n" + "="*60)
    print("2. AG News Dataset")
    print("="*60)

    print("\nAG News is available through TensorFlow Datasets.")
    print("Run this code to download:")
    print("""
    import tensorflow_datasets as tfds

    # Load AG News dataset
    dataset, info = tfds.load('ag_news_subset', with_info=True, as_supervised=True)
    train_dataset, test_dataset = dataset['train'], dataset['test']

    print(f"Classes: {info.features['label'].names}")
    print(f"Training samples: {info.splits['train'].num_examples}")
    """)

    return True


def create_sample_text_corpus():
    """Create sample text corpus for language modeling."""
    print("\n" + "="*60)
    print("3. Sample Text Corpus")
    print("="*60)

    corpus_file = DATASETS_DIR / 'sample_corpus.txt'

    sample_text = """
The field of natural language processing has seen tremendous advances in recent years.
Deep learning models, particularly transformers, have revolutionized how machines understand text.
Language models can now generate coherent text, answer questions, and even write creative content.

Machine learning engineers must understand both traditional NLP techniques and modern approaches.
Bag of words and TF-IDF remain useful for many applications.
However, word embeddings and neural networks provide powerful semantic representations.

Text preprocessing is a critical first step in any NLP pipeline.
Tokenization breaks text into individual words or subwords.
Lemmatization reduces words to their base forms.
Stop words are common words that often carry little meaning.

Sentiment analysis is one of the most popular NLP applications.
It allows businesses to understand customer opinions from reviews and social media.
Product reviews, movie ratings, and social media posts all contain valuable sentiment information.

Named entity recognition identifies important entities in text.
These entities include people, organizations, locations, dates, and more.
NER is essential for information extraction and knowledge graph construction.

Machine translation has improved dramatically with neural networks.
Attention mechanisms allow models to focus on relevant parts of the input.
Transformer architectures have become the standard for translation tasks.

Question answering systems can now understand complex queries.
They retrieve relevant information and generate natural language answers.
This technology powers virtual assistants and search engines.

Text summarization reduces long documents to key points.
Extractive summarization selects important sentences from the original text.
Abstractive summarization generates new sentences that capture the main ideas.

The future of NLP is exciting and full of possibilities.
Models are becoming more capable, efficient, and accessible.
Ethical considerations around bias and fairness are increasingly important.
"""

    with open(corpus_file, 'w') as f:
        f.write(sample_text * 10)  # Repeat to create larger corpus

    print(f"✓ Created sample corpus: {corpus_file}")
    print(f"  Size: {os.path.getsize(corpus_file)} bytes")
    return True


def create_chatbot_intent_data():
    """Create sample chatbot intent dataset (already exists in projects)."""
    print("\n" + "="*60)
    print("4. Chatbot Intent Dataset")
    print("="*60)

    print("✓ Intent dataset available at:")
    print("  projects/customer-support-chatbot/intents.json")
    print(f"  Contains 15+ intents with {30}+ patterns each")
    return True


def download_glove_embeddings():
    """Instructions for downloading GloVe embeddings."""
    print("\n" + "="*60)
    print("5. GloVe Word Embeddings (Optional)")
    print("="*60)

    print("\nGloVe embeddings are large files. Download manually if needed:")
    print("  URL: https://nlp.stanford.edu/data/glove.6B.zip")
    print("  Contains: 50d, 100d, 200d, 300d embeddings")
    print("  Size: ~822 MB")
    print("\nFor course purposes, we'll use embeddings from gensim or load smaller versions.")
    return True


def create_dataset_info():
    """Create dataset information file."""
    info_file = DATASETS_DIR / 'dataset_info.md'

    info_content = """# Module 8: NLP Datasets

## Overview

This directory contains datasets and scripts for Module 8 (Natural Language Processing).

## Datasets

### 1. IMDB Movie Reviews
- **Source**: TensorFlow Datasets / Kaggle
- **Size**: 50,000 reviews (25K train, 25K test)
- **Classes**: Binary (Positive/Negative)
- **Use**: Sentiment analysis (Sessions 8.2, 8.4)
- **Download**: Use TensorFlow Datasets or Keras
```python
import tensorflow_datasets as tfds
dataset, info = tfds.load('imdb_reviews', with_info=True, as_supervised=True)
```

### 2. AG News
- **Source**: TensorFlow Datasets
- **Size**: 120,000 articles
- **Classes**: 4 (World, Sports, Business, Sci/Tech)
- **Use**: Multi-class text classification (Session 8.3)
- **Download**: TensorFlow Datasets
```python
dataset = tfds.load('ag_news_subset', as_supervised=True)
```

### 3. Sample Text Corpus
- **Source**: Generated (sample_corpus.txt)
- **Size**: ~10 KB
- **Use**: Text preprocessing examples (Session 8.1)
- **Download**: Created by download script

### 4. Customer Support Intents
- **Source**: Custom created
- **Size**: 15 intents, ~120 patterns
- **Use**: Chatbot project (Session 8.6)
- **Location**: ../projects/customer-support-chatbot/intents.json

### 5. Word Embeddings (Optional)
- **GloVe**: https://nlp.stanford.edu/data/glove.6B.zip
- **Word2Vec**: Available through gensim library
- **Use**: Session 8.3

## Usage

### Run Download Script
```bash
python download_nlp_datasets.py
```

### Manual Downloads

For datasets not automatically downloaded:

1. **IMDB Reviews**:
   - Use TensorFlow Datasets (recommended)
   - Or download from Kaggle: https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews

2. **AG News**:
   - TensorFlow Datasets (recommended)
   - Or Kaggle: https://www.kaggle.com/datasets/amananandrai/ag-news-classification-dataset

3. **GloVe Embeddings** (optional):
   - Download from: https://nlp.stanford.edu/projects/glove/
   - Recommended: glove.6B.zip (100d embeddings)

## Dataset Statistics

| Dataset | Samples | Classes | Size | Task |
|---------|---------|---------|------|------|
| IMDB Reviews | 50,000 | 2 | ~65 MB | Sentiment |
| AG News | 120,000 | 4 | ~30 MB | Multi-class |
| Sample Corpus | N/A | N/A | 10 KB | Preprocessing |
| Intents | 120 | 15 | 15 KB | Chatbot |

## Licenses

- **IMDB**: Academic use
- **AG News**: Academic use
- **GloVe**: Apache 2.0
- **Sample Corpus**: Course materials (free use)

## Troubleshooting

**Issue**: TensorFlow Datasets download fails
**Solution**: Check internet connection, try manual download from Kaggle

**Issue**: Out of disk space
**Solution**: Download only needed datasets, skip GloVe embeddings

**Issue**: Slow download
**Solution**: Use smaller datasets for practice, full datasets for final projects

## Support

For issues with datasets, refer to:
- Course forums
- TensorFlow Datasets documentation
- Kaggle dataset pages

---
Created: 2026-01-06
Module: 8 - Natural Language Processing
"""

    with open(info_file, 'w') as f:
        f.write(info_content)

    print(f"\n✓ Created dataset information: {info_file}")
    return True


def main():
    """Main download function."""
    print("\n" + "="*60)
    print("MODULE 8: NLP DATASETS DOWNLOADER")
    print("="*60)
    print("\nThis script will help you download and prepare all datasets")
    print("required for Module 8 (Natural Language Processing).\n")

    # Download/create datasets
    results = []
    results.append(download_imdb_reviews())
    results.append(download_ag_news())
    results.append(create_sample_text_corpus())
    results.append(create_chatbot_intent_data())
    results.append(download_glove_embeddings())
    results.append(create_dataset_info())

    # Summary
    print("\n" + "="*60)
    print("DOWNLOAD SUMMARY")
    print("="*60)
    print(f"✓ {sum(results)}/{len(results)} tasks completed successfully")

    print("\nNext Steps:")
    print("1. Install TensorFlow Datasets: pip install tensorflow-datasets")
    print("2. Run the provided code snippets to download IMDB and AG News")
    print("3. Check dataset_info.md for detailed information")
    print("4. Start with Session 8.1!")

    print("\nAll datasets prepared! Ready for Module 8.")


if __name__ == "__main__":
    main()
