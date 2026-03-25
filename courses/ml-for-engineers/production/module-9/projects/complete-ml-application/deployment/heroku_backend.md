# Heroku Backend Deployment Guide

Complete step-by-step guide for deploying the Sentiment Analysis API to Heroku.

## Prerequisites

Before you begin, ensure you have:

- [ ] Heroku account (free tier available at https://heroku.com)
- [ ] Git installed on your machine
- [ ] Heroku CLI installed (https://devcenter.heroku.com/articles/heroku-cli)
- [ ] Backend code tested locally

## Step 1: Install Heroku CLI

### macOS
```bash
brew tap heroku/brew && brew install heroku
```

### Windows
Download installer from: https://devcenter.heroku.com/articles/heroku-cli

### Linux
```bash
curl https://cli-assets.heroku.com/install.sh | sh
```

Verify installation:
```bash
heroku --version
```

## Step 2: Login to Heroku

```bash
heroku login
```

This will open a browser window for authentication.

## Step 3: Prepare Your Backend

### 3.1 Navigate to backend directory
```bash
cd backend
```

### 3.2 Verify required files exist

Ensure you have:
- [x] `main.py` - Main FastAPI application
- [x] `ml_service.py` - ML service module
- [x] `requirements.txt` - Dependencies
- [x] `Procfile` - Heroku process configuration

### 3.3 Verify Procfile content

Your `Procfile` should contain:
```
web: uvicorn main:app --host 0.0.0.0 --port $PORT
```

### 3.4 Initialize Git (if not already done)

```bash
git init
git add .
git commit -m "Initial commit for Heroku deployment"
```

## Step 4: Create Heroku App

### 4.1 Create the app
```bash
heroku create your-sentiment-api
```

Replace `your-sentiment-api` with your desired app name. The name must be unique across all Heroku apps.

**Note**: If you don't specify a name, Heroku will generate a random name.

### 4.2 Verify app creation
```bash
heroku apps:info
```

You should see your app details including the web URL.

## Step 5: Configure Environment Variables

Set any necessary environment variables:

```bash
heroku config:set MODEL_VERSION=1.0.0
heroku config:set LOG_LEVEL=INFO
heroku config:set PYTHONUNBUFFERED=1
```

View all config variables:
```bash
heroku config
```

## Step 6: Deploy to Heroku

### 6.1 Deploy via Git
```bash
git push heroku main
```

**Note**: If your branch is named `master`, use:
```bash
git push heroku master
```

### 6.2 Monitor deployment
The deployment process will:
1. Detect Python app
2. Install dependencies from requirements.txt
3. Build the app
4. Start the web process

Watch for "deployed to Heroku" message.

## Step 7: Scale the App

Ensure at least one web dyno is running:

```bash
heroku ps:scale web=1
```

Check dyno status:
```bash
heroku ps
```

## Step 8: Test the Deployed API

### 8.1 Get your app URL
```bash
heroku apps:info
```

Look for "Web URL" - it will be something like:
`https://your-sentiment-api.herokuapp.com`

### 8.2 Test health endpoint
```bash
curl https://your-sentiment-api.herokuapp.com/health
```

Expected response:
```json
{
  "status": "healthy",
  "model_loaded": true,
  "timestamp": "2024-01-15T10:30:00",
  "version": "1.0.0"
}
```

### 8.3 Test prediction endpoint
```bash
curl -X POST https://your-sentiment-api.herokuapp.com/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "This is amazing!", "include_details": false}'
```

Expected response:
```json
{
  "text": "This is amazing!",
  "sentiment": "positive",
  "confidence": 0.89,
  "timestamp": "2024-01-15T10:30:00",
  "model_version": "1.0.0"
}
```

### 8.4 Test API documentation
Open in browser:
```
https://your-sentiment-api.herokuapp.com/docs
```

You should see the interactive Swagger UI.

## Step 9: Monitor Logs

### View real-time logs
```bash
heroku logs --tail
```

### View recent logs
```bash
heroku logs --num 100
```

### Filter logs by process
```bash
heroku logs --ps web
```

## Step 10: Performance Optimization

### Enable automatic HTTPS redirect
Add to your `main.py`:
```python
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
app.add_middleware(HTTPSRedirectMiddleware)
```

### Add request ID tracking
```bash
heroku labs:enable http-request-id
```

### Configure timeouts
```bash
heroku config:set TIMEOUT=30
```

## Troubleshooting

### Issue: Application Error (H10)

**Symptom**: "Application error" when accessing app

**Solutions**:
1. Check logs: `heroku logs --tail`
2. Verify Procfile is correct
3. Ensure web dyno is running: `heroku ps:scale web=1`
4. Check for errors in application startup

### Issue: Module Not Found

**Symptom**: Import errors in logs

**Solutions**:
1. Verify all dependencies in `requirements.txt`
2. Check Python version compatibility
3. Redeploy: `git push heroku main --force`

### Issue: Port Binding Error

**Symptom**: R10 error (boot timeout)

**Solutions**:
1. Ensure using `$PORT` environment variable:
   ```python
   port = int(os.getenv("PORT", 8000))
   ```
2. Update Procfile to use `--port $PORT`

### Issue: Slow Cold Starts

**Symptom**: First request is very slow

**Solutions**:
1. Upgrade to paid dyno (no sleep)
2. Use Heroku Scheduler for keep-alive pings
3. Optimize model loading

### Issue: Memory Exceeded (R14)

**Symptom**: Memory quota exceeded errors

**Solutions**:
1. Use lighter model files
2. Optimize imports
3. Upgrade to larger dyno type
4. Monitor with: `heroku logs --ps web | grep R14`

## Maintenance Commands

### Restart the app
```bash
heroku restart
```

### Run one-off commands
```bash
heroku run python
```

### Open app in browser
```bash
heroku open
```

### View app metrics
```bash
heroku logs --tail | grep "dyno"
```

## Updating Your App

### 1. Make changes locally

### 2. Test changes
```bash
python -m uvicorn main:app --reload
```

### 3. Commit changes
```bash
git add .
git commit -m "Update: description of changes"
```

### 4. Deploy
```bash
git push heroku main
```

### 5. Verify deployment
```bash
heroku logs --tail
```

## Adding a Custom Domain (Optional)

### 1. Add domain to Heroku
```bash
heroku domains:add www.yourdomain.com
```

### 2. Get DNS target
```bash
heroku domains
```

### 3. Update DNS records
Add CNAME record pointing to the Heroku DNS target.

### 4. Enable Automated Certificate Management (ACM)
```bash
heroku certs:auto:enable
```

## Scaling Your App

### Horizontal Scaling (more dynos)
```bash
heroku ps:scale web=2
```

### Vertical Scaling (larger dyno)
```bash
heroku ps:type hobby  # Hobby dyno ($7/month)
heroku ps:type standard-1x  # Standard 1X ($25/month)
```

## Cost Optimization

### Free Tier Limits
- 550 free dyno hours/month
- Apps sleep after 30 minutes of inactivity
- Wake up on request (cold start ~10 seconds)

### Tips for Free Tier
1. Use for development/testing
2. Accept cold starts
3. Monitor dyno hours: `heroku ps -a your-app`

### Upgrading to Paid
Benefits:
- No sleep (always on)
- Better performance
- SSL certificates
- Metrics and monitoring

## Security Best Practices

### 1. Environment Variables
Never commit secrets. Use config vars:
```bash
heroku config:set SECRET_KEY=your-secret-key
```

### 2. HTTPS Only
Enable HTTPS redirect in your app.

### 3. Rate Limiting
Add rate limiting middleware to prevent abuse.

### 4. CORS Configuration
Configure CORS properly for production:
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://yourfrontend.com"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)
```

## Monitoring and Alerting

### Set up logging add-on
```bash
heroku addons:create papertrail
```

### Set up monitoring
```bash
heroku addons:create newrelic
```

### Configure alerts
```bash
heroku alerts:add high-memory-usage --app your-app
```

## Rollback Deployment

### View releases
```bash
heroku releases
```

### Rollback to previous version
```bash
heroku rollback v42
```

Replace `v42` with the version number you want to rollback to.

## CI/CD Integration

### GitHub Integration

1. Go to Heroku Dashboard
2. Select your app
3. Click "Deploy" tab
4. Connect to GitHub
5. Enable automatic deploys from main branch
6. Enable "Wait for CI to pass before deploy"

## Backup and Recovery

### Backup database (if using PostgreSQL)
```bash
heroku pg:backups:capture
```

### Download backup
```bash
heroku pg:backups:download
```

## Success Checklist

After deployment, verify:

- [ ] App is accessible at Heroku URL
- [ ] Health endpoint returns "healthy"
- [ ] Prediction endpoint works correctly
- [ ] API documentation is accessible
- [ ] Logs are clean (no errors)
- [ ] Environment variables are set
- [ ] CORS is configured correctly
- [ ] HTTPS is working

## Next Steps

1. **Connect Frontend**: Update frontend API URL to point to Heroku app
2. **Add Monitoring**: Set up application monitoring
3. **Enable Logging**: Configure structured logging
4. **Performance Testing**: Load test your API
5. **Documentation**: Update README with production URL

## Resources

- **Heroku Documentation**: https://devcenter.heroku.com/
- **Heroku Python Guide**: https://devcenter.heroku.com/articles/getting-started-with-python
- **FastAPI Deployment**: https://fastapi.tiangolo.com/deployment/
- **Heroku Status**: https://status.heroku.com/

## Support

If you encounter issues:
1. Check Heroku status page
2. Review logs: `heroku logs --tail`
3. Check Heroku documentation
4. Contact Heroku support (paid plans)

---

**Congratulations!** Your Sentiment Analysis API is now deployed to production! 🎉
