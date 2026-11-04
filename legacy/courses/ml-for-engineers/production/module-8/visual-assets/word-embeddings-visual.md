# Word Embeddings Visualization

## 2D Embedding Space Concept

```
                    Positive Sentiment
                           ↑
                           │
          excellent    fantastic
              ●             ●
                           │
           great ●         │      ● amazing
                           │
    ────────────────────────┼────────────────────────→
                           │              Formal/Professional
    Casual/Informal        │
                           │
              ●            │
           bad          terrible ●
                           │
                      awful ●
                           │
                           ↓
                    Negative Sentiment

```

## Word Vector Arithmetic

```
king - man + woman ≈ queen

    king [0.2, 0.8, 0.3, ...]  (300-dimensional vector)
  - man  [0.1, 0.6, 0.2, ...]
  + woman[0.0, 0.3, 0.4, ...]
  ────────────────────────────
  = queen[0.1, 0.5, 0.5, ...]  (approximately)
```

## Embedding Dimensions

```
Dense vs Sparse:

BoW (Sparse):             Word Embedding (Dense):
[0, 0, 1, 0, 0, 0,        [0.2, -0.5, 0.8,
 0, 0, 0, 1, 0, 0,         0.1, -0.3, 0.6,
 0, 0, 0, 0, 0, 0,         ...]
 ...] (10,000 dims)       (100-300 dims)

Sparse: mostly zeros      Dense: all values used
```

## Similarity in Embedding Space

```
Cosine Similarity Example:

  car ────┐
           ├──── 0.85 (very similar)
  truck ──┘

  car ────┐
           ├──── 0.12 (not similar)
  apple ──┘
```

## Training Process (Word2Vec Skip-gram)

```
Context Window Example:

Sentence: "The cat sat on the mat"

Input word: "sat"
Context: ["cat", "on"]

    sat
     │
     ├──→ Predict: cat (✓)
     └──→ Predict: on  (✓)

The model learns embeddings where
words in similar contexts are close together.
```

## Visualization Tools:
- t-SNE: Reduces dimensions to 2D/3D
- PCA: Linear dimensionality reduction
- TensorBoard: Interactive embedding explorer

## Key Concepts:
- Similar words = Similar vectors
- Semantic relationships preserved
- Analogies work through vector arithmetic
- Dense representations (vs sparse BoW)
