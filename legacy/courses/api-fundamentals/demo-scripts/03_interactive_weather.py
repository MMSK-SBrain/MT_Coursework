#!/usr/bin/env python3
"""
Demo 3: Interactive Weather App
-------------------------------
Complete weather application with user input and error handling.

This is the "finished product" from Sessions 2-3.
"""

import requests

def get_weather(city: str, api_key: str) -> dict | None:
    """Fetch weather data for a city."""
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return None

def display_weather(data: dict) -> None:
    """Display weather data in a formatted way."""
    city = data["name"]
    country = data["sys"]["country"]
    temp = round(data["main"]["temp"])
    feels = round(data["main"]["feels_like"])
    humidity = data["main"]["humidity"]
    desc = data["weather"][0]["description"].title()
    wind = data["wind"]["speed"]

    print(f"\n{'='*45}")
    print(f"  Weather Report for {city}, {country}")
    print(f"{'='*45}")
    print(f"  Conditions:   {desc}")
    print(f"  Temperature:  {temp}°C (feels like {feels}°C)")
    print(f"  Humidity:     {humidity}%")
    print(f"  Wind Speed:   {wind} m/s")
    print(f"{'='*45}\n")

def main():
    API_KEY = "YOUR_API_KEY_HERE"  # Replace with your key

    print("\n=== Weather Lookup Tool ===\n")

    while True:
        city = input("Enter city name (or 'quit' to exit): ").strip()

        if city.lower() == 'quit':
            print("Goodbye!")
            break

        if not city:
            print("Please enter a city name.\n")
            continue

        print(f"Fetching weather for {city}...")
        data = get_weather(city, API_KEY)

        if data:
            display_weather(data)
        else:
            print(f"Could not find weather for '{city}'. Check the spelling.\n")

if __name__ == "__main__":
    main()
