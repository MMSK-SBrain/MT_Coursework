# API Security Checklist for ML Applications

Essential security practices for production ML APIs.

---

## Table of Contents

1. [Authentication & Authorization](#authentication--authorization)
2. [Input Validation](#input-validation)
3. [Rate Limiting](#rate-limiting)
4. [HTTPS & Encryption](#https--encryption)
5. [CORS Configuration](#cors-configuration)
6. [Error Handling](#error-handling)
7. [Logging & Monitoring](#logging--monitoring)
8. [Environment Variables](#environment-variables)
9. [Dependencies & Updates](#dependencies--updates)
10. [Security Testing](#security-testing)

---

## Authentication & Authorization

### Why It Matters:
Without authentication, anyone can use your API, leading to:
- Unauthorized access to predictions
- Resource abuse (costly!)
- Data leakage
- Service denial

### Implementation Options:

#### 1. API Keys (Simplest)

**Flask Example:**
```python
from flask import Flask, request, jsonify
from functools import wraps

app = Flask(__name__)

# Store API keys (in production, use database)
VALID_API_KEYS = {
    'demo-key-123': 'user1',
    'prod-key-456': 'user2'
}

def require_api_key(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        api_key = request.headers.get('X-API-Key')

        if not api_key:
            return jsonify({'error': 'API key required'}), 401

        if api_key not in VALID_API_KEYS:
            return jsonify({'error': 'Invalid API key'}), 403

        return f(*args, **kwargs)
    return decorated

@app.route('/predict', methods=['POST'])
@require_api_key
def predict():
    # Your prediction logic
    pass
```

**Usage:**
```bash
curl -X POST https://your-api.com/predict \
  -H "X-API-Key: demo-key-123" \
  -H "Content-Type: application/json" \
  -d '{"text": "example"}'
```

#### 2. JWT Tokens (More Secure)

```python
import jwt
from datetime import datetime, timedelta

SECRET_KEY = os.environ.get('JWT_SECRET_KEY')

def create_token(user_id):
    payload = {
        'user_id': user_id,
        'exp': datetime.utcnow() + timedelta(hours=24)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm='HS256')

def verify_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload['user_id']
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
```

### Security Checklist:

- [ ] Authentication implemented (API keys or JWT)
- [ ] API keys stored securely (not in code!)
- [ ] Different keys for dev/staging/production
- [ ] Key rotation policy in place
- [ ] Keys can be revoked
- [ ] Rate limiting per key
- [ ] Audit log of key usage

---

## Input Validation

### Why It Matters:
Malicious inputs can:
- Crash your API
- Execute harmful code
- Consume excessive resources
- Return sensitive information

### Best Practices:

#### 1. Validate Data Types

```python
from pydantic import BaseModel, validator

class PredictionRequest(BaseModel):
    text: str
    max_length: int = 100

    @validator('text')
    def text_not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('Text cannot be empty')
        if len(v) > 1000:
            raise ValueError('Text too long (max 1000 chars)')
        return v

    @validator('max_length')
    def valid_length(cls, v):
        if v < 1 or v > 500:
            raise ValueError('max_length must be between 1 and 500')
        return v
```

#### 2. Sanitize Inputs

```python
import re

def sanitize_text(text):
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', text)

    # Remove special characters
    text = re.sub(r'[^\w\s.,!?-]', '', text)

    # Limit length
    text = text[:1000]

    return text.strip()
```

#### 3. Validate File Uploads (for image/file models)

```python
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/predict-image', methods=['POST'])
def predict_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'Empty filename'}), 400

    if not allowed_file(file.filename):
        return jsonify({'error': 'Invalid file type'}), 400

    if len(file.read()) > MAX_FILE_SIZE:
        return jsonify({'error': 'File too large'}), 400

    file.seek(0)  # Reset file pointer
    # Process file...
```

### Validation Checklist:

- [ ] All inputs validated
- [ ] Data types checked
- [ ] String length limits enforced
- [ ] Numeric ranges validated
- [ ] File types restricted
- [ ] File sizes limited
- [ ] Special characters sanitized
- [ ] SQL injection prevented (if using database)
- [ ] Appropriate error messages returned

---

## Rate Limiting

### Why It Matters:
Prevents:
- API abuse
- DDoS attacks
- Excessive costs
- Resource exhaustion

### Implementation:

#### Using Flask-Limiter

```python
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)

limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["100 per day", "10 per hour"]
)

@app.route('/predict', methods=['POST'])
@limiter.limit("5 per minute")
def predict():
    # Your code
    pass
```

#### Custom Rate Limiting

```python
from datetime import datetime, timedelta
from collections import defaultdict

# Simple in-memory rate limiter (use Redis in production)
request_counts = defaultdict(list)

def check_rate_limit(api_key, max_requests=100, window_minutes=60):
    now = datetime.now()
    window_start = now - timedelta(minutes=window_minutes)

    # Remove old requests
    request_counts[api_key] = [
        req_time for req_time in request_counts[api_key]
        if req_time > window_start
    ]

    # Check limit
    if len(request_counts[api_key]) >= max_requests:
        return False, len(request_counts[api_key])

    # Add current request
    request_counts[api_key].append(now)
    return True, len(request_counts[api_key])

@app.route('/predict', methods=['POST'])
def predict():
    api_key = request.headers.get('X-API-Key')

    allowed, count = check_rate_limit(api_key)

    if not allowed:
        return jsonify({
            'error': 'Rate limit exceeded',
            'limit': 100,
            'window': '60 minutes'
        }), 429  # Too Many Requests

    # Continue with prediction
    pass
```

### Rate Limiting Checklist:

- [ ] Rate limits implemented
- [ ] Limits appropriate for use case
- [ ] Different limits for different tiers
- [ ] 429 status code returned when exceeded
- [ ] Retry-After header included
- [ ] Limits communicated to users
- [ ] Monitoring for rate limit hits

---

## HTTPS & Encryption

### Why It Matters:
- Prevents man-in-the-middle attacks
- Encrypts sensitive data in transit
- Required for modern browsers
- Builds user trust

### Implementation:

#### On Heroku:

HTTPS is automatic! Heroku provides SSL for all apps.

```
https://your-app.herokuapp.com  ✓ Secure
```

#### Enforce HTTPS:

```python
from flask import Flask, redirect, request

app = Flask(__name__)

@app.before_request
def before_request():
    # Redirect HTTP to HTTPS
    if request.url.startswith('http://'):
        url = request.url.replace('http://', 'https://', 1)
        return redirect(url, code=301)
```

#### Security Headers:

```python
@app.after_request
def set_security_headers(response):
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    return response
```

### HTTPS Checklist:

- [ ] HTTPS enabled
- [ ] SSL certificate valid
- [ ] HTTP redirects to HTTPS
- [ ] Security headers set
- [ ] Mixed content warnings fixed
- [ ] Certificate auto-renewal configured

---

## CORS Configuration

### Why It Matters:
Controls which websites can call your API.

### Implementation:

#### Allow All Origins (Development Only!)

```python
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow all origins - NOT for production!
```

#### Restrict Origins (Production)

```python
from flask_cors import CORS

app = Flask(__name__)

# Allow specific origins
CORS(app, resources={
    r"/api/*": {
        "origins": [
            "https://your-frontend.com",
            "https://www.your-frontend.com"
        ]
    }
})
```

#### Advanced CORS Configuration

```python
CORS(app, resources={
    r"/api/*": {
        "origins": ["https://your-frontend.com"],
        "methods": ["GET", "POST"],
        "allow_headers": ["Content-Type", "Authorization"],
        "max_age": 3600
    }
})
```

### CORS Checklist:

- [ ] CORS configured appropriately
- [ ] Origins restricted in production
- [ ] Only necessary methods allowed
- [ ] Credentials handled securely
- [ ] Preflight requests handled

---

## Error Handling

### Why It Matters:
Good error handling:
- Prevents information leakage
- Improves user experience
- Aids debugging
- Maintains security

### Best Practices:

#### 1. Don't Expose Stack Traces

```python
# BAD - Exposes internal details
@app.route('/predict', methods=['POST'])
def predict():
    try:
        result = model.predict(data)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500  # Exposes stack trace!

# GOOD - Generic error message
@app.route('/predict', methods=['POST'])
def predict():
    try:
        result = model.predict(data)
        return jsonify(result)
    except Exception as e:
        # Log the actual error
        app.logger.error(f"Prediction error: {str(e)}")

        # Return generic message
        return jsonify({
            'error': 'Prediction failed. Please try again.',
            'request_id': request_id
        }), 500
```

#### 2. Use Error Codes

```python
class APIError(Exception):
    status_code = 400

    def __init__(self, message, status_code=None):
        super().__init__()
        self.message = message
        if status_code is not None:
            self.status_code = status_code

@app.errorhandler(APIError)
def handle_api_error(error):
    response = jsonify({
        'error': error.message
    })
    response.status_code = error.status_code
    return response

# Usage
if not data:
    raise APIError('Invalid input data', 400)
```

### Error Handling Checklist:

- [ ] All exceptions caught
- [ ] No stack traces exposed
- [ ] Appropriate status codes used
- [ ] Error messages user-friendly
- [ ] Detailed errors logged internally
- [ ] Request IDs for tracking
- [ ] Error monitoring configured

---

## Logging & Monitoring

### What to Log:

```python
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    request_id = str(uuid.uuid4())

    # Log request
    logger.info(f"[{request_id}] Prediction request from {request.remote_addr}")

    try:
        data = request.json

        # Log input (be careful with sensitive data!)
        logger.info(f"[{request_id}] Input: {data}")

        # Make prediction
        result = model.predict(data)

        # Log result
        logger.info(f"[{request_id}] Prediction successful: {result}")

        return jsonify(result)

    except Exception as e:
        # Log error
        logger.error(f"[{request_id}] Error: {str(e)}", exc_info=True)
        return jsonify({'error': 'Prediction failed'}), 500
```

### What NOT to Log:

- ❌ Passwords
- ❌ API keys
- ❌ Personal identifiable information (PII)
- ❌ Credit card numbers
- ❌ Social security numbers

### Logging Checklist:

- [ ] Logging configured
- [ ] Request IDs used
- [ ] Sensitive data excluded
- [ ] Log levels appropriate
- [ ] Log rotation enabled
- [ ] Logs monitored regularly
- [ ] Alerts for errors configured

---

## Environment Variables

### Why It Matters:
Never hardcode secrets in code!

### Best Practices:

#### 1. Use Environment Variables

```python
import os

# BAD
API_KEY = 'secret-key-123'  # Don't do this!

# GOOD
API_KEY = os.environ.get('API_KEY')
if not API_KEY:
    raise ValueError("API_KEY environment variable not set")
```

#### 2. Use .env Files (Local Development)

Create `.env` file:
```
API_KEY=secret-key-123
MODEL_PATH=model.pkl
DATABASE_URL=postgresql://localhost/mydb
```

Load with python-dotenv:
```python
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.environ.get('API_KEY')
```

#### 3. Set on Heroku

```bash
heroku config:set API_KEY=secret-key-123
heroku config:set MODEL_PATH=model.pkl
```

### Environment Variables Checklist:

- [ ] No secrets in code
- [ ] .env in .gitignore
- [ ] Environment variables documented
- [ ] Different values for dev/prod
- [ ] Validation for required variables
- [ ] Secure storage of production secrets

---

## Dependencies & Updates

### Keep Dependencies Updated:

```bash
# Check for outdated packages
pip list --outdated

# Update specific package
pip install --upgrade package-name

# Update all packages (carefully!)
pip install --upgrade -r requirements.txt
```

### Security Scanning:

```bash
# Install safety
pip install safety

# Check for known vulnerabilities
safety check

# Or use pip-audit
pip install pip-audit
pip-audit
```

### Dependencies Checklist:

- [ ] Dependencies regularly updated
- [ ] Security vulnerabilities checked
- [ ] Unused dependencies removed
- [ ] Versions pinned in requirements.txt
- [ ] Dependabot or similar enabled
- [ ] Security alerts monitored

---

## Security Testing

### Manual Testing:

1. **Test Authentication:**
   - Try without API key
   - Try with invalid key
   - Try with expired token

2. **Test Input Validation:**
   - Send empty data
   - Send oversized data
   - Send wrong data types
   - Send special characters

3. **Test Rate Limiting:**
   - Send many rapid requests
   - Verify 429 response

### Automated Testing:

```python
# test_security.py
import pytest
import requests

BASE_URL = 'https://your-api.com'

def test_no_api_key():
    response = requests.post(f'{BASE_URL}/predict', json={'text': 'test'})
    assert response.status_code == 401

def test_invalid_api_key():
    headers = {'X-API-Key': 'invalid-key'}
    response = requests.post(f'{BASE_URL}/predict',
                            headers=headers,
                            json={'text': 'test'})
    assert response.status_code == 403

def test_empty_input():
    headers = {'X-API-Key': 'valid-key'}
    response = requests.post(f'{BASE_URL}/predict',
                            headers=headers,
                            json={'text': ''})
    assert response.status_code == 400

def test_rate_limit():
    headers = {'X-API-Key': 'valid-key'}
    # Send many requests
    for i in range(100):
        response = requests.post(f'{BASE_URL}/predict',
                                headers=headers,
                                json={'text': 'test'})
    # Should eventually hit rate limit
    assert response.status_code == 429
```

### Security Testing Checklist:

- [ ] Authentication tested
- [ ] Input validation tested
- [ ] Rate limiting tested
- [ ] HTTPS enforced
- [ ] CORS configured correctly
- [ ] Error handling tested
- [ ] File upload security tested
- [ ] SQL injection prevented
- [ ] XSS prevented

---

## Complete Security Checklist

### Pre-Deployment:

- [ ] Authentication implemented
- [ ] Input validation comprehensive
- [ ] Rate limiting configured
- [ ] HTTPS enforced
- [ ] CORS restricted appropriately
- [ ] Error handling secure
- [ ] Logging configured (no sensitive data)
- [ ] Environment variables used
- [ ] Dependencies updated
- [ ] Security tests pass

### Post-Deployment:

- [ ] Monitor logs regularly
- [ ] Check for security alerts
- [ ] Review access logs
- [ ] Update dependencies monthly
- [ ] Rotate API keys periodically
- [ ] Review and update CORS policies
- [ ] Audit authentication logs
- [ ] Test disaster recovery

### Monthly Security Review:

- [ ] Check for dependency vulnerabilities
- [ ] Review and rotate secrets
- [ ] Analyze access patterns
- [ ] Update security policies
- [ ] Test backups
- [ ] Review logs for anomalies

---

## Resources

- **OWASP Top 10:** https://owasp.org/www-project-top-ten/
- **API Security Best Practices:** https://owasp.org/www-project-api-security/
- **Flask Security:** https://flask.palletsprojects.com/en/2.0.x/security/
- **JWT.io:** https://jwt.io/
- **Security Headers:** https://securityheaders.com/

---

**Last Updated:** 2026-01-06
**Guide Version:** 1.0
**Module:** 9 - Deployment & MLOps
