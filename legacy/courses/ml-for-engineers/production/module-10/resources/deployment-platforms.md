# Deployment Platforms Guide

## Overview

This guide covers free and affordable deployment options for your ML projects.

---

## API Deployment

### 1. Heroku (Recommended for Beginners)

**Pros:**
- Easy Git-based deployment
- Free tier available
- Good documentation
- Supports Python Flask/FastAPI

**Cons:**
- Free tier sleeps after 30 min inactivity
- 512MB RAM limit on free tier
- Slow cold starts

**Free Tier:**
- 550-1000 dyno hours/month
- Custom domain support
- Automatic HTTPS

**Deployment Steps:**
```bash
# Install Heroku CLI
brew install heroku/brew/heroku

# Login
heroku login

# Create app
heroku create your-ml-api

# Deploy
git push heroku main

# View logs
heroku logs --tail
```

**Best for:** Simple APIs, prototypes, portfolio projects

---

### 2. Railway.app (Modern Alternative)

**Pros:**
- More generous free tier than Heroku
- Faster deployment
- Modern UI
- No sleep/cold starts

**Cons:**
- Newer platform
- Smaller community

**Free Tier:**
- $5 credit/month
- Enough for 1-2 small services

**Best for:** Modern deployment, active projects

---

### 3. Render

**Pros:**
- Free tier with no sleep
- Easy deployment
- Good performance
- Automatic HTTPS

**Cons:**
- Free tier limited to 750 hours/month
- Some restrictions

**Free Tier:**
- 750 hours/month
- 512MB RAM
- Custom domains

**Best for:** Always-on APIs, reliable deployment

---

### 4. AWS (Advanced)

**Pros:**
- Industry standard
- Highly scalable
- Many services (Lambda, EC2, Elastic Beanstalk)

**Cons:**
- Complex setup
- Can be expensive if not careful
- Steep learning curve

**Free Tier:**
- 12 months free tier
- Lambda: 1M requests/month free
- EC2: 750 hours/month free

**Best for:** Learning cloud skills, scalable production

---

### 5. Google Cloud Platform

**Pros:**
- $300 free credit for 90 days
- Good ML integration
- Cloud Run for containers

**Cons:**
- Complex pricing
- Requires credit card

**Free Tier:**
- $300 credit (90 days)
- Always-free tier for some services

**Best for:** Google ecosystem, containerized apps

---

## UI Deployment

### 1. Streamlit Cloud (Highly Recommended)

**Pros:**
- Purpose-built for Streamlit apps
- Extremely easy deployment
- Free for public repos
- Automatic updates from GitHub

**Cons:**
- Only for Streamlit apps
- Limited resources on free tier

**Free Tier:**
- Unlimited public apps
- 1GB RAM per app
- GitHub integration

**Deployment:**
1. Push to GitHub
2. Go to share.streamlit.io
3. Connect repo
4. Deploy!

**Best for:** Streamlit dashboards (perfect for capstone!)

---

### 2. Netlify (For Static Sites)

**Pros:**
- Free for static sites
- Fast CDN
- Continuous deployment
- Custom domains

**Cons:**
- Static sites only (HTML/CSS/JS)
- Can't run Python backend

**Free Tier:**
- Unlimited sites
- 100GB bandwidth/month
- Automatic HTTPS

**Best for:** React/Vue dashboards, portfolio sites

---

### 3. Vercel (For Next.js/React)

**Pros:**
- Optimized for React/Next.js
- Fast deployment
- Good performance
- Free tier generous

**Cons:**
- Better for JavaScript than Python

**Free Tier:**
- Unlimited deployments
- 100GB bandwidth

**Best for:** Modern JavaScript frontends

---

### 4. GitHub Pages (For Static Sites)

**Pros:**
- Completely free
- Built into GitHub
- Easy setup

**Cons:**
- Static sites only
- No backend

**Free Tier:**
- Unlimited static sites
- Custom domains

**Best for:** Documentation, portfolio sites

---

## Database Options (If Needed)

### 1. SQLite (Local File)

**Pros:**
- No setup required
- Works everywhere
- Perfect for small datasets

**Cons:**
- Not scalable
- Single file (large files problematic)

**Best for:** Small datasets, local development

---

### 2. PostgreSQL on Heroku

**Pros:**
- Free tier available
- Reliable
- Industry standard

**Cons:**
- 10,000 row limit on free tier

**Free Tier:**
- 10,000 rows
- 1GB storage

**Best for:** Relational data, small datasets

---

### 3. MongoDB Atlas

**Pros:**
- Free tier generous
- NoSQL flexibility
- Cloud-hosted

**Cons:**
- Learning curve if new to NoSQL

**Free Tier:**
- 512MB storage
- Shared cluster

**Best for:** JSON-like data, flexible schema

---

### 4. Supabase (PostgreSQL Alternative)

**Pros:**
- Modern interface
- Real-time capabilities
- Good free tier

**Cons:**
- Newer platform

**Free Tier:**
- 500MB database
- Unlimited API requests

**Best for:** Modern apps, real-time features

---

## Recommended Stacks for Capstone

### Stack 1: Simple & Fast ⚡
- **API:** Heroku
- **UI:** Streamlit Cloud
- **Database:** SQLite (in API)
- **Best for:** Most capstone projects

### Stack 2: Modern & Free 🚀
- **API:** Railway or Render
- **UI:** Streamlit Cloud
- **Database:** Supabase or MongoDB Atlas
- **Best for:** Active/always-on projects

### Stack 3: Production-Ready 💼
- **API:** AWS Lambda or GCP Cloud Run
- **UI:** Netlify (React) or Streamlit Cloud
- **Database:** PostgreSQL (managed)
- **Best for:** Resume-worthy, scalable projects

---

## Deployment Checklist

**Before deploying:**
- [ ] Test locally first
- [ ] requirements.txt up to date
- [ ] Environment variables configured
- [ ] .gitignore configured (no secrets!)
- [ ] Error handling implemented
- [ ] Health check endpoint added

**After deploying:**
- [ ] Test all endpoints
- [ ] Check logs for errors
- [ ] Test from different devices
- [ ] Monitor performance
- [ ] Document URLs in README

---

## Common Deployment Issues

### Issue: "Application Error" on Heroku
**Solution:**
- Check logs: `heroku logs --tail`
- Verify Procfile exists
- Check requirements.txt
- Ensure correct Python version in runtime.txt

### Issue: Streamlit app won't start
**Solution:**
- Check requirements.txt
- Verify main file path in Streamlit Cloud settings
- Check for hardcoded localhost URLs
- Review Streamlit logs

### Issue: API returns 500 errors
**Solution:**
- Add proper error handling
- Check model file paths
- Verify all dependencies installed
- Test locally first

### Issue: Large model files
**Solution:**
- Use .slugignore on Heroku
- Store models externally (S3, Google Cloud Storage)
- Compress models if possible
- Use lighter algorithms (MobileNet vs ResNet)

---

## Cost Management Tips

1. **Use free tiers first**
2. **Monitor usage** (set up billing alerts)
3. **Shut down unused resources**
4. **Use spot instances** (AWS) for dev/test
5. **Optimize model size** (smaller = cheaper)
6. **Cache predictions** when possible

---

## Platform Comparison Table

| Platform | Type | Free Tier | Ease of Use | Best For |
|----------|------|-----------|-------------|----------|
| Heroku | API | 550hrs/mo | ⭐⭐⭐⭐⭐ | Beginners |
| Railway | API | $5 credit/mo | ⭐⭐⭐⭐ | Modern apps |
| Render | API | 750hrs/mo | ⭐⭐⭐⭐ | Reliable APIs |
| Streamlit Cloud | UI | Unlimited | ⭐⭐⭐⭐⭐ | Streamlit apps |
| Netlify | UI | Unlimited | ⭐⭐⭐⭐ | Static sites |
| AWS | Both | Generous | ⭐⭐ | Learning cloud |

---

*Choose based on your project needs and comfort level!*
