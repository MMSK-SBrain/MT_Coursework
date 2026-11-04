#!/usr/bin/env python3
"""
Demo 2: Parsing JSON Response
-----------------------------
Taking raw JSON and extracting useful information.

This script shows how to navigate nested JSON structures.
"""

import requests

# Configuration
API_KEY = "YOUR_API_KEY_HERE"
CITY = "London"

url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(url)

if response.status_code == 200:
    # Parse JSON into Python dictionary
    data = response.json()

    # Extract specific values from nested structure
    city_name = data["name"]
    country = data["sys"]["country"]
    temperature = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"]
    wind_speed = data["wind"]["speed"]

    # Display formatted output
    print(f"\n{'='*40}")
    print(f"  Weather Report for {city_name}, {country}")
    print(f"{'='*40}")
    print(f"  Conditions:   {description.title()}")
    print(f"  Temperature:  {temperature}°C (feels like {feels_like}°C)")
    print(f"  Humidity:     {humidity}%")
    print(f"  Wind Speed:   {wind_speed} m/s")
    print(f"{'='*40}\n")
else:
    print(f"Error: {response.status_code}")
    print(response.text)
