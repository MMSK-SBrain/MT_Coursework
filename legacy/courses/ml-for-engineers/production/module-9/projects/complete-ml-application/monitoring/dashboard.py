"""
Monitoring Dashboard for Sentiment Analysis Application

Comprehensive monitoring dashboard for tracking predictions,
performance metrics, and system health.
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime, timedelta
import sys
import os
from pathlib import Path

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent.parent / 'frontend'))

from api_client import SentimentAPIClient
from logger import PredictionLogger
from metrics import MetricsCalculator

# Page Configuration
st.set_page_config(
    page_title="ML Monitoring Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin: 0.5rem 0;
    }
    .alert-critical {
        background-color: #dc3545;
        color: white;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
    .alert-warning {
        background-color: #ffc107;
        color: #333;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
    .alert-success {
        background-color: #28a745;
        color: white;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 1rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize components
@st.cache_resource
def init_components():
    """Initialize API client, logger, and metrics calculator"""
    api_client = SentimentAPIClient()
    logger = PredictionLogger()
    metrics = MetricsCalculator()
    return api_client, logger, metrics

api_client, logger, metrics = init_components()

# Header
st.markdown('<div class="main-header">📊 ML Monitoring Dashboard</div>', unsafe_allow_html=True)
st.markdown("**Real-time monitoring for Sentiment Analysis System**")
st.markdown("---")

# Sidebar Controls
with st.sidebar:
    st.header("⚙️ Dashboard Controls")

    # Refresh settings
    st.subheader("Refresh Settings")
    auto_refresh = st.checkbox("Auto-refresh", value=False)
    refresh_interval = st.slider("Refresh interval (seconds)", 5, 60, 10)

    if st.button("🔄 Refresh Now") or auto_refresh:
        st.rerun()

    st.divider()

    # Time range filter
    st.subheader("Time Range")
    time_range = st.selectbox(
        "Select range",
        ["Last Hour", "Last 24 Hours", "Last 7 Days", "Last 30 Days", "All Time"]
    )

    # Convert to hours
    time_range_map = {
        "Last Hour": 1,
        "Last 24 Hours": 24,
        "Last 7 Days": 168,
        "Last 30 Days": 720,
        "All Time": None
    }
    hours_back = time_range_map[time_range]

    st.divider()

    # Alert thresholds
    st.subheader("Alert Thresholds")
    confidence_threshold = st.slider("Min confidence", 0.0, 1.0, 0.5, 0.05)
    error_rate_threshold = st.slider("Max error rate (%)", 0, 100, 10)

    st.divider()

    # Export options
    st.subheader("Export")
    if st.button("📥 Export Logs"):
        logs_df = logger.get_all_logs()
        if not logs_df.empty:
            csv = logs_df.to_csv(index=False)
            st.download_button(
                "Download CSV",
                csv,
                "prediction_logs.csv",
                "text/csv"
            )
        else:
            st.warning("No logs to export")

# Get data
api_stats = api_client.get_statistics()
db_logs = logger.get_logs(hours_back=hours_back)

# System Status Section
st.header("🚦 System Status")

col1, col2, col3, col4 = st.columns(4)

# API Health
health = api_client.check_health()
with col1:
    if health and health.get('status') == 'healthy':
        st.success("✅ API Online")
    else:
        st.error("❌ API Offline")

# Model Status
with col2:
    if health and health.get('model_loaded'):
        st.success("✅ Model Loaded")
    else:
        st.error("❌ Model Not Loaded")

# Database Status
with col3:
    try:
        logger.get_logs(hours_back=1)
        st.success("✅ Database OK")
    except:
        st.error("❌ Database Error")

# Last Update
with col4:
    st.info(f"🕐 {datetime.now().strftime('%H:%M:%S')}")

st.markdown("---")

# Key Metrics
st.header("📈 Key Metrics")

if api_stats:
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.metric(
            "Total Predictions",
            api_stats.get('total_predictions', 0),
            delta=None
        )

    with col2:
        avg_confidence = 0
        if not db_logs.empty and 'confidence' in db_logs.columns:
            avg_confidence = db_logs['confidence'].mean()
        st.metric(
            "Avg Confidence",
            f"{avg_confidence:.1%}",
            delta=None
        )

    with col3:
        pos_pct = api_stats.get('positive_percentage', 0)
        st.metric(
            "Positive Rate",
            f"{pos_pct:.1f}%",
            delta=None
        )

    with col4:
        neg_pct = api_stats.get('negative_percentage', 0)
        st.metric(
            "Negative Rate",
            f"{neg_pct:.1f}%",
            delta=None
        )

    with col5:
        neu_pct = api_stats.get('neutral_percentage', 0)
        st.metric(
            "Neutral Rate",
            f"{neu_pct:.1f}%",
            delta=None
        )

st.markdown("---")

# Alerts Section
st.header("🚨 Alerts & Warnings")

alerts = []

# Check average confidence
if not db_logs.empty and 'confidence' in db_logs.columns:
    avg_conf = db_logs['confidence'].mean()
    if avg_conf < confidence_threshold:
        alerts.append({
            'type': 'warning',
            'message': f"Average confidence ({avg_conf:.1%}) below threshold ({confidence_threshold:.1%})"
        })

# Check for sentiment imbalance
if api_stats:
    total = api_stats.get('total_predictions', 0)
    if total > 10:
        pos_pct = api_stats.get('positive_percentage', 0)
        neg_pct = api_stats.get('negative_percentage', 0)

        if pos_pct > 80 or neg_pct > 80:
            alerts.append({
                'type': 'warning',
                'message': f"Sentiment imbalance detected: {max(pos_pct, neg_pct):.1f}% dominant"
            })

# Check recent activity
if not db_logs.empty and 'timestamp' in db_logs.columns:
    db_logs['timestamp'] = pd.to_datetime(db_logs['timestamp'])
    recent = db_logs[db_logs['timestamp'] > datetime.now() - timedelta(hours=1)]
    if len(recent) == 0:
        alerts.append({
            'type': 'warning',
            'message': "No predictions in the last hour"
        })

# Display alerts
if alerts:
    for alert in alerts:
        if alert['type'] == 'critical':
            st.markdown(f'<div class="alert-critical">🔴 CRITICAL: {alert["message"]}</div>', unsafe_allow_html=True)
        elif alert['type'] == 'warning':
            st.markdown(f'<div class="alert-warning">⚠️ WARNING: {alert["message"]}</div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="alert-success">✅ All systems operating normally</div>', unsafe_allow_html=True)

st.markdown("---")

# Visualizations
if not db_logs.empty:
    # Predictions Over Time
    st.header("📊 Predictions Over Time")

    if 'timestamp' in db_logs.columns:
        db_logs['timestamp'] = pd.to_datetime(db_logs['timestamp'])
        db_logs_sorted = db_logs.sort_values('timestamp')

        # Hourly aggregation
        hourly = db_logs_sorted.set_index('timestamp').resample('H').size().reset_index(name='count')

        fig = px.line(
            hourly,
            x='timestamp',
            y='count',
            title='Predictions per Hour',
            labels={'count': 'Number of Predictions', 'timestamp': 'Time'}
        )
        fig.update_traces(line_color='#667eea', line_width=3)
        fig.update_layout(height=400, hovermode='x unified')
        st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # Sentiment Distribution
    st.header("🎭 Sentiment Distribution")

    col1, col2 = st.columns(2)

    with col1:
        if 'sentiment' in db_logs.columns:
            sentiment_counts = db_logs['sentiment'].value_counts()

            fig = px.pie(
                values=sentiment_counts.values,
                names=sentiment_counts.index,
                title='Sentiment Distribution',
                color=sentiment_counts.index,
                color_discrete_map={
                    'positive': '#28a745',
                    'negative': '#dc3545',
                    'neutral': '#ffc107'
                }
            )
            fig.update_traces(textposition='inside', textinfo='percent+label')
            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True)

    with col2:
        if 'sentiment' in db_logs.columns:
            fig = px.bar(
                x=sentiment_counts.index,
                y=sentiment_counts.values,
                title='Sentiment Counts',
                labels={'x': 'Sentiment', 'y': 'Count'},
                color=sentiment_counts.index,
                color_discrete_map={
                    'positive': '#28a745',
                    'negative': '#dc3545',
                    'neutral': '#ffc107'
                }
            )
            fig.update_layout(height=400, showlegend=False)
            st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # Confidence Analysis
    st.header("🎯 Confidence Analysis")

    col1, col2 = st.columns(2)

    with col1:
        if 'confidence' in db_logs.columns:
            fig = px.histogram(
                db_logs,
                x='confidence',
                nbins=20,
                title='Confidence Score Distribution',
                labels={'confidence': 'Confidence Score', 'count': 'Frequency'}
            )
            fig.add_vline(
                x=confidence_threshold,
                line_dash="dash",
                line_color="red",
                annotation_text=f"Threshold: {confidence_threshold:.2f}"
            )
            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True)

    with col2:
        if 'confidence' in db_logs.columns and 'sentiment' in db_logs.columns:
            fig = px.box(
                db_logs,
                x='sentiment',
                y='confidence',
                title='Confidence by Sentiment',
                color='sentiment',
                color_discrete_map={
                    'positive': '#28a745',
                    'negative': '#dc3545',
                    'neutral': '#ffc107'
                }
            )
            fig.update_layout(height=400, showlegend=False)
            st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # Performance Metrics
    st.header("⚡ Performance Metrics")

    # Calculate metrics
    if 'confidence' in db_logs.columns and 'sentiment' in db_logs.columns:
        perf_metrics = metrics.calculate_performance_metrics(db_logs)

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                "High Confidence Predictions",
                f"{perf_metrics.get('high_confidence_rate', 0):.1%}",
                help="Predictions with confidence > 0.8"
            )

        with col2:
            st.metric(
                "Low Confidence Predictions",
                f"{perf_metrics.get('low_confidence_rate', 0):.1%}",
                help="Predictions with confidence < 0.5"
            )

        with col3:
            st.metric(
                "Prediction Diversity",
                f"{perf_metrics.get('diversity_score', 0):.2f}",
                help="Shannon entropy of sentiment distribution"
            )

        with col4:
            st.metric(
                "Predictions/Hour",
                f"{perf_metrics.get('predictions_per_hour', 0):.1f}",
                help="Average predictions per hour"
            )

    st.markdown("---")

    # Recent Predictions Table
    st.header("📝 Recent Predictions")

    # Display controls
    col1, col2 = st.columns([3, 1])
    with col1:
        num_recent = st.slider("Number of recent predictions", 5, 50, 20)
    with col2:
        filter_sentiment = st.selectbox(
            "Filter by sentiment",
            ["All", "positive", "negative", "neutral"]
        )

    # Filter and display
    display_df = db_logs.copy()

    if filter_sentiment != "All":
        display_df = display_df[display_df['sentiment'] == filter_sentiment]

    display_df = display_df.sort_values('timestamp', ascending=False).head(num_recent)

    # Format for display
    if not display_df.empty:
        display_cols = ['timestamp', 'text_preview', 'sentiment', 'confidence', 'model_version']
        available_cols = [col for col in display_cols if col in display_df.columns]

        st.dataframe(
            display_df[available_cols],
            use_container_width=True,
            hide_index=True
        )
    else:
        st.info("No predictions to display")

else:
    st.info("📊 No prediction data available yet. Start making predictions to see monitoring data!")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 1rem;">
    <strong>ML Monitoring Dashboard</strong> | Auto-refresh: {} | Last updated: {}
</div>
""".format(
    "Enabled" if auto_refresh else "Disabled",
    datetime.now().strftime("%Y-%m-%d %H:%M:%S")
), unsafe_allow_html=True)

# Auto-refresh logic
if auto_refresh:
    import time
    time.sleep(refresh_interval)
    st.rerun()
