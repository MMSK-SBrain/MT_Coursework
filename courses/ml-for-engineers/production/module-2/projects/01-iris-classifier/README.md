# Iris Flower Classification Project
## Your First Machine Learning Model

**Module:** 2 - Classification
**Session:** 1
**Difficulty:** ⭐ Beginner
**Time:** 2-3 hours
**Target Accuracy:** >90%

---

## Project Overview

This is your **FIRST** machine learning project! You'll build a classifier that can identify iris flower species based on their measurements.

### What You'll Build
A multi-class classification model that predicts iris species (setosa, versicolor, or virginica) from flower measurements.

### Why This Project?
- Perfect for beginners (clean, small dataset)
- Fast training (seconds, not hours)
- Clear visual results
- High accuracy achievable
- Foundation for all future ML projects

---

## Learning Objectives

By completing this project, you will:

1. ✅ Understand the complete ML workflow
2. ✅ Load and explore a dataset
3. ✅ Visualize feature relationships
4. ✅ Split data into train/test sets
5. ✅ Train your first classifier
6. ✅ Make predictions on new data
7. ✅ Evaluate model performance
8. ✅ Compare multiple algorithms
9. ✅ Interpret results

---

## Dataset: Iris Flowers

### About
- **Source:** UCI Machine Learning Repository (built into sklearn)
- **Samples:** 150 flowers (50 per species)
- **Features:** 4 measurements per flower
- **Classes:** 3 species
- **Balance:** Perfectly balanced (equal samples per class)

### Features

| Feature | Unit | Description | Range |
|---------|------|-------------|-------|
| Sepal Length | cm | Length of sepal | 4.3 - 7.9 |
| Sepal Width | cm | Width of sepal | 2.0 - 4.4 |
| Petal Length | cm | Length of petal | 1.0 - 6.9 |
| Petal Width | cm | Width of petal | 0.1 - 2.5 |

### Target Classes
- **Setosa** (0): Small petals, easy to identify
- **Versicolor** (1): Medium-sized petals
- **Virginica** (2): Large petals

---

## Project Structure

```
01-iris-classifier/
├── iris-classifier-complete.ipynb  # Main notebook
├── README.md                        # This file
├── prompts-used.md                  # AI prompts documentation
└── results/                         # Output folder (created when run)
```

---

## Requirements

### Software
- Python 3.8+
- Jupyter Notebook or Google Colab

### Libraries
```bash
pip install pandas numpy scikit-learn matplotlib seaborn
```

Or use the Module 2 requirements:
```bash
pip install -r ../../datasets/requirements.txt
```

---

## Getting Started

### Option 1: Google Colab (Recommended for Beginners)
1. Go to [Google Colab](https://colab.research.google.com/)
2. Upload `iris-classifier-complete.ipynb`
3. Run all cells (Runtime → Run all)
4. Follow along with the outputs

### Option 2: Local Jupyter
1. Install requirements: `pip install -r ../../datasets/requirements.txt`
2. Launch Jupyter: `jupyter notebook`
3. Open `iris-classifier-complete.ipynb`
4. Run cells one by one

---

## Notebook Sections

### Part 1: Setup & Data Loading (10 min)
- Import libraries
- Load Iris dataset
- Convert to pandas DataFrame
- Initial exploration

### Part 2: Exploratory Data Analysis (15 min)
- View dataset info
- Check for missing values
- Visualize class distribution
- Feature distributions by species
- Pairplot analysis
- Correlation heatmap

### Part 3: Data Preparation (5 min)
- Separate features (X) and labels (y)
- Train/test split (80/20)
- Understand why we split data

### Part 4: Model Training (10 min)
- Create Decision Tree classifier
- Train on training data
- **THE MOMENT:** Your first model trains!

### Part 5: Predictions (10 min)
- Make predictions on test set
- Compare predicted vs actual
- Test with new flower measurements

### Part 6: Evaluation (15 min)
- Calculate accuracy score
- Classification report (precision, recall, F1)
- Confusion matrix visualization
- Interpret results

### Part 7: Algorithm Comparison (20 min)
- Train 4 different algorithms:
  - Decision Tree
  - Logistic Regression
  - Random Forest
  - K-Nearest Neighbors
- Compare accuracies
- Visualize comparison
- Find best model

### Part 8: Feature Importance (10 min)
- Extract feature importance
- Visualize which features matter most
- Understand decision-making

### Part 9: Summary (5 min)
- Review accomplishments
- Key learnings
- Next steps

---

## Expected Results

### Model Performance

| Algorithm | Expected Accuracy | Training Time |
|-----------|-------------------|---------------|
| Decision Tree | 93-97% | < 1 second |
| Logistic Regression | 95-100% | < 1 second |
| Random Forest | 93-97% | 1-2 seconds |
| K-Nearest Neighbors | 95-100% | < 1 second |

**All algorithms should exceed the 90% target!**

### Sample Output

```
✓ Dataset loaded successfully!
Shape: (150, 6)
Features: 4
Classes: 3

Training samples: 120 (80.0%)
Testing samples: 30 (20.0%)

🎉 MODEL TRAINING COMPLETE! 🎉

🎯 ACCURACY: 96.67%
Out of 30 test flowers, the model correctly classified 29 of them!

🎉 EXCELLENT! Your model exceeds the 90% target!

🏆 BEST MODEL: Logistic Regression
   Accuracy: 100.00%
```

---

## Key Concepts Explained

### Train/Test Split
**Why do we split data?**
- Training set: Model learns from this (80% of data)
- Test set: Model evaluated on this (20% of data)
- **Important:** Test set is NEW data the model hasn't seen
- Like studying practice problems, then taking real exam

### Accuracy
**What is accuracy?**
- Percentage of correct predictions
- Formula: (Correct Predictions / Total Predictions) × 100%
- Example: 29 correct out of 30 = 96.67% accuracy

### Confusion Matrix
**What does it show?**
- Rows: Actual species
- Columns: Predicted species
- Diagonal: Correct predictions
- Off-diagonal: Mistakes (confusions)

### Feature Importance
**Which features matter most?**
- Typically petal length and petal width are most important
- Sepals are less distinctive
- Decision Tree learns which features to use

---

## Common Issues & Solutions

### Issue: "Module not found"
**Solution:**
```bash
pip install pandas numpy scikit-learn matplotlib seaborn
```

### Issue: Plots not showing
**Solution:**
Add to first cell:
```python
%matplotlib inline
```

### Issue: Accuracy below 90%
**Solution:**
- Check random_state is set (for reproducibility)
- Try different algorithm (Random Forest or Logistic Regression)
- Verify train/test split is working correctly

### Issue: Dataset not loading
**Solution:**
```python
from sklearn.datasets import load_iris
iris = load_iris()
```
Iris is built into sklearn, no download needed!

---

## Extension Activities

### Beginner
1. Change test_size to 0.3 (30%). How does accuracy change?
2. Try different random_state values. Does accuracy vary?
3. Create additional visualizations (box plots, violin plots)

### Intermediate
1. Implement cross-validation (5-fold)
2. Add feature scaling (StandardScaler)
3. Tune hyperparameters (max_depth for Decision Tree)
4. Create a prediction function for user input

### Advanced
1. Build a simple web app (Streamlit) to classify user-input flowers
2. Implement ensemble voting (combine multiple models)
3. Visualize decision boundaries (2D projections)
4. Create an interactive dashboard (Plotly Dash)

---

## Success Criteria

### Minimum (Pass)
- [ ] Notebook runs without errors
- [ ] Achieves >90% accuracy
- [ ] Confusion matrix displayed
- [ ] At least 2 algorithms compared

### Target (Good)
- [ ] All above, plus:
- [ ] Feature importance analyzed
- [ ] All 4 algorithms compared
- [ ] Results clearly documented

### Excellent (Outstanding)
- [ ] All above, plus:
- [ ] Additional visualizations created
- [ ] Extension activity completed
- [ ] Code well-commented
- [ ] Insights documented

---

## AI-Assisted Development

This project can be built entirely using AI assistance (ChatGPT, Claude, Gemini).

### Recommended Prompts
See `prompts-used.md` for complete list of prompts used to generate this notebook.

### Learning Approach
1. **Understand first:** Read through completed notebook
2. **Modify:** Change parameters, try different visualizations
3. **Recreate:** Use AI prompts to rebuild from scratch
4. **Extend:** Add your own features and analysis

---

## Assessment

This project contributes to Module 2 Session 1 grade:

- **Code Execution:** 25 points (runs without errors)
- **Accuracy Target:** 25 points (>90% achieved)
- **Visualization:** 20 points (clear, professional plots)
- **Algorithm Comparison:** 15 points (multiple algorithms tested)
- **Documentation:** 15 points (clear explanations, insights)

**Total:** 100 points

**Pass Threshold:** 70 points

---

## Next Steps

### Immediate
1. Complete this Iris classifier project
2. Experiment with different parameters
3. Try extension activities

### Next Session
**Session 2: Spam Email Detection**
- Text classification (NLP basics)
- Handling imbalanced data
- Real-world application

### Future Projects
- Customer churn prediction (business analytics)
- Heart disease classification (healthcare AI)
- MNIST digit recognition (computer vision)

---

## Resources

### Documentation
- [Scikit-learn Iris Dataset](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html)
- [Decision Trees](https://scikit-learn.org/stable/modules/tree.html)
- [Model Evaluation](https://scikit-learn.org/stable/modules/model_evaluation.html)

### Tutorials
- [Scikit-learn Tutorial](https://scikit-learn.org/stable/tutorial/index.html)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Gallery](https://matplotlib.org/stable/gallery/index.html)

### Community
- [Stack Overflow](https://stackoverflow.com/questions/tagged/scikit-learn)
- [Kaggle Iris Notebooks](https://www.kaggle.com/datasets/uciml/iris)

---

## Credits

**Dataset:** R.A. Fisher (1936), "The use of multiple measurements in taxonomic problems"

**Course:** ML for Engineers
**Module:** 2 - Classification
**Created:** 2026-01-05
**Version:** 1.0

---

## Questions?

If you're stuck:
1. Check the "Common Issues" section above
2. Review the completed notebook step-by-step
3. Use AI assistance (ChatGPT, Claude, Gemini)
4. Ask in course forums
5. Review Module 1 (data exploration basics)

---

**Remember:** This is your FIRST ML model. Take your time, understand each step, and celebrate when it works!

🎉 **You're building the foundation for your ML career!** 🎉
