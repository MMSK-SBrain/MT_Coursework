#!/usr/bin/env python3
"""
Demo 4: HTTP Methods Comparison
-------------------------------
Demonstrates the four main HTTP methods: GET, POST, PUT, DELETE

Uses JSONPlaceholder - a free fake API for testing and prototyping.
https://jsonplaceholder.typicode.com/

HTTP Methods Summary:
- GET:    Retrieve data (Read)
- POST:   Create new data (Create)
- PUT:    Update existing data (Update)
- DELETE: Remove data (Delete)

Together these form "CRUD" operations: Create, Read, Update, Delete
"""

import requests
import json

BASE_URL = "https://jsonplaceholder.typicode.com"

def pretty_print(data):
    """Print JSON in a readable format."""
    print(json.dumps(data, indent=2))

# ============================================================
# GET - Retrieve existing data
# ============================================================
print("\n" + "="*60)
print("1. GET REQUEST - Fetching existing data")
print("="*60)
print("Purpose: Retrieve information from the server")
print("Example: Getting a list of blog posts\n")

response = requests.get(f"{BASE_URL}/posts/1")
print(f"GET {BASE_URL}/posts/1")
print(f"Status: {response.status_code}")
print("Response:")
pretty_print(response.json())

input("\nPress Enter to continue to POST...")

# ============================================================
# POST - Create new data
# ============================================================
print("\n" + "="*60)
print("2. POST REQUEST - Creating new data")
print("="*60)
print("Purpose: Send new data to the server to create a resource")
print("Example: Creating a new blog post\n")

new_post = {
    "title": "My First API Post",
    "body": "This post was created using Python and the requests library!",
    "userId": 1
}

print("Data we're sending:")
pretty_print(new_post)
print()

response = requests.post(
    f"{BASE_URL}/posts",
    json=new_post  # Automatically converts dict to JSON and sets headers
)

print(f"POST {BASE_URL}/posts")
print(f"Status: {response.status_code}")  # 201 = Created
print("Response (server confirms creation with ID):")
pretty_print(response.json())

input("\nPress Enter to continue to PUT...")

# ============================================================
# PUT - Update existing data
# ============================================================
print("\n" + "="*60)
print("3. PUT REQUEST - Updating existing data")
print("="*60)
print("Purpose: Replace/update an existing resource")
print("Example: Editing a blog post\n")

updated_post = {
    "id": 1,
    "title": "Updated Title - Changed via API!",
    "body": "This content has been completely replaced.",
    "userId": 1
}

print("Updated data we're sending:")
pretty_print(updated_post)
print()

response = requests.put(
    f"{BASE_URL}/posts/1",
    json=updated_post
)

print(f"PUT {BASE_URL}/posts/1")
print(f"Status: {response.status_code}")  # 200 = OK
print("Response (server confirms the update):")
pretty_print(response.json())

input("\nPress Enter to continue to DELETE...")

# ============================================================
# DELETE - Remove data
# ============================================================
print("\n" + "="*60)
print("4. DELETE REQUEST - Removing data")
print("="*60)
print("Purpose: Remove a resource from the server")
print("Example: Deleting a blog post\n")

response = requests.delete(f"{BASE_URL}/posts/1")

print(f"DELETE {BASE_URL}/posts/1")
print(f"Status: {response.status_code}")  # 200 = OK
print("Response: (empty body means successful deletion)")
print(f"Response body: {response.text if response.text else '(empty)'}")

# ============================================================
# Summary
# ============================================================
print("\n" + "="*60)
print("SUMMARY: HTTP Methods")
print("="*60)
print("""
| Method | Purpose        | Has Body? | Example Use Case          |
|--------|----------------|-----------|---------------------------|
| GET    | Read data      | No        | View a user profile       |
| POST   | Create data    | Yes       | Register a new user       |
| PUT    | Update data    | Yes       | Edit profile information  |
| DELETE | Delete data    | No        | Remove an account         |

Status Codes:
- 200: OK (Success)
- 201: Created (POST success)
- 204: No Content (DELETE success, no body returned)
- 400: Bad Request (Your request was malformed)
- 404: Not Found (Resource doesn't exist)
- 500: Server Error (Something broke on their end)
""")
