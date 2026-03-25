# Custom Project Guidelines

## Overview

Want to build something unique? Great! Custom projects are encouraged as long as they meet the capstone requirements.

**Approval Required:** Yes (submit proposal by end of Week 1, Session 1)

---

## Minimum Requirements for Custom Projects

### 1. Technical Requirements

**ML Complexity:**
- ✅ Must use **at least 3 different ML techniques** from the course
- ✅ Must include **supervised learning** (classification or regression)
- ✅ Must include **at least ONE** of:
  - Unsupervised learning (clustering, dimensionality reduction, anomaly detection)
  - Deep learning (neural networks, CNNs, RNNs, LSTMs)
  - Advanced techniques (ensemble methods, transfer learning, etc.)

**Scope:**
- ✅ Sufficient complexity (not too simple)
- ✅ Feasible in 3 weeks (not too ambitious)
- ✅ Clear success criteria
- ✅ Measurable outcomes

### 2. Data Requirements

**Data Availability:**
- ✅ Dataset exists and is accessible
- ✅ Minimum 1,000 samples (for tabular data)
- ✅ Or 500+ images/videos (for computer vision)
- ✅ Or 10,000+ text samples (for NLP)
- ✅ Proper licensing for educational use

**Data Quality:**
- ✅ Sufficient features for meaningful ML
- ✅ Reasonable class balance (or plan to handle imbalance)
- ✅ No missing data > 50% (or plan to handle)

### 3. Deployment Requirements

**Production Deployment:**
- ✅ Working API (Flask/FastAPI) deployed to cloud
- ✅ User-friendly interface (Streamlit or web app)
- ✅ Both publicly accessible
- ✅ Proper error handling

### 4. Documentation Requirements

**Professional Documentation:**
- ✅ Comprehensive README
- ✅ API documentation
- ✅ User guide
- ✅ Code comments and docstrings

### 5. Presentation Requirements

**Compelling Presentation:**
- ✅ Clear problem statement
- ✅ Well-structured slides
- ✅ Working demo (live or video)
- ✅ Results and impact

---

## Custom Project Proposal Template

**Submit this for approval:**

```markdown
# Custom Capstone Project Proposal

## 1. Project Title
[Clear, descriptive title]

## 2. One-Sentence Description
[Tagline or elevator pitch]

## 3. Problem Statement (200-300 words)
- What problem are you solving?
- Who has this problem?
- Why does it matter?
- What are current solutions and their limitations?
- Why ML is appropriate for this problem?

## 4. Proposed Solution (250-300 words)
- Your ML-based approach
- Key features (list 5-7 main features)
- How it works (high-level workflow)
- Expected impact/benefits

## 5. ML Techniques (Detailed)

List all ML techniques you'll use:

| Technique | Module | Application in Project | Expected Outcome |
|-----------|--------|------------------------|------------------|
| [e.g., Random Forest] | 2 | Product recommendation | Accuracy > 80% |
| [e.g., K-Means] | 5 | Customer segmentation | 4-5 clear clusters |
| [e.g., CNN] | 7 | Image classification | Accuracy > 85% |

**Must have minimum 3 rows**

## 6. Dataset Details

**Dataset 1:**
- Name: [Dataset name]
- Source: [URL or source]
- Size: [Number of samples, features]
- Features: [List main features]
- Target variable: [What you're predicting]
- Access method: [Download, API, scraping]
- License: [Confirm legal use]
- Backup option: [Alternative if primary fails]

**Dataset 2 (if applicable):**
[Same structure as above]

**Data Validation:**
- [ ] I have verified the dataset exists
- [ ] I can access the dataset
- [ ] The license permits educational use
- [ ] The data quality is sufficient

## 7. Success Criteria (Specific & Measurable)

**Model Performance:**
- Model 1: [Metric] > [Target] (e.g., Accuracy > 85%)
- Model 2: [Metric] > [Target] (e.g., R² > 0.70)
- Model 3: [Metric] > [Target] (e.g., Silhouette score > 0.5)

**System Performance:**
- API response time < [X] seconds
- UI loads in < [Y] seconds
- Handles [Z] concurrent users

**Documentation:**
- README completeness: 100%
- All API endpoints documented
- User guide complete
- Code coverage > 80%

**Deployment:**
- Publicly accessible API
- Publicly accessible UI
- 99% uptime during testing week

## 8. Architecture Overview

[Describe or draw your system architecture]

```
Data Sources → Data Processing → ML Models → API → UI
```

Include:
- Data layer
- ML pipeline
- API endpoints
- UI components
- Deployment infrastructure

## 9. Technology Stack

**Languages:**
- Python 3.x

**ML Libraries:**
- [List: scikit-learn, TensorFlow, etc.]

**API Framework:**
- [Flask or FastAPI]

**UI Framework:**
- [Streamlit, React, etc.]

**Deployment:**
- API hosting: [Heroku, AWS, etc.]
- UI hosting: [Streamlit Cloud, Netlify, etc.]
- Database (if needed): [SQLite, PostgreSQL, etc.]

## 10. Timeline (Week by Week)

**Week 1:**
- Day 1-2: [Tasks]
- Day 3-4: [Tasks]
- Day 5-6: [Tasks]
- Milestone: [Deliverable]

**Week 2:**
- Day 1-3: [Tasks]
- Day 4-5: [Tasks]
- Day 6-7: [Tasks]
- Milestone: [Deliverable]

**Week 3:**
- Day 1-2: [Tasks]
- Day 3-4: [Tasks]
- Day 5-7: [Tasks]
- Milestone: [Deliverable]

## 11. Risks & Mitigation

| Risk | Likelihood | Impact | Mitigation Strategy |
|------|------------|--------|---------------------|
| [e.g., Data not available] | Low | High | Verified access + backup source |
| [e.g., Model underperforms] | Medium | Medium | Try multiple algorithms |
| [e.g., Deployment issues] | Low | High | Test early, use proven platforms |
| [Risk 4] | [L/M/H] | [L/M/H] | [Strategy] |

## 12. Minimum Viable Product (MVP)

**Core features that MUST work:**
1. [Feature 1]
2. [Feature 2]
3. [Feature 3]
4. [Feature 4]

**Nice-to-have features (if time permits):**
1. [Feature 5]
2. [Feature 6]

## 13. Why This Project?

**Personal Interest:**
[Why are you passionate about this?]

**Learning Goals:**
[What do you want to learn?]

**Portfolio Value:**
[How will this help your career?]

**Uniqueness:**
[What makes this project stand out?]

## 14. Similar Existing Projects

**Project 1:** [Name and URL]
- How yours is different: [Explanation]

**Project 2:** [Name and URL]
- How yours is different: [Explanation]

[Shows you've done research and your project adds value]

## 15. Checklist

Before submitting, verify:

- [ ] Project uses 3+ ML techniques
- [ ] Includes supervised learning
- [ ] Includes unsupervised OR deep learning
- [ ] Dataset is verified and accessible
- [ ] Success criteria are specific and measurable
- [ ] Timeline is realistic
- [ ] MVP is clearly defined
- [ ] Risks have mitigation strategies
- [ ] Architecture is well thought out
- [ ] I'm genuinely excited about this project!

## 16. Questions for Instructor

[Any specific questions or concerns?]

---

**Student Name:** [Your Name]
**Date:** [Submission Date]
**Preferred Communication:** [Email/Slack]
```

---

## Approval Process

### Step 1: Submit Proposal
- Email or submit via course platform
- Include complete proposal (above template)
- Submit by end of Week 1, Session 1

### Step 2: Instructor Review (24-48 hours)
Instructor evaluates:
- ✅ Technical complexity appropriate?
- ✅ Data availability confirmed?
- ✅ Scope realistic for 3 weeks?
- ✅ Clear success criteria?
- ✅ Meets all requirements?

### Step 3: Feedback
**Possible outcomes:**

**Approved:**
- Proceed with project!
- Minor suggestions may be provided

**Approved with Modifications:**
- Specific changes requested
- Resubmit modified proposal
- Usually approved after changes

**Not Approved:**
- Scope too ambitious or too simple
- Data availability concerns
- Missing requirements
- Choose from curated options or revise significantly

### Step 4: Final Confirmation
- Receive written approval
- Keep approval email for records
- Begin data collection and EDA

---

## Good Custom Project Examples

### Example 1: Music Genre Classification & Playlist Generator
- **ML Techniques:** Audio feature extraction, Classification, Clustering, Recommendation
- **Data:** Spotify API, Million Song Dataset
- **Deployment:** Upload song → Predict genre → Generate playlist
- **Why Good:** Unique, multiple techniques, clear value, feasible

### Example 2: Agricultural Crop Disease Detection
- **ML Techniques:** CNN, Transfer learning, Multi-class classification
- **Data:** PlantVillage dataset, 50K+ images
- **Deployment:** Mobile-friendly app for farmers
- **Why Good:** Social impact, computer vision depth, practical application

### Example 3: Real Estate Price Prediction & Investment Advisor
- **ML Techniques:** Regression, Clustering (neighborhood analysis), Anomaly detection
- **Data:** Zillow, public property records
- **Deployment:** Interactive map with predictions
- **Why Good:** Business value, multiple models, visualization

### Example 4: Student Performance Prediction & Intervention System
- **ML Techniques:** Classification (at-risk students), Clustering, Feature importance
- **Data:** Educational datasets (Kaggle), synthetic data
- **Deployment:** Teacher dashboard for early intervention
- **Why Good:** Education impact, interpretability, actionable insights

---

## Common Rejection Reasons (Avoid These!)

### ❌ Too Simple
- Single model, single dataset
- No clear ML complexity
- Could be done with basic statistics

**Example:** "Predict house prices using linear regression"
**Fix:** Add clustering for neighborhoods, anomaly detection for unusual properties, time series for market trends

### ❌ Too Ambitious
- Requires months of work
- Multiple complex systems
- Unrealistic data needs

**Example:** "Build complete self-driving car system with computer vision, sensor fusion, and path planning"
**Fix:** Focus on one component: "Pedestrian detection system for self-driving cars"

### ❌ Data Not Available
- Dataset doesn't exist
- Requires expensive API
- Legal/ethical issues

**Example:** "Predict credit card fraud using [bank data I don't have]"
**Fix:** Use public credit card fraud datasets from Kaggle

### ❌ Unclear Success Criteria
- Vague goals
- No measurable metrics
- "I'll see how it goes"

**Example:** "Make a good chatbot"
**Fix:** "Intent classification >90% accuracy, response relevance >80%, user satisfaction >4/5"

### ❌ Not Enough ML
- Mostly engineering, minimal ML
- Uses pre-trained model only (no training)

**Example:** "Use GPT-3 API to make chatbot"
**Fix:** "Train custom intent classifier, combine with entity extraction and response generation"

---

## Tips for Strong Custom Proposals

### Do ✅
- Choose a problem you care about
- Verify data access FIRST
- Be specific with success criteria
- Have backup plans for risks
- Show you've done research
- Be realistic about scope
- Demonstrate multiple ML techniques
- Think about deployment from day 1

### Don't ❌
- Propose without checking data
- Be vague about goals
- Overcommit to features
- Ignore existing solutions
- Skip the MVP definition
- Leave deployment for last week
- Propose something you've already built

---

## Get Help!

**Before submitting:**
- Discuss idea with peers
- Research similar projects
- Verify dataset access
- Sketch architecture

**During proposal:**
- Be open to feedback
- Ask questions if uncertain
- Iterate on suggestions

**After approval:**
- Start immediately
- Keep instructor updated
- Ask for help if stuck

---

## Final Thoughts

Custom projects can be:
- More engaging (you chose it!)
- More unique (stands out in portfolio)
- More aligned with career goals
- More challenging (no template to follow)

**But also require:**
- More planning upfront
- More self-direction
- More risk (data, scope)
- More discipline (no clear path)

**Choose custom if:**
- You have a specific passion/idea
- You've validated data exists
- You're comfortable with uncertainty
- You want to stand out

**Choose curated option if:**
- You want lower risk
- You prefer guided path
- Time is limited
- You want proven success

**Both paths lead to success. Choose what excites you!**

---

*Your project, your rules (within requirements)* 🚀
