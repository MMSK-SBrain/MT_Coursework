# Heart Disease Prediction Project Rubric

**Total Points:** 75
**Module:** 2 - Classification
**Project:** Heart Disease Predictor (Healthcare ML)
**Session:** 2.6
**Target AUC:** >0.85
**Critical Metric:** Recall >85% (catching disease cases is life-critical!)

---

## Project Overview

Build a medical diagnosis support system to predict heart disease presence based on clinical measurements. This project introduces healthcare-specific ML challenges: high stakes, ethical considerations, model interpretability requirements, and optimizing for recall (minimizing false negatives where missing a disease case could be life-threatening).

**Learning Objectives:**
- Work with medical/clinical data
- Understand high-stakes ML applications
- Master ROC curves and AUC metrics
- Prioritize recall over accuracy in critical domains
- Build interpretable models for healthcare
- Consider ethical implications of ML in medicine
- Handle class imbalance in medical contexts

**⚠️ IMPORTANT DISCLAIMER:**
This is an educational exercise. Real medical ML systems require:
- Clinical validation studies
- FDA/regulatory approval
- Healthcare professional oversight
- Rigorous testing beyond this scope
- Never use for actual medical decisions

---

## Grading Criteria

### 1. Data Exploration with Medical Context (10 points)

| Points | Criteria |
|--------|----------|
| 9-10 | **Excellent:** Loads data correctly, comprehensive EDA with medical context understanding, analyzes all features with clinical interpretation (e.g., "trestbps is resting blood pressure, normal range 120/80"), identifies normal vs abnormal ranges, visualizes feature distributions with medical thresholds, checks class distribution, analyzes correlation with medical relevance, identifies missing values and outliers with clinical perspective, documents medical significance of features |
| 7-8 | **Good:** Loads data correctly, good EDA with some medical context, analyzes features with basic clinical understanding, visualizes distributions, checks class distribution, handles missing values appropriately |
| 5-6 | **Adequate:** Loads data, basic EDA without much medical context, analyzes features statistically only, basic visualizations, checks class distribution |
| 3-4 | **Poor:** Loads data, minimal EDA, no medical context, limited analysis, poor handling of missing values |
| 0-2 | **Failing:** Cannot load data or no meaningful exploration |

**Key Requirements:**
- ✅ Load heart disease dataset (UCI Heart Disease or similar)
- ✅ Research and document each feature's medical meaning
- ✅ Identify normal vs abnormal ranges for key features
- ✅ Visualize feature distributions with medical thresholds
- ✅ Analyze class distribution (disease present vs absent)
- ✅ Check for missing values and outliers
- ✅ Explore correlations between clinical features
- ✅ Provide medical context for observations

**Expected Features (UCI Heart Disease Dataset):**
```
1. age: Age in years
2. sex: 1 = male, 0 = female
3. cp: Chest pain type (4 types: typical angina, atypical, non-anginal, asymptomatic)
4. trestbps: Resting blood pressure (mm Hg) - Normal: <120
5. chol: Serum cholesterol (mg/dl) - Normal: <200
6. fbs: Fasting blood sugar >120 mg/dl (1=true, 0=false)
7. restecg: Resting ECG results (0-2)
8. thalach: Maximum heart rate achieved - Normal: 220-age
9. exang: Exercise induced angina (1=yes, 0=no)
10. oldpeak: ST depression induced by exercise
11. slope: Slope of peak exercise ST segment
12. ca: Number of major vessels colored by fluoroscopy (0-3)
13. thal: Thalassemia (3=normal, 6=fixed defect, 7=reversible)
14. target: Heart disease (1=yes, 0=no)
```

**Medical Context Example:**
```python
# Analyze blood pressure distribution
plt.figure(figsize=(10, 5))
plt.hist(df['trestbps'], bins=30, alpha=0.7)
plt.axvline(120, color='green', linestyle='--', label='Normal threshold (120)')
plt.axvline(140, color='orange', linestyle='--', label='Hypertension Stage 1 (140)')
plt.axvline(180, color='red', linestyle='--', label='Hypertension Stage 2 (180)')
plt.xlabel('Resting Blood Pressure (mm Hg)')
plt.ylabel('Count')
plt.title('Blood Pressure Distribution with Medical Thresholds')
plt.legend()
plt.show()

# Observation: "58% of patients have BP >130, indicating high prevalence
# of hypertension in this population"
```

---

### 2. Data Preprocessing & Feature Engineering (10 points)

| Points | Criteria |
|--------|----------|
| 9-10 | **Excellent:** Handles categorical variables appropriately (one-hot encoding for chest pain type, thalassemia), scales numerical features using StandardScaler, creates clinically meaningful engineered features (age groups, BP categories, pulse pressure, etc.), justifies feature engineering with medical literature or reasoning, handles missing values appropriately for medical context, validates feature distributions after transformation |
| 7-8 | **Good:** Handles categorical variables correctly, scales numerical features, creates 1-2 engineered features with medical justification, appropriate missing value handling |
| 5-6 | **Adequate:** Basic categorical encoding, basic scaling, minimal feature engineering, basic missing value handling |
| 3-4 | **Poor:** Incomplete preprocessing, no feature engineering, poor handling of categorical or missing data |
| 0-2 | **Failing:** Critical preprocessing errors that break the model |

**Key Requirements:**
- ✅ Handle categorical variables (cp, restecg, slope, thal)
- ✅ Scale numerical features (age, trestbps, chol, thalach, oldpeak)
- ✅ Create at least 2 medically meaningful engineered features
- ✅ Handle missing values (if any) appropriately
- ✅ Document preprocessing decisions
- ✅ Validate preprocessing results

**Recommended Feature Engineering:**
```python
# Age risk categories (heart disease risk increases with age)
df['age_group'] = pd.cut(df['age'],
                         bins=[0, 40, 55, 70, 100],
                         labels=['<40', '40-55', '55-70', '70+'])

# Blood pressure categories
df['bp_category'] = pd.cut(df['trestbps'],
                           bins=[0, 120, 140, 180, 300],
                           labels=['Normal', 'Elevated', 'Stage1_HTN', 'Stage2_HTN'])

# Cholesterol risk
df['high_cholesterol'] = (df['chol'] > 200).astype(int)

# Pulse pressure (systolic - diastolic, marker of arterial stiffness)
# Note: If diastolic is available
df['pulse_pressure'] = df['trestbps'] - df['diasbp']  # if available

# Exercise capacity (max HR as % of age-predicted max)
df['hr_reserve'] = df['thalach'] / (220 - df['age'])

# Multiple risk factors count
risk_factors = ['fbs', 'high_cholesterol', 'exang']  # Add more
df['risk_factor_count'] = df[risk_factors].sum(axis=1)
```

---

### 3. Model Training with Focus on Recall (20 points)

| Points | Criteria |
|--------|----------|
| 18-20 | **Excellent:** Trains 3+ algorithms, explicitly optimizes for recall (using class_weight, threshold adjustment, or SMOTE), achieves >85% recall target, achieves AUC >0.85, implements cross-validation, handles class imbalance appropriately for medical context, compares algorithms on multiple metrics (accuracy, precision, recall, F1, AUC), creates comprehensive comparison visualizations, discusses recall vs precision tradeoff in medical context, all code runs correctly |
| 15-17 | **Good:** Trains 3 algorithms, optimizes for recall, achieves recall >80% and AUC >0.80, uses cross-validation, handles imbalance, compares on multiple metrics, discusses medical tradeoffs |
| 11-14 | **Adequate:** Trains 2 algorithms, acknowledges recall importance, achieves recall >75%, basic comparison, basic imbalance handling |
| 6-10 | **Poor:** Trains 1-2 algorithms, doesn't prioritize recall, below targets, minimal comparison, ignores imbalance |
| 0-5 | **Failing:** Cannot train models, major errors, far below targets |

**Key Requirements:**
- ✅ Train at least 3 algorithms:
  - Logistic Regression
  - Random Forest
  - Gradient Boosting or SVM
- ✅ Explicitly optimize for recall (medical priority)
- ✅ Achieve recall >85% target
- ✅ Achieve AUC >0.85 target
- ✅ Use stratified k-fold cross-validation
- ✅ Handle class imbalance
- ✅ Compare comprehensively across metrics
- ✅ Document why recall matters in healthcare

**Optimizing for Recall:**
```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

# Method 1: Class weights (penalize false negatives more)
rf_model = RandomForestClassifier(
    n_estimators=100,
    class_weight={0: 1, 1: 3},  # 3x penalty for missing disease
    random_state=42
)

# Method 2: Adjust decision threshold
# Instead of 0.5, use 0.3 to catch more disease cases
probs = model.predict_proba(X_test)[:, 1]
predictions = (probs > 0.3).astype(int)

# Method 3: Focus on recall in cross-validation
recall_scores = cross_val_score(model, X_train, y_train,
                                cv=5, scoring='recall')
print(f"Cross-val Recall: {recall_scores.mean():.3f} ± {recall_scores.std():.3f}")

# Calculate cost-sensitive metric
def medical_score(y_true, y_pred):
    # False negative (missing disease) is 10x worse than false positive
    tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()
    cost = fp * 1 + fn * 10  # Weight false negatives heavily
    return -cost  # Negative because we want to minimize cost
```

**Medical Context Discussion:**
```
In heart disease prediction:
- False Negative (FN): Patient has disease but we miss it → VERY BAD (could be fatal)
- False Positive (FP): Patient doesn't have disease but we flag them → Acceptable (leads to more tests)

Therefore:
- Prioritize RECALL (sensitivity) - catch all true disease cases
- Accept lower PRECISION - some false alarms are acceptable
- Target: Recall >85%, even if precision is 60-70%
```

---

### 4. ROC Curve & AUC Analysis (15 points)

| Points | Criteria |
|--------|----------|
| 14-15 | **Excellent:** Creates professional ROC curves for all models on same plot, calculates and displays AUC for each, explains ROC curve meaning (TPR vs FPR), interprets AUC values in medical context, identifies optimal operating point considering medical costs, compares ROC curves across algorithms, discusses threshold selection for medical application, creates precision-recall curve as complement, provides clear insights for clinical use |
| 11-13 | **Good:** Creates ROC curves for all models, calculates AUC, explains ROC and AUC meaning, interprets in medical context, identifies reasonable operating point, compares algorithms |
| 8-10 | **Adequate:** Creates ROC curve for best model, calculates AUC, basic explanation, limited medical context, basic comparison |
| 5-7 | **Poor:** Basic ROC curve, AUC calculation, minimal explanation, no medical context |
| 0-4 | **Failing:** No ROC curve or incorrect implementation |

**Key Requirements:**
- ✅ Create ROC curve for all trained models
- ✅ Calculate AUC for each model
- ✅ Plot all ROC curves on same figure for comparison
- ✅ Explain what ROC curve shows
- ✅ Interpret AUC in medical context
- ✅ Identify optimal threshold point
- ✅ Discuss threshold selection for clinical use
- ✅ (Optional) Create precision-recall curve

**ROC Curve Implementation:**
```python
from sklearn.metrics import roc_curve, roc_auc_score, auc
import matplotlib.pyplot as plt

# Calculate ROC for each model
plt.figure(figsize=(10, 8))

models = {
    'Logistic Regression': lr_model,
    'Random Forest': rf_model,
    'Gradient Boosting': gb_model
}

for name, model in models.items():
    # Get probability predictions
    y_probs = model.predict_proba(X_test)[:, 1]

    # Calculate ROC curve
    fpr, tpr, thresholds = roc_curve(y_test, y_probs)

    # Calculate AUC
    auc_score = roc_auc_score(y_test, y_probs)

    # Plot
    plt.plot(fpr, tpr, label=f'{name} (AUC = {auc_score:.3f})')

# Plot diagonal (random classifier)
plt.plot([0, 1], [0, 1], 'k--', label='Random Classifier (AUC = 0.5)')

# Formatting
plt.xlabel('False Positive Rate (1 - Specificity)')
plt.ylabel('True Positive Rate (Sensitivity/Recall)')
plt.title('ROC Curves - Heart Disease Prediction')
plt.legend(loc='lower right')
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

print(f"\nAUC Interpretation:")
print(f"0.5 = Random guessing")
print(f"0.7-0.8 = Acceptable")
print(f"0.8-0.9 = Excellent")
print(f">0.9 = Outstanding (rare in medical ML)")
```

**Threshold Selection for Medical Use:**
```python
# Find threshold that gives recall >85%
fpr, tpr, thresholds = roc_curve(y_test, y_probs)

# Find threshold where TPR (recall) >= 0.85
target_recall = 0.85
idx = np.argmax(tpr >= target_recall)
optimal_threshold = thresholds[idx]

print(f"\nOptimal Threshold for Medical Use:")
print(f"Threshold: {optimal_threshold:.3f}")
print(f"Recall (Sensitivity): {tpr[idx]:.3f}")
print(f"Specificity: {1-fpr[idx]:.3f}")
print(f"This means: We catch {tpr[idx]*100:.1f}% of disease cases,")
print(f"at the cost of {fpr[idx]*100:.1f}% false alarm rate")
```

---

### 5. Model Interpretability & Feature Importance (10 points)

| Points | Criteria |
|--------|----------|
| 9-10 | **Excellent:** Extracts and visualizes feature importance from tree-based model, identifies top 10 clinical predictors, interprets findings with medical literature references or reasoning, compares feature importance across algorithms, discusses clinical validity of important features, identifies surprising or counterintuitive findings, creates professional visualizations, provides insights useful for clinicians |
| 7-8 | **Good:** Extracts feature importance, identifies top predictors, interprets with medical reasoning, compares across some algorithms, good visualizations, useful insights |
| 5-6 | **Adequate:** Basic feature importance extraction, identifies predictors, limited medical interpretation, basic visualization |
| 3-4 | **Poor:** Minimal feature analysis, no medical interpretation, poor visualization |
| 0-2 | **Failing:** No interpretability analysis |

**Key Requirements:**
- ✅ Extract feature importance from Random Forest or Gradient Boosting
- ✅ Identify top 10 predictive features
- ✅ Interpret in medical context
- ✅ Create professional visualizations
- ✅ Discuss clinical validity
- ✅ Compare with medical literature (if known)

**Feature Importance Analysis:**
```python
# Extract from Random Forest
importances = rf_model.feature_importances_
feature_names = X_train.columns

importance_df = pd.DataFrame({
    'Feature': feature_names,
    'Importance': importances,
    'Clinical_Meaning': [
        'Patient age',
        'Resting blood pressure',
        'Max heart rate achieved',
        # ... add meanings for all features
    ]
}).sort_values('Importance', ascending=False)

# Visualize
plt.figure(figsize=(12, 8))
top_10 = importance_df.head(10)
plt.barh(range(len(top_10)), top_10['Importance'])
plt.yticks(range(len(top_10)), top_10['Feature'])
plt.xlabel('Importance Score')
plt.title('Top 10 Clinical Predictors of Heart Disease')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()

# Medical interpretation
print("\nClinical Insights:")
print(f"1. {top_10.iloc[0]['Feature']}: Most predictive feature")
print(f"   Medical relevance: {top_10.iloc[0]['Clinical_Meaning']}")
print(f"   This aligns with medical literature showing [reasoning]...")
```

---

### 6. Ethical Considerations & Clinical Deployment (10 points)

| Points | Criteria |
|--------|----------|
| 9-10 | **Excellent:** Discusses multiple ethical considerations (bias, fairness across demographics, transparency, patient autonomy), analyzes performance across subgroups (age, sex), identifies potential biases in data or model, discusses need for clinical validation, outlines deployment requirements (regulatory approval, clinician oversight, patient consent), considers consequences of errors, discusses model limitations clearly, provides responsible AI recommendations |
| 7-8 | **Good:** Discusses key ethical considerations, checks for demographic bias, identifies limitations, discusses deployment needs, considers error consequences |
| 5-6 | **Adequate:** Mentions some ethical considerations, basic bias check, acknowledges limitations, basic deployment discussion |
| 3-4 | **Poor:** Minimal ethical discussion, no bias analysis, limited limitations discussion |
| 0-2 | **Failing:** No ethical considerations or deployment discussion |

**Key Requirements:**
- ✅ Discuss at least 3 ethical considerations
- ✅ Analyze model performance across demographics (age groups, sex)
- ✅ Identify potential biases
- ✅ Discuss clinical validation needs
- ✅ Outline deployment requirements
- ✅ Consider consequences of false negatives and false positives
- ✅ State model limitations clearly

**Ethical Analysis Example:**
```python
# Check performance across demographics

# By gender
print("Performance by Gender:")
for gender in [0, 1]:
    mask = X_test_original['sex'] == gender
    if mask.sum() > 0:
        acc = accuracy_score(y_test[mask], predictions[mask])
        rec = recall_score(y_test[mask], predictions[mask])
        print(f"  {'Female' if gender==0 else 'Male'}: Accuracy={acc:.3f}, Recall={rec:.3f}")

# By age group
print("\nPerformance by Age Group:")
for age_group in ['<50', '50-60', '60+']:
    mask = X_test_original['age_group'] == age_group
    if mask.sum() > 0:
        rec = recall_score(y_test[mask], predictions[mask])
        print(f"  {age_group}: Recall={rec:.3f}")

# Ethical discussion
print("\nETHICAL CONSIDERATIONS:")
print("1. Bias: Model shows lower recall for women (68% vs 88% for men)")
print("   Action: Collect more female patient data, consider separate models")
print("")
print("2. Transparency: Clinicians need to understand why prediction was made")
print("   Action: Provide feature importance with each prediction")
print("")
print("3. Patient Autonomy: Patients should understand AI is involved")
print("   Action: Informed consent, clear explanation of AI role")
print("")
print("4. Clinical Validation: This model is NOT validated for medical use")
print("   Action: Requires clinical trials, regulatory approval before deployment")
print("")
print("5. Consequence of Errors:")
print("   - False Negative: Patient with disease missed → Further testing needed")
print("   - False Positive: Healthy patient flagged → Additional tests (acceptable)")
```

---

## Bonus Points (Optional - Up to +10 points)

### SHAP Values for Individual Predictions (+4 points)
- Implement SHAP (SHapley Additive exPlanations)
- Show why specific patients were flagged
- Create SHAP force plots and summary plots
- Explain predictions in clinically meaningful terms

### Comprehensive Bias Analysis (+3 points)
- Statistical analysis of bias across all demographic groups
- Fairness metrics (equalized odds, demographic parity)
- Recommendations for bias mitigation
- Discussion of healthcare ML bias literature

### Precision-Recall Curve (+2 points)
- Create precision-recall curve (complement to ROC)
- Explain when PR curve is more informative
- Identify optimal threshold on PR curve
- Compare with ROC insights

### Clinical Decision Support Tool (+1 point)
- Create simple function that takes patient data and outputs risk assessment
- Include confidence scores and top risk factors
- Format output for clinical use

---

## Grading Summary

| Category | Points | Your Score |
|----------|--------|------------|
| Data Exploration with Medical Context | 10 | |
| Data Preprocessing & Feature Engineering | 10 | |
| Model Training with Focus on Recall | 20 | |
| ROC Curve & AUC Analysis | 15 | |
| Model Interpretability | 10 | |
| Ethical Considerations & Deployment | 10 | |
| **Subtotal** | **75** | |
| Bonus (Optional) | +10 max | |
| Code Quality Deductions | Up to -10 | |
| **TOTAL** | **75** | |

**Passing Score:** 53/75 (70%)
**Target Score:** 60/75 (80%)
**Excellence Score:** 68+/75 (90%+)

---

## Common Mistakes to Avoid

❌ **Prioritizing accuracy over recall** - In medical ML, catching disease is critical
❌ **No medical context** - This is clinical data, understand what features mean
❌ **Ignoring class imbalance** - Medical datasets are often imbalanced
❌ **Not checking for bias** - Healthcare ML can perpetuate health disparities
❌ **Using as medical advice** - This is education only, not for real diagnosis
❌ **No interpretability** - Clinicians need to understand why predictions are made
❌ **Forgetting ethical considerations** - Healthcare ML has life-or-death implications
❌ **Not discussing limitations** - All models have limitations, state them clearly

---

## Dataset Information

**Recommended Dataset:** UCI Heart Disease Dataset
- Source: UCI Machine Learning Repository
- 303 patients from Cleveland Clinic
- 14 attributes (13 features + 1 target)
- ~54% have heart disease
- Features include clinical and test results

**Download:**
- UCI ML Repository: "Heart Disease Data Set"
- Kaggle: "Heart Disease UCI"

**Data Quality Notes:**
- Some missing values (ca, thal)
- Relatively small dataset (303 samples)
- From single medical center (potential bias)
- Collected in 1980s (medical practice has evolved)

---

## Submission Requirements

### What to Submit:
1. **Jupyter Notebook (.ipynb)** with complete analysis
2. **Medical Report** (markdown in notebook):
   - Model performance summary
   - Top clinical predictors identified
   - Recommended decision threshold
   - Ethical considerations
   - Limitations and warnings
   - NOT FOR CLINICAL USE disclaimer

### Pre-Submission Checklist:
- [ ] All code runs without errors
- [ ] AUC >0.85 achieved
- [ ] Recall >85% achieved
- [ ] ROC curves for all models
- [ ] Feature importance analyzed
- [ ] Medical context provided for all features
- [ ] Ethical considerations discussed
- [ ] Bias analysis performed
- [ ] Clear limitations stated
- [ ] Disclaimer about non-clinical use included

---

## Resources

### Documentation:
- [ROC Curve](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_curve.html)
- [AUC Score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html)
- [Class Weights](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)

### Medical ML Ethics:
- "Artificial Intelligence in Healthcare" (Nature Medicine)
- "Fairness in Machine Learning for Healthcare" (WHO guidelines)
- FDA guidance on AI/ML in medical devices

---

**⚠️ FINAL DISCLAIMER:**

This project is for **educational purposes only**. The model is NOT:
- Clinically validated
- FDA approved
- Suitable for medical decisions
- A replacement for professional medical diagnosis

Real medical ML requires extensive validation, regulatory approval, and clinical oversight.

---

**Created:** 2026-01-06
**Version:** 1.0
**Course:** ML for Engineers - Module 2
**Last Updated:** 2026-01-06
