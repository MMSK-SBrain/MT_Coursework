# Heroku Deployment Guide for ML Applications

Complete step-by-step guide for deploying Flask/FastAPI ML applications to Heroku.

---

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Heroku Setup](#heroku-setup)
3. [Preparing Your Application](#preparing-your-application)
4. [Deployment Steps](#deployment-steps)
5. [Testing Your Deployment](#testing-your-deployment)
6. [Troubleshooting](#troubleshooting)
7. [Cost Optimization](#cost-optimization)

---

## Prerequisites

### What You Need:

- [ ] Python application (Flask or FastAPI)
- [ ] Git installed and basic Git knowledge
- [ ] Heroku account (free tier available)
- [ ] Heroku CLI installed
- [ ] Your ML model saved and working locally

### System Requirements:

- Python 3.8 or later
- At least 512MB available for model files (Heroku limit)
- Internet connection

---

## Heroku Setup

### Step 1: Create Heroku Account

1. Go to [https://signup.heroku.com/](https://signup.heroku.com/)
2. Sign up with your email
3. Verify your email address
4. Choose "Python" as your primary development language

### Step 2: Install Heroku CLI

**macOS:**
```bash
brew tap heroku/brew && brew install heroku
```

**Windows:**
Download from [https://devcenter.heroku.com/articles/heroku-cli](https://devcenter.heroku.com/articles/heroku-cli)

**Linux:**
```bash
curl https://cli-assets.heroku.com/install.sh | sh
```

### Step 3: Verify Installation

```bash
heroku --version
# Should show: heroku/x.x.x
```

### Step 4: Login to Heroku

```bash
heroku login
```

This will open a browser for authentication. Follow the prompts.

---

## Preparing Your Application

### Required Files Checklist:

- [ ] `app.py` - Your Flask/FastAPI application
- [ ] `requirements.txt` - All Python dependencies
- [ ] `Procfile` - Tells Heroku how to run your app
- [ ] `runtime.txt` - Specifies Python version
- [ ] `model.pkl` (or .h5) - Your trained model
- [ ] `.gitignore` - Files to exclude from Git

### Step 1: Create requirements.txt

List all dependencies with specific versions:

```txt
# requirements.txt
flask==2.3.0
gunicorn==21.2.0
scikit-learn==1.3.0
numpy==1.24.0
pandas==2.0.0
joblib==1.3.0
```

**Generate automatically:**
```bash
pip freeze > requirements.txt
```

**Important:** Remove unnecessary packages to reduce slug size!

### Step 2: Create Procfile

Create a file named `Procfile` (no extension):

**For Flask:**
```
web: gunicorn app:app
```

**For FastAPI:**
```
web: uvicorn app:app --host 0.0.0.0 --port $PORT
```

**Explanation:**
- `web:` - Tells Heroku this is a web process
- `gunicorn app:app` - Use gunicorn WSGI server, file `app.py`, app instance `app`
- `$PORT` - Heroku provides the port number

### Step 3: Create runtime.txt

Specify Python version:

```txt
python-3.10.12
```

**Check available versions:**
[https://devcenter.heroku.com/articles/python-support](https://devcenter.heroku.com/articles/python-support)

### Step 4: Update app.py for Heroku

**Important:** Your app must use the PORT environment variable:

```python
import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
```

### Step 5: Create .gitignore

```txt
# .gitignore
__pycache__/
*.pyc
.env
venv/
*.log
.DS_Store
```

---

## Deployment Steps

### Step 1: Initialize Git Repository

```bash
# Navigate to your project directory
cd your-ml-app

# Initialize Git
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit for deployment"
```

### Step 2: Create Heroku App

```bash
# Create app with random name
heroku create

# Or specify a name
heroku create your-app-name
```

**Output:**
```
Creating app... done, ⬢ your-app-name
https://your-app-name.herokuapp.com/ | https://git.heroku.com/your-app-name.git
```

### Step 3: Configure Environment Variables (if needed)

```bash
# Set environment variables
heroku config:set VARIABLE_NAME=value

# Example
heroku config:set MODEL_PATH=model.pkl
```

### Step 4: Deploy to Heroku

```bash
git push heroku main
```

**Or if your branch is called master:**
```bash
git push heroku master
```

**Deployment Output:**
```
remote: Compressing source files... done.
remote: Building source:
remote: -----> Building on the Heroku-20 stack
remote: -----> Using buildpack: heroku/python
remote: -----> Python app detected
remote: -----> Installing python-3.10.12
remote: -----> Installing pip dependencies
remote: -----> Discovering process types
remote:        Procfile declares types -> web
remote: -----> Compressing...
remote: -----> Launching...
remote: https://your-app-name.herokuapp.com/ deployed to Heroku
```

### Step 5: Open Your App

```bash
heroku open
```

This opens your app in a browser!

---

## Testing Your Deployment

### Method 1: Browser

Navigate to: `https://your-app-name.herokuapp.com/`

### Method 2: curl

```bash
# Health check
curl https://your-app-name.herokuapp.com/health

# Make prediction
curl -X POST https://your-app-name.herokuapp.com/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "Free money now!"}'
```

### Method 3: Python

```python
import requests

url = 'https://your-app-name.herokuapp.com/predict'
data = {'text': 'Test message'}

response = requests.post(url, json=data)
print(response.json())
```

### Method 4: Postman

1. Open Postman
2. Create new POST request
3. URL: `https://your-app-name.herokuapp.com/predict`
4. Headers: `Content-Type: application/json`
5. Body: Raw JSON
6. Send request

---

## Checking Logs

### View Real-time Logs

```bash
heroku logs --tail
```

**Press Ctrl+C to stop**

### View Recent Logs

```bash
heroku logs --num 100
```

### Search Logs

```bash
heroku logs --tail | grep ERROR
```

---

## Common Issues & Solutions

### Issue 1: Application Error (H10)

**Error:**
```
Application error: H10 (App crashed)
```

**Solutions:**

1. **Check logs:**
```bash
heroku logs --tail
```

2. **Common causes:**
   - Missing dependencies in requirements.txt
   - Syntax error in code
   - Model file too large (>500MB)
   - Incorrect Procfile

3. **Fix:**
   - Add missing packages to requirements.txt
   - Test locally: `python app.py`
   - Compress or simplify model

### Issue 2: Module Not Found

**Error:**
```
ModuleNotFoundError: No module named 'xxx'
```

**Solution:**
```bash
# Add to requirements.txt
echo "missing-package==version" >> requirements.txt

# Commit and redeploy
git add requirements.txt
git commit -m "Add missing dependency"
git push heroku main
```

### Issue 3: Model File Too Large

**Error:**
```
Compiled slug size: 550MB is too large (max is 500MB)
```

**Solutions:**

1. **Compress model:**
```python
import joblib
joblib.dump(model, 'model.pkl', compress=3)  # Compression level 0-9
```

2. **Use external storage:**
   - Store model on AWS S3
   - Load model from URL at startup

3. **Simplify model:**
   - Use fewer features
   - Smaller architecture

### Issue 4: Port Binding Failure

**Error:**
```
Error R10 (Boot timeout) -> Web process failed to bind to $PORT
```

**Solution:**

Ensure your app uses Heroku's PORT:

```python
import os
port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port)
```

### Issue 5: Timeout

**Error:**
```
Request timeout
```

**Solutions:**

1. **Optimize model loading:**
```python
# Load model once at startup
model = joblib.load('model.pkl')

# NOT in predict function!
```

2. **Reduce prediction time:**
   - Simplify preprocessing
   - Use faster model
   - Cache frequent predictions

### Issue 6: CORS Errors

**Error:**
```
Access to fetch at '...' from origin '...' has been blocked by CORS policy
```

**Solution:**

Add CORS to your Flask app:

```python
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
```

Add to requirements.txt:
```
flask-cors==4.0.0
```

---

## Updating Your App

### Method 1: Git Push

```bash
# Make changes to your code
# ...

# Add and commit
git add .
git commit -m "Update model"

# Push to Heroku
git push heroku main
```

### Method 2: Heroku CLI

```bash
# Restart app
heroku restart

# Scale dynos
heroku ps:scale web=1

# Check status
heroku ps
```

---

## Monitoring & Maintenance

### Check App Status

```bash
heroku ps
```

**Output:**
```
=== web (Free): gunicorn app:app (1)
web.1: up 2023/01/15 10:30:00 +0000 (~ 2h ago)
```

### View Metrics

```bash
heroku metrics
```

### Set Up Alerts

1. Go to Heroku Dashboard
2. Select your app
3. Click "Configure Add-ons"
4. Add monitoring add-ons (some free options available)

---

## Cost Optimization

### Free Tier Limitations:

- **Dyno hours:** 550-1000 hours/month (free account)
- **Dyno sleeping:** Apps sleep after 30 minutes of inactivity
- **Slug size:** Max 500MB
- **Build time:** Max 15 minutes

### Tips to Stay Free:

1. **Use only when needed** - App will sleep when inactive
2. **Optimize slug size** - Remove unnecessary dependencies
3. **Single dyno** - Don't scale beyond 1 dyno
4. **Share apps** - Deploy multiple projects to same account

### When to Upgrade:

Upgrade to paid plan if you need:
- No sleeping (always-on)
- Custom domain
- More than 1 dyno
- SSL certificate
- Better performance

**Hobby Dyno:** $7/month
**Professional Dyno:** $25-50/month

---

## Best Practices

### ✅ DO:

- Keep requirements.txt minimal
- Use environment variables for secrets
- Add health check endpoint
- Implement proper logging
- Test locally before deploying
- Use .gitignore properly
- Document your API
- Monitor your logs
- Set up error tracking

### ❌ DON'T:

- Commit API keys to Git
- Use development server in production
- Ignore Heroku logs
- Deploy without testing
- Hard-code configuration
- Use debug=True in production
- Forget to update requirements.txt
- Store large files in Git

---

## Deployment Checklist

Before deploying, verify:

- [ ] Code works locally
- [ ] All dependencies in requirements.txt
- [ ] Procfile created correctly
- [ ] runtime.txt specifies Python version
- [ ] .gitignore includes sensitive files
- [ ] Environment variables configured
- [ ] Model file size < 500MB
- [ ] App uses $PORT environment variable
- [ ] CORS configured (if needed for web apps)
- [ ] Health check endpoint exists
- [ ] Error handling implemented
- [ ] Logging configured
- [ ] README updated with deployment URL
- [ ] Tested endpoints with curl/Postman

---

## Next Steps

After successful deployment:

1. **Share your URL** - Add to portfolio, resume, LinkedIn
2. **Monitor usage** - Check logs regularly
3. **Gather feedback** - Let others test your API
4. **Iterate** - Update and improve based on feedback
5. **Consider scaling** - Upgrade if needed

---

## Additional Resources

- **Heroku Dev Center:** https://devcenter.heroku.com/
- **Heroku Python Guide:** https://devcenter.heroku.com/articles/getting-started-with-python
- **Heroku CLI Reference:** https://devcenter.heroku.com/articles/heroku-cli-commands
- **Heroku Status:** https://status.heroku.com/

---

## Alternative Platforms

If Heroku doesn't fit your needs:

1. **Render** - Similar to Heroku, generous free tier
2. **Railway** - Modern platform, easy deployment
3. **AWS Elastic Beanstalk** - More complex, highly scalable
4. **Google Cloud Run** - Serverless, pay-per-use
5. **Azure App Service** - Microsoft's platform
6. **DigitalOcean App Platform** - Simple and affordable

---

**Last Updated:** 2026-01-06
**Guide Version:** 1.0
**Module:** 9 - Deployment & MLOps
