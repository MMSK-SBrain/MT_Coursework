# Module 6 Project Rubrics
## Neural Networks & Deep Learning

---

## Session Projects (Sessions 1-5)

### General Session Project Rubric (15 points each)

| Category | Excellent (5) | Good (3-4) | Needs Improvement (1-2) | Points |
|----------|---------------|------------|-------------------------|--------|
| **Implementation (5 pts)** | Code runs without errors, all requirements met, clean code | Code runs with minor issues, most requirements met | Multiple errors, missing requirements | /5 |
| **Target Achievement (5 pts)** | Meets or exceeds accuracy target | Within 2-3% of target | >5% below target | /5 |
| **Visualizations (3 pts)** | All required plots, clear and professional | Most plots present, adequate quality | Missing plots or poor quality | /3 |
| **Documentation (2 pts)** | Clear comments, markdown explanations | Basic documentation | Minimal or no documentation | /2 |

**Total: /15 points per session project**

---

## Session-Specific Requirements

### Session 1: Iris Neural Network (15 points)

**Requirements:**
- ✅ Load Iris dataset
- ✅ Build simple NN (input → hidden → output)
- ✅ Train and evaluate
- ✅ Compare to Decision Tree
- ✅ Achieve 95%+ accuracy
- ✅ Training curves visualization
- ✅ NN vs Traditional ML comparison

**Scoring:**
- Implementation: 5 pts (model builds and trains)
- Accuracy: 5 pts (95%+ = 5, 90-94% = 3, <90% = 1)
- Visualizations: 3 pts (training curves, comparison chart)
- Documentation: 2 pts (insights on when to use NN vs ML)

---

### Session 2: MNIST Baseline (15 points)

**Requirements:**
- ✅ Load and preprocess MNIST
- ✅ Build Dense NN (784 → 128 → 64 → 10)
- ✅ Train for 10 epochs
- ✅ Achieve >95% test accuracy
- ✅ Confusion matrix
- ✅ Training/validation curves
- ✅ Misclassified examples visualization

**Scoring:**
- Implementation: 5 pts (proper preprocessing, model architecture)
- Accuracy: 5 pts (>95% = 5, 93-95% = 4, 90-92% = 3, <90% = 1)
- Visualizations: 3 pts (curves, confusion matrix, examples)
- Documentation: 2 pts (explain architecture choices)

---

### Session 3: Fashion MNIST Training (15 points)

**Requirements:**
- ✅ Systematic experiments (batch size, learning rate, optimizers)
- ✅ Early stopping implementation
- ✅ Achieve >85% accuracy
- ✅ Experiment comparison charts
- ✅ Best model saved

**Scoring:**
- Implementation: 5 pts (all experiments run successfully)
- Accuracy: 5 pts (>85% = 5, 82-85% = 4, 80-82% = 3, <80% = 1)
- Visualizations: 3 pts (experiment comparisons, training curves)
- Documentation: 2 pts (analysis of experiment results)

---

### Session 4: MNIST Optimized (15 points)

**Requirements:**
- ✅ Baseline model (from Session 2)
- ✅ Add Dropout regularization
- ✅ Add Batch Normalization
- ✅ Learning rate scheduling
- ✅ Early stopping
- ✅ Achieve >98% accuracy
- ✅ Before/after comparison

**Scoring:**
- Implementation: 5 pts (all regularization techniques applied)
- Accuracy: 5 pts (>98% = 5, 97-98% = 4, 96-97% = 3, <96% = 1)
- Visualizations: 3 pts (baseline vs optimized comparison)
- Documentation: 2 pts (explain impact of each technique)

---

### Session 5: Transfer Learning (15 points)

**Requirements:**
- ✅ Load pre-trained model (VGG16)
- ✅ Feature extraction phase (frozen base)
- ✅ Fine-tuning phase
- ✅ Achieve >90% accuracy
- ✅ Training curves for both phases
- ✅ Comparison to training from scratch (if applicable)

**Scoring:**
- Implementation: 5 pts (proper freezing/unfreezing, correct LR)
- Accuracy: 5 pts (>90% = 5, 85-90% = 4, 80-85% = 3, <80% = 1)
- Visualizations: 3 pts (both phases visualized, comparisons)
- Documentation: 2 pts (explain transfer learning benefits)

---

## CAPSTONE PROJECT: Stock Predictor with Neural Networks (100 points)

### Overview
Build BOTH LSTM and Dense neural networks for stock prediction and compare to traditional ML from Module 3.

### Detailed Rubric

#### 1. Data Preparation (15 points)

| Criteria | Points | Description |
|----------|--------|-------------|
| Data loading | 3 | Successfully load stock data (Module 3 or new) |
| Feature engineering | 5 | Apply technical indicators using Module 3 library |
| Proper scaling | 3 | StandardScaler for features, proper handling for target |
| Time series split | 4 | No data leakage, chronological split |

**Total Data Prep: /15**

---

#### 2. LSTM Network Implementation (20 points)

| Criteria | Points | Description |
|----------|--------|-------------|
| Sequence creation | 5 | Create proper sequences (e.g., 60-day windows) |
| LSTM architecture | 7 | 2+ LSTM layers, appropriate Dense layers, proper output |
| Training | 5 | Use callbacks (EarlyStopping, ReduceLR), train successfully |
| Model saved | 3 | Save trained LSTM model (.h5) |

**Total LSTM: /20**

---

#### 3. Dense Network Implementation (15 points)

| Criteria | Points | Description |
|----------|--------|-------------|
| Architecture | 7 | 3-4 hidden layers with decreasing size (e.g., 256→128→64→32) |
| Regularization | 5 | Dropout and Batch Normalization applied |
| Training | 3 | Successful training with callbacks |

**Total Dense NN: /15**

---

#### 4. Traditional ML Baseline (15 points)

| Criteria | Points | Description |
|----------|--------|-------------|
| Random Forest | 5 | Train RF regressor on same data |
| Linear Regression | 3 | Train linear regression baseline |
| Proper evaluation | 7 | Calculate MAE, RMSE, R² for both |

**Total Traditional ML: /15**

---

#### 5. Comprehensive Comparison (20 points)

| Criteria | Points | Description |
|----------|--------|-------------|
| Performance metrics | 8 | MAE, RMSE, R² for all 4 models (LR, RF, Dense NN, LSTM) |
| Visualization | 7 | Comparison charts (bar charts, actual vs predicted plots) |
| Statistical analysis | 5 | Identify best model, quantify improvements |

**Total Comparison: /20**

---

#### 6. Insights and Decision Framework (10 points)

| Criteria | Points | Description |
|----------|--------|-------------|
| When-to-use guide | 5 | Clear decision framework for NN vs Traditional ML |
| Stock prediction insights | 3 | Specific insights for stock/time series prediction |
| Recommendations | 2 | Practical recommendations for real-world use |

**Total Insights: /10**

---

#### 7. Code Quality and Documentation (5 points)

| Criteria | Points | Description |
|----------|--------|-------------|
| Code organization | 2 | Clean, organized, commented code |
| Markdown explanations | 2 | Clear explanations throughout notebook |
| Reproducibility | 1 | Set random seeds, clear instructions |

**Total Quality: /5**

---

### Capstone Performance Targets

| Model | Target R² | Excellent | Good | Acceptable | Needs Work |
|-------|-----------|-----------|------|------------|------------|
| Linear Regression | Baseline | >0.65 | 0.60-0.65 | 0.50-0.60 | <0.50 |
| Random Forest | >0.70 | >0.75 | 0.70-0.75 | 0.65-0.70 | <0.65 |
| Dense NN | >0.70 | >0.75 | 0.70-0.75 | 0.65-0.70 | <0.65 |
| LSTM | >0.70 | >0.75 | 0.70-0.75 | 0.65-0.70 | <0.65 |

**Grading Scale:**
- 90-100: Excellent - All models train successfully, R² >0.70, comprehensive analysis
- 80-89: Good - Models work well, R² 0.65-0.70, good comparison
- 70-79: Acceptable - Models run, R² 0.60-0.65, basic comparison
- <70: Needs Improvement - Issues with implementation or performance

---

## Capstone Scoring Breakdown

### Example Scoring

**Student achieves:**
- Data Prep: 14/15 (minor issue with scaling)
- LSTM: 18/20 (sequence creation could be better)
- Dense NN: 15/15 (perfect implementation)
- Traditional ML: 14/15 (missing one metric)
- Comparison: 18/20 (good charts, could analyze more deeply)
- Insights: 9/10 (excellent decision framework)
- Code Quality: 5/5 (clean, well-documented)

**Total: 93/100 (Excellent, Grade: A)**

---

## Key Success Criteria

### To Pass (70+):
✅ All models train without errors
✅ At least 2 models achieve R² >0.65
✅ Basic comparison completed
✅ Decision framework provided

### For Excellence (90+):
✅ All models achieve R² >0.70
✅ Comprehensive comparison with visualizations
✅ Deep insights and analysis
✅ Professional code quality
✅ Clear demonstration of NN vs Traditional ML tradeoffs

---

## Common Mistakes to Avoid

### Critical Errors (Major Point Deductions):
❌ **Data Leakage** - Shuffling time series data (-10 pts)
❌ **No Feature Scaling** - NNs train poorly (-5 pts)
❌ **Wrong Loss Function** - Using classification loss for regression (-5 pts)
❌ **No Validation** - Training without validation split (-5 pts)
❌ **Unfair Comparison** - Comparing models trained on different data (-10 pts)

### Style Issues (Minor Deductions):
⚠️ Missing documentation (-1 to -2 pts)
⚠️ No random seeds (not reproducible) (-1 pt)
⚠️ Poor code organization (-1 to -2 pts)
⚠️ Missing visualizations (-1 pt each)

---

## Bonus Points (Optional, up to +10)

**+5 points:** Implement ensemble method (combine NN + RF predictions)
**+3 points:** Try additional architectures (GRU, Bidirectional LSTM)
**+2 points:** Deploy model as Streamlit app

---

## Submission Requirements

### Required Files:
1. `stock-predictor-neural-network.ipynb` (main notebook)
2. `stock_predictor_lstm.h5` (saved LSTM model)
3. `stock_predictor_dense_nn.h5` (saved Dense model)
4. `stock_predictor_rf.pkl` (saved Random Forest)
5. `scalers.pkl` (saved scalers)

### Optional Files:
- `stock-predictor-summary.pdf` (executive summary)
- `requirements.txt` (dependencies)
- `README.md` (project documentation)

---

## Self-Assessment Checklist

Before submitting, verify:

**Data Preparation:**
- [ ] Data loaded correctly
- [ ] Features engineered using Module 3 library
- [ ] Proper time series split (no shuffle!)
- [ ] Features scaled for NNs

**LSTM Implementation:**
- [ ] Sequences created correctly
- [ ] Model architecture appropriate
- [ ] Trains without errors
- [ ] Achieves R² >0.70

**Dense NN Implementation:**
- [ ] Architecture suitable for tabular data
- [ ] Regularization applied
- [ ] Trains successfully

**Traditional ML:**
- [ ] Random Forest trained
- [ ] Linear Regression trained
- [ ] Both evaluated properly

**Comparison:**
- [ ] All 4 models compared
- [ ] Visualizations clear
- [ ] Best model identified

**Insights:**
- [ ] When-to-use guide provided
- [ ] Stock prediction specific insights
- [ ] Practical recommendations

**Code Quality:**
- [ ] Clean, commented code
- [ ] Markdown explanations
- [ ] Reproducible (random seeds set)

---

## Grading Timeline

1. **Submission:** Upload all files to LMS
2. **Auto-Check:** Automated tests verify files run
3. **Manual Review:** Instructor reviews code, visualizations, insights
4. **Feedback:** Detailed feedback within 3-5 business days
5. **Resubmission:** If needed, one resubmission allowed

---

## Frequently Asked Questions

**Q: Can I use different stocks?**
A: Yes! But ensure you have sufficient data (5+ years recommended).

**Q: What if my LSTM doesn't reach R² >0.70?**
A: Document why (e.g., stock is hard to predict, need more data). Show you tried different architectures. You won't lose full points if you demonstrate effort.

**Q: Can I use libraries like Prophet or ARIMA?**
A: Bonus! But ensure you still implement the required LSTM and Dense NNs.

**Q: How long should training take?**
A: 5-15 minutes for all models on CPU, 2-5 minutes on GPU.

**Q: Can I work in groups?**
A: Capstone is individual work. But you can discuss approaches (not share code).

---

**Good luck with your capstone!** 🚀

This is where you demonstrate mastery of neural networks AND the wisdom to know when to use them vs traditional ML.
