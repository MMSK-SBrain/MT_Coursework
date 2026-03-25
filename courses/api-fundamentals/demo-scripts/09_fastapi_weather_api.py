#!/usr/bin/env python3
"""
FastAPI Demo 3: Weather API Server
----------------------------------
A weather API that acts as a proxy to OpenWeatherMap.

This shows how real APIs often:
1. Wrap other APIs
2. Add authentication
3. Transform/simplify data
4. Add caching (not implemented here, but mentioned)

To run:
1. pip install fastapi uvicorn requests
2. Set your API key below
3. uvicorn 09_fastapi_weather_api:app --reload
4. Open: http://localhost:8000/docs
"""

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
import requests
from typing import Optional

# ============================================================
# Configuration
# ============================================================
OPENWEATHER_API_KEY = "YOUR_API_KEY_HERE"  # Replace with your key
OPENWEATHER_BASE_URL = "https://api.openweathermap.org/data/2.5"

# ============================================================
# FastAPI App
# ============================================================
app = FastAPI(
    title="Weather API",
    description="""
    A simplified weather API that wraps OpenWeatherMap.

    This demonstrates how APIs often:
    - Wrap and simplify other APIs
    - Transform data into cleaner formats
    - Hide implementation details (API keys)
    """,
    version="1.0.0"
)

# ============================================================
# Response Models
# ============================================================
class WeatherResponse(BaseModel):
    """Simplified weather response."""
    city: str
    country: str
    temperature: float
    feels_like: float
    humidity: int
    conditions: str
    wind_speed: float
    icon: str

class ForecastDay(BaseModel):
    """Single day forecast."""
    date: str
    temperature_high: float
    temperature_low: float
    conditions: str

class ErrorResponse(BaseModel):
    """Error response."""
    error: str
    detail: str

# ============================================================
# API Endpoints
# ============================================================

@app.get("/", tags=["Root"])
def root():
    """API information."""
    return {
        "name": "Weather API",
        "version": "1.0.0",
        "endpoints": {
            "GET /weather/{city}": "Get current weather for a city",
            "GET /weather": "Get weather with query parameters",
        },
        "docs": "/docs"
    }

@app.get("/weather/{city}", response_model=WeatherResponse, tags=["Weather"])
def get_weather_by_path(city: str):
    """
    Get current weather for a city.

    - **city**: City name (e.g., "London", "Tokyo", "New York")
    """
    return fetch_weather(city)

@app.get("/weather", response_model=WeatherResponse, tags=["Weather"])
def get_weather_by_query(
    city: str = Query(..., description="City name", example="London"),
    units: str = Query("metric", description="Units: metric or imperial")
):
    """
    Get current weather with query parameters.

    - **city**: City name
    - **units**: Temperature units (metric=Celsius, imperial=Fahrenheit)
    """
    return fetch_weather(city, units)

# ============================================================
# Helper Functions
# ============================================================

def fetch_weather(city: str, units: str = "metric") -> dict:
    """Fetch weather from OpenWeatherMap and transform the response."""

    url = f"{OPENWEATHER_BASE_URL}/weather"
    params = {
        "q": city,
        "appid": OPENWEATHER_API_KEY,
        "units": units
    }

    try:
        response = requests.get(url, params=params, timeout=10)

        if response.status_code == 404:
            raise HTTPException(
                status_code=404,
                detail=f"City '{city}' not found. Check spelling."
            )
        elif response.status_code == 401:
            raise HTTPException(
                status_code=500,
                detail="Weather service configuration error"
            )
        elif response.status_code != 200:
            raise HTTPException(
                status_code=502,
                detail="Weather service unavailable"
            )

        data = response.json()

        # Transform the complex OpenWeatherMap response into our simpler format
        return {
            "city": data["name"],
            "country": data["sys"]["country"],
            "temperature": round(data["main"]["temp"], 1),
            "feels_like": round(data["main"]["feels_like"], 1),
            "humidity": data["main"]["humidity"],
            "conditions": data["weather"][0]["description"].title(),
            "wind_speed": data["wind"]["speed"],
            "icon": data["weather"][0]["icon"]
        }

    except requests.exceptions.Timeout:
        raise HTTPException(status_code=504, detail="Weather service timeout")
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=502, detail=f"Weather service error: {str(e)}")


# ============================================================
# Run with: uvicorn 09_fastapi_weather_api:app --reload
#
# Test endpoints:
#   http://localhost:8000/weather/London
#   http://localhost:8000/weather?city=Tokyo&units=metric
#   http://localhost:8000/docs
# ============================================================
