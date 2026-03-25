# Session 4: Behind the Scenes

**Module:** 3 - API Creation & Security Overview
**Duration:** ~20 minutes
**Type:** Lecture with discussion
**Prerequisites:** Sessions 1-3 completed

---

## Session Overview

| Learning Outcome | Code | What Learners Will Do |
|-----------------|------|----------------------|
| Describe server-side processing | SO-3-1-1 | Understand what happens when an API receives a request |
| List common security measures | SO-3-1-2 | Recognize API keys, OAuth, and rate limiting |
| Explain why keys must be secret | SO-3-1-3 | Understand the risks of exposed credentials |

---

## Materials Needed

- Projector/screen for slides
- (Optional) Flask demo code for brief demonstration
- No learner coding required this session

---

## Session Script

### Opening: Flipping the Perspective (2 minutes)

> "For the past hour, we've been the **client** - the app asking for data. We made requests, got responses, and built something useful."

> "But what's happening on the other side? When you send `requests.get()` to OpenWeatherMap, what actually happens on their servers?"

> "Understanding this will help you:"
> - "Work better with developers on your team"
> - "Understand why things sometimes go wrong"
> - "Make smarter decisions about which APIs to use"

> "We're not going to build an API today - that would take much longer. But I'll show you what's involved."

---

### Part 1: The Server's Perspective (6 minutes)

**[SLIDE: Request journey diagram]**

#### What Happens When You Click "Send"

> "Let's trace what happens when your Python code calls the weather API:"

```
Your Code → Internet → Load Balancer → API Server → Database → Response
```

---

##### Step 1: Your Request Travels

> "When you call `requests.get()`, your request gets packaged up and sent over the internet - through your router, your ISP, across data centers, until it reaches OpenWeatherMap's servers."

> "This happens in milliseconds. Pretty amazing when you think about it!"

---

##### Step 2: The Server Receives It

> "OpenWeatherMap has servers running 24/7, waiting for requests. When yours arrives, the server software wakes up and says: 'Okay, let me process this.'"

---

##### Step 3: Validation

> "The server checks:"
> - "Is this a valid request format?"
> - "Does this API key exist and is it active?"
> - "Is this user within their usage limits?"

> "If any check fails, you get an error code back. Remember those 401 and 429 codes? This is where they come from."

---

##### Step 4: Processing the Request

> "If everything checks out, the server does the actual work:"
> - "Parse your parameters (city = London)"
> - "Look up the data (query their weather database)"
> - "Format the response (build that JSON we saw)"

---

##### Step 5: Sending the Response

> "Finally, the server packages up the JSON and sends it back the way it came. Your code receives it, and you see the weather data."

---

#### Interactive: Timing Discussion

> "Quick thought experiment: We asked for London's weather. Where do you think OpenWeatherMap gets that data originally?"

*[Wait for responses - weather stations, satellites, meteorological services, etc.]*

> "Right! They're aggregating data from thousands of sources. That's the value they provide - you don't have to figure out all those sources yourself."

---

### Part 2: A Quick Peek at Building APIs (5 minutes)

**[SLIDE: Flask code example]**

> "I promised I'd show you what building an API looks like. Here's a super simple example using Python and a tool called Flask:"

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/greeting')
def greeting():
    return jsonify({
        "message": "Hello from my API!",
        "status": "success"
    })

if __name__ == '__main__':
    app.run()
```

> "This is about 10 lines of code, and it creates an API that responds to requests."

> "Let me break it down:"
> - "`Flask` is a library that handles the server stuff for us"
> - "`@app.route('/api/greeting')` says 'when someone visits this address...'"
> - "`return jsonify({...})` sends back JSON data"

**[Optional: Run the demo live if time permits]**

> "If I ran this on my computer, I could visit `http://localhost:5000/api/greeting` and get:"

```json
{
  "message": "Hello from my API!",
  "status": "success"
}
```

> "Obviously, real APIs are much more complex - they connect to databases, handle thousands of requests per second, and include lots of security. But this is the foundation."

---

#### Why Does This Matter to You?

> "You're not going to build APIs - that's what your developers do. But understanding this helps you:"

> "**1. Set realistic expectations**"
> "When a developer says 'the API will take two weeks,' you'll understand there's validation, databases, testing, and more involved."

> "**2. Debug issues**"
> "If something isn't working, you can ask better questions. 'Is it a 401 or a 500?' tells you whether it's your credentials or their server."

> "**3. Speak the language**"
> "You can now participate in technical discussions. 'We need to rate limit this endpoint' isn't Greek anymore."

---

### Part 3: API Security (7 minutes)

**[SLIDE: "Keeping APIs Safe"]**

> "Let's talk about something critical: security. You've been using an API key all session - let's understand why it matters."

---

#### Why API Keys Exist

> "API keys serve three purposes:"

> "**1. Identity** - Who's making this request?"
> "OpenWeatherMap knows it's you (or your account) asking for data."

> "**2. Access Control** - What can you do?"
> "Free tier? You get 1,000 requests/day. Premium? Maybe unlimited."

> "**3. Accountability** - Track usage"
> "If someone abuses the API, they can be blocked by their key."

---

#### The Danger of Exposed Keys

**[SLIDE: Horror story headline]**

> "Here's a real scenario that happens all too often:"

> "A developer writes some code with their API key. They push it to GitHub (a code sharing site). Someone finds it. They use that key to make thousands of requests. The original developer gets a bill for $50,000."

> "This has happened with AWS keys, Google Cloud keys, all sorts of services."

---

#### Interactive: Security Quiz

> "Pop quiz! Which of these is a bad idea?"

> "A) Sharing your API key with a colleague via secure company chat"
> "B) Putting your API key directly in code that gets saved to GitHub"
> "C) Storing your API key in a configuration file on your computer"
> "D) Posting your API key in a public Slack channel"

*[Wait for responses]*

> "B and D are definitely bad. A is okay if your company approves. C is the recommended approach - we call this using 'environment variables' or config files that don't get shared."

---

#### Beyond API Keys: OAuth

**[SLIDE: OAuth flow diagram]**

> "You know when you click 'Sign in with Google' on a website? That's using something called OAuth."

> "OAuth is a more sophisticated authentication system. Instead of sharing a password, you:"
> 1. "Get redirected to Google"
> 2. "Log in there"
> 3. "Google tells the website 'Yes, this person is legit'"
> 4. "You're logged in, without the website ever seeing your Google password"

> "You don't need to implement this - just know it exists when you hear the term."

---

#### Rate Limiting: The Traffic Cop

> "Remember status code 429 - 'Too Many Requests'? That's rate limiting in action."

> "Why do APIs limit how many requests you can make?"

> "**1. Fair usage** - One person shouldn't hog all the resources"
> "**2. Protection** - Prevents attacks that flood the server"
> "**3. Business model** - Want more? Pay for a higher tier"

> "If you hit a rate limit, the solution is usually: wait a while, or upgrade your plan."

---

### Workshop Wrap-Up & Q&A (5 minutes)

**[SLIDE: "What You've Learned Today"]**

> "Let's take a step back and look at everything we covered in these two hours:"

---

#### Knowledge You've Gained

> "**Session 1: Concepts**"
> - "What an API is (the waiter analogy)"
> - "Real-world examples you use daily"
> - "Request/response cycle"
> - "JSON data format"

> "**Sessions 2-3: Skills**"
> - "Setting up Python for API calls"
> - "Getting and using API keys"
> - "Making GET requests"
> - "Parsing JSON responses"
> - "Extracting specific data"
> - "Handling errors gracefully"

> "**Session 4: Context**"
> - "What happens on the server side"
> - "Security best practices"
> - "Why credentials matter"

---

#### What You Can Do Now

**[SLIDE: Practical applications]**

> "With what you've learned, you can:"

> "✓ Have informed conversations with developers about APIs"
> "✓ Read basic API documentation and understand it"
> "✓ Write simple Python scripts to fetch data from public APIs"
> "✓ Troubleshoot common API issues (wrong key, bad city name, etc.)"
> "✓ Understand security concerns and why credentials matter"

---

#### Resources for Going Further

**[SLIDE: Resource list]**

> "If you want to keep learning:"

| Resource | What It's For |
|----------|---------------|
| [Postman](https://www.postman.com/) | GUI tool for testing APIs without code |
| [RapidAPI Hub](https://rapidapi.com/) | Discover thousands of public APIs |
| [Python Requests Docs](https://docs.python-requests.org/) | Deep dive into the library we used |
| [JSONPlaceholder](https://jsonplaceholder.typicode.com/) | Fake API for practice |
| [OpenWeatherMap Docs](https://openweathermap.org/api) | The API we used - try other endpoints! |

---

#### Open Q&A

> "We have a few minutes left. What questions do you have? About anything we covered today, or APIs in general?"

**[Common questions to prepare for:]**

**Q: "How do I find APIs for my work?"**
> A: Start with RapidAPI or Google "[what you need] API". Many services you already use have APIs - Slack, Salesforce, Google Sheets, etc.

**Q: "What's the difference between REST and GraphQL?"**
> A: REST is what we used today - fixed endpoints for fixed data. GraphQL lets you specify exactly what data you want. Both are valid approaches.

**Q: "Can I automate reports using APIs?"**
> A: Absolutely! Pull data from your CRM API, process it in Python, output to a spreadsheet or dashboard. This is a common use case.

**Q: "How secure is this really?"**
> A: Over HTTPS (which most APIs use), the data is encrypted in transit. Your main risk is exposing credentials. Use them carefully and rotate them if compromised.

---

### Closing

> "Thank you all for your attention and participation today! You came in as API newcomers and you're leaving having actually used one."

> "Remember: the best way to get comfortable with this is practice. Try different APIs, break things, fix them. That's how learning works."

> "Don't forget to save your `weather.py` code - you built that! And if you have questions later, feel free to reach out."

> "Great job today, everyone!"

---

## Instructor Notes

### Demo Prep (Optional Flask Demo)

If you want to do the Flask demo live:

```bash
pip install flask
```

Save this as `demo_api.py`:
```python
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/greeting')
def greeting():
    name = request.args.get('name', 'World')
    return jsonify({
        "message": f"Hello, {name}!",
        "status": "success"
    })

@app.route('/api/add')
def add():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify({
        "result": a + b
    })

if __name__ == '__main__':
    app.run(debug=True)
```

Run with: `python demo_api.py`

Test with: `http://localhost:5000/api/greeting?name=Workshop`

### Timing Checkpoints

| Time | You Should Be At |
|------|------------------|
| 2 min | Opening complete |
| 8 min | Server perspective done |
| 13 min | API building peek done |
| 20 min | Security & wrap-up |

### If Questions Run Long

- Skip or shorten the Flask demo
- Move resources slide to handout instead of discussing

### Common Misconceptions to Address

| Misconception | Clarification |
|---------------|---------------|
| "APIs are only for programmers" | Many no-code tools (Zapier, Power Automate) use APIs under the hood |
| "Public APIs are always free" | Most have free tiers but charge for heavy usage |
| "API keys are like passwords" | Similar, but usually for apps, not human login |
| "All APIs work the same" | Core concepts are similar, but details vary widely |

### Handout/Follow-Up Email

Consider sending participants:
- Link to the complete code
- List of resources
- API key safety checklist
- Encouragement to explore other APIs
