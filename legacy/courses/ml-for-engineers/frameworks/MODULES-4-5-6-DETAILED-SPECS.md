# Modules 4, 5, 6: Detailed Production Specifications
## Complete Production-Ready Requirements

**Created:** 2026-01-05
**Purpose:** Detailed specifications for creating production materials
**Detail Level:** Full production specifications (ready for agent execution)
**Status:** Ready for production material creation

---

# TABLE OF CONTENTS

1. [Module 4: Model Evaluation & Optimization](#module-4-model-evaluation--optimization)
2. [Module 5: Unsupervised Learning](#module-5-unsupervised-learning)
3. [Module 6: Neural Networks & Deep Learning](#module-6-neural-networks--deep-learning)
4. [Cross-Module Requirements](#cross-module-requirements)

---

# MODULE 4: Model Evaluation & Optimization

## Module Overview

**Duration:** 1.5 weeks (9-11 hours video + 15-20 hours hands-on)
**Purpose:** Transform good models into production-quality models
**Prerequisites:** Modules 2-3 (classification and regression)
**Theory/Practice Ratio:** 40% / 60%

**The Hook:**
"Your models work... but are they GOOD? Learn to make them 10-20% better!"

**Emotional Arc:**
- Start: "My model gets 75% accuracy... is that good?"
- Middle: "Ah! Cross-validation shows it's actually overfitting!"
- End: "I optimized it to 87% accuracy with confidence it will generalize!"

**Connection to Previous Modules:**
- Uses models from Modules 2-3 as starting point
- Improves stock predictor from Module 3
- Re-evaluates spam detector from Module 2
- Sets foundation for production deployment (Module 9)

---

## Complete Session Breakdown

### Session 1: Classification Metrics Deep Dive (2 hours)

**Learning Objectives:**
1. Calculate and interpret precision, recall, F1-score
2. Choose appropriate metrics for business context
3. Analyze confusion matrices deeply
4. Understand ROC curves and AUC
5. Apply proper metrics to previous projects

**Video Content (60 minutes):**

#### Video 1.1: Beyond Accuracy (12 minutes)
- Why accuracy can be misleading
- Imbalanced class problem example
- Real-world scenario: Fraud detection (99% accuracy but useless)
- The need for more nuanced metrics

#### Video 1.2: Precision vs Recall (15 minutes)
- Precision: "When I predict positive, am I right?"
- Recall: "Did I catch all the positives?"
- The tradeoff
- Business context examples:
  - Spam filter (precision matters - avoid false positives)
  - Disease detection (recall matters - catch all cases)
  - Fraud detection (balance both)

#### Video 1.3: F1-Score and Other Metrics (10 minutes)
- F1 as harmonic mean
- When to use F1
- Weighted F1 for imbalanced classes
- F-beta scores (F2 for recall emphasis)

#### Video 1.4: Confusion Matrix Deep Dive (12 minutes)
- Not just a 2x2 grid
- Reading the matrix systematically
- Identifying patterns of errors
- Multi-class confusion matrices
- Visualizing with heatmaps

#### Video 1.5: ROC Curves and AUC (11 minutes)
- Receiver Operating Characteristic explained
- TPR vs FPR tradeoff
- AUC interpretation (0.5 to 1.0)
- Comparing multiple models
- When AUC is appropriate

**Hands-On Activity (60 minutes):**

**Project: Re-evaluate Module 2 Projects**

Code Requirements:
```python
# Required implementations:
1. Calculate all metrics for spam detector
   - Accuracy, Precision, Recall, F1
   - Confusion matrix
   - ROC curve and AUC

2. Business context analysis
   - Which metric matters most for spam?
   - What threshold should we use?

3. Compare to original evaluation
   - Was our initial assessment correct?
   - Are there hidden problems?

4. Visualization requirements:
   - Confusion matrix heatmap
   - ROC curve with AUC annotation
   - Precision-Recall curve
   - Metrics comparison bar chart
```

**Deliverables:**
- `classification-metrics-deep-dive.ipynb`
- Re-evaluation of spam detector with all metrics
- Business recommendations document

**Success Criteria:**
- All 5 metrics calculated correctly
- Clear visualization of tradeoffs
- Justified metric selection for business context

---

### Session 2: Regression Metrics Deep Dive (2 hours)

**Learning Objectives:**
1. Understand MAE, MSE, RMSE differences
2. Interpret R² correctly
3. Perform residual analysis
4. Identify problematic predictions
5. Choose metrics for regression tasks

**Video Content (60 minutes):**

#### Video 2.1: Regression Metrics Overview (12 minutes)
- MAE (Mean Absolute Error): "Average dollars off"
- MSE (Mean Squared Error): "Penalizes big errors"
- RMSE (Root MSE): "Back to original units"
- When to use each metric

#### Video 2.2: R² Explained Properly (15 minutes)
- NOT "percentage correct"
- Variance explained interpretation
- Negative R² (worse than mean!)
- Adjusted R² for multiple features
- Limitations of R²

#### Video 2.3: Residual Analysis (18 minutes)
- What are residuals?
- Residual plots
- Patterns indicating problems:
  - Heteroscedasticity
  - Non-linearity
  - Outliers
- Q-Q plots for normality

#### Video 2.4: Putting It Together (15 minutes)
- Comprehensive regression evaluation
- Metric combination strategy
- Reporting regression results
- Example: Stock predictor evaluation

**Hands-On Activity (60 minutes):**

**Project: Re-evaluate Module 3 Stock Predictor**

Code Requirements:
```python
# Required implementations:
1. Calculate all regression metrics
   - MAE, MSE, RMSE, R²
   - MAPE (Mean Absolute Percentage Error)

2. Residual analysis
   - Residual plots (actual vs predicted)
   - Residual distribution histogram
   - Q-Q plot
   - Identify outliers

3. Error analysis by stock
   - Which stocks predict well?
   - Which stocks predict poorly?
   - Why the difference?

4. Visualization requirements:
   - Actual vs Predicted scatter
   - Residuals over time
   - Error distribution
   - Metrics comparison table
```

**Deliverables:**
- `regression-metrics-deep-dive.ipynb`
- Complete stock predictor re-evaluation
- Error analysis report

**Success Criteria:**
- All metrics calculated and interpreted
- Residual patterns identified
- Improvement recommendations provided

---

### Session 3: Cross-Validation (2 hours)

**Learning Objectives:**
1. Understand why train/test split isn't enough
2. Implement K-Fold cross-validation
3. Use stratified CV for classification
4. Apply time series CV correctly
5. Interpret CV results properly

**Video Content (60 minutes):**

#### Video 3.1: Why Cross-Validation? (10 minutes)
- Single split = lucky or unlucky?
- The validation problem
- Using data more efficiently
- Getting reliable performance estimates

#### Video 3.2: K-Fold Cross-Validation (15 minutes)
- The folding process
- Training on K-1 folds, testing on 1
- Rotating through all folds
- Averaging results
- Choosing K (typically 5 or 10)

#### Video 3.3: Stratified K-Fold (12 minutes)
- Why stratification matters
- Maintaining class distribution
- Critical for imbalanced data
- Implementation in sklearn

#### Video 3.4: Time Series Cross-Validation (15 minutes)
- Why regular CV fails for time series
- Forward-chaining validation
- Rolling window approach
- Expanding window approach
- Preventing data leakage

#### Video 3.5: Interpreting CV Results (8 minutes)
- Mean and standard deviation
- High variance = unstable model
- Comparing models with CV
- Statistical significance

**Hands-On Activity (60 minutes):**

**Project: Apply CV to Previous Models**

Code Requirements:
```python
# Required implementations:
1. K-Fold CV on spam detector
   - 5-fold cross-validation
   - Report mean ± std for all metrics

2. Stratified K-Fold on churn predictor
   - Handle imbalanced classes
   - Compare to regular K-Fold

3. Time Series CV on stock predictor
   - Forward-chaining validation
   - No data leakage!
   - Compare to random split

4. Visualization requirements:
   - CV scores distribution (box plots)
   - Fold-by-fold performance
   - Comparison of CV strategies
```

**Deliverables:**
- `cross-validation-complete.ipynb`
- CV applied to 3 models
- Performance comparison report

**Success Criteria:**
- CV correctly implemented
- Results show stability (or instability!)
- Data leakage prevented in time series

---

### Session 4: Diagnosing Overfitting & Underfitting (2 hours)

**Learning Objectives:**
1. Recognize overfitting and underfitting
2. Create and interpret learning curves
3. Use validation curves
4. Apply regularization techniques
5. Find the right model complexity

**Video Content (60 minutes):**

#### Video 4.1: Overfitting vs Underfitting (12 minutes)
- High training accuracy, low test accuracy = overfitting
- Low accuracy on both = underfitting
- The Goldilocks zone
- Real examples from previous modules

#### Video 4.2: Learning Curves (18 minutes)
- Training vs validation curves
- Reading the curves:
  - Converging = good
  - Diverging = overfitting
  - Both low = underfitting
- How much data do we need?
- Diminishing returns

#### Video 4.3: Validation Curves (12 minutes)
- Model complexity parameter (e.g., max_depth)
- Finding optimal complexity
- The sweet spot
- Practical examples

#### Video 4.4: Regularization Techniques (18 minutes)
- L1 regularization (Lasso)
- L2 regularization (Ridge)
- Elastic Net (combined)
- When to use which
- Regularization strength (alpha)

**Hands-On Activity (60 minutes):**

**Project: Fix Overfitted Spam Detector**

Code Requirements:
```python
# Required implementations:
1. Generate learning curves
   - Plot training/validation scores
   - Identify overfitting/underfitting

2. Create validation curves
   - Vary model complexity parameter
   - Find optimal complexity

3. Apply regularization
   - Try L1, L2, Elastic Net
   - Compare results

4. Model comparison:
   - Original model (overfitted)
   - Regularized model (improved)
   - Metrics comparison

5. Visualization requirements:
   - Learning curve plots
   - Validation curve plots
   - Before/after comparison
```

**Deliverables:**
- `overfitting-diagnosis-fix.ipynb`
- Fixed spam detector model
- Improvement documentation

**Success Criteria:**
- Overfitting reduced (smaller train/test gap)
- Test accuracy maintained or improved
- Proper regularization applied

---

### Session 5: Hyperparameter Tuning (2 hours)

**Learning Objectives:**
1. Understand hyperparameters vs parameters
2. Implement Grid Search
3. Use Random Search effectively
4. Apply Bayesian Optimization (intro)
5. Combine CV with tuning

**Video Content (60 minutes):**

#### Video 5.1: Hyperparameters Explained (10 minutes)
- Parameters: Learned from data (weights)
- Hyperparameters: Set by us (learning rate, depth, etc.)
- Impact on model performance
- The tuning challenge

#### Video 5.2: Grid Search (15 minutes)
- Exhaustive search over grid
- Example: max_depth × min_samples_split
- Exponential growth problem
- When to use grid search

#### Video 5.3: Random Search (12 minutes)
- Random sampling from distributions
- More efficient than grid search
- Better coverage
- Practical advantages

#### Video 5.4: Bayesian Optimization Intro (13 minutes)
- Smarter search using previous results
- Probabilistic model of objective
- Exploration vs exploitation
- Libraries: Optuna, Hyperopt

#### Video 5.5: Best Practices (10 minutes)
- Always use CV with tuning
- Avoid overfitting to validation set
- Computational cost considerations
- Nested CV (advanced)

**Hands-On Activity (60 minutes):**

**Project: Optimize Stock Predictor Hyperparameters**

Code Requirements:
```python
# Required implementations:
1. Grid Search on Random Forest
   - n_estimators: [50, 100, 200]
   - max_depth: [10, 20, 30, None]
   - min_samples_split: [2, 5, 10]
   - With 5-fold CV

2. Random Search comparison
   - Same parameter space
   - 30 iterations
   - Compare results to grid search

3. Bayesian Optimization (optional)
   - Using Optuna
   - 50 trials
   - Best parameters

4. Results comparison:
   - Original model performance
   - Grid search best model
   - Random search best model
   - Improvement percentage

5. Visualization requirements:
   - Hyperparameter importance
   - Optimization history
   - Performance comparison
```

**Deliverables:**
- `hyperparameter-tuning-stock.ipynb`
- Optimized stock predictor model
- Performance improvement report (target: 10%+ improvement)

**Success Criteria:**
- Model performance improved by 10%+
- Optimal hyperparameters found
- Clear documentation of search process

---

### Session 6: Feature Selection & Model Comparison (2 hours + Capstone)

**Learning Objectives:**
1. Understand feature importance
2. Perform feature selection
3. Use Recursive Feature Elimination
4. Build systematic model comparison framework
5. Apply all techniques to fraud detection

**Video Content (60 minutes):**

#### Video 6.1: Feature Importance (12 minutes)
- Tree-based feature importance
- Permutation importance
- SHAP values (brief intro)
- Interpreting importance

#### Video 6.2: Feature Selection Methods (15 minutes)
- Filter methods (correlation, mutual info)
- Wrapper methods (RFE)
- Embedded methods (Lasso)
- When to use each

#### Video 6.3: Recursive Feature Elimination (12 minutes)
- RFE algorithm
- Starting with all features
- Removing least important
- Finding optimal subset

#### Video 6.4: Model Selection Framework (11 minutes)
- Comparing multiple models systematically
- Cross-validation + metrics
- Statistical testing
- Confidence in selection

#### Video 6.5: Capstone Introduction (10 minutes)
- Fraud Detection System overview
- Dataset introduction
- Business requirements
- Success criteria

**Hands-On Activity (60 minutes):**

**Project: Feature Selection Lab**

Code Requirements:
```python
# Required implementations:
1. Feature importance analysis
   - Calculate importance for all features
   - Visualize top 20 features
   - Remove low-importance features

2. Recursive Feature Elimination
   - Start with all features
   - Find optimal subset
   - Compare to full model

3. Correlation analysis
   - Remove highly correlated features
   - Impact on performance

4. Model comparison:
   - Full features vs selected features
   - Performance and speed comparison
```

**Capstone Project (2-3 hours):**

**Fraud Detection System (Finance)**

Dataset Requirements:
- Credit card transactions dataset
- ~284,807 transactions
- 30 features (V1-V28 PCA, Amount, Time)
- Highly imbalanced (0.172% fraud)
- Source: Kaggle Credit Card Fraud Detection

Code Requirements:
```python
# Complete fraud detection system:
1. Exploratory Data Analysis
   - Class distribution
   - Feature distributions
   - Correlation analysis

2. Data Preparation
   - Handle imbalance (SMOTE or class weights)
   - Feature scaling
   - Time-aware splitting

3. Model Training
   - Try multiple algorithms:
     - Logistic Regression
     - Random Forest
     - Gradient Boosting
     - XGBoost

4. Evaluation (ALL techniques from Module 4)
   - Precision, Recall, F1 (precision critical!)
   - Confusion matrix
   - ROC curve and AUC
   - Cross-validation (time-aware!)
   - Learning curves

5. Optimization
   - Hyperparameter tuning
   - Feature selection
   - Threshold optimization (for high precision)

6. Final Model
   - Best model selection
   - Performance metrics
   - Business recommendations
   - Deployment considerations

7. Visualization requirements:
   - Class distribution
   - Feature importance
   - ROC curve
   - Precision-Recall curve
   - Confusion matrix
   - Learning curves
   - Results comparison table
```

**Deliverables:**
- `fraud-detection-system.ipynb` (complete end-to-end)
- `fraud-detection-report.md` (business recommendations)
- Trained model file (fraud_detector_model.pkl)

**Success Criteria:**
- Precision > 90% (minimize false positives)
- Recall > 70% (catch most fraud)
- AUC > 0.95
- Proper handling of imbalanced data
- All Module 4 techniques applied

---

## Module 4: Complete Dataset Requirements

### Dataset 1: Previous Module Models (Reuse)
- Spam detector from Module 2
- Churn predictor from Module 2
- Stock predictor from Module 3
- **No new download needed**

### Dataset 2: Credit Card Fraud Detection
- **Source:** Kaggle (https://www.kaggle.com/mlg-ulb/creditcardfraud)
- **Alternative:** synthetic fraud data generator script
- **Size:** ~150 MB
- **Samples:** 284,807 transactions
- **Features:** 30 (Time, Amount, V1-V28 from PCA)
- **Target:** Class (0 = normal, 1 = fraud)
- **Imbalance:** 0.172% fraud (492 frauds out of 284,807)

Download Script Required:
```python
# download_fraud_data.py
import pandas as pd
from sklearn.datasets import make_classification

# Option 1: Kaggle download (requires API key)
# Option 2: Generate synthetic data
def generate_synthetic_fraud_data():
    X, y = make_classification(
        n_samples=285000,
        n_features=30,
        n_informative=15,
        n_redundant=10,
        n_classes=2,
        weights=[0.998, 0.002],
        random_state=42
    )
    # Save as CSV
```

---

## Module 4: Complete Assessment Requirements

### Quizzes (6 total, ~50 questions)

**Session 1 Quiz (8-10 questions):**
- Precision vs Recall scenarios
- Confusion matrix interpretation
- ROC curve questions
- Metric selection for business context

**Session 2 Quiz (8-10 questions):**
- MAE, MSE, RMSE calculations
- R² interpretation
- Residual analysis
- Regression metric selection

**Session 3 Quiz (8-10 questions):**
- K-Fold CV process
- Stratified vs regular CV
- Time series CV
- Interpreting CV results

**Session 4 Quiz (8-10 questions):**
- Overfitting identification
- Learning curve interpretation
- Regularization techniques
- Model complexity

**Session 5 Quiz (8-10 questions):**
- Hyperparameters vs parameters
- Grid search vs random search
- Bayesian optimization
- Best practices

**Session 6 Quiz (8-10 questions):**
- Feature importance
- Feature selection methods
- RFE algorithm
- Model selection

### Project Rubrics

**Session Projects (5 × 10 points = 50 points):**
- Correct implementation (40%)
- Proper metrics calculated (30%)
- Visualizations (20%)
- Documentation (10%)

**Fraud Detection Capstone (100 points):**
- EDA and data preparation (15 points)
- Multiple models trained (20 points)
- All evaluation techniques applied (25 points)
- Optimization performed (20 points)
- Business recommendations (10 points)
- Code quality and documentation (10 points)

---

## Module 4: Visual Assets Needed

1. **Precision vs Recall Trade-off Diagram**
2. **Confusion Matrix Anatomy**
3. **ROC Curve Explained**
4. **Learning Curves Examples** (good vs overfitting vs underfitting)
5. **Cross-Validation Process Diagram**
6. **Grid Search Visualization**
7. **Feature Importance Bar Charts**
8. **Module 4 Workflow Diagram**

---

## Module 4: Success Metrics

**By end of module, learners should:**
- ✅ Calculate and interpret all major metrics
- ✅ Properly implement cross-validation
- ✅ Diagnose and fix overfitting
- ✅ Optimize hyperparameters systematically
- ✅ Select features effectively
- ✅ Improve previous models by 10%+
- ✅ Build production-quality fraud detector

---

# MODULE 5: Unsupervised Learning

## Module Overview

**Duration:** 2 weeks (12-14 hours video + 20-25 hours hands-on)
**Purpose:** Discover patterns without labels
**Prerequisites:** Modules 2-4 (supervised learning foundation)
**Theory/Practice Ratio:** 35% / 65%

**The Hook:**
"What if you DON'T have labels? Find hidden patterns in your data!"

**Emotional Arc:**
- Start: "All we've done needs labels... what if we don't have them?"
- Middle: "Whoa! The algorithm found 4 customer segments I never knew existed!"
- End: "I can find insights WITHOUT expensive labeling!"

**Connection to Previous Modules:**
- Contrast to supervised learning (Modules 2-3)
- Uses evaluation techniques from Module 4
- Sets up neural networks (Module 6)
- Complements fraud detection (supervised vs unsupervised)

---

## Complete Session Breakdown

### Session 1: K-Means Clustering (2 hours)

**Learning Objectives:**
1. Understand clustering concept
2. Implement K-Means algorithm
3. Choose optimal K (elbow method, silhouette)
4. Interpret clustering results
5. Apply to customer segmentation

**Video Content (60 minutes):**

#### Video 1.1: Introduction to Clustering (12 minutes)
- What is clustering?
- Supervised vs unsupervised contrast
- Real-world applications
- When to use clustering

#### Video 1.2: K-Means Algorithm (18 minutes)
- The algorithm:
  1. Initialize K centroids randomly
  2. Assign points to nearest centroid
  3. Update centroids
  4. Repeat until convergence
- Visualization of iterations
- Strengths and limitations

#### Video 1.3: Choosing K (15 minutes)
- The K selection problem
- Elbow method
- Silhouette score
- Gap statistic (brief)
- Practical considerations

#### Video 1.4: Interpreting Clusters (15 minutes)
- Cluster profiling
- Feature means by cluster
- Visualization techniques
- Naming/labeling clusters

**Hands-On Activity (60 minutes):**

**Project: Customer Segmentation (E-commerce)**

Dataset Requirements:
- E-commerce customer data
- ~2,000 customers
- Features: Recency, Frequency, Monetary value, Age, Web visits
- Source: Synthetic or UCI/Kaggle

Code Requirements:
```python
# Required implementations:
1. Data Preparation
   - Feature scaling (critical for K-Means!)
   - Handle missing values

2. Optimal K Selection
   - Elbow method (plot inertia)
   - Silhouette scores (K=2 to 10)
   - Select optimal K

3. K-Means Clustering
   - Fit model with optimal K
   - Assign cluster labels

4. Cluster Analysis
   - Profile each cluster:
     - Mean values for all features
     - Cluster sizes
     - Characteristics
   - Name clusters (e.g., "High-value frequent buyers")

5. Business Recommendations
   - Marketing strategy per segment
   - Targeted campaigns
   - Resource allocation

6. Visualization requirements:
   - Elbow curve
   - Silhouette plot
   - 2D cluster visualization (PCA if needed)
   - Cluster profiles (radar charts)
   - Feature distributions by cluster
```

**Deliverables:**
- `customer-segmentation-kmeans.ipynb`
- `customer-segments-report.md` (business insights)
- Cluster profiles summary

**Success Criteria:**
- 4-5 distinct customer segments identified
- Clear differentiation between segments
- Actionable business recommendations

---

### Session 2: Hierarchical & DBSCAN Clustering (2 hours)

**Learning Objectives:**
1. Understand hierarchical clustering
2. Read and interpret dendrograms
3. Implement DBSCAN
4. Choose between clustering algorithms
5. Apply to healthcare patient grouping

**Video Content (60 minutes):**

#### Video 2.1: Hierarchical Clustering (18 minutes)
- Agglomerative (bottom-up) approach
- Linkage methods:
  - Single linkage
  - Complete linkage
  - Average linkage
  - Ward's method
- Dendrograms explained
- Cutting the dendrogram

#### Video 2.2: DBSCAN (18 minutes)
- Density-based clustering
- Core points, border points, noise
- Parameters: eps (radius), min_samples
- Advantages:
  - Finds arbitrary shapes
  - Identifies outliers
  - No need to specify K
- Parameter tuning

#### Video 2.3: Comparing Clustering Methods (14 minutes)
- K-Means vs Hierarchical vs DBSCAN
- When to use which:
  - K-Means: Fast, spherical clusters, known K
  - Hierarchical: Small datasets, dendrograms useful
  - DBSCAN: Arbitrary shapes, outlier detection
- Practical decision framework

#### Video 2.4: Clustering Evaluation (10 minutes)
- Internal metrics (silhouette, Davies-Bouldin)
- External metrics (if labels available)
- Stability assessment
- Domain expert validation

**Hands-On Activity (60 minutes):**

**Project: Patient Grouping (Healthcare)**

Dataset Requirements:
- Patient medical data
- ~500-1000 patients
- Features: Age, BMI, Blood pressure, Glucose, various symptoms
- Source: Diabetes/Health dataset from UCI or synthetic

Code Requirements:
```python
# Required implementations:
1. Hierarchical Clustering
   - Try different linkage methods
   - Generate dendrogram
   - Choose optimal cut
   - Analyze patient groups

2. DBSCAN Clustering
   - Tune eps and min_samples
   - Identify patient clusters
   - Find outlier patients (important!)

3. Method Comparison
   - K-Means from Session 1
   - Hierarchical
   - DBSCAN
   - Compare results (silhouette scores)
   - Which method is best for this data?

4. Clinical Insights
   - Profile each patient group
   - Common characteristics
   - Treatment recommendations per group
   - Flag high-risk patients (outliers)

5. Visualization requirements:
   - Dendrogram (hierarchical)
   - DBSCAN cluster visualization
   - Method comparison table
   - Patient profiles by cluster
```

**Deliverables:**
- `patient-clustering-comparison.ipynb`
- `patient-groups-clinical-report.md`
- Treatment recommendations per group

**Success Criteria:**
- 3+ patient groups identified
- Outliers flagged appropriately
- Clear differentiation in health profiles
- Clinical recommendations provided

---

### Session 3: Real-World Clustering Applications (2 hours)

**Learning Objectives:**
1. Apply clustering to text data
2. Cluster images
3. Use clustering for recommendation
4. Validate clustering results
5. Present clustering insights

**Video Content (60 minutes):**

#### Video 3.1: Document Clustering (15 minutes)
- Text vectorization (TF-IDF)
- Clustering documents
- Topic discovery
- Applications: News, research papers, customer feedback

#### Video 3.2: Image Clustering (12 minutes)
- Feature extraction from images
- Color-based clustering
- Deep features (CNN embeddings)
- Applications: Photo organization, similar image search

#### Video 3.3: Clustering for Recommendations (15 minutes)
- Item-based clustering
- User-based clustering
- Collaborative filtering connection
- Cold start problem

#### Video 3.4: Validating and Presenting Clusters (18 minutes)
- Domain expert validation
- A/B testing with clusters
- Visualization best practices
- Storytelling with clusters
- Common pitfalls

**Hands-On Activity (60 minutes):**

**Project: News Article Clustering**

Dataset Requirements:
- News articles dataset
- ~1,000-2,000 articles
- Multiple categories (Sports, Politics, Tech, Business, etc.)
- Source: BBC News, 20 Newsgroups, or Kaggle

Code Requirements:
```python
# Required implementations:
1. Text Preprocessing
   - Tokenization
   - Stop word removal
   - Lemmatization
   - TF-IDF vectorization

2. Clustering
   - K-Means on TF-IDF vectors
   - Optimal K selection
   - Cluster assignment

3. Topic Discovery
   - Top keywords per cluster
   - Cluster naming
   - Compare to actual categories

4. Evaluation
   - If labels available: compare to actual categories
   - Purity, completeness, V-measure
   - Qualitative assessment

5. Insights
   - Did clustering find meaningful topics?
   - Any surprising groupings?
   - Practical applications

6. Visualization requirements:
   - Word clouds per cluster
   - t-SNE visualization of documents
   - Top terms per cluster (bar charts)
   - Confusion with actual categories
```

**Deliverables:**
- `news-clustering-unsupervised.ipynb`
- Topic discovery report
- Comparison to supervised categories

**Success Criteria:**
- Clusters align with topics (even without labels)
- Clear topic differentiation
- Meaningful insights discovered

---

### Session 4: PCA - Principal Component Analysis (2 hours)

**Learning Objectives:**
1. Understand dimensionality curse
2. Implement PCA
3. Interpret explained variance
4. Use PCA for visualization
5. Apply PCA before clustering

**Video Content (60 minutes):**

#### Video 4.1: The Curse of Dimensionality (12 minutes)
- Why many features = problem
- Sparsity in high dimensions
- Computational complexity
- Visualization impossibility
- Feature correlation

#### Video 4.2: PCA Intuition (18 minutes)
- Finding directions of maximum variance
- Principal components
- Orthogonality
- Dimensionality reduction
- Information preservation

#### Video 4.3: PCA Implementation (15 minutes)
- Standardization (critical!)
- sklearn PCA
- Choosing number of components
- Explained variance ratio
- Cumulative explained variance

#### Video 4.4: PCA Applications (15 minutes)
- Visualization (50D → 2D)
- Noise reduction
- Feature extraction
- Speed up algorithms
- Preprocessing for clustering

**Hands-On Activity (60 minutes):**

**Project: High-Dimensional Data Visualization**

Dataset Requirements:
- High-dimensional dataset (50+ features)
- Options:
  - MNIST (784 features)
  - Gene expression data
  - Financial indicators
  - Customer behavior with many features
- Source: UCI, Kaggle, or sklearn datasets

Code Requirements:
```python
# Required implementations:
1. Data Preparation
   - Load high-dimensional data
   - Standardization (critical for PCA!)
   - Check for missing values

2. PCA Analysis
   - Fit PCA on all features
   - Plot explained variance
   - Cumulative explained variance
   - Choose number of components (e.g., 95% variance)

3. Dimensionality Reduction
   - Reduce to 2D for visualization
   - Reduce to 3D for interactive plots
   - Reduce to optimal dimensions for clustering

4. Visualization
   - 2D scatter plot of first 2 PCs
   - 3D interactive plot
   - Color by known labels (if available)
   - Identify patterns

5. Applications
   - Apply clustering on reduced dimensions
   - Compare to clustering on full dimensions
   - Speed and performance comparison

6. Visualization requirements:
   - Explained variance plot
   - Cumulative variance plot
   - 2D PCA scatter (colored)
   - 3D PCA interactive plot
   - Comparison before/after PCA
```

**Deliverables:**
- `pca-dimensionality-reduction.ipynb`
- Visualization gallery
- PCA insights report

**Success Criteria:**
- Successfully reduced dimensions (e.g., 784 → 50 → 2)
- Retained 90%+ explained variance
- Clear visualization of patterns
- Speed improvements demonstrated

---

### Session 5: t-SNE & Advanced Visualization (2 hours)

**Learning Objectives:**
1. Understand t-SNE differences from PCA
2. Implement t-SNE effectively
3. Tune perplexity parameter
4. Compare PCA vs t-SNE
5. Visualize complex patterns

**Video Content (60 minutes):**

#### Video 5.1: Introduction to t-SNE (15 minutes)
- t-Distributed Stochastic Neighbor Embedding
- Preserves local structure
- Non-linear dimensionality reduction
- Differences from PCA:
  - PCA: Linear, preserves global structure
  - t-SNE: Non-linear, preserves local structure

#### Video 5.2: t-SNE Implementation (18 minutes)
- Perplexity parameter (5-50)
- Learning rate
- Number of iterations
- Computational cost (slow!)
- Reproducibility (random initialization)

#### Video 5.3: When PCA vs t-SNE (12 minutes)
- PCA:
  - Fast
  - Interpretable components
  - Global structure
  - Can transform new data
- t-SNE:
  - Better visualization
  - Local structure
  - Slower
  - Cannot transform new data easily

#### Video 5.4: UMAP (Brief Introduction) (15 minutes)
- Uniform Manifold Approximation and Projection
- Faster than t-SNE
- Preserves both local and global structure
- Growing popularity
- Quick demo

**Hands-On Activity (60 minutes):**

**Project: Iris Revisited with Dimensionality Reduction**

Dataset Requirements:
- Iris dataset (Module 2 callback!)
- MNIST subset (for comparison)
- Fashion MNIST subset

Code Requirements:
```python
# Required implementations:
1. PCA on Iris
   - Reduce 4D → 2D
   - Visualize with species colors
   - How well are species separated?

2. t-SNE on Iris
   - Reduce 4D → 2D
   - Try different perplexities (5, 15, 30, 50)
   - Compare to PCA

3. Comparison on MNIST
   - PCA visualization (784 → 2D)
   - t-SNE visualization (784 → 2D)
   - Which shows digit clusters better?

4. Visualization Gallery
   - Side-by-side PCA vs t-SNE
   - Different perplexity effects
   - Interactive plots

5. Insights
   - When did PCA work well?
   - When did t-SNE shine?
   - Computational time comparison
   - Best practices guide

6. Visualization requirements:
   - Iris: PCA vs t-SNE (side by side)
   - MNIST: PCA vs t-SNE comparison
   - Perplexity comparison (multiple plots)
   - Computation time bar chart
```

**Deliverables:**
- `tsne-advanced-visualization.ipynb`
- Visualization comparison gallery
- PCA vs t-SNE decision guide

**Success Criteria:**
- Clear understanding of PCA vs t-SNE tradeoffs
- Effective visualizations created
- Appropriate algorithm chosen for context

---

### Session 6: Anomaly Detection (2 hours + Capstone)

**Learning Objectives:**
1. Understand anomaly detection concept
2. Implement Isolation Forest
3. Use One-Class SVM
4. Apply statistical methods
5. Compare to supervised fraud detection

**Video Content (60 minutes):**

#### Video 6.1: Introduction to Anomaly Detection (12 minutes)
- What are anomalies/outliers?
- Supervised vs unsupervised anomaly detection
- Applications:
  - Fraud detection
  - Quality control
  - Network intrusion
  - Health monitoring

#### Video 6.2: Isolation Forest (18 minutes)
- How it works:
  - Anomalies are "easy to isolate"
  - Random partitioning
  - Shorter paths = anomalies
- Parameters: contamination, n_estimators
- Advantages: Fast, effective

#### Video 6.3: One-Class SVM (12 minutes)
- Learning the "normal" region
- Kernel trick
- Parameters: nu, gamma
- When to use vs Isolation Forest

#### Video 6.4: Statistical Methods (10 minutes)
- Z-score method
- IQR (Interquartile Range)
- Elliptic Envelope (Gaussian assumption)
- Simple but effective

#### Video 6.5: Capstone Introduction (8 minutes)
- Fraud detection revisited
- Supervised (Module 4) vs Unsupervised (now)
- Real-world scenario: No fraud labels
- Performance comparison

**Hands-On Activity (60 minutes):**

**Project: Anomaly Detection Methods Comparison**

Code Requirements:
```python
# Required implementations:
1. Isolation Forest
   - Fit on normal transactions
   - Detect anomalies
   - Tune contamination parameter

2. One-Class SVM
   - Train on normal data
   - Detect outliers
   - Compare to Isolation Forest

3. Statistical Methods
   - Z-score approach
   - IQR method
   - Elliptic Envelope

4. Method Comparison
   - Which found most fraud?
   - False positive rates
   - Computational speed
   - Ease of use

5. Visualization requirements:
   - Anomaly scores distribution
   - Detected vs actual fraud (if labels available)
   - Method comparison table
   - ROC curves (if labels available)
```

**Capstone Project (2-3 hours):**

**Credit Card Fraud Detection (Unsupervised Approach)**

Dataset Requirements:
- Same fraud dataset from Module 4
- BUT: Pretend we don't have fraud labels!
- Use only for final evaluation

Code Requirements:
```python
# Complete unsupervised fraud detection:
1. Data Preparation
   - Feature scaling
   - No stratification (we're unsupervised!)

2. Anomaly Detection
   - Isolation Forest (main approach)
   - Tune contamination to match real fraud rate (~0.2%)
   - Detect anomalies

3. Clustering + Anomaly
   - Cluster transactions
   - Find anomalies within clusters
   - Two-level approach

4. Evaluation (using held-out labels)
   - Precision, Recall for "anomalies" = fraud
   - Compare to Module 4 supervised approach
   - ROC curve and AUC

5. Hybrid Approach
   - Unsupervised to find candidates
   - Manual review simulation
   - Cost-benefit analysis

6. Comparison Report
   - Supervised (Module 4) vs Unsupervised (Module 5)
   - Pros/cons of each
   - When to use which
   - Real-world recommendations

7. Visualization requirements:
   - Anomaly scores distribution
   - Confusion matrix (anomalies vs actual fraud)
   - ROC curve comparison
   - Cost-benefit analysis chart
   - Method comparison table
```

**Deliverables:**
- `fraud-detection-unsupervised.ipynb`
- `supervised-vs-unsupervised-comparison.md`
- Decision framework document

**Success Criteria:**
- Anomaly detection Precision > 50%
- Anomaly detection Recall > 40%
- Clear understanding of supervised vs unsupervised tradeoffs
- Real-world applicability demonstrated

---

## Module 5: Complete Dataset Requirements

### Dataset 1: E-commerce Customer Data
- **Source:** UCI Online Retail or synthetic
- **Samples:** ~2,000 customers
- **Features:** RFM (Recency, Frequency, Monetary), Age, Web visits, etc.
- **Format:** CSV

### Dataset 2: Patient/Healthcare Data
- **Source:** UCI Diabetes, Heart Disease, or synthetic
- **Samples:** 500-1,000 patients
- **Features:** Demographics, vitals, symptoms, lab results
- **Format:** CSV

### Dataset 3: News Articles Dataset
- **Source:** BBC News, 20 Newsgroups, or Kaggle
- **Samples:** 1,000-2,000 articles
- **Features:** Text content, categories (for validation)
- **Format:** CSV or JSON

### Dataset 4: High-Dimensional Data
- **Source:** MNIST (sklearn), gene expression, or financial
- **Features:** 50-784 dimensions
- **Format:** Built-in or CSV

### Dataset 5: Credit Card Fraud (Reuse from Module 4)
- **Source:** Module 4 dataset
- **Use:** Unsupervised anomaly detection

Download Script Required:
```python
# download_unsupervised_datasets.py
# Automated download for all Module 5 datasets
```

---

## Module 5: Complete Assessment Requirements

### Quizzes (6 total, ~50 questions)

**Session 1 Quiz (8-10 questions):**
- Clustering concept
- K-Means algorithm steps
- Elbow method
- Silhouette scores
- Applications

**Session 2 Quiz (8-10 questions):**
- Hierarchical clustering
- Dendrogram interpretation
- DBSCAN parameters
- Method comparison
- When to use which

**Session 3 Quiz (8-10 questions):**
- Document clustering
- Image clustering
- Validation methods
- Real-world applications

**Session 4 Quiz (8-10 questions):**
- Dimensionality curse
- PCA concept
- Explained variance
- Component interpretation
- Applications

**Session 5 Quiz (8-10 questions):**
- t-SNE vs PCA
- Perplexity parameter
- Visualization best practices
- UMAP overview

**Session 6 Quiz (8-10 questions):**
- Anomaly detection concept
- Isolation Forest
- One-Class SVM
- Statistical methods
- Applications

### Project Rubrics

**Session Projects (5 × 10 points = 50 points):**
- Correct implementation (40%)
- Proper evaluation (30%)
- Visualizations (20%)
- Insights/recommendations (10%)

**Fraud Detection Capstone (100 points):**
- Implementation correctness (25 points)
- Multiple methods comparison (20 points)
- Evaluation vs ground truth (20 points)
- Supervised vs unsupervised comparison (20 points)
- Recommendations and insights (15 points)

---

## Module 5: Visual Assets Needed

1. **Supervised vs Unsupervised Comparison**
2. **K-Means Algorithm Animation**
3. **Elbow Method Example**
4. **Hierarchical Clustering Dendrogram**
5. **DBSCAN Concept Diagram**
6. **PCA Explained Variance Plot**
7. **t-SNE vs PCA Comparison**
8. **Anomaly Detection Concept**
9. **Module 5 Workflow Diagram**

---

## Module 5: Success Metrics

**By end of module, learners should:**
- ✅ Implement and compare 3+ clustering algorithms
- ✅ Segment customers meaningfully
- ✅ Reduce dimensions effectively (PCA, t-SNE)
- ✅ Detect anomalies without labels
- ✅ Understand supervised vs unsupervised tradeoffs
- ✅ Apply unsupervised learning to real problems

---

# MODULE 6: Neural Networks & Deep Learning

## Module Overview

**Duration:** 2 weeks (14-16 hours video + 25-30 hours hands-on)
**Purpose:** Introduction to deep learning and neural networks
**Prerequisites:** Modules 2-5 (strong ML foundation)
**Theory/Practice Ratio:** 40% / 60%

**The Hook:**
"Traditional ML is great... but neural networks can learn MORE complex patterns!"

**Emotional Arc:**
- Start: "I've been doing well with sklearn... why learn something harder?"
- Middle: "Whoa! This network just learned to recognize handwritten digits at 98%!"
- End: "I can build deep learning models AND know when to use them vs traditional ML!"

**Connection to Previous Modules:**
- Builds on supervised learning (Modules 2-3)
- More complex than traditional ML
- Foundation for CV (Module 7) and NLP (Module 8)
- Callback to stock prediction (Module 3)

---

## Complete Session Breakdown

### Session 1: Introduction to Neural Networks (2 hours)

**Learning Objectives:**
1. Understand what neural networks are
2. Learn neurons, layers, and connections
3. Grasp forward propagation concept
4. Compare to traditional ML
5. Build first neural network

**Video Content (60 minutes):**

#### Video 1.1: What Are Neural Networks? (15 minutes)
- Biological inspiration (brief!)
- Artificial neurons
- Layers: Input, Hidden, Output
- Why "deep" learning?
- Historical context (AI winters, recent success)

#### Video 1.2: The Neuron (12 minutes)
- Inputs × Weights
- Sum
- Bias
- Activation function
- Output
- Mathematical notation

#### Video 1.3: Forward Propagation (18 minutes)
- Layer-by-layer computation
- Matrix operations
- Example walkthrough (3-layer network)
- Vectorization benefits

#### Video 1.4: NN vs Traditional ML (15 minutes)
- When to use neural networks:
  - Very large datasets
  - Unstructured data (images, text, audio)
  - Complex patterns
- When NOT to use:
  - Small datasets
  - Interpretability critical
  - Computational constraints
- Comparison table

**Hands-On Activity (60 minutes):**

**Project: Simple NN for Iris (compare to Module 2)**

Code Requirements:
```python
# Required implementations:
1. Load Iris Dataset
   - Same as Module 2
   - Prepare for neural network

2. Build Simple Neural Network
   - Input layer: 4 features
   - Hidden layer: 8 neurons, ReLU activation
   - Output layer: 3 classes, Softmax activation
   - Use Keras Sequential API

3. Compile Model
   - Loss: categorical_crossentropy
   - Optimizer: adam
   - Metrics: accuracy

4. Train Model
   - Fit for 100 epochs
   - Validation split
   - Monitor training

5. Evaluate
   - Test accuracy
   - Confusion matrix
   - Compare to Decision Tree (Module 2)

6. Insights
   - Is NN better than Decision Tree?
   - Why or why not?
   - Trade-offs (training time, interpretability)

7. Visualization requirements:
   - Training/validation accuracy curves
   - Training/validation loss curves
   - Confusion matrix
   - Comparison table (NN vs Decision Tree)
```

**Deliverables:**
- `iris-neural-network.ipynb`
- Comparison to Module 2 results
- When-to-use-NN guide (start)

**Success Criteria:**
- NN achieves 95%+ accuracy
- Clear understanding of NN structure
- Thoughtful comparison to traditional ML

---

### Session 2: Building with Keras (2 hours)

**Learning Objectives:**
1. Master Keras Sequential API
2. Understand Dense layers
3. Use activation functions correctly
4. Compile models properly
5. Build MNIST digit recognizer

**Video Content (60 minutes):**

#### Video 2.1: Keras Overview (10 minutes)
- High-level API for TensorFlow
- Sequential vs Functional API
- Model building workflow
- Why Keras is beginner-friendly

#### Video 2.2: Dense Layers (15 minutes)
- Fully connected layers
- Parameters: units, activation
- Input shape specification
- Stacking layers

#### Video 2.3: Activation Functions (20 minutes)
- ReLU (Rectified Linear Unit):
  - Most common in hidden layers
  - Solves vanishing gradient
- Sigmoid:
  - Binary classification output
  - Outputs 0-1
- Softmax:
  - Multi-class classification
  - Probability distribution
- Tanh (brief mention)
- When to use which

#### Video 2.4: Compiling Models (15 minutes)
- Loss functions:
  - binary_crossentropy
  - categorical_crossentropy
  - mse (for regression)
- Optimizers:
  - SGD
  - Adam (recommended)
  - RMSprop
- Metrics (accuracy, etc.)

**Hands-On Activity (60 minutes):**

**Project: MNIST Digit Recognition**

Dataset Requirements:
- MNIST handwritten digits
- 60,000 training images
- 10,000 test images
- 28×28 grayscale images
- Built into Keras

Code Requirements:
```python
# Required implementations:
1. Load and Prepare MNIST
   - Load from keras.datasets
   - Normalize pixels (0-255 → 0-1)
   - Flatten images (28×28 → 784)
   - One-hot encode labels

2. Build Neural Network
   - Input: 784 neurons
   - Hidden 1: 128 neurons, ReLU
   - Hidden 2: 64 neurons, ReLU
   - Output: 10 neurons, Softmax

3. Compile
   - Loss: categorical_crossentropy
   - Optimizer: adam
   - Metrics: accuracy

4. Train
   - Epochs: 10
   - Batch size: 128
   - Validation split: 20%
   - Monitor progress

5. Evaluate
   - Test accuracy (target: >95%)
   - Confusion matrix (10×10)
   - Find misclassified examples

6. Visualize
   - Sample predictions with images
   - Most confident correct predictions
   - Most confident wrong predictions
   - Learning curves

7. Visualization requirements:
   - Sample MNIST digits (grid)
   - Training history (accuracy + loss)
   - Confusion matrix (heatmap)
   - Misclassified examples (with predictions)
```

**Deliverables:**
- `mnist-digit-recognition.ipynb`
- Trained model saved (`mnist_model.h5`)
- Misclassification analysis

**Success Criteria:**
- Test accuracy > 95%
- Understand each layer's role
- Can build similar networks independently

---

### Session 3: Training Neural Networks (2 hours)

**Learning Objectives:**
1. Understand loss functions deeply
2. Choose optimizers appropriately
3. Set batch size and epochs
4. Monitor training effectively
5. Use early stopping

**Video Content (60 minutes):**

#### Video 3.1: Loss Functions Deep Dive (18 minutes)
- What is a loss function?
- Binary crossentropy (binary classification)
- Categorical crossentropy (multi-class)
- MSE (regression)
- MAE (regression, robust to outliers)
- Choosing the right loss

#### Video 3.2: Optimizers Explained (18 minutes)
- Gradient Descent concept
- SGD (Stochastic Gradient Descent)
- Mini-batch gradient descent
- Adam (Adaptive Moment Estimation):
  - Combines momentum + adaptive learning rate
  - Best default choice
- Learning rate importance
- Optimizer comparison

#### Video 3.3: Training Dynamics (14 minutes)
- Epochs: Full pass through dataset
- Batch size: Trade-offs
  - Small batch: Noisy gradients, slower
  - Large batch: Stable gradients, memory-intensive
- Typical values: 32, 64, 128
- Training time considerations

#### Video 3.4: Early Stopping & Callbacks (10 minutes)
- Overfitting during training
- Early stopping:
  - Monitor validation loss
  - Stop when no improvement
  - Restore best weights
- Other callbacks:
  - ModelCheckpoint
  - ReduceLROnPlateau
  - TensorBoard

**Hands-On Activity (60 minutes):**

**Project: Fashion MNIST Classification**

Dataset Requirements:
- Fashion MNIST
- 60,000 training images
- 10,000 test images
- 28×28 grayscale images
- 10 classes (T-shirt, Trouser, Pullover, Dress, Coat, Sandal, Shirt, Sneaker, Bag, Ankle boot)
- Built into Keras

Code Requirements:
```python
# Required implementations:
1. Load Fashion MNIST
   - Load from keras.datasets
   - Normalize
   - Flatten or keep as 28×28

2. Build Neural Network
   - Experiment with architecture
   - 2-3 hidden layers
   - Try different units (64, 128, 256)

3. Training Experiments
   - Experiment 1: Vary batch size (32, 64, 128, 256)
   - Experiment 2: Vary learning rate (0.001, 0.01, 0.1)
   - Experiment 3: Different optimizers (SGD, Adam, RMSprop)
   - Track and compare results

4. Early Stopping
   - Implement early stopping callback
   - Monitor validation loss
   - Patience = 5 epochs
   - Restore best weights

5. Final Model
   - Best configuration from experiments
   - Train with early stopping
   - Evaluate on test set

6. Analysis
   - Which class is hardest? (confusion matrix)
   - What mistakes are common?
   - Visualize misclassifications

7. Visualization requirements:
   - Fashion items sample grid
   - Batch size comparison (accuracy)
   - Learning rate comparison (loss curves)
   - Optimizer comparison (training time + accuracy)
   - Final model confusion matrix
   - Misclassified examples
```

**Deliverables:**
- `fashion-mnist-training.ipynb`
- Experiment results summary
- Best model saved

**Success Criteria:**
- Test accuracy > 85%
- Systematic experimentation completed
- Understand training hyperparameters impact

---

### Session 4: Regularization & Optimization (2 hours)

**Learning Objectives:**
1. Diagnose overfitting in neural networks
2. Apply Dropout regularization
3. Use Batch Normalization
4. Implement learning rate scheduling
5. Optimize MNIST to 98%+

**Video Content (60 minutes):**

#### Video 4.1: Overfitting in Neural Networks (12 minutes)
- Signs of overfitting
- Training accuracy → 99%, Test accuracy → 85%
- The memorization problem
- When NNs are prone to overfit

#### Video 4.2: Dropout Regularization (18 minutes)
- Randomly dropping neurons during training
- Dropout rate (typically 0.2-0.5)
- Where to add dropout (after hidden layers)
- How it prevents co-adaptation
- Implementation in Keras

#### Video 4.3: Batch Normalization (15 minutes)
- Normalizing activations between layers
- Speeds up training
- Acts as regularization
- Where to add (after Dense, before Activation)
- Controversy and best practices

#### Video 4.4: Learning Rate Scheduling (15 minutes)
- Adaptive learning rates
- ReduceLROnPlateau callback
- Step decay
- Exponential decay
- Cyclic learning rates (brief)

**Hands-On Activity (60 minutes):**

**Project: Improve MNIST to >98%**

Code Requirements:
```python
# Required implementations:
1. Baseline Model (from Session 2)
   - Reload MNIST model
   - Current performance: ~95-96%
   - Identify overfitting (train vs val curves)

2. Add Dropout
   - Add Dropout(0.2) after each Dense layer
   - Retrain
   - Compare to baseline

3. Add Batch Normalization
   - Add BatchNormalization after each Dense layer
   - Retrain
   - Compare to baseline and dropout

4. Combine Techniques
   - Dropout + Batch Normalization
   - Early stopping
   - Learning rate reduction
   - Optimal architecture:
     - 784 input
     - Dense(256) + BatchNorm + ReLU + Dropout(0.3)
     - Dense(128) + BatchNorm + ReLU + Dropout(0.2)
     - Dense(10) + Softmax

5. Training
   - 50 epochs max
   - Early stopping (patience=10)
   - ReduceLROnPlateau (patience=5)
   - Track all experiments

6. Evaluation
   - Test accuracy goal: >98%
   - Confusion matrix
   - Error analysis

7. Visualization requirements:
   - Baseline vs regularized (comparison)
   - Training curves (all experiments)
   - Confusion matrix (improved model)
   - Regularization impact chart
```

**Deliverables:**
- `mnist-optimized-98plus.ipynb`
- Model progression analysis
- Final model >98% accuracy

**Success Criteria:**
- Test accuracy > 98%
- Overfitting reduced (train/val gap < 2%)
- All regularization techniques applied correctly

---

### Session 5: Transfer Learning (2 hours)

**Learning Objectives:**
1. Understand transfer learning concept
2. Use pre-trained models (VGG16, ResNet)
3. Freeze and unfreeze layers
4. Fine-tune models
5. Apply to image classification

**Video Content (60 minutes):**

#### Video 5.1: Transfer Learning Concept (12 minutes)
- Training from scratch vs transfer learning
- Pre-trained models on ImageNet
- Feature extraction:
  - Early layers: edges, textures
  - Middle layers: patterns, parts
  - Late layers: complex objects
- When to use transfer learning

#### Video 5.2: Pre-trained Models (15 minutes)
- VGG16/19: Simple, deep
- ResNet50: Skip connections
- InceptionV3: Multi-scale
- MobileNet: Lightweight
- EfficientNet: State-of-the-art
- Choosing a model

#### Video 5.3: Feature Extraction (18 minutes)
- Using pre-trained model as feature extractor
- Freeze all layers
- Add custom classification head
- Train only new layers
- Fast training!

#### Video 5.4: Fine-Tuning (15 minutes)
- Unfreezing layers
- Fine-tuning top layers
- Very small learning rate
- Two-stage training:
  1. Train classifier (frozen base)
  2. Fine-tune (unfreeze top layers)

**Hands-On Activity (60 minutes):**

**Project: Image Classification with VGG16/ResNet**

Dataset Requirements:
- Small image dataset for transfer learning
- Options:
  - Cats vs Dogs (25,000 images)
  - Flowers (5 classes, ~3,000 images)
  - Food101 subset
  - Custom dataset
- Source: Kaggle or TensorFlow Datasets

Code Requirements:
```python
# Required implementations:
1. Load Pre-trained Model
   - VGG16 from keras.applications
   - Weights='imagenet'
   - Include_top=False

2. Feature Extraction
   - Freeze all VGG16 layers
   - Add custom classification head:
     - GlobalAveragePooling2D
     - Dense(256) + ReLU + Dropout(0.5)
     - Dense(num_classes) + Softmax

3. Data Preparation
   - Load images
   - Resize to 224×224
   - Normalize (important!)
   - Data augmentation:
     - Rotation, flip, zoom
     - ImageDataGenerator

4. Training (Feature Extraction)
   - Train only new layers
   - 10 epochs
   - Evaluate

5. Fine-Tuning
   - Unfreeze top 4 VGG16 layers
   - Very small learning rate (1e-5)
   - Train 10 more epochs
   - Evaluate

6. Comparison
   - Training from scratch (optional, for comparison)
   - Feature extraction only
   - Fine-tuned model
   - Accuracy and training time

7. Visualization requirements:
   - Data augmentation examples
   - Training curves (feature extraction + fine-tuning)
   - Confusion matrix
   - Sample predictions
   - Comparison table
```

**Deliverables:**
- `transfer-learning-vgg16.ipynb`
- Fine-tuned model saved
- Transfer learning vs from-scratch comparison

**Success Criteria:**
- Model accuracy > 90%
- Transfer learning faster than from scratch
- Understanding of when to use transfer learning

---

### Session 6: Neural Networks for Tabular Data (2 hours + Capstone)

**Learning Objectives:**
1. Apply NNs to structured/tabular data
2. Design architectures for tabular data
3. Compare NN to traditional ML
4. Use embeddings for categorical features
5. Build NN stock predictor

**Video Content (60 minutes):**

#### Video 6.1: NNs for Tabular Data (15 minutes)
- Most tabular data: traditional ML wins
- When NNs for tabular:
  - Very large datasets (millions of rows)
  - Complex interactions
  - Mixed data types
- Entity embeddings for categoricals

#### Video 6.2: Architecture Design (15 minutes)
- Input layer: All features
- Hidden layers: 2-4 layers
- Layer sizes: Decreasing (e.g., 256 → 128 → 64)
- Regularization: Dropout, BatchNorm
- Output: Regression or classification

#### Video 6.3: Preprocessing for NNs (15 minutes)
- Feature scaling (CRITICAL!)
- Handling categorical variables:
  - One-hot encoding
  - Embeddings (advanced)
- Missing values
- Feature engineering still important

#### Video 6.4: NN vs Traditional ML (15 minutes)
- Comparison on several datasets
- When NN wins:
  - Large data
  - Deep interactions
- When traditional ML wins:
  - Small data
  - Interpretability matters
  - Faster training needed
- Practical advice

**Hands-On Activity (60 minutes):**

**Project: Tabular Data NN Comparison**

Code Requirements:
```python
# Required implementations:
1. Load Tabular Dataset
   - Churn dataset from Module 2
   - Or house prices from Module 3

2. Preprocessing
   - Feature scaling (StandardScaler)
   - Handle categoricals
   - Train/test split

3. Build Neural Network
   - Input: All features
   - Hidden: 3 layers (128 → 64 → 32)
   - Dropout + BatchNorm
   - Output: 1 (sigmoid for classification)

4. Train
   - Early stopping
   - Learning rate reduction
   - 100 epochs max

5. Compare to Traditional ML
   - Random Forest (Module 2)
   - Gradient Boosting
   - Logistic Regression
   - Metrics comparison
   - Training time comparison

6. Analysis
   - When did NN win?
   - When did traditional ML win?
   - Trade-offs

7. Visualization requirements:
   - Training curves
   - Model comparison table
   - Performance vs training time scatter
```

**Capstone Project (3-4 hours):**

**Stock Predictor with Neural Networks**

Code Requirements:
```python
# Complete NN stock predictor (Module 3 callback!):
1. Data Preparation
   - Load stock data (Module 3)
   - Feature engineering (Module 3 library)
   - Scale features
   - Time series split

2. Build LSTM Network
   - Input: Sequence of past days
   - LSTM layers: 2 layers (50 units each)
   - Dense layers: 2 layers
   - Output: Next day's price

3. Alternative: Dense Network
   - Input: Engineered features
   - Hidden layers: 4 layers
   - Output: Price prediction

4. Training
   - Early stopping
   - Learning rate scheduling
   - 100-200 epochs

5. Evaluation
   - MAE, MSE, RMSE, R²
   - Residual analysis
   - Visual predictions

6. Comparison to Module 3
   - Random Forest regressor (Module 3)
   - Linear Regression (Module 3)
   - LSTM Neural Network (NEW!)
   - Dense Neural Network (NEW!)
   - Which is best?
   - Why?

7. Insights
   - Do neural networks help for stock prediction?
   - Trade-offs (accuracy vs complexity)
   - Recommendations

8. Visualization requirements:
   - Actual vs Predicted (all models)
   - Training curves
   - Model comparison table
   - Performance metrics comparison
   - Residual plots
   - Feature importance (if applicable)
```

**Deliverables:**
- `stock-predictor-neural-network.ipynb`
- LSTM model saved
- Dense model saved
- Comprehensive comparison to Module 3
- When-to-use-NNs decision guide (complete)

**Success Criteria:**
- NN achieves competitive performance (R² > 0.70)
- LSTM and Dense networks compared
- Thoughtful comparison to traditional ML
- Clear understanding of when NNs are appropriate
- Complete decision framework for ML vs DL

---

## Module 6: Complete Dataset Requirements

### Dataset 1: Iris (Reuse)
- From Module 2
- Built into sklearn

### Dataset 2: MNIST Digits
- Built into Keras
- 60,000 train, 10,000 test
- 28×28 grayscale

### Dataset 3: Fashion MNIST
- Built into Keras
- Same dimensions as MNIST
- 10 fashion classes

### Dataset 4: Cats vs Dogs OR Flowers
- **Cats vs Dogs:**
  - Source: Kaggle
  - 25,000 images
  - Binary classification
- **Flowers:**
  - Source: TensorFlow Datasets
  - 5 classes, ~3,000 images
  - Multi-class classification

### Dataset 5: Stock Data (Reuse)
- From Module 3
- With feature engineering

Download Script:
```python
# download_module6_datasets.py
# MNIST and Fashion MNIST: Built-in
# Cats vs Dogs: Kaggle API or manual
# Stock data: Reuse Module 3
```

---

## Module 6: Complete Assessment Requirements

### Quizzes (6 total, ~50 questions)

**Session 1 Quiz (8-10 questions):**
- Neural network concepts
- Neurons and layers
- Forward propagation
- NN vs traditional ML

**Session 2 Quiz (8-10 questions):**
- Keras Sequential API
- Dense layers
- Activation functions
- Model compilation

**Session 3 Quiz (8-10 questions):**
- Loss functions
- Optimizers
- Batch size and epochs
- Early stopping

**Session 4 Quiz (8-10 questions):**
- Overfitting in NNs
- Dropout
- Batch Normalization
- Learning rate scheduling

**Session 5 Quiz (8-10 questions):**
- Transfer learning concept
- Pre-trained models
- Feature extraction vs fine-tuning
- When to use transfer learning

**Session 6 Quiz (8-10 questions):**
- NNs for tabular data
- Architecture design
- Embeddings
- NN vs traditional ML

### Project Rubrics

**Session Projects (5 × 15 points = 75 points):**
- Correct implementation (50%)
- Target accuracy achieved (25%)
- Visualizations and analysis (15%)
- Documentation (10%)

**Stock Predictor NN Capstone (100 points):**
- Data preparation (15 points)
- LSTM implementation (20 points)
- Dense network implementation (15 points)
- Training and optimization (15 points)
- Comprehensive comparison (20 points)
- Insights and recommendations (10 points)
- Code quality and documentation (5 points)

---

## Module 6: Visual Assets Needed

1. **Neuron Anatomy Diagram**
2. **Neural Network Architecture Visualization**
3. **Forward Propagation Animation**
4. **Activation Functions Comparison**
5. **Training Process Flowchart**
6. **Overfitting Visualization**
7. **Transfer Learning Concept Diagram**
8. **Feature Extraction vs Fine-Tuning**
9. **NN vs Traditional ML Decision Tree**
10. **Module 6 Workflow Diagram**

---

## Module 6: Success Metrics

**By end of module, learners should:**
- ✅ Build neural networks with Keras
- ✅ Achieve MNIST >98% accuracy
- ✅ Apply transfer learning successfully
- ✅ Understand when to use NNs vs traditional ML
- ✅ Build LSTM for time series
- ✅ Compare deep learning to previous methods
- ✅ Make informed decisions on ML vs DL

---

# CROSS-MODULE REQUIREMENTS

## Shared Code Libraries

### 1. Feature Engineering Library (from Module 3)
- Reused in Module 6 for stock predictor

### 2. Evaluation Metrics Library (from Module 4)
- Used in all subsequent modules

### 3. Visualization Utilities
- Consistent plotting styles
- Reusable plot functions

## Consistent Documentation

### README Template
```markdown
# Project Name

## Overview
Brief description

## Dataset
Source, features, size

## Requirements
```bash
pip install -r requirements.txt
```

## Usage
How to run

## Expected Results
Performance targets

## Visualizations
What to expect

## Success Criteria
How to know it worked
```

### Notebook Template
- Imports section
- Data loading
- EDA
- Model building
- Training
- Evaluation
- Visualizations
- Conclusions

## Visual Design System

### Colors
- Primary: Blue (#1f77b4)
- Secondary: Orange (#ff7f0e)
- Success: Green (#2ca02c)
- Error: Red (#d62728)

### Plot Styles
- Consistent figure sizes: (12, 6) or (10, 8)
- Grid: Always on
- Font size: Title 14, Labels 12
- DPI: 100

---

# PRODUCTION PRIORITIES

## High Priority (Core Functionality)
1. All code notebooks with working implementations
2. All datasets sourced and downloadable
3. Complete evaluation for all projects
4. Working models that achieve targets

## Medium Priority (Quality)
5. Complete quiz banks (50 questions per module)
6. Detailed project rubrics
7. README files for all projects
8. AI prompts documentation

## Lower Priority (Enhancement)
9. Visual assets (can be added later)
10. Advanced extensions
11. Optional bonus projects

---

**Status:** DETAILED SPECIFICATIONS COMPLETE
**Ready for:** Agent deployment for production material creation
**Estimated Time per Module:** 15-25 hours of production work each

---

**Created:** 2026-01-05
**Version:** 1.0 (Production Specifications)
**Total Pages:** 80+ (comprehensive detail for all 3 modules)
