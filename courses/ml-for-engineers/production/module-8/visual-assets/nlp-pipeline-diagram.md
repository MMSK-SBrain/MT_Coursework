# NLP Pipeline Diagram

## Text Preprocessing Pipeline

```
┌─────────────────────────────────────────────────────────────────────┐
│                         RAW TEXT INPUT                              │
│  "Hi there! Check my order #12345 @ https://shop.com/orders"       │
└────────────────────┬────────────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────────────┐
│                    1. LOWERCASING                                   │
│  "hi there! check my order #12345 @ https://shop.com/orders"       │
└────────────────────┬────────────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────────────┐
│                 2. REMOVE URLs & MENTIONS                           │
│              "hi there check my order"                              │
└────────────────────┬────────────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────────────┐
│              3. REMOVE SPECIAL CHARACTERS                           │
│               "hi there check my order"                             │
└────────────────────┬────────────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────────────┐
│                    4. TOKENIZATION                                  │
│           ["hi", "there", "check", "my", "order"]                   │
└────────────────────┬────────────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────────────┐
│                5. STOP WORD REMOVAL                                 │
│                  ["check", "order"]                                 │
└────────────────────┬────────────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────────────┐
│              6. LEMMATIZATION/STEMMING                              │
│                ["check", "order"]                                   │
└────────────────────┬────────────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────────────┐
│                   CLEANED TEXT OUTPUT                               │
│                    "check order"                                    │
└─────────────────────────────────────────────────────────────────────┘
```

## Full NLP Application Pipeline

```
┌─────────────────┐
│   USER INPUT    │
│ "I love this!"  │
└────────┬────────┘
         │
         ▼
┌─────────────────────────┐
│   TEXT PREPROCESSING    │
│   • Lowercase           │
│   • Clean               │
│   • Tokenize            │
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│   FEATURE EXTRACTION    │
│   • BoW / TF-IDF        │
│   • Word Embeddings     │
│   • BERT Tokenization   │
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│     ML MODEL            │
│   • Naive Bayes         │
│   • Logistic Regression │
│   • LSTM                │
│   • Transformers        │
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│    PREDICTION           │
│  Sentiment: Positive    │
│  Confidence: 95%        │
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│   OUTPUT/RESPONSE       │
│  "Positive sentiment    │
│   detected!"            │
└─────────────────────────┘
```

## Use This Diagram For:
- Understanding the NLP workflow
- Explaining preprocessing steps
- Teaching pipeline architecture
- Debugging processing issues

## Tools Illustrated:
- NLTK for tokenization and lemmatization
- Regex for cleaning
- scikit-learn for vectorization
- TensorFlow/Keras for deep learning models
