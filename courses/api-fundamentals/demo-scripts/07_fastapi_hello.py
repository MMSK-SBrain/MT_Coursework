#!/usr/bin/env python3
"""
FastAPI Demo 1: Hello World API
-------------------------------
The simplest possible API server using FastAPI.

To run this:
1. Install FastAPI: pip install fastapi uvicorn
2. Run: uvicorn 07_fastapi_hello:app --reload
3. Open browser: http://localhost:8000
4. See docs: http://localhost:8000/docs

FastAPI automatically creates interactive documentation!
"""

from fastapi import FastAPI

# Create the FastAPI application
app = FastAPI(
    title="My First API",
    description="A simple API built with FastAPI",
    version="1.0.0"
)

# Define a route - when someone visits "/", return this
@app.get("/")
def read_root():
    """Return a simple greeting."""
    return {"message": "Hello, World!", "status": "success"}

# Another route - with a path parameter
@app.get("/greet/{name}")
def greet_user(name: str):
    """Greet a specific user by name."""
    return {
        "message": f"Hello, {name}!",
        "name": name
    }

# Route with query parameters
@app.get("/calculate")
def calculate(a: int, b: int, operation: str = "add"):
    """
    Perform a calculation.

    - **a**: First number
    - **b**: Second number
    - **operation**: add, subtract, multiply, or divide
    """
    if operation == "add":
        result = a + b
    elif operation == "subtract":
        result = a - b
    elif operation == "multiply":
        result = a * b
    elif operation == "divide":
        result = a / b if b != 0 else "Cannot divide by zero"
    else:
        return {"error": f"Unknown operation: {operation}"}

    return {
        "a": a,
        "b": b,
        "operation": operation,
        "result": result
    }


# ============================================================
# Run with: uvicorn 07_fastapi_hello:app --reload
#
# Then try these URLs:
#   http://localhost:8000/
#   http://localhost:8000/greet/Alice
#   http://localhost:8000/calculate?a=10&b=5&operation=add
#   http://localhost:8000/docs  (interactive documentation!)
# ============================================================
