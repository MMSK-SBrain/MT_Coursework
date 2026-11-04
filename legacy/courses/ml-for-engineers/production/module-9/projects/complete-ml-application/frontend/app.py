"""
Streamlit Frontend for Sentiment Analysis Application

Beautiful, user-friendly interface for sentiment analysis with
real-time predictions, visualizations, and analytics.
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import time
from api_client import SentimentAPIClient

# Page Configuration
st.set_page_config(
    page_title="Sentiment Analyzer",
    page_icon="💭",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for beautiful styling
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
    }
    .positive {
        color: #28a745;
        font-weight: bold;
    }
    .negative {
        color: #dc3545;
        font-weight: bold;
    }
    .neutral {
        color: #ffc107;
        font-weight: bold;
    }
    .stButton>button {
        width: 100%;
        background-color: #1f77b4;
        color: white;
        font-weight: bold;
        padding: 0.5rem 1rem;
        border-radius: 0.5rem;
    }
    .footer {
        text-align: center;
        color: #666;
        margin-top: 3rem;
        padding: 1rem;
        border-top: 1px solid #ddd;
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize API client
@st.cache_resource
def get_api_client():
    """Initialize and cache API client"""
    return SentimentAPIClient()

api_client = get_api_client()

# Header
st.markdown('<div class="main-header">💭 Sentiment Analyzer</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Analyze the sentiment of any text with AI-powered analysis</div>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.header("⚙️ Settings")

    # API Status
    st.subheader("API Status")
    health = api_client.check_health()

    if health and health.get("status") == "healthy":
        st.success("✅ API Connected")
        st.info(f"🤖 Model Version: {health.get('version', 'Unknown')}")
    else:
        st.error("❌ API Disconnected")
        st.warning("Please check your API configuration")

    st.divider()

    # Configuration
    st.subheader("Configuration")
    api_url = st.text_input(
        "API URL",
        value=api_client.base_url,
        help="Enter the backend API URL"
    )

    if st.button("Update API URL"):
        api_client.base_url = api_url
        st.success("API URL updated!")
        st.rerun()

    st.divider()

    # Analysis Options
    st.subheader("Analysis Options")
    include_details = st.checkbox(
        "Show detailed analysis",
        value=False,
        help="Include preprocessing details and scores"
    )

    st.divider()

    # About
    st.subheader("About")
    st.info("""
    This sentiment analyzer uses machine learning to classify text as:
    - ✅ Positive
    - ❌ Negative
    - ⚖️ Neutral

    Perfect for analyzing:
    - Product reviews
    - Customer feedback
    - Social media posts
    - Survey responses
    """)

# Main Content
tab1, tab2, tab3, tab4 = st.tabs(["🔍 Analyze", "📊 Statistics", "📈 Insights", "ℹ️ Info"])

# Tab 1: Analyze
with tab1:
    st.header("Analyze Text Sentiment")

    # Input Methods
    input_method = st.radio(
        "Choose input method:",
        ["Type Text", "Upload File", "Try Examples"],
        horizontal=True
    )

    text_to_analyze = ""

    if input_method == "Type Text":
        text_to_analyze = st.text_area(
            "Enter text to analyze:",
            height=200,
            placeholder="Type or paste your text here...\n\nExample: This product exceeded my expectations! The quality is outstanding and delivery was fast.",
            help="Enter any text you want to analyze (up to 5000 characters)"
        )

    elif input_method == "Upload File":
        uploaded_file = st.file_uploader(
            "Upload a text file",
            type=['txt'],
            help="Upload a .txt file to analyze"
        )
        if uploaded_file:
            text_to_analyze = uploaded_file.read().decode('utf-8')
            st.text_area("File content:", text_to_analyze, height=200, disabled=True)

    else:  # Try Examples
        examples = {
            "Positive Review": "This product is absolutely amazing! I love everything about it. The quality is outstanding and it arrived faster than expected. Highly recommend!",
            "Negative Review": "Terrible experience. The product broke after one day and customer service was unhelpful. Complete waste of money. Very disappointed.",
            "Neutral Statement": "The package arrived on Tuesday. It contains the items I ordered. The color is blue as described in the listing.",
            "Mixed Sentiment": "The product quality is great and works as advertised, but the price is too high and shipping took forever.",
            "Short Positive": "Excellent! Love it!",
            "Short Negative": "Awful. Don't buy."
        }

        selected_example = st.selectbox("Select an example:", list(examples.keys()))
        text_to_analyze = examples[selected_example]
        st.text_area("Example text:", text_to_analyze, height=150, disabled=True)

    # Analyze Button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        analyze_button = st.button("🔍 Analyze Sentiment", use_container_width=True)

    # Perform Analysis
    if analyze_button:
        if not text_to_analyze or not text_to_analyze.strip():
            st.error("⚠️ Please enter some text to analyze")
        else:
            with st.spinner("Analyzing sentiment..."):
                result = api_client.predict_sentiment(text_to_analyze, include_details)

                if result:
                    # Display Results
                    st.success("✅ Analysis Complete!")

                    # Sentiment Result Card
                    sentiment = result.get('sentiment', 'unknown')
                    confidence = result.get('confidence', 0)

                    # Color coding
                    if sentiment == 'positive':
                        color = '#28a745'
                        emoji = '😊'
                        sentiment_class = 'positive'
                    elif sentiment == 'negative':
                        color = '#dc3545'
                        emoji = '😞'
                        sentiment_class = 'negative'
                    else:
                        color = '#ffc107'
                        emoji = '😐'
                        sentiment_class = 'neutral'

                    # Result Display
                    st.markdown("---")
                    col1, col2, col3 = st.columns([1, 2, 1])

                    with col2:
                        st.markdown(f"""
                        <div style="text-align: center; padding: 2rem; background-color: {color}15; border-radius: 1rem; border: 2px solid {color};">
                            <div style="font-size: 4rem;">{emoji}</div>
                            <div style="font-size: 2rem; font-weight: bold; color: {color}; margin: 1rem 0;">
                                {sentiment.upper()}
                            </div>
                            <div style="font-size: 1.5rem; color: #666;">
                                Confidence: {confidence:.1%}
                            </div>
                        </div>
                        """, unsafe_allow_html=True)

                    # Confidence Meter
                    st.markdown("### Confidence Score")
                    fig = go.Figure(go.Indicator(
                        mode="gauge+number",
                        value=confidence * 100,
                        domain={'x': [0, 1], 'y': [0, 1]},
                        title={'text': "Confidence", 'font': {'size': 20}},
                        number={'suffix': "%", 'font': {'size': 40}},
                        gauge={
                            'axis': {'range': [0, 100], 'tickwidth': 1},
                            'bar': {'color': color},
                            'bgcolor': "white",
                            'borderwidth': 2,
                            'bordercolor': "gray",
                            'steps': [
                                {'range': [0, 50], 'color': '#f8f9fa'},
                                {'range': [50, 75], 'color': '#e9ecef'},
                                {'range': [75, 100], 'color': '#dee2e6'}
                            ],
                            'threshold': {
                                'line': {'color': "red", 'width': 4},
                                'thickness': 0.75,
                                'value': 90
                            }
                        }
                    ))
                    fig.update_layout(height=300, margin=dict(l=20, r=20, t=50, b=20))
                    st.plotly_chart(fig, use_container_width=True)

                    # Details Section
                    if include_details and 'details' in result and result['details']:
                        st.markdown("---")
                        st.markdown("### 📋 Detailed Analysis")

                        details = result['details']

                        col1, col2, col3 = st.columns(3)

                        with col1:
                            st.metric("Text Length", f"{details.get('text_length', 0)} chars")
                            st.metric("Word Count", details.get('word_count', 0))

                        with col2:
                            st.metric("Analysis Method", details.get('method', 'unknown').replace('_', ' ').title())
                            if 'positive_score' in details:
                                st.metric("Positive Score", f"{details['positive_score']:.2f}")

                        with col3:
                            if 'negative_score' in details:
                                st.metric("Negative Score", f"{details['negative_score']:.2f}")

                        # Preprocessed Text
                        with st.expander("🔍 View Preprocessed Text"):
                            st.code(details.get('preprocessed_text', ''))

                    # Metadata
                    st.markdown("---")
                    with st.expander("📊 Analysis Metadata"):
                        col1, col2 = st.columns(2)
                        with col1:
                            st.write(f"**Timestamp:** {result.get('timestamp', 'N/A')}")
                            st.write(f"**Model Version:** {result.get('model_version', 'N/A')}")
                        with col2:
                            st.write(f"**API Status:** Connected")
                            st.write(f"**Response Time:** < 1s")

                else:
                    st.error("❌ Failed to analyze text. Please check API connection.")

# Tab 2: Statistics
with tab2:
    st.header("📊 Prediction Statistics")

    if st.button("🔄 Refresh Statistics"):
        st.rerun()

    stats = api_client.get_statistics()

    if stats:
        # Overview Metrics
        st.subheader("Overview")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                "Total Predictions",
                stats.get('total_predictions', 0),
                delta=None
            )

        with col2:
            st.metric(
                "Positive",
                stats.get('positive_count', 0),
                delta=f"{stats.get('positive_percentage', 0):.1f}%"
            )

        with col3:
            st.metric(
                "Negative",
                stats.get('negative_count', 0),
                delta=f"{stats.get('negative_percentage', 0):.1f}%"
            )

        with col4:
            st.metric(
                "Neutral",
                stats.get('neutral_count', 0),
                delta=f"{stats.get('neutral_percentage', 0):.1f}%"
            )

        # Distribution Chart
        if stats.get('total_predictions', 0) > 0:
            st.markdown("---")
            st.subheader("Sentiment Distribution")

            col1, col2 = st.columns(2)

            with col1:
                # Pie Chart
                fig = px.pie(
                    values=[
                        stats.get('positive_count', 0),
                        stats.get('negative_count', 0),
                        stats.get('neutral_count', 0)
                    ],
                    names=['Positive', 'Negative', 'Neutral'],
                    color=['Positive', 'Negative', 'Neutral'],
                    color_discrete_map={
                        'Positive': '#28a745',
                        'Negative': '#dc3545',
                        'Neutral': '#ffc107'
                    },
                    hole=0.4
                )
                fig.update_traces(textposition='inside', textinfo='percent+label')
                fig.update_layout(showlegend=True, height=400)
                st.plotly_chart(fig, use_container_width=True)

            with col2:
                # Bar Chart
                fig = px.bar(
                    x=['Positive', 'Negative', 'Neutral'],
                    y=[
                        stats.get('positive_count', 0),
                        stats.get('negative_count', 0),
                        stats.get('neutral_count', 0)
                    ],
                    color=['Positive', 'Negative', 'Neutral'],
                    color_discrete_map={
                        'Positive': '#28a745',
                        'Negative': '#dc3545',
                        'Neutral': '#ffc107'
                    },
                    labels={'x': 'Sentiment', 'y': 'Count'},
                    title='Prediction Counts by Sentiment'
                )
                fig.update_layout(showlegend=False, height=400)
                st.plotly_chart(fig, use_container_width=True)

        # Recent Predictions
        recent = stats.get('recent_predictions', [])
        if recent:
            st.markdown("---")
            st.subheader("Recent Predictions")

            # Convert to DataFrame
            df = pd.DataFrame(recent)

            # Display as table
            st.dataframe(
                df[['timestamp', 'text_preview', 'sentiment', 'confidence']],
                use_container_width=True,
                hide_index=True
            )

    else:
        st.warning("⚠️ No statistics available. Make some predictions first!")

# Tab 3: Insights
with tab3:
    st.header("📈 Insights & Analytics")

    stats = api_client.get_statistics()

    if stats and stats.get('total_predictions', 0) > 0:
        # Key Insights
        st.subheader("🔍 Key Insights")

        total = stats.get('total_predictions', 0)
        pos_pct = stats.get('positive_percentage', 0)
        neg_pct = stats.get('negative_percentage', 0)
        neu_pct = stats.get('neutral_percentage', 0)

        # Dominant Sentiment
        dominant = max(
            [('Positive', pos_pct), ('Negative', neg_pct), ('Neutral', neu_pct)],
            key=lambda x: x[1]
        )

        col1, col2 = st.columns(2)

        with col1:
            st.info(f"""
            **Dominant Sentiment:** {dominant[0]}

            {dominant[1]:.1f}% of all predictions are {dominant[0].lower()}.
            """)

            if pos_pct > 60:
                st.success("😊 Overall sentiment is very positive!")
            elif neg_pct > 60:
                st.error("😞 Overall sentiment is quite negative.")
            else:
                st.warning("😐 Sentiment is mixed or neutral.")

        with col2:
            st.metric("Sentiment Diversity", f"{100 - dominant[1]:.1f}%")
            st.caption("How varied are the predictions?")

            avg_confidence = sum(
                p.get('confidence', 0) for p in stats.get('recent_predictions', [])
            ) / max(len(stats.get('recent_predictions', [])), 1)

            st.metric("Average Confidence", f"{avg_confidence:.1%}")
            st.caption("How confident is the model?")

        # Trend Analysis (simulated)
        st.markdown("---")
        st.subheader("📊 Sentiment Trends")

        # Create sample trend data
        recent_preds = stats.get('recent_predictions', [])
        if len(recent_preds) >= 5:
            # Show last 20 predictions trend
            trend_data = recent_preds[-20:]
            trend_df = pd.DataFrame(trend_data)

            # Sentiment over time
            sentiment_map = {'positive': 1, 'neutral': 0, 'negative': -1}
            trend_df['sentiment_value'] = trend_df['sentiment'].map(sentiment_map)

            fig = px.line(
                trend_df,
                y='sentiment_value',
                title='Sentiment Trend (Recent 20 Predictions)',
                labels={'sentiment_value': 'Sentiment', 'index': 'Prediction #'}
            )
            fig.add_hline(y=0, line_dash="dash", line_color="gray")
            fig.update_yaxis(tickvals=[-1, 0, 1], ticktext=['Negative', 'Neutral', 'Positive'])
            st.plotly_chart(fig, use_container_width=True)

            # Confidence distribution
            fig = px.histogram(
                trend_df,
                x='confidence',
                nbins=10,
                title='Confidence Score Distribution',
                labels={'confidence': 'Confidence Score', 'count': 'Frequency'}
            )
            st.plotly_chart(fig, use_container_width=True)

        else:
            st.info("📊 Not enough data for trend analysis. Make more predictions!")

    else:
        st.info("📊 No data available yet. Start analyzing text to see insights!")

# Tab 4: Info
with tab4:
    st.header("ℹ️ Information & Help")

    # How it Works
    st.subheader("🔬 How It Works")
    st.markdown("""
    This sentiment analyzer uses machine learning to understand the emotional tone of text:

    1. **Text Preprocessing**: Cleans and normalizes the input text
    2. **Feature Extraction**: Identifies sentiment-bearing words and patterns
    3. **Classification**: Predicts sentiment category with confidence score
    4. **Visualization**: Presents results in an intuitive format

    ### Sentiment Categories

    - **Positive (😊)**: Expresses satisfaction, happiness, or approval
        - Examples: "Great product!", "I love it!", "Highly recommended"

    - **Negative (😞)**: Expresses dissatisfaction, frustration, or criticism
        - Examples: "Terrible quality", "Disappointed", "Don't buy"

    - **Neutral (😐)**: Factual statements without strong emotion
        - Examples: "It arrived Tuesday", "The color is blue", "As described"
    """)

    st.markdown("---")

    # Use Cases
    st.subheader("💡 Use Cases")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        **Business Applications:**
        - Product review analysis
        - Customer feedback monitoring
        - Brand sentiment tracking
        - Survey response analysis
        - Support ticket classification
        """)

    with col2:
        st.markdown("""
        **Personal Applications:**
        - Social media analysis
        - Email tone checking
        - Content moderation
        - Writing assistance
        - Communication insights
        """)

    st.markdown("---")

    # Tips
    st.subheader("💭 Tips for Best Results")
    st.markdown("""
    - **Clear text**: Write complete sentences for better accuracy
    - **Context matters**: Longer text provides more context
    - **Mixed sentiment**: Complex opinions may show neutral
    - **Sarcasm**: May not be detected accurately
    - **Languages**: Works best with English text
    """)

    st.markdown("---")

    # Technical Details
    st.subheader("🛠️ Technical Details")

    version_info = api_client.get_version()

    if version_info:
        col1, col2 = st.columns(2)

        with col1:
            st.markdown(f"""
            **API Information:**
            - Version: {version_info.get('api_version', 'N/A')}
            - Framework: {version_info.get('framework', 'N/A')}
            - ML Library: {version_info.get('ml_library', 'N/A')}
            """)

        with col2:
            st.markdown(f"""
            **Model Information:**
            - Version: {version_info.get('model_version', 'N/A')}
            - Type: Rule-based / ML Hybrid
            - Update: Real-time
            """)

    st.markdown("---")

    # Contact & Support
    st.subheader("📞 Support")
    st.info("""
    **Need Help?**
    - Check the API documentation: `/docs` endpoint
    - Review example analyses in the Analyze tab
    - Monitor system status in the sidebar
    - Check recent statistics for system health
    """)

# Footer
st.markdown("---")
st.markdown("""
<div class="footer">
    <p><strong>Sentiment Analyzer</strong> | Powered by FastAPI & Streamlit | ML for Engineers Course</p>
    <p>Built with ❤️ for production-ready ML applications</p>
</div>
""", unsafe_allow_html=True)
