# Spam Email Detector Project Rubric

**Total Points:** 75
**Module:** 2 - Classification
**Project:** Spam Email Classifier
**Session:** 2.4
**Target Accuracy:** >90%
**Target Recall:** >85% (catching spam is critical!)

---

## Project Overview

Build a real-world text classification system to detect spam emails. This project introduces natural language processing (NLP) fundamentals and handling imbalanced datasets. Unlike Iris with numerical features, you'll work with text data that requires preprocessing and vectorization.

**Learning Objectives:**
- Preprocess text data for machine learning
- Convert text to numerical features (Bag of Words, TF-IDF)
- Handle imbalanced datasets
- Optimize for precision vs recall tradeoffs
- Test classifier on real-world emails
- Understand spam detection challenges

---

## Grading Criteria

### 1. Text Preprocessing (15 points)

| Points | Criteria |
|--------|----------|
| 14-15 | **Excellent:** Implements comprehensive preprocessing pipeline including: lowercase conversion, punctuation removal, tokenization, stop word removal, handles special characters and numbers appropriately, creates reusable preprocessing function, demonstrates preprocessing on sample emails, explains purpose of each step, handles edge cases (empty strings, special characters) |
| 11-13 | **Good:** Implements most preprocessing steps (lowercase, punctuation, tokenization), basic stop word removal, demonstrates on samples, explains main steps, handles common cases |
| 8-10 | **Adequate:** Implements basic preprocessing (lowercase, basic cleaning), limited stop word handling, minimal demonstration, basic explanations, handles simple cases only |
| 5-7 | **Poor:** Minimal preprocessing (only 1-2 steps), no stop words, no demonstration, unclear explanations, doesn't handle special cases |
| 0-4 | **Failing:** No preprocessing or critical errors that break the pipeline |

**Key Requirements:**
- ✅ Convert text to lowercase
- ✅ Remove punctuation
- ✅ Tokenize (split into words)
- ✅ Remove stop words (common words like 'the', 'is', 'a')
- ✅ Handle numbers and special characters
- ✅ Create function or pipeline for reusability
- ✅ Demonstrate on 3+ sample emails

**Code Example:**
```python
import string
from nltk.corpus import stopwords

def preprocess_text(text):
    # Lowercase
    text = text.lower()

    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Tokenize and remove stop words
    words = text.split()
    words = [w for w in words if w not in stopwords.words('english')]

    return ' '.join(words)
```

---

### 2. Feature Extraction (TF-IDF / Bag of Words) (15 points)

| Points | Criteria |
|--------|----------|
| 14-15 | **Excellent:** Implements both CountVectorizer (Bag of Words) and TF-IDF, compares both approaches with accuracy metrics, understands differences and when to use each, configures parameters appropriately (max_features, min_df, max_df), demonstrates vocabulary size understanding, handles sparse matrices correctly, explains vectorization concept clearly |
| 11-13 | **Good:** Implements both CountVectorizer and TF-IDF, basic comparison, understands main differences, uses some parameters, handles matrices correctly, decent explanation |
| 8-10 | **Adequate:** Implements one vectorization method (Count or TF-IDF) correctly, basic parameter usage, minimal comparison, basic understanding, simple explanation |
| 5-7 | **Poor:** Implements one method with errors, no parameter tuning, no comparison, limited understanding, weak explanation |
| 0-4 | **Failing:** Cannot implement vectorization or critical errors |

**Key Requirements:**
- ✅ Import CountVectorizer and TfidfVectorizer from sklearn
- ✅ Implement Bag of Words (CountVectorizer)
- ✅ Implement TF-IDF (TfidfVectorizer)
- ✅ Compare accuracy of both methods
- ✅ Use parameters: max_features, min_df, max_df (optional but recommended)
- ✅ Understand vocabulary size
- ✅ Explain what vectors represent

**Code Example:**
```python
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

# Bag of Words
vectorizer_bow = CountVectorizer(max_features=3000)
X_bow = vectorizer_bow.fit_transform(emails)

# TF-IDF
vectorizer_tfidf = TfidfVectorizer(max_features=3000)
X_tfidf = vectorizer_tfidf.fit_transform(emails)

print(f"Vocabulary size: {len(vectorizer_tfidf.vocabulary_)}")
```

---

### 3. Model Training & Tuning (20 points)

| Points | Criteria |
|--------|----------|
| 18-20 | **Excellent:** Trains 3+ algorithms (Naive Bayes, Logistic Regression, SVM/Random Forest), achieves >90% accuracy AND >85% recall, implements hyperparameter tuning (GridSearchCV or manual), compares algorithms comprehensively (accuracy, precision, recall, F1, training time), addresses class imbalance (class weights or SMOTE), uses cross-validation, all code runs without errors |
| 15-17 | **Good:** Trains 3 algorithms, achieves >90% accuracy, basic hyperparameter adjustment, good comparison (multiple metrics), acknowledges imbalance, uses train/test split properly |
| 11-14 | **Adequate:** Trains 2 algorithms, achieves 85-90% accuracy, default hyperparameters, basic comparison (accuracy + one metric), basic imbalance handling |
| 6-10 | **Poor:** Trains 1-2 algorithms, below 85% accuracy, no tuning, accuracy-only comparison, ignores imbalance |
| 0-5 | **Failing:** Cannot train models, major errors, or below 75% accuracy |

**Key Requirements:**
- ✅ Implement at least 3 algorithms:
  - Multinomial Naive Bayes (recommended for text)
  - Logistic Regression
  - SVM or Random Forest
- ✅ Achieve >90% accuracy target
- ✅ Achieve >85% recall target
- ✅ Use appropriate parameters for each algorithm
- ✅ Handle class imbalance (check class distribution)
- ✅ Compare all algorithms with multiple metrics
- ✅ Document best performing model

**Recommended Algorithms:**
```python
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

# Naive Bayes (fast, works well with text)
nb_model = MultinomialNB()

# Logistic Regression (good baseline)
lr_model = LogisticRegression(max_iter=1000)

# SVM (powerful but slower)
svm_model = SVC(kernel='linear', probability=True)
```

---

### 4. Evaluation with Confusion Matrix (15 points)

| Points | Criteria |
|--------|----------|
| 14-15 | **Excellent:** Uses precision, recall, F1-score (not just accuracy), creates confusion matrix with professional heatmap visualization, generates classification report, analyzes false positives vs false negatives, discusses precision/recall tradeoff for spam detection, compares metrics across all algorithms, creates ROC curve (optional), provides actionable insights |
| 11-13 | **Good:** Uses precision, recall, F1, confusion matrix with visualization, classification report, analyzes FP/FN, discusses metric importance, compares across algorithms |
| 8-10 | **Adequate:** Uses some metrics beyond accuracy, basic confusion matrix, limited analysis, acknowledges precision/recall importance, basic comparison |
| 5-7 | **Poor:** Primarily uses accuracy, minimal confusion matrix, little analysis, doesn't discuss metric tradeoffs |
| 0-4 | **Failing:** Accuracy only, no confusion matrix, or no proper evaluation |

**Key Requirements:**
- ✅ Calculate precision, recall, F1-score for all models
- ✅ Create confusion matrix for best model
- ✅ Visualize confusion matrix as heatmap
- ✅ Generate classification_report
- ✅ Analyze false positives (ham classified as spam)
- ✅ Analyze false negatives (spam classified as ham)
- ✅ Discuss which error is worse for spam detection
- ✅ Create comparison table of all metrics

**Important for Spam Detection:**
- **False Positives (FP):** Legitimate emails marked as spam (user misses important emails - BAD)
- **False Negatives (FN):** Spam emails that get through (user sees spam - annoying but less critical)
- **Tradeoff:** Usually better to let some spam through than to block legitimate emails

---

### 5. Real-World Testing (10 points)

| Points | Criteria |
|--------|----------|
| 9-10 | **Excellent:** Tests with 20+ custom emails (10+ spam, 10+ ham), creates diverse test cases (obvious spam, subtle spam, business emails, personal emails), displays predictions with confidence scores, analyzes errors (which emails were misclassified and why), tests edge cases (very short emails, all caps, heavy punctuation), provides insights on model strengths and weaknesses |
| 7-8 | **Good:** Tests with 10-15 custom emails (balanced spam/ham), varied test cases, shows predictions and confidence, analyzes some errors, tests a few edge cases |
| 5-6 | **Adequate:** Tests with 5-10 emails, basic variety, shows predictions, minimal error analysis, limited edge cases |
| 3-4 | **Poor:** Tests with 1-5 emails, little variety, predictions only (no confidence), no error analysis |
| 0-2 | **Failing:** No custom testing or only 1-2 emails |

**Key Requirements:**
- ✅ Create at least 20 custom test emails
  - 10+ obvious spam examples
  - 5+ subtle spam examples
  - 10+ legitimate (ham) examples
- ✅ Use model.predict() and model.predict_proba()
- ✅ Display predictions with confidence scores
- ✅ Analyze misclassifications
- ✅ Test edge cases
- ✅ Create function for easy testing

**Example Test Function:**
```python
def test_email(text, vectorizer, model):
    # Preprocess
    clean_text = preprocess_text(text)

    # Vectorize
    vec = vectorizer.transform([clean_text])

    # Predict
    pred = model.predict(vec)[0]
    prob = model.predict_proba(vec)[0]

    # Display
    label = "SPAM" if pred == 1 else "HAM"
    confidence = prob[pred] * 100

    print(f"📧 Email: {text[:50]}...")
    print(f"🏷️  Prediction: {label}")
    print(f"📊 Confidence: {confidence:.1f}%\n")
```

**Example Test Emails:**
```python
# Obvious spam
"FREE MONEY!!! Click here NOW to claim your prize!!!"
"Congratulations! You won $1,000,000 dollars!"
"BUY CHEAP VIAGRA NOW! Limited time offer!!!"

# Subtle spam
"Hi, I'm a prince from Nigeria and need your help transferring funds"
"Your account has been compromised. Click here to verify your information"

# Legitimate emails
"Hi Sarah, can we reschedule our meeting to 3pm tomorrow?"
"Reminder: Project deadline is Friday at 5pm"
"Thanks for your purchase! Your order #12345 will arrive in 3 days"
```

---

## Bonus Points (Optional - Up to +10 points)

### Feature Analysis (+3 points)
- Extract and display most important words for spam vs ham
- Create word clouds for spam and ham classes
- Analyze which words have highest TF-IDF scores for each class
- Provide insights on spam indicators

### Advanced Preprocessing (+2 points)
- Implement stemming or lemmatization
- Handle contractions (don't → do not)
- Remove HTML tags if present
- Compare performance with/without advanced preprocessing

### Hyperparameter Tuning (+3 points)
- Use GridSearchCV or RandomizedSearchCV
- Tune at least 2 algorithms
- Compare tuned vs untuned performance
- Document optimal parameters found

### Cross-Validation (+2 points)
- Implement k-fold cross-validation
- Compare CV scores to single train/test split
- Calculate mean and std of CV scores
- Discuss reliability of results

---

## Code Quality Standards

### Required Elements:
- ✅ **Organization:** Clear sections (imports, preprocessing, vectorization, training, evaluation, testing)
- ✅ **Comments:** Explain complex steps, especially preprocessing and vectorization
- ✅ **Functions:** Create reusable functions for preprocessing and testing
- ✅ **Variable Names:** Descriptive (vectorizer_tfidf, nb_model, spam_emails)
- ✅ **Reproducibility:** Set random_state where applicable
- ✅ **Outputs:** Clear labels, formatted results
- ✅ **Visualizations:** Professional charts with titles and labels

### Deductions for Poor Quality:
- -3 points: No functions, everything in main code block
- -2 points: Poor or no comments
- -2 points: Unclear variable names
- -1 point: No random_state
- -1 point: Poorly formatted output
- -1 point: Unlabeled visualizations

---

## Submission Requirements

### What to Submit:
1. **Jupyter Notebook (.ipynb)** with:
   - All code, outputs, and visualizations
   - Markdown explanations of approach
   - Analysis of results

2. **Brief Report** (can be markdown in notebook):
   - Best model and metrics achieved
   - Comparison of Bag of Words vs TF-IDF
   - Analysis of false positives vs false negatives
   - Insights on spam detection challenges
   - Recommendations for improvement

3. **Test Email Collection:**
   - At least 20 custom test emails
   - Documented in code or separate file

### File Naming:
- `spam-detector-[YourName].ipynb`
- Example: `spam-detector-marcus-johnson.ipynb`

### Pre-Submission Checklist:
- [ ] All code runs without errors (Kernel → Restart & Run All)
- [ ] Achieves >90% accuracy and >85% recall
- [ ] At least 3 algorithms implemented
- [ ] Confusion matrix and classification report included
- [ ] 20+ custom emails tested
- [ ] Both CountVectorizer and TF-IDF implemented
- [ ] Preprocessing pipeline complete
- [ ] All visualizations display correctly
- [ ] Code is well-organized and commented

---

## Common Mistakes to Avoid

❌ **Fitting vectorizer on test data** - Only fit on training data, transform test data
❌ **Not handling imbalanced classes** - Check class distribution, use appropriate metrics
❌ **Using accuracy alone** - Precision and recall are critical for spam detection
❌ **No text preprocessing** - Raw text performs poorly, always preprocess
❌ **Overfitting to test set** - Don't tune based on test performance
❌ **Not testing with real emails** - Essential for validating practical usefulness
❌ **Ignoring false positives** - Blocking legitimate email is worse than letting spam through
❌ **Forgetting to handle sparse matrices** - TF-IDF produces sparse matrices

---

## Grading Summary

| Category | Points | Your Score |
|----------|--------|------------|
| Text Preprocessing | 15 | |
| Feature Extraction (Vectorization) | 15 | |
| Model Training & Tuning | 20 | |
| Evaluation with Confusion Matrix | 15 | |
| Real-World Testing | 10 | |
| **Subtotal** | **75** | |
| Bonus (Optional) | +10 max | |
| Code Quality Deductions | Up to -10 | |
| **TOTAL** | **75** | |

**Passing Score:** 53/75 (70%)
**Target Score:** 60/75 (80%)
**Excellence Score:** 68+/75 (90%+)

---

## Success Criteria

### Minimum Requirements (Pass - 53/75):
- ✅ Basic text preprocessing (lowercase, punctuation)
- ✅ Implement one vectorization method
- ✅ Train 2 classification algorithms
- ✅ Achieve >85% accuracy
- ✅ Basic confusion matrix
- ✅ Test with 10+ custom emails

### Target Performance (B - 60/75):
- All minimum requirements, plus:
- ✅ Complete preprocessing pipeline
- ✅ Both CountVectorizer and TF-IDF
- ✅ Train 3 algorithms
- ✅ Achieve >90% accuracy and >85% recall
- ✅ Comprehensive evaluation (precision, recall, F1)
- ✅ Test with 20+ custom emails
- ✅ Good code organization

### Excellent Performance (A - 68+/75):
- All target requirements, plus:
- ✅ Advanced preprocessing (stop words, stemming)
- ✅ Hyperparameter tuning
- ✅ Feature analysis (word importance)
- ✅ Thorough error analysis
- ✅ Professional visualizations
- ✅ Outstanding code quality
- ✅ Actionable insights

---

## Dataset Information

**Recommended Dataset:** SMS Spam Collection
- 5,574 messages
- 13.4% spam, 86.6% ham (imbalanced!)
- Available from UCI ML Repository
- Can also use Kaggle spam datasets

**Alternative:** Create your own dataset by collecting emails (ensure privacy compliance)

---

## Resources

### Documentation:
- [CountVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html)
- [TfidfVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html)
- [Multinomial Naive Bayes](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.MultinomialNB.html)
- [NLTK Stop Words](https://www.nltk.org/api/nltk.corpus.html)

### Helpful Tutorials:
- Session 2.4 Video: "Email Spam Detection"
- Module 2 Framework: Text Classification section

---

**Created:** 2026-01-06
**Version:** 1.0
**Course:** ML for Engineers - Module 2
**Last Updated:** 2026-01-06
