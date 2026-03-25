# Hugging Face Transformers - Setup Guide

## What is Hugging Face?

Hugging Face is a platform and library that provides:
- Thousands of pre-trained models (BERT, GPT, T5, etc.)
- Easy-to-use APIs for NLP tasks
- Model Hub for sharing and discovering models
- Datasets library for accessing datasets

## Installation

### Basic Installation

```bash
pip install transformers
```

### With TensorFlow/PyTorch

```bash
# For TensorFlow
pip install transformers tensorflow

# For PyTorch  
pip install transformers torch

# For both
pip install transformers tensorflow torch
```

### Additional Dependencies

```bash
pip install datasets  # For accessing datasets
pip install sentencepiece  # For certain tokenizers
pip install accelerate  # For faster training
```

## Quick Start Examples

### 1. Sentiment Analysis (Pipeline API - Easiest)

```python
from transformers import pipeline

# Load sentiment analysis pipeline
classifier = pipeline("sentiment-analysis")

# Analyze sentiment
result = classifier("I love this product!")
print(result)
# [{'label': 'POSITIVE', 'score': 0.9998}]
```

### 2. Text Generation (GPT-2)

```python
from transformers import pipeline

# Load text generation pipeline
generator = pipeline("text-generation", model="gpt2")

# Generate text
result = generator(
    "Once upon a time",
    max_length=50,
    num_return_sequences=1
)
print(result[0]['generated_text'])
```

### 3. Question Answering (BERT)

```python
from transformers import pipeline

# Load QA pipeline
qa = pipeline("question-answering")

# Ask a question
context = "The Eiffel Tower is located in Paris, France."
question = "Where is the Eiffel Tower?"

result = qa(question=question, context=context)
print(result)
# {'answer': 'Paris, France', 'score': 0.998, ...}
```

### 4. Text Classification (Fine-tuning)

```python
from transformers import BertTokenizer, BertForSequenceClassification
from transformers import Trainer, TrainingArguments

# Load model and tokenizer
model = BertForSequenceClassification.from_pretrained(
    "bert-base-uncased",
    num_labels=2
)
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

# Tokenize data
texts = ["I love this!", "This is terrible"]
labels = [1, 0]

encodings = tokenizer(
    texts,
    truncation=True,
    padding=True,
    return_tensors="pt"
)

# Training (simplified)
training_args = TrainingArguments(
    output_dir="./results",
    num_train_epochs=3,
    per_device_train_batch_size=8,
)

# Create trainer and train
# trainer = Trainer(model=model, args=training_args, ...)
# trainer.train()
```

## Model Selection Guide

### For Sentiment Analysis:
- **DistilBERT** (distilbert-base-uncased-finetuned-sst-2-english)
  - Fast, lightweight
  - Good for production
- **RoBERTa** (roberta-base)
  - Higher accuracy
  - Slower

### For Text Generation:
- **GPT-2** (gpt2, gpt2-medium, gpt2-large)
  - English text generation
  - Various sizes for speed/quality tradeoff
- **GPT-Neo** (EleutherAI/gpt-neo-125M)
  - Open-source alternative

### For Question Answering:
- **BERT** (bert-base-uncased)
  - Standard choice
- **RoBERTa** (deepset/roberta-base-squad2)
  - Fine-tuned on SQuAD dataset

### For Summarization:
- **T5** (t5-small, t5-base)
  - Text-to-text format
- **BART** (facebook/bart-large-cnn)
  - Excellent for summarization

## Common Issues and Solutions

### Issue 1: Out of Memory

**Problem**: Model too large for GPU/RAM

**Solutions**:
```python
# Use smaller model
model = BertModel.from_pretrained("distilbert-base-uncased")

# Use CPU
model = BertModel.from_pretrained("bert-base-uncased", device_map="cpu")

# Reduce batch size
training_args = TrainingArguments(per_device_train_batch_size=4)
```

### Issue 2: Slow Download

**Problem**: Model download takes too long

**Solutions**:
```python
# Download once, cache locally
from transformers import AutoModel
model = AutoModel.from_pretrained(
    "bert-base-uncased",
    cache_dir="./models"  # Save to local directory
)

# Use smaller model variants
model = AutoModel.from_pretrained("distilbert-base-uncased")
```

### Issue 3: Token Limit Exceeded

**Problem**: Input text too long

**Solutions**:
```python
# Truncate text
encodings = tokenizer(
    text,
    truncation=True,
    max_length=512  # BERT's max
)

# Split long texts into chunks
def split_text(text, max_length=512):
    tokens = tokenizer.tokenize(text)
    chunks = [tokens[i:i+max_length] for i in range(0, len(tokens), max_length)]
    return chunks
```

### Issue 4: Tokenizer Warnings

**Problem**: "Token indices sequence length is longer than..."

**Solution**:
```python
# Always use padding and truncation
encodings = tokenizer(
    texts,
    padding=True,
    truncation=True,
    max_length=512,
    return_tensors="pt"
)
```

## Best Practices

### 1. Always Cache Models

```python
# Set cache directory to avoid re-downloading
import os
os.environ["TRANSFORMERS_CACHE"] = "./model_cache"
```

### 2. Use Auto Classes for Flexibility

```python
from transformers import AutoTokenizer, AutoModel

# Automatically loads correct classes
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
model = AutoModel.from_pretrained("bert-base-uncased")
```

### 3. Handle Errors Gracefully

```python
try:
    result = pipeline("sentiment-analysis")(text)
except Exception as e:
    print(f"Error: {e}")
    result = {"label": "UNKNOWN", "score": 0.0}
```

### 4. Monitor Resource Usage

```python
import torch

# Check GPU availability
if torch.cuda.is_available():
    device = "cuda"
    print(f"Using GPU: {torch.cuda.get_device_name(0)}")
else:
    device = "cpu"
    print("Using CPU")

model = model.to(device)
```

## Useful Resources

- **Hugging Face Hub**: https://huggingface.co/models
- **Documentation**: https://huggingface.co/docs
- **Course**: https://huggingface.co/course
- **Forums**: https://discuss.huggingface.co

## Quick Reference

### Pipeline Tasks

```python
# Available pipeline tasks:
"sentiment-analysis"
"text-generation"
"question-answering"
"summarization"
"translation"
"zero-shot-classification"
"fill-mask"
"ner"  # Named Entity Recognition
```

### Common Model Sizes

- **Small**: distilbert, t5-small (~66M params)
- **Base**: bert-base, gpt2 (~110M-125M params)
- **Large**: bert-large, gpt2-large (~340M-700M params)

Choose based on:
- **Speed needed**: Small models
- **Accuracy needed**: Large models
- **Resource constraints**: Small/Base models

## Next Steps

1. Explore the Model Hub: https://huggingface.co/models
2. Try different models for your task
3. Fine-tune on your specific dataset
4. Deploy with appropriate model size

---

**Updated**: 2026-01-06
**Module**: 8 - Natural Language Processing
