# Guide: Testing APIs with Postman

**Type:** Reference Guide / Optional Session Extension
**Duration:** ~15-20 minutes (if taught as session)
**Prerequisites:** Understanding of APIs, HTTP methods, JSON

---

## What is Postman?

Postman is a popular tool for testing and exploring APIs **without writing code**. It provides a visual interface to:

- Make API requests (GET, POST, PUT, DELETE)
- View responses in a readable format
- Save and organize requests
- Share API collections with your team
- Generate code snippets in various languages

> **Why Postman?** For non-technical staff, Postman offers a way to interact with APIs without needing to write Python or any other code. It's like having a universal remote control for APIs.

---

## Getting Started

### Installation

1. Go to https://www.postman.com/downloads/
2. Download the desktop app (free)
3. Install and create a free account (or use without account)

*Alternative: Use the web version at https://web.postman.com*

---

## Postman Interface Overview

```
┌─────────────────────────────────────────────────────────────────┐
│  [Collections]  [History]  [Environments]                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  [GET ▼]  │ https://api.example.com/weather?city=London │[Send] │
│                                                                 │
├──────────┬──────────┬──────────┬──────────┬──────────────────────┤
│  Params  │  Auth    │  Headers │  Body    │  Pre-request │ Tests │
├──────────┴──────────┴──────────┴──────────┴──────────────────────┤
│                                                                 │
│  KEY              VALUE                                         │
│  city             London                                        │
│  appid            your-api-key-here                            │
│  units            metric                                        │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│  Response                                              200 OK   │
├─────────────────────────────────────────────────────────────────┤
│  {                                                              │
│    "name": "London",                                            │
│    "main": {                                                    │
│      "temp": 15.2,                                              │
│      "humidity": 72                                             │
│    }                                                            │
│  }                                                              │
└─────────────────────────────────────────────────────────────────┘
```

### Key Areas

| Area | Purpose |
|------|---------|
| **Method dropdown** | Select GET, POST, PUT, DELETE, etc. |
| **URL bar** | Enter the API endpoint address |
| **Send button** | Execute the request |
| **Params tab** | Add query parameters (key-value pairs) |
| **Auth tab** | Configure authentication (API keys, OAuth) |
| **Headers tab** | Add HTTP headers |
| **Body tab** | Add request body (for POST/PUT) |
| **Response area** | View the API response |

---

## Tutorial: Making Your First Request

### Step 1: Simple GET Request

Let's fetch a random joke from a free API.

1. Open Postman
2. Select **GET** from the method dropdown
3. Enter this URL: `https://official-joke-api.appspot.com/random_joke`
4. Click **Send**

You should see a response like:
```json
{
  "type": "general",
  "setup": "Why did the scarecrow win an award?",
  "punchline": "Because he was outstanding in his field.",
  "id": 1
}
```

**Congratulations!** You just made an API call without writing any code.

---

### Step 2: GET with Parameters

Now let's use the weather API with query parameters.

1. Select **GET**
2. Enter: `https://api.openweathermap.org/data/2.5/weather`
3. Go to the **Params** tab
4. Add these key-value pairs:

| KEY | VALUE |
|-----|-------|
| q | London |
| appid | YOUR_API_KEY_HERE |
| units | metric |

5. Click **Send**

Notice how Postman automatically builds the URL:
```
https://api.openweathermap.org/data/2.5/weather?q=London&appid=YOUR_KEY&units=metric
```

---

### Step 3: POST Request (Creating Data)

Let's create a new post using JSONPlaceholder (a test API).

1. Select **POST** from the dropdown
2. Enter: `https://jsonplaceholder.typicode.com/posts`
3. Go to the **Body** tab
4. Select **raw** and choose **JSON** from the dropdown
5. Enter this JSON:

```json
{
  "title": "My Test Post",
  "body": "This is the content of my post.",
  "userId": 1
}
```

6. Click **Send**

You should see status **201 Created** and a response with your new post (including an assigned ID).

---

### Step 4: PUT Request (Updating Data)

1. Select **PUT**
2. Enter: `https://jsonplaceholder.typicode.com/posts/1`
3. Go to **Body** → **raw** → **JSON**
4. Enter:

```json
{
  "id": 1,
  "title": "Updated Title",
  "body": "This content has been updated.",
  "userId": 1
}
```

5. Click **Send**

You should see the updated data returned.

---

### Step 5: DELETE Request

1. Select **DELETE**
2. Enter: `https://jsonplaceholder.typicode.com/posts/1`
3. Click **Send**

You should see status **200 OK** with an empty object `{}` confirming deletion.

---

## Working with Authentication

### API Key in Query Parameters

1. Go to the **Params** tab
2. Add: `appid` = `your-api-key`

### API Key in Headers

1. Go to the **Headers** tab
2. Add: `X-API-Key` = `your-api-key`

### Using the Auth Tab

1. Go to the **Auth** tab
2. Select **API Key** from the Type dropdown
3. Enter:
   - Key: `appid` (or whatever the API requires)
   - Value: Your API key
   - Add to: Query Params or Header

### Bearer Token (OAuth)

1. Go to **Auth** tab
2. Select **Bearer Token**
3. Enter your token

---

## Organizing Requests

### Collections

Collections let you save and organize your API requests.

1. Click **New** → **Collection**
2. Name it (e.g., "Weather API Tests")
3. Save your requests into the collection

### Environments

Environments let you store variables (like API keys) and switch between them.

1. Click the gear icon → **Manage Environments**
2. Create a new environment (e.g., "Development")
3. Add variables:
   - `base_url` = `https://api.openweathermap.org`
   - `api_key` = `your-key-here`
4. Use them in requests: `{{base_url}}/data/2.5/weather?appid={{api_key}}`

---

## Reading Responses

### Status Codes

Postman shows the status code prominently:

| Code | Meaning | Color |
|------|---------|-------|
| 200 OK | Success | Green |
| 201 Created | Resource created | Green |
| 400 Bad Request | Your request has errors | Red |
| 401 Unauthorized | Authentication failed | Red |
| 404 Not Found | Resource doesn't exist | Red |
| 500 Server Error | Server problem | Red |

### Response Tabs

| Tab | Shows |
|-----|-------|
| **Body** | The actual response data |
| **Headers** | Response headers from server |
| **Cookies** | Any cookies set |
| **Test Results** | Results of any tests you've written |

### Formatting Options

In the Body tab, you can view responses as:
- **Pretty** - Formatted JSON (easiest to read)
- **Raw** - Unformatted text
- **Preview** - HTML rendered (for web pages)

---

## Useful Features

### Generate Code

Postman can generate code snippets for your request:

1. Click the `</>` icon (Code)
2. Select a language (Python, JavaScript, cURL, etc.)
3. Copy the generated code

This is great for sharing with developers or learning how the request translates to code!

### History

All your requests are saved in History (left sidebar). Click any past request to reload it.

### Import/Export

- **Import**: Load API collections from files or URLs
- **Export**: Save your collections to share with others

### Mock Servers

Create fake API responses for testing without a real server.

---

## Postman vs Python

| Task | Postman | Python |
|------|---------|--------|
| Quick API testing | Excellent | Good |
| Exploring new APIs | Excellent | Good |
| Automation | Limited | Excellent |
| Data processing | Limited | Excellent |
| Learning/prototyping | Excellent | Good |
| Sharing with team | Excellent | Requires code |

**Recommendation**: Use Postman for exploration and testing. Use Python when you need to automate, process data, or integrate APIs into applications.

---

## Practice Exercises

### Exercise 1: Weather Lookup
1. Create a new request for OpenWeatherMap
2. Add your API key as an environment variable
3. Test weather for 3 different cities
4. Save all requests to a "Weather" collection

### Exercise 2: CRUD Operations
Using JSONPlaceholder:
1. GET all posts: `GET /posts`
2. GET one post: `GET /posts/1`
3. CREATE a post: `POST /posts`
4. UPDATE a post: `PUT /posts/1`
5. DELETE a post: `DELETE /posts/1`

### Exercise 3: Explore a New API
1. Pick an API from https://github.com/public-apis/public-apis
2. Read its documentation
3. Make successful requests in Postman
4. Save working requests to a collection

---

## Quick Reference

### Common Headers

| Header | Purpose | Example |
|--------|---------|---------|
| Content-Type | Format of body data | `application/json` |
| Authorization | Authentication token | `Bearer your-token` |
| Accept | Expected response format | `application/json` |
| X-API-Key | API key (custom header) | `your-api-key` |

### Keyboard Shortcuts

| Action | Windows/Linux | Mac |
|--------|---------------|-----|
| Send request | Ctrl + Enter | Cmd + Enter |
| Save request | Ctrl + S | Cmd + S |
| New request | Ctrl + N | Cmd + N |
| New tab | Ctrl + T | Cmd + T |

---

## Resources

| Resource | URL |
|----------|-----|
| Postman Download | https://www.postman.com/downloads/ |
| Postman Learning Center | https://learning.postman.com/ |
| Public APIs List | https://github.com/public-apis/public-apis |
| JSONPlaceholder (Test API) | https://jsonplaceholder.typicode.com/ |

---

## Alternatives to Postman

| Tool | Description |
|------|-------------|
| **Insomnia** | Similar to Postman, open source option |
| **Thunder Client** | VS Code extension |
| **HTTPie** | Command-line tool |
| **cURL** | Command-line classic |
| **Hoppscotch** | Open source, web-based |

---

## Instructor Notes

### If Teaching as Session

**Duration:** 15-20 minutes

**Flow:**
1. Demo Postman interface (3 min)
2. Live: Make a GET request together (5 min)
3. Live: Make a POST request (5 min)
4. Show Collections and Environments (3 min)
5. Show code generation feature (2 min)

**Key Points:**
- Emphasize no coding required
- Show how it's useful for testing before writing code
- Demonstrate the code generation feature as bridge to Python

### When to Introduce

- **Option A:** After Session 1 (before Python coding) - gives immediate hands-on
- **Option B:** After Session 3 (after Python) - shows alternative approach
- **Option C:** As take-home reference material only
