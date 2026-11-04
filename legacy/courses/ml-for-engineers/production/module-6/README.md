# Module 6: Neural Networks & Deep Learning
## Introduction to Deep Learning for ML Engineers

**Duration:** 2 weeks (14-16 hours video + 25-30 hours hands-on)
**Prerequisites:** Modules 2-5 (Strong ML foundation required)
**Difficulty:** Intermediate to Advanced

---

## Module Overview

**The Hook:**
*"Traditional ML is great... but neural networks can learn MORE complex patterns!"*

**The Question:**
*"When should I use Neural Networks vs Traditional ML?"*

**The Answer:**
By the end of this module, you'll know exactly when neural networks shine and when traditional ML is better!

---

## What You'll Learn

### Core Skills:
1. ✅ Build neural networks with Keras/TensorFlow
2. ✅ Achieve MNIST >98% accuracy
3. ✅ Apply transfer learning to new tasks
4. ✅ Use LSTM for time series
5. ✅ Compare deep learning to traditional ML
6. ✅ Make informed decisions on ML vs DL

### Technical Skills:
- Keras Sequential API
- Dense, LSTM layers
- Activation functions (ReLU, Softmax, Sigmoid)
- Loss functions and optimizers
- Dropout and Batch Normalization
- Early stopping and learning rate scheduling
- Transfer learning (VGG16, ResNet)
- Model evaluation and comparison

### Decision-Making Skills:
- When to use NNs vs Traditional ML
- Architecture design for different problems
- Regularization techniques
- Hyperparameter tuning for NNs

---

## Module Structure

### Session 1: Introduction to Neural Networks (2 hours)
**Notebook:** `iris-neural-network.ipynb`

**Topics:**
- What are neural networks?
- Neurons, layers, and connections
- Forward propagation
- NN vs Traditional ML comparison

**Project:** Build simple NN for Iris, compare to Decision Tree
**Target:** 95%+ accuracy
**Key Insight:** For small datasets, traditional ML often wins!

---

### Session 2: Building with Keras (2 hours)
**Notebook:** `mnist-digit-recognition.ipynb`

**Topics:**
- Keras Sequential API
- Dense layers
- Activation functions (ReLU, Softmax)
- Model compilation
- Training and evaluation

**Project:** MNIST digit recognizer (baseline)
**Target:** >95% accuracy
**Key Skill:** Build and train neural networks from scratch

---

### Session 3: Training Neural Networks (2 hours)
**Notebook:** `fashion-mnist-training.ipynb`

**Topics:**
- Loss functions deep dive
- Optimizers (SGD, Adam)
- Batch size and epochs
- Early stopping
- Training dynamics

**Project:** Fashion MNIST classifier with systematic experiments
**Target:** >85% accuracy
**Key Skill:** Train NNs effectively through experimentation

---

### Session 4: Regularization & Optimization (2 hours)
**Notebook:** `mnist-optimized-98plus.ipynb`

**Topics:**
- Overfitting in neural networks
- Dropout regularization
- Batch Normalization
- Learning rate scheduling
- Advanced callbacks

**Project:** Improve MNIST from 95% to >98%
**Target:** >98% accuracy
**Key Achievement:** Eliminate 60% of errors through optimization!

---

### Session 5: Transfer Learning (2 hours)
**Notebook:** `transfer-learning-vgg16.ipynb`

**Topics:**
- Transfer learning concept
- Pre-trained models (VGG16, ResNet)
- Feature extraction vs fine-tuning
- Freezing/unfreezing layers
- Data augmentation

**Project:** Image classification with VGG16
**Target:** >90% accuracy
**Key Insight:** Stand on the shoulders of giants!

---

### Session 6: Neural Networks for Tabular Data + CAPSTONE (3-4 hours)
**Notebook:** `stock-predictor-neural-network.ipynb`

**Topics:**
- NNs for structured data
- Architecture design for tabular data
- LSTM for sequences
- NN vs Traditional ML (the ultimate comparison)

**Capstone:** Stock predictor with LSTM and Dense NNs
**Compare to:** Random Forest and Linear Regression (Module 3)
**Target:** R² > 0.70
**Key Deliverable:** Complete decision framework for ML vs DL

---

## The Learning Journey

### Emotional Arc:
- **Start:** "I've been doing well with sklearn... why learn something harder?"
- **Middle:** "Whoa! This network just learned to recognize handwritten digits at 98%!"
- **End:** "I can build deep learning models AND know when to use them vs traditional ML!"

### From Module 0 to Module 6:
- **Module 0:** "Wow! A stock predictor demo!"
- **Module 1:** "I can explore stock data!"
- **Module 2:** "I understand classification!"
- **Module 3:** "I BUILT a stock predictor with Random Forest!"
- **Module 4-5:** "I can evaluate and optimize models!"
- **Module 6:** "I can use NEURAL NETWORKS and know WHEN to use them!"

---

## Performance Targets

| Session | Project | Target | Difficulty |
|---------|---------|--------|------------|
| 1 | Iris NN | 95%+ accuracy | Easy |
| 2 | MNIST Baseline | >95% accuracy | Medium |
| 3 | Fashion MNIST | >85% accuracy | Medium |
| 4 | MNIST Optimized | >98% accuracy | Hard |
| 5 | Transfer Learning | >90% accuracy | Medium |
| 6 | Stock Predictor NN | R² >0.70 | Hard |

**All targets are achievable with provided notebooks!**

---

## Key Datasets

1. **Iris** - Built into sklearn (150 samples)
2. **MNIST Digits** - Built into Keras (70,000 images)
3. **Fashion MNIST** - Built into Keras (70,000 images)
4. **Stock Data** - Yahoo Finance via yfinance (reuse Module 3)
5. **Flowers/Cats-Dogs** - TensorFlow Datasets or Kaggle

**Download Script:** `datasets/download_module6_datasets.py`
**Full Guide:** `datasets/datasets-readme.md`

---

## System Requirements

### Minimum:
- **RAM:** 8 GB
- **Disk:** 2 GB
- **CPU:** Multi-core
- **Python:** 3.7+

### Recommended:
- **RAM:** 16 GB+
- **GPU:** NVIDIA GPU with CUDA support (or use Google Colab!)
- **Python:** 3.8-3.10

### Install:
```bash
pip install tensorflow scikit-learn pandas numpy matplotlib seaborn yfinance
```

---

## Module Philosophy

### The Most Important Lesson:

**More complex models aren't always better!**

- Start simple (Linear Regression, Logistic Regression)
- Try proven methods (Random Forest, XGBoost)
- Add complexity only if needed (Neural Networks)
- Measure, compare, decide!

### When Neural Networks Excel:
✅ Large datasets (>100k samples)
✅ Unstructured data (images, text, audio)
✅ Complex non-linear patterns
✅ Sequential dependencies (LSTM)
✅ You have GPU resources

### When Traditional ML Wins:
✅ Small-medium tabular datasets
✅ Need interpretability
✅ Limited compute resources
✅ Fast training required
✅ Simpler is better

---

## Decision Framework

### For Tabular Data (like stock prediction):

**1. Start with Random Forest**
- Fast to train
- Good performance
- Feature importance
- Interpretable

**2. If RF achieves your goals → STOP!**
- Don't add complexity unnecessarily
- Simpler = easier to maintain

**3. Try Neural Networks if:**
- RF falls short of requirements
- You have >100k rows of data
- You need the extra 2-5% improvement
- Willing to trade interpretability

### For Images/Text/Audio:

**Always use Neural Networks (or pre-trained models!)**
- Traditional ML doesn't work well
- Transfer learning makes it easy
- Pre-trained models save time

---

## Success Metrics

**By end of module, you should be able to:**
- ✅ Build neural networks with Keras
- ✅ Achieve MNIST >98% accuracy
- ✅ Apply transfer learning successfully
- ✅ Understand when to use NNs vs traditional ML
- ✅ Build LSTM for time series
- ✅ Compare deep learning to previous methods
- ✅ Make informed decisions on ML vs DL

---

## Project Structure

```
module-6/
├── code/
│   ├── iris-neural-network.ipynb
│   ├── mnist-digit-recognition.ipynb
│   ├── fashion-mnist-training.ipynb
│   ├── mnist-optimized-98plus.ipynb
│   ├── transfer-learning-vgg16.ipynb
│   └── stock-predictor-neural-network.ipynb (CAPSTONE)
├── datasets/
│   ├── download_module6_datasets.py
│   └── datasets-readme.md
├── quizzes/
│   └── module-6-quizzes.json (54 questions)
├── rubrics/
│   └── module-6-rubrics.md
└── README.md (this file)
```

---

## Assessments

### Quizzes:
- **Total Questions:** 54
- **Format:** Multiple choice with explanations
- **Coverage:** All 6 sessions
- **Topics:** NN basics, Keras, training, regularization, transfer learning, NN vs ML

### Session Projects:
- **5 projects** (15 points each = 75 points)
- **Rubric:** Implementation, accuracy, visualizations, documentation

### Capstone Project:
- **Stock Predictor with Neural Networks** (100 points)
- **Components:** LSTM, Dense NN, Random Forest, Linear Regression
- **Key:** Comprehensive comparison and decision framework

**Total: 175 points**

---

## Getting Started

### Step 1: Setup
```bash
# Install required packages
pip install tensorflow scikit-learn pandas numpy matplotlib seaborn yfinance

# Verify TensorFlow
python -c "import tensorflow as tf; print(tf.__version__)"
```

### Step 2: Download Datasets
```bash
cd datasets
python download_module6_datasets.py
```

### Step 3: Start Learning
1. Open `iris-neural-network.ipynb`
2. Work through each session sequentially
3. Complete all projects
4. Build the capstone!

---

## Common Challenges & Solutions

### Challenge 1: Training is slow
**Solutions:**
- Use GPU (or Google Colab)
- Reduce batch size
- Reduce model size
- Use fewer epochs

### Challenge 2: Model doesn't converge
**Solutions:**
- Check data normalization (critical!)
- Reduce learning rate
- Try different optimizer
- Check for NaN values

### Challenge 3: Overfitting
**Solutions:**
- Add Dropout
- Add Batch Normalization
- Use Early Stopping
- Get more data

### Challenge 4: Can't install TensorFlow
**Solutions:**
- Use Google Colab (free GPU!)
- Try: `pip install tensorflow==2.12.0`
- Check Python version (3.7-3.10)

---

## Tips for Success

1. **Start Simple**
   - Begin with small models
   - Add complexity gradually
   - Understand each component

2. **Visualize Everything**
   - Training curves
   - Confusion matrices
   - Model architecture
   - Comparisons

3. **Compare to Baselines**
   - Always have a baseline (Linear Regression)
   - Try traditional ML first
   - Show improvements

4. **Document Your Journey**
   - Explain your choices
   - Document experiments
   - Share insights

5. **Embrace Failure**
   - Models won't always reach targets
   - Learn from failures
   - Iterate and improve

---

## Resources

### Official Documentation:
- TensorFlow: https://www.tensorflow.org/
- Keras: https://keras.io/
- scikit-learn: https://scikit-learn.org/

### Additional Learning:
- Deep Learning Specialization (Coursera)
- Fast.ai Course
- CS231n (Stanford)
- Neural Networks and Deep Learning (book)

### Tools:
- Google Colab (free GPU!)
- TensorBoard (visualization)
- Weights & Biases (experiment tracking)

---

## Next Steps

After completing Module 6, you're ready for:

- **Module 7:** Computer Vision & CNNs
  - Convolutional Neural Networks
  - Image classification
  - Object detection

- **Module 8:** Natural Language Processing
  - Text processing
  - Sentiment analysis
  - Transformers

- **Module 9:** Model Deployment
  - Production ML
  - APIs and web apps
  - MLOps basics

---

## FAQ

**Q: Do I need a GPU?**
A: No, but it helps! Use Google Colab for free GPU access.

**Q: Can I skip straight to deep learning?**
A: Don't skip Modules 2-3! You need traditional ML foundation.

**Q: What if I can't reach accuracy targets?**
A: Document your efforts, show experiments. Partial credit given.

**Q: Should I always use neural networks now?**
A: NO! Use the decision framework. Often traditional ML is better.

**Q: How long does this module take?**
A: 2-3 weeks with 15-20 hours per week.

---

## The Big Picture

### Module 6 in Context:

You've come a long way:
- **Modules 0-1:** Basics and foundations
- **Modules 2-3:** Traditional ML (classification, regression)
- **Modules 4-5:** Evaluation and unsupervised learning
- **Module 6:** Neural networks and deep learning ← YOU ARE HERE
- **Modules 7-8:** Advanced deep learning (CV, NLP)
- **Module 9:** Production and deployment

**You're 60% through the course!** 🎉

---

## The Ultimate Goal

By the end of Module 6, you should be able to confidently answer:

**"When should I use Neural Networks vs Traditional ML?"**

And back it up with:
- Hands-on experience with both
- Performance comparisons
- Real-world examples
- A decision framework

**That's valuable ML engineering wisdom!**

---

## Final Thoughts

**Remember:**
- Neural networks are powerful tools
- But they're not magic
- Traditional ML often works just as well
- Choose the right tool for the job
- Simpler is often better
- Measure, compare, decide!

**Good luck with Module 6!** 🚀

You're learning one of the most exciting technologies in AI. Enjoy the journey!

---

**Module 6 Created:** 2026-01-05
**Status:** Production-ready
**Questions?** Check the FAQ or ask your instructor!
