# Module 7: Computer Vision - Dataset Information

Complete information about all datasets used in Module 7 sessions and capstone project.

---

## Session 7.1: MNIST Handwritten Digits

### Overview
- **Name**: MNIST (Modified National Institute of Standards and Technology)
- **Size**: 70,000 images (60,000 training, 10,000 test)
- **Image Dimensions**: 28×28 pixels, grayscale
- **Classes**: 10 (digits 0-9)
- **File Size**: ~11MB

### Access
```python
from tensorflow.keras.datasets import mnist
(X_train, y_train), (X_test, y_test) = mnist.load_data()
```

### Source
- Built into TensorFlow/Keras
- Original: http://yann.lecun.com/exdb/mnist/

### License
Public domain

### Notes
- Classic benchmark dataset
- Well-balanced classes
- Perfect for learning CNN basics

---

## Session 7.2: CIFAR-10

### Overview
- **Name**: CIFAR-10 (Canadian Institute For Advanced Research)
- **Size**: 60,000 images (50,000 training, 10,000 test)
- **Image Dimensions**: 32×32 pixels, RGB (3 channels)
- **Classes**: 10 (airplane, automobile, bird, cat, deer, dog, frog, horse, ship, truck)
- **File Size**: ~163MB

### Access
```python
from tensorflow.keras.datasets import cifar10
(X_train, y_train), (X_test, y_test) = cifar10.load_data()
```

### Source
- Built into TensorFlow/Keras
- Original: https://www.cs.toronto.edu/~kriz/cifar.html

### License
MIT License

### Notes
- More challenging than MNIST
- Color images, natural objects
- Good for learning data augmentation

---

## Session 7.3: Cats vs Dogs

### Overview
- **Name**: Dogs vs. Cats
- **Size**: 25,000 images (12,500 cats, 12,500 dogs)
- **Recommended Subset**: 4,000 images for training (faster)
- **Image Dimensions**: Variable (resize to 224×224)
- **Classes**: 2 (cat, dog)
- **File Size**: ~800MB (full), ~150MB (subset)

### Access Options

#### Option 1: TensorFlow Datasets
```python
import tensorflow_datasets as tfds
ds = tfds.load('cats_vs_dogs', split='train')
```

#### Option 2: Kaggle CLI
```bash
kaggle datasets download -d salader/dogs-vs-cats
```

#### Option 3: Microsoft Download
Direct download: https://download.microsoft.com/download/3/E/1/3E1C3F21-ECDB-4869-8368-6DEBA77B919F/kagglecatsanddogs_5340.zip

### Source
- Original Kaggle competition
- https://www.kaggle.com/c/dogs-vs-cats

### License
Free to use for educational purposes

### Directory Structure
```
cats_vs_dogs/
  train/
    cats/
      cat.0.jpg
      cat.1.jpg
      ...
    dogs/
      dog.0.jpg
      dog.1.jpg
      ...
  validation/
    cats/
    dogs/
```

### Notes
- Perfect for transfer learning
- Variable image sizes
- Some noisy/ambiguous images

---

## Session 7.5: Chest X-Ray (Pneumonia Detection)

### Overview
- **Name**: Chest X-Ray Images (Pneumonia)
- **Size**: 5,863 images
  - Training: 5,216 (1,341 normal, 3,875 pneumonia)
- **Image Dimensions**: Variable (resize to 224×224)
- **Classes**: 2 (Normal, Pneumonia)
- **File Size**: ~1.2GB

### Access
```bash
# Kaggle CLI
kaggle datasets download -d paultimothymooney/chest-xray-pneumonia
```

### Source
- Kaggle: https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia
- Original: https://data.mendeley.com/datasets/rscbjbr9sj/2

### License
CC BY 4.0

### Directory Structure
```
chest_xray/
  train/
    NORMAL/
    PNEUMONIA/
  test/
    NORMAL/
    PNEUMONIA/
  val/
    NORMAL/
    PNEUMONIA/
```

### Important Notes
- **Class Imbalance**: More pneumonia than normal cases
- **Medical Data**: Handle with care, understand limitations
- **Grayscale Images**: X-rays are single channel
- **Evaluation**: Recall (sensitivity) is critical metric

### Citation
```
Kermany, Daniel; Zhang, Kang; Goldbaum, Michael (2018),
"Labeled Optical Coherence Tomography (OCT) and Chest X-Ray Images for Classification",
Mendeley Data, V2, doi: 10.17632/rscbjbr9sj.2
```

---

## Session 7.6: Manufacturing Defect Detection

### Overview
- **Name**: Casting Product Image Data
- **Size**: 7,348 images
  - Training: 6,633 (3,758 defective, 2,875 OK)
  - Test: 715
- **Image Dimensions**: 300×300 pixels, grayscale
- **Classes**: 2 (OK, Defective)
- **File Size**: ~350MB

### Access
```bash
kaggle datasets download -d ravirajsinh45/real-life-industrial-dataset-of-casting-product
```

### Source
- Kaggle: https://www.kaggle.com/datasets/ravirajsinh45/real-life-industrial-dataset-of-casting-product

### License
Database Contents License (DbCL) v1.0

### Directory Structure
```
casting_data/
  train/
    ok_front/
    def_front/
  test/
    ok_front/
    def_front/
```

### Notes
- Real industrial dataset
- Limited data scenario (good for transfer learning)
- Class imbalance
- Fast inference required for production

---

## Capstone: Cricket Shot Recognition

### Overview
- **Name**: Cricket Shot Dataset (Custom)
- **Recommended Size**: 1,200-1,800 images
  - ~200-300 images per class
- **Image Dimensions**: Variable (resize to 224×224)
- **Classes**: 6
  1. Cover Drive
  2. Straight Drive
  3. Pull Shot
  4. Hook Shot
  5. Sweep Shot
  6. Defensive Shot
- **File Size**: ~500MB-1GB (estimated)

### Data Collection

#### Sources
1. **Video Screenshots**
   - Cricket match highlights on YouTube
   - Extract frames showing clear shots
   - Tools: VLC, FFmpeg

2. **Image Galleries**
   - ICC official website
   - ESPN Cricinfo
   - Getty Images (with license)
   - Unsplash/Pexels (limited availability)

3. **Web Scraping** (with permission)
   - Google Images (check usage rights)
   - Cricket news websites
   - Respect copyright and terms of service

#### Collection Guidelines
- **Quality**: Clear, well-lit, focused on batsman
- **Consistency**: Similar shot stage (mid-execution)
- **Variety**: Different players, stadiums, angles
- **Balance**: Equal images per shot type
- **Resolution**: At least 224×224 (higher is better)

### Directory Structure
```
cricket_shots/
  train/
    cover_drive/
      img_0001.jpg
      img_0002.jpg
      ...
    straight_drive/
    pull/
    hook/
    sweep/
    defensive/
  test/
    (same structure, 20% of data)
```

### Labeling Tips
- Focus on bat angle and body position
- Consider shot intent, not outcome
- Hook vs Pull: Hook is to bouncer (chest-high)
- Cover vs Straight: Angle of bat face
- Use consistent criteria across dataset

### License Considerations
- **Educational Use**: Most images OK for learning
- **Commercial Use**: Requires proper licensing
- **Attribution**: Credit sources appropriately
- **Privacy**: Avoid close-ups of spectators

### Data Augmentation Strategy
Given limited data:
- Rotation: ±30° (varied cricket angles)
- Horizontal flip: Yes (left/right handed)
- Vertical flip: No
- Zoom: 20%
- Brightness: ±20%
- Shift: 20%

---

## General Dataset Management

### Directory Organization
```
module-7-datasets/
├── mnist/                 # Auto-downloaded
├── cifar10/              # Auto-downloaded
├── cats_vs_dogs/
│   ├── train/
│   └── test/
├── chest_xray/
│   ├── train/
│   ├── test/
│   └── val/
├── casting_defects/
│   ├── train/
│   └── test/
└── cricket_shots/        # Custom collection
    ├── train/
    └── test/
```

### Storage Requirements
| Dataset | Size | Storage Type |
|---------|------|--------------|
| MNIST | 11MB | SSD OK |
| CIFAR-10 | 163MB | SSD OK |
| Cats vs Dogs | 800MB | SSD recommended |
| Chest X-Ray | 1.2GB | SSD recommended |
| Casting Defects | 350MB | SSD OK |
| Cricket Shots | 500MB-1GB | SSD OK |
| **Total** | **~3.5GB** | **SSD recommended** |

### Download Script
Use the provided download script:
```bash
python download_vision_datasets.py
```

### Verification
After downloading, verify datasets:
```bash
python verify_datasets.py
```

---

## Ethical Considerations

### Medical Imaging (Chest X-Ray)
- ⚠ Not for clinical use
- ⚠ Educational purposes only
- ⚠ Understand limitations and biases
- ⚠ Patient privacy already anonymized

### Manufacturing (Defects)
- Real industrial data
- Understand business context
- False positive vs false negative costs

### Sports (Cricket)
- Respect image copyrights
- Attribute sources properly
- Consider diversity in dataset

---

## Troubleshooting

### Download Failures
- Check internet connection
- Verify Kaggle API setup
- Try manual download as fallback
- Use VPN if geo-restricted

### Extraction Errors
- Ensure sufficient disk space
- Check file integrity (re-download if corrupted)
- Use appropriate extraction tool

### Dataset Not Found
- Check directory structure matches expectations
- Verify file naming conventions
- Run verification script

---

## Additional Resources

- **Computer Vision Datasets**: https://www.visualdata.io/
- **Kaggle Datasets**: https://www.kaggle.com/datasets
- **TensorFlow Datasets**: https://www.tensorflow.org/datasets
- **Papers with Code**: https://paperswithcode.com/datasets

---

**Last Updated**: 2026-01-06
**Module**: 7 - Computer Vision
**Course**: ML for Engineers
