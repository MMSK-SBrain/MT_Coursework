# Course Structure: API Fundamentals

## Overview

| Attribute | Value |
|-----------|-------|
| Course Name | API Fundamentals for Non-Technical Professionals |
| Course Code | APIF |
| Duration | 1 Day (~2.5 hour workshop) |
| Format | Guided practice workshop with live demos |
| Theory/Practice | 40% / 60% |

---

## Learning Outcomes Hierarchy

### Course Outcomes (CO)

| ID | Code | Description | Category | Bloom |
|----|------|-------------|----------|-------|
| co-1 | APIF-CO-1 | Explain what APIs are and how they enable software integration | Knowledge | Understand |
| co-2 | APIF-CO-2 | Consume a public API using Python to retrieve and use real data | Skill | Apply |
| co-3 | APIF-CO-3 | Understand how APIs are built and secured | Knowledge | Understand |

---

## Module 1: API Fundamentals (~40 min)

**Purpose:** Build conceptual understanding of APIs, HTTP, and data formats

### Module Outcomes

| ID | Code | Description | Category | Bloom | Parent CO |
|----|------|-------------|----------|-------|-----------|
| mo-1-1 | APIF-MO-1-1 | Describe what an API is and why it matters | Knowledge | Understand | co-1 |
| mo-1-2 | APIF-MO-1-2 | Explain the request/response cycle | Knowledge | Understand | co-1 |
| mo-1-3 | APIF-MO-1-3 | Differentiate HTTP methods and their purposes | Knowledge | Understand | co-1 |

### Lesson 1.1: What is an API? (Day 1)

| SO ID | Code | Description | Category | Bloom | Session Type |
|-------|------|-------------|----------|-------|--------------|
| so-1-1-1 | APIF-SO-1-1-1 | Define API in non-technical terms | Knowledge | Remember | lecture |
| so-1-1-2 | APIF-SO-1-1-2 | Identify real-world examples of APIs (weather apps, payment systems) | Knowledge | Understand | lecture |
| so-1-1-3 | APIF-SO-1-1-3 | Describe the client-server request/response model | Knowledge | Understand | lecture |
| so-1-1-4 | APIF-SO-1-1-4 | Explain what JSON is and how to read it | Knowledge | Understand | lecture |
| so-1-1-5 | APIF-SO-1-1-5 | Differentiate GET, POST, PUT, DELETE methods and their purposes | Knowledge | Understand | lecture |

**Content:**
- Restaurant analogy: API as a waiter between customer (app) and kitchen (server)
- Examples: Weather widgets, payment buttons, social media embeds
- Request → Process → Response diagram
- JSON basics: key-value pairs, reading data
- HTTP Methods: GET (read), POST (create), PUT (update), DELETE (remove)
- CRUD operations and their HTTP equivalents

**Demo Scripts:** `04_http_methods_demo.py`

---

## Module 2: Consuming APIs (~60 min) - PRIMARY FOCUS

**Purpose:** Hands-on practice making API calls

### Module Outcomes

| ID | Code | Description | Category | Bloom | Parent CO |
|----|------|-------------|----------|-------|-----------|
| mo-2-1 | APIF-MO-2-1 | Make GET requests to a public API using Python | Skill | Apply | co-2 |
| mo-2-2 | APIF-MO-2-2 | Extract and use data from JSON responses | Skill | Apply | co-2 |

### Lesson 2.1: Your First API Call (Day 1)

| SO ID | Code | Description | Category | Bloom | Session Type |
|-------|------|-------------|----------|-------|--------------|
| so-2-1-1 | APIF-SO-2-1-1 | Install and import the Python requests library | Skill | Apply | lab |
| so-2-1-2 | APIF-SO-2-1-2 | Obtain and use an API key for authentication | Skill | Apply | lab |
| so-2-1-3 | APIF-SO-2-1-3 | Make a GET request to the weather API | Skill | Apply | lab |
| so-2-1-4 | APIF-SO-2-1-4 | Interpret HTTP status codes (200 OK, 401, 404) | Knowledge | Understand | lab |

**Demo Scripts:** `01_simple_get.py`

### Lesson 2.2: Working with Response Data (Day 1)

| SO ID | Code | Description | Category | Bloom | Session Type |
|-------|------|-------------|----------|-------|--------------|
| so-2-2-1 | APIF-SO-2-2-1 | Parse JSON response into Python dictionary | Skill | Apply | lab |
| so-2-2-2 | APIF-SO-2-2-2 | Extract specific values from nested JSON | Skill | Apply | lab |
| so-2-2-3 | APIF-SO-2-2-3 | Print formatted weather information to console | Skill | Apply | lab |

**Demo Scripts:** `02_parsed_weather.py`, `03_interactive_weather.py`

**Hands-on Exercise:**
1. Sign up for OpenWeatherMap API key
2. Write Python script to fetch current weather
3. Extract temperature, humidity, description
4. Display: "The weather in [city] is [description], [temp]C"

---

## Module 3: API Creation & Security (~35 min)

**Purpose:** Understanding how APIs are built and secured

### Module Outcomes

| ID | Code | Description | Category | Bloom | Parent CO |
|----|------|-------------|----------|-------|-----------|
| mo-3-1 | APIF-MO-3-1 | Explain how APIs are created at a high level | Knowledge | Understand | co-3 |
| mo-3-2 | APIF-MO-3-2 | Identify common API security practices | Knowledge | Remember | co-3 |
| mo-3-3 | APIF-MO-3-3 | Recognize FastAPI's key features and patterns | Knowledge | Understand | co-3 |

### Lesson 3.1: Behind the Scenes (Day 1) - 20 min

| SO ID | Code | Description | Category | Bloom | Session Type |
|-------|------|-------------|----------|-------|--------------|
| so-3-1-1 | APIF-SO-3-1-1 | Describe what happens on the server side when an API receives a request | Knowledge | Understand | lecture |
| so-3-1-2 | APIF-SO-3-1-2 | List common API security measures (API keys, OAuth, rate limiting) | Knowledge | Remember | lecture |
| so-3-1-3 | APIF-SO-3-1-3 | Explain why API keys should be kept secret | Knowledge | Understand | lecture |

**Content:**
- Server-side request processing
- API key security: don't commit to git, use environment variables
- Rate limiting: why APIs restrict requests
- Authentication types: API keys vs OAuth

### Lesson 3.2: Building APIs with FastAPI (Day 1) - 15 min LIVE SHOWCASE

| SO ID | Code | Description | Category | Bloom | Session Type |
|-------|------|-------------|----------|-------|--------------|
| so-3-2-1 | APIF-SO-3-2-1 | Observe how a simple API is created with FastAPI | Knowledge | Understand | lecture |
| so-3-2-2 | APIF-SO-3-2-2 | Recognize automatic documentation generation in FastAPI | Knowledge | Remember | lecture |
| so-3-2-3 | APIF-SO-3-2-3 | Connect consumer and producer perspectives of APIs | Knowledge | Understand | lecture |

**Demo Scripts:** `07_fastapi_hello.py`, `08_fastapi_crud.py`, `09_fastapi_weather_api.py`

**Live Demo Content:**
1. Create Hello World API from scratch (~5 min)
2. Add path and query parameters (~4 min)
3. Show automatic documentation at /docs (~2 min)
4. Brief look at CRUD patterns (~2 min)
5. Connect consumer/producer perspectives (~2 min)

---

## Summary

| Module | Lessons | Duration | Focus |
|--------|---------|----------|-------|
| 1. API Fundamentals | 1 | ~40 min | Theory + HTTP Methods |
| 2. Consuming APIs | 2 | ~60 min | Hands-on Labs |
| 3. Creation & Security | 2 | ~35 min | Awareness + FastAPI Demo |
| **Total** | **5** | **~135 min** | + 15 min buffer/Q&A |

---

## Session Flow

| Session | Title | Duration | Type |
|---------|-------|----------|------|
| 1 | What is an API? | 40 min | Lecture |
| 2 | Your First API Call | 30 min | Lab |
| 3 | Working with Response Data | 30 min | Lab |
| 4 | Behind the Scenes | 20 min | Lecture |
| 5 | FastAPI Showcase | 15 min | Live Demo |

---

## Demo Scripts Reference

| Script | Used In | Purpose |
|--------|---------|---------|
| `01_simple_get.py` | Session 2 | Basic GET request |
| `02_parsed_weather.py` | Session 3 | JSON parsing |
| `03_interactive_weather.py` | Session 3 | Complete app |
| `04_http_methods_demo.py` | Session 1 | GET/POST/PUT/DELETE comparison |
| `05_post_example.py` | Reference | POST in detail |
| `06_put_example.py` | Reference | PUT in detail |
| `07_fastapi_hello.py` | Session 5 | FastAPI Hello World |
| `08_fastapi_crud.py` | Session 5 | FastAPI CRUD example |
| `09_fastapi_weather_api.py` | Reference | Weather API wrapper |

---

## Outcomes Summary

- **Course Outcomes:** 3
- **Module Outcomes:** 8
- **Session Outcomes:** 18
- **Sessions:** 5
- **Demo Scripts:** 9
