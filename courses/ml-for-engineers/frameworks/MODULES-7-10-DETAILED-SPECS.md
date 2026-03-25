# Modules 7, 8, 9, 10: Detailed Production Specifications
## Complete Production-Ready Requirements for Final Modules

**Created:** 2026-01-06
**Purpose:** Detailed specifications for creating production materials
**Detail Level:** Full production specifications (ready for agent execution)
**Status:** Ready for production material creation

---

# TABLE OF CONTENTS

1. [Module 7: Computer Vision](#module-7-computer-vision)
2. [Module 8: Natural Language Processing](#module-8-natural-language-processing)
3. [Module 9: Deployment & MLOps](#module-9-deployment--mlops)
4. [Module 10: Capstone Project](#module-10-capstone-project)
5. [Cross-Module Requirements](#cross-module-requirements)

---

# MODULE 7: COMPUTER VISION

## Module Overview

**Duration:** 2 weeks (14-16 hours video + 25-30 hours hands-on)
**Purpose:** Build systems that can SEE - image classification, object detection
**Prerequisites:** Module 6 (Neural Networks foundation)
**Theory/Practice Ratio:** 30% / 70%

**The Hook:**
"Remember the face detection demo from Module 0? Now BUILD it!"

**Emotional Arc:**
- Start: "Images are just pixels... how does a computer 'see'?"
- Middle: "My CNN just classified 10,000 images at 92% accuracy!"
- End: "I built a cricket shot recognizer and deployed it!"

**Connection to Previous Modules:**
- Builds on Module 6 (neural networks, transfer learning)
- Uses CNNs (not just dense networks)
- Applies to real-world visual problems
- Deploys model (preview Module 9)

---

## Complete Session Breakdown

### Session 1: Introduction to Computer Vision (2 hours)

**Learning Objectives:**
1. Understand images as data (pixels, channels, dimensions)
2. Perform image preprocessing
3. Apply data augmentation
4. Build first image classifier
5. Understand CV applications

**Video Content (60 minutes):**

#### Video 1.1: Images as Data (15 minutes)
- Pixels and color channels (RGB)
- Image dimensions (height × width × channels)
- Grayscale vs color images
- Image arrays in numpy
- Visualizing images with matplotlib
- Normalization (0-255 → 0-1)

#### Video 1.2: Image Preprocessing (15 minutes)
- Resizing images (different input sizes)
- Normalization and standardization
- Image augmentation preview
- Batch processing
- Why preprocessing matters for NNs

#### Video 1.3: Data Augmentation (20 minutes)
- Rotation, flip, zoom
- Brightness, contrast adjustments
- Why augmentation prevents overfitting
- ImageDataGenerator in Keras
- Real-time augmentation during training
- Examples showing augmented images

#### Video 1.4: Computer Vision Applications (10 minutes)
- Image classification (what's in the image?)
- Object detection (where is it?)
- Semantic segmentation
- Face recognition
- Medical imaging
- Autonomous vehicles
- Quality control in manufacturing

**Hands-On Activity (60 minutes):**

**Project: Cats vs Dogs Binary Classifier**

Dataset Requirements:
- Cats vs Dogs dataset
- ~25,000 images (12,500 cats, 12,500 dogs)
- Source: Kaggle or TensorFlow Datasets
- Alternative: Subset of 2,000 images for faster training

Code Requirements:
```python
# Required implementations:
1. Data Loading
   - Load images from directory
   - Resize to 150×150 or 224×224
   - Normalize pixel values
   - Split train/validation

2. Data Augmentation
   - ImageDataGenerator with:
     - Rotation (20 degrees)
     - Width/height shift (0.2)
     - Horizontal flip
     - Zoom (0.2)
   - Visualize augmented samples

3. Build Simple CNN
   - Conv2D(32, 3×3) + ReLU + MaxPooling2D
   - Conv2D(64, 3×3) + ReLU + MaxPooling2D
   - Conv2D(128, 3×3) + ReLU + MaxPooling2D
   - Flatten
   - Dense(128) + ReLU + Dropout(0.5)
   - Dense(1) + Sigmoid

4. Compile and Train
   - Loss: binary_crossentropy
   - Optimizer: adam
   - Metrics: accuracy
   - Epochs: 15-20
   - Batch size: 32

5. Evaluate
   - Validation accuracy (target: >80%)
   - Training/validation curves
   - Sample predictions with images
   - Confusion matrix

6. Visualization requirements:
   - Original vs augmented images (side by side)
   - Training history (accuracy + loss)
   - Sample predictions (correct and incorrect)
   - Confusion matrix
```

**Deliverables:**
- `cats-vs-dogs-classifier.ipynb`
- Trained model saved (`cats_dogs_model.h5`)
- Sample predictions with images

**Success Criteria:**
- Validation accuracy > 80%
- Data augmentation working
- Understand image → pixels → CNN workflow

---

### Session 2: Convolutional Neural Networks (2 hours)

**Learning Objectives:**
1. Understand convolution operation
2. Learn pooling layers
3. Grasp CNN architecture design
4. Build CNN from scratch
5. Apply to CIFAR-10 dataset

**Video Content (60 minutes):**

#### Video 2.1: The Convolution Operation (18 minutes)
- What is convolution?
- Filters/kernels (3×3, 5×5)
- Stride and padding
- Feature maps
- Edge detection example
- Why convolution for images?
- Local connectivity vs fully connected

#### Video 2.2: Pooling Layers (12 minutes)
- Max pooling vs average pooling
- Reducing spatial dimensions
- Translation invariance
- Typical: 2×2 max pooling
- Why pooling helps

#### Video 2.3: CNN Architecture Design (20 minutes)
- Typical pattern:
  - Conv → ReLU → Pool → Repeat
  - Flatten → Dense layers
- Increasing filter depth (32 → 64 → 128)
- Decreasing spatial size
- Famous architectures preview (LeNet, AlexNet, VGG)
- Design principles

#### Video 2.4: Batch Normalization in CNNs (10 minutes)
- Adding batch norm after Conv layers
- Speeds up training
- Regularization effect
- Where to add (after Conv, before activation)

**Hands-On Activity (60 minutes):**

**Project: CIFAR-10 CNN from Scratch**

Dataset Requirements:
- CIFAR-10 dataset
- 60,000 images (50,000 train, 10,000 test)
- 32×32 color images
- 10 classes (airplane, car, bird, cat, deer, dog, frog, horse, ship, truck)
- Built into Keras

Code Requirements:
```python
# Required implementations:
1. Load and Prepare CIFAR-10
   - Load from keras.datasets
   - Normalize (0-1)
   - One-hot encode labels
   - No resizing needed (already 32×32)

2. Build CNN Architecture
   - Block 1: Conv2D(32, 3×3) + ReLU + Conv2D(32, 3×3) + ReLU + MaxPooling2D
   - Block 2: Conv2D(64, 3×3) + ReLU + Conv2D(64, 3×3) + ReLU + MaxPooling2D
   - Block 3: Conv2D(128, 3×3) + ReLU + Conv2D(128, 3×3) + ReLU + MaxPooling2D
   - Flatten
   - Dense(128) + ReLU + Dropout(0.5)
   - Dense(10) + Softmax

3. Data Augmentation
   - ImageDataGenerator:
     - Rotation: 15 degrees
     - Width/height shift: 0.1
     - Horizontal flip
   - fit on training data

4. Compile and Train
   - Loss: categorical_crossentropy
   - Optimizer: Adam
   - Metrics: accuracy
   - Epochs: 30-50
   - Early stopping (patience=10)

5. Evaluate
   - Test accuracy (target: >70%)
   - Confusion matrix (10×10)
   - Per-class accuracy
   - Hardest classes to classify

6. Architecture Analysis
   - Print model summary
   - Count parameters
   - Visualize architecture
   - Explain design choices

7. Visualization requirements:
   - CIFAR-10 samples (grid of 100)
   - Training history
   - Confusion matrix heatmap
   - Per-class accuracy bar chart
   - Sample predictions (correct + incorrect)
```

**Deliverables:**
- `cifar10-cnn-scratch.ipynb`
- Trained model (`cifar10_cnn.h5`)
- Architecture diagram/summary

**Success Criteria:**
- Test accuracy > 70%
- Understand convolution and pooling
- Can design CNN architecture independently

---

### Session 3: Advanced Image Classification (2 hours)

**Learning Objectives:**
1. Apply advanced data augmentation
2. Handle imbalanced image datasets
3. Build medical image classifier
4. Understand high-stakes CV applications
5. Achieve high accuracy (>85%)

**Video Content (60 minutes):**

#### Video 3.1: Advanced Data Augmentation (15 minutes)
- Mixup and CutMix (advanced techniques)
- Random erasing
- Color jittering
- AutoAugment (brief)
- When to use which technique
- Avoiding overfitting with augmentation

#### Video 3.2: Handling Class Imbalance in Images (12 minutes)
- Class weights
- Oversampling minority class
- Focal loss (brief)
- Stratified sampling
- Medical imaging often imbalanced

#### Video 3.3: Medical Image Classification (18 minutes)
- Unique challenges (high stakes, limited data)
- Transfer learning critical
- Interpretability matters (not just accuracy)
- Regulatory considerations
- Real-world examples:
  - Pneumonia detection
  - Diabetic retinopathy
  - Skin lesion classification

#### Video 3.4: Building Trust in CV Models (15 minutes)
- Accuracy isn't everything
- Precision vs recall in medical context
- False negatives can be deadly
- Grad-CAM visualizations (show what model "sees")
- Clinical validation
- Human-in-the-loop

**Hands-On Activity (60 minutes):**

**Project: Chest X-ray Pneumonia Detection (Healthcare)**

Dataset Requirements:
- Chest X-ray dataset (Normal vs Pneumonia)
- ~5,000 images
- Source: Kaggle "Chest X-Ray Images (Pneumonia)"
- Alternative: Synthetic or smaller subset

Code Requirements:
```python
# Required implementations:
1. Data Loading
   - Load X-ray images
   - Check class distribution (likely imbalanced!)
   - Resize to 224×224 (for transfer learning)
   - Normalize

2. Handle Class Imbalance
   - Calculate class weights
   - Or oversample minority class
   - Apply during training

3. Build CNN with Transfer Learning
   - Use VGG16 or ResNet50 (pretrained on ImageNet)
   - Freeze base layers
   - Add custom classifier:
     - GlobalAveragePooling2D
     - Dense(256) + ReLU + Dropout(0.5)
     - Dense(2) + Softmax (Normal vs Pneumonia)

4. Data Augmentation (Medical Images)
   - Rotation: 10 degrees (less aggressive)
   - Width/height shift: 0.1
   - Zoom: 0.1
   - Horizontal flip (careful! anatomical considerations)
   - No vertical flip (not medically valid)

5. Training
   - Compile with class weights
   - Train 20-30 epochs
   - Early stopping
   - Monitor validation accuracy AND recall

6. Evaluation (Medical Context)
   - Accuracy, Precision, Recall, F1
   - Recall is critical (catch all pneumonia!)
   - Confusion matrix
   - ROC curve and AUC
   - Sample predictions with X-ray images

7. Grad-CAM Visualization (Optional but valuable)
   - Show what regions model focuses on
   - Validate clinical relevance
   - Build trust

8. Visualization requirements:
   - Sample X-rays (Normal vs Pneumonia)
   - Class distribution
   - Training history
   - Confusion matrix
   - ROC curve
   - Grad-CAM heatmaps (if implemented)
```

**Deliverables:**
- `pneumonia-xray-classifier.ipynb`
- Trained model (`pneumonia_model.h5`)
- Clinical evaluation report

**Success Criteria:**
- Recall > 85% (catch most pneumonia cases)
- Precision reasonable (minimize false alarms)
- Understand medical CV unique requirements

---

### Session 4: Object Detection (2 hours)

**Learning Objectives:**
1. Understand detection vs classification
2. Learn bounding boxes and IoU
3. Use pre-trained object detectors
4. Build face detection application
5. Understand YOLO, SSD concepts

**Video Content (60 minutes):**

#### Video 4.1: Detection vs Classification (12 minutes)
- Classification: "What is it?" (label)
- Detection: "What is it and WHERE?" (label + bounding box)
- Multiple objects per image
- Applications:
  - Autonomous driving
  - Surveillance
  - Retail (checkout-free stores)
  - Sports analytics

#### Video 4.2: Bounding Boxes and IoU (15 minutes)
- Bounding box: (x, y, width, height)
- Ground truth vs predicted boxes
- Intersection over Union (IoU)
- IoU threshold (typically 0.5)
- Non-Maximum Suppression (NMS)

#### Video 4.3: Object Detection Architectures (18 minutes)
- Two-stage detectors (R-CNN family)
  - Slow but accurate
- One-stage detectors (YOLO, SSD)
  - Fast, real-time
- YOLO overview:
  - Grid-based detection
  - Bounding box + class prediction
  - Real-time capability
- When to use which

#### Video 4.4: Using Pre-trained Detectors (15 minutes)
- Why build from scratch is hard
- Pre-trained models (COCO dataset)
- Loading and using YOLO, SSD
- Fine-tuning for custom objects
- Practical approach for most projects

**Hands-On Activity (60 minutes):**

**Project: Face Detection Application**

Code Requirements:
```python
# Required implementations:
1. Face Detection with OpenCV (Classical Method)
   - Load Haar Cascade classifier
   - Detect faces in images
   - Draw bounding boxes
   - Count faces
   - Simple and fast

2. Face Detection with Deep Learning (MTCNN or similar)
   - Install face_recognition or MTCNN
   - Detect faces with bounding boxes
   - Detect facial landmarks (eyes, nose, mouth)
   - Higher accuracy

3. Real-time Detection (Webcam)
   - Access webcam with OpenCV
   - Detect faces in video stream
   - Draw bounding boxes in real-time
   - FPS counter

4. Face Detection Application
   - Upload image → detect faces → display
   - Batch processing (multiple images)
   - Save results with bounding boxes

5. Comparison
   - Haar Cascade vs Deep Learning
   - Speed vs accuracy tradeoff
   - When to use which

6. Visualization requirements:
   - Sample images with bounding boxes
   - Multiple faces detected
   - Facial landmarks visualization
   - Speed comparison chart
```

**Deliverables:**
- `face-detection-app.ipynb`
- Working face detector (image input)
- Real-time webcam demo (optional)

**Success Criteria:**
- Detect faces accurately in various conditions
- Understand bounding box concepts
- Can apply pre-trained detectors

---

### Session 5: Transfer Learning for Vision (2 hours)

**Learning Objectives:**
1. Master transfer learning for images
2. Apply to manufacturing (defect detection)
3. Work with limited data
4. Fine-tune effectively
5. Deploy for quality control

**Video Content (60 minutes):**

#### Video 5.1: Transfer Learning Deep Dive (15 minutes)
- Recall Module 6 transfer learning
- Why especially powerful for images
- ImageNet pre-training (1.2M images, 1000 classes)
- Learned features:
  - Early layers: edges, textures
  - Middle layers: patterns, parts
  - Late layers: objects
- Transfer to new domains

#### Video 5.2: Fine-tuning Strategies (18 minutes)
- Feature extraction (freeze all, train classifier)
- Fine-tuning (unfreeze top layers, small LR)
- When to fine-tune:
  - Similar task: freeze more
  - Different task: fine-tune more
  - Very little data: feature extraction only
- Learning rate: typically 1e-4 to 1e-5
- Two-phase training recommended

#### Video 5.3: Working with Limited Data (12 minutes)
- The small data problem
- Transfer learning to the rescue
- Data augmentation critical
- Few-shot learning (brief)
- Synthetic data generation
- When is data "enough"?

#### Video 5.4: Manufacturing Quality Control (15 minutes)
- Defect detection use case
- Types of defects (cracks, scratches, discoloration)
- Binary (defect/no defect) or multi-class
- Real-time requirements
- Integration with production line
- ROI and business case

**Hands-On Activity (60 minutes):**

**Project: Manufacturing Defect Detection (Quality Control)**

Dataset Requirements:
- Manufacturing defect dataset
- Options:
  - Kaggle "Casting Product Image Data" (OK/Defective)
  - Semiconductor defect dataset
  - Custom synthetic dataset
- ~1,000-2,000 images (limited data scenario)

Code Requirements:
```python
# Required implementations:
1. Load Limited Dataset
   - Small dataset (1000-2000 images)
   - Binary classification (OK vs Defective)
   - Imbalanced (fewer defects)

2. Extensive Data Augmentation
   - Rotation, flip, zoom
   - Brightness, contrast
   - Elastic transforms (for manufacturing)
   - Generate 10x more data through augmentation

3. Transfer Learning with MobileNet
   - Use MobileNet (lightweight, fast)
   - Pretrained on ImageNet
   - Freeze all layers
   - Add classifier:
     - GlobalAveragePooling2D
     - Dense(128) + ReLU + Dropout(0.5)
     - Dense(1) + Sigmoid

4. Phase 1: Feature Extraction
   - Train classifier only
   - 10-15 epochs
   - Evaluate

5. Phase 2: Fine-tuning
   - Unfreeze top 10 layers of MobileNet
   - Very small learning rate (1e-5)
   - Train 10 more epochs
   - Evaluate improvement

6. Deployment Considerations
   - Inference speed (manufacturing line)
   - Accuracy requirements
   - False positive vs false negative cost
   - Integration points

7. Visualization requirements:
   - Sample products (OK vs Defective)
   - Data augmentation examples
   - Training history (phase 1 + phase 2)
   - Confusion matrix
   - Sample predictions
   - Speed benchmark (inference time)
```

**Deliverables:**
- `defect-detection-transfer-learning.ipynb`
- Fine-tuned model (`defect_detector.h5`)
- Deployment recommendations

**Success Criteria:**
- Accuracy > 85% despite limited data
- Fast inference (<100ms per image)
- Understand transfer learning power

---

### Session 6: Computer Vision Capstone (2 hours + 2-3 hours project time)

**Learning Objectives:**
1. Apply all CV techniques learned
2. Build end-to-end CV application
3. Deploy model (preview Module 9)
4. Create cricket shot classifier
5. Complete CV portfolio piece

**Video Content (60 minutes):**

#### Video 6.1: Capstone Project Overview (10 minutes)
- Cricket shot recognition project
- Why this project:
  - Callback to Module 0 (cricket predictor)
  - Real-world sports analytics
  - Challenging (similar poses)
  - Portfolio-worthy
- Success criteria

#### Video 6.2: Sports Analytics with CV (15 minutes)
- Applications:
  - Player tracking
  - Action recognition
  - Performance analysis
  - Automated highlights
  - Referee assistance
- Cricket specifics:
  - Shot classification (cover drive, pull, sweep, etc.)
  - Bowling action analysis
  - Field placement optimization

#### Video 6.3: Deployment Preview (Module 9 Sneak Peek) (20 minutes)
- Saving the model
- Creating prediction function
- Building simple web UI (Streamlit)
- Hosting options (Streamlit Cloud, Heroku)
- Making it public
- Portfolio piece

#### Video 6.4: Capstone Walkthrough (15 minutes)
- Step-by-step approach
- Dataset considerations
- Architecture choice
- Training strategy
- Deployment process
- Common pitfalls

**Hands-On Activity (120-180 minutes):**

**Capstone Project: Cricket Shot Recognition**

Dataset Requirements:
- Cricket shot images
- Options:
  - Custom collected from internet (with proper licenses)
  - Synthetic dataset
  - 6 shot types: Cover Drive, Straight Drive, Pull, Hook, Sweep, Defensive
- ~1,200-1,800 images (200-300 per class)

Code Requirements:
```python
# Complete end-to-end project:
1. Data Collection & Preparation
   - Gather cricket shot images (or use provided)
   - Organize by shot type
   - Check class balance
   - Resize to 224×224
   - Split train/validation/test

2. Exploratory Data Analysis
   - Sample images from each class
   - Class distribution
   - Image quality check

3. Data Augmentation
   - Rotation (30 degrees - varied cricket angles)
   - Zoom, shift, flip
   - Brightness adjustments
   - Generate training data

4. Model Architecture
   - Transfer learning with ResNet50 or EfficientNet
   - Freeze base
   - Custom classifier:
     - GlobalAveragePooling2D
     - Dense(512) + BatchNorm + ReLU + Dropout(0.5)
     - Dense(256) + BatchNorm + ReLU + Dropout(0.3)
     - Dense(6) + Softmax (6 shot types)

5. Training Strategy
   - Phase 1: Train classifier (frozen base)
     - 15-20 epochs
     - Adam optimizer
   - Phase 2: Fine-tune (unfreeze top layers)
     - 10-15 epochs
     - Small learning rate (1e-5)
   - Early stopping + ReduceLROnPlateau

6. Evaluation
   - Test accuracy (target: >75%, challenging task!)
   - Confusion matrix (which shots confused?)
   - Per-class accuracy
   - Error analysis

7. Deployment (Streamlit App)
   - Simple UI: Upload image → Predict shot type
   - Display prediction with confidence
   - Show top 3 predictions
   - Sample images for demo
   - Deploy to Streamlit Cloud (public URL!)

8. Documentation
   - README with project overview
   - How to run locally
   - How to use deployed app
   - Model architecture and performance
   - Future improvements

9. Visualization requirements:
   - Sample shots from each class
   - Class distribution bar chart
   - Training history (both phases)
   - Confusion matrix heatmap
   - Sample predictions (correct + incorrect)
   - Deployment screenshots
```

**Deliverables:**
- `cricket-shot-recognition-complete.ipynb`
- Trained model (`cricket_shot_model.h5`)
- `app.py` (Streamlit deployment)
- README.md (complete documentation)
- Public deployed URL

**Success Criteria:**
- Test accuracy > 75%
- Working Streamlit app
- Publicly accessible deployment
- Complete documentation
- Portfolio-ready project

**Deployment Bonus:**
- Deploy to Streamlit Cloud
- Share public URL
- Add to portfolio/resume

---

## Module 7: Complete Dataset Requirements

### Dataset 1: Cats vs Dogs
- **Source:** Kaggle or TensorFlow Datasets
- **Size:** 25,000 images (or subset of 2,000)
- **Format:** JPG images
- **Classes:** 2 (cat, dog)

### Dataset 2: CIFAR-10
- **Source:** Built into Keras
- **Size:** 60,000 images (32×32)
- **Classes:** 10

### Dataset 3: Chest X-ray (Pneumonia)
- **Source:** Kaggle "Chest X-Ray Images (Pneumonia)"
- **Size:** ~5,000 images
- **Classes:** 2 (Normal, Pneumonia)
- **Alternative:** Smaller subset or synthetic

### Dataset 4: Face Images (for detection)
- **Source:** Sample images (can use any photos)
- **Purpose:** Testing face detection
- **No specific dataset needed**

### Dataset 5: Manufacturing Defects
- **Source:** Kaggle "Casting Product Image Data" or similar
- **Size:** 1,000-2,000 images
- **Classes:** 2 (OK, Defective)

### Dataset 6: Cricket Shots
- **Source:** Custom collection or synthetic
- **Size:** 1,200-1,800 images
- **Classes:** 6 (different shot types)
- **Alternative:** Provide sample dataset

Download Script Required:
```python
# download_cv_datasets.py
# Automated download for all Module 7 datasets
# Kaggle API integration
# TensorFlow Datasets usage
# Instructions for manual downloads
```

---

## Module 7: Complete Assessment Requirements

### Quizzes (6 total, ~54 questions)

**Session 1 Quiz (9 questions):**
- Image representation (pixels, channels)
- Preprocessing techniques
- Data augmentation purposes
- CV applications

**Session 2 Quiz (9 questions):**
- Convolution operation
- Pooling layers
- CNN architecture design
- Filter depth progression

**Session 3 Quiz (9 questions):**
- Advanced augmentation
- Class imbalance handling
- Medical imaging considerations
- High-stakes CV

**Session 4 Quiz (9 questions):**
- Detection vs classification
- Bounding boxes and IoU
- Object detection architectures
- Pre-trained detectors

**Session 5 Quiz (9 questions):**
- Transfer learning strategies
- Fine-tuning approaches
- Limited data scenarios
- Manufacturing CV applications

**Session 6 Quiz (9 questions):**
- End-to-end CV projects
- Deployment considerations
- Sports analytics
- Portfolio development

### Project Rubrics

**Session Projects (5 × 15 points = 75 points):**
- Correct implementation (50%)
- Target accuracy achieved (25%)
- Visualizations (15%)
- Documentation (10%)

**Cricket Shot Recognition Capstone (100 points):**
- Data preparation (10 points)
- Model architecture (15 points)
- Training strategy (15 points)
- Evaluation and analysis (20 points)
- Deployment (Streamlit app) (25 points)
- Documentation (10 points)
- Code quality (5 points)

---

## Module 7: Visual Assets Needed

1. **Pixels and Channels Diagram**
2. **Convolution Operation Animation**
3. **Pooling Visualization**
4. **CNN Architecture Diagram**
5. **Data Augmentation Examples**
6. **Bounding Box and IoU Illustration**
7. **Transfer Learning Concept**
8. **Module 7 Workflow Diagram**

---

## Module 7: Success Metrics

**By end of module, learners should:**
- ✅ Build CNNs for image classification
- ✅ Achieve CIFAR-10 >70%, Medical imaging >85%
- ✅ Apply object detection (face detection)
- ✅ Master transfer learning for limited data
- ✅ Deploy CV model as web app
- ✅ Build portfolio-worthy cricket shot recognizer

---

# MODULE 8: NATURAL LANGUAGE PROCESSING

## Module Overview

**Duration:** 2 weeks (14-16 hours video + 25-30 hours hands-on)
**Purpose:** Build systems that understand LANGUAGE
**Prerequisites:** Module 6 (Neural Networks, LSTM basics)
**Theory/Practice Ratio:** 30% / 70%

**The Hook:**
"Remember the sentiment analyzer and chatbot from Module 0? Now BUILD them!"

**Emotional Arc:**
- Start: "Text is just strings... how does a computer 'understand'?"
- Middle: "My sentiment analyzer just classified 10,000 reviews at 89% accuracy!"
- End: "I built a customer support chatbot and it works!"

**Connection to Previous Modules:**
- Builds on Module 6 (RNNs, LSTMs, transformers intro)
- Text = sequences (like time series in Module 3)
- Transfer learning (like Module 7 for images)
- Deploys chatbot (Module 9 preview)

---

## Complete Session Breakdown

### Session 1: Introduction to NLP (2 hours)

**Learning Objectives:**
1. Understand text as data
2. Perform text preprocessing
3. Tokenization, stemming, lemmatization
4. Build text preprocessing pipeline
5. Understand NLP applications

**Video Content (60 minutes):**

#### Video 1.1: Text as Data (12 minutes)
- Text is unstructured
- Converting text to numbers
- Vocabulary and tokens
- Sequences of words
- NLP vs Computer Vision similarities

#### Video 1.2: Tokenization (15 minutes)
- Word tokenization
- Sentence tokenization
- Subword tokenization (BPE, WordPiece)
- NLTK and spaCy libraries
- Handling punctuation, capitalization

#### Video 1.3: Text Cleaning (18 minutes)
- Lowercasing
- Removing punctuation
- Removing stop words ("the", "a", "is")
- Stemming (running → run, roughly)
- Lemmatization (running → run, properly)
- When to use which

#### Video 1.4: NLP Applications (15 minutes)
- Sentiment analysis (reviews, social media)
- Text classification (spam, topic)
- Named Entity Recognition (people, places, organizations)
- Machine translation
- Question answering
- Chatbots and virtual assistants
- Text summarization

**Hands-On Activity (60 minutes):**

**Project: Text Preprocessing Pipeline**

Dataset Requirements:
- Sample text data (tweets, reviews, articles)
- Can use NLTK sample data or small custom dataset

Code Requirements:
```python
# Required implementations:
1. Install Libraries
   - NLTK
   - spaCy
   - Download required data (stopwords, punkt)

2. Tokenization Examples
   - Word tokenization
   - Sentence tokenization
   - Compare NLTK vs spaCy

3. Text Cleaning Pipeline
   - Function to clean text:
     - Lowercase
     - Remove URLs
     - Remove mentions (@user)
     - Remove hashtags
     - Remove punctuation
     - Remove numbers (optional)
   - Test on sample texts

4. Stop Words Removal
   - Load NLTK stop words
   - Remove from text
   - Show before/after comparison

5. Stemming vs Lemmatization
   - Apply PorterStemmer
   - Apply WordNetLemmatizer
   - Compare results
   - Understand tradeoffs

6. Complete Preprocessing Function
   - Combine all steps
   - Input: raw text → Output: clean tokens
   - Test on various examples

7. Visualization requirements:
   - Word cloud (before and after cleaning)
   - Word frequency bar chart
   - Token length distribution
```

**Deliverables:**
- `text-preprocessing-pipeline.ipynb`
- Reusable preprocessing functions
- Before/after comparisons

**Success Criteria:**
- Clean text preprocessing pipeline
- Understand all preprocessing steps
- Can apply to any text data

---

### Session 2: Text Classification Basics (2 hours)

**Learning Objectives:**
1. Understand Bag of Words
2. Learn TF-IDF
3. Build sentiment analyzer
4. Compare to Module 0 demo
5. Achieve >85% accuracy

**Video Content (60 minutes):**

#### Video 2.1: Bag of Words (BoW) (15 minutes)
- Representing text as vectors
- Vocabulary creation
- Word counts
- Limitations (no order, no semantics)
- CountVectorizer in sklearn

#### Video 2.2: TF-IDF (20 minutes)
- Term Frequency (TF)
- Inverse Document Frequency (IDF)
- TF-IDF score
- Why better than raw counts
- Captures importance
- TfidfVectorizer in sklearn

#### Video 2.3: Text Classification with Traditional ML (15 minutes)
- Vectorize text (BoW or TF-IDF)
- Train classifier (Logistic Regression, Naive Bayes, SVM)
- Naive Bayes especially good for text
- Multiclass classification
- Evaluation metrics (precision, recall, F1)

#### Video 2.4: Sentiment Analysis Overview (10 minutes)
- Binary (positive/negative)
- Multi-class (positive/neutral/negative)
- Applications: product reviews, social media, customer feedback
- Business value

**Hands-On Activity (60 minutes):**

**Project: Sentiment Analysis on Movie Reviews**

Dataset Requirements:
- IMDB movie reviews dataset
- 50,000 reviews (25,000 train, 25,000 test)
- Binary sentiment (positive/negative)
- Source: Built into TensorFlow Datasets or Kaggle

Code Requirements:
```python
# Required implementations:
1. Load Movie Reviews Dataset
   - IMDB reviews
   - 50,000 reviews
   - Binary labels

2. Text Preprocessing
   - Apply preprocessing pipeline from Session 1
   - Clean all reviews
   - Tokenize

3. Feature Extraction (Bag of Words)
   - CountVectorizer
   - Max features: 5000
   - Convert text to BoW vectors

4. Train Classifier (Naive Bayes)
   - MultinomialNB
   - Fit on training data
   - Predict on test data
   - Evaluate (accuracy, precision, recall, F1)

5. Feature Extraction (TF-IDF)
   - TfidfVectorizer
   - Max features: 5000
   - Convert text to TF-IDF vectors

6. Train Classifier (Logistic Regression)
   - LogisticRegression
   - Fit on TF-IDF features
   - Predict on test data
   - Evaluate

7. Compare Approaches
   - BoW + Naive Bayes
   - TF-IDF + Logistic Regression
   - Which is better?
   - Why?

8. Test on Custom Reviews
   - Write your own movie reviews
   - Predict sentiment
   - See if it works!

9. Compare to Module 0 Demo
   - Recall Module 0 sentiment analyzer
   - "I just built that!"
   - Understand what was under the hood

10. Visualization requirements:
    - Word clouds (positive vs negative)
    - Top positive/negative words
    - Confusion matrix
    - Model comparison bar chart
    - Sample predictions
```

**Deliverables:**
- `sentiment-analysis-movie-reviews.ipynb`
- Trained models (Naive Bayes, Logistic Regression)
- Model comparison report

**Success Criteria:**
- Test accuracy > 85%
- Understand BoW and TF-IDF
- Compare to Module 0 demo successfully

---

### Session 3: Advanced Text Features (2 hours)

**Learning Objectives:**
1. Understand word embeddings
2. Use Word2Vec, GloVe pre-trained
3. Build multi-class text classifier
4. Apply to news categorization
5. Understand semantic representations

**Video Content (60 minutes):**

#### Video 3.1: Limitations of BoW and TF-IDF (10 minutes)
- No semantic meaning
- "King" and "Queen" are equally different from each other as "King" and "Apple"
- No word order
- Sparse vectors
- Need better representations

#### Video 3.2: Word Embeddings (20 minutes)
- Dense vector representations
- Capturing semantic meaning
- Similar words have similar vectors
- Word2Vec (skip-gram, CBOW)
- GloVe (global vectors)
- Embedding dimensions (50, 100, 300)
- Analogies: king - man + woman ≈ queen

#### Video 3.3: Using Pre-trained Embeddings (20 minutes)
- Training embeddings requires huge data
- Use pre-trained (GloVe, Word2Vec, FastText)
- Loading pre-trained embeddings
- Using in Keras Embedding layer
- Fine-tuning vs freezing

#### Video 3.4: Embeddings in Neural Networks (10 minutes)
- Embedding layer in Keras
- Convert words → indices → embeddings
- Feed to LSTM or Dense layers
- End-to-end learning

**Hands-On Activity (60 minutes):**

**Project: Multi-Class Text Classification (News Categorization)**

Dataset Requirements:
- News articles dataset
- Options:
  - AG News (4 categories: World, Sports, Business, Sci/Tech)
  - 20 Newsgroups (20 categories)
  - BBC News (5 categories)
- ~10,000-120,000 articles depending on dataset

Code Requirements:
```python
# Required implementations:
1. Load News Dataset
   - Choose AG News or 20 Newsgroups
   - Load articles and labels
   - Check class distribution

2. Text Preprocessing
   - Clean articles
   - Tokenize
   - Create vocabulary
   - Convert to sequences

3. Approach 1: TF-IDF + Classifier (Baseline)
   - TfidfVectorizer
   - Logistic Regression (multi-class)
   - Evaluate

4. Approach 2: Embeddings + Neural Network
   - Tokenize and pad sequences
   - Embedding layer (100 dimensions)
   - LSTM or GRU layer (64 units)
   - Dense layers
   - Softmax output (number of categories)
   - Train and evaluate

5. Approach 3: Pre-trained GloVe Embeddings
   - Download GloVe embeddings (100d)
   - Load into Keras Embedding layer
   - Freeze embeddings
   - Train classifier only
   - Compare to learned embeddings

6. Model Comparison
   - TF-IDF baseline
   - Learned embeddings
   - Pre-trained embeddings
   - Which is best?

7. Error Analysis
   - Confusion matrix
   - Which categories confused?
   - Sample misclassifications

8. Application: Customer Support Ticket Routing
   - Same approach applies
   - Route tickets to departments
   - Business value

9. Visualization requirements:
   - Class distribution
   - Training history
   - Confusion matrix (heatmap)
   - Model comparison table
   - Sample predictions
```

**Deliverables:**
- `news-classification-embeddings.ipynb`
- Models (TF-IDF baseline, embedding-based)
- Embedding visualization (optional)

**Success Criteria:**
- Accuracy > 80% (multi-class harder)
- Understand word embeddings
- Compare baseline vs embeddings

---

### Session 4: Sequence Models (2 hours)

**Learning Objectives:**
1. Apply RNNs and LSTMs to text
2. Build sequence models
3. Next word prediction
4. Understand text generation basics
5. Handle variable-length sequences

**Video Content (60 minutes):**

#### Video 4.1: Why Sequences Matter (12 minutes)
- Text is sequential
- Word order matters
- "Dog bites man" ≠ "Man bites dog"
- Recurrent Neural Networks (RNNs)
- Recap from Module 6

#### Video 4.2: LSTMs for Text (18 minutes)
- LSTM architecture recap
- Handling long-term dependencies
- Bidirectional LSTMs
- Stacking LSTMs
- When to use

#### Video 4.3: Text Generation Basics (15 minutes)
- Language modeling
- Predicting next word
- Sampling strategies (greedy, temperature, beam search)
- Applications: autocomplete, chatbots, creative writing

#### Video 4.4: Handling Variable Lengths (15 minutes)
- Padding sequences
- Masking in Keras
- Packing padded sequences
- Truncation strategies

**Hands-On Activity (60 minutes):**

**Project: Next Word Prediction (Text Generation)**

Dataset Requirements:
- Text corpus (Shakespeare, news articles, or custom)
- Large text file (at least 100KB text)

Code Requirements:
```python
# Required implementations:
1. Prepare Text Data
   - Load text corpus
   - Tokenize into words
   - Create vocabulary
   - Convert to sequences

2. Create Training Data for Next Word Prediction
   - Input: sequence of N words
   - Output: next word
   - Example: "The cat sat on the" → "mat"
   - Generate many such pairs

3. Pad Sequences
   - All sequences same length
   - Padding

4. Build LSTM Model
   - Embedding layer (100 dimensions)
   - LSTM layer (128 units)
   - Dense layer (vocab size) + Softmax
   - Categorical crossentropy loss

5. Train Model
   - 20-50 epochs
   - Monitor loss
   - Early stopping

6. Text Generation
   - Start with seed text (e.g., "The cat")
   - Predict next word
   - Append to sequence
   - Repeat to generate paragraph
   - Temperature sampling for diversity

7. Evaluation
   - Perplexity (if time permits)
   - Sample generated text
   - Does it make sense?

8. Applications
   - Autocomplete
   - Text suggestions
   - Creative writing assistance

9. Visualization requirements:
   - Training loss curve
   - Sample generated texts (different seeds)
   - Temperature comparison (greedy vs random)
```

**Deliverables:**
- `next-word-prediction.ipynb`
- Trained language model
- Generated text samples

**Success Criteria:**
- Model trains successfully
- Generated text somewhat coherent
- Understand sequence modeling

---

### Session 5: Transformers & Pre-trained Models (2 hours)

**Learning Objectives:**
1. Understand transformers concept
2. Use BERT, GPT models
3. Apply Hugging Face library
4. Build text summarizer
5. Leverage pre-trained models

**Video Content (60 minutes):**

#### Video 5.1: Attention Mechanism (15 minutes)
- Limitations of LSTMs
- Attention concept
- "Which words to focus on?"
- Self-attention
- Multi-head attention

#### Video 5.2: Transformers Overview (20 minutes)
- Transformer architecture (high-level)
- Encoder-decoder structure
- Positional encoding
- Why transformers dominate NLP now
- Parallel processing (vs sequential RNNs)
- BERT, GPT, T5, etc.

#### Video 5.3: Pre-trained Models (15 minutes)
- Training transformers is expensive
- Use pre-trained models
- BERT (Bidirectional Encoder)
  - Masked language modeling
  - Fine-tune for classification, NER, etc.
- GPT (Generative Pre-trained Transformer)
  - Next word prediction
  - Text generation
- Hugging Face library

#### Video 5.4: Fine-tuning Transformers (10 minutes)
- Loading pre-trained model
- Adding task-specific head
- Fine-tuning on small dataset
- Fast and effective
- Example: BERT for sentiment analysis

**Hands-On Activity (60 minutes):**

**Project: Text Summarization with Transformers**

Dataset Requirements:
- News articles or documents (with summaries)
- Options:
  - CNN/DailyMail dataset
  - XSum dataset
  - Custom articles
- Use pre-trained T5 or BART

Code Requirements:
```python
# Required implementations:
1. Install Hugging Face Transformers
   - pip install transformers
   - Import pipeline

2. Use Pre-trained Summarization Model (Zero-shot)
   - Load T5 or BART summarization pipeline
   - Summarize sample articles
   - No training needed!
   - See how well it works

3. Load Sample Articles
   - 5-10 articles (or from dataset)
   - Long text that needs summarizing

4. Generate Summaries
   - Apply summarization model
   - Set max_length (e.g., 50-100 words)
   - Generate summaries for all articles

5. Evaluate Summaries
   - Read original and summary
   - Is it capturing main points?
   - ROUGE score (if ground truth available)

6. Experiment with Parameters
   - max_length
   - min_length
   - num_beams (beam search)
   - See how they affect output

7. Fine-tuning (Optional, if time)
   - Load BERT for classification
   - Fine-tune on sentiment dataset
   - Compare to Session 2 baseline

8. Applications
   - News summarization
   - Document summarization
   - Email summarization
   - Meeting notes

9. Visualization requirements:
   - Side-by-side (original vs summary)
   - Summary length comparison
   - ROUGE scores (if available)
```

**Deliverables:**
- `text-summarization-transformers.ipynb`
- Generated summaries
- Comparison to original texts

**Success Criteria:**
- Successfully use pre-trained model
- Generate coherent summaries
- Understand transformers power

---

### Session 6: NLP Capstone (2 hours + 2-3 hours project time)

**Learning Objectives:**
1. Build end-to-end chatbot
2. Intent classification
3. Response generation
4. Deploy chatbot
5. Complete NLP portfolio piece

**Video Content (60 minutes):**

#### Video 6.1: Chatbot Architecture (15 minutes)
- Types of chatbots:
  - Rule-based
  - Retrieval-based
  - Generative
- Intent classification
- Entity extraction
- Response selection
- Conversation management

#### Video 6.2: Intent Classification (15 minutes)
- User query → intent label
- Examples:
  - "What's my account balance?" → check_balance
  - "I want to cancel my order" → cancel_order
- Text classification problem
- Multi-class classification

#### Video 6.3: Response Generation (15 minutes)
- Template-based responses
- Retrieval from FAQ database
- Generative responses (transformers)
- Hybrid approach
- Handling unknown intents

#### Video 6.4: Deployment and Integration (15 minutes)
- Chatbot interfaces (web, Slack, WhatsApp)
- Streamlit chatbot UI
- API integration
- Logging and analytics
- Continuous improvement

**Hands-On Activity (120-180 minutes):**

**Capstone Project: Customer Support Chatbot**

Dataset Requirements:
- FAQ dataset or intent classification dataset
- Options:
  - Custom FAQ (create 30-50 QA pairs)
  - Intent classification dataset (Kaggle)
  - Banking/e-commerce customer queries

Code Requirements:
```python
# Complete end-to-end chatbot:
1. Define Intents and Responses
   - 10-15 intents (e.g., greeting, check_balance, cancel_order, etc.)
   - Multiple example queries per intent
   - Template responses per intent

2. Create Intent Training Data
   - Label queries with intents
   - 20-50 examples per intent
   - Split train/test

3. Build Intent Classifier
   - Text preprocessing
   - TF-IDF or embeddings
   - Classifier (Logistic Regression or neural network)
   - Train on intent data
   - Evaluate accuracy (target: >90%)

4. Build Response Generator
   - Template-based responses
   - If intent = greeting → "Hello! How can I help you?"
   - Map intents to responses
   - Add randomization for naturalness

5. Chatbot Logic
   - Function: user_query → cleaned_query → intent → response
   - Handle unknown intents gracefully
   - Confidence threshold

6. Streamlit Chatbot UI
   - Text input for user query
   - Display chat history
   - Show bot responses
   - Nice styling

7. Advanced Features (Optional)
   - Entity extraction (e.g., order number, date)
   - Contextual conversations
   - FAQ database integration

8. Deployment
   - Deploy to Streamlit Cloud
   - Public URL
   - Test with real queries

9. Compare to Module 0 Demo
   - Recall Module 0 chatbot demo
   - "I built this!"
   - Understand internals

10. Documentation
    - README with project overview
    - Supported intents list
    - How to extend with new intents
    - Deployment instructions

11. Visualization requirements:
    - Intent distribution
    - Classifier confusion matrix
    - Sample conversations
    - Deployment screenshots
```

**Deliverables:**
- `customer-support-chatbot.ipynb` (intent classifier)
- `chatbot-app.py` (Streamlit UI)
- `intents.json` (intent definitions)
- README.md
- Public deployed chatbot URL

**Success Criteria:**
- Intent classifier >90% accuracy
- Chatbot responds correctly to 10+ intents
- Streamlit UI working
- Publicly deployed
- Portfolio-ready project

---

## Module 8: Complete Dataset Requirements

### Dataset 1: Sample Text (for preprocessing)
- **Source:** NLTK sample data, tweets, or custom
- **Purpose:** Practice preprocessing
- **Size:** Small (100-1000 samples)

### Dataset 2: IMDB Movie Reviews
- **Source:** TensorFlow Datasets or Kaggle
- **Size:** 50,000 reviews
- **Classes:** 2 (positive, negative)

### Dataset 3: AG News or 20 Newsgroups
- **Source:** TensorFlow Datasets or sklearn
- **Size:** 10,000-120,000 articles
- **Classes:** 4-20 categories

### Dataset 4: Text Corpus (for generation)
- **Source:** Shakespeare, news, or custom
- **Size:** 100KB+ text
- **Purpose:** Next word prediction

### Dataset 5: News Articles (for summarization)
- **Source:** Sample articles or CNN/DailyMail
- **Size:** 5-10 articles (pre-trained model used)
- **Purpose:** Summarization testing

### Dataset 6: Intent Classification / FAQ
- **Source:** Custom or Kaggle chatbot datasets
- **Size:** 500-1,000 queries
- **Intents:** 10-15

Download Script:
```python
# download_nlp_datasets.py
# Automated download for NLP datasets
# TensorFlow Datasets integration
# NLTK data download
# Instructions for manual sources
```

---

## Module 8: Complete Assessment Requirements

### Quizzes (6 total, ~54 questions)

**Session 1 Quiz (9 questions):**
- Text representation
- Tokenization
- Preprocessing steps
- NLP applications

**Session 2 Quiz (9 questions):**
- Bag of Words
- TF-IDF
- Sentiment analysis
- Text classification

**Session 3 Quiz (9 questions):**
- Word embeddings
- Word2Vec, GloVe
- Pre-trained embeddings
- Multi-class classification

**Session 4 Quiz (9 questions):**
- Sequence models
- LSTMs for text
- Text generation
- Variable-length handling

**Session 5 Quiz (9 questions):**
- Attention mechanism
- Transformers
- BERT, GPT
- Hugging Face library

**Session 6 Quiz (9 questions):**
- Chatbot architecture
- Intent classification
- Response generation
- Deployment

### Project Rubrics

**Session Projects (5 × 15 points = 75 points):**
- Correct implementation (50%)
- Target accuracy (25%)
- Visualizations (15%)
- Documentation (10%)

**Customer Support Chatbot Capstone (100 points):**
- Intent classifier (25 points)
- Response generation (20 points)
- Chatbot logic (20 points)
- Streamlit UI (20 points)
- Deployment (10 points)
- Documentation (5 points)

---

## Module 8: Visual Assets Needed

1. **Text to Vector Illustration**
2. **BoW vs TF-IDF Comparison**
3. **Word Embeddings Visualization**
4. **LSTM for Text Diagram**
5. **Transformer Architecture (High-Level)**
6. **Chatbot Architecture Flowchart**
7. **Module 8 Workflow Diagram**

---

## Module 8: Success Metrics

**By end of module, learners should:**
- ✅ Preprocess text data effectively
- ✅ Build sentiment analyzer >85% accuracy
- ✅ Use word embeddings
- ✅ Apply LSTMs to text
- ✅ Use transformers (Hugging Face)
- ✅ Build and deploy working chatbot
- ✅ Complete NLP portfolio piece

---

# MODULE 9: DEPLOYMENT & MLOPS

## Module Overview

**Duration:** 2 weeks (12-14 hours video + 20-25 hours hands-on)
**Purpose:** Take models from notebooks to PRODUCTION
**Prerequisites:** Modules 2-8 (have models to deploy)
**Theory/Practice Ratio:** 25% / 75%

**The Hook:**
"Your models work in notebooks... but the world needs APIs and apps!"

**Emotional Arc:**
- Start: "My model is amazing in Jupyter... but now what?"
- Middle: "I just deployed my stock predictor to the cloud - anyone can use it!"
- End: "I have a complete production ML system in my portfolio!"

**Connection to Previous Modules:**
- Deploys models from Modules 2-8
- Stock predictor (Module 3)
- Cricket shot recognizer (Module 7)
- Chatbot (Module 8)
- Real-world productionization

---

## Complete Session Breakdown

### Session 1: ML Pipeline for Production (2 hours)

**Learning Objectives:**
1. Understand production ML workflow
2. Version control for ML
3. Model serialization (pickle, joblib)
4. Save and load models properly
5. Prepare for deployment

**Video Content (60 minutes):**

#### Video 1.1: Production ML Workflow (15 minutes)
- Development vs Production
- Jupyter notebook ≠ production code
- The ML pipeline:
  1. Data collection
  2. Data preprocessing
  3. Feature engineering
  4. Model training
  5. Model evaluation
  6. Model deployment
  7. Monitoring
  8. Retraining
- Continuous cycle

#### Video 1.2: Version Control for ML (18 minutes)
- Git for code (obviously)
- Data versioning (DVC intro)
- Model versioning
- Experiment tracking (MLflow intro)
- Reproduc

ibility
- What to version control, what not to

#### Video 1.3: Model Serialization (15 minutes)
- Saving trained models
- pickle (Python standard)
- joblib (better for large models)
- SavedModel format (TensorFlow/Keras)
- ONNX (cross-framework)
- Best practices

#### Video 1.4: Preparing for Deployment (12 minutes)
- Preprocessing pipeline = part of model
- Save scaler, encoder, etc.
- Complete prediction function
- Input validation
- Error handling
- Testing saved model

**Hands-On Activity (60 minutes):**

**Project: Save and Load Models Properly**

Code Requirements:
```python
# Required implementations:
1. Load Previous Models
   - Stock predictor (Module 3)
   - Sentiment analyzer (Module 8)
   - Image classifier (Module 7)

2. Save with Pickle/Joblib
   - Save sklearn models (joblib)
   - Save preprocessing pipelines
   - Save with correct file naming

3. Save Keras Models
   - model.save() to HDF5
   - Or SavedModel format
   - Include architecture + weights

4. Create Complete Pipeline
   - Preprocessing + Model as single object
   - sklearn Pipeline
   - Test that it works

5. Load and Test
   - Load saved model
   - Make predictions on new data
   - Verify identical to original

6. Version Management
   - Model versioning scheme (v1.0.0)
   - Changelog
   - When to increment version

7. Git Integration
   - .gitignore for large model files
   - Git LFS for model versioning (optional)
   - README with model info

8. Error Handling
   - Check file exists before loading
   - Handle incompatible versions
   - Graceful degradation

9. Documentation
   - Model card (what model does, performance, limitations)
   - Save/load instructions
   - Dependencies and versions
```

**Deliverables:**
- Saved models from previous modules
- Model loading utilities
- Model cards documenting each model

**Success Criteria:**
- Models save and load correctly
- Predictions match original
- Proper version control

---

### Session 2: Building ML APIs (2 hours)

**Learning Objectives:**
1. Understand REST APIs
2. Build Flask API
3. Learn FastAPI
4. Create ML prediction endpoints
5. Test with Postman/curl

**Video Content (60 minutes):**

#### Video 2.1: REST APIs Overview (12 minutes)
- What is an API?
- REST principles
- HTTP methods (GET, POST)
- JSON input/output
- Endpoints
- Why APIs for ML?

#### Video 2.2: Flask Basics (18 minutes)
- Flask framework
- Routes and endpoints
- Request and response
- JSON handling
- POST endpoint for predictions
- Simple Flask app example

#### Video 2.3: FastAPI Introduction (18 minutes)
- Modern alternative to Flask
- Type hints and automatic validation
- Interactive documentation (Swagger)
- Async support
- Faster development
- When to use Flask vs FastAPI

#### Video 2.4: ML API Best Practices (12 minutes)
- Input validation
- Error handling
- Response formats
- API versioning (/v1/predict)
- Authentication (brief)
- Rate limiting
- Logging

**Hands-On Activity (60 minutes):**

**Project: Spam Detector API (Local)**

Code Requirements:
```python
# Required implementations:
1. Build Flask API
   - Install Flask
   - Create app.py
   - Import spam detector model (Module 2)

2. Create Prediction Endpoint
   - POST /predict
   - Accept JSON: {"text": "Your message here"}
   - Return JSON: {"spam": true/false, "confidence": 0.95}

3. Implement Prediction Function
   - Load saved spam model
   - Preprocess input text
   - Make prediction
   - Return result

4. Input Validation
   - Check "text" field exists
   - Check not empty
   - Handle errors gracefully
   - Return appropriate error codes

5. Test Locally
   - Run Flask app (python app.py)
   - Test with Postman or curl
   - Send various requests
   - Verify responses

6. Add Health Check Endpoint
   - GET /health
   - Return {"status": "ok"}
   - For monitoring

7. Error Handling
   - Try-except blocks
   - Return error messages
   - Proper HTTP status codes

8. Documentation
   - README with API usage
   - Example requests
   - Expected responses

9. FastAPI Version (Optional)
   - Build same API with FastAPI
   - Compare development experience
   - Interactive docs at /docs
```

**Deliverables:**
- `app.py` (Flask API)
- Working spam detector API (local)
- API documentation
- Test requests/responses

**Success Criteria:**
- API runs locally
- POST /predict works correctly
- Proper error handling
- Clear documentation

---

### Session 3: Cloud Deployment (2 hours)

**Learning Objectives:**
1. Understand cloud platforms
2. Deploy to Heroku
3. Containerization basics (Docker)
4. Deploy stock predictor to cloud
5. Create public API

**Video Content (60 minutes):**

#### Video 3.1: Cloud Platforms Overview (15 minutes)
- Heroku (easiest, free tier)
- AWS (scalable, complex)
- Google Cloud Platform (integrated with TensorFlow)
- Azure (enterprise)
- Which to choose?
- This session: Heroku

#### Video 3.2: Heroku Deployment (20 minutes)
- Heroku account setup
- Heroku CLI
- Git-based deployment
- Procfile, requirements.txt
- Deployment process
- Logs and debugging

#### Video 3.3: Docker Basics (15 minutes)
- What is Docker?
- Containers vs VMs
- Dockerfile
- Building images
- Why Docker for ML?
- Docker + Heroku (optional)

#### Video 3.4: Production Considerations (10 minutes)
- Environment variables (API keys, secrets)
- Scaling (vertical vs horizontal)
- Cold starts
- Costs
- Security basics

**Hands-On Activity (60 minutes):**

**Project: Deploy Stock Predictor to Heroku**

Code Requirements:
```python
# Required implementations:
1. Prepare Flask App
   - Load stock predictor model (Module 3)
   - Create prediction endpoint
   - POST /predict
   - Input: {"ticker": "AAPL", "features": [...]}
   - Output: {"predicted_price": 150.25}

2. Create Requirements File
   - requirements.txt with all dependencies
   - Pin versions for reproducibility
   - Flask, scikit-learn, pandas, numpy, etc.

3. Create Procfile
   - Tell Heroku how to run app
   - web: gunicorn app:app

4. Test Locally
   - Run with gunicorn locally
   - Test all endpoints
   - Fix any issues

5. Git Setup
   - Initialize git repo
   - Add .gitignore (venv, __pycache__, etc.)
   - Commit all files

6. Heroku Deployment
   - Create Heroku app
   - Connect git repo
   - Deploy with git push heroku main
   - Monitor logs

7. Test Deployed API
   - Get Heroku app URL
   - Test /predict endpoint
   - Verify it works publicly!

8. API Documentation
   - Create README with:
     - API URL
     - Endpoints
     - Request/response examples
     - Try it out instructions

9. Share and Celebrate
   - Public URL for portfolio
   - Test from different locations
   - Share with friends!
```

**Deliverables:**
- Deployed stock predictor API (Heroku URL)
- API documentation
- Deployment guide

**Success Criteria:**
- API publicly accessible
- Works from anywhere
- Documentation clear
- Portfolio-worthy

---

### Session 4: Model Monitoring (2 hours)

**Learning Objectives:**
1. Understand model degradation
2. Monitor prediction requests
3. Track accuracy over time
4. Set up logging
5. Create alerts

**Video Content (60 minutes):**

#### Video 4.1: Why Models Degrade (15 minutes)
- Data drift (input distribution changes)
- Concept drift (relationship changes)
- Examples:
  - COVID changed customer behavior
  - New products not in training data
  - Seasonal changes
- Need for monitoring

#### Video 4.2: Monitoring Metrics (15 minutes)
- Request volume
- Response time
- Prediction distribution
- Input feature distribution
- Accuracy (if ground truth available)
- Error rates

#### Video 4.3: Logging Best Practices (15 minutes)
- What to log
  - Timestamp
  - Input features
  - Prediction
  - Confidence
  - Model version
- Where to log (files, databases, cloud services)
- Privacy considerations

#### Video 4.4: Alerts and Dashboards (15 minutes)
- When to alert (thresholds)
- Alerting channels (email, Slack)
- Simple dashboards
- Grafana, Kibana (preview)
- This session: simple dashboard

**Hands-On Activity (60 minutes):**

**Project: Monitoring Dashboard for Deployed Model**

Code Requirements:
```python
# Required implementations:
1. Add Logging to API
   - Log every prediction request
   - Save to SQLite database or CSV
   - Fields: timestamp, input, prediction, confidence, model_version

2. Logging Function
   - Function to log prediction
   - Call after each prediction
   - Handle errors

3. Dashboard with Streamlit
   - Load prediction logs
   - Display metrics:
     - Total predictions
     - Predictions per day (line chart)
     - Prediction distribution (histogram)
     - Average confidence
   - Refresh button

4. Monitoring Metrics
   - Request volume over time
   - Prediction distribution (has it changed?)
   - Confidence scores over time
   - Response time (if logged)

5. Simulate Model Drift
   - Generate synthetic requests
   - Change input distribution
   - See how dashboard shows drift

6. Simple Alerts
   - Check if predictions per day drops below threshold
   - Check if confidence drops below threshold
   - Print alert message or send email (basic)

7. Deploy Dashboard
   - Deploy Streamlit dashboard (separate app)
   - Or add to existing API
   - Monitor deployed model

8. Documentation
   - How to access dashboard
   - What metrics mean
   - How to respond to alerts
```

**Deliverables:**
- Logging integrated into API
- Streamlit monitoring dashboard
- Alert system (basic)

**Success Criteria:**
- Predictions logged correctly
- Dashboard shows useful metrics
- Can detect simulated drift
- Alerts trigger appropriately

---

### Session 5: Updating & A/B Testing (2 hours)

**Learning Objectives:**
1. Model versioning strategies
2. A/B testing for ML
3. Gradual rollout
4. Rollback procedures
5. Deploy multiple model versions

**Video Content (60 minutes):**

#### Video 5.1: Model Versioning Strategies (15 minutes)
- Semantic versioning (v1.0.0, v1.1.0, v2.0.0)
- When to update model
- Backward compatibility
- Managing multiple versions
- Blue-green deployment

#### Video 5.2: A/B Testing for ML (18 minutes)
- What is A/B testing?
- Why A/B test models?
- Traffic splitting (50/50, 90/10)
- Metrics to compare
- Statistical significance
- Duration of test

#### Video 5.3: Gradual Rollout (15 minutes)
- Canary deployment
- Start with 5% traffic
- Gradually increase if successful
- Monitor closely
- Rollback if issues

#### Video 5.4: Rollback Procedures (12 minutes)
- When to rollback
- How to rollback quickly
- Keep old model version running
- Automated vs manual rollback
- Post-mortem analysis

**Hands-On Activity (60 minutes):**

**Project: Deploy Two Model Versions with A/B Testing**

Code Requirements:
```python
# Required implementations:
1. Train Two Models
   - Version 1: Existing model
   - Version 2: Improved model (e.g., more features, better hyperparameters)
   - Save both

2. Update API for Multiple Versions
   - Load both models
   - Add version parameter
   - GET /predict?version=v1 or v2
   - Or random selection (A/B test)

3. A/B Testing Logic
   - Random assignment (50/50)
   - Log which version used
   - Return prediction from assigned version

4. Comparison Metrics
   - Track predictions from v1 and v2
   - Compare:
     - Confidence scores
     - Prediction distribution
     - Response time
     - User feedback (simulated)

5. Analysis Dashboard
   - Compare v1 vs v2 metrics
   - Which is better?
   - Statistical significance test

6. Gradual Rollout Simulation
   - Start: 90% v1, 10% v2
   - If v2 performs well: 50/50
   - If v2 still good: 10% v1, 90% v2
   - Finally: 100% v2

7. Rollback Procedure
   - Function to switch back to v1
   - Test rollback
   - Monitor after rollback

8. Documentation
   - Versioning strategy
   - A/B test results
   - Rollout plan
   - Rollback procedure
```

**Deliverables:**
- API with A/B testing
- Comparison dashboard
- A/B test results report

**Success Criteria:**
- Both versions deployed
- A/B testing works
- Can compare performance
- Rollback procedure tested

---

### Session 6: Complete MLOps Project (2 hours + 3-4 hours project time)

**Learning Objectives:**
1. Build complete ML application
2. Integrate all MLOps practices
3. Deploy with UI and monitoring
4. Create portfolio piece
5. Document production system

**Video Content (60 minutes):**

#### Video 6.1: Complete MLOps Pipeline (20 minutes)
- Full pipeline overview:
  - Development
  - Version control
  - Training
  - Evaluation
  - Deployment
  - Monitoring
  - Updating
- CI/CD for ML (brief)
- Production checklist

#### Video 6.2: Streamlit for ML UIs (15 minutes)
- Streamlit basics
- File upload
- User inputs
- Display predictions
- Charts and visualizations
- Deployment to Streamlit Cloud

#### Video 6.3: Production Documentation (15 minutes)
- README for users
- README for developers
- API documentation
- Architecture diagram
- Troubleshooting guide
- Portfolio presentation

#### Video 6.4: Portfolio and Job Search (10 minutes)
- What makes a good portfolio project
- How to present ML projects
- GitHub profile optimization
- Demo video
- LinkedIn/resume
- Interview talking points

**Hands-On Activity (180-240 minutes):**

**Capstone Project: Complete ML Application**

Options:
1. Stock Predictor with complete UI and monitoring
2. Image Classifier with web interface
3. Chatbot with deployment and logging

Code Requirements (using Stock Predictor example):
```python
# Complete production ML system:
1. Model Development
   - Train final stock predictor
   - Optimize for production
   - Save model properly

2. API Development (Flask or FastAPI)
   - POST /predict endpoint
   - Input validation
   - Error handling
   - Logging
   - Version endpoint (GET /version)
   - Health check (GET /health)

3. Streamlit UI
   - Stock ticker selection
   - Date range input
   - Predict button
   - Display prediction with confidence
   - Historical chart
   - Model info
   - Beautiful styling

4. Monitoring
   - Log all predictions
   - Dashboard showing:
     - Total predictions
     - Most predicted stocks
     - Prediction distribution
     - Model performance over time

5. Deployment
   - Deploy API to Heroku
   - Deploy UI to Streamlit Cloud
   - Connect UI to API
   - Test end-to-end

6. Version Control
   - Git repository
   - Proper .gitignore
   - Clear commit messages
   - README with setup instructions

7. Documentation
   - README.md:
     - Project overview
     - Features
     - Tech stack
     - Setup instructions (local)
     - Deployment guide
     - API documentation
     - Screenshots
   - API docs (Swagger or manual)
   - Code comments
   - Architecture diagram

8. Testing
   - Unit tests for key functions
   - API endpoint tests
   - End-to-end test

9. Production Checklist
   - [ ] Model trained and saved
   - [ ] API deployed and working
   - [ ] UI deployed and working
   - [ ] Monitoring functional
   - [ ] Documentation complete
   - [ ] Testing done
   - [ ] Public URLs obtained
   - [ ] Portfolio ready

10. Portfolio Presentation
    - Demo video (2-3 minutes)
    - Screenshots
    - GitHub README
    - Add to LinkedIn projects
```

**Deliverables:**
- Complete ML application (deployed)
- API (Heroku URL)
- UI (Streamlit Cloud URL)
- Monitoring dashboard
- GitHub repository (public)
- Documentation (README, API docs, architecture diagram)
- Demo video

**Success Criteria:**
- Fully functional deployed application
- API and UI work together
- Monitoring operational
- Complete documentation
- Portfolio-quality project
- Can demo confidently

---

## Module 9: Complete Dataset Requirements

**No new datasets needed!**
- Reuse models from Modules 2-8
- Stock predictor (Module 3)
- Spam detector (Module 2)
- Image classifier (Module 7)
- Chatbot (Module 8)

---

## Module 9: Complete Assessment Requirements

### Quizzes (6 total, ~54 questions)

**Session 1 Quiz (9 questions):**
- Production ML workflow
- Version control
- Model serialization
- Saving/loading models

**Session 2 Quiz (9 questions):**
- REST APIs
- Flask basics
- FastAPI
- ML API best practices

**Session 3 Quiz (9 questions):**
- Cloud platforms
- Heroku deployment
- Docker basics
- Production considerations

**Session 4 Quiz (9 questions):**
- Model degradation
- Monitoring metrics
- Logging
- Alerts

**Session 5 Quiz (9 questions):**
- Model versioning
- A/B testing
- Gradual rollout
- Rollback procedures

**Session 6 Quiz (9 questions):**
- Complete MLOps pipeline
- Streamlit
- Documentation
- Portfolio development

### Project Rubrics

**Session Projects (5 × 10 points = 50 points):**
- Correct implementation (50%)
- Working functionality (30%)
- Documentation (15%)
- Best practices (5%)

**Complete MLOps Application Capstone (150 points):**
- Model deployment (API) (30 points)
- User interface (30 points)
- Monitoring system (25 points)
- Documentation (25 points)
- Code quality and testing (20 points)
- Public accessibility (15 points)
- Portfolio presentation (5 points)

---

## Module 9: Visual Assets Needed

1. **Production ML Workflow Diagram**
2. **API Architecture Illustration**
3. **Deployment Process Flowchart**
4. **Monitoring Dashboard Screenshot**
5. **A/B Testing Concept**
6. **Complete MLOps Pipeline Diagram**

---

## Module 9: Success Metrics

**By end of module, learners should:**
- ✅ Save and load models correctly
- ✅ Build ML APIs (Flask/FastAPI)
- ✅ Deploy to cloud (Heroku or similar)
- ✅ Implement monitoring and logging
- ✅ Perform A/B testing
- ✅ Build complete production ML system
- ✅ Have at least 2 publicly deployed models

---

# MODULE 10: CAPSTONE PROJECT

## Module Overview

**Duration:** 3 weeks (4-5 hours guidance + 35-45 hours project work)
**Purpose:** Portfolio-worthy, job-ready capstone project
**Prerequisites:** All previous modules (integrate everything)
**Theory/Practice Ratio:** 5% / 95%

**The Hook:**
"Build YOUR masterpiece. The project that gets you hired."

**Emotional Arc:**
- Week 1: "I can really build anything I want? Exciting!"
- Week 2: "This is challenging but I'm making real progress!"
- Week 3: "I built an amazing ML system and I'm so proud!"

**Connection to Previous Modules:**
- Integrates techniques from ALL modules
- Uses supervised learning (Modules 2-4)
- May use unsupervised learning (Module 5)
- May use neural networks (Module 6)
- May use computer vision (Module 7)
- May use NLP (Module 8)
- MUST deploy (Module 9)

---

## Three-Week Structure

### Week 1: Planning & Design (6-9 hours)

#### Session 1: Project Selection & Planning (2-3 hours)

**Learning Objectives:**
1. Choose capstone project
2. Define scope clearly
3. Set success criteria
4. Create timeline
5. Get approval

**Guidance Content (30 minutes):**

**Video: Project Selection Strategies**
- Choosing a project you're passionate about
- Balancing ambition with feasibility
- Considering job market (what employers want)
- Portfolio differentiation

**Project Options:**

**Option 1: Stock Trading Strategy System (Finance)**
- Multi-stock prediction models
- Portfolio optimization
- Risk analysis
- Backtesting framework
- Real-time prediction API
- Trading signals dashboard
- Technical difficulty: High
- Business value: Very high
- Portfolio impact: Excellent

**Option 2: Cricket Analytics Platform (Sports)**
- Match outcome prediction
- Player performance analysis
- Team selection optimization
- Live score prediction
- Fantasy cricket assistant
- Interactive dashboard
- Technical difficulty: Medium-High
- Portfolio impact: Very good (unique!)

**Option 3: Healthcare Diagnostic Assistant**
- Disease prediction models (multiple conditions)
- Medical image analysis (X-rays, scans)
- Patient risk scoring
- Treatment recommendations
- Doctor dashboard
- Patient portal
- Technical difficulty: High
- Business value: Very high
- Portfolio impact: Excellent (social impact)

**Option 4: E-commerce Intelligence Suite**
- Customer segmentation
- Churn prediction
- Recommendation system
- Demand forecasting
- Sentiment analysis (reviews)
- Admin dashboard
- Technical difficulty: Medium
- Business value: High
- Portfolio impact: Very good

**Option 5: Manufacturing Quality Control System**
- Defect detection (computer vision)
- Predictive maintenance
- Process optimization
- Anomaly detection
- Real-time monitoring dashboard
- Quality prediction
- Technical difficulty: Medium-High
- Business value: High
- Portfolio impact: Very good

**Option 6: Custom Project (Proposed by Student)**
- Must integrate 3+ ML techniques
- Must include supervised AND (unsupervised OR deep learning)
- Must deploy to production
- Must have real-world applicability
- Requires approval

**Activity:**
- Choose project option
- Write 1-2 page proposal:
  - Problem statement
  - Solution approach
  - ML techniques to use (list from Modules 2-9)
  - Data sources
  - Success criteria (specific metrics)
  - Timeline (week by week)
  - Risks and mitigations

**Deliverable:** Project Proposal Document

---

#### Session 2: Data Collection & EDA (3-4 hours)

**Learning Objectives:**
1. Gather/create dataset
2. Perform thorough EDA
3. Assess data quality
4. Plan preprocessing
5. Document findings

**Guidance Content (30 minutes):**

**Video: Data Collection Strategies**
- Finding datasets (Kaggle, UCI, APIs, web scraping)
- Creating synthetic data
- Data licensing and ethics
- How much data is enough?

**Activity:**
- Collect dataset(s) for chosen project
- Load and explore data
- EDA notebook:
  - Dataset statistics
  - Missing values analysis
  - Class distribution (if classification)
  - Feature distributions
  - Correlations
  - Visualizations (10-15 plots)
  - Insights and observations
  - Data quality issues identified
  - Preprocessing plan

**Deliverable:** EDA Report (Jupyter notebook with analysis and insights)

---

#### Session 3: Architecture Design (2-3 hours)

**Learning Objectives:**
1. Design system architecture
2. Plan ML pipeline
3. Choose technology stack
4. Plan deployment strategy
5. Create visual architecture

**Guidance Content (30 minutes):**

**Video: System Architecture for ML**
- Components: Data layer, ML layer, API layer, UI layer, monitoring layer
- Design patterns
- Scalability considerations
- Technology choices

**Activity:**
- Create architecture diagram (draw.io, Lucidchart, or hand-drawn)
- Document:
  - Data flow (from source to prediction)
  - ML pipeline components
  - API endpoints
  - UI components
  - Deployment plan
  - Technology stack:
    - Languages (Python)
    - ML libraries (scikit-learn, TensorFlow, etc.)
    - API framework (Flask/FastAPI)
    - UI framework (Streamlit, HTML/JS)
    - Cloud platform (Heroku, AWS, etc.)
    - Database (if needed)
- Timeline with milestones

**Deliverable:** Architecture Document with diagram and tech stack

---

### Week 2: Implementation (18-22 hours)

#### Session 4: Model Development (6-8 hours)

**Learning Objectives:**
1. Try multiple algorithms
2. Feature engineering
3. Hyperparameter tuning
4. Model selection
5. Achieve target performance

**Guidance Content (30 minutes):**

**Video: Systematic Model Development**
- Baseline model first
- Try multiple algorithms
- Cross-validation
- Hyperparameter tuning strategies
- Model selection criteria

**Activity:**
- Implement complete ML pipeline:
  - Data preprocessing
  - Feature engineering (use techniques from course)
  - Train multiple models (at least 3):
    - Baseline (simple model)
    - Traditional ML (Random Forest, XGBoost, etc.)
    - Deep learning (if applicable)
  - Evaluate all models
  - Hyperparameter tuning on best model(s)
  - Select final model(s)
- Apply techniques from all modules as appropriate:
  - Proper evaluation (Module 4)
  - Unsupervised learning if needed (Module 5)
  - Neural networks if applicable (Module 6)
  - CNNs for images (Module 7)
  - NLP techniques for text (Module 8)

**Deliverable:** Trained Models with Evaluation Report

---

#### Session 5: Optimization & Testing (4-6 hours)

**Learning Objectives:**
1. Improve model accuracy
2. Handle edge cases
3. Error analysis
4. Robustness testing
5. Final model validation

**Guidance Content (30 minutes):**

**Video: Model Optimization and Testing**
- Analyzing errors
- Improving based on error analysis
- Edge case handling
- Robustness tests
- Final validation

**Activity:**
- Error analysis:
  - Identify failure patterns
  - Analyze misclassifications/poor predictions
  - Hypothesize reasons
- Improvement strategies:
  - More feature engineering
  - Handle edge cases
  - Ensemble methods
  - Threshold optimization
- Testing:
  - Test on held-out data
  - Test edge cases
  - Robustness checks
  - Cross-validation (if not done yet)
- Final model:
  - Optimized and validated
  - Ready for deployment

**Deliverable:** Optimized Final Model with Testing Report

---

#### Session 6: Deployment (6-8 hours)

**Learning Objectives:**
1. Build production API
2. Deploy to cloud
3. Create user interface
4. Integrate components
5. Test deployed system

**Guidance Content (30 minutes):**

**Video: Deployment Best Practices**
- Recap Module 9 techniques
- API development
- Cloud deployment
- UI creation
- Integration testing

**Activity:**
- Build API:
  - Flask or FastAPI
  - Prediction endpoint
  - Input validation
  - Error handling
  - Logging
- Deploy API:
  - Heroku or chosen platform
  - Test deployed API
- Create UI:
  - Streamlit app or web interface
  - User-friendly design
  - Input forms
  - Display predictions
  - Visualizations
- Deploy UI:
  - Streamlit Cloud or static hosting
- Integration:
  - Connect UI to API
  - End-to-end testing
  - Fix any bugs

**Deliverable:** Deployed Application (public URLs for API and UI)

---

### Week 3: Polish & Present (12-16 hours)

#### Session 7: Documentation (4-5 hours)

**Learning Objectives:**
1. Create comprehensive README
2. Document API
3. Comment code thoroughly
4. Provide usage examples
5. Professional presentation

**Guidance Content (30 minutes):**

**Video: Professional Documentation**
- README best practices
- API documentation standards
- Code comments
- User guides
- Portfolio presentation

**Activity:**
- README.md:
  - Project title and description
  - Problem statement
  - Solution overview
  - Tech stack
  - Architecture diagram
  - Setup instructions (local)
  - Usage guide
  - API documentation
  - Deployed app links
  - Screenshots/GIFs
  - Performance metrics
  - Future improvements
  - Acknowledgements
- API Documentation:
  - All endpoints
  - Request/response formats
  - Examples
- Code Comments:
  - Docstrings for all functions
  - Inline comments where needed
- User Guide:
  - How to use the application
  - Input requirements
  - Expected outputs

**Deliverable:** Complete Documentation

---

#### Session 8: Presentation Preparation (4-5 hours)

**Learning Objectives:**
1. Create presentation slides
2. Record demo video
3. Prepare demo script
4. Practice presentation
5. Prepare for Q&A

**Guidance Content (30 minutes):**

**Video: Presenting Technical Projects**
- Storytelling for technical projects
- Slide design
- Demo best practices
- Handling Q&A
- Portfolio and resume integration

**Activity:**
- Create Presentation Slides:
  - Title slide (project name, your name)
  - Problem statement (why does this matter?)
  - Solution overview (what you built)
  - Data and methodology
  - Model performance (metrics, visualizations)
  - System architecture
  - Demo (screenshots or embedded)
  - Challenges and learnings
  - Future work
  - Q&A
- Record Demo Video:
  - 2-3 minutes
  - Show the application working
  - Narrate what's happening
  - Highlight key features
  - Show results
- Demo Script:
  - What to say during live demo
  - Which features to highlight
  - Backup plan if demo fails
- Practice:
  - Present to camera
  - Time yourself (aim for 5-7 minutes + demo)
  - Refine based on practice

**Deliverable:** Presentation Slides and Demo Video

---

#### Session 9: Final Review & Submission (4-6 hours)

**Learning Objectives:**
1. Code review and cleanup
2. Final testing
3. Peer review
4. Submit all deliverables
5. Celebrate!

**Guidance Content (30 minutes):**

**Video: Final Review Checklist**
- Code quality review
- Testing checklist
- Submission requirements
- Portfolio integration
- Next steps (job search, further learning)

**Activity:**
- Code Review:
  - Read through all code
  - Refactor if needed
  - Remove commented-out code
  - Ensure consistent style
  - Check all functions work
- Final Testing:
  - End-to-end test
  - Test on different devices
  - Test edge cases
  - Fix any bugs
- Peer Review:
  - Exchange projects with peers
  - Review each other's work
  - Provide constructive feedback
  - Incorporate feedback
- Submission Checklist:
  - [ ] Code repository (GitHub, public)
  - [ ] Deployed API (working URL)
  - [ ] Deployed UI (working URL)
  - [ ] README complete
  - [ ] API documentation
  - [ ] Demo video
  - [ ] Presentation slides
  - [ ] All code commented
  - [ ] Testing done
- Portfolio Integration:
  - Add to GitHub profile README
  - Add to LinkedIn projects
  - Add to resume
  - Prepare elevator pitch
- Celebrate:
  - You built an amazing ML system!
  - Share with friends and family
  - Post on LinkedIn
  - You're job-ready!

**Deliverable:** Complete Project Package (all deliverables submitted)

---

## Module 10: Complete Deliverables Checklist

**Each student must submit:**

1. **Code Repository (GitHub)**
   - All source code
   - Clean and commented
   - .gitignore properly configured
   - README.md (comprehensive)

2. **Deployed Application**
   - API (publicly accessible URL)
   - UI (publicly accessible URL)
   - Both working and integrated

3. **Documentation**
   - README.md (project overview, setup, usage)
   - API documentation (endpoints, examples)
   - Architecture diagram
   - User guide

4. **Presentation Materials**
   - Slides (PDF or Google Slides link)
   - Demo video (2-3 minutes, uploaded to YouTube or similar)
   - Transcript or demo script

5. **Technical Report** (Optional but Recommended)
   - Problem statement
   - Data and methodology
   - Model development process
   - Results and evaluation
   - Challenges and solutions
   - Future work
   - 10-15 pages

---

## Module 10: Assessment Rubric (200 points total)

### Technical Implementation (100 points)

**Data and Preprocessing (15 points)**
- Data collection and quality (5)
- Preprocessing and feature engineering (5)
- EDA thoroughness (5)

**Model Development (30 points)**
- Multiple models tried (10)
- Proper evaluation (Module 4 techniques) (10)
- Hyperparameter tuning (5)
- Performance meets targets (5)

**Deployment (25 points)**
- Working API (10)
- Working UI (10)
- Integration (5)

**Code Quality (15 points)**
- Clean, readable code (5)
- Proper comments and docstrings (5)
- Best practices followed (5)

**Testing (15 points)**
- Unit tests or API tests (5)
- End-to-end testing (5)
- Edge case handling (5)

### Documentation & Presentation (60 points)

**Documentation (30 points)**
- README completeness (10)
- API documentation (10)
- Code comments (5)
- User guide (5)

**Presentation (20 points)**
- Slide quality (5)
- Demo video quality (5)
- Storytelling and clarity (10)

**Peer Review (10 points)**
- Provide constructive feedback to peers (5)
- Incorporate feedback received (5)

### Innovation & Impact (40 points)

**Technical Innovation (15 points)**
- Novel approach or creative solution (5)
- Integration of multiple techniques (5)
- Technical complexity (5)

**Real-World Applicability (15 points)**
- Solves real problem (5)
- Business or social value (5)
- Potential for real-world use (5)

**Portfolio Quality (10 points)**
- Professional presentation (5)
- Portfolio-worthy quality (5)

---

## Module 10: Example Capstone Specifications

### Option 1: Stock Trading Strategy System (Detailed Example)

**Problem Statement:**
Develop a comprehensive stock trading system that predicts stock prices, optimizes portfolio allocation, and provides trading signals.

**Required Components:**
1. **Data Collection:**
   - Historical stock data (5+ years, 10+ stocks)
   - Technical indicators
   - Market sentiment (optional)

2. **ML Models (Multiple):**
   - Price prediction (regression - Module 3)
   - Trend classification (up/down/sideways - Module 2)
   - Anomaly detection (unusual movements - Module 5)
   - (Optional) Deep learning (LSTM - Module 6)

3. **Analysis Components:**
   - Portfolio optimization (risk vs return)
   - Backtesting framework
   - Risk analysis
   - Trading signal generation

4. **Deployment:**
   - API for predictions
   - Interactive dashboard (Streamlit):
     - Stock selection
     - Price predictions
     - Portfolio recommendations
     - Historical performance charts
     - Risk metrics
   - Real-time updates (bonus)

5. **Documentation:**
   - Complete README
   - API documentation
   - User guide
   - Trading strategy explanation

**Success Criteria:**
- Price prediction R² > 0.70
- Backtesting shows positive returns
- Working deployed application
- Comprehensive documentation

**Technical Difficulty:** High
**Estimated Time:** 40-50 hours

---

## Module 10: Success Metrics

**By end of module, learners should:**
- ✅ Complete original ML project from scratch
- ✅ Integrate techniques from multiple modules
- ✅ Deploy fully functional application
- ✅ Create professional documentation
- ✅ Present work effectively
- ✅ Have portfolio-worthy capstone
- ✅ Be job-ready

---

# CROSS-MODULE REQUIREMENTS (Modules 7-10)

## Shared Code Libraries

### From Previous Modules:
- Feature engineering library (Module 3)
- Evaluation metrics library (Module 4)
- Preprocessing utilities (Modules 1-8)

### New for Modules 7-10:
- Image preprocessing utilities (Module 7)
- Text preprocessing utilities (Module 8)
- Deployment utilities (Module 9)

## Consistent Documentation Standards

### Notebook Template:
- Title and overview
- Imports and setup
- Data loading
- EDA
- Preprocessing
- Model building
- Training
- Evaluation
- Visualizations
- Conclusions and next steps

### Deployment README Template:
- Project overview
- Features
- Tech stack
- Architecture diagram
- Setup instructions (local and cloud)
- API documentation
- Usage guide
- Screenshots
- Performance metrics
- Future improvements

## Visual Design Consistency

### Colors (consistent across all modules):
- Primary: Blue (#1f77b4)
- Secondary: Orange (#ff7f0e)
- Success: Green (#2ca02c)
- Error: Red (#d62728)
- Neutral: Gray (#7f7f7f)

### Plot Standards:
- Figure sizes: (12, 6) or (10, 8)
- Grid: Always on
- Font sizes: Title 14, Labels 12, Ticks 10
- DPI: 100
- Style: seaborn default

---

# PRODUCTION PRIORITIES (Modules 7-10)

## High Priority (Core Functionality)
1. All code notebooks working correctly
2. All datasets sourced or generated
3. All models achieving target metrics
4. Deployment for at least 2 projects per module

## Medium Priority (Quality)
5. Complete quiz banks (54 questions per module)
6. Detailed rubrics for all projects
7. Comprehensive README files
8. API documentation

## Lower Priority (Enhancement)
9. Visual assets (diagrams, illustrations)
10. Video scripts (detailed)
11. Advanced extensions
12. Optional bonus projects

---

**Status:** DETAILED SPECIFICATIONS COMPLETE FOR MODULES 7-10
**Ready for:** Agent deployment for production material creation
**Estimated Time per Module:**
- Module 7: 20-25 hours
- Module 8: 20-25 hours
- Module 9: 15-20 hours
- Module 10: 10-15 hours (mostly guidance)

---

**Created:** 2026-01-06
**Version:** 1.0 (Production Specifications)
**Total Pages:** 100+ (comprehensive detail for all 4 modules)
**Total Estimated Production Time:** 65-85 hours for all 4 modules
