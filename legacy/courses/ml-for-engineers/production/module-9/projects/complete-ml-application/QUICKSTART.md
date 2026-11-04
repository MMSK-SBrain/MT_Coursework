# Quick Start Guide

Get the Sentiment Analysis application running in 5 minutes!

## 🚀 Fastest Path to Running

### Option 1: Docker Compose (Recommended)

**Requirements**: Docker installed

```bash
# 1. Navigate to project
cd complete-ml-application

# 2. Start all services
docker-compose -f deployment/docker-compose.yml up

# 3. Access applications
# Frontend: http://localhost:8501
# Backend: http://localhost:8000
# API Docs: http://localhost:8000/docs
```

**Done!** All services are running.

---

### Option 2: Manual Setup (Detailed)

**Requirements**: Python 3.11+

#### Backend First

```bash
# 1. Navigate to backend
cd backend

# 2. Create virtual environment
python -m venv venv

# 3. Activate virtual environment
# macOS/Linux:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run the API
uvicorn main:app --reload
```

✅ Backend running at http://localhost:8000

#### Frontend Second (New Terminal)

```bash
# 1. Navigate to frontend
cd frontend

# 2. Create virtual environment
python -m venv venv

# 3. Activate virtual environment
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate  # Windows

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run the UI
streamlit run app.py
```

✅ Frontend running at http://localhost:8501

---

## 🎯 First Steps

### 1. Check Backend is Running

Open browser: http://localhost:8000

You should see:
```json
{
  "message": "Sentiment Analysis API",
  "version": "1.0.0",
  "status": "operational"
}
```

### 2. Check API Documentation

Open browser: http://localhost:8000/docs

You should see interactive API documentation (Swagger UI).

### 3. Use the Frontend

Open browser: http://localhost:8501

You should see the Sentiment Analyzer interface.

---

## 🧪 Test It Out

### Test 1: Analyze Positive Text

1. Go to http://localhost:8501
2. Type: "This product is absolutely amazing! I love it!"
3. Click "Analyze Sentiment"
4. You should see: **POSITIVE** with high confidence

### Test 2: Analyze Negative Text

1. Type: "Terrible quality, complete waste of money"
2. Click "Analyze Sentiment"
3. You should see: **NEGATIVE** with high confidence

### Test 3: View Statistics

1. Click the "Statistics" tab
2. You should see your predictions counted
3. Charts showing sentiment distribution

---

## 🔧 Troubleshooting

### Backend Won't Start

**Error**: "Port 8000 is already in use"

**Solution**:
```bash
# Kill process on port 8000
lsof -ti:8000 | xargs kill -9  # macOS/Linux
# Then restart: uvicorn main:app --reload
```

### Frontend Can't Connect

**Error**: "API Disconnected" in sidebar

**Solutions**:
1. Verify backend is running at http://localhost:8000
2. Check `frontend/api_client.py` has correct URL
3. Restart frontend

### Module Not Found

**Error**: "ModuleNotFoundError: No module named 'fastapi'"

**Solution**:
```bash
# Make sure virtual environment is activated
source venv/bin/activate  # macOS/Linux
# Then reinstall:
pip install -r requirements.txt
```

### Virtual Environment Issues

**Problem**: Can't activate virtual environment

**Solution**:
```bash
# Delete and recreate
rm -rf venv
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## 📋 Next Steps

### After Getting It Running:

1. **Explore the UI**
   - Try different text examples
   - Upload a text file
   - View statistics and insights

2. **Test the API**
   - Visit http://localhost:8000/docs
   - Try the interactive API docs
   - Make API calls with curl

3. **Run Tests**
   ```bash
   pytest tests/ -v
   ```

4. **View Monitoring**
   ```bash
   cd monitoring
   streamlit run dashboard.py --server.port 8502
   # Access at http://localhost:8502
   ```

5. **Read Documentation**
   - [Backend README](backend/README.md)
   - [Frontend README](frontend/README.md)
   - [Main README](README.md)

---

## 🚢 Deploy to Production

### Backend to Heroku

```bash
cd backend
heroku create your-app-name
git push heroku main
```

See full guide: [deployment/heroku_backend.md](deployment/heroku_backend.md)

### Frontend to Streamlit Cloud

1. Push to GitHub
2. Go to https://share.streamlit.io
3. Connect repository
4. Deploy!

See full guide: [deployment/heroku_frontend.md](deployment/heroku_frontend.md)

---

## 💡 Tips

### Development Tips

1. **Use auto-reload**
   - Backend: `uvicorn main:app --reload`
   - Frontend: Streamlit auto-reloads on save

2. **Check logs**
   - Backend: Watch terminal for API logs
   - Frontend: Watch terminal for Streamlit logs

3. **Use API docs**
   - Faster to test at http://localhost:8000/docs
   - No need to use frontend for every test

### Testing Tips

1. **Use example texts**
   - Frontend has built-in examples
   - Quick way to test different sentiments

2. **Monitor statistics**
   - Watch statistics tab to verify logging
   - Check confidence distributions

3. **Test edge cases**
   - Very long text
   - Special characters
   - Empty inputs (should error)

---

## 📚 Learning Path

### Beginner
1. ✅ Get it running locally
2. ✅ Try analyzing different texts
3. ✅ Explore the statistics
4. ✅ Read the code comments

### Intermediate
1. ✅ Run the tests
2. ✅ Modify the UI styling
3. ✅ Add a new endpoint
4. ✅ Deploy to staging

### Advanced
1. ✅ Add a trained ML model
2. ✅ Implement caching
3. ✅ Add authentication
4. ✅ Scale for production

---

## 🎓 Course Context

This is the **capstone project for Module 9: Deployment & MLOps**.

**Skills Demonstrated**:
- ✅ REST API development (FastAPI)
- ✅ Frontend development (Streamlit)
- ✅ Model deployment
- ✅ Monitoring and logging
- ✅ Production deployment
- ✅ Testing and validation
- ✅ Documentation

**Perfect for**:
- Portfolio projects
- Job interviews
- Learning MLOps
- Understanding production ML

---

## ❓ Common Questions

**Q: Can I use a different ML model?**

A: Yes! The system uses a rule-based model by default, but you can easily integrate a trained scikit-learn model or even transformers. See `backend/ml_service.py`.

**Q: Is this production-ready?**

A: It demonstrates production concepts. For real production, add authentication, rate limiting, and more robust error handling.

**Q: Can I customize the UI?**

A: Absolutely! Edit `frontend/app.py`. Streamlit makes it easy to modify the interface.

**Q: How do I add more features?**

A: Add new endpoints in `backend/main.py`, update the frontend in `frontend/app.py`, and add tests in `tests/`.

**Q: Can I use this for my portfolio?**

A: Yes! That's exactly what it's designed for. Deploy it and add the URL to your resume.

---

## 🆘 Need Help?

### Check These First:
1. Is Python 3.11+ installed? `python --version`
2. Is virtual environment activated? Look for `(venv)` in terminal
3. Are dependencies installed? `pip list`
4. Is backend running? `curl http://localhost:8000/health`
5. Check logs in terminal for error messages

### Still Stuck?

1. Review the full [README.md](README.md)
2. Check component-specific READMEs
3. Review error messages carefully
4. Try restarting from scratch

---

## ✅ Quick Checklist

Before moving on, make sure:

- [ ] Backend runs without errors
- [ ] Frontend runs without errors
- [ ] Can analyze text and see results
- [ ] Statistics update correctly
- [ ] API docs accessible
- [ ] Tests pass
- [ ] Understanding the architecture

---

**Ready to build amazing ML applications!** 🚀

**Next**: Deploy to production and add to your portfolio!
