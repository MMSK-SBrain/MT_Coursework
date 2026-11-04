"""
Stock Price Predictor API
A Flask-based REST API for predicting stock prices using machine learning.

Author: ML for Engineers Course
Date: 2024
"""

from flask import Flask, request, jsonify
import joblib
import numpy as np
import os
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)

# Configuration
MODEL_PATH = os.environ.get('MODEL_PATH', 'stock_model.pkl')
MODEL_VERSION = os.environ.get('MODEL_VERSION', 'v1.0.0')
API_KEY = os.environ.get('API_KEY', None)  # Optional API key for authentication

# Global model variable (lazy loading)
model = None


def load_model():
    """Load the ML model (lazy loading)."""
    global model
    if model is None:
        try:
            logger.info(f"Loading model from {MODEL_PATH}...")
            model = joblib.load(MODEL_PATH)
            logger.info("Model loaded successfully!")
        except FileNotFoundError:
            logger.error(f"Model file not found: {MODEL_PATH}")
            raise
        except Exception as e:
            logger.error(f"Error loading model: {e}")
            raise
    return model


def validate_api_key(request):
    """Validate API key if configured."""
    if API_KEY is None:
        return True  # No API key required

    provided_key = request.headers.get('X-API-Key')
    return provided_key == API_KEY


@app.route('/', methods=['GET'])
def home():
    """Home endpoint with API information."""
    return jsonify({
        'name': 'Stock Price Predictor API',
        'version': MODEL_VERSION,
        'status': 'running',
        'endpoints': {
            'health': '/health',
            'predict': '/predict (POST)',
            'info': '/info'
        },
        'documentation': 'See README.md for usage instructions'
    })


@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint for monitoring."""
    try:
        # Try to load model to ensure it's available
        load_model()
        return jsonify({
            'status': 'healthy',
            'model_loaded': True,
            'model_version': MODEL_VERSION,
            'timestamp': datetime.now().isoformat()
        }), 200
    except Exception as e:
        logger.error(f"Health check failed: {e}")
        return jsonify({
            'status': 'unhealthy',
            'model_loaded': False,
            'error': str(e),
            'timestamp': datetime.now().isoformat()
        }), 503


@app.route('/info', methods=['GET'])
def model_info():
    """Return information about the model."""
    try:
        model_obj = load_model()
        return jsonify({
            'model_version': MODEL_VERSION,
            'model_type': type(model_obj).__name__,
            'features_required': [
                'day_of_year',
                'day_of_week',
                'trend',
                'price_lag_1',
                'price_lag_7',
                'price_lag_30',
                'rolling_mean_7',
                'rolling_std_7'
            ],
            'feature_count': 8,
            'description': 'Random Forest model for stock price prediction'
        })
    except Exception as e:
        logger.error(f"Error getting model info: {e}")
        return jsonify({'error': str(e)}), 500


@app.route('/predict', methods=['POST'])
def predict():
    """
    Make a stock price prediction.

    Expected JSON input:
    {
        "day_of_year": 350,
        "day_of_week": 3,
        "trend": 500,
        "price_lag_1": 195.5,
        "price_lag_7": 193.2,
        "price_lag_30": 188.7,
        "rolling_mean_7": 194.3,
        "rolling_std_7": 2.1
    }

    Returns:
    {
        "predicted_price": 196.45,
        "model_version": "v1.0.0",
        "timestamp": "2024-01-06T10:30:00"
    }
    """
    try:
        # Validate API key if configured
        if not validate_api_key(request):
            return jsonify({'error': 'Invalid or missing API key'}), 401

        # Get JSON data
        data = request.get_json()
        if data is None:
            return jsonify({'error': 'No JSON data provided'}), 400

        # Define required features
        required_features = [
            'day_of_year',
            'day_of_week',
            'trend',
            'price_lag_1',
            'price_lag_7',
            'price_lag_30',
            'rolling_mean_7',
            'rolling_std_7'
        ]

        # Validate all required features are present
        missing_features = [f for f in required_features if f not in data]
        if missing_features:
            return jsonify({
                'error': f'Missing required features: {missing_features}',
                'required_features': required_features
            }), 400

        # Extract and validate feature values
        try:
            features = []
            for feature in required_features:
                value = float(data[feature])
                features.append(value)

            # Additional validation
            if not 1 <= features[0] <= 366:  # day_of_year
                return jsonify({'error': 'day_of_year must be between 1 and 366'}), 400

            if not 0 <= features[1] <= 6:  # day_of_week
                return jsonify({'error': 'day_of_week must be between 0 and 6'}), 400

        except (ValueError, TypeError) as e:
            return jsonify({
                'error': f'Invalid feature values. All features must be numeric: {str(e)}'
            }), 400

        # Load model and make prediction
        model_obj = load_model()
        features_array = np.array([features])

        # Make prediction
        prediction = model_obj.predict(features_array)[0]

        # Log the prediction
        logger.info(f"Prediction made: {prediction:.2f}")

        # Return response
        return jsonify({
            'predicted_price': round(float(prediction), 2),
            'model_version': MODEL_VERSION,
            'timestamp': datetime.now().isoformat(),
            'input_features': dict(zip(required_features, features))
        }), 200

    except Exception as e:
        logger.error(f"Prediction error: {e}")
        return jsonify({
            'error': 'Internal server error during prediction',
            'details': str(e)
        }), 500


@app.route('/batch_predict', methods=['POST'])
def batch_predict():
    """
    Make predictions for multiple inputs.

    Expected JSON input:
    {
        "predictions": [
            {
                "day_of_year": 350,
                "day_of_week": 3,
                ...
            },
            {
                "day_of_year": 351,
                "day_of_week": 4,
                ...
            }
        ]
    }
    """
    try:
        # Validate API key
        if not validate_api_key(request):
            return jsonify({'error': 'Invalid or missing API key'}), 401

        data = request.get_json()
        if data is None or 'predictions' not in data:
            return jsonify({'error': 'No predictions array provided'}), 400

        predictions_input = data['predictions']
        if not isinstance(predictions_input, list):
            return jsonify({'error': 'predictions must be an array'}), 400

        if len(predictions_input) > 100:
            return jsonify({'error': 'Maximum 100 predictions per request'}), 400

        # Make predictions for each input
        results = []
        for idx, item in enumerate(predictions_input):
            try:
                # Reuse single prediction logic
                with app.test_request_context(
                    '/predict',
                    method='POST',
                    json=item,
                    headers=request.headers
                ):
                    response = predict()
                    if response[1] == 200:
                        results.append({
                            'index': idx,
                            'success': True,
                            'prediction': response[0].get_json()
                        })
                    else:
                        results.append({
                            'index': idx,
                            'success': False,
                            'error': response[0].get_json()
                        })
            except Exception as e:
                results.append({
                    'index': idx,
                    'success': False,
                    'error': str(e)
                })

        return jsonify({
            'total_predictions': len(results),
            'successful': sum(1 for r in results if r['success']),
            'failed': sum(1 for r in results if not r['success']),
            'results': results
        }), 200

    except Exception as e:
        logger.error(f"Batch prediction error: {e}")
        return jsonify({'error': str(e)}), 500


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({
        'error': 'Endpoint not found',
        'available_endpoints': ['/', '/health', '/info', '/predict', '/batch_predict']
    }), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    logger.error(f"Internal server error: {error}")
    return jsonify({
        'error': 'Internal server error',
        'message': 'An unexpected error occurred'
    }), 500


if __name__ == '__main__':
    # This is for local development only
    # In production, use Gunicorn (see Procfile)
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('DEBUG', 'False') == 'True'

    logger.info(f"Starting Flask app on port {port}...")
    app.run(host='0.0.0.0', port=port, debug=debug)
