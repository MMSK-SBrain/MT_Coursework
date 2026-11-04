# Transformer Architecture (Simplified)

## High-Level Architecture

```
┌───────────────────────────────────────────────────────────┐
│                     INPUT TEXT                            │
│            "The cat sat on the mat"                       │
└─────────────────────┬─────────────────────────────────────┘
                      │
                      ▼
┌───────────────────────────────────────────────────────────┐
│                  TOKENIZATION                             │
│      ["The", "cat", "sat", "on", "the", "mat"]           │
└─────────────────────┬─────────────────────────────────────┘
                      │
                      ▼
┌───────────────────────────────────────────────────────────┐
│              EMBEDDING + POSITIONAL ENCODING              │
│    [vec1+pos1, vec2+pos2, vec3+pos3, ...]               │
└─────────────────────┬─────────────────────────────────────┘
                      │
                      ▼
┌───────────────────────────────────────────────────────────┐
│                SELF-ATTENTION LAYERS                      │
│  ┌──────────────────────────────────────────────┐        │
│  │  Query   Key   Value                         │        │
│  │    │      │      │                            │        │
│  │    └──────┴──────┘                            │        │
│  │          │                                    │        │
│  │     Attention Weights                         │        │
│  │          │                                    │        │
│  │     Context Vector                            │        │
│  └──────────────────────────────────────────────┘        │
│  (Repeated N times with Multi-Head Attention)             │
└─────────────────────┬─────────────────────────────────────┘
                      │
                      ▼
┌───────────────────────────────────────────────────────────┐
│               FEED-FORWARD NETWORKS                       │
│         Dense → ReLU → Dense                              │
└─────────────────────┬─────────────────────────────────────┘
                      │
                      ▼
┌───────────────────────────────────────────────────────────┐
│                OUTPUT LAYER                               │
│     (Classification, Generation, etc.)                    │
└───────────────────────────────────────────────────────────┘
```

## Self-Attention Mechanism

```
Input: "The cat sat"

Step 1: Create Query, Key, Value vectors for each word

        The     cat     sat
Query:  [q1]    [q2]    [q3]
Key:    [k1]    [k2]    [k3]
Value:  [v1]    [v2]    [v3]

Step 2: Calculate attention scores

For word "cat":
  Score with "The" = q2 · k1
  Score with "cat" = q2 · k2
  Score with "sat" = q2 · k3

Step 3: Softmax to get attention weights

  Attention("cat") = 0.2*v1 + 0.5*v2 + 0.3*v3

Result: Context-aware representation of "cat"
```

## Multi-Head Attention

```
Input embedding
       │
       ├──→ Head 1 (learns syntax patterns)
       ├──→ Head 2 (learns semantic relationships)
       ├──→ Head 3 (learns positional patterns)
       ├──→ ... (typically 8-12 heads)
       └──→ Head N
       │
    Concatenate
       │
    Linear layer
       │
    Output
```

## Why Transformers Are Powerful

1. **Parallel Processing**
   - Unlike LSTMs, can process all tokens simultaneously
   - Much faster training

2. **Long-Range Dependencies**
   - Attention can connect any two words
   - No vanishing gradient issues

3. **Contextual Understanding**
   - Each word's representation depends on entire sentence
   - "bank" in "river bank" vs "bank account"

## Key Innovations:
- Self-Attention
- Positional Encoding
- Multi-Head Attention
- Layer Normalization
- Residual Connections

## Famous Transformers:
- BERT (Encoder-only)
- GPT (Decoder-only)
- T5 (Encoder-Decoder)
