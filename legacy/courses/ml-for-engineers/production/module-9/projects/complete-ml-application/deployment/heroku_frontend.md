# Streamlit Cloud Frontend Deployment Guide

Complete step-by-step guide for deploying the Sentiment Analysis UI to Streamlit Cloud.

## Prerequisites

Before you begin, ensure you have:

- [ ] GitHub account
- [ ] Streamlit Cloud account (free at https://share.streamlit.io)
- [ ] Backend API deployed and accessible
- [ ] Frontend code tested locally
- [ ] Repository pushed to GitHub

## Step 1: Prepare Your Repository

### 1.1 Repository Structure

Ensure your repository has this structure:
```
your-repo/
├── frontend/
│   ├── app.py
│   ├── api_client.py
│   ├── requirements.txt
│   └── README.md
├── backend/
│   └── ...
└── README.md
```

### 1.2 Verify requirements.txt

Your `frontend/requirements.txt` should include:
```
streamlit==1.29.0
requests==2.31.0
pandas==2.1.3
plotly==5.18.0
python-dotenv==1.0.0
```

### 1.3 Create .streamlit/config.toml (Optional)

For custom theming, create `frontend/.streamlit/config.toml`:

```toml
[theme]
primaryColor = "#1f77b4"
backgroundColor = "#ffffff"
secondaryBackgroundColor = "#f0f2f6"
textColor = "#262730"
font = "sans serif"

[server]
headless = true
port = 8501
enableCORS = false
enableXsrfProtection = true
```

## Step 2: Push to GitHub

### 2.1 Initialize Git (if not done)
```bash
git init
git add .
git commit -m "Initial commit"
```

### 2.2 Create GitHub repository

1. Go to https://github.com/new
2. Create a new repository (public or private)
3. Copy the repository URL

### 2.3 Push your code
```bash
git remote add origin https://github.com/yourusername/your-repo.git
git branch -M main
git push -u origin main
```

## Step 3: Sign Up for Streamlit Cloud

### 3.1 Create account
1. Go to https://share.streamlit.io
2. Sign up with your GitHub account
3. Authorize Streamlit to access your repositories

## Step 4: Deploy Your App

### 4.1 Create new app

1. Click "New app" button
2. Select your repository
3. Configure deployment settings:
   - **Branch**: main (or your default branch)
   - **Main file path**: `frontend/app.py`
   - **App URL**: Choose a custom subdomain (optional)

### 4.2 Example configuration
```
Repository: yourusername/sentiment-analysis
Branch: main
Main file path: frontend/app.py
App URL (optional): my-sentiment-analyzer
```

## Step 5: Configure Secrets

### 5.1 Add API URL secret

1. In Streamlit Cloud dashboard, go to your app
2. Click "Settings" (⋮ menu)
3. Select "Secrets"
4. Add your secrets in TOML format:

```toml
SENTIMENT_API_URL = "https://your-sentiment-api.herokuapp.com"
```

### 5.2 Update api_client.py to use secrets

Ensure your `api_client.py` reads from Streamlit secrets:

```python
import os
import streamlit as st

# Try Streamlit secrets first, then environment variable
try:
    base_url = st.secrets.get("SENTIMENT_API_URL", "http://localhost:8000")
except:
    base_url = os.getenv('SENTIMENT_API_URL', 'http://localhost:8000')
```

Or update your `app.py`:
```python
import streamlit as st
from api_client import SentimentAPIClient

# Get API URL from secrets
api_url = st.secrets.get("SENTIMENT_API_URL", "http://localhost:8000")
api_client = SentimentAPIClient(base_url=api_url)
```

## Step 6: Deploy!

### 6.1 Click "Deploy"

Streamlit Cloud will:
1. Clone your repository
2. Install dependencies from requirements.txt
3. Run your app
4. Provide a public URL

### 6.2 Monitor deployment

Watch the deployment logs in real-time. Look for:
- ✅ Dependencies installed
- ✅ App started
- ✅ Public URL generated

## Step 7: Test Your Deployed App

### 7.1 Access your app

Your app will be available at:
```
https://yourusername-your-repo-frontend-app-hash.streamlit.app
```

Or your custom URL:
```
https://my-sentiment-analyzer.streamlit.app
```

### 7.2 Test functionality

1. **API Connection**: Check sidebar for "API Connected" status
2. **Analyze Text**: Try analyzing sample text
3. **Statistics**: View prediction statistics
4. **Insights**: Check insights dashboard
5. **Navigation**: Test all tabs

## Step 8: Configure Advanced Settings

### 8.1 Python version

Create `frontend/.python-version` file:
```
3.11
```

Or specify in `.streamlit/config.toml`:
```toml
[server]
pythonVersion = "3.11"
```

### 8.2 Custom domain (paid plan)

1. Go to app settings
2. Add custom domain
3. Configure DNS records
4. Enable HTTPS

## Automatic Redeployment

### Push to GitHub to redeploy

Every time you push to your repository, Streamlit Cloud will:
1. Detect the change
2. Automatically redeploy
3. Maintain zero downtime

```bash
# Make changes
git add .
git commit -m "Update UI"
git push origin main
```

## Troubleshooting

### Issue: ModuleNotFoundError

**Symptom**: Missing module errors

**Solutions**:
1. Add module to `requirements.txt`
2. Commit and push changes
3. Streamlit will auto-redeploy

### Issue: API Connection Failed

**Symptom**: "API Disconnected" in sidebar

**Solutions**:
1. Verify backend URL in secrets
2. Check backend is running: `curl https://your-api.herokuapp.com/health`
3. Verify CORS settings in backend allow Streamlit domain
4. Check secrets spelling (case-sensitive)

### Issue: Secrets Not Loading

**Symptom**: Default localhost URL being used

**Solutions**:
1. Check secrets syntax in TOML format
2. Ensure no extra quotes or spaces
3. Restart app after adding secrets
4. Use `st.secrets["KEY"]` syntax

### Issue: App Crashes on Startup

**Symptom**: Red error screen

**Solutions**:
1. Check deployment logs
2. Verify all imports in requirements.txt
3. Check Python version compatibility
4. Test locally first

### Issue: Slow Performance

**Symptom**: App is slow or unresponsive

**Solutions**:
1. Add `@st.cache_resource` to expensive operations
2. Optimize data loading
3. Reduce chart complexity
4. Limit historical data display

## Monitoring Your App

### View Analytics

1. Go to Streamlit Cloud dashboard
2. Select your app
3. Click "Analytics"

Metrics available:
- App views
- Unique visitors
- Session duration
- Error rate

### View Logs

1. Go to app dashboard
2. Click "Manage app"
3. Select "Logs"

View:
- Application logs
- Error messages
- Print statements

## App Management

### Restart App
```
Dashboard → Manage app → Reboot
```

### Delete App
```
Dashboard → Settings → Delete app
```

### Change App Settings
```
Dashboard → Settings → Edit
```

## Optimizing for Production

### 1. Add Loading States

```python
with st.spinner("Analyzing sentiment..."):
    result = api_client.predict_sentiment(text)
```

### 2. Error Handling

```python
try:
    result = api_client.predict_sentiment(text)
    if result:
        st.success("Analysis complete!")
    else:
        st.error("Failed to analyze. Please try again.")
except Exception as e:
    st.error(f"Error: {str(e)}")
```

### 3. Caching

```python
@st.cache_resource
def get_api_client():
    return SentimentAPIClient()

@st.cache_data(ttl=300)  # Cache for 5 minutes
def get_statistics():
    return api_client.get_statistics()
```

### 4. Session State

```python
if 'predictions' not in st.session_state:
    st.session_state.predictions = []

# Add prediction to session
st.session_state.predictions.append(result)
```

## Sharing Your App

### Public URL
Your app is automatically public at:
```
https://your-app.streamlit.app
```

### Share Link
Share the URL on:
- LinkedIn
- Twitter
- Portfolio website
- Resume
- GitHub README

### Embed in Website
```html
<iframe
  src="https://your-app.streamlit.app/?embed=true"
  height="600"
  width="100%"
></iframe>
```

## Security Considerations

### 1. API Keys in Secrets
Never expose API keys in code. Always use secrets:
```toml
# .streamlit/secrets.toml (local)
API_KEY = "your-secret-key"
```

### 2. Input Validation
Validate all user inputs:
```python
if len(text) > 5000:
    st.error("Text too long (max 5000 characters)")
    return
```

### 3. Rate Limiting
Consider implementing rate limiting for public apps.

### 4. Authentication
For private apps, use Streamlit's authentication (paid plan).

## CI/CD Integration

### GitHub Actions Workflow

Create `.github/workflows/streamlit.yml`:

```yaml
name: Streamlit App CI

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.11
    - name: Install dependencies
      run: |
        cd frontend
        pip install -r requirements.txt
    - name: Test imports
      run: |
        cd frontend
        python -c "import streamlit; import plotly; import pandas"
```

## Cost and Limits

### Free Tier
- Unlimited public apps
- 1 GB RAM per app
- Community Cloud resources
- Public repository required (or 1 private)

### Paid Tiers
- **Starter** ($20/month): Private apps, more resources
- **Team** ($250/month): Team collaboration, priority support
- **Enterprise**: Custom pricing, dedicated resources

## Best Practices

### 1. Repository Organization
```
repo/
├── frontend/              # Streamlit app
│   ├── app.py
│   ├── requirements.txt
│   └── .streamlit/
│       └── config.toml
├── backend/              # API code
├── tests/               # Tests
└── README.md            # Documentation
```

### 2. Version Pinning
Always pin versions in requirements.txt:
```
streamlit==1.29.0  # Not streamlit>=1.29.0
```

### 3. Secrets Management
- Use secrets for all sensitive data
- Never commit secrets to Git
- Use different secrets for dev/prod

### 4. Performance
- Cache expensive operations
- Lazy load data
- Optimize chart rendering
- Use session state wisely

## Success Checklist

After deployment, verify:

- [ ] App is accessible at public URL
- [ ] API connection works
- [ ] All tabs/features functional
- [ ] Charts and visualizations render
- [ ] Secrets configured correctly
- [ ] No errors in logs
- [ ] Mobile responsive
- [ ] Performance acceptable
- [ ] Shared on portfolio/LinkedIn

## Updating Your App

### Method 1: Git Push (Recommended)
```bash
git add .
git commit -m "Update feature"
git push origin main
```
Streamlit auto-deploys!

### Method 2: Direct Edit
1. Edit file on GitHub
2. Commit changes
3. Streamlit auto-deploys

### Method 3: Reboot
1. Go to app dashboard
2. Click "Reboot"
3. Fresh deployment

## Analytics and Insights

Track:
- Daily active users
- Session duration
- Feature usage
- Error rates
- Geographic distribution

## Support Resources

- **Streamlit Docs**: https://docs.streamlit.io
- **Community Forum**: https://discuss.streamlit.io
- **Gallery**: https://streamlit.io/gallery
- **Blog**: https://blog.streamlit.io
- **GitHub**: https://github.com/streamlit/streamlit

## Advanced Features

### 1. Multi-page Apps
Create `frontend/pages/` directory:
```
frontend/
├── app.py
└── pages/
    ├── 1_📊_Analytics.py
    └── 2_⚙️_Settings.py
```

### 2. File Downloads
```python
import pandas as pd

df = pd.DataFrame(data)
csv = df.to_csv(index=False)
st.download_button(
    "Download CSV",
    csv,
    "data.csv",
    "text/csv"
)
```

### 3. Custom Components
Install custom components:
```
streamlit-aggrid
streamlit-plotly-events
streamlit-elements
```

## Next Steps

1. **Monitor Usage**: Check analytics regularly
2. **Gather Feedback**: Share with users and iterate
3. **Add Features**: Enhance based on feedback
4. **Optimize Performance**: Profile and improve
5. **Documentation**: Keep README updated
6. **Portfolio**: Add to portfolio website

## Demo Video Script

Record a 2-3 minute demo:

1. **Introduction** (15s)
   - "This is my Sentiment Analyzer..."
   - Show the URL

2. **Demo Features** (90s)
   - Analyze sample text
   - Show confidence visualization
   - Navigate to statistics
   - Explore insights

3. **Technical Stack** (30s)
   - Streamlit frontend
   - FastAPI backend
   - Deployed on Streamlit Cloud & Heroku

4. **Conclusion** (15s)
   - GitHub link
   - Call to action

---

**Congratulations!** Your Sentiment Analysis UI is now live! 🚀

Share your app URL in your portfolio and on LinkedIn!
