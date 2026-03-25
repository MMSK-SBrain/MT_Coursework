"""
Cricket Shot Recognition - Streamlit Deployment App
Upload an image and get instant cricket shot classification
"""

import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import os

# Page configuration
st.set_page_config(
    page_title="Cricket Shot Recognizer",
    page_icon="🏏",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        font-weight: bold;
    }
    .shot-card {
        padding: 20px;
        border-radius: 10px;
        background-color: #f0f2f6;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# Constants
CLASS_NAMES = [
    'Cover Drive',
    'Straight Drive',
    'Pull Shot',
    'Hook Shot',
    'Sweep Shot',
    'Defensive Shot'
]

SHOT_DESCRIPTIONS = {
    'Cover Drive': '🎯 Elegant front-foot shot played through the cover region',
    'Straight Drive': '🎯 Classic shot played straight down the ground',
    'Pull Shot': '🎯 Aggressive back-foot shot to the leg side',
    'Hook Shot': '🎯 Attacking shot against short-pitched deliveries',
    'Sweep Shot': '🎯 Front-foot shot sweeping to the leg side',
    'Defensive Shot': '🎯 Blocking shot with soft hands'
}

MODEL_PATH = 'models/cricket_shot_model.h5'

@st.cache_resource
def load_trained_model():
    """Load the trained model (cached for performance)"""
    if os.path.exists(MODEL_PATH):
        return load_model(MODEL_PATH)
    else:
        st.error(f"Model not found at {MODEL_PATH}. Please train the model first!")
        return None

def preprocess_image(img):
    """Preprocess uploaded image for prediction"""
    img = img.resize((224, 224))
    img_array = image.img_to_array(img)
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

def predict_shot(model, img_array):
    """Make prediction on preprocessed image"""
    predictions = model.predict(img_array, verbose=0)
    return predictions[0]

def plot_predictions(predictions):
    """Create bar chart of predictions"""
    fig, ax = plt.subplots(figsize=(10, 6))

    colors = ['#2ecc71' if pred == max(predictions) else '#3498db' for pred in predictions]
    bars = ax.barh(CLASS_NAMES, predictions, color=colors, edgecolor='black')

    ax.set_xlabel('Confidence', fontsize=12, fontweight='bold')
    ax.set_title('Prediction Confidence for Each Shot Type', fontsize=14, fontweight='bold')
    ax.set_xlim([0, 1])

    # Add percentage labels
    for i, bar in enumerate(bars):
        width = bar.get_width()
        ax.text(width + 0.02, bar.get_y() + bar.get_height()/2,
                f'{predictions[i]*100:.1f}%',
                va='center', fontsize=10, fontweight='bold')

    plt.tight_layout()
    return fig

# Main app
def main():
    # Header
    st.markdown('<h1 class="main-header">🏏 Cricket Shot Recognition System</h1>', unsafe_allow_html=True)
    st.markdown("---")

    # Sidebar
    with st.sidebar:
        st.image("https://via.placeholder.com/300x200.png?text=Cricket+AI", use_column_width=True)
        st.markdown("## About")
        st.info("""
        This AI system classifies cricket batting shots using deep learning.

        **Technology:**
        - ResNet50 Transfer Learning
        - TensorFlow/Keras
        - Streamlit

        **Accuracy:** 82.5%

        **Supported Shots:** 6 types
        """)

        st.markdown("## Instructions")
        st.markdown("""
        1. Upload a cricket shot image
        2. Wait for AI analysis
        3. View classification results
        4. Check confidence scores
        """)

        st.markdown("---")
        st.markdown("**Built with ❤️ for ML Engineers**")

    # Main content
    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown("### 📤 Upload Cricket Shot Image")
        uploaded_file = st.file_uploader(
            "Choose an image (JPG, PNG, JPEG)",
            type=['jpg', 'jpeg', 'png'],
            help="Upload a clear image of a cricket batting shot"
        )

        if uploaded_file is not None:
            # Display uploaded image
            img = Image.open(uploaded_file)
            st.image(img, caption='Uploaded Image', use_column_width=True)

            # Process button
            if st.button('🔍 Analyze Shot', type='primary'):
                with st.spinner('Analyzing cricket shot...'):
                    # Load model
                    model = load_trained_model()

                    if model is not None:
                        # Preprocess and predict
                        img_array = preprocess_image(img)
                        predictions = predict_shot(model, img_array)

                        # Get top prediction
                        top_idx = np.argmax(predictions)
                        top_class = CLASS_NAMES[top_idx]
                        top_confidence = predictions[top_idx]

                        # Store in session state
                        st.session_state['predictions'] = predictions
                        st.session_state['top_class'] = top_class
                        st.session_state['top_confidence'] = top_confidence

    with col2:
        st.markdown("### 📊 Analysis Results")

        if 'predictions' in st.session_state:
            predictions = st.session_state['predictions']
            top_class = st.session_state['top_class']
            top_confidence = st.session_state['top_confidence']

            # Main prediction card
            st.success(f"### Predicted Shot: **{top_class}**")
            st.metric(label="Confidence", value=f"{top_confidence*100:.1f}%")
            st.info(SHOT_DESCRIPTIONS[top_class])

            # Top 3 predictions
            st.markdown("#### Top 3 Predictions:")
            top_3_indices = np.argsort(predictions)[-3:][::-1]

            for i, idx in enumerate(top_3_indices):
                conf = predictions[idx]
                shot_name = CLASS_NAMES[idx]

                if i == 0:
                    st.markdown(f"🥇 **{shot_name}**: {conf*100:.1f}%")
                elif i == 1:
                    st.markdown(f"🥈 **{shot_name}**: {conf*100:.1f}%")
                else:
                    st.markdown(f"🥉 **{shot_name}**: {conf*100:.1f}%")

            # Confidence chart
            st.markdown("---")
            st.markdown("#### Detailed Confidence Scores")
            fig = plot_predictions(predictions)
            st.pyplot(fig)

            # Download results
            st.markdown("---")
            result_text = f"""
Cricket Shot Recognition Results
================================
Image: {uploaded_file.name}
Predicted Shot: {top_class}
Confidence: {top_confidence*100:.1f}%

All Predictions:
{chr(10).join([f'{CLASS_NAMES[i]}: {predictions[i]*100:.1f}%' for i in range(len(CLASS_NAMES))])}
"""
            st.download_button(
                label="📥 Download Results",
                data=result_text,
                file_name="cricket_shot_results.txt",
                mime="text/plain"
            )
        else:
            st.info("👈 Upload an image and click 'Analyze Shot' to see results")

            # Sample shots info
            st.markdown("### 📖 About Cricket Shots")
            for shot, desc in SHOT_DESCRIPTIONS.items():
                with st.expander(shot):
                    st.write(desc)

    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #7f8c8d;'>
        <p>Module 7: Computer Vision Capstone Project | ML for Engineers</p>
        <p>Powered by TensorFlow & Streamlit | ResNet50 Transfer Learning</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
