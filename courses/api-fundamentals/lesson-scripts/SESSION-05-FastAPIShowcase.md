# Session 5: Building APIs with FastAPI - Live Showcase

**Module:** 3 - API Creation & Security Overview (Extended)
**Duration:** ~15 minutes
**Type:** Live coding demonstration
**Prerequisites:** Sessions 1-4 completed

---

## Session Overview

| Learning Outcome | Code | What Learners Will Do |
|-----------------|------|----------------------|
| Understand how APIs are built | SO-3-1-4 | Watch a simple API being created from scratch |
| Recognize FastAPI's key features | SO-3-1-5 | See automatic documentation and type validation |
| Connect consumer/producer perspectives | SO-3-1-6 | Understand both sides of the API conversation |

---

## Materials Needed

- Instructor laptop with:
  - Python 3.8+
  - FastAPI and uvicorn installed (`pip install fastapi uvicorn`)
  - Code editor visible on projector
  - Terminal visible on projector
- Demo scripts ready: `07_fastapi_hello.py`, `08_fastapi_crud.py`

### Pre-Demo Checklist

```bash
# Verify installation
pip install fastapi uvicorn

# Test that it works
python -c "import fastapi; print('FastAPI ready!')"
```

---

## Session Script

### Opening: Flipping to the Other Side (2 minutes)

> "So far, we've been the **consumers** - we asked APIs for data and got responses back. But who builds these APIs? How does it actually work on the other side?"

> "I'm going to show you - live - how to build a simple API server. We won't write it together (that would take longer than we have), but I want you to see that it's not magic."

> "We're using a Python library called **FastAPI**. It's one of the most popular tools for building APIs, and it's surprisingly simple."

---

### Part 1: FastAPI Introduction (3 minutes)

**[SLIDE: FastAPI logo and features]**

#### Why FastAPI?

> "There are many tools for building APIs - Flask, Django, Express, Spring. I chose FastAPI for this demo because:"

> "**1. It's Python** - Same language you just learned to use!"

> "**2. It's minimal** - We can build a working API in about 10 lines of code"

> "**3. Auto-documentation** - It automatically creates interactive docs (this is really cool, you'll see)"

> "**4. It's modern** - Used by Microsoft, Netflix, Uber, and many others"

---

#### The Basic Structure

> "Every FastAPI app has this basic structure:"

**[SLIDE: Code structure]**

```python
from fastapi import FastAPI    # Import the library

app = FastAPI()                 # Create an app

@app.get("/")                   # Define a route
def home():
    return {"message": "Hello"} # Return JSON
```

> "That's it. Four lines and you have a working API."

> "Let me show you..."

---

### Part 2: Live Demo - Hello World API (5 minutes)

**[Switch to code editor - visible on screen]**

> "I'm going to build this from scratch. Watch what happens."

#### Step 1: Create the File

> "First, let me create a new file called `my_api.py`..."

**[Type in editor]**

```python
from fastapi import FastAPI

app = FastAPI(title="My First API")

@app.get("/")
def home():
    return {"message": "Hello from my API!"}
```

> "Let me explain each line:"
> - "`from fastapi import FastAPI` - We import the library"
> - "`app = FastAPI()` - We create our application"
> - "`@app.get('/')` - This is called a 'decorator' - it says 'when someone visits /, run this function'"
> - "`return {...}` - We return a dictionary, which FastAPI converts to JSON"

---

#### Step 2: Run It

> "Now let's run it..."

**[Switch to terminal]**

```bash
uvicorn my_api:app --reload
```

> "Uvicorn is a web server that runs our API. The `--reload` flag means it restarts automatically when we change code."

**[Server should start]**

> "See that? It's running on `http://localhost:8000`"

---

#### Step 3: Test It

> "Let's visit it in the browser..."

**[Open browser to http://localhost:8000]**

> "There it is! Our API returned JSON, just like the weather API we used earlier. But this time, WE built it!"

---

#### Step 4: The Magic - Auto Documentation

> "Now here's the really cool part. Go to `/docs`..."

**[Navigate to http://localhost:8000/docs]**

> "Look at that! FastAPI automatically created interactive documentation. We didn't write any of this - it generated it from our code."

> "You can actually test the API right here..."

**[Click on the endpoint, click "Try it out", then "Execute"]**

> "See? It made a request and showed the response. This is what makes FastAPI special - it gives you documentation for free."

---

### Part 3: Adding More Features (4 minutes)

> "Let me quickly show you how easy it is to add more functionality..."

**[Back to editor - add to existing code]**

```python
from fastapi import FastAPI

app = FastAPI(title="My First API")

@app.get("/")
def home():
    return {"message": "Hello from my API!"}

# NEW: Greeting with a name
@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}!", "name": name}

# NEW: Simple calculator
@app.get("/add")
def add(a: int, b: int):
    return {"a": a, "b": b, "result": a + b}
```

> "I added two more endpoints:"
> - "`/greet/{name}` - The `{name}` in curly braces is a **path parameter** - whatever you put there becomes the `name` variable"
> - "`/add` - This expects **query parameters** `a` and `b`"

**[Refresh browser docs page]**

> "Look - the docs updated automatically! We now have three endpoints."

**[Demo each one]**

> "Let's try the greeting..."

**[In docs: /greet/{name} → Try it out → name: "Workshop" → Execute]**

> "And the calculator..."

**[In docs: /add → Try it out → a: 10, b: 5 → Execute]**

> "Notice something interesting? I said `a: int` and `b: int` in the code. FastAPI automatically validates that these are numbers. Try putting text..."

**[Demo validation error]**

> "See? It tells you 'value is not a valid integer'. We didn't write that validation - FastAPI did it automatically because we specified the types."

---

### Part 4: Quick Look at CRUD (2 minutes)

> "In the real world, APIs usually do more than just read data. Remember our CRUD operations? GET, POST, PUT, DELETE?"

> "Let me show you a more complete example..."

**[Open `08_fastapi_crud.py` - or show on slide]**

```python
@app.get("/tasks")
def get_all_tasks():
    return list(tasks_db.values())

@app.post("/tasks")
def create_task(task: TaskCreate):
    # ... creates a new task
    return new_task

@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: TaskCreate):
    # ... updates existing task
    return updated_task

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    # ... deletes the task
    return {"message": "Deleted"}
```

> "See how similar the patterns are? You just use `@app.post()` for POST, `@app.put()` for PUT, `@app.delete()` for DELETE."

> "The structure is the same - you define a function, and FastAPI handles the HTTP plumbing."

**[If time: Open localhost:8000/docs for CRUD app and show all endpoints]**

---

### Wrap-Up: Connecting the Dots (2 minutes)

**[SLIDE: Consumer vs Producer]**

> "Let's connect what you learned today:"

```
CONSUMER (You earlier)          PRODUCER (What you just saw)
─────────────────────           ────────────────────────────
requests.get(url)         →     @app.get("/...")
response.json()           ←     return {"data": ...}
Status codes (200, 404)   ←     FastAPI handles automatically
```

> "When you called `requests.get()` in Sessions 2 and 3, there was a server somewhere running code just like this - waiting for your request, processing it, and sending back JSON."

> "You've now seen both sides of the conversation!"

---

#### Key Takeaways

**[SLIDE: Summary]**

> "What we saw:"

> "**1. APIs are just code** - Python functions that return data"

> "**2. FastAPI is simple** - Working API in ~10 lines"

> "**3. Auto-documentation is amazing** - Write code, get docs free"

> "**4. Type hints enable validation** - Specify types, get automatic checking"

> "**5. Same patterns, different decorators** - GET, POST, PUT, DELETE all work similarly"

---

#### Resources for the Curious

> "If you want to explore this more on your own:"

| Resource | URL |
|----------|-----|
| FastAPI Tutorial | https://fastapi.tiangolo.com/tutorial/ |
| Full Documentation | https://fastapi.tiangolo.com/ |
| Demo Scripts | See `demo-scripts/` folder |

> "The demo code I showed is in your course materials. You can run it yourself and experiment."

---

## Complete Demo Files Reference

### Quick Start (for instructor)

```bash
# Navigate to demo folder
cd demo-scripts/

# Run Hello World
uvicorn 07_fastapi_hello:app --reload

# Run CRUD API (more complete example)
uvicorn 08_fastapi_crud:app --reload

# Run Weather Wrapper (shows real-world pattern)
uvicorn 09_fastapi_weather_api:app --reload
```

### Files Provided to Students

| File | Purpose |
|------|---------|
| `07_fastapi_hello.py` | Basic Hello World - matches live demo |
| `08_fastapi_crud.py` | Complete CRUD example with tasks |
| `09_fastapi_weather_api.py` | Weather API wrapper - shows real-world pattern |

---

## Instructor Notes

### Pre-Demo Setup

1. Test all demos work before class
2. Have terminal and browser windows arranged for easy switching
3. Increase font size in editor and terminal
4. Close other applications to avoid notifications

### Common Demo Issues

| Issue | Solution |
|-------|----------|
| Port 8000 in use | Use `--port 8001` |
| Module not found | Run `pip install fastapi uvicorn` |
| Changes not reflecting | Check `--reload` flag is set |
| Can't access localhost | Try `127.0.0.1:8000` instead |

### If Running Behind

- Skip the calculator demo, just show greeting
- Don't demo the CRUD file, just show the code on slide
- Cut the validation demo

### If Running Ahead

- Show the weather wrapper API (`09_fastapi_weather_api.py`)
- Let students try accessing the API from their machines (share localhost via ngrok if available)
- Discuss how this would be deployed to production

### Engagement Tips

- Ask students to predict what will happen before each demo step
- "What do you think we'll see when I visit /docs?"
- "What error might we get if I type 'hello' instead of a number?"

### Backup Plan

If live demo fails, use the pre-recorded video or static screenshots in slides. The demo files in `demo-scripts/` can be shown as code-only without running.
