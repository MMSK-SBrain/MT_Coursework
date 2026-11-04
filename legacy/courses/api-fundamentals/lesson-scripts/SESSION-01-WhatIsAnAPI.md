# Session 1: What is an API?

**Module:** 1 - API Fundamentals
**Duration:** ~40 minutes (extended to include HTTP methods)
**Type:** Lecture with interactive elements
**Prerequisites:** None - this is the opening session

---

## Session Overview

| Learning Outcome | Code | What Learners Will Do |
|-----------------|------|----------------------|
| Define API in non-technical terms | SO-1-1-1 | Explain APIs using everyday language |
| Identify real-world examples | SO-1-1-2 | Recognize APIs in apps they already use |
| Describe request/response cycle | SO-1-1-3 | Understand how apps "talk" to servers |
| Explain JSON basics | SO-1-1-4 | Read simple JSON data structures |
| Differentiate HTTP methods | SO-1-1-5 | Understand GET, POST, PUT, DELETE purposes |

---

## Materials Needed

- Projector/screen for slides
- Whiteboard or digital drawing tool
- (Optional) Printed JSON examples for hands-on reference

---

## Session Script

### Opening Hook (2 minutes)

**[SLIDE: Weather app screenshot showing temperature]**

> "Quick question for everyone - raise your hand if you checked the weather on your phone this morning."

*[Wait for hands]*

> "Great! Now here's something you might not have thought about: your weather app doesn't actually know what the weather is. It's not measuring the temperature itself. So where does that information come from?"

*[Pause for a response or two]*

> "Exactly - it comes from somewhere else. Your phone asked a weather service for the data, and that service sent it back. That 'asking and receiving' - that's an API in action. And by the end of this session, you'll understand exactly how that works."

---

### Part 1: What is an API? (8 minutes)

**[SLIDE: "API = Application Programming Interface"]**

> "Let's start with the name itself. API stands for Application Programming Interface. But honestly? That doesn't help much, does it? It sounds very technical."

> "So let me give you a much simpler way to think about it..."

---

#### The Restaurant Analogy

**[SLIDE: Simple restaurant illustration - customer, waiter, kitchen]**

> "Imagine you're at a restaurant. You're hungry, you want food. The kitchen has food and can make it for you. But you don't walk into the kitchen yourself, right? That would be chaos!"

> "Instead, there's a waiter. The waiter takes your order, brings it to the kitchen, and then brings your food back to you. The waiter is the go-between."

**[Draw or show diagram]**

```
YOU (Customer)  →  WAITER  →  KITCHEN
                     ↓
              Your Food!
```

> "An API is like that waiter. It's the messenger that lets two different systems talk to each other."

> "In the tech world:"
> - "**You** = the app on your phone"
> - "**The waiter** = the API"
> - "**The kitchen** = the server that has the data"

---

#### Interactive Moment: The Menu

**[SLIDE: Restaurant menu image]**

> "Here's another important part of the analogy. When you order at a restaurant, you can't just say 'give me something delicious.' You need to order from the menu - specific items, in a specific way."

> "APIs work the same way. They have rules - a 'menu' of what you can ask for and how to ask for it. This is called the API's **documentation**."

**[QUICK POLL]**

> "Has anyone here ever looked at API documentation before? Maybe at work when talking to developers?"

*[Acknowledge responses]*

> "Don't worry if you haven't - by the end of today, you'll be able to read basic API docs and understand what they're saying."

---

### Part 2: APIs in Your Daily Life (7 minutes)

**[SLIDE: "APIs Are Everywhere"]**

> "Now that we understand what an API is, let's look at where you're already using them - probably dozens of times a day without realizing it."

---

#### Example 1: Weather Apps

**[SLIDE: Weather app screenshots]**

> "We started with this one. When you open your weather app:"
> 1. "Your phone sends a request to a weather API - 'What's the weather in [your city]?'"
> 2. "The weather service looks up the data"
> 3. "It sends back: temperature, humidity, forecast"
> 4. "Your app displays it in a nice format"

> "The app could be Apple Weather, Google Weather, or Weather.com - they might all be getting data from the same source via APIs!"

---

#### Example 2: Payment Buttons

**[SLIDE: "Pay with PayPal" / "Apple Pay" buttons on a website]**

> "Ever bought something online and clicked 'Pay with PayPal' or 'Apple Pay'? That's an API."

> "The shopping website doesn't handle your credit card directly. Instead:"
> 1. "It sends your payment request to PayPal's API"
> 2. "PayPal processes the payment"
> 3. "PayPal tells the website 'Payment successful' or 'Payment failed'"

> "This is why online stores can offer 10 different payment options without building 10 payment systems themselves."

---

#### Example 3: Social Media Embeds

**[SLIDE: Embedded tweet on a news website]**

> "When you see a tweet embedded in a news article, that's Twitter's API. The news site asks Twitter: 'Give me the content of this tweet,' and Twitter sends it over."

---

#### Interactive Activity: Spot the API (3 minutes)

**[SLIDE: List of scenarios]**

> "Let's play a quick game. I'll describe a scenario, and you tell me: is there an API involved? And if so, what's talking to what?"

**Scenario 1:** "You open Google Maps and search for 'coffee shops near me.' It shows you a list with ratings and hours."

*[Wait for responses]*

> "Yes! Google Maps is using APIs - potentially its own places API, plus the business's APIs for hours and ratings."

**Scenario 2:** "You log into a website using 'Sign in with Google' instead of creating a new account."

*[Wait for responses]*

> "Absolutely! That's Google's authentication API. The website asks Google: 'Is this person who they say they are?' Google says yes or no."

**Scenario 3:** "You type a document in Microsoft Word on your computer with no internet."

*[Wait for responses]*

> "Trick question! No API here - you're not communicating with another system. But the moment you save to OneDrive... then yes, APIs are involved."

---

### Part 3: The Request/Response Cycle (7 minutes)

**[SLIDE: Request → Server → Response diagram]**

> "Now let's get a bit more specific about how this 'conversation' actually works."

---

#### The Cycle Explained

> "Every API interaction follows this pattern:"

**[Draw or animate step by step]**

```
1. REQUEST: Your app asks for something
      ↓
2. PROCESSING: The server figures out the answer
      ↓
3. RESPONSE: The server sends back the answer
```

> "Let's use our weather example again:"

| Step | What Happens | Example |
|------|--------------|---------|
| Request | App asks for weather | "What's the weather in Tokyo?" |
| Processing | Server looks up data | (happens on their computers) |
| Response | Server sends answer | "Sunny, 22°C, 45% humidity" |

---

#### What's in a Request?

**[SLIDE: Anatomy of an API request]**

> "When your app makes a request, it typically includes:"

> "**1. The URL (address)** - Where to send the request"
>
> "Think of this like a street address. For weather, it might be something like:"
> `https://api.openweathermap.org/data/2.5/weather`

> "**2. The Method** - What you want to do"
>
> "The most common is **GET** - which means 'give me information.' We'll focus on this today."

> "**3. Parameters** - The details of your question"
>
> "Like adding 'city=Tokyo' to specify which city's weather you want."

---

#### What's in a Response?

**[SLIDE: API response example]**

> "The server sends back:"

> "**1. A status code** - Did it work?"
> - "**200** = Success! Here's your data"
> - "**404** = Not found (you've seen this on websites!)"
> - "**401** = Unauthorized - you need to prove who you are"

> "**2. The data itself** - Usually in a format called JSON"

> "Let's talk about JSON..."

---

### Part 4: Understanding JSON (6 minutes)

**[SLIDE: "JSON = JavaScript Object Notation"]**

> "JSON is just a way to format data so computers can easily read it. But here's the good news - humans can read it too!"

---

#### JSON Basics

**[SLIDE: Simple JSON example]**

> "Here's what weather data might look like in JSON:"

```json
{
  "city": "Tokyo",
  "temperature": 22,
  "unit": "celsius",
  "conditions": "sunny",
  "humidity": 45
}
```

> "Let's break this down:"
> - "The curly braces `{ }` contain all the data"
> - "Each piece of data has a **name** (like 'city') and a **value** (like 'Tokyo')"
> - "They're separated by colons"
> - "Text values have quotes, numbers don't"

---

#### Interactive: Reading JSON Together

**[SLIDE: More complex JSON]**

> "Now let's try a slightly more complex example:"

```json
{
  "city": "Tokyo",
  "country": "Japan",
  "weather": {
    "temperature": 22,
    "feels_like": 24,
    "conditions": "sunny"
  },
  "forecast": ["sunny", "cloudy", "rain"]
}
```

> "A few new things here:"

> "**Nested data** - See how 'weather' contains its own set of data inside? That's like a folder inside a folder."

> "**Lists** - 'forecast' has square brackets `[ ]` containing multiple values - the weather for the next few days."

**[QUICK EXERCISE]**

> "Looking at this JSON, can someone tell me:"
> 1. "What country is this for?" *(Japan)*
> 2. "What does it feel like outside?" *(24)*
> 3. "What's tomorrow's forecast?" *(cloudy - second item in the list)*

*[Call on volunteers or ask the room]*

---

### Part 5: HTTP Methods - The Verbs of APIs (8 minutes)

**[SLIDE: "HTTP Methods - What Do You Want to DO?"]**

> "Earlier, I mentioned that requests have a 'method' - what you want to do. Let's dig into that, because it's really important for understanding how APIs work."

> "Think about data operations. There are really only four things you can do with data:"

```
CREATE  →  Make something new
READ    →  Get something that exists
UPDATE  →  Change something that exists
DELETE  →  Remove something
```

> "In the API world, we use HTTP methods to express these actions."

---

#### The Four Main HTTP Methods

**[SLIDE: CRUD table]**

| Method | Action | Example | Restaurant Analogy |
|--------|--------|---------|-------------------|
| **GET** | Read/Retrieve | Get weather data | "What's on the menu?" |
| **POST** | Create | Submit a new order | "I'd like to place an order" |
| **PUT** | Update/Replace | Change your order | "Actually, change my order to..." |
| **DELETE** | Remove | Cancel your order | "Cancel my order please" |

> "Together, these form what we call **CRUD operations** - Create, Read, Update, Delete."

---

#### GET - The Reader

**[SLIDE: GET method]**

> "GET is what we'll use most today. It says: 'Give me this data.'"

```
GET /weather?city=London
→ Returns: Weather data for London
```

> "GET requests are **safe** - they don't change anything on the server. You're just reading."

> "Think of it like looking at a restaurant menu - you're not ordering yet, just looking."

---

#### POST - The Creator

**[SLIDE: POST method]**

> "POST says: 'Here's new data - create something with it.'"

```
POST /users
Body: {"name": "Alice", "email": "alice@example.com"}
→ Creates: A new user account
```

> "Unlike GET, POST **sends data** to the server. It's like handing your order to the waiter."

> "When you submit a form online - registering for an account, posting a comment - that's usually a POST request."

---

#### PUT - The Updater

**[SLIDE: PUT method]**

> "PUT says: 'Replace this existing thing with new data.'"

```
PUT /users/123
Body: {"name": "Alice Smith", "email": "alice.smith@example.com"}
→ Updates: User #123's information
```

> "PUT is used when you want to **change** something that already exists."

> "Like telling the waiter: 'I ordered the chicken, but actually make it the fish instead.'"

---

#### DELETE - The Remover

**[SLIDE: DELETE method]**

> "DELETE says: 'Remove this thing.'"

```
DELETE /users/123
→ Removes: User #123 from the system
```

> "This one's straightforward - you're asking the server to delete something."

> "Like canceling your restaurant order before the kitchen starts making it."

---

#### Interactive: Match the Method

**[SLIDE: Scenarios]**

> "Quick exercise - what HTTP method would you use for each scenario?"

**Scenario 1:** "View your bank account balance"
*[Wait]* → "**GET** - you're just reading data"

**Scenario 2:** "Post a photo to Instagram"
*[Wait]* → "**POST** - you're creating new content"

**Scenario 3:** "Update your profile picture"
*[Wait]* → "**PUT** - you're replacing existing data"

**Scenario 4:** "Remove a tweet"
*[Wait]* → "**DELETE** - you're removing content"

---

#### Why Does This Matter?

> "You might think: 'I'm not building APIs, why do I need to know this?'"

> "Two reasons:"

> "**1. Better communication with developers**"
> "When a developer says 'We need a POST endpoint for this,' you'll know what they mean."

> "**2. Understanding API documentation**"
> "API docs list methods for each endpoint. Now you can read them!"

**[SLIDE: Example API documentation]**

```
User API Endpoints:
- GET    /users      → List all users
- GET    /users/123  → Get user #123
- POST   /users      → Create new user
- PUT    /users/123  → Update user #123
- DELETE /users/123  → Delete user #123
```

> "See how each endpoint tells you what method to use? That's the menu we talked about!"

**[OPTIONAL LIVE DEMO]**

> "Let me show you all four methods in action..."

*[Run `04_http_methods_demo.py` from demo-scripts folder]*

---

### Wrap-Up & Transition (2 minutes)

**[SLIDE: Key Takeaways]**

> "Let's recap what we've learned:"

> "**1. An API is a messenger** - It lets different software systems talk to each other, like a waiter between you and the kitchen."

> "**2. APIs are everywhere** - Weather apps, payment buttons, social logins, maps - you use them constantly."

> "**3. Request → Response** - Your app asks a question, the server sends back an answer."

> "**4. JSON is readable** - It's just organized data with names and values."

> "**5. HTTP methods define actions** - GET reads, POST creates, PUT updates, DELETE removes."

**[SLIDE: "Coming Up Next..."]**

> "In the next session, we're going to stop just talking about APIs and actually USE one. You'll write a few lines of Python code to fetch real weather data. Don't worry if you've never coded before - I'll walk you through every single step."

> "Any questions before we move on?"

*[Take 2-3 questions if time permits]*

---

## Instructor Notes

### Common Questions & Answers

**Q: "Do I need to be a programmer to use APIs?"**
> A: For basic consumption, you need minimal coding (which we'll learn today). But many tools like Postman or Zapier let you use APIs without any code at all.

**Q: "Is this the same as a website?"**
> A: Related but different. A website is for humans to look at. An API is for software to get data from. Sometimes they share the same server!

**Q: "Why don't apps just store all the data themselves?"**
> A: Storage, freshness, and specialization. Weather data changes constantly - better to ask an expert service than try to track it yourself.

### Timing Checkpoints

| Time | You Should Be At |
|------|------------------|
| 5 min | Finished opening hook |
| 13 min | Finished restaurant analogy |
| 20 min | Finished real-world examples |
| 27 min | Finished request/response |
| 33 min | Finished JSON basics |
| 40 min | Finished HTTP methods & wrap-up |

### If Running Behind

- Shorten the "Spot the API" activity to 1 scenario
- Skip the nested JSON example, stick to simple key-value pairs
- For HTTP methods, show only GET and POST, mention PUT/DELETE briefly
- Skip the live demo of `04_http_methods_demo.py`
- Move some Q&A to the break between sessions

### If Running Ahead

- Add more JSON reading practice
- Run the full `04_http_methods_demo.py` live demo
- Discuss REST vs other API types briefly
- Introduce PATCH as a fifth method (partial updates)
- Take more audience questions about their work contexts

### Demo Script Reference

For the HTTP methods section, you can run:
```bash
python demo-scripts/04_http_methods_demo.py
```
This interactively shows GET, POST, PUT, and DELETE against a test API.
