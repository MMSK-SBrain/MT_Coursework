#!/usr/bin/env python3
"""
FastAPI Demo 2: Full CRUD API
-----------------------------
A complete API with Create, Read, Update, Delete operations.

This simulates a simple task/todo management system.

To run:
1. pip install fastapi uvicorn
2. uvicorn 08_fastapi_crud:app --reload
3. Open: http://localhost:8000/docs

The /docs page lets you test all endpoints interactively!
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

# Create the app
app = FastAPI(
    title="Task Manager API",
    description="A CRUD API for managing tasks - demonstrates GET, POST, PUT, DELETE",
    version="1.0.0"
)

# ============================================================
# Data Model - defines the structure of a Task
# ============================================================
class TaskCreate(BaseModel):
    """Schema for creating a new task."""
    title: str
    description: Optional[str] = None
    completed: bool = False

class Task(BaseModel):
    """Schema for a complete task (includes ID)."""
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False

# ============================================================
# In-memory "database" (just a dictionary for demo)
# ============================================================
tasks_db: dict[int, dict] = {
    1: {"id": 1, "title": "Learn APIs", "description": "Understand REST concepts", "completed": True},
    2: {"id": 2, "title": "Build an API", "description": "Create a FastAPI server", "completed": False},
    3: {"id": 3, "title": "Deploy to production", "description": None, "completed": False},
}
next_id = 4  # Track the next available ID

# ============================================================
# GET - Read operations
# ============================================================

@app.get("/", tags=["Root"])
def root():
    """API welcome message."""
    return {
        "message": "Welcome to the Task Manager API",
        "docs": "Visit /docs for interactive documentation",
        "endpoints": {
            "GET /tasks": "List all tasks",
            "GET /tasks/{id}": "Get a specific task",
            "POST /tasks": "Create a new task",
            "PUT /tasks/{id}": "Update a task",
            "DELETE /tasks/{id}": "Delete a task"
        }
    }

@app.get("/tasks", response_model=list[Task], tags=["Tasks"])
def get_all_tasks():
    """
    Get all tasks.

    Returns a list of all tasks in the system.
    """
    return list(tasks_db.values())

@app.get("/tasks/{task_id}", response_model=Task, tags=["Tasks"])
def get_task(task_id: int):
    """
    Get a specific task by ID.

    - **task_id**: The unique identifier of the task
    """
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail=f"Task {task_id} not found")
    return tasks_db[task_id]

# ============================================================
# POST - Create operation
# ============================================================

@app.post("/tasks", response_model=Task, status_code=201, tags=["Tasks"])
def create_task(task: TaskCreate):
    """
    Create a new task.

    - **title**: The task title (required)
    - **description**: Optional description
    - **completed**: Whether the task is done (default: false)
    """
    global next_id

    new_task = {
        "id": next_id,
        "title": task.title,
        "description": task.description,
        "completed": task.completed
    }

    tasks_db[next_id] = new_task
    next_id += 1

    return new_task

# ============================================================
# PUT - Update operation
# ============================================================

@app.put("/tasks/{task_id}", response_model=Task, tags=["Tasks"])
def update_task(task_id: int, task: TaskCreate):
    """
    Update an existing task.

    Replaces the task with the provided data.
    """
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail=f"Task {task_id} not found")

    updated_task = {
        "id": task_id,
        "title": task.title,
        "description": task.description,
        "completed": task.completed
    }

    tasks_db[task_id] = updated_task
    return updated_task

# ============================================================
# DELETE - Delete operation
# ============================================================

@app.delete("/tasks/{task_id}", tags=["Tasks"])
def delete_task(task_id: int):
    """
    Delete a task.

    - **task_id**: The ID of the task to delete
    """
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail=f"Task {task_id} not found")

    deleted_task = tasks_db.pop(task_id)
    return {"message": f"Task {task_id} deleted", "deleted_task": deleted_task}

# ============================================================
# Bonus: Filter tasks
# ============================================================

@app.get("/tasks/filter/", response_model=list[Task], tags=["Tasks"])
def filter_tasks(completed: Optional[bool] = None):
    """
    Filter tasks by completion status.

    - **completed**: true for completed tasks, false for pending
    """
    if completed is None:
        return list(tasks_db.values())

    return [task for task in tasks_db.values() if task["completed"] == completed]


# ============================================================
# Run with: uvicorn 08_fastapi_crud:app --reload
#
# Then open: http://localhost:8000/docs
# You can test all operations directly from the browser!
# ============================================================
