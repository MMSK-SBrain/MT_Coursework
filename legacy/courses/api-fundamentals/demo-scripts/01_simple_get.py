#!/usr/bin/env python3
"""
Demo 1: Simple GET Request
--------------------------
The most basic API call - fetching data from a server.

This script fetches weather data for a city using OpenWeatherMap API.
"""

import requests

# Configuration
API_KEY = "YOUR_API_KEY_HERE"  # Replace with your OpenWeatherMap API key
CITY = "London"

# Build the API URL
url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

# Make the GET request
print(f"Fetching weather for {CITY}...")
response = requests.get(url)

# Check if successful
print(f"Status Code: {response.status_code}")

# Show the raw response
print("\nRaw JSON Response:")
print(response.text)
