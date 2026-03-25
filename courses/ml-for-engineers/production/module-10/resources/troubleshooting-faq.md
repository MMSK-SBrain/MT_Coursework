# Capstone Project: Troubleshooting FAQ

## Planning & Scoping Issues

### Q: My project scope is too large. What should I cut?
**A:** Focus on MVP:
1. Identify your 3 core features
2. Move everything else to "stretch goals"
3. Ensure core features work excellently
4. Add extras only if time permits

**Example:** Stock predictor
- **Keep:** Basic price prediction, simple backtesting, Streamlit dashboard
- **Cut for now:** Real-time updates, advanced strategies, mobile app

---

### Q: I can't find a good dataset for my idea
**A:** Options:
1. Try alternative datasets (see resources/dataset-sources.md)
2. Generate synthetic data
3. Choose a different project with available data
4. Web scraping (if legal and ethical)

**Remember:** Verify data access BEFORE committing to project!

---

### Q: How do I know if my project is complex enough?
**A:** Checklist:
- [ ] Uses 3+ ML techniques
- [ ] Includes supervised learning
- [ ] Includes unsupervised OR deep learning
- [ ] Has clear business value
- [ ] Requires meaningful data processing
- [ ] Not solvable with simple rules

If all checked, you're good!

---

## Data & EDA Issues

### Q: My dataset has 40% missing values. What do I do?
**A:** Strategies:
1. Drop columns if missing > 50%
2. Impute with median/mean/mode
3. Use algorithms that handle missing values (XGBoost)
4. Create "missing" indicator features
5. If critical column, find better dataset

**Best practice:** Document your decision and impact on performance

---

### Q: My classes are severely imbalanced (95/5 split)
**A:** Solutions:
1. Use class weights in model
2. SMOTE for oversampling minority
3. Undersample majority class
4. Focus on recall for minority class
5. Use F1-score instead of accuracy
6. Try anomaly detection instead

**Healthcare/Fraud:** Imbalance is expected! Focus on catching rare cases.

---

### Q: Data leakage - how do I avoid it?
**A:** Rules:
1. Split data FIRST, before any processing
2. Fit preprocessors (scalers, imputers) on training data only
3. Never use test data for any decisions
4. Time series: use time-based splits
5. Watch for features that include target info
6. Remove features that wouldn't exist at prediction time

**Example leak:** Using "next_day_price" to predict "today's_direction"

---

## Modeling Issues

### Q: My model accuracy is only 55%. Is this bad?
**A:** Depends on context:
- **Binary classification:** 55% barely better than random (50%)
- **10-class classification:** 55% is good! (random = 10%)
- **Regression:** Check R² and domain expectations

**Steps to improve:**
1. Check baseline performance
2. Add more relevant features
3. Try different algorithms
4. Tune hyperparameters
5. Ensure no data quality issues

---

### Q: Training accuracy 95%, test accuracy 60%. What's wrong?
**A:** Classic overfitting!

**Solutions:**
1. Reduce model complexity
2. Add regularization (L1/L2)
3. Use dropout (neural networks)
4. Get more training data
5. Reduce features (remove redundant)
6. Cross-validation to verify
7. Ensemble methods often help

---

### Q: My model is too slow (training takes hours)
**A:** Speed-up strategies:
1. Use smaller subset for development
2. Reduce features (PCA, selection)
3. Use simpler algorithms first
4. Parallel processing (n_jobs=-1)
5. Use GPU (if deep learning)
6. Sample data for hyperparameter tuning

**Remember:** Good model fast > perfect model never finishes

---

### Q: Which algorithm should I use?
**A:** Decision guide:
- **Start simple:** Linear/Logistic Regression
- **Structured data:** Random Forest, XGBoost
- **Images:** CNN with transfer learning
- **Text:** TF-IDF + classifier or BERT
- **Time series:** ARIMA, LSTM
- **Clustering:** K-Means, DBSCAN
- **Anomaly:** Isolation Forest

**Always try 3+ algorithms!**

---

## Deployment Issues

### Q: "Application Error" when deploying to Heroku
**A:** Checklist:
```bash
# Check logs
heroku logs --tail

# Common fixes:
1. Verify Procfile exists: web: gunicorn app:app
2. Check requirements.txt has all dependencies
3. Add runtime.txt: python-3.9.18
4. Ensure PORT environment variable used:
   port = int(os.environ.get("PORT", 5000))
5. Model files < 500MB (Heroku limit)
```

---

### Q: My Streamlit app shows "Module not found" error
**A:** Fixes:
1. Add missing module to requirements.txt
2. Check spelling in import statements
3. Verify package names (sklearn vs scikit-learn)
4. Push updated requirements.txt
5. Redeploy from Streamlit Cloud dashboard

---

### Q: API works locally but fails in production
**A:** Common issues:
1. **File paths:** Use os.path.join, not hardcoded paths
2. **Environment variables:** Use .env file, not hardcoded
3. **Model loading:** Ensure model files uploaded or in correct location
4. **Dependencies:** requirements.txt complete and correct versions
5. **Port:** Use environment PORT variable

---

### Q: My deployed model is too large (>500MB)
**A:** Solutions:
1. Use model compression
2. Store model on S3/Google Cloud Storage, load at startup
3. Use lighter algorithms (MobileNet instead of ResNet)
4. Quantization (reduce precision)
5. Remove unnecessary model components

---

## Documentation Issues

### Q: What should I include in my README?
**A:** Must-haves:
1. Project title and description
2. Problem statement
3. Features list
4. Installation instructions
5. Usage examples
6. Architecture diagram
7. Model performance metrics
8. Deployed URLs
9. Contact information

See templates/project-structure-template/README.md

---

### Q: How detailed should my API documentation be?
**A:** Include:
1. Base URL
2. All endpoints with HTTP methods
3. Request format (JSON schema)
4. Response format (examples)
5. Error codes and messages
6. Authentication (if any)
7. Rate limits (if any)
8. Code examples (curl, Python, JavaScript)

---

## Time Management Issues

### Q: It's Week 3 and my model still doesn't work well
**A:** Emergency plan:
1. Lock current model (even if not perfect)
2. Focus on deployment and documentation
3. Note limitations in README
4. Explain challenges in presentation
5. Discuss improvements as "future work"

**Remember:** Shipped imperfect project > perfect unfinished project

---

### Q: I'm behind schedule. What's most important?
**A:** Priority order:
1. **Must have:** Working model (any performance) + Basic deployment
2. **Should have:** Documentation (README, API docs)
3. **Nice to have:** Model optimization, advanced features
4. **Can skip:** Perfect accuracy, all stretch goals

**Focus on MVP!**

---

## Technical Issues

### Q: ImportError / ModuleNotFoundError
**A:**
```bash
# Install missing package
pip install package-name

# Update requirements.txt
pip freeze > requirements.txt

# Or add manually to requirements.txt
echo "package-name==version" >> requirements.txt
```

---

### Q: Kernel crashes when training model
**A:** Likely memory issue:
1. Reduce batch size
2. Use smaller model
3. Process data in chunks
4. Close other applications
5. Restart kernel and clear output
6. Use Google Colab for more RAM

---

### Q: Git push fails / file too large
**A:**
```bash
# Add large files to .gitignore
echo "*.pkl" >> .gitignore
echo "*.h5" >> .gitignore
echo "data/*.csv" >> .gitignore

# Remove large files from git history (if committed)
git rm --cached large_file.pkl
git commit -m "Remove large file"

# Use Git LFS for large files (alternative)
git lfs install
git lfs track "*.pkl"
```

---

### Q: JSON parsing error in API
**A:** Debug steps:
```python
# Add error handling
try:
    data = request.get_json()
except Exception as e:
    return jsonify({"error": f"Invalid JSON: {str(e)}"}), 400

# Validate required fields
if 'features' not in data:
    return jsonify({"error": "Missing 'features' field"}), 400

# Print for debugging
print(f"Received data: {data}")
```

---

### Q: Streamlit app is slow
**A:** Optimization tips:
```python
# Use caching
@st.cache_data
def load_data():
    return pd.read_csv('data.csv')

@st.cache_resource
def load_model():
    return joblib.load('model.pkl')

# Load model once at startup (outside main)
model = load_model()

# Reduce data displayed
df.head(100)  # Not entire dataset
```

---

## Presentation Issues

### Q: My demo isn't working during presentation!
**A:** Backup plan:
1. Have screenshots ready
2. Use demo video (2-3 min)
3. Show code and explain
4. Show previous successful run
5. Explain what should happen

**Prevention:** Test demo 10 minutes before presenting!

---

### Q: How do I present technical content to non-technical audience?
**A:** Strategies:
1. Start with the problem (relatable)
2. Explain solution in simple terms
3. Show visual results (charts, UI)
4. Use analogies for complex concepts
5. Focus on impact, not just algorithms
6. Save technical details for Q&A

---

## Getting Help

### Still stuck?
1. **Google the error message** (exact text)
2. **Check Stack Overflow** (likely someone had same issue)
3. **Review course materials** (similar examples)
4. **Ask peers** (Slack/Discord)
5. **Attend office hours** (instructor help)
6. **ChatGPT/Claude** (explain your specific issue)

### When asking for help:
1. Describe what you're trying to do
2. Show what you tried
3. Include error messages (full text)
4. Share relevant code (not everything)
5. Explain what you've already attempted

---

## Remember!

- **Perfect is the enemy of done**
- **Shipped imperfect > unfinished perfect**
- **Ask for help early** (don't struggle alone for days)
- **Document as you go** (not at the end)
- **Test frequently** (not just at the end)
- **Take breaks** (fresh mind solves problems faster)

**You've got this!** 💪

---

*Can't find your issue? Check course Slack or ask instructor!*
