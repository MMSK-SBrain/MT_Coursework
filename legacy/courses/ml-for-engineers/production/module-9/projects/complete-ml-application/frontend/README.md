# Sentiment Analysis Frontend

Beautiful, interactive Streamlit interface for sentiment analysis. Provides real-time text analysis, statistics visualization, and insights dashboard.

## Features

- **Interactive UI**: User-friendly interface with multiple input methods
- **Real-time Analysis**: Instant sentiment predictions with confidence scores
- **Rich Visualizations**: Charts, gauges, and graphs powered by Plotly
- **Statistics Dashboard**: Track predictions and sentiment distributions
- **Insights & Analytics**: Trend analysis and key metrics
- **Multiple Input Methods**: Type, upload files, or try examples
- **Detailed Analysis**: Optional preprocessing details and scores
- **Responsive Design**: Works on desktop and mobile devices

## Screenshots

### Main Analysis Interface
- Clean, modern design with emoji indicators
- Confidence score gauge visualization
- Detailed analysis expansion panels
- Example text library

### Statistics Dashboard
- Total prediction counter
- Sentiment distribution pie charts and bar graphs
- Recent predictions table
- Percentage breakdowns

### Insights Tab
- Key insights summary
- Sentiment trends over time
- Confidence distribution histograms
- Dominant sentiment analysis

## Local Setup

### Prerequisites
- Python 3.8 or higher
- Backend API running (see backend/README.md)
- pip package manager

### Installation

1. **Navigate to frontend directory:**
```bash
cd frontend
```

2. **Create virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

### Configuration

Create a `.env` file (optional):
```env
SENTIMENT_API_URL=http://localhost:8000
```

Or configure directly in the Streamlit sidebar.

### Running Locally

**Start the Streamlit app:**
```bash
streamlit run app.py
```

**Custom port:**
```bash
streamlit run app.py --server.port 8501
```

**Access the app:**
- Open browser: http://localhost:8501

## Deployment to Streamlit Cloud

### Prerequisites
- GitHub account
- Streamlit Cloud account (free at share.streamlit.io)
- Backend API deployed and accessible

### Deployment Steps

1. **Push to GitHub:**
```bash
git add .
git commit -m "Add Streamlit frontend"
git push origin main
```

2. **Deploy on Streamlit Cloud:**
   - Go to https://share.streamlit.io/
   - Click "New app"
   - Select your repository
   - Set main file path: `frontend/app.py`
   - Click "Deploy"

3. **Configure Secrets:**
   - In Streamlit Cloud dashboard, go to App Settings
   - Add secrets in TOML format:
   ```toml
   SENTIMENT_API_URL = "https://your-api-url.herokuapp.com"
   ```

4. **Access your app:**
   - You'll get a public URL like: https://username-app-name.streamlit.app/

### Alternative: Deploy via CLI

```bash
# Install Streamlit Cloud CLI
pip install streamlit

# Deploy
streamlit cloud deploy app.py
```

## Usage Guide

### Analyzing Text

1. **Choose Input Method:**
   - **Type Text**: Enter or paste text directly
   - **Upload File**: Upload .txt files
   - **Try Examples**: Select from pre-loaded examples

2. **Configure Options:**
   - Toggle "Show detailed analysis" in sidebar
   - Adjust API URL if needed

3. **Analyze:**
   - Click "Analyze Sentiment" button
   - View results with confidence visualization
   - Explore detailed analysis if enabled

### Viewing Statistics

1. Navigate to "Statistics" tab
2. View total predictions and distribution
3. Explore recent predictions table
4. Click "Refresh Statistics" to update

### Insights & Analytics

1. Navigate to "Insights" tab
2. Review key insights summary
3. Explore sentiment trends
4. Analyze confidence distributions

## API Client

The `api_client.py` module handles all backend communication:

### Features
- Connection pooling for performance
- Automatic retries on failure
- Comprehensive error handling
- Timeout management
- Health checking
- Batch predictions

### Usage Example
```python
from api_client import SentimentAPIClient

# Initialize client
client = SentimentAPIClient("http://localhost:8000")

# Check health
health = client.check_health()

# Predict sentiment
result = client.predict_sentiment(
    "This is amazing!",
    include_details=True
)

# Get statistics
stats = client.get_statistics()
```

## Customization

### Changing Colors

Edit the CSS in `app.py`:
```python
st.markdown("""
    <style>
    .positive { color: #YOUR_COLOR; }
    .negative { color: #YOUR_COLOR; }
    .neutral { color: #YOUR_COLOR; }
    </style>
    """, unsafe_allow_html=True)
```

### Adding Features

The app is modular and easy to extend:
- Add new tabs in the main tabs section
- Create new visualization functions
- Extend the API client with new endpoints
- Add export functionality for results

### Custom Examples

Edit the examples dictionary in `app.py`:
```python
examples = {
    "Your Example Name": "Your example text here...",
    # Add more examples
}
```

## Troubleshooting

### Cannot Connect to API

**Problem**: "API Disconnected" in sidebar

**Solutions:**
1. Check if backend is running: `curl http://localhost:8000/health`
2. Verify API URL in sidebar settings
3. Check firewall/network settings
4. Review backend logs for errors

### Slow Performance

**Problem**: App is slow or unresponsive

**Solutions:**
1. Use caching for API client: `@st.cache_resource`
2. Limit recent predictions display
3. Optimize visualization rendering
4. Check backend response time

### Deployment Issues

**Problem**: App doesn't work on Streamlit Cloud

**Solutions:**
1. Verify requirements.txt has all dependencies
2. Check Python version compatibility
3. Ensure API URL is in secrets (not hardcoded)
4. Review deployment logs in Streamlit Cloud dashboard

## Performance Optimization

### Caching
The app uses Streamlit caching for:
- API client initialization
- Static content
- Configuration loading

### Best Practices
- Keep visualizations lightweight
- Limit historical data display
- Use pagination for large datasets
- Implement lazy loading for heavy components

## Architecture

```
frontend/
├── app.py              # Main Streamlit application
├── api_client.py       # Backend API client
├── requirements.txt    # Python dependencies
└── README.md          # This file

Key Components:
- Page Config: Layout and theme settings
- Sidebar: Configuration and status
- Main Tabs: Analyze, Statistics, Insights, Info
- API Integration: RESTful communication
- Visualizations: Plotly charts and graphs
```

## Features Breakdown

### Tab 1: Analyze
- Text input (type, upload, examples)
- Sentiment prediction display
- Confidence gauge visualization
- Detailed analysis expansion
- Metadata display

### Tab 2: Statistics
- Total predictions counter
- Sentiment distribution (pie & bar charts)
- Recent predictions table
- Refresh functionality

### Tab 3: Insights
- Key insights summary
- Dominant sentiment analysis
- Sentiment trends visualization
- Confidence distribution
- Diversity metrics

### Tab 4: Info
- How it works explanation
- Use cases
- Tips for best results
- Technical details
- Support information

## Advanced Features

### Batch Analysis
Process multiple texts at once (extend api_client.py):
```python
texts = ["text 1", "text 2", "text 3"]
results = client.batch_predict(texts)
```

### Export Results
Add CSV export functionality:
```python
import csv
df = pd.DataFrame(predictions)
csv = df.to_csv(index=False)
st.download_button("Download CSV", csv)
```

### Custom Themes
Create `.streamlit/config.toml`:
```toml
[theme]
primaryColor = "#1f77b4"
backgroundColor = "#ffffff"
secondaryBackgroundColor = "#f0f2f6"
textColor = "#262730"
font = "sans serif"
```

## Testing

### Manual Testing
1. Test all input methods
2. Verify API connectivity
3. Check statistics accuracy
4. Validate visualizations
5. Test error handling

### Automated Testing
```bash
# Install testing dependencies
pip install pytest streamlit-testing

# Run tests
pytest test_app.py
```

## Maintenance

### Regular Tasks
- Update dependencies: `pip install --upgrade -r requirements.txt`
- Monitor error logs
- Check API health regularly
- Update examples with relevant content
- Refresh visualizations

### Monitoring
- Track app usage via Streamlit Cloud analytics
- Monitor API response times
- Check error rates
- Review user feedback

## Support & Resources

**Streamlit Documentation:**
- https://docs.streamlit.io/

**Plotly Documentation:**
- https://plotly.com/python/

**API Client Documentation:**
- See backend/README.md for API details

**Community:**
- Streamlit Forum: https://discuss.streamlit.io/
- GitHub Issues: Report bugs and request features

## Future Enhancements

Potential features to add:
- [ ] User authentication
- [ ] Historical data persistence
- [ ] Export functionality (CSV, JSON)
- [ ] Sentiment heatmaps
- [ ] Multi-language support
- [ ] Real-time streaming analysis
- [ ] Comparison mode (compare multiple texts)
- [ ] Custom model upload
- [ ] API key management
- [ ] Advanced filtering and search

## License

This project is for educational purposes as part of the ML for Engineers course.

## Contributors

Built with passion for teaching production ML systems!
