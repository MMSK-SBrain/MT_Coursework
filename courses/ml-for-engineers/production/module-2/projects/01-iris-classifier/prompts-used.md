# AI Prompts Used - Iris Classifier Project
## Complete Prompt Library for Building This Project

**Project:** Iris Flower Classification
**Module:** 2 - Classification
**Purpose:** Document all AI prompts used to create this project
**Use:** Students can use these prompts to recreate or modify the project

---

## How to Use This Document

1. **Copy any prompt below**
2. **Paste into your AI assistant** (ChatGPT, Claude, Gemini)
3. **Review and run the generated code**
4. **Modify as needed** for your specific requirements

**Note:** Prompts are ordered in the sequence used to build the project.

---

## Prompt 1: Project Setup

### Purpose
Initialize the project and import necessary libraries

### Prompt
```
Create Python code to import all necessary libraries for an Iris flower
classification project. Include:
- pandas and numpy for data manipulation
- sklearn for machine learning (datasets, model_selection, tree, metrics)
- matplotlib and seaborn for visualization
- Set up plotting style and random seed for reproducibility
```

### Expected Output
```python
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('seaborn-v0_8-darkgrid')
np.random.seed(42)
```

---

## Prompt 2: Load Dataset

### Purpose
Load the Iris dataset and convert to pandas DataFrame

### Prompt
```
Load the Iris dataset from sklearn and convert it to a pandas DataFrame.
Include:
1. Load the dataset using load_iris()
2. Create DataFrame with feature names as columns
3. Add target column with species labels (0, 1, 2)
4. Add species_name column with actual species names
5. Display first few rows and dataset info
```

### Expected Output
```python
# Load dataset
iris = load_iris()

# Convert to DataFrame
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = iris.target
df['species_name'] = df['species'].map({
    0: 'setosa', 1: 'versicolor', 2: 'virginica'
})

print(df.head())
print(df.info())
```

---

## Prompt 3: Exploratory Data Analysis

### Purpose
Create comprehensive EDA visualizations

### Prompt
```
Create exploratory data analysis for the Iris dataset including:
1. Display first 5 rows
2. Show dataset info and statistical summary
3. Check for missing values
4. Create bar chart of class distribution with custom colors
5. Create histograms showing feature distributions by species (2x2 grid)
6. Generate pairplot showing relationships between all features
7. Create correlation heatmap

Use professional styling with titles, labels, and legends.
```

### Expected Output
Multiple code cells with visualizations for each analysis component.

---

## Prompt 4: Class Distribution Visualization

### Purpose
Visualize the balance of classes in the dataset

### Prompt
```
Create a bar chart showing the distribution of iris species in the dataset.
Requirements:
- Use custom colors: '#FF6B6B', '#4ECDC4', '#45B7D1'
- Add title "Iris Species Distribution"
- Label axes properly
- Add gridlines
- Display count values
- Figure size: 8x5 inches
```

---

## Prompt 5: Feature Distribution by Species

### Purpose
Show how each feature varies across species

### Prompt
```
Create a 2x2 grid of histograms showing the distribution of each Iris
feature (sepal length, sepal width, petal length, petal width) colored
by species. Each subplot should:
- Show overlapping histograms for 3 species
- Use semi-transparent colors
- Include legend
- Have proper title and labels
- Show gridlines
```

---

## Prompt 6: Pairplot

### Purpose
Visualize all feature relationships simultaneously

### Prompt
```
Create a seaborn pairplot for the Iris dataset colored by species.
Use custom color palette: ['#FF6B6B', '#4ECDC4', '#45B7D1']
Add a super title "Iris Dataset - Feature Relationships"
```

---

## Prompt 7: Correlation Heatmap

### Purpose
Show correlation between numerical features

### Prompt
```
Create a correlation heatmap for the Iris dataset features (excluding target).
Requirements:
- Use 'coolwarm' colormap
- Display correlation values (annot=True)
- Center colormap at 0
- Square cells
- Add colorbar
- Title: "Feature Correlation Heatmap"
- Figure size: 10x8 inches
```

---

## Prompt 8: Train/Test Split

### Purpose
Prepare data for machine learning

### Prompt
```
Split the Iris dataset into training and testing sets.
Requirements:
1. Separate features (X) and target (y)
2. Use 80/20 train/test split
3. Set random_state=42 for reproducibility
4. Use stratify=y to maintain class balance
5. Print the shapes and sizes of resulting sets
6. Add explanatory comments about why we split data
```

### Expected Output
```python
# Separate features and target
X = iris.data
y = iris.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print(f"Training samples: {len(X_train)}")
print(f"Testing samples: {len(X_test)}")
```

---

## Prompt 9: Train Decision Tree Model

### Purpose
Build and train the first classification model

### Prompt
```
Create and train a Decision Tree classifier for the Iris dataset.
Include:
1. Create DecisionTreeClassifier with random_state=42
2. Train the model using fit() on training data
3. Print confirmation messages before and after training
4. Add celebratory message when complete
5. Explain what's happening during training
```

### Expected Output
```python
# Create model
model = DecisionTreeClassifier(random_state=42)

# Train model
print("Training model...")
model.fit(X_train, y_train)
print("✓ Model training complete!")
```

---

## Prompt 10: Make Predictions

### Purpose
Use trained model to predict species

### Prompt
```
Use the trained model to make predictions on the test set.
Then create a comparison showing:
1. First 10 actual species names
2. First 10 predicted species names
3. Checkmark (✓) for correct predictions, (✗) for incorrect
4. Display as a formatted pandas DataFrame
```

---

## Prompt 11: Calculate Accuracy

### Purpose
Evaluate model performance

### Prompt
```
Calculate and display the accuracy of the Iris classifier.
Include:
1. Use accuracy_score to calculate accuracy
2. Display accuracy as percentage with 2 decimal places
3. Show interpretation (e.g., "29 out of 30 correct")
4. Add conditional message:
   - "EXCELLENT!" if accuracy >= 90%
   - "GOOD!" if accuracy >= 80%
   - "Needs improvement" if below 80%
5. Use celebratory formatting with emojis
```

---

## Prompt 12: Classification Report

### Purpose
Show detailed performance metrics

### Prompt
```
Generate and display a detailed classification report for the Iris model.
Include:
1. Use sklearn's classification_report
2. Show precision, recall, f1-score for each species
3. Add explanation of what each metric means
4. Format output clearly with proper labels
```

---

## Prompt 13: Confusion Matrix

### Purpose
Visualize prediction errors

### Prompt
```
Create and visualize a confusion matrix for the Iris classifier.
Requirements:
1. Calculate confusion matrix using sklearn
2. Visualize using ConfusionMatrixDisplay
3. Use 'Blues' colormap
4. Show species names as labels
5. Add title "Confusion Matrix - Decision Tree"
6. Figure size: 10x8 inches
7. Include explanation of how to read the matrix
```

---

## Prompt 14: Predict New Flowers

### Purpose
Test model with custom input

### Prompt
```
Create code to predict species for 3 new iris flowers with these measurements:
1. [5.1, 3.5, 1.4, 0.2] - likely setosa
2. [6.5, 3.0, 5.2, 2.0] - likely virginica
3. [5.9, 3.0, 4.2, 1.5] - likely versicolor

For each flower:
- Show the measurements
- Display predicted species
- Show probability/confidence for each class
- Format output clearly
```

---

## Prompt 15: Compare Multiple Algorithms

### Purpose
Train and compare 4 different classification algorithms

### Prompt
```
Compare 4 classification algorithms on the Iris dataset:
1. Decision Tree
2. Logistic Regression (max_iter=200)
3. Random Forest (n_estimators=100)
4. K-Nearest Neighbors (n_neighbors=5)

For each algorithm:
- Train on training data
- Predict on test data
- Calculate accuracy
- Store results in a dictionary

Print results and find the best performing model.
Set random_state=42 where applicable.
```

---

## Prompt 16: Visualize Algorithm Comparison

### Purpose
Create bar chart comparing algorithm performance

### Prompt
```
Create a bar chart comparing the accuracy of 4 classification algorithms
on the Iris dataset. Requirements:
- X-axis: Algorithm names
- Y-axis: Accuracy percentage
- Use colors: ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4']
- Add accuracy value labels on top of each bar
- Add horizontal line at 90% (target accuracy) in red dashed
- Title: "Algorithm Comparison - Iris Classification"
- Figure size: 12x6 inches
- Add legend for target line
- Rotate x-labels if needed
- Set y-axis limits to [80, 105] for better view
```

---

## Prompt 17: Feature Importance

### Purpose
Determine which features are most important

### Prompt
```
Extract and visualize feature importance from a Decision Tree trained
on the Iris dataset. Include:
1. Train a new Decision Tree
2. Extract feature_importances_
3. Create DataFrame with feature names and importance scores
4. Sort by importance (descending)
5. Display as table
6. Create horizontal bar chart of importance
7. Title: "Feature Importance - Decision Tree"
8. Color: '#45B7D1'
9. Add gridlines on x-axis
```

---

## Prompt 18: Project Summary

### Purpose
Create comprehensive project summary

### Prompt
```
Create a formatted project summary for the Iris classification project
including:
1. What was accomplished (8 key points)
2. Key learnings (6 bullet points)
3. Results summary:
   - Dataset statistics
   - Best model and accuracy
   - Target achievement status
4. Next steps (4 items)
5. Use celebratory formatting with emojis and section dividers
6. Make it clear this is a milestone achievement
```

---

## Advanced Prompts (Extensions)

### Prompt: Cross-Validation

```
Implement 5-fold cross-validation for the Iris dataset.
Use Decision Tree classifier and:
1. Import cross_val_score from sklearn
2. Perform 5-fold cross-validation
3. Print accuracy for each fold
4. Calculate mean and standard deviation
5. Compare to single train/test split result
6. Explain what cross-validation does and why it's better
```

### Prompt: Hyperparameter Tuning

```
Perform hyperparameter tuning for Decision Tree on Iris dataset using GridSearchCV.
Test these parameters:
- max_depth: [3, 5, 7, 10, None]
- min_samples_split: [2, 5, 10]
- min_samples_leaf: [1, 2, 4]

Display:
- Best parameters found
- Best cross-validation score
- Comparison to default parameters
```

### Prompt: Decision Boundary Visualization

```
Visualize decision boundaries for Iris classification using 2 features
(petal length and petal width). Create:
1. 2D scatter plot of data points colored by species
2. Decision boundary overlay showing regions for each class
3. Use Decision Tree classifier
4. Create mesh grid for smooth boundaries
5. Add legend and labels
6. Title: "Decision Boundaries - Iris Classification"
```

### Prompt: Interactive Prediction App

```
Create a simple interactive function that:
1. Takes 4 input parameters (sepal length, sepal width, petal length, petal width)
2. Validates inputs are within reasonable ranges
3. Makes prediction using trained model
4. Displays predicted species with confidence scores
5. Shows which features contributed most to the prediction
6. Formats output clearly
```

---

## Prompt Engineering Tips

### For Better Results

1. **Be Specific:** Include exact requirements (colors, sizes, formats)
2. **Provide Context:** Mention it's for Iris classification
3. **Request Explanations:** Ask for comments and interpretations
4. **Specify Libraries:** Mention sklearn, pandas, matplotlib, etc.
5. **Ask for Professional Styling:** Request titles, labels, legends

### Example Good Prompt Structure

```
[Action Verb] + [What to Create] + [Specific Requirements]

Example:
"Create a confusion matrix visualization for Iris classification using sklearn's
ConfusionMatrixDisplay. Use 'Blues' colormap, show species names as labels,
figure size 10x8, and include title 'Confusion Matrix - Decision Tree'. Add
explanation of how to read the matrix below the plot."
```

### Iterative Refinement

If output isn't perfect:
1. **"Make the plot larger"** → adjusts figure size
2. **"Add gridlines"** → adds grid
3. **"Use different colors"** → changes color scheme
4. **"Add more explanation"** → adds comments/text
5. **"Show as percentage"** → formats numbers

---

## Testing Your Prompts

### Verification Checklist

For each prompt, check:
- [ ] Code runs without errors
- [ ] Output matches expected format
- [ ] Visualizations are clear and professional
- [ ] Comments explain what's happening
- [ ] Results are accurate

### Modification Ideas

Try modifying prompts to:
- Use different colors/styles
- Add more visualizations
- Change model parameters
- Add error handling
- Include more explanations

---

## Prompt Sequences for Complete Project

### Sequence 1: Basic Iris Classifier (30 min)
```
1. Prompt 1 (Setup)
2. Prompt 2 (Load data)
3. Prompt 8 (Train/test split)
4. Prompt 9 (Train model)
5. Prompt 10 (Make predictions)
6. Prompt 11 (Calculate accuracy)
```

### Sequence 2: Full Analysis (90 min)
```
1-6 from Basic, plus:
7. Prompt 3 (EDA)
8. Prompt 13 (Confusion matrix)
9. Prompt 15 (Compare algorithms)
10. Prompt 16 (Visualize comparison)
11. Prompt 17 (Feature importance)
12. Prompt 18 (Summary)
```

### Sequence 3: Production-Ready (2-3 hours)
```
All of Full Analysis, plus:
13. Advanced prompts (cross-validation, tuning)
14. Error handling
15. Documentation
16. Testing with edge cases
```

---

## Common Modifications

### Change Test Size
```
Original: test_size=0.2
Modified: test_size=0.3  # 30% for testing

Ask AI: "Modify the train/test split to use 70/30 instead of 80/20"
```

### Try Different Algorithm
```
Ask AI: "Replace Decision Tree with SVM (Support Vector Machine) and
compare performance to Decision Tree"
```

### Add More Visualizations
```
Ask AI: "Add box plots showing feature distributions by species"
Ask AI: "Create violin plots for all 4 features"
Ask AI: "Add 3D scatter plot using 3 best features"
```

### Improve Styling
```
Ask AI: "Make all plots use a consistent color scheme matching
brand colors: primary=#2C3E50, secondary=#E74C3C, accent=#3498DB"
```

---

## Learning Path Suggestions

### Week 1: Use Provided Prompts
- Run each prompt as-is
- Understand the output
- Read the code generated

### Week 2: Modify Prompts
- Change parameters
- Try different colors/styles
- Add your own requirements

### Week 3: Create Your Own Prompts
- Write prompts from scratch
- Build variations of the project
- Apply to different datasets

### Week 4: Advanced Techniques
- Combine multiple prompts
- Create complex analyses
- Build complete projects

---

## Resources

### Prompt Engineering Guides
- OpenAI Prompt Engineering Guide
- Anthropic Claude Prompting Guide
- Google Gemini Best Practices

### ML Documentation
- [Scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Tutorials](https://matplotlib.org/stable/tutorials/index.html)

---

## Questions?

If your prompts aren't working:
1. Check spelling and syntax
2. Be more specific about requirements
3. Break complex requests into smaller prompts
4. Ask AI to explain what went wrong
5. Try rephrasing the prompt

**Remember:** AI assistants are tools to help you learn faster, not replacements for understanding. Always read and understand the generated code!

---

**Created:** 2026-01-05
**Course:** ML for Engineers - Module 2
**Project:** Iris Classification
**Purpose:** Complete prompt documentation for learning

**Status:** ✅ Ready to use
