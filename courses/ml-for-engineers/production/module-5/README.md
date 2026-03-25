# Module 5: Unsupervised Learning

## Discover Patterns Without Labels!

**Duration:** 2 weeks (12-14 hours video + 20-25 hours hands-on)
**Difficulty:** Intermediate
**Prerequisites:** Modules 2-4 (Supervised Learning & Model Evaluation)

---

## Module Overview

### The Hook
"What if you DON'T have labels? Find hidden patterns in your data without expensive labeling!"

### What You'll Learn
This module introduces unsupervised learning - discovering structure and patterns in data without labeled examples. You'll master clustering algorithms, dimensionality reduction techniques, and anomaly detection methods essential for real-world machine learning.

### Why It Matters
- Most real-world data is unlabeled
- Labels are expensive and time-consuming to obtain
- Discover insights you didn't know to look for
- Complement supervised learning approaches
- Essential for exploratory data analysis

---

## Module Structure

### Session 1: K-Means Clustering (2 hours)
**Project:** Customer Segmentation for E-commerce

Learn the foundational clustering algorithm and apply it to segment 2,000 customers into distinct marketing groups.

**Key Concepts:**
- Supervised vs unsupervised learning
- K-Means algorithm mechanics
- Elbow method for selecting K
- Silhouette analysis for cluster quality
- Customer profiling and business insights

**Deliverables:**
- `customer-segmentation-kmeans.ipynb`
- 4-5 distinct customer segments
- Marketing recommendations per segment

---

### Session 2: Hierarchical Clustering & DBSCAN (2 hours)
**Project:** Patient Grouping for Healthcare

Compare three clustering algorithms on medical data to identify patient risk groups and outliers.

**Key Concepts:**
- Hierarchical (agglomerative) clustering
- Dendrograms and linkage methods
- DBSCAN (density-based clustering)
- Outlier detection
- Algorithm comparison and selection

**Deliverables:**
- `patient-clustering-comparison.ipynb`
- 3+ patient groups identified
- Outliers/high-risk patients flagged
- Method comparison and recommendations

---

### Session 3: Real-World Clustering Applications (2 hours)
**Project:** News Article Clustering with NLP

Apply clustering to text data to discover topics without labeled categories.

**Key Concepts:**
- Text preprocessing (tokenization, stop words, lemmatization)
- TF-IDF vectorization
- Document clustering
- Topic discovery
- Word clouds and visualization

**Deliverables:**
- `news-clustering-unsupervised.ipynb`
- Topics discovered from 1,200+ articles
- Word clouds per cluster
- Comparison to supervised categories

---

### Session 4: PCA - Principal Component Analysis (2 hours)
**Project:** High-Dimensional Data Visualization

Master dimensionality reduction to visualize complex data and speed up algorithms.

**Key Concepts:**
- Curse of dimensionality
- PCA intuition and mathematics
- Explained variance
- Dimensionality reduction (784D → 2D)
- PCA before clustering for speed

**Deliverables:**
- `pca-dimensionality-reduction.ipynb`
- MNIST digits visualized in 2D/3D
- 90%+ variance retained with fewer dimensions
- Speed improvements demonstrated

---

### Session 5: t-SNE & Advanced Visualization (2 hours)
**Project:** PCA vs t-SNE Comparison

Learn when to use linear (PCA) vs nonlinear (t-SNE) dimensionality reduction.

**Key Concepts:**
- t-SNE (t-Distributed Stochastic Neighbor Embedding)
- PCA vs t-SNE tradeoffs
- Perplexity parameter tuning
- Local vs global structure preservation
- UMAP introduction

**Deliverables:**
- `tsne-advanced-visualization.ipynb`
- Side-by-side PCA vs t-SNE visualizations
- Perplexity exploration
- Decision guide for PCA vs t-SNE

---

### Session 6: Anomaly Detection (2 hours + Capstone)
**Project:** Fraud Detection WITHOUT Labels

Apply unsupervised anomaly detection and compare to supervised approaches.

**Key Concepts:**
- Anomaly detection fundamentals
- Isolation Forest algorithm
- One-Class SVM
- Supervised vs unsupervised comparison
- Hybrid approaches

**Deliverables:**
- `fraud-detection-unsupervised.ipynb`
- 10,000 transactions analyzed (5% fraud)
- Precision > 50%, Recall > 40%
- Decision framework: when to use supervised vs unsupervised
- Comprehensive comparison to Module 4

---

## Learning Outcomes

By the end of this module, you will be able to:

1. **Understand Unsupervised Learning**
   - Explain difference between supervised and unsupervised
   - Identify when unsupervised methods are appropriate
   - Apply unsupervised learning to real problems

2. **Master Clustering Algorithms**
   - Implement K-Means with optimal K selection
   - Apply hierarchical clustering and read dendrograms
   - Use DBSCAN for arbitrary-shaped clusters and outlier detection
   - Compare and choose appropriate clustering algorithms

3. **Reduce Dimensionality**
   - Apply PCA for dimensionality reduction
   - Visualize high-dimensional data in 2D/3D
   - Use t-SNE for beautiful visualizations
   - Understand PCA vs t-SNE tradeoffs

4. **Detect Anomalies**
   - Implement Isolation Forest and One-Class SVM
   - Detect anomalies without labeled examples
   - Compare unsupervised to supervised detection
   - Design hybrid approaches

5. **Make Informed Decisions**
   - Choose between supervised and unsupervised approaches
   - Understand performance tradeoffs
   - Apply appropriate methods to business problems
   - Communicate insights from unsupervised learning

---

## Datasets

All datasets are either synthetic (reproducible) or built into scikit-learn:

1. **E-commerce Customers** (2,000 customers)
   - Features: Recency, Frequency, Monetary, Age, Web visits
   - Source: Synthetic (generated)

2. **Patient Health Data** (800 patients)
   - Features: Age, BMI, Blood pressure, Glucose, Cholesterol
   - Source: Synthetic (generated)

3. **News Articles** (1,200 articles)
   - Features: Text content, 3 categories
   - Source: Synthetic (generated)

4. **MNIST Digits** (1,797 images)
   - Features: 64 dimensions (8×8 grayscale images)
   - Source: Built into scikit-learn

5. **Credit Card Fraud** (10,000 transactions)
   - Features: Amount, Time, Distance, Risk score
   - Source: Synthetic (generated)

### Download Datasets
```bash
cd production/module-5/datasets
python download_unsupervised_datasets.py
```

All datasets will be saved to `datasets/data/` directory.

---

## Technical Requirements

### Python Libraries
```bash
pip install numpy pandas matplotlib seaborn scikit-learn
pip install wordcloud  # For text clustering visualization
```

### Recommended Setup
- Python 3.8+
- Jupyter Notebook or JupyterLab
- 4GB+ RAM (for dimensionality reduction on larger datasets)

---

## Project Structure

```
module-5/
├── README.md                          # This file
├── code/                              # Jupyter notebooks
│   ├── customer-segmentation-kmeans.ipynb
│   ├── patient-clustering-comparison.ipynb
│   ├── news-clustering-unsupervised.ipynb
│   ├── pca-dimensionality-reduction.ipynb
│   ├── tsne-advanced-visualization.ipynb
│   └── fraud-detection-unsupervised.ipynb  # CAPSTONE
├── datasets/                          # Data and download script
│   ├── download_unsupervised_datasets.py
│   ├── datasets-readme.md
│   └── data/                          # Generated datasets
├── quizzes/                           # Assessment materials
│   └── module-5-quizzes.json         # 54 questions
├── rubrics/                           # Grading guidelines
│   └── module-5-rubrics.md
└── projects/                          # Additional resources
```

---

## Getting Started

### 1. Setup Environment
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Download Datasets
```bash
cd datasets
python download_unsupervised_datasets.py
```

### 3. Start with Session 1
```bash
cd ../code
jupyter notebook customer-segmentation-kmeans.ipynb
```

---

## Key Concepts Reference

### Clustering Algorithms Comparison

| Algorithm | Pros | Cons | Best For |
|-----------|------|------|----------|
| **K-Means** | Fast, scalable, simple | Requires K, assumes spherical clusters | Large datasets, known K |
| **Hierarchical** | No K needed, dendrogram | Slow (O(n³)), memory-intensive | Small datasets, explore structure |
| **DBSCAN** | Arbitrary shapes, outliers | Sensitive to parameters | Irregular clusters, outlier detection |

### Dimensionality Reduction Comparison

| Method | Speed | Structure Preserved | Transform New Data | Best For |
|--------|-------|---------------------|-------------------|----------|
| **PCA** | Fast | Global | Yes | Preprocessing, feature extraction |
| **t-SNE** | Slow | Local | No | Visualization only |
| **UMAP** | Medium | Local + Global | Yes | Best of both worlds |

### Supervised vs Unsupervised

| Aspect | Supervised | Unsupervised |
|--------|------------|--------------|
| **Labels Required** | Yes | No |
| **Accuracy** | Higher (~85-95%) | Lower (~50-70%) |
| **Use Case** | Known patterns | Pattern discovery |
| **Example** | Fraud detection (with labels) | Customer segmentation |
| **Cost** | High (labeling) | Low (no labels) |

---

## Assessment

### Grading Breakdown
- **Session Projects (5 × 10 pts):** 50 points
- **Fraud Detection Capstone:** 100 points
- **Total:** 150 points

### Success Criteria

**Session Projects:**
- Code runs without errors
- Appropriate techniques applied
- Clear visualizations
- Insights and recommendations

**Capstone Project:**
- Isolation Forest & One-Class SVM implemented
- Precision > 50%, Recall > 40%
- Comprehensive comparison to supervised learning
- Decision framework for when to use which approach

---

## Common Pitfalls and How to Avoid Them

### 1. Forgetting to Scale Features
**Problem:** K-Means dominated by features with large ranges
**Solution:** Always use `StandardScaler` before clustering!

### 2. Not Validating Cluster Quality
**Problem:** Accepting any clustering result without evaluation
**Solution:** Use silhouette scores, elbow method, domain expertise

### 3. Over-interpreting Unsupervised Results
**Problem:** Claiming clusters are "truth" when they're patterns
**Solution:** Validate with domain experts, business context

### 4. Using t-SNE for Everything
**Problem:** t-SNE is slow and can't transform new data
**Solution:** Use PCA first, t-SNE only for final visualization

### 5. Expecting Unsupervised = Supervised Performance
**Problem:** Disappointed when anomaly detection gets 50% vs 90%
**Solution:** Understand tradeoffs - unsupervised needs NO labels!

---

## Additional Resources

### Books
- "Pattern Recognition and Machine Learning" - Bishop
- "The Elements of Statistical Learning" - Hastie, Tibshirani, Friedman
- "Hands-On Machine Learning" - Géron (Chapter 9)

### Online Resources
- [scikit-learn Clustering Documentation](https://scikit-learn.org/stable/modules/clustering.html)
- [Visualizing MNIST with PCA and t-SNE](https://colah.github.io/posts/2014-10-Visualizing-MNIST/)
- [Understanding K-Means](https://stanford.edu/~cpiech/cs221/handouts/kmeans.html)

### Papers
- t-SNE: "Visualizing Data using t-SNE" - van der Maaten & Hinton (2008)
- UMAP: "UMAP: Uniform Manifold Approximation and Projection" - McInnes et al. (2018)
- Isolation Forest: "Isolation Forest" - Liu, Ting & Zhou (2008)

---

## FAQ

**Q: Do I always need to scale features for clustering?**
A: For distance-based algorithms (K-Means, DBSCAN), yes! Hierarchical with certain linkages also benefits from scaling.

**Q: How do I choose between K-Means and hierarchical clustering?**
A: K-Means for large datasets and speed. Hierarchical for exploring structure and creating dendrograms. Try both!

**Q: Can unsupervised learning ever outperform supervised?**
A: For pattern discovery and novel anomalies, yes! But for known patterns with labels, supervised usually wins.

**Q: Should I use PCA or t-SNE for visualization?**
A: Use PCA first (fast, preserves global structure). If visualization quality matters most, use t-SNE (slow, beautiful local structure).

**Q: How many clusters should I choose?**
A: Use elbow method and silhouette analysis as guides, but ultimately let business context and domain expertise decide.

**Q: What if my silhouette score is low (~0.3)?**
A: Could indicate overlapping clusters, wrong K, or inappropriate algorithm. Try different methods or accept that data may not have strong natural groupings.

---

## Next Steps

After completing Module 5, you're ready for:

- **Module 6: Neural Networks & Deep Learning** - When traditional ML isn't enough
- **Module 7: Computer Vision** - Apply deep learning to images
- **Module 8: Natural Language Processing** - Work with text data at scale

---

## Support

- **Office Hours:** Check course schedule
- **Discussion Forum:** Post questions and help peers
- **Email:** instructor@example.com
- **GitHub Issues:** Report bugs or improvements

---

## License

Course materials © 2026 ML for Engineers. For educational use only.

---

**Ready to discover hidden patterns? Start with Session 1: Customer Segmentation!**

