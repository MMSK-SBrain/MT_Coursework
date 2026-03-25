# Module 5: Unsupervised Learning - Grading Rubrics

## Overview
Module 5 consists of 5 session projects (10 points each) and 1 capstone project (100 points).

**Total Points:** 150 points
- Session Projects: 50 points (5 × 10 points)
- Capstone Project: 100 points

---

## Session Project Rubrics (10 points each)

### General Session Project Rubric

All session projects (Sessions 1-5) follow this general structure:

| Criterion | Points | Description |
|-----------|--------|-------------|
| **Implementation Correctness** | 4 | Code runs without errors, implements required techniques correctly |
| **Proper Evaluation** | 3 | Appropriate metrics used (silhouette scores, etc.), results interpreted correctly |
| **Visualizations** | 2 | Clear, labeled visualizations that support analysis |
| **Insights/Recommendations** | 1 | Thoughtful analysis and actionable insights provided |

---

### Session 1: Customer Segmentation with K-Means (10 points)

| Criterion | Points | Excellent (Full Points) | Good (Partial) | Needs Improvement (Minimal/None) |
|-----------|--------|------------------------|----------------|----------------------------------|
| **Data Preparation & Scaling** | 1 | Features properly scaled using StandardScaler before K-Means | Features scaled but some issues | No feature scaling (critical error!) |
| **Optimal K Selection** | 2 | Both elbow method AND silhouette analysis performed, optimal K justified | Only one method used | No systematic K selection |
| **K-Means Implementation** | 2 | K-Means correctly implemented with optimal K, convergence achieved | K-Means runs but suboptimal K or poor convergence | Major implementation errors |
| **Cluster Analysis** | 2 | 4-5 distinct segments identified, clear profiles created, segments named meaningfully | Segments identified but weak profiling | Unclear or overlapping segments |
| **Business Recommendations** | 2 | Specific, actionable marketing strategies per segment | Generic recommendations | No business context |
| **Visualizations** | 1 | Elbow curve, silhouette plot, 2D cluster viz (PCA), radar charts | Missing 1-2 key visualizations | Poor or missing visualizations |

**Success Criteria:**
- 4-5 distinct customer segments
- Silhouette score > 0.4
- Clear differentiation between segments
- Actionable marketing recommendations

---

### Session 2: Patient Clustering Comparison (10 points)

| Criterion | Points | Excellent (Full Points) | Good (Partial) | Needs Improvement (Minimal/None) |
|-----------|--------|------------------------|----------------|----------------------------------|
| **K-Means Implementation** | 1 | K-Means correctly applied to patient data | Runs with issues | Major errors |
| **Hierarchical Clustering** | 2 | Dendrogram created, linkage method chosen and justified, clusters extracted | Dendrogram created but weak analysis | Poor implementation |
| **DBSCAN Implementation** | 2 | DBSCAN with tuned eps/min_samples, outliers identified | DBSCAN runs but poor tuning | Major errors |
| **Method Comparison** | 3 | All three methods compared on same data, silhouette scores calculated, strengths/weaknesses discussed | Comparison incomplete | No meaningful comparison |
| **Clinical Insights** | 1 | Patient groups profiled with health characteristics, treatment recommendations | Basic profiling only | No clinical context |
| **Visualizations** | 1 | Dendrogram, cluster comparisons, patient profiles | Missing key visualizations | Poor visualizations |

**Success Criteria:**
- 3+ patient groups identified
- Outliers flagged appropriately
- Clear method comparison
- Clinical recommendations provided

---

### Session 3: News Article Clustering (10 points)

| Criterion | Points | Excellent (Full Points) | Good (Partial) | Needs Improvement (Minimal/None) |
|-----------|--------|------------------------|----------------|----------------------------------|
| **Text Preprocessing** | 2 | Proper tokenization, stop word removal, TF-IDF vectorization | Some preprocessing steps missing | Poor or no preprocessing |
| **Clustering Implementation** | 2 | K-Means on TF-IDF vectors, optimal K selected | Clustering runs but suboptimal | Major errors |
| **Topic Discovery** | 3 | Top keywords extracted per cluster, clusters named/interpreted, meaningful topics found | Topics identified but weak interpretation | Unclear topics |
| **Evaluation** | 2 | Compared to actual categories (if available), qualitative assessment of topic coherence | Minimal evaluation | No evaluation |
| **Visualizations** | 1 | Word clouds per cluster, t-SNE visualization, top terms plots | Missing 1-2 visualizations | Poor visualizations |

**Success Criteria:**
- Clusters align with underlying topics
- Clear topic differentiation
- Meaningful keyword extraction
- Word clouds show distinct topics

---

### Session 4: PCA Dimensionality Reduction (10 points)

| Criterion | Points | Excellent (Full Points) | Good (Partial) | Needs Improvement (Minimal/None) |
|-----------|--------|------------------------|----------------|----------------------------------|
| **Standardization** | 1 | Data standardized before PCA (critical!) | Standardized with issues | No standardization |
| **Explained Variance Analysis** | 3 | Scree plot created, cumulative variance analyzed, optimal components selected (e.g., 95% variance) | Analysis incomplete | Poor or no analysis |
| **Dimensionality Reduction** | 2 | Successfully reduced high-dim to 2D/3D, patterns visible | Reduction done but unclear | Major errors |
| **PCA for Clustering** | 2 | Applied PCA before clustering, speed comparison shown, performance maintained | PCA applied but weak comparison | No clustering application |
| **Visualizations** | 2 | Explained variance plot, cumulative variance, 2D scatter, 3D plot | Missing key visualizations | Poor visualizations |

**Success Criteria:**
- Successfully reduced 64D (or higher) to 2D/3D
- Retained 90%+ explained variance
- Clear visualization of patterns
- Speed improvements demonstrated

---

### Session 5: t-SNE Advanced Visualization (10 points)

| Criterion | Points | Excellent (Full Points) | Good (Partial) | Needs Improvement (Minimal/None) |
|-----------|--------|------------------------|----------------|----------------------------------|
| **PCA Implementation** | 2 | PCA correctly applied for comparison baseline | PCA runs with issues | Poor PCA |
| **t-SNE Implementation** | 3 | t-SNE correctly applied with tuned perplexity, convergence achieved | t-SNE runs but poor tuning | Major errors |
| **PCA vs t-SNE Comparison** | 3 | Side-by-side comparison, speed measured, quality assessed, tradeoffs discussed | Comparison incomplete | No meaningful comparison |
| **Perplexity Exploration** | 1 | Multiple perplexity values tested and compared | Only one value used | No exploration |
| **Visualizations** | 1 | PCA vs t-SNE side-by-side, perplexity comparison, digit clusters clearly visible | Missing key visualizations | Poor visualizations |

**Success Criteria:**
- Clear understanding of PCA vs t-SNE tradeoffs
- Effective visualizations with cluster separation
- Appropriate algorithm choice justified
- Perplexity effects demonstrated

---

## Capstone Project Rubric: Fraud Detection with Unsupervised Learning (100 points)

### Overall Structure

| Section | Points | Description |
|---------|--------|-------------|
| Data Preparation | 15 | Dataset creation/loading, exploration, feature scaling |
| Isolation Forest Implementation | 20 | Correct implementation, tuning, anomaly detection |
| One-Class SVM Implementation | 15 | Correct implementation, comparison to Isolation Forest |
| Evaluation vs Ground Truth | 20 | Metrics calculation, confusion matrix, performance analysis |
| Supervised vs Unsupervised Comparison | 20 | Comprehensive comparison, tradeoff analysis |
| Decision Framework & Recommendations | 10 | When to use which approach, business recommendations |

### Detailed Rubric

#### 1. Data Preparation (15 points)

| Criterion | Points | Excellent | Good | Needs Improvement |
|-----------|--------|-----------|------|-------------------|
| **Dataset Creation** | 5 | Realistic fraud dataset with ~5% fraud rate, multiple features, clear patterns | Dataset created but unrealistic | Poor or missing dataset |
| **Exploratory Analysis** | 5 | Feature distributions visualized, fraud vs normal compared, patterns identified | Basic EDA only | Minimal or no EDA |
| **Feature Scaling** | 5 | Proper standardization for both methods | Scaled but with issues | No scaling |

#### 2. Isolation Forest Implementation (20 points)

| Criterion | Points | Excellent | Good | Needs Improvement |
|-----------|--------|-----------|------|-------------------|
| **Implementation** | 8 | Isolation Forest correctly implemented, contamination parameter set appropriately | Runs with issues | Major implementation errors |
| **Tuning** | 6 | Contamination tuned to match expected fraud rate, n_estimators optimized | Minimal tuning | No tuning |
| **Anomaly Scores** | 6 | Anomaly scores extracted and analyzed, distribution visualized | Scores extracted but weak analysis | No score analysis |

#### 3. One-Class SVM Implementation (15 points)

| Criterion | Points | Excellent | Good | Needs Improvement |
|-----------|--------|-----------|------|-------------------|
| **Implementation** | 8 | One-Class SVM correctly implemented with rbf kernel | Runs with issues | Major errors |
| **Parameter Tuning** | 4 | Nu and gamma parameters tuned | Minimal tuning | No tuning |
| **Decision Scores** | 3 | Decision scores analyzed | Basic analysis | No analysis |

#### 4. Evaluation vs Ground Truth (20 points)

| Criterion | Points | Excellent | Good | Needs Improvement |
|-----------|--------|-----------|------|-------------------|
| **Metrics Calculation** | 8 | Precision, Recall, F1 calculated for both methods | Some metrics missing | Poor metrics |
| **Confusion Matrix** | 4 | Confusion matrices created and interpreted | Created but weak interpretation | Missing or poor |
| **Performance Analysis** | 8 | Clear analysis of what works and what doesn't, error analysis | Basic analysis | Minimal analysis |

**Target Performance:**
- Precision > 50% (acceptable for unsupervised)
- Recall > 40% (catches significant fraud)
- Clear understanding that this is lower than supervised

#### 5. Supervised vs Unsupervised Comparison (20 points)

| Criterion | Points | Excellent | Good | Needs Improvement |
|-----------|--------|-----------|------|-------------------|
| **Performance Comparison** | 10 | Detailed comparison table, supervised achieves ~85-92%, unsupervised ~50-60%, gap explained | Comparison present but incomplete | Poor or missing comparison |
| **Tradeoff Analysis** | 10 | Pros/cons of each approach discussed, when each is appropriate, real-world scenarios | Basic tradeoffs only | No meaningful analysis |

**Required Insights:**
- Supervised is more accurate but needs labels
- Unsupervised works without labels but lower performance
- Supervised ~85-92% precision/recall
- Unsupervised ~50-60% precision/recall
- Gap of ~30-35 percentage points

#### 6. Decision Framework & Recommendations (10 points)

| Criterion | Points | Excellent | Good | Needs Improvement |
|-----------|--------|-----------|------|-------------------|
| **Decision Framework** | 6 | Clear framework for when to use supervised vs unsupervised, hybrid approach described | Basic framework | Poor or missing |
| **Business Recommendations** | 4 | Specific recommendations for real-world deployment, cost-benefit considered | Generic recommendations | No recommendations |

**Required Components:**
- When to use supervised (have labels, need high accuracy)
- When to use unsupervised (no labels, novel fraud patterns)
- Hybrid approach (start unsupervised, evolve to supervised)
- Real-world deployment strategy

---

## Code Quality Standards (Applied to All Projects)

### Code Quality Deductions (up to -20% per project)

| Issue | Deduction |
|-------|-----------|
| Code doesn't run | -50% to -100% (depending on severity) |
| Major errors or crashes | -30% to -50% |
| Poor code organization | -10% to -20% |
| No comments or documentation | -10% |
| Hardcoded values (should use variables) | -5% |
| Unused imports or messy code | -5% |

### Visualization Quality Standards

| Criterion | Expected |
|-----------|----------|
| **Labels** | All axes labeled with units |
| **Titles** | Descriptive titles on all plots |
| **Legends** | Legends included where needed |
| **Readability** | Appropriate font sizes, colors, and layout |
| **Relevance** | Visualizations support the analysis |

---

## Submission Requirements

### Session Projects
- Jupyter notebook (.ipynb file)
- README with brief summary
- All visualizations embedded in notebook
- Code runs without errors

### Capstone Project
- Jupyter notebook (.ipynb file)
- `supervised-vs-unsupervised-comparison.md` document
- Decision framework document
- README with comprehensive summary
- All code runs without errors

---

## Grade Scale

| Percentage | Letter Grade |
|------------|--------------|
| 90-100% | A |
| 80-89% | B |
| 70-79% | C |
| 60-69% | D |
| <60% | F |

---

## Academic Integrity

- All work must be your own
- You may use online resources for learning, but cite sources
- Copying code from classmates or online without understanding is plagiarism
- Use of AI assistants (ChatGPT, etc.) must be disclosed
- When in doubt, ask the instructor!

---

## Tips for Success

1. **Start Early**: Don't wait until the last minute
2. **Test Incrementally**: Run code cells frequently to catch errors early
3. **Comment Your Code**: Help yourself and graders understand your logic
4. **Interpret Results**: Don't just produce outputs - explain what they mean
5. **Business Context**: Always connect technical results to business value
6. **Visualize Well**: Good visualizations make insights obvious
7. **Compare Methods**: When comparing algorithms, be thorough and fair
8. **Ask Questions**: If stuck, reach out to instructors or peers

---

**Module 5 Focus:** Understanding unsupervised learning, knowing when to use it vs supervised learning, and applying clustering and anomaly detection to real-world problems!
