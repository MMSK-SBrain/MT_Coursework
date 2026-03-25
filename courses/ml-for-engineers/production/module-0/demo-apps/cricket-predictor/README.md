# Cricket Match Outcome Predictor

## Overview

A production-ready cricket match prediction web application that forecasts match winners using Machine Learning. Demo #2 from Module 0 of the ML for Engineers course.

## Features

- **Match Outcome Prediction**: Predict winner between any two teams
- **10 International Teams**: India, Australia, England, Pakistan, SA, NZ, WI, SL, BD, AFG
- **10 Major Venues**: Including Mumbai, Sydney, Lords, Lahore, etc.
- **Smart Factors**:
  - Team rankings and ratings
  - Home advantage
  - Toss winner and decision
  - Recent form (last 5 matches)
  - Venue type (batting/bowling friendly)
- **Interactive Visualizations**: Probability charts, factor analysis
- **Responsive Design**: Works on all devices

## How It Works

The prediction model considers:

1. **Team Strength (50%)**:
   - World ranking (25%)
   - ICC rating (25%)

2. **Environmental Factors (20%)**:
   - Home advantage (20%)

3. **Recent Performance (20%)**:
   - Form in last 5 matches (20%)

4. **Match Conditions (10%)**:
   - Toss advantage (10%)

## Installation

### Local Setup

```bash
# Navigate to directory
cd cricket-predictor

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

App opens at `http://localhost:8501`

## Deployment

### Streamlit Cloud (Recommended - Free)

1. Push to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect repository
4. Deploy

### Heroku

```bash
# Create Procfile
echo "web: streamlit run app.py --server.port=$PORT" > Procfile

# Deploy
heroku create cricket-predictor-app
git push heroku main
```

## Usage Guide

1. **Select Teams**:
   - Choose Team A from dropdown
   - Choose Team B (different from Team A)

2. **Set Venue**:
   - Select match venue
   - Affects home advantage calculation

3. **Toss Details**:
   - Who won the toss
   - Bat or Bowl decision

4. **Recent Form**:
   - Enter last 5 matches (W=Win, L=Loss)
   - Example: WWLWW

5. **Predict**:
   - Click "Predict Winner"
   - View results in 2-3 seconds

## Sample Predictions

### Example 1: India vs Australia at Mumbai
```
Team A: India (Rank #2)
Team B: Australia (Rank #4)
Venue: Mumbai (India's home)
Toss: India won, chose to bat
Form: India (WWWWL), Australia (WLWLW)

Prediction: India wins (68% probability)
Key Factor: Home advantage
```

### Example 2: England vs Pakistan at Dubai
```
Team A: England (Rank #5)
Team B: Pakistan (Rank #7)
Venue: Dubai (Neutral)
Toss: Pakistan won, chose to bowl
Form: England (LWWLW), Pakistan (LLWWW)

Prediction: England wins (55% probability)
Key Factor: Better ranking
```

## Technical Details

### Algorithm
- **Type**: Classification (Binary)
- **Method**: Composite scoring with weighted factors
- **Output**: Win probabilities for both teams

### Features
1. Team ranking difference
2. Team rating difference
3. Home advantage (binary + continuous)
4. Form score (weighted recent results)
5. Toss advantage (context-dependent)

### Tech Stack
- **Frontend**: Streamlit
- **Data Processing**: Pandas, NumPy
- **Visualization**: Plotly
- **Python**: 3.8+

## Testing

```bash
# Run locally
streamlit run app.py

# Test cases:
1. Same teams (should error)
2. Invalid form string (should error)
3. Home advantage (India at Mumbai)
4. Neutral venue (any team at Dubai)
5. Strong vs weak team (India vs Bangladesh)
6. Close match (India vs Australia)
```

## Expected Behavior

- **Load Time**: < 2 seconds
- **Prediction Time**: < 1 second
- **Accuracy**: Conceptual model (for educational purposes)
- **Mobile**: Fully responsive

## Customization

### Add More Teams

```python
TEAMS = {
    'India': {'rank': 2, 'rating': 118},
    'Your Team': {'rank': X, 'rating': Y},
    # Add more...
}
```

### Add More Venues

```python
VENUES = {
    'Mumbai': {'country': 'India', 'type': 'Batting', 'avg_score': 280},
    'Your Venue': {'country': 'Country', 'type': 'Type', 'avg_score': XXX},
    # Add more...
}
```

### Adjust Factor Weights

```python
# In predict_match_outcome function
strength_a = (
    rank_advantage_a * 0.25 +  # Change weights here
    rating_a * 0.25 +
    home_adv_a * 0.20 +
    form_score_a * 0.20 +
    toss_adv_a * 0.10
)
```

## AI Prompts Used

1. **Initial app structure**:
   ```
   Create a Streamlit app for cricket match prediction.
   Include team selection, venue, toss, and recent form.
   Use classification ML approach.
   ```

2. **Prediction logic**:
   ```
   Create a function to predict cricket match winner based on:
   - Team rankings
   - Home advantage
   - Toss winner
   - Recent form (W/L string)
   Calculate win probabilities.
   ```

3. **Visualizations**:
   ```
   Add Plotly charts showing:
   - Win probabilities (stacked bar)
   - Factor importance
   - Team comparison metrics
   ```

4. **Validation**:
   ```
   Add input validation for:
   - Same team selection
   - Invalid form strings
   - Edge cases
   ```

## Troubleshooting

### Issue: Teams not displaying
```python
# Check TEAMS dictionary is properly defined
print(TEAMS.keys())
```

### Issue: Prediction always 50-50
```python
# Verify factors are being calculated
print(f"Team A strength: {strength_a}")
print(f"Team B strength: {strength_b}")
```

### Issue: Deployment fails
```bash
# Check requirements.txt versions
pip list

# Update if needed
pip install --upgrade streamlit
```

## Data Sources

- **Team Rankings**: Based on ICC official rankings (simplified)
- **Team Ratings**: Based on ICC rating points (simplified)
- **Venues**: Real cricket stadiums with approximate characteristics
- **Model**: Educational/demonstration purposes

## Course Integration

- **Module 0 - Session 1**: Students see this demo
- **Module 2**: Students learn classification
- **Module 3**: Students can build similar sports predictors

## Future Enhancements

- [ ] Add player statistics
- [ ] Include weather conditions
- [ ] Historical match database
- [ ] More sophisticated ML model (trained on real data)
- [ ] Probability confidence intervals
- [ ] Match format-specific models

## License

MIT License - Free for educational use

## Credits

**Built for:** ML for Engineers Course
**Module:** 0 (The Hook)
**Demo:** #2 (Cricket Predictor)
**Date:** January 2026

---

**🎓 Want to build this yourself?**

Join the ML for Engineers course and learn to build cricket predictors,
stock forecasters, chatbots, and more!
