# CNN Architecture Visual Diagram

## Classic CNN Architecture for Image Classification

```
INPUT IMAGE                                                    OUTPUT
(224×224×3)                                                   (6 classes)
    │
    ▼
┌─────────────────────────────────────────────────────────────────┐
│                     CONVOLUTIONAL LAYERS                         │
│                   (Feature Extraction)                           │
└─────────────────────────────────────────────────────────────────┘

    │   ┌──────────────────────────────────────┐
    ├──▶│ Conv2D(32, 3×3)  │  ReLU            │
    │   │ Output: 222×222×32                   │
    │   └──────────────────────────────────────┘
    │
    │   ┌──────────────────────────────────────┐
    ├──▶│ MaxPooling2D(2×2)                    │
    │   │ Output: 111×111×32                   │
    │   └──────────────────────────────────────┘
    │
    │   ┌──────────────────────────────────────┐
    ├──▶│ Conv2D(64, 3×3)  │  ReLU            │
    │   │ Output: 109×109×64                   │
    │   └──────────────────────────────────────┘
    │
    │   ┌──────────────────────────────────────┐
    ├──▶│ MaxPooling2D(2×2)                    │
    │   │ Output: 54×54×64                     │
    │   └──────────────────────────────────────┘
    │
    │   ┌──────────────────────────────────────┐
    ├──▶│ Conv2D(128, 3×3)  │  ReLU           │
    │   │ Output: 52×52×128                    │
    │   └──────────────────────────────────────┘
    │
    │   ┌──────────────────────────────────────┐
    ├──▶│ MaxPooling2D(2×2)                    │
    │   │ Output: 26×26×128                    │
    │   └──────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────────────────────────────────┐
│                    CLASSIFICATION LAYERS                         │
│                   (Decision Making)                              │
└─────────────────────────────────────────────────────────────────┘

    │   ┌──────────────────────────────────────┐
    ├──▶│ Flatten                              │
    │   │ Output: 86,528 features              │
    │   └──────────────────────────────────────┘
    │
    │   ┌──────────────────────────────────────┐
    ├──▶│ Dense(256)  │  ReLU  │  Dropout(0.5) │
    │   │ Output: 256 features                 │
    │   └──────────────────────────────────────┘
    │
    │   ┌──────────────────────────────────────┐
    └──▶│ Dense(6)  │  Softmax                 │
        │ Output: 6 class probabilities        │
        └──────────────────────────────────────┘
            │
            ▼
    [cover_drive, straight_drive, pull, hook, sweep, defensive]
      [0.45, 0.25, 0.15, 0.08, 0.05, 0.02]
```

---

## Detailed Layer-by-Layer Explanation

### Input Layer
- **Shape**: (224, 224, 3)
- **Description**: RGB image (height × width × channels)
- **Cricket Example**: Image of batsman playing shot

### Convolutional Block 1
**Conv2D(32, 3×3) + ReLU**
- **Filters**: 32
- **Kernel Size**: 3×3
- **Activation**: ReLU
- **Purpose**: Detects low-level features (edges, colors)
- **Output**: 222×222×32

**MaxPooling2D(2×2)**
- **Pool Size**: 2×2
- **Purpose**: Reduces spatial dimensions, retains important features
- **Output**: 111×111×32

### Convolutional Block 2
**Conv2D(64, 3×3) + ReLU**
- **Filters**: 64 (increased depth)
- **Purpose**: Detects mid-level features (textures, patterns)
- **Output**: 109×109×64

**MaxPooling2D(2×2)**
- **Output**: 54×54×64

### Convolutional Block 3
**Conv2D(128, 3×3) + ReLU**
- **Filters**: 128 (further increased depth)
- **Purpose**: Detects high-level features (bat angle, body position)
- **Output**: 52×52×128

**MaxPooling2D(2×2)**
- **Output**: 26×26×128

### Classification Layers

**Flatten**
- **Purpose**: Converts 3D feature maps to 1D vector
- **Output**: 86,528 features (26×26×128)

**Dense(256) + ReLU + Dropout(0.5)**
- **Units**: 256
- **Purpose**: Learns complex combinations of features
- **Dropout**: 50% prevents overfitting

**Dense(6) + Softmax**
- **Units**: 6 (number of cricket shots)
- **Activation**: Softmax (outputs probabilities)
- **Output**: Probability distribution over 6 classes

---

## CNN Design Principles

### 1. Hierarchical Feature Learning
```
Low-Level        →    Mid-Level       →    High-Level
(Early Layers)        (Middle Layers)      (Late Layers)

Edges, Colors    →    Textures,       →    Complex Objects
                      Patterns              (Bat, Body Position)
```

### 2. Spatial Dimension Reduction
```
Input: 224×224   →   111×111   →   54×54   →   26×26   →   Flatten

(Pooling reduces size while maintaining important features)
```

### 3. Filter Depth Progression
```
32 filters   →   64 filters   →   128 filters

(More filters = more complex features learned)
```

---

## Convolution Operation Visualization

### 3×3 Filter on Image

```
Input (5×5):                Filter (3×3):           Output:

┌─────────────┐            ┌─────────┐
│ 1  2  3  4  5│            │ 1  0 -1│
│ 2  3  4  5  6│            │ 2  0 -2│         ╔═══════╗
│ 3  4  5  6  7│      *     │ 1  0 -1│    =    ║ 0  -8 ║
│ 4  5  6  7  8│            └─────────┘         ╚═══════╝
│ 5  6  7  8  9│        (Edge Detector)
└─────────────┘

This filter detects vertical edges!
```

### Stride and Padding

**Stride = 1 (default)**
```
Filter moves 1 pixel at a time
→ → → →
```

**Stride = 2**
```
Filter moves 2 pixels at a time (faster, smaller output)
→   →   →
```

**Padding = 'same'**
```
Adds zeros around input to maintain size
┌─────────────┐
│ 0  0  0  0  0│
│ 0  X  X  X  0│
│ 0  X  X  X  0│
│ 0  0  0  0  0│
└─────────────┘
```

---

## MaxPooling Operation

### 2×2 Max Pooling (most common)

```
Input (4×4):                       Output (2×2):

┌─────────────────┐
│  1    5  │  3    2│            ┌─────────┐
│  4    3  │  7    8│            │  5  │  8│
├──────────┼────────┤      →     ├─────┼───┤
│  2    6  │  4    1│            │  6  │  9│
│  1    2  │  9    5│            └─────────┘
└─────────────────┘

Takes maximum value from each 2×2 region
Reduces size by half, retains strongest features
```

---

## Parameter Calculation

### Conv2D(32, 3×3) on RGB input

```
Parameters = (filter_height × filter_width × input_channels + 1) × num_filters
           = (3 × 3 × 3 + 1) × 32
           = (27 + 1) × 32
           = 28 × 32
           = 896 parameters

(+1 for bias term)
```

### Why CNNs have fewer parameters than Dense networks

**Dense Network for 224×224×3 image:**
```
Input neurons: 224 × 224 × 3 = 150,528
Hidden layer (256 neurons): 150,528 × 256 = 38,535,168 parameters! 😱
```

**CNN:**
```
Conv2D(32, 3×3): Only 896 parameters
Shares weights across entire image → much more efficient! 🎉
```

---

## Transfer Learning Visualization

### Pre-trained Model (e.g., ResNet50)

```
┌─────────────────────────────────────────┐
│          PRE-TRAINED LAYERS             │
│      (Learned from ImageNet)            │
│                                          │
│  ┌──────────────────────────────────┐  │
│  │ Early Layers                     │  │  ← Detect edges, colors
│  │ (Frozen during training)         │  │    (General features)
│  └──────────────────────────────────┘  │
│                                          │
│  ┌──────────────────────────────────┐  │
│  │ Middle Layers                    │  │  ← Detect textures, patterns
│  │ (Frozen during training)         │  │    (More complex features)
│  └──────────────────────────────────┘  │
│                                          │
│  ┌──────────────────────────────────┐  │
│  │ Late Layers                      │  │  ← Can be fine-tuned
│  │ (Unfrozen for fine-tuning)       │  │    (Task-specific)
│  └──────────────────────────────────┘  │
└─────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────┐
│       CUSTOM CLASSIFIER                  │
│      (Your task-specific layers)         │
│                                          │
│  GlobalAveragePooling2D                  │
│  Dense(256) + Dropout                    │
│  Dense(6) + Softmax                      │
│     ↓                                    │
│  [Cricket Shot Predictions]              │
└─────────────────────────────────────────┘
```

---

## Receptive Field Growth

### How CNNs "see" larger areas with depth

```
Layer 1:        Layer 2:           Layer 3:
Conv 3×3        Conv 3×3           Conv 3×3

┌───┐           ┌─────┐            ┌───────┐
│ 3×3│    →     │ 5×5 │      →     │ 7×7   │
└───┘           └─────┘            └───────┘

Each layer sees a larger region of original input
Deep networks capture global context!
```

---

**Key Takeaway**: CNNs are powerful for images because they:
1. Learn hierarchical features (edges → textures → objects)
2. Use parameter sharing (efficient)
3. Maintain spatial relationships
4. Achieve translation invariance through pooling

This makes them perfect for cricket shot recognition!
