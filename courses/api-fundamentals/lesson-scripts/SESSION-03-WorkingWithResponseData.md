# Session 3: Working with Response Data

**Module:** 2 - Consuming APIs
**Duration:** ~30 minutes
**Type:** Hands-on Lab (guided practice)
**Prerequisites:** Session 2 completed, working weather.py file

---

## Session Overview

| Learning Outcome | Code | What Learners Will Do |
|-----------------|------|----------------------|
| Parse JSON into Python dictionary | SO-2-2-1 | Convert response text to usable Python data |
| Extract values from nested JSON | SO-2-2-2 | Navigate JSON structure to get specific data |
| Print formatted weather info | SO-2-2-3 | Create a clean, readable weather report |

---

## Materials Needed

- Learner's `weather.py` file from Session 2
- Working internet connection
- (Optional) JSON viewer browser extension for visualization

---

## Session Script

### Opening: From Messy to Meaningful (2 minutes)

> "Welcome back! Last session, we successfully called an API and got data back. But that data looked like a mess, right? A wall of text with curly braces everywhere."

> "Today, we're going to transform that chaos into something useful. By the end of this session, your code will print something like:"

**[SLIDE: Target output]**

```
Weather Report for London
-------------------------
Conditions: scattered clouds
Temperature: 15°C (feels like 14°C)
Humidity: 72%
```

> "Much nicer! Let's make that happen."

---

### Part 1: Parsing JSON into Python (8 minutes)

#### Understanding the Problem

> "Open your `weather.py` file from last session. If you lost it, here's what we had:"

```python
import requests

api_key = "YOUR_API_KEY_HERE"
city = "London"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
print(response.text)
```

> "Run this and look at the output. You'll see something like:"

```
{"coord":{"lon":-0.1257,"lat":51.5085},"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04d"}],"base":"stations","main":{"temp":15.2,"feels_like":14.5,"temp_min":13.8,"temp_max":16.1,"pressure":1012,"humidity":72}...
```

> "This is JSON - which we learned about in Session 1. The data IS there: temperature is 15.2, humidity is 72. But how do we get just those values?"

---

#### The Magic of `.json()`

> "Python makes this easy. Instead of `response.text` (which gives us a string), we can use `response.json()` (which gives us a dictionary)."

> "What's a dictionary? In Python, it's like a filing cabinet - you look things up by name."

> "Let's update our code:"

```python
import requests

api_key = "YOUR_API_KEY_HERE"
city = "London"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()  # Convert JSON text to Python dictionary

print(data)
```

> "Run it. The output looks similar, but now Python understands the structure - it's not just text anymore."

---

#### Accessing Data by Name

> "Now let's grab specific pieces. Remember JSON has names and values? In Python dictionaries, we access values using square brackets and the name:"

```python
print(data["name"])
```

> "Add this line and run it. What do you get?"

*[Should print the city name: "London"]*

> "We just extracted one piece of data from that whole blob!"

---

#### Interactive Practice

> "Try these yourself - add each line, run, and see what you get:"

```python
print(data["main"])
print(data["weather"])
```

> "What did you notice about the outputs?"

*[Wait for responses]*

> "Right! `data['main']` gave us ANOTHER dictionary (more curly braces). And `data['weather']` gave us a list (square brackets). The data is nested - like folders inside folders."

---

### Part 2: Navigating Nested Data (10 minutes)

**[SLIDE: JSON structure visualization]**

#### Visualizing the Structure

> "Let's map out what's inside this JSON. Think of it like a tree:"

```
data
├── "name": "London"
├── "main": {
│     ├── "temp": 15.2
│     ├── "feels_like": 14.5
│     └── "humidity": 72
│   }
└── "weather": [
      └── {
            ├── "main": "Clouds"
            └── "description": "broken clouds"
          }
    ]
```

> "So to get the temperature, we need to go: `data` → `main` → `temp`"

---

#### Chaining Access

> "In Python, we chain these with multiple brackets:"

```python
temperature = data["main"]["temp"]
print(temperature)
```

> "Add these lines to your code and run it."

> "Beautiful! We extracted just the temperature number."

---

#### Handling Lists

> "What about the weather description? That's inside a list. In Python, lists use numbers (starting from 0) to access items:"

```python
weather_info = data["weather"][0]  # Get the first item in the list
print(weather_info)
```

> "Now to get the description:"

```python
description = data["weather"][0]["description"]
print(description)
```

> "We're saying: 'Go into the weather list, get the first item (index 0), then get the description from that item.'"

---

#### Guided Exercise: Extract All the Data

> "Let's build up our extractions. Update your code to extract everything we need:"

```python
import requests

api_key = "YOUR_API_KEY_HERE"
city = "London"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()

# Extract specific values
city_name = data["name"]
temperature = data["main"]["temp"]
feels_like = data["main"]["feels_like"]
humidity = data["main"]["humidity"]
description = data["weather"][0]["description"]

# Print them
print(f"City: {city_name}")
print(f"Temperature: {temperature}")
print(f"Feels like: {feels_like}")
print(f"Humidity: {humidity}")
print(f"Conditions: {description}")
```

> "Run this and admire your work! Clean, individual data points."

**[Walk around and check everyone got this working]**

---

#### Interactive Check-In

> "Quick quiz - don't look at your code. If I wanted to get the `temp_min` value, what would I type?"

*[Wait for responses: `data["main"]["temp_min"]`]*

> "And what about `temp_max`?"

*[Wait for responses: `data["main"]["temp_max"]`]*

> "You're getting it! It's just following the path through the nested structure."

---

### Part 3: Creating a Beautiful Output (8 minutes)

#### Formatting Our Report

> "Now let's turn this into a proper weather report. We'll use Python string formatting to make it look nice."

> "Replace your print statements with this:"

```python
import requests

api_key = "YOUR_API_KEY_HERE"
city = "London"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()

# Extract values
city_name = data["name"]
temperature = data["main"]["temp"]
feels_like = data["main"]["feels_like"]
humidity = data["main"]["humidity"]
description = data["weather"][0]["description"]

# Create formatted report
print(f"Weather Report for {city_name}")
print("-" * 30)
print(f"Conditions: {description}")
print(f"Temperature: {temperature}°C (feels like {feels_like}°C)")
print(f"Humidity: {humidity}%")
```

> "A few things to notice:"
> - "`'-' * 30`" prints a line of 30 dashes - makes a nice divider
> - "We combine variables and text in f-strings"
> - "Added units like °C and %"

> "Run it!"

**[SLIDE: Expected output]**

```
Weather Report for London
------------------------------
Conditions: broken clouds
Temperature: 15.2°C (feels like 14.5°C)
Humidity: 72%
```

---

#### Making It Interactive

> "Want to make it even cooler? Let's let the user choose the city! Add this at the top, replacing the hardcoded city:"

```python
import requests

api_key = "YOUR_API_KEY_HERE"
city = input("Enter a city name: ")  # Ask the user!
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

# ... rest of the code stays the same
```

> "The `input()` function asks for text and waits for the user to type something."

> "Run it and try different cities - Tokyo, New York, Sydney, your hometown!"

---

#### Adding Error Handling (Bonus)

> "One small improvement - what if someone types a city that doesn't exist? Let's check:"

```python
import requests

api_key = "YOUR_API_KEY_HERE"
city = input("Enter a city name: ")
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)

# Check if the request worked
if response.status_code == 200:
    data = response.json()

    city_name = data["name"]
    temperature = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"]

    print(f"\nWeather Report for {city_name}")
    print("-" * 30)
    print(f"Conditions: {description}")
    print(f"Temperature: {temperature}°C (feels like {feels_like}°C)")
    print(f"Humidity: {humidity}%")
else:
    print(f"Error: Could not find weather for '{city}'")
    print(f"Status code: {response.status_code}")
```

> "Now try entering 'asdfghjk' as a city. Instead of crashing, you'll get a helpful error message!"

---

### Part 4: Celebrate & Experiment (5 minutes)

**[SLIDE: "You Built Something Real!"]**

> "Take a moment to appreciate what you've accomplished. You've built a functional weather app! It's simple, but it works - and it uses the same technology that professional apps use."

---

#### Interactive Challenge

> "For the last few minutes, try these challenges. Raise your hand if you get stuck or want to show off your solution!"

**Challenge 1:** Add wind speed to your report
- Hint: Look for `data["wind"]["speed"]`

**Challenge 2:** Round the temperature to a whole number
- Hint: Use `round(temperature)` or `int(temperature)`

**Challenge 3:** Add a country code to the city name
- Hint: Look for `data["sys"]["country"]`

*[Give ~3 minutes for exploration, help as needed]*

---

### Wrap-Up & Transition (2 minutes)

**[SLIDE: Session Summary]**

> "What we accomplished:"

> "✓ Converted JSON text to usable Python data"
> "✓ Navigated nested structures with bracket notation"
> "✓ Extracted exactly the values we needed"
> "✓ Created a formatted, user-friendly output"
> "✓ Added error handling for robustness"

> "You now have a complete, working program that:"
> 1. "Asks for a city"
> 2. "Calls a real API"
> 3. "Handles the response"
> 4. "Displays useful information"

**[SLIDE: What's Next]**

> "In our final session, we'll take a step back and talk about what happens on the OTHER side - how APIs are built, and how to keep them secure. It's more conceptual, but it'll help you understand the full picture."

> "Make sure to save your code - you've earned it!"

---

## Complete Final Code

```python
import requests

api_key = "YOUR_API_KEY_HERE"
city = input("Enter a city name: ")
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    city_name = data["name"]
    country = data["sys"]["country"]
    temperature = round(data["main"]["temp"])
    feels_like = round(data["main"]["feels_like"])
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"]
    wind_speed = data["wind"]["speed"]

    print(f"\nWeather Report for {city_name}, {country}")
    print("-" * 35)
    print(f"Conditions: {description}")
    print(f"Temperature: {temperature}°C (feels like {feels_like}°C)")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")
else:
    print(f"Error: Could not find weather for '{city}'")
    print(f"Status code: {response.status_code}")
```

---

## Instructor Notes

### Common Issues & Solutions

| Problem | Solution |
|---------|----------|
| `KeyError` | The key doesn't exist - check spelling, check structure with `print(data)` |
| `TypeError: 'NoneType'` | The API returned nothing - check city spelling and API key |
| `IndexError: list index out of range` | The list was empty - usually wrong city |
| Encoding issues with °C | Use `\u00B0` or copy the ° character |

### JSON Structure Reference

Full structure of OpenWeatherMap response:
```json
{
  "coord": {"lon": -0.13, "lat": 51.51},
  "weather": [{"id": 803, "main": "Clouds", "description": "broken clouds", "icon": "04d"}],
  "main": {
    "temp": 15.2,
    "feels_like": 14.5,
    "temp_min": 13.8,
    "temp_max": 16.1,
    "pressure": 1012,
    "humidity": 72
  },
  "wind": {"speed": 3.6, "deg": 230},
  "sys": {"country": "GB", "sunrise": 1698734567, "sunset": 1698771234},
  "name": "London"
}
```

### Timing Checkpoints

| Time | You Should Be At |
|------|------------------|
| 8 min | Everyone has extracted single values |
| 18 min | Everyone has navigated nested data |
| 26 min | Everyone has formatted output |
| 30 min | Challenges & wrap-up |

### If Running Behind

- Skip the interactive user input feature
- Provide the final code instead of building step by step
- Skip the bonus challenges

### If Running Ahead

- Explore more data fields (sunrise/sunset, pressure)
- Try multiple cities in one run (loop)
- Discuss how to save results to a file
