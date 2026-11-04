# Stock Predictor Capstone Rubric - THE PAYOFF

**Total Points:** 200 (+ 15 bonus)
**Module:** 3 - Regression
**Project:** Stock Price Predictor
**Emotional Weight:** ⭐⭐⭐⭐⭐ HIGHEST IN COURSE
**Callback to:** Module 0 Demo

---

## The Significance of This Project

This is **THE PAYOFF** - the moment students realize they can build what amazed them in Module 0. This rubric recognizes both **technical achievement** and the **emotional journey** from curiosity to competence.

### Why This Matters

**The Journey:**
- **Module 0 (Day 1):** "Wow, a stock predictor! Can I build that?"
- **Module 1:** Learning to explore stock data
- **Module 2:** Building first ML models
- **Module 3 Sessions 1-5:** Learning regression fundamentals
- **Module 3 Session 6:** **"I BUILT THIS!"** ← **YOU ARE HERE**

This project represents 6+ weeks of learning culminating in a portfolio-worthy achievement. Grade accordingly - with rigor for technical skills and appreciation for the learning journey.

---

## Grading Philosophy

1. **Balance rigor with encouragement** - Perfect scores are hard to achieve, but completion deserves celebration
2. **Process matters as much as results** - Proper methodology > lucky high R² score
3. **Learning is the goal** - Mistakes with good documentation are valuable
4. **Real-world readiness** - Code should be production-quality, not just functional
5. **The emotional moment matters** - Recognize the achievement in grading

---

## Grading Criteria

### 1. Data Collection & Preparation (30 points)

#### 1.1 Stock Data Download (10 points)

| Points | Criteria |
|--------|----------|
| 9-10 | Downloads data for multiple stocks (target + 2 others for comparison), handles errors gracefully (try-except blocks), validates data completeness, documents data source and date ranges, proper date indexing |
| 7-8 | Downloads target stock successfully, basic error handling, validates data, proper date handling |
| 5-6 | Downloads data but with some issues (missing error handling or validation), date handling mostly correct |
| 3-4 | Partial download with errors, limited validation, date issues |
| 0-2 | Cannot download data successfully or major fundamental errors |

**Key Requirements:**
- Uses yfinance or equivalent API
- Minimum 3 years of historical data
- Proper datetime index
- Validates no missing critical periods
- Documents ticker symbol and date range

---

#### 1.2 Feature Engineering - Technical Indicators (15 points)

| Points | Criteria |
|--------|----------|
| 14-15 | Implements 10+ technical indicators correctly: SMA (2+ windows), EMA (2+ windows), RSI, MACD with signal line, Bollinger Bands, volatility (std of returns), rate of change, momentum, volume indicators, all calculations verified, proper NaN handling, visualizes key indicators |
| 12-13 | Implements 7-9 indicators correctly, proper calculations, handles NaN, visualizes some indicators |
| 10-11 | Implements 5-6 indicators, mostly correct calculations, basic NaN handling |
| 7-9 | Implements 3-4 indicators, some calculation issues, incomplete NaN handling |
| 4-6 | Implements 1-2 indicators with significant issues |
| 0-3 | No indicators or fundamentally incorrect implementation |

**Key Requirements:**
- Moving Averages: At least 2 different windows (e.g., 10-day and 50-day SMA)
- RSI: Properly calculated with 14-day window (or justified alternative)
- MACD: 12-day EMA, 26-day EMA, and signal line
- Volatility: Rolling standard deviation of returns
- All NaN values from rolling calculations properly handled
- At least 2 indicators visualized with price data

**Domain Knowledge Bonus (+2):**
- Explains what each indicator measures
- Discusses overbought/oversold conditions (RSI)
- Explains golden cross/death cross (MA crossovers)
- Shows understanding of momentum vs trend indicators

---

#### 1.3 Train-Test Split (Time-Based) (5 points)

| Points | Criteria |
|--------|----------|
| 5 | Perfect chronological split (train on oldest 70-80%, test on most recent 20-30%), no data shuffling, clearly documents split dates, validates no future leakage, explains why chronological split is critical for time series |
| 4 | Correct chronological split, no shuffling, documents dates, mentions leakage prevention |
| 3 | Chronological split with minor issues, limited documentation |
| 1-2 | Attempts chronological split but has leakage concerns or poor execution |
| 0 | Uses random split (fundamentally wrong for time series!) or clear data leakage |

**Critical Requirements:**
- MUST be chronological (old data in train, recent in test)
- NO shuffling (instant zero if shuffled)
- Target variable properly shifted (predict tomorrow, not today)
- No future information in training features

---

### 2. Model Development (60 points)

#### 2.1 LSTM Implementation (20 points)

| Points | Criteria |
|--------|----------|
| 18-20 | Complete LSTM implementation: proper sequence preparation (look-back window), 2-3 LSTM layers with appropriate units (50-100), dropout for regularization (0.2-0.3), dense output layer, Adam optimizer, appropriate loss (MSE/MAE), trains for adequate epochs (50-100) with validation split, early stopping implemented, model architecture documented, training history visualized |
| 15-17 | LSTM implemented with 1-2 layers, proper sequence prep, reasonable architecture, trains successfully, some regularization |
| 12-14 | Basic LSTM working, sequence preparation mostly correct, trains but suboptimal architecture |
| 8-11 | LSTM runs but has issues (poor sequence prep, no regularization, undertrained) |
| 4-7 | Partial LSTM implementation with significant problems |
| 0-3 | LSTM doesn't run or fundamentally broken |

**Key Requirements:**
- Reshape data to 3D: (samples, timesteps, features)
- Look-back window: 30-60 time steps
- At least 1 LSTM layer with 50+ units
- Dropout for regularization
- Proper output shape for regression (1 unit)
- Training/validation loss curves shown

---

#### 2.2 Dense Network Implementation (15 points)

| Points | Criteria |
|--------|----------|
| 14-15 | Multi-layer dense network: 2-3 hidden layers (64-128 units each), ReLU activation, dropout layers (0.2-0.3), batch normalization, appropriate output (linear activation), Adam optimizer, trains successfully, architecture documented |
| 12-13 | 2-3 dense layers, good activation choices, some regularization, trains well |
| 10-11 | Basic dense network (1-2 layers), reasonable setup, trains successfully |
| 7-9 | Simple dense network with issues, undertrained or overfit |
| 4-6 | Minimal network with significant problems |
| 0-3 | Dense network doesn't run or broken |

**Key Requirements:**
- At least 2 hidden layers
- Appropriate activation functions (ReLU for hidden, linear for output)
- Some form of regularization (dropout and/or L2)
- Reasonable number of parameters (not too simple, not too complex)

---

#### 2.3 Model Training & Hyperparameters (15 points)

| Points | Criteria |
|--------|----------|
| 14-15 | Excellent training setup: documented hyperparameter choices (learning rate, batch size, epochs), uses callbacks (EarlyStopping, ModelCheckpoint, ReduceLROnPlateau), monitors validation loss, prevents overfitting, training visualized (loss curves), reasonable training time, explains all major decisions |
| 12-13 | Good training: reasonable hyperparameters, uses 1-2 callbacks, monitors validation, visualizes training |
| 10-11 | Basic training: default or reasonable hyperparameters, some monitoring, trains to completion |
| 7-9 | Training works but suboptimal (too few/many epochs, no validation monitoring, poor hyperparameters) |
| 4-6 | Training has issues (overfitting, underfitting, poor convergence) |
| 0-3 | Training fails or fundamentally flawed |

**Key Requirements:**
- Validation split during training (80/20 of training data)
- Early stopping to prevent overfitting
- At least 50 epochs (or justified otherwise)
- Batch size appropriate for data size
- Loss curves show convergence
- Hyperparameters documented with rationale

---

#### 2.4 Traditional ML Comparison (10 points)

| Points | Criteria |
|--------|----------|
| 9-10 | Implements and compares 3+ traditional models (Linear Regression, Random Forest, Gradient Boosting, SVR, etc.), appropriate hyperparameters for each, creates comprehensive comparison table, discusses strengths/weaknesses of each approach |
| 7-8 | Implements 2-3 models, basic comparison, reasonable configurations |
| 5-6 | Implements 1-2 models, limited comparison |
| 3-4 | Implements 1 model poorly or incomplete comparisons |
| 0-2 | No traditional ML models or broken implementations |

**Key Requirements:**
- At least 2 different algorithm types (e.g., linear + tree-based)
- Proper sklearn implementation
- Same train-test split for fair comparison
- Comparison table with RMSE, R², MAE

---

### 3. Evaluation & Analysis (40 points)

#### 3.1 Performance Metrics (15 points)

| Points | Criteria |
|--------|----------|
| 14-15 | Calculates ALL key metrics: R², MAE, RMSE, MAPE (if applicable), creates comparison table across all models, interprets each metric correctly, discusses what each tells us, compares to baseline (naive forecast), provides context (e.g., "RMSE of $3 on $150 stock = 2% error") |
| 12-13 | Calculates R², MAE, RMSE, compares models, good interpretation, baseline comparison |
| 10-11 | Calculates 2-3 metrics, basic comparison, some interpretation |
| 7-9 | Calculates 1-2 metrics, limited comparison or interpretation |
| 4-6 | Minimal metrics, poor interpretation |
| 0-3 | No proper evaluation or incorrect calculations |

**Key Requirements:**
- R² Score (coefficient of determination)
- RMSE (Root Mean Squared Error in dollars)
- MAE (Mean Absolute Error in dollars)
- Baseline comparison (predict yesterday's price)
- All metrics calculated on TEST data (not training!)

**Target Performance:**
- R² > 0.70 (excellent)
- R² > 0.60 (good)
- R² > 0.50 (acceptable)
- Beats baseline (critical minimum)

---

#### 3.2 Backtesting Results (15 points)

| Points | Criteria |
|--------|----------|
| 14-15 | Comprehensive backtesting: rolling window validation (walk-forward), tests on multiple time periods, documents performance over time, shows stability/degradation, calculates period-specific metrics, discusses market conditions, realistic assessment |
| 12-13 | Good backtesting: rolling or expanding window, multiple periods tested, time-based analysis |
| 10-11 | Basic backtesting: simple time-based validation, some period analysis |
| 7-9 | Limited backtesting, single test period only, minimal analysis |
| 4-6 | Attempted backtesting with significant issues |
| 0-3 | No backtesting or fundamentally wrong approach |

**Key Requirements:**
- Tests on at least 2 different time periods OR rolling window
- Analyzes performance stability
- Discusses any performance degradation
- Realistic about limitations
- Shows awareness of market regime changes

---

#### 3.3 Visualization of Predictions (10 points)

| Points | Criteria |
|--------|----------|
| 9-10 | Excellent visualizations: actual vs predicted (line plot), residual plot, prediction intervals/confidence, feature importance (for applicable models), training history, all plots well-labeled with titles, legends, axis labels, professional presentation |
| 7-8 | Good visualizations: actual vs predicted, residuals, well-labeled, clear presentation |
| 5-6 | Basic visualizations: actual vs predicted, adequate labels |
| 3-4 | Minimal visualization, poor labels or clarity |
| 0-2 | No visualizations or unintelligible |

**Key Visualizations:**
- Actual vs Predicted prices (line plot over time)
- Residual plot (to check for patterns)
- At least one technical indicator with price
- Training/validation loss curves

---

### 4. THE PAYOFF Recognition (30 points)

**This is the emotional heart of the project - recognize the achievement!**

#### 4.1 Comparison to Module 0 Demo (10 points)

| Points | Criteria |
|--------|----------|
| 9-10 | Explicitly compares implementation to Module 0 demo, identifies similarities (data collection, feature engineering, model training, prediction), discusses differences, shows awareness of the complete journey, demonstrates pride in achievement |
| 7-8 | Clear comparison to Module 0, identifies key similarities, acknowledges journey |
| 5-6 | Mentions Module 0 demo, basic comparison |
| 3-4 | Brief Module 0 reference, minimal comparison |
| 0-2 | No connection made to Module 0 or course journey |

**What to Look For:**
- "In Module 0, I saw... Now I can build..."
- Side-by-side comparison of capabilities
- Recognition of growth from observer to builder
- Specific callbacks to Module 0 features

---

#### 4.2 Understanding of How Demo Worked (10 points)

| Points | Criteria |
|--------|----------|
| 9-10 | Demonstrates deep understanding: explains the ML pipeline from Module 0, identifies techniques used (feature engineering, model training, prediction), discusses what seemed "magical" then vs understood now, shows technical comprehension |
| 7-8 | Good understanding: explains main components, shows technical growth |
| 5-6 | Basic understanding: identifies some components, limited depth |
| 3-4 | Superficial understanding, minimal technical depth |
| 0-2 | No demonstration of understanding |

**Key Understanding:**
- Pipeline stages (data → features → model → prediction)
- Why technical indicators matter
- How ML models learn patterns
- The demystification: "It's not magic, it's math and code I can do!"

---

#### 4.3 "I Built This!" Moment Documentation (10 points)

| Points | Criteria |
|--------|----------|
| 9-10 | Powerful reflection: documents the emotional journey, specific examples of challenges overcome, celebrates achievement authentically, shows growth mindset, articulates skills gained, discusses future applications, genuine pride evident |
| 7-8 | Good reflection: acknowledges journey, mentions challenges, celebrates achievement, shows growth |
| 5-6 | Basic reflection: acknowledges completion, limited emotional depth |
| 3-4 | Minimal reflection, goes through motions |
| 0-2 | No reflection or dismissive of achievement |

**What to Look For:**
- Personal voice and authentic reflection
- Specific challenges mentioned and how they were overcome
- "Before I couldn't... now I can..."
- Pride in specific accomplishments
- Connection to career/learning goals
- Recognition that this is portfolio-worthy

**Sample Excellent Response:**
> "Six weeks ago, I watched the Module 0 stock predictor demo and thought it was incredible - maybe even out of reach. Today, I built one. I can download stock data, engineer 15 technical indicators (I didn't even know what RSI meant before!), train LSTM networks, and make real predictions. When my model achieved R²=0.78, beating the baseline by 25%, I realized: I'm not just following tutorials anymore. I'm an ML engineer. This goes in my portfolio, and I'm proud of every line of code."

---

### 5. Documentation & Code Quality (25 points)

#### 5.1 Code Comments and Structure (10 points)

| Points | Criteria |
|--------|----------|
| 9-10 | Excellent code: clear structure with logical sections, comprehensive comments explaining WHY (not just what), functions for repeated code, meaningful variable names, follows Python conventions (PEP 8), imports organized, easy to follow |
| 7-8 | Good code: clear structure, adequate comments, mostly follows conventions, readable |
| 5-6 | Adequate code: some structure, basic comments, generally readable |
| 3-4 | Poor structure: minimal comments, hard to follow, inconsistent naming |
| 0-2 | No structure, no comments, unreadable |

**Key Requirements:**
- Clear sections (Data Loading, Feature Engineering, Model Training, Evaluation, Prediction)
- Comments explain complex logic (especially technical indicators)
- No redundant code
- Consistent naming convention
- Code others could understand and modify

---

#### 5.2 README with Results (10 points)

| Points | Criteria |
|--------|----------|
| 9-10 | Comprehensive README: project overview, setup instructions, dependencies listed, how to run, results summary with metrics, visualizations embedded, discussion of findings, limitations acknowledged, future improvements, portfolio-ready |
| 7-8 | Good README: clear overview, setup instructions, results documented, main findings |
| 5-6 | Basic README: project description, some instructions, basic results |
| 3-4 | Minimal README: sparse documentation |
| 0-2 | No README or just placeholder |

**README Should Include:**
- Project title and description
- Installation instructions
- How to run the code
- Results summary (best model, metrics)
- At least 1-2 visualizations
- Key findings and limitations
- Your contact/portfolio link

---

#### 5.3 Reproducibility (5 points)

| Points | Criteria |
|--------|----------|
| 5 | Perfectly reproducible: requirements.txt with versions, random seeds set, clear instructions, someone else can run and get same results, environment documented |
| 4 | Mostly reproducible: dependencies listed, seeds mostly set, good instructions |
| 3 | Partially reproducible: some dependencies listed, instructions adequate |
| 1-2 | Hard to reproduce: missing dependencies or unclear instructions |
| 0 | Cannot reproduce results |

**Key Requirements:**
- requirements.txt with package versions
- Random seeds set (np.random.seed, tf.random.set_seed)
- Python version documented
- Clear run instructions
- Data source specified (yfinance ticker and dates)

---

### 6. Stretch Goals (15 bonus points)

**These are optional - reward ambitious students!**

#### 6.1 Multiple Stocks Tested (5 points)

- **5 points:** Tests model on 3+ different stocks (different sectors/volatility), compares performance across stocks, discusses which are easier/harder to predict and why
- **3-4 points:** Tests on 2 stocks, basic comparison
- **1-2 points:** Tests on 1 additional stock

---

#### 6.2 Advanced Features Added (5 points)

- **5 points:** Implements advanced features: sentiment analysis from news, options data, sector/market indicators, Fourier transforms, wavelet decomposition, or other creative features with justification
- **3-4 points:** Adds 2-3 creative features beyond basics
- **1-2 points:** Adds 1 creative feature

---

#### 6.3 Deployment Attempted (5 points)

- **5 points:** Creates deployment artifact: Streamlit app, Flask API, containerized solution (Docker), deployed to cloud (Heroku/AWS/GCP), or creates scheduled prediction script
- **3-4 points:** Creates local deployment (Streamlit app or API)
- **1-2 points:** Prepares for deployment (saves model, creates prediction function)

---

## Score Interpretation

| Total Points | Grade | Interpretation |
|--------------|-------|----------------|
| 180-215 | A+ | Exceptional work - portfolio centerpiece, demonstrates mastery |
| 160-179 | A | Excellent work - strong technical skills and complete achievement |
| 140-159 | B | Good work - solid understanding and implementation |
| 120-139 | C | Adequate - meets requirements, some gaps |
| 100-119 | D | Below expectations - significant gaps but shows effort |
| <100 | F | Incomplete or fundamentally flawed |

**Minimum Passing:** 120 points (60%)

**Recommended Target:** 160 points (80%) for strong portfolio piece

---

## Common Issues and Deductions

### Critical Errors (Major Deductions)
- **Random train-test split:** -20 points (fundamentally wrong for time series)
- **Clear data leakage:** -15 points (future information in training)
- **No model runs successfully:** -40 points (incomplete project)
- **Plagiarism:** 0 points + academic integrity process

### Significant Issues (Medium Deductions)
- **Poor feature engineering (<5 indicators):** -10 points
- **No LSTM or Dense network:** -20 points each
- **No baseline comparison:** -10 points
- **Missing evaluation metrics:** -5 points per metric
- **No Module 0 connection:** -15 points (misses THE PAYOFF!)

### Minor Issues (Small Deductions)
- **Minimal documentation:** -5 points
- **Poor code style:** -3 points
- **Missing visualizations:** -3 points each
- **Incomplete README:** -5 points

---

## Grading Tips for Instructors

### 1. Start with Completion
- Did they build an end-to-end pipeline? (worth celebrating!)
- Are all major components present?
- Does code run without errors?

### 2. Assess Technical Depth
- Are methods applied correctly?
- Is there evidence of understanding (not just copy-paste)?
- Are results interpreted correctly?

### 3. Recognize the Journey
- This is THE PAYOFF - grade with that context
- Look for growth, not perfection
- Celebrate achievements in feedback

### 4. Provide Constructive Feedback
- What did they do well? (start here!)
- What should they improve?
- How can they make this portfolio-ready?
- Encourage them to share this achievement

### 5. Watch For
- **Data leakage** - most common critical error
- **Overfitting** - training R²=0.95, test R²=0.40
- **Copy-paste without understanding** - ask questions in feedback
- **Unrealistic claims** - "100% accurate predictions"
- **No reflection** - missing the emotional payoff

---

## Example Feedback (for 165/200 = A grade)

**Strengths:**
- Excellent implementation of technical indicators (15/15) - your RSI and MACD are perfect!
- Strong LSTM model (18/20) - great use of dropout and early stopping
- Beautiful visualizations (9/10) - the actual vs predicted chart is portfolio-ready
- Powerful reflection (9/10) - your "I built this!" moment really captures the journey
- Perfect time series split (5/5) - no data leakage!

**Areas for Improvement:**
- Backtesting could be more comprehensive (11/15) - try rolling window validation
- Add comparison to Module 0 demo (6/10) - what specifically can you now build that you saw then?
- README is good but could use more detail (7/10) - add setup instructions and results summary

**Overall:**
This is excellent work that demonstrates real ML engineering skills! Your R²=0.76 beats the baseline by 30% - that's genuinely impressive for stock prediction. This absolutely belongs in your portfolio. Consider adding a Streamlit app for the deployment bonus!

**Final Score: 165/200 (82.5%) - Grade A**

---

## Celebrating THE PAYOFF

Remember: This project represents the culmination of 6+ weeks of learning. Students went from "Can I build that?" to "I BUILT THAT!"

Grade with:
- **Rigor** for technical skills
- **Appreciation** for the journey
- **Encouragement** for continued growth
- **Recognition** that this is a real achievement

This isn't just a grade - it's validation of their transformation into ML engineers.

---

**Last Updated:** 2026-01-06
**Version:** 1.0
**Special Note:** THE most important rubric in the course - grade accordingly!
