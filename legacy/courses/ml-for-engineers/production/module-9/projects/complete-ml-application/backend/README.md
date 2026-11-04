# Sentiment Analysis API Backend

Production-ready FastAPI backend for sentiment analysis. Provides REST endpoints for text sentiment classification with monitoring and statistics tracking.

## Features

- **FastAPI Framework**: High-performance async API
- **Sentiment Analysis**: Classify text as positive, negative, or neutral
- **Health Monitoring**: Health check and version endpoints
- **Statistics Tracking**: Monitor predictions and distributions
- **CORS Enabled**: Cross-origin resource sharing for frontend integration
- **Auto Documentation**: Interactive API docs at `/docs`
- **Error Handling**: Comprehensive error responses
- **Logging**: Production-ready logging configuration

## API Endpoints

### 1. Root Endpoint
```
GET /
```
Returns API information and available endpoints.

**Response:**
```json
{
  "message": "Sentiment Analysis API",
  "version": "1.0.0",
  "status": "operational",
  "endpoints": {
    "predict": "/predict",
    "health": "/health",
    "version": "/version",
    "stats": "/stats",
    "docs": "/docs"
  }
}
```

### 2. Predict Sentiment
```
POST /predict
```
Analyze sentiment of provided text.

**Request Body:**
```json
{
  "text": "This product is amazing! I absolutely love it!",
  "include_details": false
}
```

**Response:**
```json
{
  "text": "This product is amazing! I absolutely love it!",
  "sentiment": "positive",
  "confidence": 0.89,
  "timestamp": "2024-01-15T10:30:00",
  "model_version": "1.0.0",
  "details": null
}
```

**With Details:**
```json
{
  "text": "This product is amazing! I absolutely love it!",
  "sentiment": "positive",
  "confidence": 0.89,
  "timestamp": "2024-01-15T10:30:00",
  "model_version": "1.0.0",
  "details": {
    "preprocessed_text": "this product is amazing i absolutely love it",
    "text_length": 45,
    "word_count": 8,
    "method": "rule_based",
    "positive_score": 3.5,
    "negative_score": 0.0
  }
}
```

### 3. Health Check
```
GET /health
```
Check API health status.

**Response:**
```json
{
  "status": "healthy",
  "model_loaded": true,
  "timestamp": "2024-01-15T10:30:00",
  "version": "1.0.0"
}
```

### 4. Version Information
```
GET /version
```
Get API and model version details.

**Response:**
```json
{
  "api_version": "1.0.0",
  "model_version": "1.0.0",
  "framework": "FastAPI",
  "ml_library": "scikit-learn / transformers"
}
```

### 5. Statistics
```
GET /stats
```
Get prediction statistics and analytics.

**Response:**
```json
{
  "total_predictions": 150,
  "positive_count": 80,
  "negative_count": 50,
  "neutral_count": 20,
  "positive_percentage": 53.33,
  "negative_percentage": 33.33,
  "neutral_percentage": 13.33,
  "recent_predictions": [
    {
      "timestamp": "2024-01-15T10:30:00",
      "text_preview": "This product is amazing! I absolutely love...",
      "sentiment": "positive",
      "confidence": 0.89,
      "client_ip": "127.0.0.1"
    }
  ]
}
```

### 6. Reset Statistics (Development)
```
POST /reset-stats
```
Reset prediction statistics to zero.

## Local Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone or navigate to the backend directory:**
```bash
cd backend
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

### Running Locally

**Development mode with auto-reload:**
```bash
uvicorn main:app --reload
```

**Production mode:**
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

**Access the API:**
- API Root: http://localhost:8000
- Interactive Docs: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Deployment to Heroku

### Prerequisites
- Heroku account
- Heroku CLI installed
- Git initialized in project

### Deployment Steps

1. **Login to Heroku:**
```bash
heroku login
```

2. **Create Heroku app:**
```bash
heroku create your-sentiment-api
```

3. **Deploy:**
```bash
git add .
git commit -m "Deploy sentiment analysis API"
git push heroku main
```

4. **Open the app:**
```bash
heroku open
```

5. **View logs:**
```bash
heroku logs --tail
```

### Environment Variables

Set environment variables on Heroku:
```bash
heroku config:set MODEL_VERSION=1.0.0
heroku config:set LOG_LEVEL=INFO
```

## Testing

### Run Tests
```bash
pytest tests/ -v
```

### Test Coverage
```bash
pytest --cov=. --cov-report=html
```

### Manual Testing with curl

**Health Check:**
```bash
curl http://localhost:8000/health
```

**Predict Sentiment:**
```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "This is amazing!", "include_details": true}'
```

**Get Statistics:**
```bash
curl http://localhost:8000/stats
```

## Architecture

```
backend/
├── main.py              # FastAPI application & endpoints
├── ml_service.py        # ML model service & predictions
├── requirements.txt     # Python dependencies
├── Procfile            # Heroku deployment config
└── README.md           # This file
```

## ML Service

The `ml_service.py` module provides:

### SentimentAnalyzer Class
- **Preprocessing**: Text cleaning and normalization
- **Rule-Based Analysis**: Fast sentiment classification using keyword matching
- **ML Model Support**: Can load trained scikit-learn or transformer models
- **Version Management**: Track model versions
- **Confidence Scoring**: Probability-based confidence levels

### Sentiment Categories
- **Positive**: Happy, satisfied, enthusiastic text
- **Negative**: Unhappy, critical, disappointed text
- **Neutral**: Factual, balanced, or ambiguous text

## Error Handling

The API provides comprehensive error responses:

**Invalid Input:**
```json
{
  "detail": "Text cannot be empty"
}
```

**Model Not Available:**
```json
{
  "detail": "Model not available"
}
```

**Internal Error:**
```json
{
  "detail": "Prediction failed: <error message>"
}
```

## Performance Considerations

- **Async Processing**: FastAPI async endpoints for concurrent requests
- **Model Caching**: Model loaded once at startup
- **Lightweight Rules**: Fast rule-based analysis for production
- **Request Validation**: Pydantic models for input validation
- **Response Compression**: Automatic compression for large responses

## Security

- **Input Validation**: Length limits and type checking
- **CORS Configuration**: Configure allowed origins for production
- **Rate Limiting**: Consider adding rate limiting for production
- **API Keys**: Add authentication for production deployment

## Monitoring

Built-in monitoring features:
- Request logging
- Prediction statistics
- Health checks
- Error tracking
- Performance metrics

## Troubleshooting

### Common Issues

**Port Already in Use:**
```bash
# Kill process on port 8000
lsof -ti:8000 | xargs kill -9
```

**Dependencies Error:**
```bash
# Reinstall dependencies
pip install --upgrade -r requirements.txt
```

**Model Not Loading:**
- Check model file path
- Verify model format compatibility
- Check logs for detailed error messages

## Next Steps

1. **Add Authentication**: Implement API key authentication
2. **Add Rate Limiting**: Prevent API abuse
3. **Database Integration**: Store predictions in PostgreSQL
4. **Model Updates**: Implement model versioning and A/B testing
5. **Caching**: Add Redis for response caching
6. **Metrics**: Integrate Prometheus for metrics collection

## Support

For issues and questions:
- Check `/docs` for interactive API documentation
- Review logs: `heroku logs --tail` (production)
- Consult FastAPI documentation: https://fastapi.tiangolo.com/

## License

This project is for educational purposes as part of the ML for Engineers course.
