"""
ML Model Monitoring Dashboard
A Streamlit-based dashboard for monitoring machine learning model performance in production.

Author: ML for Engineers Course
Date: 2024
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime, timedelta
import sqlite3
from scipy import stats
import json

# Page config
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
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
    }
    .alert-high {
        background-color: #ffebee;
        color: #c62828;
        padding: 10px;
        border-radius: 5px;
        border-left: 5px solid #c62828;
    }
    .alert-medium {
        background-color: #fff3e0;
        color: #ef6c00;
        padding: 10px;
        border-radius: 5px;
        border-left: 5px solid #ef6c00;
    }
    .status-healthy {
        color: #2e7d32;
        font-weight: bold;
    }
    .status-warning {
        color: #ef6c00;
        font-weight: bold;
    }
    .status-critical {
        color: #c62828;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)


class MonitoringDashboard:
    """Main dashboard class for ML monitoring."""

    def __init__(self, db_path='predictions.db'):
        self.db_path = db_path
        self.alerts = []

    def load_data(self, start_date=None, end_date=None, limit=None):
        """Load prediction data from database."""
        try:
            conn = sqlite3.connect(self.db_path)

            if start_date and end_date:
                query = """
                    SELECT * FROM predictions
                    WHERE timestamp BETWEEN ? AND ?
                    ORDER BY timestamp DESC
                """
                df = pd.read_sql_query(query, conn, params=(start_date, end_date))
            elif limit:
                query = f"SELECT * FROM predictions ORDER BY timestamp DESC LIMIT {limit}"
                df = pd.read_sql_query(query, conn)
            else:
                query = "SELECT * FROM predictions ORDER BY timestamp DESC"
                df = pd.read_sql_query(query, conn)

            conn.close()

            if len(df) > 0:
                df['timestamp'] = pd.to_datetime(df['timestamp'])
                df['date'] = df['timestamp'].dt.date
                df['hour'] = df['timestamp'].dt.hour

            return df
        except Exception as e:
            st.error(f"Error loading data: {e}")
            return pd.DataFrame()

    def calculate_metrics(self, df):
        """Calculate key monitoring metrics."""
        if len(df) == 0:
            return {}

        metrics = {
            'total_predictions': len(df),
            'date_range': (df['timestamp'].min(), df['timestamp'].max()),
            'avg_prediction': df['prediction'].mean(),
            'std_prediction': df['prediction'].std(),
            'avg_confidence': df['confidence'].mean() if 'confidence' in df.columns else None,
            'avg_response_time': df['response_time_ms'].mean() if 'response_time_ms' in df.columns else None,
            'p50_response_time': df['response_time_ms'].median() if 'response_time_ms' in df.columns else None,
            'p95_response_time': df['response_time_ms'].quantile(0.95) if 'response_time_ms' in df.columns else None,
            'p99_response_time': df['response_time_ms'].quantile(0.99) if 'response_time_ms' in df.columns else None,
            'predictions_per_day': len(df) / max((df['timestamp'].max() - df['timestamp'].min()).days, 1)
        }

        return metrics

    def check_alerts(self, df):
        """Check for various alert conditions."""
        alerts = []

        if len(df) == 0:
            return alerts

        # Check 1: Low confidence
        if 'confidence' in df.columns:
            avg_confidence = df['confidence'].mean()
            if avg_confidence < 0.7:
                alerts.append({
                    'severity': 'HIGH' if avg_confidence < 0.6 else 'MEDIUM',
                    'type': 'LOW_CONFIDENCE',
                    'message': f'Average confidence is low: {avg_confidence:.3f}',
                    'timestamp': datetime.now()
                })

        # Check 2: Response time
        if 'response_time_ms' in df.columns:
            p95_time = df['response_time_ms'].quantile(0.95)
            if p95_time > 1000:  # 1 second
                alerts.append({
                    'severity': 'HIGH' if p95_time > 2000 else 'MEDIUM',
                    'type': 'SLOW_RESPONSE',
                    'message': f'P95 response time is high: {p95_time:.0f}ms',
                    'timestamp': datetime.now()
                })

        # Check 3: Prediction drift (compare recent vs baseline)
        if len(df) > 100:
            # Last 20% vs first 20%
            cutoff = len(df) // 5
            baseline = df.iloc[-cutoff:]['prediction']
            recent = df.iloc[:cutoff]['prediction']

            drift_pct = abs(recent.mean() - baseline.mean()) / baseline.mean()
            if drift_pct > 0.15:
                alerts.append({
                    'severity': 'HIGH' if drift_pct > 0.25 else 'MEDIUM',
                    'type': 'PREDICTION_DRIFT',
                    'message': f'Prediction drift detected: {drift_pct*100:.1f}% change',
                    'timestamp': datetime.now()
                })

        # Check 4: Volume anomaly (last day vs average)
        if len(df) > 0:
            df_copy = df.copy()
            df_copy['date'] = pd.to_datetime(df_copy['timestamp']).dt.date
            daily_counts = df_copy.groupby('date').size()

            if len(daily_counts) > 1:
                last_day = daily_counts.iloc[-1]
                avg_day = daily_counts.iloc[:-1].mean()
                std_day = daily_counts.iloc[:-1].std()

                if std_day > 0:
                    z_score = abs(last_day - avg_day) / std_day
                    if z_score > 2:
                        alerts.append({
                            'severity': 'MEDIUM',
                            'type': 'VOLUME_ANOMALY',
                            'message': f'Unusual request volume: {last_day} vs avg {avg_day:.0f} (z={z_score:.1f})',
                            'timestamp': datetime.now()
                        })

        return alerts


def main():
    """Main dashboard function."""

    st.title("📊 ML Model Monitoring Dashboard")
    st.markdown("Real-time monitoring for production machine learning models")

    # Sidebar
    st.sidebar.header("⚙️ Settings")

    # Database path
    db_path = st.sidebar.text_input(
        "Database Path",
        value="predictions.db",
        help="Path to SQLite database containing predictions"
    )

    # Date range selector
    st.sidebar.subheader("Date Range")
    date_option = st.sidebar.radio(
        "Select range:",
        ["Last 24 hours", "Last 7 days", "Last 30 days", "Custom"]
    )

    if date_option == "Last 24 hours":
        start_date = datetime.now() - timedelta(days=1)
        end_date = datetime.now()
    elif date_option == "Last 7 days":
        start_date = datetime.now() - timedelta(days=7)
        end_date = datetime.now()
    elif date_option == "Last 30 days":
        start_date = datetime.now() - timedelta(days=30)
        end_date = datetime.now()
    else:
        col1, col2 = st.sidebar.columns(2)
        start_date = col1.date_input("Start", datetime.now() - timedelta(days=7))
        end_date = col2.date_input("End", datetime.now())
        start_date = datetime.combine(start_date, datetime.min.time())
        end_date = datetime.combine(end_date, datetime.max.time())

    # Auto-refresh
    auto_refresh = st.sidebar.checkbox("Auto-refresh (30s)", value=False)
    if auto_refresh:
        st.sidebar.info("Dashboard will refresh every 30 seconds")
        import time
        time.sleep(30)
        st.rerun()

    # Refresh button
    if st.sidebar.button("🔄 Refresh Now"):
        st.rerun()

    # Initialize dashboard
    dashboard = MonitoringDashboard(db_path)

    # Load data
    with st.spinner("Loading data..."):
        df = dashboard.load_data(
            start_date=start_date.isoformat(),
            end_date=end_date.isoformat()
        )

    if len(df) == 0:
        st.warning("No data found for the selected date range.")
        st.info("Make sure predictions are being logged to the database.")
        return

    # Calculate metrics
    metrics = dashboard.calculate_metrics(df)

    # Check alerts
    alerts = dashboard.check_alerts(df)

    # Display alerts
    if alerts:
        st.subheader("⚠️ Active Alerts")
        for alert in alerts:
            if alert['severity'] == 'HIGH':
                st.markdown(f"""
                    <div class="alert-high">
                        <strong>🚨 {alert['type']}</strong><br>
                        {alert['message']}
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                    <div class="alert-medium">
                        <strong>⚠️ {alert['type']}</strong><br>
                        {alert['message']}
                    </div>
                """, unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)
    else:
        st.success("✅ No alerts - All systems healthy!")

    st.divider()

    # Key metrics overview
    st.subheader("📈 Key Metrics")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Total Predictions",
            f"{metrics['total_predictions']:,}",
            help="Total number of predictions in selected range"
        )

    with col2:
        if metrics['avg_confidence']:
            confidence_status = "🟢" if metrics['avg_confidence'] >= 0.8 else "🟡" if metrics['avg_confidence'] >= 0.7 else "🔴"
            st.metric(
                "Avg Confidence",
                f"{confidence_status} {metrics['avg_confidence']:.3f}",
                help="Average model confidence score"
            )

    with col3:
        if metrics['avg_response_time']:
            time_status = "🟢" if metrics['p95_response_time'] < 500 else "🟡" if metrics['p95_response_time'] < 1000 else "🔴"
            st.metric(
                "P95 Response Time",
                f"{time_status} {metrics['p95_response_time']:.0f}ms",
                help="95th percentile response time"
            )

    with col4:
        st.metric(
            "Predictions/Day",
            f"{metrics['predictions_per_day']:.0f}",
            help="Average predictions per day"
        )

    st.divider()

    # Time series analysis
    st.subheader("📊 Time Series Analysis")

    # Predictions over time
    tab1, tab2, tab3 = st.tabs(["Volume", "Predictions", "Performance"])

    with tab1:
        st.markdown("### Request Volume Over Time")

        # Hourly counts
        hourly_counts = df.groupby(df['timestamp'].dt.floor('H')).size().reset_index()
        hourly_counts.columns = ['timestamp', 'count']

        fig = px.line(
            hourly_counts,
            x='timestamp',
            y='count',
            title='Predictions per Hour',
            labels={'count': 'Predictions', 'timestamp': 'Time'}
        )
        fig.update_traces(line_color='#1f77b4', line_width=2)
        fig.update_layout(hovermode='x unified')
        st.plotly_chart(fig, use_container_width=True)

        # Daily breakdown
        daily_counts = df.groupby('date').size().reset_index()
        daily_counts.columns = ['date', 'count']

        fig2 = px.bar(
            daily_counts,
            x='date',
            y='count',
            title='Predictions per Day',
            labels={'count': 'Predictions', 'date': 'Date'}
        )
        fig2.update_traces(marker_color='#2ca02c')
        st.plotly_chart(fig2, use_container_width=True)

    with tab2:
        st.markdown("### Prediction Distribution & Drift")

        # Prediction over time
        fig = px.scatter(
            df,
            x='timestamp',
            y='prediction',
            color='confidence' if 'confidence' in df.columns else None,
            title='Predictions Over Time',
            labels={'prediction': 'Predicted Value', 'timestamp': 'Time'},
            opacity=0.6
        )

        # Add rolling mean
        df_sorted = df.sort_values('timestamp')
        window_size = min(50, len(df) // 10)
        if window_size > 1:
            rolling_mean = df_sorted['prediction'].rolling(window=window_size, center=True).mean()
            fig.add_trace(
                go.Scatter(
                    x=df_sorted['timestamp'],
                    y=rolling_mean,
                    mode='lines',
                    name='Rolling Mean',
                    line=dict(color='red', width=3)
                )
            )

        st.plotly_chart(fig, use_container_width=True)

        # Distribution histogram
        col1, col2 = st.columns(2)

        with col1:
            fig = px.histogram(
                df,
                x='prediction',
                nbins=50,
                title='Prediction Distribution',
                labels={'prediction': 'Predicted Value'}
            )
            fig.add_vline(
                x=df['prediction'].mean(),
                line_dash="dash",
                line_color="red",
                annotation_text=f"Mean: {df['prediction'].mean():.2f}"
            )
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            if 'confidence' in df.columns:
                fig = px.histogram(
                    df,
                    x='confidence',
                    nbins=30,
                    title='Confidence Distribution',
                    labels={'confidence': 'Confidence Score'}
                )
                fig.add_vline(
                    x=df['confidence'].mean(),
                    line_dash="dash",
                    line_color="red",
                    annotation_text=f"Mean: {df['confidence'].mean():.3f}"
                )
                st.plotly_chart(fig, use_container_width=True)

    with tab3:
        st.markdown("### Response Time Analysis")

        if 'response_time_ms' in df.columns:
            # Response time over time
            fig = px.scatter(
                df,
                x='timestamp',
                y='response_time_ms',
                title='Response Time Over Time',
                labels={'response_time_ms': 'Response Time (ms)', 'timestamp': 'Time'},
                opacity=0.5
            )

            # Add P95 line
            p95 = df['response_time_ms'].quantile(0.95)
            fig.add_hline(
                y=p95,
                line_dash="dash",
                line_color="red",
                annotation_text=f"P95: {p95:.0f}ms"
            )

            st.plotly_chart(fig, use_container_width=True)

            # Response time distribution
            fig = px.histogram(
                df,
                x='response_time_ms',
                nbins=50,
                title='Response Time Distribution',
                labels={'response_time_ms': 'Response Time (ms)'}
            )
            st.plotly_chart(fig, use_container_width=True)

            # Percentiles
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("P50 (Median)", f"{metrics['p50_response_time']:.0f}ms")
            with col2:
                st.metric("P95", f"{metrics['p95_response_time']:.0f}ms")
            with col3:
                st.metric("P99", f"{metrics['p99_response_time']:.0f}ms")
        else:
            st.info("Response time data not available")

    st.divider()

    # Drift detection
    st.subheader("🔍 Drift Detection")

    if len(df) > 100:
        # Compare recent vs baseline
        cutoff = len(df) // 3
        df_sorted = df.sort_values('timestamp')
        baseline = df_sorted.iloc[:cutoff]
        recent = df_sorted.iloc[-cutoff:]

        # Statistical tests
        ks_stat, ks_pvalue = stats.ks_2samp(baseline['prediction'], recent['prediction'])
        t_stat, t_pvalue = stats.ttest_ind(baseline['prediction'], recent['prediction'])

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("**Statistical Tests**")
            st.write(f"KS Test p-value: {ks_pvalue:.4f}")
            st.write(f"T-Test p-value: {t_pvalue:.4f}")

            if ks_pvalue < 0.05:
                st.error("⚠️ Distribution shift detected (KS test)")
            else:
                st.success("✅ No significant distribution shift")

            if t_pvalue < 0.05:
                st.warning("⚠️ Mean has shifted significantly (T-test)")
            else:
                st.success("✅ Mean is stable")

        with col2:
            st.markdown("**Distribution Comparison**")
            st.write(f"Baseline mean: {baseline['prediction'].mean():.2f}")
            st.write(f"Recent mean: {recent['prediction'].mean():.2f}")
            st.write(f"Difference: {abs(recent['prediction'].mean() - baseline['prediction'].mean()):.2f} ({abs(recent['prediction'].mean() / baseline['prediction'].mean() - 1)*100:.1f}%)")

        # Visualization
        fig = go.Figure()
        fig.add_trace(go.Histogram(
            x=baseline['prediction'],
            name='Baseline',
            opacity=0.6,
            nbinsx=30
        ))
        fig.add_trace(go.Histogram(
            x=recent['prediction'],
            name='Recent',
            opacity=0.6,
            nbinsx=30
        ))
        fig.update_layout(
            title='Distribution Comparison: Baseline vs Recent',
            xaxis_title='Prediction Value',
            yaxis_title='Frequency',
            barmode='overlay'
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Need more data for drift detection (minimum 100 predictions)")

    st.divider()

    # Raw data
    with st.expander("📋 View Raw Data"):
        st.dataframe(
            df[['timestamp', 'model_version', 'prediction', 'confidence', 'response_time_ms']].head(100),
            use_container_width=True
        )

        # Download button
        csv = df.to_csv(index=False)
        st.download_button(
            label="Download Full Data as CSV",
            data=csv,
            file_name=f"predictions_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
            mime="text/csv"
        )

    # Footer
    st.divider()
    st.markdown(f"""
        <div style='text-align: center; color: #666; padding: 20px;'>
            Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} |
            Monitoring {metrics['total_predictions']:,} predictions from {metrics['date_range'][0].strftime('%Y-%m-%d')} to {metrics['date_range'][1].strftime('%Y-%m-%d')}
        </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
