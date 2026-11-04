# Module 9: MLOps Capstone Project Rubric

## Total Points: 200

---

## I. Technical Implementation (100 points)

### A. Data & Preprocessing (15 points)

| Score | Criteria |
|-------|----------|
| **13-15** | Excellent data collection and quality. Comprehensive preprocessing and feature engineering. Thorough EDA with insights documented. |
| **10-12** | Good data quality. Solid preprocessing. EDA present with basic insights. |
| **7-9** | Adequate data with some quality issues. Basic preprocessing. Minimal EDA. |
| **0-6** | Poor data quality or inadequate preprocessing. No meaningful EDA. |

**Evaluation Checklist:**
- [ ] Data collected from appropriate sources
- [ ] Data quality assessed and documented
- [ ] Preprocessing pipeline implemented (scaling, encoding, etc.)
- [ ] Feature engineering demonstrates understanding
- [ ] EDA notebook with visualizations and insights
- [ ] Train/validation/test split correctly implemented

---

### B. Model Development (30 points)

| Score | Criteria |
|-------|----------|
| **26-30** | Multiple models tried (≥3) with systematic comparison. Proper evaluation using Module 4 techniques. Hyperparameter tuning demonstrated. Performance meets/exceeds targets. |
| **20-25** | Multiple models tried. Good evaluation practices. Some tuning. Performance reasonable. |
| **14-19** | Limited model experimentation. Basic evaluation. Minimal tuning. Performance below target. |
| **0-13** | Single model or poor evaluation. No tuning. Performance significantly below target. |

**Evaluation Checklist:**
- [ ] Baseline model established
- [ ] At least 3 different algorithms tested
- [ ] Cross-validation used
- [ ] Hyperparameter tuning (GridSearch/RandomSearch)
- [ ] Performance metrics documented
- [ ] Model selection justified
- [ ] Appropriate for problem type (classification/regression/etc.)

**Performance Targets (adjust based on project):**
- Classification: Accuracy > 80% or F1 > 0.75
- Regression: R² > 0.70 or RMSE within acceptable range
- NLP: Accuracy > 85% for classification tasks
- Computer Vision: Accuracy > 75% for multi-class

---

### C. API Development (25 points)

| Score | Criteria |
|-------|----------|
| **22-25** | Complete, production-ready API (Flask or FastAPI). Multiple endpoints (/predict, /health, /). Comprehensive input validation and error handling. Proper HTTP status codes. CORS enabled. |
| **17-21** | Working API with main functionality. Basic validation and error handling. |
| **11-16** | API runs but with significant limitations or bugs. Minimal validation. |
| **0-10** | API doesn't work reliably or missing critical functionality. |

**Evaluation Checklist:**
- [ ] Prediction endpoint works correctly
- [ ] Health check endpoint implemented
- [ ] Input validation prevents errors
- [ ] Error handling with appropriate HTTP codes
- [ ] JSON request/response format
- [ ] CORS configured (if needed)
- [ ] Model loaded efficiently (once at startup)
- [ ] Logging implemented
- [ ] Requirements.txt complete

---

### D. User Interface (20 points)

| Score | Criteria |
|-------|----------|
| **18-20** | Polished, user-friendly UI (Streamlit or web app). Clear input forms. Well-formatted output. Visualizations enhance understanding. Error handling visible to users. |
| **14-17** | Functional UI with good usability. Some visualizations. Basic error handling. |
| **9-13** | Basic UI that works but could be more user-friendly. Minimal visualizations. |
| **0-8** | Poor UI or doesn't work reliably. Confusing to users. |

**Evaluation Checklist:**
- [ ] Input forms are clear and intuitive
- [ ] Predictions displayed in user-friendly format
- [ ] Includes visualizations (charts, graphs, images)
- [ ] Error messages help users understand issues
- [ ] Responsive design (works on different screen sizes)
- [ ] Includes example inputs or demo mode
- [ ] Professional appearance

---

### E. Deployment (10 points)

| Score | Criteria |
|-------|----------|
| **9-10** | Successfully deployed to cloud with public URLs for both API and UI. Both components work reliably. Proper configuration files. |
| **7-8** | Deployed but with minor reliability issues or only one component deployed. |
| **4-6** | Deployment attempted but significant issues. Intermittent availability. |
| **0-3** | Not deployed or completely non-functional in cloud. |

**Evaluation Checklist:**
- [ ] API deployed with public URL
- [ ] UI deployed with public URL
- [ ] Both components accessible from anywhere
- [ ] Proper environment configuration
- [ ] No hardcoded secrets in code
- [ ] Deployment works consistently

---

## II. Documentation & Presentation (60 points)

### A. README Documentation (25 points)

| Score | Criteria |
|-------|----------|
| **22-25** | Comprehensive README with project overview, architecture diagram, setup instructions, usage guide, API docs, performance metrics, and future improvements. Professional quality. |
| **17-21** | Good README covering most essential elements. Clear and well-organized. |
| **11-16** | Basic README with essential information but lacking detail or organization. |
| **0-10** | Minimal README or poorly organized. Critical information missing. |

**Required Sections:**
- [ ] Project title and description
- [ ] Problem statement and motivation
- [ ] Features list
- [ ] Tech stack
- [ ] Architecture diagram
- [ ] Local setup instructions
- [ ] Usage guide with examples
- [ ] API documentation (endpoints, formats)
- [ ] Deployed app links
- [ ] Screenshots or GIFs
- [ ] Performance metrics
- [ ] Known limitations
- [ ] Future improvements
- [ ] License and attribution

---

### B. Code Quality & Comments (15 points)

| Score | Criteria |
|-------|----------|
| **13-15** | Clean, well-organized code following best practices. Comprehensive docstrings. Meaningful variable names. Proper code structure. |
| **10-12** | Good code quality. Most functions documented. Generally follows conventions. |
| **6-9** | Adequate code but could be better organized. Some documentation. |
| **0-5** | Poor code quality. Minimal documentation. Hard to understand. |

**Evaluation Checklist:**
- [ ] Functions have docstrings
- [ ] Variable names are descriptive
- [ ] Code is modular (not one giant function)
- [ ] Follows PEP 8 style guide
- [ ] No commented-out code blocks
- [ ] Complex logic explained with comments
- [ ] Imports organized
- [ ] Consistent formatting

---

### C. Presentation Materials (20 points)

| Score | Criteria |
|-------|----------|
| **18-20** | Excellent presentation with clear slides, working demo video, and compelling storytelling. Covers problem, solution, results, and learnings. |
| **14-17** | Good presentation covering key points. Demo works. Clear communication. |
| **9-13** | Basic presentation. Demo present but may have issues. Communication adequate. |
| **0-8** | Poor presentation or demo doesn't work. Unclear communication. |

**Required Components:**
- [ ] Presentation slides (8-12 slides)
- [ ] Demo video (2-3 minutes)
- [ ] Problem statement explained clearly
- [ ] Solution architecture shown
- [ ] Results/metrics presented
- [ ] Live demo or video demonstration
- [ ] Challenges and learnings discussed
- [ ] Future work outlined
- [ ] Professional appearance
- [ ] Time management (5-7 minute presentation)

---

## III. Innovation & Impact (40 points)

### A. Technical Innovation (15 points)

| Score | Criteria |
|-------|----------|
| **13-15** | Novel approach or creative solution. Successfully integrates multiple techniques from course. High technical complexity handled well. |
| **10-12** | Good integration of course concepts. Some creative elements. Moderate complexity. |
| **6-9** | Standard implementation without much innovation. Basic complexity. |
| **0-5** | Minimal complexity or innovation. Simple application of single technique. |

**Innovation Indicators:**
- [ ] Combines techniques from multiple modules
- [ ] Creative feature engineering
- [ ] Novel application domain
- [ ] Advanced techniques beyond basic requirements
- [ ] Handles complex challenges well

---

### B. Real-World Applicability (15 points)

| Score | Criteria |
|-------|----------|
| **13-15** | Addresses real, important problem. Clear business or social value. Production-ready quality. Could actually be deployed for real users. |
| **10-12** | Solves meaningful problem. Good practical value. Nearly production-ready. |
| **6-9** | Addresses simple problem. Some practical value. Needs work for production. |
| **0-5** | Toy problem or unclear value. Not suitable for production. |

**Applicability Checklist:**
- [ ] Solves real problem (not just academic exercise)
- [ ] Business value clearly articulated
- [ ] Scalability considered
- [ ] Security basics addressed
- [ ] Error handling for edge cases
- [ ] User-centric design
- [ ] Performance is acceptable
- [ ] Could be extended/maintained

---

### C. Portfolio Quality (10 points)

| Score | Criteria |
|-------|----------|
| **9-10** | Outstanding portfolio piece. Professional presentation. Would impress employers. Demonstrates mastery of ML deployment. |
| **7-8** | Strong portfolio piece. Good demonstration of skills. Professional quality. |
| **4-6** | Adequate for portfolio. Shows competence but not exceptional. |
| **0-3** | Not portfolio-ready. Significant improvements needed. |

**Portfolio Evaluation:**
- [ ] Professional GitHub repository
- [ ] Clear, compelling project description
- [ ] Visual appeal (screenshots, diagrams)
- [ ] Demonstrates multiple skills
- [ ] Public deployment showing it works
- [ ] Well-documented
- [ ] Suitable for job applications
- [ ] Shows end-to-end capability

---

## Grading Scale

| Grade | Points | Percentage |
|-------|--------|------------|
| **A+** | 190-200 | 95-100% |
| **A** | 180-189 | 90-94% |
| **A-** | 170-179 | 85-89% |
| **B+** | 160-169 | 80-84% |
| **B** | 150-159 | 75-79% |
| **B-** | 140-149 | 70-74% |
| **C+** | 130-139 | 65-69% |
| **C** | 120-129 | 60-64% |
| **C-** | 110-119 | 55-59% |
| **D** | 100-109 | 50-54% |
| **F** | < 100 | < 50% |

---

## Submission Requirements

### Required Deliverables:

1. **Code Repository** (GitHub)
   - All source code
   - README.md
   - requirements.txt
   - .gitignore
   - Proper folder structure

2. **Deployed Application**
   - API URL (public and working)
   - UI URL (public and working)
   - Must remain live for at least 2 weeks after submission

3. **Documentation**
   - Complete README
   - API documentation
   - Architecture diagram
   - Model card

4. **Presentation Materials**
   - Slides (PDF or Google Slides link)
   - Demo video (YouTube/Vimeo/Loom link)
   - Transcript or speaker notes

5. **Submission Form**
   - API URL
   - UI URL
   - GitHub repository URL
   - Demo video URL
   - Slide deck URL
   - Brief project summary (200 words)

### Late Submission Policy:
- 1-2 days late: -10 points
- 3-5 days late: -25 points
- > 5 days late: -50 points
- Not accepted after 7 days

---

## Common Pitfalls to Avoid

1. **Incomplete Deployment** - Both API and UI must be publicly accessible
2. **Poor Documentation** - README is critical; don't neglect it
3. **No Error Handling** - Production code must handle errors gracefully
4. **Minimal Features** - Go beyond basic requirements to stand out
5. **Toy Problem** - Choose a problem with real-world significance
6. **Last-Minute Rush** - Start early; deployment often has unexpected issues
7. **Hardcoded Values** - Use environment variables for configuration
8. **No Testing** - Test thoroughly before submission
9. **Forgotten Requirements.txt** - Must include all dependencies
10. **Broken Links** - Verify all URLs work before submitting

---

## Instructor Evaluation Notes

### Holistic Assessment:
Beyond the rubric scores, consider:
- Overall polish and professionalism
- Effort and growth demonstrated
- Creativity and problem-solving
- Presentation and communication skills
- Ability to debug and handle challenges

### Bonus Points (up to 10 extra):
- Exceptional innovation or creativity
- Significantly exceeds requirements
- Publication quality work
- Open source contribution potential
- Advanced features (Docker, CI/CD, etc.)

### Feedback Guidelines:
- Highlight specific strengths
- Provide actionable improvement suggestions
- Acknowledge effort and growth
- Encourage continued learning
- Connect to career opportunities

---

**Created:** 2026-01-06
**Version:** 1.0
**Module:** 9 - Deployment & MLOps
