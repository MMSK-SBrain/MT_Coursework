#!/usr/bin/env python3
"""
Demo 6: PUT Request - Updating Data
-----------------------------------
Detailed example of updating existing data via API.

PUT is used when you want to UPDATE/REPLACE something that already exists.
Examples:
- Updating user profile
- Changing settings
- Editing a document
- Modifying a record
"""

import requests
import json

# We're updating post with ID 1
url = "https://jsonplaceholder.typicode.com/posts/1"

print("="*50)
print("PUT Request Demo - Updating an Existing Post")
print("="*50)

# First, let's see what the current data looks like
print("\n1. First, let's GET the current data:")
current = requests.get(url).json()
print(json.dumps(current, indent=2))

# The updated data - we're replacing the entire resource
updated_post = {
    "id": 1,
    "title": "UPDATED: New and Improved Title",
    "body": "This content has been completely updated via PUT request.",
    "userId": 1
}

print("\n2. The updated data we're sending:")
print(json.dumps(updated_post, indent=2))

print("\n3. Making the PUT request...")

# PUT replaces the entire resource
response = requests.put(url, json=updated_post)

print(f"\n4. Server response:")
print(f"   Status Code: {response.status_code}")

if response.status_code == 200:
    print("   Result: SUCCESS - Resource updated!")
    print("\n   Updated resource:")
    print(json.dumps(response.json(), indent=2))
else:
    print(f"   Result: FAILED - {response.status_code}")

print("\n" + "="*50)
print("PUT vs PATCH:")
print("="*50)
print("""
PUT:   Replaces the ENTIRE resource
       You must send ALL fields, even unchanged ones

PATCH: Updates ONLY the specified fields
       You send only what you want to change

Example:
  Current: {"name": "John", "age": 30, "city": "London"}

  PUT with {"name": "Jane", "age": 30, "city": "London"}
    → Replaces everything (must include all fields)

  PATCH with {"name": "Jane"}
    → Only changes name, keeps age and city
""")
