"""
FastAPI Backend for Sentiment Analysis ML Application

This module provides a production-ready REST API for sentiment analysis,
including health checks, versioning, and statistics tracking.
"""

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Dict, List, Optional
import logging
from datetime import datetime
import json
from pathlib import Path

from ml_service import SentimentAnalyzer

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="Sentiment Analysis API",
    description="Production-ready sentiment analysis service for text classification",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize ML service
analyzer = None
prediction_stats = {
    "total_predictions": 0,
    "positive_count": 0,
    "negative_count": 0,
    "neutral_count": 0,
    "predictions": []
}

# Request/Response Models
class TextInput(BaseModel):
    """Input schema for sentiment analysis"""
    text: str = Field(..., min_length=1, max_length=5000,
                     description="Text to analyze (1-5000 characters)")
    include_details: bool = Field(default=False,
                                  description="Include detailed analysis")

class PredictionResponse(BaseModel):
    """Response schema for sentiment prediction"""
    text: str
    sentiment: str
    confidence: float
    timestamp: str
    model_version: str
    details: Optional[Dict] = None

class HealthResponse(BaseModel):
    """Health check response"""
    status: str
    model_loaded: bool
    timestamp: str
    version: str

class StatsResponse(BaseModel):
    """Statistics response"""
    total_predictions: int
    positive_count: int
    negative_count: int
    neutral_count: int
    positive_percentage: float
    negative_percentage: float
    neutral_percentage: float
    recent_predictions: List[Dict]


@app.on_event("startup")
async def startup_event():
    """Initialize model on startup"""
    global analyzer
    try:
        logger.info("Loading sentiment analysis model...")
        analyzer = SentimentAnalyzer()
        logger.info("Model loaded successfully!")
    except Exception as e:
        logger.error(f"Failed to load model: {str(e)}")
        raise


@app.get("/", tags=["General"])
async def root():
    """Root endpoint with API information"""
    return {
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


@app.get("/health", response_model=HealthResponse, tags=["Monitoring"])
async def health_check():
    """
    Health check endpoint

    Returns:
        Health status including model availability
    """
    return {
        "status": "healthy" if analyzer else "unhealthy",
        "model_loaded": analyzer is not None,
        "timestamp": datetime.now().isoformat(),
        "version": "1.0.0"
    }


@app.get("/version", tags=["Monitoring"])
async def get_version():
    """
    Get API and model version information

    Returns:
        Version details
    """
    model_version = analyzer.get_version() if analyzer else "unknown"
    return {
        "api_version": "1.0.0",
        "model_version": model_version,
        "framework": "FastAPI",
        "ml_library": "scikit-learn / transformers"
    }


@app.post("/predict", response_model=PredictionResponse, tags=["Prediction"])
async def predict_sentiment(input_data: TextInput, request: Request):
    """
    Predict sentiment for given text

    Args:
        input_data: Text input with optional details flag

    Returns:
        Sentiment prediction with confidence score

    Raises:
        HTTPException: If prediction fails
    """
    if not analyzer:
        logger.error("Model not loaded")
        raise HTTPException(status_code=503, detail="Model not available")

    try:
        # Get prediction
        result = analyzer.predict(input_data.text, input_data.include_details)

        # Update statistics
        prediction_stats["total_predictions"] += 1
        sentiment = result["sentiment"]

        if sentiment == "positive":
            prediction_stats["positive_count"] += 1
        elif sentiment == "negative":
            prediction_stats["negative_count"] += 1
        else:
            prediction_stats["neutral_count"] += 1

        # Store recent prediction (keep last 100)
        prediction_record = {
            "timestamp": result["timestamp"],
            "text_preview": input_data.text[:50] + "..." if len(input_data.text) > 50 else input_data.text,
            "sentiment": sentiment,
            "confidence": result["confidence"],
            "client_ip": request.client.host
        }
        prediction_stats["predictions"].append(prediction_record)
        if len(prediction_stats["predictions"]) > 100:
            prediction_stats["predictions"].pop(0)

        # Log prediction
        logger.info(f"Prediction made: {sentiment} ({result['confidence']:.2f})")

        return result

    except Exception as e:
        logger.error(f"Prediction error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")


@app.get("/stats", response_model=StatsResponse, tags=["Monitoring"])
async def get_statistics():
    """
    Get prediction statistics

    Returns:
        Aggregated statistics and recent predictions
    """
    total = prediction_stats["total_predictions"]

    if total == 0:
        percentages = {"positive": 0.0, "negative": 0.0, "neutral": 0.0}
    else:
        percentages = {
            "positive": (prediction_stats["positive_count"] / total) * 100,
            "negative": (prediction_stats["negative_count"] / total) * 100,
            "neutral": (prediction_stats["neutral_count"] / total) * 100
        }

    return {
        "total_predictions": total,
        "positive_count": prediction_stats["positive_count"],
        "negative_count": prediction_stats["negative_count"],
        "neutral_count": prediction_stats["neutral_count"],
        "positive_percentage": round(percentages["positive"], 2),
        "negative_percentage": round(percentages["negative"], 2),
        "neutral_percentage": round(percentages["neutral"], 2),
        "recent_predictions": prediction_stats["predictions"][-20:]  # Last 20
    }


@app.post("/reset-stats", tags=["Monitoring"])
async def reset_statistics():
    """Reset prediction statistics (for testing/development)"""
    global prediction_stats
    prediction_stats = {
        "total_predictions": 0,
        "positive_count": 0,
        "negative_count": 0,
        "neutral_count": 0,
        "predictions": []
    }
    logger.info("Statistics reset")
    return {"message": "Statistics reset successfully"}


# Error handlers
@app.exception_handler(404)
async def not_found_handler(request: Request, exc):
    return {
        "error": "Not Found",
        "message": f"The endpoint {request.url.path} does not exist",
        "available_endpoints": ["/", "/predict", "/health", "/version", "/stats", "/docs"]
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
