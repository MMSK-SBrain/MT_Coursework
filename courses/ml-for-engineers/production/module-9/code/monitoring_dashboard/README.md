# ML Model Monitoring Dashboard

A comprehensive monitoring solution for tracking machine learning model performance in production.

## Overview

This monitoring system provides real-time insights into your deployed ML models, helping you detect issues like data drift, performance degradation, and anomalies before they impact users.

## Features

### Core Capabilities

1. **Prediction Logging**
   - Log all predictions with metadata
   - Track model versions
   - Store confidence scores and response times
   - Privacy-preserving user ID hashing

2. **Real-time Monitoring Dashboard**
   - Interactive Streamlit dashboard
   - Time series visualizations
   - Distribution analysis
   - Alert notifications

3. **Drift Detection**
   - Data drift detection (KS test, T-test)
   - Concept drift monitoring
   - Statistical significance testing
   - Effect size calculation

4. **Performance Tracking**
   - Response time metrics (P50, P95, P99)
   - Request volume monitoring
   - Confidence score tracking
   - Model accuracy (when ground truth available)

5. **Automated Alerts**
   - Low confidence warnings
   - Volume anomalies
   - Response time violations
   - Prediction distribution shifts

## Installation

### Prerequisites

- Python 3.8+
- pip

### Setup

```bash
# Install dependencies
pip install streamlit pandas numpy plotly scipy

# Or use requirements file
pip install -r requirements.txt
```

Create a `requirements.txt`:
```
streamlit==1.29.0
pandas==2.1.4
numpy==1.26.2
plotly==5.18.0
scipy==1.11.4
```

## Quick Start

### 1. Initialize the Logger

```python
from logger import PredictionLogger

# Create logger instance
logger = PredictionLogger('predictions.db')

# Log a prediction
logger.log_prediction(
    model_version='v1.0.0',
    input_features={'feature1': 0.5, 'feature2': 100},
    prediction=123.45,
    confidence=0.89,
    response_time_ms=150
)
```

### 2. Integrate with Your API

Add logging to your Flask/FastAPI endpoints:

```python
from flask import Flask, request, jsonify
from logger import PredictionLogger
import time

app = Flask(__name__)
logger = PredictionLogger('predictions.db')

@app.route('/predict', methods=['POST'])
def predict():
    start_time = time.time()

    # Get input
    data = request.get_json()

    # Make prediction (your model code)
    prediction = model.predict([data['features']])[0]
    confidence = model.predict_proba([data['features']]).max()

    # Calculate response time
    response_time = (time.time() - start_time) * 1000

    # Log prediction
    logger.log_prediction(
        model_version='v1.0.0',
        input_features=data['features'],
        prediction=prediction,
        confidence=confidence,
        response_time_ms=response_time,
        user_id=data.get('user_id')
    )

    return jsonify({
        'prediction': prediction,
        'confidence': confidence
    })
```

### 3. Launch the Dashboard

```bash
streamlit run app.py
```

The dashboard will open in your browser at `http://localhost:8501`

## Dashboard Features

### Overview Section

- **Total Predictions**: Count of all predictions in selected range
- **Average Confidence**: Mean confidence score with health indicator
- **P95 Response Time**: 95th percentile latency
- **Predictions/Day**: Average daily volume

### Time Series Analysis

#### Volume Tab
- Hourly request volume
- Daily prediction counts
- Trend analysis

#### Predictions Tab
- Prediction values over time
- Rolling averages
- Distribution histograms
- Confidence score distributions

#### Performance Tab
- Response time over time
- Response time distribution
- Percentile metrics (P50, P95, P99)

### Drift Detection

- Statistical tests (Kolmogorov-Smirnov, T-test)
- Baseline vs recent comparison
- Distribution visualizations
- Automatic drift alerts

### Alerts

The dashboard automatically checks for:

1. **Low Confidence** (threshold: 0.7)
2. **Slow Response** (P95 > 1000ms)
3. **Prediction Drift** (>15% change)
4. **Volume Anomalies** (>2σ from mean)

## Advanced Usage

### Metrics Tracker

Use the `MetricsTracker` class for programmatic monitoring:

```python
from metrics_tracker import MetricsTracker
from logger import PredictionLogger

logger = PredictionLogger('predictions.db')
tracker = MetricsTracker(logger)

# Generate health report
report = tracker.generate_health_report()
print(f"Status: {report['overall_status']}")
print(f"Issues: {report['issues_detected']}")

# Check for drift
drift_result = tracker.detect_data_drift(
    baseline_days=7,
    recent_days=7
)
if drift_result['drift_detected']:
    print("⚠️ Data drift detected!")
    print(f"KS p-value: {drift_result['ks_test']['pvalue']}")

# Check confidence
confidence_result = tracker.check_confidence_degradation()
if confidence_result['degradation_detected']:
    print("⚠️ Confidence has degraded!")
    print(f"Current: {confidence_result['current_confidence']:.3f}")
```

### Batch Logging

Log multiple predictions efficiently:

```python
predictions = [
    {
        'model_version': 'v1.0.0',
        'input_features': {'x': 1, 'y': 2},
        'prediction': 100,
        'confidence': 0.9
    },
    {
        'model_version': 'v1.0.0',
        'input_features': {'x': 3, 'y': 4},
        'prediction': 200,
        'confidence': 0.85
    }
]

logger.log_batch(predictions)
```

### Query Predictions

```python
# Get recent predictions
recent = logger.get_recent_predictions(limit=100)

# Get predictions by date range
from datetime import datetime, timedelta
start = (datetime.now() - timedelta(days=7)).isoformat()
end = datetime.now().isoformat()
weekly = logger.get_predictions_by_date_range(start, end)

# Get statistics
stats = logger.get_statistics()
print(f"Total: {stats['total_predictions']}")
print(f"Mean prediction: {stats['predictions']['mean']:.2f}")
print(f"Mean confidence: {stats['confidence']['mean']:.3f}")
```

### Update Ground Truth

When actual values become available:

```python
# Update ground truth for accuracy tracking
logger.update_ground_truth(
    prediction_id=123,
    ground_truth=125.5
)
```

### Data Retention

Clean up old data:

```python
# Delete predictions older than 90 days
deleted = logger.delete_old_predictions(days=90)
print(f"Deleted {deleted} old predictions")
```

## Configuration

### Dashboard Settings

Customize the dashboard via the sidebar:

- **Database Path**: Location of predictions.db
- **Date Range**: Last 24h, 7d, 30d, or custom
- **Auto-refresh**: Enable 30-second auto-refresh

### Alert Thresholds

Modify thresholds in `metrics_tracker.py`:

```python
# Confidence threshold
confidence_result = tracker.check_confidence_degradation(
    threshold=0.7,        # Minimum acceptable confidence
    drop_threshold=0.15   # Maximum acceptable drop (15%)
)

# Volume anomaly threshold
volume_result = tracker.check_volume_anomaly(
    std_threshold=2.5     # Number of standard deviations
)

# Response time thresholds
response_result = tracker.check_response_time(
    p95_threshold_ms=1000,  # P95 threshold
    p99_threshold_ms=2000   # P99 threshold
)
```

## Privacy Considerations

### User ID Anonymization

By default, user IDs are hashed for privacy:

```python
logger.log_prediction(
    model_version='v1.0.0',
    input_features=data,
    prediction=pred,
    user_id='user_12345',
    anonymize_user=True  # Default: True
)
# Stored as: "8d969eef6ecad3c2"
```

### Sensitive Data

**DO:**
- Log aggregate statistics
- Hash/anonymize user identifiers
- Encrypt sensitive features
- Implement data retention policies

**DON'T:**
- Log PII (names, emails, addresses)
- Log credit card numbers, SSNs
- Log passwords or API keys
- Keep data indefinitely

## Monitoring Checklist

### Daily
- [ ] Check dashboard for alerts
- [ ] Review request volume
- [ ] Monitor response times

### Weekly
- [ ] Analyze drift detection
- [ ] Review confidence trends
- [ ] Check prediction distributions

### Monthly
- [ ] Generate health reports
- [ ] Update ground truth data
- [ ] Clean up old predictions
- [ ] Review and adjust thresholds

## Troubleshooting

### Database Issues

**Problem:** `no such table: predictions`

**Solution:**
```python
logger = PredictionLogger('predictions.db')
logger.init_database()  # Recreate schema
```

### Dashboard Not Loading

**Problem:** Dashboard shows no data

**Solution:**
1. Check database path in sidebar
2. Verify predictions are being logged
3. Check date range settings
4. Run: `logger.get_statistics()` to verify data

### Performance Issues

**Problem:** Dashboard is slow

**Solution:**
1. Limit date range
2. Create indexes on timestamp column
3. Archive old predictions
4. Use batch queries instead of individual

## Best Practices

1. **Log Everything**: Capture all predictions with metadata
2. **Monitor Continuously**: Set up auto-refresh or scheduled reports
3. **Set Reasonable Thresholds**: Based on your model's characteristics
4. **Act on Alerts**: Don't ignore warnings
5. **Track Ground Truth**: Update when actual values are available
6. **Regular Cleanup**: Implement data retention policies
7. **Document Changes**: Note when model versions change
8. **Test Alerts**: Simulate issues to verify alerting works

## Integration Examples

### With Heroku Deployment

```python
# app.py
import os
from logger import PredictionLogger

# Use environment variable for database path
DB_PATH = os.environ.get('DATABASE_URL', 'predictions.db')
logger = PredictionLogger(DB_PATH)
```

### With Scheduled Reports

```python
# report_job.py
from metrics_tracker import MetricsTracker
from logger import PredictionLogger
import smtplib
from email.mime.text import MIMEText

logger = PredictionLogger('predictions.db')
tracker = MetricsTracker(logger)

# Generate report
report = tracker.generate_health_report()

# Send email if issues detected
if report['overall_status'] != 'HEALTHY':
    msg = MIMEText(f"Status: {report['overall_status']}\n"
                   f"Issues: {report['issues_detected']}")
    msg['Subject'] = 'ML Model Alert'
    msg['From'] = 'monitoring@example.com'
    msg['To'] = 'team@example.com'

    # Send email (configure SMTP)
    # smtp.send_message(msg)
```

### With Cron Job

```bash
# Run health check every hour
0 * * * * cd /path/to/monitoring && python report_job.py
```

## API Reference

### PredictionLogger

- `log_prediction()`: Log single prediction
- `log_batch()`: Log multiple predictions
- `get_recent_predictions()`: Get N most recent
- `get_predictions_by_date_range()`: Query by date
- `get_statistics()`: Get summary stats
- `update_ground_truth()`: Add actual values
- `delete_old_predictions()`: Clean up old data

### MetricsTracker

- `detect_data_drift()`: Statistical drift detection
- `check_confidence_degradation()`: Monitor confidence
- `check_volume_anomaly()`: Detect unusual traffic
- `check_response_time()`: Monitor latency
- `generate_health_report()`: Complete health check

## Resources

- [Streamlit Documentation](https://docs.streamlit.io/)
- [ML Monitoring Best Practices](https://ml-ops.org/content/mlops-principles)
- [Data Drift Detection](https://www.evidentlyai.com/blog/data-drift-detection)

## Support

For issues or questions:
1. Check this README
2. Review course materials (Session 9.5)
3. Examine example code
4. Check Streamlit logs: `~/.streamlit/logs/`

## License

MIT License - see course materials for details.
