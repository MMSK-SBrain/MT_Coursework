# Iris Classifier Project Rubric

**Total Points:** 50
**Module:** 2 - Classification
**Project:** Iris Classifier (Foundational)
**Session:** 2.1
**Target Accuracy:** >90%

---

## Project Overview

This is your first complete machine learning project. You will build a classification model to predict iris flower species based on physical measurements. This project establishes the fundamental ML workflow that you'll use throughout the course.

**Learning Objectives:**
- Load and explore a dataset
- Understand features vs labels
- Implement train/test split
- Train classification models
- Evaluate model performance
- Compare multiple algorithms

---

## Grading Criteria

### 1. Data Loading & Exploration (10 points)

| Points | Criteria |
|--------|----------|
| 9-10 | **Excellent:** Loads data correctly using sklearn, converts to pandas DataFrame, explores all features with summary statistics, generates insightful visualizations (class distribution, feature distributions, pairplot, correlation heatmap), identifies patterns (e.g., petal measurements are most discriminative), checks for missing values, provides clear observations |
| 7-8 | **Good:** Loads data correctly, basic exploration with summary statistics, 2-3 standard visualizations (class distribution, basic plots), identifies some patterns, checks for missing values |
| 5-6 | **Adequate:** Loads data successfully, minimal exploration (head/info only), 1 visualization, basic observations, may miss missing value check |
| 3-4 | **Poor:** Loads data with errors or incomplete exploration, no visualizations, no meaningful observations |
| 0-2 | **Failing:** Cannot load data or no exploration performed |

**Key Requirements:**
- ✅ Load Iris dataset from sklearn
- ✅ Convert to pandas DataFrame
- ✅ Display first few rows, info(), describe()
- ✅ Check for missing values
- ✅ Create at least 2 visualizations
- ✅ Provide observations about the data

---

### 2. Train/Test Split Implementation (5 points)

| Points | Criteria |
|--------|----------|
| 5 | **Excellent:** Correctly implements 80/20 train/test split using sklearn's train_test_split, uses random_state for reproducibility, applies stratify parameter to maintain class distribution, correctly separates features (X) from labels (y), verifies split sizes, explains purpose of split |
| 4 | **Good:** Correct 80/20 split with random_state, separates X and y correctly, verifies sizes, basic explanation |
| 3 | **Adequate:** Implements split (may not be 80/20), may miss random_state or stratify, basic X/y separation, minimal explanation |
| 2 | **Poor:** Incorrect split ratio, doesn't use random_state, doesn't verify sizes, no explanation |
| 0-1 | **Failing:** No proper train/test split or critical errors |

**Key Requirements:**
- ✅ Separate features (X) from target (y)
- ✅ Use 80/20 or similar split ratio
- ✅ Set random_state=42 (or any fixed value)
- ✅ Use stratify=y to maintain class balance
- ✅ Verify training and test set sizes
- ✅ Explain why we split data

---

### 3. Model Training (15 points)

| Points | Criteria |
|--------|----------|
| 14-15 | **Excellent:** Trains 4+ different classification algorithms (Decision Tree, Logistic Regression, Random Forest, KNN), all implemented correctly with appropriate hyperparameters, uses random_state for reproducibility, code runs without errors, achieves >90% accuracy on at least 3 algorithms, includes informative comments |
| 11-13 | **Good:** Trains 3 algorithms correctly, appropriate hyperparameters, achieves >90% on at least 2 algorithms, includes basic comments, minor issues only |
| 8-10 | **Adequate:** Trains 2 algorithms, basic implementation, achieves 80-90% accuracy, minimal comments, some errors but code generally works |
| 5-7 | **Poor:** Trains 1 algorithm only, or below 80% accuracy, or significant implementation errors, poor documentation |
| 0-4 | **Failing:** Cannot train models, code doesn't run, or major conceptual errors |

**Key Requirements:**
- ✅ Import appropriate sklearn libraries
- ✅ Create model instances
- ✅ Train using model.fit(X_train, y_train)
- ✅ Implement at least 3 algorithms:
  - Decision Tree Classifier
  - Logistic Regression
  - Random Forest Classifier
  - K-Nearest Neighbors (optional 4th)
- ✅ Use random_state for reproducible results
- ✅ Add code comments explaining each step
- ✅ Achieve target accuracy (>90%)

**Suggested Algorithms & Parameters:**
```python
# Decision Tree
DecisionTreeClassifier(random_state=42)

# Logistic Regression
LogisticRegression(max_iter=200, random_state=42)

# Random Forest
RandomForestClassifier(n_estimators=100, random_state=42)

# K-Nearest Neighbors
KNeighborsClassifier(n_neighbors=5)
```

---

### 4. Model Evaluation & Comparison (15 points)

| Points | Criteria |
|--------|----------|
| 14-15 | **Excellent:** Calculates accuracy for all models, creates comprehensive confusion matrix with heatmap visualization, generates classification report with precision/recall/F1, compares all algorithms with bar chart visualization, identifies best performing model, analyzes where model makes mistakes, provides insights and recommendations |
| 11-13 | **Good:** Calculates accuracy for all models, confusion matrix with visualization, classification report, algorithm comparison chart, identifies best model, basic error analysis |
| 8-10 | **Adequate:** Calculates accuracy, basic confusion matrix (may lack visualization), limited classification report, simple comparison, identifies best model, minimal analysis |
| 5-7 | **Poor:** Accuracy calculation only, incomplete confusion matrix, no comparison visualization, limited insights |
| 0-4 | **Failing:** No proper evaluation or comparison, missing key metrics |

**Key Requirements:**
- ✅ Calculate accuracy_score for all models
- ✅ Create confusion matrix (at least for best model)
- ✅ Visualize confusion matrix as heatmap
- ✅ Generate classification_report
- ✅ Create comparison table or chart of all algorithms
- ✅ Identify and highlight best performing algorithm
- ✅ Analyze and explain results
- ✅ Discuss which species (if any) are confused

**Required Visualizations:**
1. Confusion matrix heatmap
2. Algorithm comparison bar chart (accuracy)
3. (Optional) Feature importance chart

---

### 5. Testing with New Data (5 points)

| Points | Criteria |
|--------|----------|
| 5 | **Excellent:** Tests model with 3+ new flower samples, shows predictions with confidence probabilities, verifies predictions make sense (e.g., small petals → setosa), includes varied test cases, provides clear output with species names (not just numbers) |
| 4 | **Good:** Tests with 2-3 new samples, shows predictions, basic probability output, reasonable verification |
| 3 | **Adequate:** Tests with 1-2 samples, shows predictions, minimal probability info, limited verification |
| 2 | **Poor:** Tests with 1 sample only, no probabilities, no verification |
| 0-1 | **Failing:** No testing with new data |

**Key Requirements:**
- ✅ Create new flower measurement arrays
- ✅ Use model.predict() for predictions
- ✅ Use model.predict_proba() for confidence scores
- ✅ Display results clearly with species names
- ✅ Test at least 3 different flower measurements

**Example Test Cases:**
```python
# Small petals (likely setosa)
[5.1, 3.5, 1.4, 0.2]

# Large petals (likely virginica)
[6.5, 3.0, 5.2, 2.0]

# Medium petals (likely versicolor)
[5.9, 3.0, 4.2, 1.5]
```

---

## Bonus Points (Optional - Up to +5 points)

### Feature Importance Analysis (+3 points)
- Extract and visualize feature importance from Decision Tree or Random Forest
- Create horizontal bar chart showing importance scores
- Explain which features matter most for classification
- Relate findings to exploratory analysis

### Cross-Validation (+2 points)
- Implement k-fold cross-validation (k=5)
- Compare cross-validation scores to single train/test split
- Discuss advantages of cross-validation
- Calculate mean and standard deviation of CV scores

---

## Code Quality Standards

### Required Code Quality Elements:
- ✅ **Comments:** Clear comments explaining what each code section does
- ✅ **Structure:** Organized sections (imports, loading, EDA, training, evaluation)
- ✅ **Naming:** Descriptive variable names (model_dt, X_train, accuracy_lr)
- ✅ **Reproducibility:** Random seeds set (random_state=42)
- ✅ **Output:** Clear print statements and labels for all results
- ✅ **Visualizations:** Professional charts with titles, labels, legends

### Deductions for Poor Code Quality:
- -2 points: No comments or unclear code
- -1 point: Poor variable naming (x1, x2, m1, m2)
- -1 point: No random_state (results not reproducible)
- -1 point: Missing labels on charts
- -1 point: Disorganized or messy code structure

---

## Submission Requirements

### What to Submit:
1. **Jupyter Notebook (.ipynb)** with all code and outputs
2. **Brief Report** (can be in notebook as markdown):
   - Summary of approach
   - Best model and accuracy achieved
   - Key insights from analysis
   - Any challenges faced

### File Naming:
- `iris-classifier-[YourName].ipynb`
- Example: `iris-classifier-sarah-chen.ipynb`

### Checklist Before Submission:
- [ ] All code cells run without errors (Kernel → Restart & Run All)
- [ ] All visualizations display correctly
- [ ] Achieves >90% accuracy target
- [ ] At least 3 algorithms implemented and compared
- [ ] Confusion matrix included
- [ ] New data predictions demonstrated
- [ ] Code is well-commented
- [ ] Results are clearly labeled

---

## Common Mistakes to Avoid

❌ **Testing on training data** - Always evaluate on X_test, never X_train
❌ **No train/test split** - Never train and test on the same data
❌ **Ignoring random_state** - Results won't be reproducible
❌ **Only checking accuracy** - Use confusion matrix and classification report too
❌ **Not testing with new data** - Demonstrate real-world prediction capability
❌ **Unlabeled visualizations** - Always add titles, axis labels, legends
❌ **No comparison** - Must compare multiple algorithms
❌ **Copy-paste without understanding** - Make sure you understand each line

---

## Grading Summary

| Category | Points | Your Score |
|----------|--------|------------|
| Data Loading & Exploration | 10 | |
| Train/Test Split | 5 | |
| Model Training | 15 | |
| Model Evaluation & Comparison | 15 | |
| Testing with New Data | 5 | |
| **Subtotal** | **50** | |
| Bonus (Optional) | +5 max | |
| Code Quality Deductions | Up to -5 | |
| **TOTAL** | **50** | |

**Passing Score:** 35/50 (70%)
**Target Score:** 40/50 (80%)
**Excellence Score:** 45+/50 (90%+)

---

## Success Criteria

### Minimum Requirements (Pass - 35/50):
- ✅ Load and explore Iris dataset
- ✅ Implement proper train/test split
- ✅ Train at least 2 classification algorithms
- ✅ Achieve >80% accuracy
- ✅ Calculate and display accuracy scores
- ✅ Basic confusion matrix
- ✅ Test with at least 1 new sample

### Target Performance (B - 40/50):
- All minimum requirements, plus:
- ✅ Train 3+ algorithms
- ✅ Achieve >90% accuracy
- ✅ Detailed confusion matrix with visualization
- ✅ Algorithm comparison with chart
- ✅ Test with 3+ new samples
- ✅ Good code quality and documentation

### Excellent Performance (A - 45+/50):
- All target requirements, plus:
- ✅ Train 4 algorithms
- ✅ Classification report analysis
- ✅ Feature importance or cross-validation
- ✅ Comprehensive analysis with insights
- ✅ Professional visualizations
- ✅ Outstanding code quality

---

## AI-Assisted Development Notes

This project is designed to be completed with AI assistance (ChatGPT, Claude, etc.).

**Recommended Prompts:**
```
1. "Load the Iris dataset from sklearn and convert it to a pandas DataFrame.
   Show me the first few rows and create visualizations of the data."

2. "Split the Iris dataset into training and testing sets (80/20).
   Explain what X and y represent."

3. "Train a Decision Tree classifier on the Iris dataset.
   Calculate and display the accuracy."

4. "Compare 4 different classification algorithms on Iris:
   Decision Tree, Logistic Regression, Random Forest, and KNN.
   Create a comparison chart."

5. "Create a confusion matrix for the Iris classification results.
   Visualize it as a heatmap."
```

**Learning Tip:** Don't just copy-paste AI code. Ask AI to explain each part, then type it yourself!

---

## Resources

### Documentation:
- [Scikit-learn Classification Guide](https://scikit-learn.org/stable/supervised_learning.html#supervised-learning)
- [Iris Dataset Documentation](https://scikit-learn.org/stable/datasets/toy_dataset.html#iris-dataset)
- [Train/Test Split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html)
- [Confusion Matrix](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html)

### Helpful Tutorials:
- Session 2.1 Video: "Your First Classifier"
- Module 2 Framework: Classification section
- Iris Classifier Example Notebook (provided)

---

**Created:** 2026-01-06
**Version:** 1.0
**Course:** ML for Engineers - Module 2
**Last Updated:** 2026-01-06
