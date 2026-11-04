# Stock Price Predictor API - Deployment Guide

A production-ready Flask API for stock price prediction using machine learning.

## Overview

This API provides real-time stock price predictions using a Random Forest regression model. It's designed to be deployed on Heroku (or any cloud platform) and includes features like:

- RESTful API endpoints
- Input validation
- Error handling
- Health monitoring
- API key authentication (optional)
- Batch predictions
- Comprehensive logging

## Features

### Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | API information and available endpoints |
| `/health` | GET | Health check for monitoring |
| `/info` | GET | Model information and required features |
| `/predict` | POST | Single prediction |
| `/batch_predict` | POST | Multiple predictions in one request |

## Local Development

### Prerequisites

- Python 3.11+
- pip
- virtualenv (recommended)

### Setup

1. **Clone or navigate to the directory:**
   ```bash
   cd stock_predictor_deployment
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Train and save a model (or use existing):**
   ```bash
   # Run the training code from session-9.4 notebook
   # This creates stock_model.pkl
   ```

5. **Run locally with Flask (development):**
   ```bash
   python app.py
   ```

6. **Run with Gunicorn (production-like):**
   ```bash
   gunicorn app:app
   ```

7. **Test the API:**
   ```bash
   # Health check
   curl http://localhost:5000/health

   # Get model info
   curl http://localhost:5000/info

   # Make a prediction
   curl -X POST http://localhost:5000/predict \
     -H "Content-Type: application/json" \
     -d '{
       "day_of_year": 350,
       "day_of_week": 3,
       "trend": 500,
       "price_lag_1": 195.5,
       "price_lag_7": 193.2,
       "price_lag_30": 188.7,
       "rolling_mean_7": 194.3,
       "rolling_std_7": 2.1
     }'
   ```

## Heroku Deployment

### Prerequisites

- Heroku account (free tier available)
- Heroku CLI installed
- Git installed

### Deployment Steps

1. **Login to Heroku:**
   ```bash
   heroku login
   ```

2. **Initialize Git repository:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Stock predictor API"
   ```

3. **Create Heroku app:**
   ```bash
   heroku create your-app-name
   # Or let Heroku generate a random name:
   heroku create
   ```

4. **Deploy to Heroku:**
   ```bash
   git push heroku main
   ```

5. **Check deployment status:**
   ```bash
   heroku ps
   heroku logs --tail
   ```

6. **Open your app:**
   ```bash
   heroku open
   ```

### Configuration (Environment Variables)

Set environment variables on Heroku:

```bash
# Optional: Set API key for authentication
heroku config:set API_KEY=your-secret-key

# Set model version
heroku config:set MODEL_VERSION=v1.0.0

# Disable debug mode in production
heroku config:set DEBUG=False

# View all config
heroku config
```

## API Usage

### Making Predictions

#### Single Prediction

**Request:**
```bash
curl -X POST https://your-app-name.herokuapp.com/predict \
  -H "Content-Type: application/json" \
  -H "X-API-Key: your-secret-key" \
  -d '{
    "day_of_year": 350,
    "day_of_week": 3,
    "trend": 500,
    "price_lag_1": 195.5,
    "price_lag_7": 193.2,
    "price_lag_30": 188.7,
    "rolling_mean_7": 194.3,
    "rolling_std_7": 2.1
  }'
```

**Response:**
```json
{
  "predicted_price": 196.45,
  "model_version": "v1.0.0",
  "timestamp": "2024-01-06T10:30:00.123456",
  "input_features": {
    "day_of_year": 350,
    "day_of_week": 3,
    "trend": 500,
    "price_lag_1": 195.5,
    "price_lag_7": 193.2,
    "price_lag_30": 188.7,
    "rolling_mean_7": 194.3,
    "rolling_std_7": 2.1
  }
}
```

#### Batch Predictions

**Request:**
```bash
curl -X POST https://your-app-name.herokuapp.com/batch_predict \
  -H "Content-Type: application/json" \
  -d '{
    "predictions": [
      {
        "day_of_year": 350,
        "day_of_week": 3,
        "trend": 500,
        "price_lag_1": 195.5,
        "price_lag_7": 193.2,
        "price_lag_30": 188.7,
        "rolling_mean_7": 194.3,
        "rolling_std_7": 2.1
      },
      {
        "day_of_year": 351,
        "day_of_week": 4,
        "trend": 501,
        "price_lag_1": 196.2,
        "price_lag_7": 194.1,
        "price_lag_30": 189.3,
        "rolling_mean_7": 195.1,
        "rolling_std_7": 2.3
      }
    ]
  }'
```

### Python Client Example

```python
import requests
import json

# API configuration
API_URL = "https://your-app-name.herokuapp.com"
API_KEY = "your-secret-key"  # Optional

headers = {
    "Content-Type": "application/json",
    "X-API-Key": API_KEY
}

# Make prediction
data = {
    "day_of_year": 350,
    "day_of_week": 3,
    "trend": 500,
    "price_lag_1": 195.5,
    "price_lag_7": 193.2,
    "price_lag_30": 188.7,
    "rolling_mean_7": 194.3,
    "rolling_std_7": 2.1
}

response = requests.post(
    f"{API_URL}/predict",
    headers=headers,
    json=data
)

if response.status_code == 200:
    result = response.json()
    print(f"Predicted price: ${result['predicted_price']}")
else:
    print(f"Error: {response.json()}")
```

## Required Features

The model expects the following 8 features:

| Feature | Type | Description | Range |
|---------|------|-------------|-------|
| `day_of_year` | int | Day of the year (1-366) | 1-366 |
| `day_of_week` | int | Day of the week (0=Monday, 6=Sunday) | 0-6 |
| `trend` | float | Overall trend indicator | Any |
| `price_lag_1` | float | Price from 1 day ago | Any positive |
| `price_lag_7` | float | Price from 7 days ago | Any positive |
| `price_lag_30` | float | Price from 30 days ago | Any positive |
| `rolling_mean_7` | float | 7-day rolling average | Any positive |
| `rolling_std_7` | float | 7-day rolling standard deviation | Any positive |

## Troubleshooting

### Common Issues

#### 1. Application Error (H10)

**Symptoms:** "Application Error" when visiting URL

**Solutions:**
- Check logs: `heroku logs --tail`
- Verify Procfile is correct
- Ensure all dependencies in requirements.txt
- Check Python version in runtime.txt

#### 2. Module Not Found

**Symptoms:** `ModuleNotFoundError: No module named 'sklearn'`

**Solutions:**
- Verify requirements.txt includes `scikit-learn`
- Regenerate requirements: `pip freeze > requirements.txt`
- Redeploy: `git add requirements.txt && git commit -m "Update deps" && git push heroku main`

#### 3. Model File Not Found

**Symptoms:** `FileNotFoundError: [Errno 2] No such file or directory: 'stock_model.pkl'`

**Solutions:**
- Ensure model file is committed to Git
- Check .gitignore doesn't exclude .pkl files
- Model file must be in the same directory as app.py

#### 4. Memory Exceeded (R14)

**Symptoms:** App crashes with "Memory quota exceeded"

**Solutions:**
- Optimize model size (use model compression)
- Implement lazy loading (already included in app.py)
- Upgrade dyno: `heroku ps:scale web=1:standard-2x`

### Viewing Logs

```bash
# Real-time logs
heroku logs --tail

# Last 100 lines
heroku logs -n 100

# Filter for errors
heroku logs --tail | grep "ERROR"
```

## Monitoring & Maintenance

### Health Checks

The `/health` endpoint returns the application status:

```bash
curl https://your-app-name.herokuapp.com/health
```

Response:
```json
{
  "status": "healthy",
  "model_loaded": true,
  "model_version": "v1.0.0",
  "timestamp": "2024-01-06T10:30:00.123456"
}
```

### Scaling

```bash
# Scale to 2 dynos (horizontal scaling)
heroku ps:scale web=2

# Check current scaling
heroku ps
```

### Updating the Model

1. Train new model
2. Save as `stock_model.pkl`
3. Update MODEL_VERSION environment variable
4. Deploy:
   ```bash
   git add stock_model.pkl
   git commit -m "Update model to v2.0.0"
   git push heroku main
   heroku config:set MODEL_VERSION=v2.0.0
   ```

## Security Best Practices

1. **Use HTTPS:** Heroku provides free SSL
2. **API Key Authentication:** Set `API_KEY` environment variable
3. **Input Validation:** Already implemented in app.py
4. **Rate Limiting:** Consider adding with Flask-Limiter
5. **Keep Dependencies Updated:** Regularly update requirements.txt
6. **Environment Variables:** Never hardcode secrets

## Cost Considerations

### Heroku Free Tier
- **Cost:** $0/month
- **Hours:** 550-1000 dyno hours/month
- **RAM:** 512MB
- **Sleeping:** App sleeps after 30min inactivity
- **Best for:** Development, demos, portfolio projects

### Heroku Hobby Tier
- **Cost:** $7/month
- **Hours:** Always on (no sleeping)
- **RAM:** 512MB
- **Best for:** Production apps with low traffic

## File Structure

```
stock_predictor_deployment/
├── app.py                 # Main Flask application
├── stock_model.pkl        # Trained ML model
├── requirements.txt       # Python dependencies
├── Procfile              # Heroku process configuration
├── runtime.txt           # Python version specification
└── README.md             # This file
```

## License

MIT License - see course materials for details.

## Support

For issues or questions:
1. Check this README
2. Review course materials (Session 9.4)
3. Check Heroku logs: `heroku logs --tail`
4. Consult Heroku documentation: https://devcenter.heroku.com/

## Next Steps

After deploying this API, consider:

1. **Add Monitoring** (Session 9.5)
   - Log all predictions
   - Track model performance
   - Build monitoring dashboard

2. **A/B Testing** (Session 9.6)
   - Deploy multiple model versions
   - Compare performance
   - Gradual rollout strategies

3. **Enhancements**
   - Add caching (Redis)
   - Rate limiting
   - Better error messages
   - API documentation (Swagger)
   - CI/CD pipeline (GitHub Actions)

## Resources

- [Heroku Python Guide](https://devcenter.heroku.com/categories/python-support)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Gunicorn Documentation](https://docs.gunicorn.org/)
- [ML Deployment Best Practices](https://ml-ops.org/)
