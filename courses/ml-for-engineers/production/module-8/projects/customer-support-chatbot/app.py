"""
Customer Support Chatbot - Streamlit App
==========================================

A conversational AI chatbot for customer support using intent classification
and template-based response generation.

Author: ML for Engineers Course
Date: 2026-01-06
"""

import streamlit as st
import joblib
import json
import random
import re
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Customer Support Chatbot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .user-message {
        background-color: #e3f2fd;
        padding: 10px 15px;
        border-radius: 15px;
        margin: 5px 0;
        text-align: right;
    }
    .bot-message {
        background-color: #f5f5f5;
        padding: 10px 15px;
        border-radius: 15px;
        margin: 5px 0;
        text-align: left;
    }
    .intent-badge {
        background-color: #2ca02c;
        color: white;
        padding: 3px 8px;
        border-radius: 5px;
        font-size: 0.8rem;
    }
</style>
""", unsafe_allow_html=True)


# Load models and data
@st.cache_resource
def load_models():
    """Load trained classifier and vectorizer."""
    try:
        classifier = joblib.load('intent_classifier.pkl')
        vectorizer = joblib.load('tfidf_vectorizer.pkl')
        with open('intents.json', 'r') as f:
            intents_data = json.load(f)
        return classifier, vectorizer, intents_data
    except FileNotFoundError:
        st.error("⚠️ Model files not found! Please train the model first.")
        st.stop()


def preprocess_text(text):
    """Clean and preprocess user input."""
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def get_response(intent, intents_data):
    """Get random response for predicted intent."""
    for intent_obj in intents_data['intents']:
        if intent_obj['tag'] == intent:
            return random.choice(intent_obj['responses'])
    return "I'm not sure how to help with that. Could you rephrase your question?"


def predict_intent(user_input, classifier, vectorizer):
    """Predict intent and get confidence score."""
    cleaned = preprocess_text(user_input)
    vectorized = vectorizer.transform([cleaned])
    intent = classifier.predict(vectorized)[0]
    probabilities = classifier.predict_proba(vectorized)[0]
    confidence = max(probabilities)
    return intent, confidence


# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append({
        'role': 'bot',
        'content': 'Hello! I\'m your customer support assistant. How can I help you today?',
        'intent': 'greeting',
        'confidence': 1.0,
        'timestamp': datetime.now()
    })


# Main app
def main():
    """Main Streamlit app."""

    # Header
    st.markdown('<h1 class="main-header">🤖 Customer Support Chatbot</h1>', unsafe_allow_html=True)

    # Load models
    classifier, vectorizer, intents_data = load_models()

    # Sidebar
    with st.sidebar:
        st.header("📊 Chatbot Info")
        st.markdown(f"""
        **Capabilities:**
        - {len(intents_data['intents'])} supported intents
        - Natural language understanding
        - Real-time response generation

        **Available Intents:**
        """)

        for intent in intents_data['intents']:
            st.markdown(f"• {intent['tag']}")

        st.markdown("---")

        if st.button("🗑️ Clear Chat History"):
            st.session_state.messages = []
            st.session_state.messages.append({
                'role': 'bot',
                'content': 'Chat history cleared. How can I help you?',
                'intent': 'greeting',
                'confidence': 1.0,
                'timestamp': datetime.now()
            })
            st.experimental_rerun()

        st.markdown("---")
        st.info("💡 **Tip:** Try asking about orders, returns, shipping, or account help!")

    # Main chat area
    st.subheader("💬 Chat")

    # Display chat messages
    chat_container = st.container()
    with chat_container:
        for message in st.session_state.messages:
            if message['role'] == 'user':
                st.markdown(
                    f'<div class="user-message"><strong>You:</strong> {message["content"]}</div>',
                    unsafe_allow_html=True
                )
            else:
                intent_badge = f'<span class="intent-badge">{message["intent"]}</span>'
                confidence_text = f' ({message["confidence"]:.0%} confidence)' if message.get('confidence', 0) < 1.0 else ''
                st.markdown(
                    f'<div class="bot-message"><strong>Bot:</strong> {message["content"]}<br>{intent_badge}{confidence_text}</div>',
                    unsafe_allow_html=True
                )

    # Chat input
    st.markdown("---")
    col1, col2 = st.columns([4, 1])

    with col1:
        user_input = st.text_input(
            "Type your message here...",
            key="user_input",
            placeholder="e.g., Where is my order?",
            label_visibility="collapsed"
        )

    with col2:
        send_button = st.button("Send", use_container_width=True)

    # Process user input
    if send_button and user_input:
        # Add user message
        st.session_state.messages.append({
            'role': 'user',
            'content': user_input,
            'timestamp': datetime.now()
        })

        # Get bot response
        intent, confidence = predict_intent(user_input, classifier, vectorizer)
        response = get_response(intent, intents_data)

        # Add bot response
        st.session_state.messages.append({
            'role': 'bot',
            'content': response,
            'intent': intent,
            'confidence': confidence,
            'timestamp': datetime.now()
        })

        # Rerun to update chat
        st.experimental_rerun()

    # Statistics
    st.markdown("---")
    col1, col2, col3 = st.columns(3)

    with col1:
        total_messages = len([m for m in st.session_state.messages if m['role'] == 'user'])
        st.metric("Total Messages", total_messages)

    with col2:
        if st.session_state.messages:
            avg_confidence = sum([m.get('confidence', 0) for m in st.session_state.messages if m['role'] == 'bot']) / max(1, len([m for m in st.session_state.messages if m['role'] == 'bot']))
            st.metric("Avg Confidence", f"{avg_confidence:.1%}")
        else:
            st.metric("Avg Confidence", "N/A")

    with col3:
        unique_intents = len(set([m.get('intent', '') for m in st.session_state.messages if m['role'] == 'bot']))
        st.metric("Unique Intents", unique_intents)


if __name__ == "__main__":
    main()
