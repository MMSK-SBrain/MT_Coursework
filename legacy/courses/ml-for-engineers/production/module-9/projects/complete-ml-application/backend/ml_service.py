"""
ML Service Module for Sentiment Analysis

Handles model loading, preprocessing, prediction, and version management.
Uses a simple but effective approach suitable for production deployment.
"""

import re
import string
from datetime import datetime
from typing import Dict, List, Optional
import pickle
import logging

logger = logging.getLogger(__name__)


class SentimentAnalyzer:
    """
    Sentiment Analysis ML Service

    Provides text preprocessing, prediction, and model management
    for sentiment classification tasks.
    """

    def __init__(self, model_path: Optional[str] = None):
        """
        Initialize the sentiment analyzer

        Args:
            model_path: Path to saved model (optional, uses default rules if not provided)
        """
        self.model = None
        self.vectorizer = None
        self.model_version = "1.0.0"
        self.loaded_at = datetime.now().isoformat()

        # Load model if path provided
        if model_path:
            self._load_model(model_path)
        else:
            logger.info("Using rule-based sentiment analysis (demo mode)")

        # Sentiment keywords for rule-based approach
        self.positive_words = {
            'good', 'great', 'excellent', 'amazing', 'wonderful', 'fantastic',
            'love', 'best', 'perfect', 'awesome', 'outstanding', 'brilliant',
            'superb', 'happy', 'delighted', 'pleased', 'satisfied', 'enjoyed',
            'beautiful', 'incredible', 'exceptional', 'terrific', 'magnificent',
            'fabulous', 'lovely', 'nice', 'pleasant', 'impressive', 'positive'
        }

        self.negative_words = {
            'bad', 'terrible', 'awful', 'horrible', 'worst', 'poor', 'hate',
            'disappointing', 'disappointed', 'useless', 'waste', 'annoying',
            'frustrating', 'problem', 'issue', 'broken', 'failed', 'failure',
            'wrong', 'error', 'bug', 'crash', 'slow', 'expensive', 'overpriced',
            'never', 'unfortunately', 'sadly', 'unhappy', 'angry', 'negative'
        }

        # Intensifiers and negations
        self.intensifiers = {'very', 'extremely', 'absolutely', 'really', 'totally'}
        self.negations = {'not', 'no', 'never', 'neither', "n't", 'none', 'nobody'}

    def _load_model(self, model_path: str):
        """
        Load trained model from disk

        Args:
            model_path: Path to pickled model file
        """
        try:
            with open(model_path, 'rb') as f:
                model_data = pickle.load(f)

            self.model = model_data.get('model')
            self.vectorizer = model_data.get('vectorizer')
            self.model_version = model_data.get('version', '1.0.0')

            logger.info(f"Model loaded successfully from {model_path}")
        except Exception as e:
            logger.error(f"Failed to load model: {str(e)}")
            raise

    def preprocess_text(self, text: str) -> str:
        """
        Preprocess text for analysis

        Args:
            text: Raw input text

        Returns:
            Cleaned and normalized text
        """
        # Convert to lowercase
        text = text.lower()

        # Remove URLs
        text = re.sub(r'http\S+|www\S+', '', text)

        # Remove email addresses
        text = re.sub(r'\S+@\S+', '', text)

        # Remove special characters but keep apostrophes for contractions
        text = re.sub(r'[^a-zA-Z\s\']', '', text)

        # Remove extra whitespace
        text = ' '.join(text.split())

        return text

    def _rule_based_prediction(self, text: str) -> Dict:
        """
        Simple rule-based sentiment analysis

        Args:
            text: Preprocessed text

        Returns:
            Dictionary with sentiment and confidence
        """
        words = text.lower().split()

        # Count sentiment words
        positive_count = 0
        negative_count = 0
        negation_active = False

        for i, word in enumerate(words):
            # Check for negations
            if word in self.negations:
                negation_active = True
                continue

            # Check for intensifiers
            is_intensified = (i > 0 and words[i-1] in self.intensifiers)
            weight = 1.5 if is_intensified else 1.0

            # Count sentiment words with negation handling
            if word in self.positive_words:
                if negation_active:
                    negative_count += weight
                else:
                    positive_count += weight
                negation_active = False

            elif word in self.negative_words:
                if negation_active:
                    positive_count += weight
                else:
                    negative_count += weight
                negation_active = False

            else:
                negation_active = False

        # Determine sentiment
        total_sentiment = positive_count + negative_count

        if total_sentiment == 0:
            sentiment = "neutral"
            confidence = 0.5
        elif positive_count > negative_count:
            sentiment = "positive"
            confidence = min(0.95, 0.5 + (positive_count / (total_sentiment * 2)))
        elif negative_count > positive_count:
            sentiment = "negative"
            confidence = min(0.95, 0.5 + (negative_count / (total_sentiment * 2)))
        else:
            sentiment = "neutral"
            confidence = 0.5

        return {
            "sentiment": sentiment,
            "confidence": round(confidence, 4),
            "positive_score": round(positive_count, 2),
            "negative_score": round(negative_count, 2)
        }

    def _model_based_prediction(self, text: str) -> Dict:
        """
        ML model-based sentiment analysis

        Args:
            text: Preprocessed text

        Returns:
            Dictionary with sentiment and confidence
        """
        # Vectorize text
        text_vector = self.vectorizer.transform([text])

        # Get prediction and probability
        prediction = self.model.predict(text_vector)[0]
        probabilities = self.model.predict_proba(text_vector)[0]

        # Map prediction to sentiment
        sentiment_map = {0: "negative", 1: "neutral", 2: "positive"}
        sentiment = sentiment_map.get(prediction, "neutral")

        # Get confidence (max probability)
        confidence = max(probabilities)

        return {
            "sentiment": sentiment,
            "confidence": round(confidence, 4),
            "probabilities": {
                "negative": round(probabilities[0], 4),
                "neutral": round(probabilities[1], 4) if len(probabilities) > 2 else 0.0,
                "positive": round(probabilities[-1], 4)
            }
        }

    def predict(self, text: str, include_details: bool = False) -> Dict:
        """
        Predict sentiment for input text

        Args:
            text: Input text to analyze
            include_details: Whether to include detailed analysis

        Returns:
            Prediction result with sentiment, confidence, and optional details
        """
        # Validate input
        if not text or not text.strip():
            raise ValueError("Text cannot be empty")

        # Preprocess
        processed_text = self.preprocess_text(text)

        # Get prediction
        if self.model and self.vectorizer:
            result = self._model_based_prediction(processed_text)
        else:
            result = self._rule_based_prediction(processed_text)

        # Build response
        response = {
            "text": text,
            "sentiment": result["sentiment"],
            "confidence": result["confidence"],
            "timestamp": datetime.now().isoformat(),
            "model_version": self.model_version
        }

        # Add details if requested
        if include_details:
            response["details"] = {
                "preprocessed_text": processed_text,
                "text_length": len(text),
                "word_count": len(processed_text.split()),
                "method": "ml_model" if self.model else "rule_based",
                **{k: v for k, v in result.items() if k not in ["sentiment", "confidence"]}
            }

        return response

    def get_version(self) -> str:
        """Get model version"""
        return self.model_version

    def get_info(self) -> Dict:
        """
        Get model information

        Returns:
            Dictionary with model metadata
        """
        return {
            "version": self.model_version,
            "loaded_at": self.loaded_at,
            "type": "ml_model" if self.model else "rule_based",
            "has_vectorizer": self.vectorizer is not None,
            "positive_words_count": len(self.positive_words),
            "negative_words_count": len(self.negative_words)
        }


# Example usage and testing
if __name__ == "__main__":
    # Initialize analyzer
    analyzer = SentimentAnalyzer()

    # Test cases
    test_texts = [
        "This product is absolutely amazing! I love it!",
        "Terrible experience. Complete waste of money.",
        "It's okay, nothing special.",
        "Not bad, but could be better.",
        "The service was great, but the price was too high.",
        "I'm extremely disappointed with this purchase."
    ]

    print("Sentiment Analysis Test Results:")
    print("=" * 60)

    for text in test_texts:
        result = analyzer.predict(text, include_details=True)
        print(f"\nText: {text}")
        print(f"Sentiment: {result['sentiment']}")
        print(f"Confidence: {result['confidence']:.2%}")
        if "details" in result:
            print(f"Method: {result['details']['method']}")
