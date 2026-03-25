from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np
import os

# Create Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load model at startup
MODEL_PATH = 'model.pkl'
model = None

try:
    model = joblib.load(MODEL_PATH)
    print(f"✓ Model loaded successfully from {MODEL_PATH}")
except Exception as e:
    print(f"✗ Error loading model: {str(e)}")


@app.route('/', methods=['GET'])
def home():
    """Welcome endpoint"""
    return jsonify({
        'message': 'Spam Detector API',
        'version': '1.0.0',
        'endpoints': {
            'POST /predict': 'Make spam predictions',
            'GET /health': 'Check API health',
            'GET /': 'This page'
        }
    })


@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'model_loaded': model is not None
    })


@app.route('/predict', methods=['POST'])
def predict():
    """Spam prediction endpoint"""
    try:
        # Check if model is loaded
        if model is None:
            return jsonify({
                'error': 'Model not loaded'
            }), 500

        # Get JSON data from request
        data = request.get_json()

        # Validate input
        if not data or 'text' not in data:
            return jsonify({
                'error': 'Missing required field: text'
            }), 400

        text = data['text']

        # Validate text is not empty
        if not text or not text.strip():
            return jsonify({
                'error': 'Text cannot be empty'
            }), 400

        # Make prediction
        prediction = model.predict([text])[0]
        probabilities = model.predict_proba([text])[0]

        # Prepare response
        result = {
            'text': text,
            'is_spam': bool(prediction == 1),
            'label': 'spam' if prediction == 1 else 'ham',
            'confidence': float(probabilities[prediction]),
            'probabilities': {
                'ham': float(probabilities[0]),
                'spam': float(probabilities[1])
            }
        }

        return jsonify(result), 200

    except Exception as e:
        return jsonify({
            'error': f'Prediction failed: {str(e)}'
        }), 500


if __name__ == '__main__':
    # Run the app
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
