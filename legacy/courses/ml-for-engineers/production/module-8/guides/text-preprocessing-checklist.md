# Text Preprocessing Checklist

## Pre-Processing Decision Guide

Use this checklist to determine which preprocessing steps to apply for your specific NLP task.

## Step 1: Understand Your Task

- [ ] **Task Type**:
  - [ ] Sentiment Analysis
  - [ ] Text Classification
  - [ ] Named Entity Recognition
  - [ ] Topic Modeling
  - [ ] Question Answering
  - [ ] Text Generation
  - [ ] Machine Translation

## Step 2: Core Preprocessing Steps

### Lowercasing

- [ ] **Apply if**: 
  - Case doesn't matter (sentiment, topic classification)
  - Want to reduce vocabulary size
- [ ] **Skip if**:
  - Proper nouns are important (NER, Q&A)
  - Acronyms carry meaning
  - Analyzing code or technical text

**Code:**
```python
text = text.lower()
```

---

### Remove Punctuation

- [ ] **Apply if**:
  - Punctuation adds no semantic value
  - Using Bag of Words
- [ ] **Skip if**:
  - Emoticons matter (sentiment: ":-)" vs ":-(")
  - Question marks indicate questions
  - Domain-specific (chemical formulas, code)

**Code:**
```python
import re
text = re.sub(r'[^\w\s]', '', text)
```

---

### Remove Numbers

- [ ] **Apply if**:
  - Numbers don't carry meaning
  - General text classification
- [ ] **Skip if**:
  - Numbers are features (product reviews mentioning "$50")
  - Financial/technical text
  - Dates and quantities matter

**Code:**
```python
text = re.sub(r'\d+', '', text)
```

---

### Remove URLs and Emails

- [ ] **Apply if**:
  - URLs/emails don't add value
  - Social media text cleaning
- [ ] **Skip if**:
  - Analyzing spam detection (URLs might indicate spam)
  - Web scraping tasks

**Code:**
```python
# Remove URLs
text = re.sub(r'https?://\S+|www\.\S+', '', text)

# Remove emails
text = re.sub(r'\S+@\S+', '', text)
```

---

### Remove Mentions and Hashtags

- [ ] **Apply if**:
  - Social media mentions irrelevant (@username)
  - Hashtags redundant
- [ ] **Skip if**:
  - Hashtags carry topical information (#COVID19)
  - Analyzing social networks

**Code:**
```python
# Remove @mentions
text = re.sub(r'@\w+', '', text)

# Remove #hashtags
text = re.sub(r'#\w+', '', text)

# Or keep hashtag content
text = re.sub(r'#(\w+)', r'\1', text)  # #python → python
```

---

### Remove Stop Words

- [ ] **Apply if**:
  - Using TF-IDF or BoW
  - Topic modeling
  - Keyword extraction
- [ ] **Skip if**:
  - Word order matters (sentiment: "not good")
  - Using deep learning (models can learn importance)
  - Question answering ("is", "the" provide structure)

**Code:**
```python
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))
words = text.split()
filtered = [w for w in words if w.lower() not in stop_words]
text = ' '.join(filtered)
```

---

### Stemming

- [ ] **Apply if**:
  - Need speed over accuracy
  - Information retrieval
  - BoW/TF-IDF models
- [ ] **Skip if**:
  - Accuracy is critical
  - Meaningful word forms needed
  - Using pre-trained embeddings

**Code:**
```python
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()
words = text.split()
stemmed = [stemmer.stem(w) for w in words]
text = ' '.join(stemmed)
```

---

### Lemmatization

- [ ] **Apply if**:
  - Accuracy matters
  - Valid word forms needed
  - Smaller datasets
- [ ] **Skip if**:
  - Speed is critical
  - Using character/subword models
  - Very large datasets (too slow)

**Code:**
```python
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
words = text.split()
lemmatized = [lemmatizer.lemmatize(w, pos='v') for w in words]
text = ' '.join(lemmatized)
```

---

### Remove Extra Whitespace

- [ ] **Always apply** (standard cleanup)

**Code:**
```python
text = re.sub(r'\s+', ' ', text).strip()
```

---

## Step 3: Task-Specific Checklists

### Sentiment Analysis
- [x] Lowercase
- [ ] Remove punctuation (keep emoticons!)
- [ ] Remove numbers (unless rating-related)
- [x] Remove URLs
- [ ] Remove stop words (be careful: "not good")
- [x] Lemmatization (for accuracy)

### Named Entity Recognition (NER)
- [ ] Lowercase (NO - loses proper noun info)
- [ ] Remove punctuation (NO - helps with boundaries)
- [ ] Remove stop words (NO - provides context)
- [ ] Stemming/Lemmatization (MAYBE - depends on model)

### Topic Modeling
- [x] Lowercase
- [x] Remove punctuation
- [x] Remove numbers
- [x] Remove URLs
- [x] Remove stop words
- [x] Lemmatization
- [x] Keep only nouns and verbs

### Text Classification (General)
- [x] Lowercase
- [x] Remove punctuation
- [x] Remove special characters
- [x] Remove URLs/emails
- [ ] Remove numbers (task-dependent)
- [x] Lemmatization or stemming
- [ ] Remove stop words (if using BoW/TF-IDF)

### Chatbot/Q&A
- [x] Lowercase
- [ ] Remove punctuation (keep "?", "!")
- [ ] Remove numbers (NO - "What's 2+2?")
- [ ] Remove stop words (NO - grammar matters)
- [x] Lemmatization (standardize questions)

## Step 4: Validation

After preprocessing, check:

- [ ] Sample texts before/after
- [ ] Vocabulary size (reduced?)
- [ ] Are meaningful words preserved?
- [ ] Are irrelevant features removed?
- [ ] Does it make sense for your task?

**Code to Compare:**
```python
print("BEFORE:", original_text[:200])
print("AFTER:", processed_text[:200])
print(f"Vocab size: {len(set(processed_text.split()))}")
```

## Common Mistakes to Avoid

1. **Over-preprocessing**: Removing too much information
2. **Under-preprocessing**: Leaving noise that hurts model
3. **Wrong order**: e.g., removing stop words before lemmatization
4. **Not validating**: Not checking preprocessing results
5. **One-size-fits-all**: Using same preprocessing for all tasks

## Complete Preprocessing Function Template

```python
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

def preprocess_text(text,
                   lowercase=True,
                   remove_urls=True,
                   remove_mentions=True,
                   remove_hashtags=True,
                   remove_numbers=True,
                   remove_punctuation=True,
                   remove_stopwords=True,
                   lemmatize=True):
    """
    Comprehensive preprocessing function.
    Customize parameters based on your task.
    """
    
    # Lowercase
    if lowercase:
        text = text.lower()
    
    # Remove URLs
    if remove_urls:
        text = re.sub(r'https?://\S+|www\.\S+', '', text)
    
    # Remove mentions
    if remove_mentions:
        text = re.sub(r'@\w+', '', text)
    
    # Remove hashtags
    if remove_hashtags:
        text = re.sub(r'#\w+', '', text)
    
    # Remove numbers
    if remove_numbers:
        text = re.sub(r'\d+', '', text)
    
    # Remove punctuation
    if remove_punctuation:
        text = re.sub(r'[^\w\s]', '', text)
    
    # Tokenize
    tokens = nltk.word_tokenize(text)
    
    # Remove stop words
    if remove_stopwords:
        stop_words = set(stopwords.words('english'))
        tokens = [t for t in tokens if t.lower() not in stop_words]
    
    # Lemmatization
    if lemmatize:
        lemmatizer = WordNetLemmatizer()
        tokens = [lemmatizer.lemmatize(t, pos='v') for t in tokens]
    
    # Join back
    text = ' '.join(tokens)
    
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

# Usage examples:
# Sentiment analysis
processed = preprocess_text(text, remove_stopwords=False)

# Topic modeling
processed = preprocess_text(text, remove_stopwords=True, lemmatize=True)

# NER
processed = preprocess_text(text, lowercase=False, remove_punctuation=False)
```

## Quick Reference

| Task | Lowercase | Remove Punct | Remove Numbers | Remove Stop Words | Lemmatize |
|------|-----------|--------------|----------------|-------------------|-----------|
| Sentiment | Yes | No (emojis!) | Maybe | No | Yes |
| Topic Model | Yes | Yes | Yes | Yes | Yes |
| NER | No | No | No | No | Maybe |
| Classification | Yes | Yes | Maybe | Maybe | Yes |
| Q&A | Yes | Partial | No | No | Yes |
| Generation | No | No | No | No | No |

---

**Best Practice**: Start with minimal preprocessing, evaluate performance, then add steps as needed.

**Updated**: 2026-01-06
**Module**: 8 - Natural Language Processing
