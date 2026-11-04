#!/usr/bin/env python3
"""
Demo 5: POST Request - Creating Data
------------------------------------
Detailed example of sending data to an API.

POST is used when you want to CREATE something new on the server.
Examples:
- Creating a user account
- Submitting a form
- Uploading a file
- Adding a new record to a database
"""

import requests
import json

# Using JSONPlaceholder's /posts endpoint
url = "https://jsonplaceholder.typicode.com/posts"

# The data we want to create
# This would be like filling out a form
new_post = {
    "title": "Understanding POST Requests",
    "body": "POST requests send data TO the server to create new resources.",
    "userId": 42
}

print("="*50)
print("POST Request Demo - Creating a New Blog Post")
print("="*50)

print("\n1. The data we're sending:")
print(json.dumps(new_post, indent=2))

print("\n2. Making the POST request...")

# Key difference from GET:
# - We use requests.post() instead of requests.get()
# - We include data in the 'json' parameter
response = requests.post(url, json=new_post)

print(f"\n3. Server response:")
print(f"   Status Code: {response.status_code}")

if response.status_code == 201:  # 201 = Created
    print("   Result: SUCCESS - Resource created!")
    result = response.json()
    print(f"\n4. Server assigned ID: {result.get('id')}")
    print("\n   Full response:")
    print(json.dumps(result, indent=2))
else:
    print(f"   Result: FAILED - {response.status_code}")
    print(response.text)

print("\n" + "="*50)
print("Key Takeaways:")
print("="*50)
print("""
1. POST sends data IN the request body
2. Server processes the data and creates a resource
3. Server returns the created resource (often with a new ID)
4. Status 201 means "Created" - the operation succeeded
""")
