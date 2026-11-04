# Advanced API Topics

**Type:** Reference Material / Self-Study Guide
**Audience:** Learners who want to go deeper after the workshop
**Prerequisites:** Completion of main workshop sessions

---

## Table of Contents

1. [REST vs GraphQL vs gRPC](#1-rest-vs-graphql-vs-grpc)
2. [API Versioning](#2-api-versioning)
3. [Pagination](#3-pagination)
4. [Webhooks: Push vs Pull](#4-webhooks-push-vs-pull)
5. [Authentication Deep Dive](#5-authentication-deep-dive)
6. [CORS: Cross-Origin Resource Sharing](#6-cors-cross-origin-resource-sharing)
7. [API Documentation Standards](#7-api-documentation-standards)
8. [Error Handling Patterns](#8-error-handling-patterns)
9. [Rate Limiting Strategies](#9-rate-limiting-strategies)
10. [Caching](#10-caching)
11. [Idempotency](#11-idempotency)
12. [WebSockets: Real-Time APIs](#12-websockets-real-time-apis)
13. [API Gateways](#13-api-gateways)
14. [Microservices Architecture](#14-microservices-architecture)
15. [API Design Best Practices](#15-api-design-best-practices)

---

## 1. REST vs GraphQL vs gRPC

### REST (What We Learned)

REST (Representational State Transfer) is what we used in the workshop:

```
GET /users/123        → Get user 123
POST /users           → Create a user
PUT /users/123        → Update user 123
DELETE /users/123     → Delete user 123
```

**Pros:**
- Simple and widely understood
- Stateless - each request is independent
- Cacheable
- Works with any data format (usually JSON)

**Cons:**
- Multiple requests for related data (N+1 problem)
- Over-fetching (getting more data than needed)
- Under-fetching (needing multiple requests)

---

### GraphQL

GraphQL is an alternative developed by Facebook. Instead of multiple endpoints, there's one endpoint where you specify exactly what data you want.

```graphql
# Request - ask for exactly what you need
query {
  user(id: 123) {
    name
    email
    posts {
      title
    }
  }
}

# Response - only what you asked for
{
  "data": {
    "user": {
      "name": "Alice",
      "email": "alice@example.com",
      "posts": [
        {"title": "My First Post"},
        {"title": "Another Post"}
      ]
    }
  }
}
```

**Pros:**
- Get exactly the data you need in one request
- Strongly typed schema
- Great for complex, nested data
- Single endpoint

**Cons:**
- More complex to set up
- Caching is harder
- Learning curve

**When to use:** Mobile apps, complex data relationships, when bandwidth matters.

---

### gRPC

gRPC (Google Remote Procedure Call) is a high-performance protocol using Protocol Buffers.

```protobuf
// Define the service
service UserService {
  rpc GetUser (UserRequest) returns (UserResponse);
}

message UserRequest {
  int32 id = 1;
}

message UserResponse {
  string name = 1;
  string email = 2;
}
```

**Pros:**
- Very fast (binary format)
- Strongly typed
- Bi-directional streaming
- Code generation for many languages

**Cons:**
- Not human-readable
- Browser support limited
- More complex setup

**When to use:** Microservices communication, high-performance needs, real-time streaming.

---

### Comparison Summary

| Feature | REST | GraphQL | gRPC |
|---------|------|---------|------|
| Protocol | HTTP | HTTP | HTTP/2 |
| Data Format | JSON | JSON | Protocol Buffers |
| Endpoints | Multiple | Single | Multiple (services) |
| Learning Curve | Low | Medium | High |
| Browser Support | Excellent | Excellent | Limited |
| Best For | General APIs | Complex queries | Microservices |

---

## 2. API Versioning

APIs evolve over time. Versioning helps manage changes without breaking existing integrations.

### URL Path Versioning

```
https://api.example.com/v1/users
https://api.example.com/v2/users
```

**Pros:** Clear, easy to understand
**Cons:** URL changes when version changes

### Query Parameter Versioning

```
https://api.example.com/users?version=1
https://api.example.com/users?version=2
```

**Pros:** URL stays the same
**Cons:** Easy to forget the parameter

### Header Versioning

```
GET /users
Headers:
  Accept: application/vnd.example.v1+json
```

**Pros:** Clean URLs
**Cons:** Hidden, harder to test

### Best Practices

1. **Start with v1** - Even if you think you won't need versions
2. **Deprecate gracefully** - Give users time to migrate
3. **Document changes** - Maintain a changelog
4. **Support multiple versions** - At least 2-3 versions simultaneously

---

## 3. Pagination

When APIs return large datasets, they use pagination to split results into manageable chunks.

### Offset-Based Pagination

```
GET /posts?offset=0&limit=10    → Posts 1-10
GET /posts?offset=10&limit=10   → Posts 11-20
GET /posts?offset=20&limit=10   → Posts 21-30
```

**Pros:** Simple to implement
**Cons:** Inconsistent if data changes between requests

### Cursor-Based Pagination

```
GET /posts?limit=10
→ Returns: posts + cursor: "abc123"

GET /posts?limit=10&cursor=abc123
→ Returns: next 10 posts + cursor: "def456"
```

**Pros:** Consistent results, better performance
**Cons:** Can't jump to arbitrary page

### Page-Based Pagination

```
GET /posts?page=1&per_page=10
GET /posts?page=2&per_page=10
```

**Pros:** Intuitive for users
**Cons:** Same issues as offset-based

### Response Format

```json
{
  "data": [...],
  "pagination": {
    "total": 150,
    "page": 1,
    "per_page": 10,
    "total_pages": 15,
    "next": "/posts?page=2",
    "previous": null
  }
}
```

---

## 4. Webhooks: Push vs Pull

### Pull Model (Polling)

What we did in the workshop - your app repeatedly asks the API for updates.

```
Every 5 seconds:
  GET /orders/status
  → "pending"
  → "pending"
  → "pending"
  → "shipped"  ← Finally!
```

**Cons:** Wasted requests, delays, server load

### Push Model (Webhooks)

The server notifies YOUR endpoint when something happens.

```
1. Register webhook: POST /webhooks
   {"url": "https://your-app.com/notifications", "event": "order.shipped"}

2. Wait...

3. When order ships, API calls YOUR endpoint:
   POST https://your-app.com/notifications
   {"event": "order.shipped", "order_id": 123, "timestamp": "..."}
```

**Pros:** Real-time, efficient, no wasted requests

### Common Webhook Events

| Service | Events |
|---------|--------|
| Stripe | `payment.completed`, `subscription.cancelled` |
| GitHub | `push`, `pull_request.opened`, `issue.created` |
| Slack | `message.posted`, `channel.created` |
| Shopify | `order.created`, `product.updated` |

### Webhook Security

1. **Verify signatures** - APIs send a signature you can verify
2. **Use HTTPS** - Encrypt the data in transit
3. **Validate payload** - Check the data makes sense
4. **Respond quickly** - Return 200 OK fast, process async

---

## 5. Authentication Deep Dive

### API Keys (Basic)

What we used in the workshop.

```
GET /weather?appid=abc123
# or
Headers: X-API-Key: abc123
```

**Good for:** Server-to-server, simple integrations
**Bad for:** User-specific data, mobile apps (keys can be extracted)

---

### OAuth 2.0

The standard for "Login with Google/Facebook/etc."

#### Authorization Code Flow (Web Apps)

```
1. User clicks "Login with Google"
2. Redirect to Google: /authorize?client_id=...&redirect_uri=...
3. User logs in at Google
4. Google redirects back: /callback?code=xyz
5. Exchange code for token: POST /token {code: xyz}
6. Receive access_token
7. Use token: GET /api/user Headers: Authorization: Bearer {token}
```

#### Token Types

| Token | Purpose | Lifespan |
|-------|---------|----------|
| Access Token | API requests | Short (minutes to hours) |
| Refresh Token | Get new access tokens | Long (days to months) |
| ID Token | User identity info | Short |

---

### JWT (JSON Web Tokens)

A self-contained token that carries information.

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.
eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4iLCJpYXQiOjE1MTYyMzkwMjJ9.
SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
```

Three parts (base64 encoded):
1. **Header** - Algorithm and token type
2. **Payload** - User data (claims)
3. **Signature** - Verification

**Pros:** Stateless, self-contained
**Cons:** Can't revoke easily, payload is readable (not secret)

---

### API Key vs OAuth vs JWT

| Scenario | Use |
|----------|-----|
| Server-to-server | API Key |
| User login | OAuth 2.0 |
| Stateless auth | JWT |
| Mobile app | OAuth 2.0 + JWT |
| Simple scripts | API Key |

---

## 6. CORS: Cross-Origin Resource Sharing

### The Problem

Browsers block requests from one domain to another for security.

```
Your website: https://myapp.com
API: https://api.weather.com

Browser: "Nope! Different domains. Blocked."
```

### The Solution

The API server sends headers allowing cross-origin requests:

```
Access-Control-Allow-Origin: https://myapp.com
Access-Control-Allow-Methods: GET, POST
Access-Control-Allow-Headers: Content-Type, Authorization
```

### Preflight Requests

For "complex" requests (POST with JSON, custom headers), browsers send an OPTIONS request first:

```
1. Browser: OPTIONS /api/users (Can I make this request?)
2. Server: Yes, here are the allowed methods/headers
3. Browser: POST /api/users (Actual request)
```

### Why You See CORS Errors

| Error | Cause |
|-------|-------|
| "No 'Access-Control-Allow-Origin' header" | Server doesn't allow your domain |
| "Method not allowed" | Server doesn't allow that HTTP method |
| "Header not allowed" | Server doesn't allow that header |

**Note:** CORS is a browser security feature. Server-to-server requests (Python, Postman) aren't affected.

---

## 7. API Documentation Standards

### OpenAPI (Swagger)

The most popular standard. Describes APIs in YAML or JSON.

```yaml
openapi: 3.0.0
info:
  title: Weather API
  version: 1.0.0
paths:
  /weather:
    get:
      summary: Get weather for a city
      parameters:
        - name: city
          in: query
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Weather data
          content:
            application/json:
              schema:
                type: object
                properties:
                  temperature:
                    type: number
                  conditions:
                    type: string
```

**Benefits:**
- Auto-generate documentation (Swagger UI)
- Auto-generate client code
- Validate requests/responses
- Testing tools integration

### Tools

| Tool | Purpose |
|------|---------|
| Swagger UI | Interactive documentation |
| Swagger Editor | Write OpenAPI specs |
| Redoc | Alternative documentation |
| Postman | Import OpenAPI specs |

---

## 8. Error Handling Patterns

### Standard Error Response

```json
{
  "error": {
    "code": "INVALID_PARAMETER",
    "message": "The 'email' field is not a valid email address",
    "field": "email",
    "documentation_url": "https://api.example.com/docs/errors"
  }
}
```

### HTTP Status Codes for Errors

| Code | When to Use |
|------|-------------|
| 400 Bad Request | Invalid input from client |
| 401 Unauthorized | Missing or invalid authentication |
| 403 Forbidden | Valid auth, but not allowed |
| 404 Not Found | Resource doesn't exist |
| 409 Conflict | Resource already exists |
| 422 Unprocessable Entity | Validation failed |
| 429 Too Many Requests | Rate limited |
| 500 Internal Server Error | Server bug |
| 502 Bad Gateway | Upstream service failed |
| 503 Service Unavailable | Server overloaded/maintenance |

### Best Practices

1. **Be specific** - "Invalid email format" not just "Bad request"
2. **Include error codes** - Machine-readable identifiers
3. **Provide help** - Link to documentation
4. **Don't expose internals** - No stack traces in production
5. **Log details server-side** - For debugging

---

## 9. Rate Limiting Strategies

### Why Rate Limit?

- Prevent abuse
- Ensure fair usage
- Protect server resources
- Manage costs

### Common Approaches

#### Fixed Window

```
1000 requests per hour
Resets at the top of each hour
```

#### Sliding Window

```
1000 requests in any 60-minute period
More even distribution
```

#### Token Bucket

```
Start with 100 tokens
Each request costs 1 token
Tokens regenerate at 10/second
```

### Rate Limit Headers

```
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 847
X-RateLimit-Reset: 1623456789
```

### Handling Rate Limits

```python
response = requests.get(url)

if response.status_code == 429:
    retry_after = int(response.headers.get('Retry-After', 60))
    time.sleep(retry_after)
    response = requests.get(url)  # Try again
```

---

## 10. Caching

### Why Cache?

- Faster responses
- Reduced server load
- Lower costs
- Better user experience

### Cache-Control Headers

```
Cache-Control: max-age=3600        # Cache for 1 hour
Cache-Control: no-cache            # Always validate with server
Cache-Control: no-store            # Never cache
Cache-Control: private             # Only cache in browser
Cache-Control: public              # Can cache anywhere
```

### ETags (Entity Tags)

```
1. GET /users/123
   Response: {"name": "Alice"}, ETag: "abc123"

2. GET /users/123
   Headers: If-None-Match: "abc123"

3. If unchanged: 304 Not Modified (no body, use cache)
   If changed: 200 OK with new data and new ETag
```

### Caching Strategies

| Strategy | Use Case |
|----------|----------|
| Cache-aside | Read-heavy data |
| Write-through | Data consistency critical |
| Write-behind | Write-heavy, eventual consistency OK |
| Refresh-ahead | Predictable access patterns |

---

## 11. Idempotency

### What is Idempotency?

An operation is idempotent if doing it multiple times has the same effect as doing it once.

```
Idempotent:
  GET /users/123          → Same user every time
  PUT /users/123 {...}    → Same result if repeated
  DELETE /users/123       → User deleted (or already deleted)

NOT Idempotent:
  POST /orders            → Creates new order each time!
```

### Why It Matters

Network issues can cause duplicate requests:
```
1. Client sends POST /orders
2. Server processes, creates order
3. Network hiccup - client doesn't get response
4. Client retries POST /orders
5. Server creates ANOTHER order ← Problem!
```

### Idempotency Keys

Solution: Client sends a unique key with each request.

```
POST /orders
Headers: Idempotency-Key: unique-request-id-12345

Server checks:
  - If key exists → Return cached response
  - If new key → Process and save response
```

### HTTP Method Idempotency

| Method | Idempotent? | Safe? |
|--------|-------------|-------|
| GET | Yes | Yes |
| HEAD | Yes | Yes |
| PUT | Yes | No |
| DELETE | Yes | No |
| POST | No | No |
| PATCH | No | No |

---

## 12. WebSockets: Real-Time APIs

### REST Limitation

REST is request-response. Client must keep asking for updates.

### WebSockets Solution

Persistent, bidirectional connection.

```
1. Client connects: ws://api.example.com/socket
2. Connection stays open
3. Server can push messages anytime
4. Client can send messages anytime
5. Connection closed when done
```

### Use Cases

| Use Case | Why WebSockets |
|----------|----------------|
| Chat apps | Instant message delivery |
| Live sports scores | Real-time updates |
| Stock tickers | Continuous data stream |
| Gaming | Low-latency communication |
| Collaborative editing | Sync between users |

### Python Example

```python
import websocket

def on_message(ws, message):
    print(f"Received: {message}")

def on_open(ws):
    ws.send("Hello, Server!")

ws = websocket.WebSocketApp(
    "wss://echo.websocket.org",
    on_message=on_message,
    on_open=on_open
)
ws.run_forever()
```

### REST vs WebSockets

| Feature | REST | WebSockets |
|---------|------|------------|
| Connection | New each request | Persistent |
| Direction | Client → Server | Bidirectional |
| Overhead | Higher | Lower (after connect) |
| Caching | Easy | Difficult |
| Scaling | Easier | More complex |

---

## 13. API Gateways

### What is an API Gateway?

A single entry point that sits in front of multiple APIs.

```
                    ┌─────────────────┐
                    │   API Gateway   │
                    │  (Kong, AWS,    │
Clients ──────────► │   Apigee)       │
                    └────────┬────────┘
                             │
        ┌────────────────────┼────────────────────┐
        ▼                    ▼                    ▼
  ┌──────────┐        ┌──────────┐        ┌──────────┐
  │ Users    │        │ Orders   │        │ Products │
  │ Service  │        │ Service  │        │ Service  │
  └──────────┘        └──────────┘        └──────────┘
```

### Gateway Functions

| Function | Description |
|----------|-------------|
| **Routing** | Direct requests to correct service |
| **Authentication** | Verify tokens, API keys |
| **Rate Limiting** | Enforce usage limits |
| **Caching** | Cache responses |
| **Logging** | Track all requests |
| **Transformation** | Modify requests/responses |
| **Load Balancing** | Distribute traffic |

### Popular API Gateways

- **Kong** - Open source, extensible
- **AWS API Gateway** - AWS managed service
- **Apigee** - Google's enterprise solution
- **Azure API Management** - Microsoft's offering
- **Nginx** - Can act as simple gateway

---

## 14. Microservices Architecture

### Monolith vs Microservices

**Monolith:**
```
┌─────────────────────────────────────┐
│           Single Application        │
│  ┌─────┐  ┌─────┐  ┌─────┐        │
│  │Users│  │Orders│ │Products│       │
│  └─────┘  └─────┘  └─────┘        │
│         Single Database             │
└─────────────────────────────────────┘
```

**Microservices:**
```
┌─────────┐    ┌─────────┐    ┌─────────┐
│  Users  │    │ Orders  │    │Products │
│ Service │    │ Service │    │ Service │
│   API   │    │   API   │    │   API   │
├─────────┤    ├─────────┤    ├─────────┤
│Users DB │    │Orders DB│    │Prod DB  │
└─────────┘    └─────────┘    └─────────┘
```

### Microservices Communicate via APIs

```
Order Service needs user info:
  GET http://users-service/users/123

Products Service needs to check inventory:
  GET http://inventory-service/stock/456
```

### Benefits

- Independent deployment
- Technology flexibility
- Scalability per service
- Team autonomy

### Challenges

- Network complexity
- Distributed transactions
- Debugging across services
- Operational overhead

---

## 15. API Design Best Practices

### Naming Conventions

```
✓ Good:
  GET /users
  GET /users/123
  GET /users/123/orders
  POST /users

✗ Bad:
  GET /getUsers
  GET /user_list
  POST /createNewUser
```

### Use Nouns, Not Verbs

```
✓ GET /orders         (noun)
✗ GET /getOrders      (verb in URL)

✓ POST /users         (noun)
✗ POST /createUser    (verb in URL)
```

### Use Plural Names

```
✓ /users, /orders, /products
✗ /user, /order, /product
```

### Hierarchical Resources

```
GET /users/123/orders          # Orders for user 123
GET /orders/456/items          # Items in order 456
```

### Filtering, Sorting, Pagination

```
GET /products?category=electronics    # Filter
GET /products?sort=price              # Sort
GET /products?page=2&limit=10         # Paginate
GET /products?category=electronics&sort=price&page=2
```

### Consistent Response Format

```json
{
  "data": { ... },
  "meta": {
    "total": 100,
    "page": 1
  },
  "links": {
    "self": "/users?page=1",
    "next": "/users?page=2"
  }
}
```

### Use Appropriate Status Codes

| Action | Success Code |
|--------|--------------|
| GET | 200 OK |
| POST | 201 Created |
| PUT | 200 OK |
| DELETE | 204 No Content |

### Version Your API

```
/v1/users
/v2/users
```

### Document Everything

- All endpoints
- Request/response formats
- Error codes
- Authentication
- Rate limits
- Examples

---

## Summary: What to Learn Next

Based on your role and interests:

| If You're... | Focus On |
|--------------|----------|
| **Product Manager** | API versioning, documentation, webhooks |
| **Business Analyst** | GraphQL queries, pagination, error patterns |
| **Project Manager** | Rate limiting, SLAs, monitoring |
| **Technical Lead** | All topics, especially architecture |
| **Developer (next step)** | Authentication, WebSockets, caching |

---

## Resources for Further Learning

### Books
- "RESTful Web APIs" by Leonard Richardson
- "API Design Patterns" by JJ Geewax
- "Building Microservices" by Sam Newman

### Online Courses
- Postman API Fundamentals (free)
- REST API Design (Udemy, Coursera)
- OAuth 2.0 courses (various platforms)

### Documentation
- https://swagger.io/specification/ (OpenAPI)
- https://graphql.org/learn/ (GraphQL)
- https://oauth.net/2/ (OAuth 2.0)

### Practice
- https://github.com/public-apis/public-apis (API list)
- https://httpbin.org (Testing tool)
- https://reqres.in (Fake API for testing)
