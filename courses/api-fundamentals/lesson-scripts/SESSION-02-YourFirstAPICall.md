# Session 2: Your First API Call

**Module:** 2 - Consuming APIs
**Duration:** ~30 minutes
**Type:** Hands-on Lab (guided practice)
**Prerequisites:** Session 1 completed, Python installed on learner machines

---

## Session Overview

| Learning Outcome | Code | What Learners Will Do |
|-----------------|------|----------------------|
| Install and import requests library | SO-2-1-1 | Set up Python environment for API calls |
| Obtain and use an API key | SO-2-1-2 | Sign up for OpenWeatherMap and use their key |
| Make a GET request | SO-2-1-3 | Write Python code to fetch weather data |
| Interpret HTTP status codes | SO-2-1-4 | Understand what 200, 401, 404 mean |

---

## Materials Needed

- Each learner needs:
  - Laptop with Python 3 installed
  - Internet connection
  - Text editor or IDE (VS Code, IDLE, or even Notepad)
- Instructor should have:
  - Pre-registered OpenWeatherMap API key (as backup)
  - Sample code ready to share/display

---

## Pre-Session Setup Check

**[Before starting, verify everyone is ready]**

> "Before we dive in, let's make sure everyone's set up. Can you open a terminal or command prompt and type:"

```
python --version
```

> "You should see something like 'Python 3.10' or higher. If you see 'Python 2' or an error, raise your hand and I'll help."

*[Assist anyone with issues - have backup plan for any who can't run Python]*

---

## Session Script

### Opening: From Theory to Practice (2 minutes)

> "Alright! In the last session, we talked about what APIs are. Now we're going to actually use one. By the end of this session, you'll have written code that fetches real weather data from the internet."

> "I know some of you might be thinking 'I've never coded before' - and that's totally fine. We're going to do this together, step by step. Just follow along, and if you get stuck, raise your hand."

> "We're going to use a free weather API called OpenWeatherMap. It's the same kind of service that powers weather widgets on websites."

---

### Part 1: Setting Up Our Tools (8 minutes)

#### Step 1: Installing the Requests Library

**[SLIDE: Terminal/command prompt]**

> "Python is great at many things, but to make API calls, we need a helper tool called `requests`. Think of it as giving Python the ability to browse the internet."

> "Open your terminal or command prompt, and type this:"

```bash
pip install requests
```

> "Then press Enter."

**[Walk around or ask for thumbs up]**

> "You should see some text scroll by, and then it should say 'Successfully installed' or 'Requirement already satisfied' if you had it already."

**[TROUBLESHOOTING BOX]**
> If you see an error about 'pip not found':
> - Try `pip3 install requests` instead
> - On Windows, try `python -m pip install requests`

---

#### Step 2: Create Your Python File

> "Now let's create a file for our code. Open your text editor and create a new file. Save it somewhere you can find it, like your Desktop, and name it:"

```
weather.py
```

> "The `.py` extension tells your computer this is a Python file."

---

#### Step 3: Import the Library

> "In your `weather.py` file, type this first line:"

```python
import requests
```

> "This line says: 'Hey Python, I want to use that `requests` tool we just installed.'"

**[PAUSE]**

> "Save your file. We'll add more code in a moment, but first, we need something important - an API key."

---

### Part 2: Getting Your API Key (7 minutes)

#### What's an API Key?

**[SLIDE: Key icon]**

> "Remember how we said APIs have rules about who can use them? An API key is like your ID badge. It tells the API: 'This person is allowed to make requests.'"

> "It's also how the API tracks usage. Free services like OpenWeatherMap might say 'You can make 1,000 requests per day' - the key is how they count your requests."

---

#### Signing Up for OpenWeatherMap

**[SLIDE: OpenWeatherMap website screenshot]**

> "Let's get your key. Open your web browser and go to:"

```
https://openweathermap.org/api
```

> "I'll walk you through the signup:"

**[Guide step by step - adjust based on current website UI]**

1. "Click 'Sign Up' or 'Get API key'"
2. "Create a free account - you just need an email"
3. "Verify your email if required"
4. "Go to your account → 'API keys' tab"
5. "You'll see a key that looks like a long string of letters and numbers"

> "Copy that key - we'll use it in a moment."

**[IMPORTANT NOTE]**

> "Quick heads-up: new API keys sometimes take 10-20 minutes to activate. If yours doesn't work right away, don't worry - I have a backup key we can use for this session."

---

#### Interactive Check-In

> "Everyone got their API key? Hold up your hand if you're still working on it."

*[Provide the backup key to anyone stuck, displayed privately or via chat]*

---

### Part 3: Making Your First Request (10 minutes)

#### Building the Code Step by Step

> "Now for the exciting part - let's write the code! Go back to your `weather.py` file."

**[SLIDE: Code editor view]**

> "We already have our import line. Now let's add more. I'll explain each line as we go."

---

##### Line 2: Your API Key

> "Add a new line to store your API key:"

```python
import requests

api_key = "YOUR_API_KEY_HERE"
```

> "Replace `YOUR_API_KEY_HERE` with the actual key you copied. Keep the quotes around it!"

> "This creates a variable - think of it as a labeled box that holds your key so we can use it later."

---

##### Line 3: The City

> "Next, let's specify which city's weather we want:"

```python
import requests

api_key = "YOUR_API_KEY_HERE"
city = "London"
```

> "Feel free to change 'London' to your city! Just keep it in quotes."

---

##### Line 4: Building the URL

> "Now we need to tell Python WHERE to send the request. This is the API's address plus our specific question:"

```python
import requests

api_key = "YOUR_API_KEY_HERE"
city = "London"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
```

> "Whoa, that's a long line! Let's break it down:"

| Part | What It Means |
|------|---------------|
| `https://api.openweathermap.org/data/2.5/weather` | The API's address |
| `?` | "Here come my parameters" |
| `q={city}` | "The city I'm asking about" |
| `&appid={api_key}` | "Here's my ID badge" |
| `&units=metric` | "Give me temperatures in Celsius" |

> "The `f` at the beginning and the `{curly braces}` are Python's way of inserting our variables into the text."

---

##### Line 5: Making the Request!

> "Now the magic line - actually calling the API:"

```python
import requests

api_key = "YOUR_API_KEY_HERE"
city = "London"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
```

> "`requests.get(url)` says: 'Go to this address and GET me what's there.'"

> "The result gets stored in a variable called `response` - this contains everything the API sent back."

---

##### Line 6: See What We Got

> "Finally, let's print the response:"

```python
import requests

api_key = "YOUR_API_KEY_HERE"
city = "London"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
print(response.text)
```

> "`response.text` gives us the actual data (the JSON) that came back."

---

#### Running Your Code

> "Save your file! Now let's run it. In your terminal, navigate to where you saved the file and type:"

```bash
python weather.py
```

> "Press Enter and..."

**[PAUSE FOR EXCITEMENT]**

> "You should see a bunch of JSON data appear! It'll look messy, but that's real weather data you just fetched from the internet!"

**[Walk around and help anyone with errors]**

---

### Part 4: Understanding Status Codes (5 minutes)

**[SLIDE: HTTP Status Codes]**

> "Before we celebrate too much, let's add a safety check. What if something goes wrong?"

> "APIs tell us if a request worked using status codes. Let's check ours:"

> "Modify your code to add these lines before the print:"

```python
import requests

api_key = "YOUR_API_KEY_HERE"
city = "London"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)

print(f"Status Code: {response.status_code}")
print(response.text)
```

> "Run it again. You should see `Status Code: 200` - that means success!"

---

#### Common Status Codes

**[SLIDE: Status code reference]**

> "Here are the codes you'll see most often:"

| Code | Meaning | What Went Wrong? |
|------|---------|------------------|
| **200** | OK - Success! | Nothing - it worked! |
| **401** | Unauthorized | Your API key is invalid or missing |
| **404** | Not Found | The city name was wrong, or the URL is incorrect |
| **429** | Too Many Requests | You've hit your usage limit |
| **500** | Server Error | The API itself is having problems |

---

#### Interactive: Let's Break It!

> "Want to see what an error looks like? Let's intentionally break our code."

> "Try changing your city to something fake:"

```python
city = "Fakecityxyz123"
```

> "Run it again. What status code do you get?"

*[Should get 404]*

> "Now try removing a character from your API key and run it. What happens?"

*[Should get 401]*

> "See? The status code tells you exactly what went wrong. Always check it!"

> "Don't forget to fix your code back to working values!"

---

### Wrap-Up & Transition (2 minutes)

**[SLIDE: What We Accomplished]**

> "Look at what you just did!"

> "✓ Installed a Python library"
> "✓ Got your own API key"
> "✓ Wrote Python code that talks to a real server"
> "✓ Fetched live weather data from the internet"
> "✓ Learned to check if requests succeeded"

> "That's not 'learning about APIs' - that's actually USING an API. You're already ahead of many people who've only heard the term!"

**[SLIDE: Coming Up Next]**

> "In the next session, we'll take that messy JSON blob and turn it into something useful - like printing 'The weather in London is cloudy, 15°C.'"

> "Save your code! We'll build on it in the next session."

---

## Complete Code Reference

For learners who got lost, here's the complete working code:

```python
import requests

# Your API key from OpenWeatherMap
api_key = "YOUR_API_KEY_HERE"

# City to check weather for
city = "London"

# Build the API URL
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

# Make the request
response = requests.get(url)

# Check if it worked
print(f"Status Code: {response.status_code}")

# Show the data
print(response.text)
```

---

## Instructor Notes

### Common Issues & Solutions

| Problem | Solution |
|---------|----------|
| `pip not found` | Try `pip3` or `python -m pip install requests` |
| `ModuleNotFoundError: requests` | Pip installed to wrong Python version - use `python3 -m pip` |
| API key not working | New keys take 10-20 min to activate - use backup key |
| `JSONDecodeError` | Usually means wrong URL or API is down |
| 401 error | API key issue - check for typos, extra spaces |
| 404 error | City name issue - check spelling, try major city |

### Backup API Key

Keep a working API key ready to share (via chat, not screen) for learners whose keys aren't activated yet.

### Timing Checkpoints

| Time | You Should Be At |
|------|------------------|
| 5 min | Everyone has requests installed |
| 12 min | Everyone has an API key |
| 25 min | Everyone has run the code successfully |
| 30 min | Covered status codes & wrap-up |

### If Running Behind

- Skip the "Let's Break It" activity
- Provide pre-written code for copying instead of typing line by line
- Move status code deep-dive to Session 4

### If Running Ahead

- Try different cities and compare results
- Show `response.json()` as a preview of next session
- Discuss what other parameters the API accepts (check the docs)
