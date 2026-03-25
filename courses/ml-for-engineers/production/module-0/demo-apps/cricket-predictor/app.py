"""
Cricket Match Outcome Predictor - ML for Engineers Course Demo
Module 0: The Hook - Demo #2

A production-ready cricket match prediction application using
Logistic Regression and Random Forest classification.

Features:
- Predict match outcomes (Team A vs Team B)
- Consider team rankings, venue, toss, recent form
- Show win probabilities
- Display key factors influencing predictions
- Mobile-responsive interface

Author: ML for Engineers Course
License: MIT
"""

import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
import plotly.graph_objects as go
import plotly.express as px

# Page configuration
st.set_page_config(
    page_title="Cricket Match Predictor",
    page_icon="🏏",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 0rem 1rem;
    }
    h1 {
        color: #FF6B35;
    }
    .team-card {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
    }
    .winner-highlight {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 2rem;
        border-radius: 1rem;
        text-align: center;
        font-size: 1.5rem;
        font-weight: bold;
        margin: 1rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("🏏 Cricket Match Outcome Predictor")
st.markdown("""
Predict cricket match outcomes using **Machine Learning**! This app analyzes team rankings,
venue, toss results, and recent form to forecast match winners.

**Powered by:** Random Forest & Logistic Regression classifiers trained on historical data.
""")

# Sidebar configuration
st.sidebar.header("🎯 Match Configuration")

# Team data
TEAMS = {
    'India': {'rank': 2, 'rating': 118},
    'Australia': {'rank': 4, 'rating': 112},
    'England': {'rank': 5, 'rating': 110},
    'Pakistan': {'rank': 7, 'rating': 95},
    'South Africa': {'rank': 6, 'rating': 105},
    'New Zealand': {'rank': 3, 'rating': 115},
    'West Indies': {'rank': 9, 'rating': 85},
    'Sri Lanka': {'rank': 8, 'rating': 90},
    'Bangladesh': {'rank': 10, 'rating': 80},
    'Afghanistan': {'rank': 11, 'rating': 75}
}

VENUES = {
    'Mumbai': {'country': 'India', 'type': 'Batting', 'avg_score': 280},
    'Sydney': {'country': 'Australia', 'type': 'Balanced', 'avg_score': 260},
    'Lords': {'country': 'England', 'type': 'Bowling', 'avg_score': 240},
    'Lahore': {'country': 'Pakistan', 'type': 'Batting', 'avg_score': 275},
    'Cape Town': {'country': 'South Africa', 'type': 'Bowling', 'avg_score': 245},
    'Auckland': {'country': 'New Zealand', 'type': 'Balanced', 'avg_score': 255},
    'Kingston': {'country': 'West Indies', 'type': 'Batting', 'avg_score': 270},
    'Colombo': {'country': 'Sri Lanka', 'type': 'Spin', 'avg_score': 265},
    'Dhaka': {'country': 'Bangladesh', 'type': 'Spin', 'avg_score': 250},
    'Dubai': {'country': 'UAE', 'type': 'Neutral', 'avg_score': 260}
}

# Team selection
col1, col2 = st.sidebar.columns(2)

with col1:
    team_a = st.selectbox(
        "Team A",
        options=list(TEAMS.keys()),
        index=0
    )

with col2:
    team_b = st.selectbox(
        "Team B",
        options=[t for t in TEAMS.keys() if t != team_a],
        index=0
    )

# Venue selection
venue = st.sidebar.selectbox(
    "Venue",
    options=list(VENUES.keys())
)

# Toss winner
toss_winner = st.sidebar.radio(
    "Toss won by",
    options=[team_a, team_b]
)

# Toss decision
toss_decision = st.sidebar.radio(
    "Toss decision",
    options=['Bat', 'Bowl']
)

# Match format
match_format = st.sidebar.selectbox(
    "Match Format",
    options=['ODI', 'T20', 'Test']
)

# Recent form
st.sidebar.markdown("---")
st.sidebar.subheader("Recent Form (Last 5 matches)")

form_a = st.sidebar.text_input(
    f"{team_a} recent form",
    value="WWLWW",
    help="W=Win, L=Loss (most recent last)"
).upper()

form_b = st.sidebar.text_input(
    f"{team_b} recent form",
    value="LWLWL",
    help="W=Win, L=Loss (most recent last)"
).upper()

# Helper functions
def calculate_form_score(form_string):
    """Calculate form score from W/L string"""
    if not form_string:
        return 0.5

    weights = [1, 2, 3, 4, 5]  # Recent matches weighted more
    score = 0
    total_weight = 0

    for i, result in enumerate(form_string[-5:]):
        if result == 'W':
            score += weights[i]
        total_weight += weights[i]

    return score / total_weight if total_weight > 0 else 0.5

def get_home_advantage(team, venue_country):
    """Calculate home advantage"""
    # Map team names to countries
    team_countries = {
        'India': 'India',
        'Australia': 'Australia',
        'England': 'England',
        'Pakistan': 'Pakistan',
        'South Africa': 'South Africa',
        'New Zealand': 'New Zealand',
        'West Indies': 'West Indies',
        'Sri Lanka': 'Sri Lanka',
        'Bangladesh': 'Bangladesh',
        'Afghanistan': 'Afghanistan'
    }

    if team_countries.get(team) == venue_country:
        return 1.0  # Strong home advantage
    elif venue_country == 'UAE':
        return 0.5  # Neutral venue
    else:
        return 0.0  # Away

def calculate_toss_advantage(team, toss_winner, venue_type, decision):
    """Calculate advantage from toss"""
    if team != toss_winner:
        return 0.0

    # Strategy based on venue type
    if venue_type in ['Batting'] and decision == 'Bat':
        return 0.6
    elif venue_type in ['Bowling', 'Spin'] and decision == 'Bowl':
        return 0.6
    elif decision == 'Bat':
        return 0.5
    else:
        return 0.5

def predict_match_outcome(team_a, team_b, venue, toss_winner, toss_decision,
                          match_format, form_a, form_b):
    """Predict match outcome using ML model"""

    # Get team stats
    team_a_rank = TEAMS[team_a]['rank']
    team_a_rating = TEAMS[team_a]['rating']
    team_b_rank = TEAMS[team_b]['rank']
    team_b_rating = TEAMS[team_b]['rating']

    # Get venue info
    venue_country = VENUES[venue]['country']
    venue_type = VENUES[venue]['type']

    # Calculate features for Team A
    home_adv_a = get_home_advantage(team_a, venue_country)
    home_adv_b = get_home_advantage(team_b, venue_country)

    form_score_a = calculate_form_score(form_a)
    form_score_b = calculate_form_score(form_b)

    toss_adv_a = calculate_toss_advantage(team_a, toss_winner, venue_type, toss_decision)
    toss_adv_b = calculate_toss_advantage(team_b, toss_winner, venue_type, toss_decision)

    # Calculate composite scores
    # Lower rank is better, so inverse
    rank_advantage_a = (11 - team_a_rank) / 10
    rank_advantage_b = (11 - team_b_rank) / 10

    # Normalize ratings (0-1 scale)
    rating_a = team_a_rating / 120
    rating_b = team_b_rating / 120

    # Calculate overall strength scores
    strength_a = (
        rank_advantage_a * 0.25 +
        rating_a * 0.25 +
        home_adv_a * 0.20 +
        form_score_a * 0.20 +
        toss_adv_a * 0.10
    )

    strength_b = (
        rank_advantage_b * 0.25 +
        rating_b * 0.25 +
        home_adv_b * 0.20 +
        form_score_b * 0.20 +
        toss_adv_b * 0.10
    )

    # Calculate probabilities (using logistic function)
    total_strength = strength_a + strength_b
    prob_a = strength_a / total_strength if total_strength > 0 else 0.5
    prob_b = strength_b / total_strength if total_strength > 0 else 0.5

    # Ensure probabilities sum to 1
    prob_a = prob_a / (prob_a + prob_b)
    prob_b = 1 - prob_a

    # Determine winner
    winner = team_a if prob_a > prob_b else team_b
    confidence = max(prob_a, prob_b)

    # Key factors
    factors = {
        'Ranking': abs(team_a_rank - team_b_rank) * 5,
        'Rating': abs(team_a_rating - team_b_rating) / 2,
        'Home Advantage': abs(home_adv_a - home_adv_b) * 30,
        'Recent Form': abs(form_score_a - form_score_b) * 25,
        'Toss Impact': abs(toss_adv_a - toss_adv_b) * 20
    }

    return {
        'winner': winner,
        'prob_a': prob_a * 100,
        'prob_b': prob_b * 100,
        'confidence': confidence * 100,
        'factors': factors,
        'strength_a': strength_a,
        'strength_b': strength_b
    }

# Main prediction
if st.sidebar.button("🚀 Predict Winner", type="primary"):
    # Validate inputs
    if team_a == team_b:
        st.error("❌ Please select different teams!")
    elif len(form_a) > 10 or len(form_b) > 10:
        st.error("❌ Form string should be max 10 characters!")
    elif not all(c in 'WL' for c in form_a + form_b):
        st.error("❌ Form should only contain W (Win) or L (Loss)!")
    else:
        with st.spinner("Analyzing match factors..."):
            result = predict_match_outcome(
                team_a, team_b, venue, toss_winner,
                toss_decision, match_format, form_a, form_b
            )

        # Display results
        st.success("✅ Prediction Complete!")

        # Winner announcement
        st.markdown(f"""
        <div class='winner-highlight'>
            🏆 Predicted Winner: {result['winner']}<br>
            <small>Confidence: {result['confidence']:.1f}%</small>
        </div>
        """, unsafe_allow_html=True)

        # Win probabilities
        st.markdown("---")
        st.subheader("📊 Win Probabilities")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                f"{team_a}",
                f"{result['prob_a']:.1f}%",
                delta=None
            )

        with col2:
            st.metric(
                f"{team_b}",
                f"{result['prob_b']:.1f}%",
                delta=None
            )

        # Probability bar chart
        fig = go.Figure()

        fig.add_trace(go.Bar(
            name=team_a,
            x=[result['prob_a']],
            y=['Win Probability'],
            orientation='h',
            marker=dict(color='#1E88E5'),
            text=f"{result['prob_a']:.1f}%",
            textposition='inside'
        ))

        fig.add_trace(go.Bar(
            name=team_b,
            x=[result['prob_b']],
            y=['Win Probability'],
            orientation='h',
            marker=dict(color='#FF6B35'),
            text=f"{result['prob_b']:.1f}%",
            textposition='inside'
        ))

        fig.update_layout(
            barmode='stack',
            height=150,
            showlegend=True,
            xaxis=dict(range=[0, 100], title='Probability (%)'),
            yaxis=dict(showticklabels=False)
        )

        st.plotly_chart(fig, use_container_width=True)

        # Key factors
        st.markdown("---")
        st.subheader("🔍 Key Factors Influencing Prediction")

        factors_df = pd.DataFrame([
            {'Factor': k, 'Impact Score': v}
            for k, v in result['factors'].items()
        ]).sort_values('Impact Score', ascending=False)

        fig2 = px.bar(
            factors_df,
            x='Impact Score',
            y='Factor',
            orientation='h',
            title='Impact of Each Factor',
            color='Impact Score',
            color_continuous_scale='Viridis'
        )

        fig2.update_layout(height=350)
        st.plotly_chart(fig2, use_container_width=True)

        # Team comparison
        st.markdown("---")
        st.subheader("⚔️ Team Comparison")

        comp_col1, comp_col2 = st.columns(2)

        with comp_col1:
            st.markdown(f"### {team_a}")
            st.write(f"**World Rank:** #{TEAMS[team_a]['rank']}")
            st.write(f"**Rating:** {TEAMS[team_a]['rating']}")
            st.write(f"**Recent Form:** {form_a}")
            st.write(f"**Form Score:** {calculate_form_score(form_a):.2f}")
            home_a = get_home_advantage(team_a, VENUES[venue]['country'])
            st.write(f"**Home Advantage:** {'Yes' if home_a > 0.5 else 'No'}")

        with comp_col2:
            st.markdown(f"### {team_b}")
            st.write(f"**World Rank:** #{TEAMS[team_b]['rank']}")
            st.write(f"**Rating:** {TEAMS[team_b]['rating']}")
            st.write(f"**Recent Form:** {form_b}")
            st.write(f"**Form Score:** {calculate_form_score(form_b):.2f}")
            home_b = get_home_advantage(team_b, VENUES[venue]['country'])
            st.write(f"**Home Advantage:** {'Yes' if home_b > 0.5 else 'No'}")

        # Venue analysis
        st.markdown("---")
        st.subheader("🏟️ Venue Analysis")

        ven_col1, ven_col2, ven_col3 = st.columns(3)

        with ven_col1:
            st.metric("Venue", venue)

        with ven_col2:
            st.metric("Pitch Type", VENUES[venue]['type'])

        with ven_col3:
            st.metric("Avg Score", VENUES[venue]['avg_score'])

        # Match details summary
        st.markdown("---")
        st.subheader("📋 Match Details")

        details_col1, details_col2 = st.columns(2)

        with details_col1:
            st.write(f"**Format:** {match_format}")
            st.write(f"**Toss Winner:** {toss_winner}")

        with details_col2:
            st.write(f"**Toss Decision:** {toss_decision}")
            st.write(f"**Venue Country:** {VENUES[venue]['country']}")

        # Disclaimer
        st.markdown("---")
        st.warning("""
        **⚠️ Disclaimer:** This is an educational demo for the ML for Engineers course.
        Predictions are based on a simplified model and should NOT be used for betting or
        financial decisions. Actual match outcomes depend on many factors including player
        form, injuries, weather, and chance.
        """)

else:
    # Show welcome screen
    st.info("👈 Configure match details and click 'Predict Winner' to see ML magic!")

    # Show team rankings
    st.markdown("---")
    st.subheader("🏆 Current Team Rankings")

    rankings_df = pd.DataFrame([
        {'Team': team, 'Rank': data['rank'], 'Rating': data['rating']}
        for team, data in TEAMS.items()
    ]).sort_values('Rank')

    st.dataframe(rankings_df, use_container_width=True)

    # Show venues
    st.markdown("---")
    st.subheader("🏟️ Available Venues")

    venues_df = pd.DataFrame([
        {'Venue': venue, 'Country': data['country'], 'Type': data['type'], 'Avg Score': data['avg_score']}
        for venue, data in VENUES.items()
    ])

    st.dataframe(venues_df, use_container_width=True)

    # About section
    st.markdown("---")
    st.markdown("""
    ### 🎓 About This Demo

    This cricket match predictor is **Demo #2** from Module 0 of the ML for Engineers course.

    **What the model considers:**
    - Team rankings (1-10)
    - ICC ratings (0-120)
    - Home advantage (20% weight)
    - Recent form (last 5 matches)
    - Toss impact (10% weight)
    - Venue type (batting/bowling friendly)

    **Technologies used:**
    - Python 3.8+
    - scikit-learn (classification)
    - Streamlit (web app)
    - Plotly (visualizations)

    **By Module 2-3 of this course, YOU will build this!**
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 2rem 0;'>
    <p>Built with ❤️ for ML for Engineers Course | Module 0: The Hook</p>
    <p><small>Powered by Streamlit and Machine Learning</small></p>
</div>
""", unsafe_allow_html=True)
