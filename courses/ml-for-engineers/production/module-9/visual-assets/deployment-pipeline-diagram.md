# ML Deployment Pipeline Diagram

## Complete End-to-End ML Deployment Flow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          ML DEPLOYMENT PIPELINE                              │
└─────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────┐
│   1. DEVELOPMENT     │
│   ────────────────   │
│                      │
│  ┌───────────────┐  │
│  │ Jupyter       │  │
│  │ Notebook      │  │
│  │               │  │
│  │ • EDA         │  │
│  │ • Feature Eng │  │
│  │ • Train Model │  │
│  │ • Evaluate    │  │
│  └───────┬───────┘  │
│          │          │
│          ▼          │
│  ┌───────────────┐  │
│  │ Local Testing │  │
│  │               │  │
│  │ • Test Data   │  │
│  │ • Validation  │  │
│  │ • Metrics OK? │  │
│  └───────┬───────┘  │
└──────────┼──────────┘
           │
           │ Model meets
           │ performance
           │ criteria
           ▼
┌──────────────────────┐
│  2. SERIALIZATION    │
│  ─────────────────   │
│                      │
│  ┌───────────────┐  │
│  │ Save Model    │  │
│  │               │  │
│  │ model.pkl     │  │
│  │ (joblib)      │  │
│  └───────┬───────┘  │
│          │          │
│          ▼          │
│  ┌───────────────┐  │
│  │ Save Pipeline │  │
│  │               │  │
│  │ • Scaler      │  │
│  │ • Encoder     │  │
│  │ • Vectorizer  │  │
│  └───────┬───────┘  │
│          │          │
│          ▼          │
│  ┌───────────────┐  │
│  │ Version       │  │
│  │ & Metadata    │  │
│  │               │  │
│  │ v1.0.0        │  │
│  │ metrics.json  │  │
│  └───────┬───────┘  │
└──────────┼──────────┘
           │
           ▼
┌──────────────────────┐
│   3. API CREATION    │
│   ────────────────   │
│                      │
│  ┌───────────────┐  │
│  │ Flask/FastAPI │  │
│  │               │  │
│  │ app.py        │  │
│  └───────┬───────┘  │
│          │          │
│          ▼          │
│  ┌───────────────┐  │
│  │ Endpoints     │  │
│  │               │  │
│  │ POST /predict │  │
│  │ GET  /health  │  │
│  │ GET  /        │  │
│  └───────┬───────┘  │
│          │          │
│          ▼          │
│  ┌───────────────┐  │
│  │ Error         │  │
│  │ Handling      │  │
│  │               │  │
│  │ • Validation  │  │
│  │ • Try/Except  │  │
│  │ • HTTP Codes  │  │
│  └───────┬───────┘  │
└──────────┼──────────┘
           │
           │ Local
           │ Testing
           ▼
┌──────────────────────┐
│  4. CONTAINERIZATION │
│  (Optional)          │
│  ─────────────────   │
│                      │
│  ┌───────────────┐  │
│  │ Dockerfile    │  │
│  │               │  │
│  │ FROM python   │  │
│  │ COPY ...      │  │
│  │ RUN pip ...   │  │
│  │ CMD ["..."]   │  │
│  └───────┬───────┘  │
│          │          │
│          ▼          │
│  ┌───────────────┐  │
│  │ Build Image   │  │
│  │               │  │
│  │ docker build  │  │
│  └───────┬───────┘  │
│          │          │
│          ▼          │
│  ┌───────────────┐  │
│  │ Test Container│  │
│  │               │  │
│  │ docker run    │  │
│  └───────┬───────┘  │
└──────────┼──────────┘
           │
           ▼
┌──────────────────────┐
│  5. CLOUD DEPLOYMENT │
│  ─────────────────   │
│                      │
│  ┌───────────────┐  │
│  │ Version       │  │
│  │ Control       │  │
│  │               │  │
│  │ git init      │  │
│  │ git add .     │  │
│  │ git commit    │  │
│  └───────┬───────┘  │
│          │          │
│          ▼          │
│  ┌───────────────┐  │
│  │ Platform      │  │
│  │ Config        │  │
│  │               │  │
│  │ Procfile      │  │
│  │ runtime.txt   │  │
│  │ requirements  │  │
│  └───────┬───────┘  │
│          │          │
│          ▼          │
│  ┌───────────────┐  │
│  │ Deploy        │  │
│  │               │  │
│  │ git push      │  │
│  │ heroku main   │  │
│  └───────┬───────┘  │
└──────────┼──────────┘
           │
           │ Public URL
           │ Generated
           ▼
┌──────────────────────┐
│  6. PRODUCTION       │
│  ─────────────────   │
│                      │
│  ┌───────────────┐  │
│  │ API Server    │  │
│  │               │  │
│  │ https://...   │  │
│  │               │  │
│  │ ┌─────────┐   │  │
│  │ │ Model   │   │  │
│  │ └─────────┘   │  │
│  └───────┬───────┘  │
│          │          │
│          ▼          │
│  ┌───────────────┐  │
│  │ User Requests │  │
│  │               │  │
│  │ Web → API     │  │
│  │ Mobile → API  │  │
│  │ Other → API   │  │
│  └───────┬───────┘  │
│          │          │
│          ▼          │
│  ┌───────────────┐  │
│  │ Responses     │  │
│  │               │  │
│  │ Predictions   │  │
│  │ JSON          │  │
│  └───────────────┘  │
└──────────────────────┘
           │
           │
           ▼
┌──────────────────────┐
│  7. MONITORING       │
│  ─────────────────   │
│                      │
│  ┌───────────────┐  │
│  │ Logging       │  │
│  │               │  │
│  │ • Requests    │  │
│  │ • Predictions │  │
│  │ • Errors      │  │
│  └───────┬───────┘  │
│          │          │
│          ▼          │
│  ┌───────────────┐  │
│  │ Metrics       │  │
│  │               │  │
│  │ • Volume      │  │
│  │ • Latency     │  │
│  │ • Confidence  │  │
│  └───────┬───────┘  │
│          │          │
│          ▼          │
│  ┌───────────────┐  │
│  │ Dashboard     │  │
│  │               │  │
│  │ Visualize     │  │
│  │ Metrics       │  │
│  └───────┬───────┘  │
│          │          │
│          ▼          │
│  ┌───────────────┐  │
│  │ Alerts        │  │
│  │               │  │
│  │ • Low Conf    │  │
│  │ • High Errors │  │
│  │ • Data Drift  │  │
│  └───────┬───────┘  │
└──────────┼──────────┘
           │
           │ Issues
           │ Detected?
           ▼
┌──────────────────────┐
│  8. MAINTENANCE      │
│  ─────────────────   │
│                      │
│  ┌───────────────┐  │
│  │ Model Update  │  │
│  │               │  │
│  │ • Retrain     │  │
│  │ • New Data    │  │
│  │ • Save v2.0.0 │  │
│  └───────┬───────┘  │
│          │          │
│          ▼          │
│  ┌───────────────┐  │
│  │ A/B Testing   │  │
│  │               │  │
│  │ v1.0 ← 90%    │  │
│  │ v2.0 ← 10%    │  │
│  └───────┬───────┘  │
│          │          │
│          ▼          │
│  ┌───────────────┐  │
│  │ Compare       │  │
│  │               │  │
│  │ Which better? │  │
│  └───────┬───────┘  │
│          │          │
│          ├─ v2 Better ─→ Gradual Rollout
│          │
│          └─ v1 Better ─→ Rollback to v1
│                      │
└─────────────────────┼┘
                      │
                      │
                      └──→ Back to Production
                           (Continuous Cycle)


═══════════════════════════════════════════════════════════════════════════════

KEY COMPONENTS:

┌─────────────────┐
│ Development     │  Where you train and test models
└─────────────────┘

┌─────────────────┐
│ Serialization   │  Save model + pipeline + metadata
└─────────────────┘

┌─────────────────┐
│ API Creation    │  Wrap model in REST API
└─────────────────┘

┌─────────────────┐
│ Deployment      │  Push to cloud platform
└─────────────────┘

┌─────────────────┐
│ Production      │  Serve predictions to users
└─────────────────┘

┌─────────────────┐
│ Monitoring      │  Track performance and issues
└─────────────────┘

┌─────────────────┐
│ Maintenance     │  Update and improve models
└─────────────────┘

═══════════════════════════════════════════════════════════════════════════════

CRITICAL FILES NEEDED:

Development:
  • model_training.ipynb    (Jupyter notebook)
  • data/                   (Training data)

Serialization:
  • model.pkl               (Saved model)
  • pipeline.pkl            (Preprocessing)
  • metadata.json           (Version info)

API:
  • app.py                  (Flask/FastAPI app)
  • requirements.txt        (Dependencies)

Deployment:
  • Procfile                (Heroku: how to run)
  • runtime.txt             (Python version)
  • .gitignore              (Exclude secrets)

Monitoring:
  • logging config          (Track requests)
  • dashboard.py            (Visualization)

═══════════════════════════════════════════════════════════════════════════════

DECISION POINTS:

1. Model Performance OK?
   YES → Continue to Serialization
   NO → Return to Development

2. API Works Locally?
   YES → Deploy to Cloud
   NO → Fix Errors

3. Deployment Successful?
   YES → Monitor in Production
   NO → Check Logs, Troubleshoot

4. New Model Better?
   YES → Gradual Rollout
   NO → Keep Current Model

═══════════════════════════════════════════════════════════════════════════════

TIME ESTIMATES:

Development:           2-4 hours (model already trained)
Serialization:         15-30 minutes
API Creation:          1-2 hours
Deployment:            30-60 minutes
Monitoring Setup:      1-2 hours
A/B Testing:           2-3 hours

TOTAL: 7-12 hours for complete deployment

═══════════════════════════════════════════════════════════════════════════════
```

## Usage Instructions

This diagram shows the complete journey of an ML model from development to production:

1. **Read top-to-bottom** - Follow the arrows
2. **Boxes** represent stages/activities
3. **Arrows** show flow and decisions
4. **Dotted lines** indicate optional paths

## For Instructors:

- Walk through each stage during lectures
- Emphasize critical files needed
- Point out common failure points
- Use for project planning

## For Students:

- Use as checklist for projects
- Refer to when stuck
- Understand complete workflow
- Plan deployment timeline

---

**Created:** 2026-01-06
**Module:** 9 - Deployment & MLOps
