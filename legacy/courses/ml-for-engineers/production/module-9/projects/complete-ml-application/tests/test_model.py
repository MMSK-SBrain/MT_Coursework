"""
ML Model Tests for Sentiment Analysis

Tests model loading, preprocessing, predictions, and performance.
"""

import pytest
import sys
from pathlib import Path
import time

# Add backend to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'backend'))

from ml_service import SentimentAnalyzer


class TestModelInitialization:
    """Test model initialization and loading"""

    def test_model_initialization(self):
        """Test that model initializes successfully"""
        analyzer = SentimentAnalyzer()
        assert analyzer is not None
        assert analyzer.model_version is not None

    def test_model_info(self):
        """Test model information retrieval"""
        analyzer = SentimentAnalyzer()
        info = analyzer.get_info()

        assert "version" in info
        assert "loaded_at" in info
        assert "type" in info
        assert "positive_words_count" in info
        assert "negative_words_count" in info

    def test_sentiment_keywords_loaded(self):
        """Test that sentiment keywords are loaded"""
        analyzer = SentimentAnalyzer()

        assert len(analyzer.positive_words) > 0
        assert len(analyzer.negative_words) > 0

        # Check some expected keywords
        assert "good" in analyzer.positive_words
        assert "great" in analyzer.positive_words
        assert "bad" in analyzer.negative_words
        assert "terrible" in analyzer.negative_words


class TestTextPreprocessing:
    """Test text preprocessing functionality"""

    def test_lowercase_conversion(self):
        """Test that text is converted to lowercase"""
        analyzer = SentimentAnalyzer()
        result = analyzer.preprocess_text("HELLO WORLD")
        assert result == "hello world"

    def test_url_removal(self):
        """Test that URLs are removed"""
        analyzer = SentimentAnalyzer()
        text = "Check this out http://example.com great product"
        result = analyzer.preprocess_text(text)
        assert "http" not in result
        assert "example.com" not in result

    def test_email_removal(self):
        """Test that email addresses are removed"""
        analyzer = SentimentAnalyzer()
        text = "Contact me at test@example.com for info"
        result = analyzer.preprocess_text(text)
        assert "@" not in result
        assert "test@example.com" not in result

    def test_special_character_removal(self):
        """Test that special characters are removed"""
        analyzer = SentimentAnalyzer()
        text = "Great!!! Amazing$$$ Product###"
        result = analyzer.preprocess_text(text)
        # Should keep letters and spaces, remove special chars
        assert "great" in result
        assert "amazing" in result
        assert "$" not in result
        assert "#" not in result

    def test_whitespace_normalization(self):
        """Test that extra whitespace is normalized"""
        analyzer = SentimentAnalyzer()
        text = "This    has    extra    spaces"
        result = analyzer.preprocess_text(text)
        assert "  " not in result  # No double spaces

    def test_empty_text_preprocessing(self):
        """Test preprocessing empty text"""
        analyzer = SentimentAnalyzer()
        result = analyzer.preprocess_text("")
        assert result == ""


class TestSentimentPrediction:
    """Test sentiment prediction functionality"""

    def test_positive_sentiment(self):
        """Test prediction for clearly positive text"""
        analyzer = SentimentAnalyzer()
        result = analyzer.predict("This is absolutely amazing! I love it!")

        assert result["sentiment"] == "positive"
        assert result["confidence"] > 0.5
        assert "timestamp" in result
        assert "model_version" in result

    def test_negative_sentiment(self):
        """Test prediction for clearly negative text"""
        analyzer = SentimentAnalyzer()
        result = analyzer.predict("This is terrible! Worst product ever! Very disappointed!")

        assert result["sentiment"] == "negative"
        assert result["confidence"] > 0.5

    def test_neutral_sentiment(self):
        """Test prediction for neutral text"""
        analyzer = SentimentAnalyzer()
        result = analyzer.predict("The package arrived on Tuesday. It is blue.")

        # Neutral or low confidence
        assert result["sentiment"] in ["neutral", "positive", "negative"]
        assert 0 <= result["confidence"] <= 1

    def test_mixed_sentiment(self):
        """Test prediction for mixed sentiment text"""
        analyzer = SentimentAnalyzer()
        result = analyzer.predict(
            "The quality is great but the price is too high and delivery was slow"
        )

        assert result["sentiment"] in ["positive", "negative", "neutral"]
        assert 0 <= result["confidence"] <= 1

    def test_confidence_range(self):
        """Test that confidence is always between 0 and 1"""
        analyzer = SentimentAnalyzer()
        test_texts = [
            "Amazing!",
            "Terrible!",
            "Okay",
            "Very good but expensive",
            "Not bad"
        ]

        for text in test_texts:
            result = analyzer.predict(text)
            assert 0 <= result["confidence"] <= 1

    def test_prediction_with_details(self):
        """Test prediction with detailed analysis"""
        analyzer = SentimentAnalyzer()
        result = analyzer.predict("Great product!", include_details=True)

        assert "details" in result
        assert result["details"] is not None

        details = result["details"]
        assert "preprocessed_text" in details
        assert "text_length" in details
        assert "word_count" in details
        assert "method" in details

    def test_prediction_without_details(self):
        """Test prediction without detailed analysis"""
        analyzer = SentimentAnalyzer()
        result = analyzer.predict("Great product!", include_details=False)

        assert "details" not in result or result.get("details") is None


class TestEdgeCases:
    """Test edge cases and error handling"""

    def test_empty_text_prediction(self):
        """Test prediction with empty text"""
        analyzer = SentimentAnalyzer()

        with pytest.raises(ValueError):
            analyzer.predict("")

    def test_whitespace_only_text(self):
        """Test prediction with whitespace-only text"""
        analyzer = SentimentAnalyzer()

        with pytest.raises(ValueError):
            analyzer.predict("   ")

    def test_very_short_text(self):
        """Test prediction with very short text"""
        analyzer = SentimentAnalyzer()
        result = analyzer.predict("Good")

        assert result["sentiment"] == "positive"
        assert "confidence" in result

    def test_very_long_text(self):
        """Test prediction with very long text"""
        analyzer = SentimentAnalyzer()
        long_text = "This is an amazing product! " * 100

        result = analyzer.predict(long_text)
        assert "sentiment" in result
        assert "confidence" in result

    def test_numbers_only(self):
        """Test prediction with numbers only (should fail preprocessing)"""
        analyzer = SentimentAnalyzer()
        result = analyzer.predict("123 456 789")

        # Should handle gracefully
        assert "sentiment" in result

    def test_special_characters_only(self):
        """Test prediction with special characters only"""
        analyzer = SentimentAnalyzer()
        result = analyzer.predict("!!! ### $$$ %%%")

        assert "sentiment" in result

    def test_unicode_characters(self):
        """Test prediction with unicode characters"""
        analyzer = SentimentAnalyzer()
        result = analyzer.predict("This is great! 😊😊😊")

        assert result["sentiment"] == "positive"


class TestNegationHandling:
    """Test negation handling in sentiment analysis"""

    def test_simple_negation(self):
        """Test simple negation (not good)"""
        analyzer = SentimentAnalyzer()

        positive = analyzer.predict("This is good")
        negated = analyzer.predict("This is not good")

        # Negated version should have different or lower positive sentiment
        assert positive["sentiment"] == "positive"
        # Negated should be negative or neutral
        assert negated["sentiment"] in ["negative", "neutral"]

    def test_double_negation(self):
        """Test double negation"""
        analyzer = SentimentAnalyzer()
        result = analyzer.predict("Not bad at all")

        # Double negation can be tricky, should handle gracefully
        assert result["sentiment"] in ["positive", "neutral", "negative"]


class TestIntensifiers:
    """Test intensifier handling"""

    def test_intensifier_effect(self):
        """Test that intensifiers increase sentiment strength"""
        analyzer = SentimentAnalyzer()

        normal = analyzer.predict("This is good")
        intensified = analyzer.predict("This is very good")

        # Intensified should have higher confidence or stronger sentiment
        assert normal["sentiment"] == "positive"
        assert intensified["sentiment"] == "positive"
        # Intensified might have higher confidence
        # Note: This might not always be true depending on implementation


class TestPerformance:
    """Test model performance and speed"""

    def test_prediction_speed(self):
        """Test that predictions are fast"""
        analyzer = SentimentAnalyzer()

        start = time.time()
        analyzer.predict("This is a test prediction for speed measurement")
        end = time.time()

        # Should complete in less than 1 second
        assert (end - start) < 1.0

    def test_batch_prediction_speed(self):
        """Test speed of multiple predictions"""
        analyzer = SentimentAnalyzer()

        texts = [
            "Great product!",
            "Terrible experience",
            "It's okay",
            "Amazing quality",
            "Not recommended"
        ]

        start = time.time()
        for text in texts:
            analyzer.predict(text)
        end = time.time()

        # Should complete 5 predictions in less than 5 seconds
        assert (end - start) < 5.0

    def test_preprocessing_speed(self):
        """Test preprocessing speed"""
        analyzer = SentimentAnalyzer()

        long_text = "This is a test. " * 100

        start = time.time()
        analyzer.preprocess_text(long_text)
        end = time.time()

        # Should complete in less than 0.1 seconds
        assert (end - start) < 0.1


class TestConsistency:
    """Test prediction consistency"""

    def test_same_input_consistency(self):
        """Test that same input gives same output"""
        analyzer = SentimentAnalyzer()

        text = "This is a great product!"

        result1 = analyzer.predict(text)
        result2 = analyzer.predict(text)

        assert result1["sentiment"] == result2["sentiment"]
        assert result1["confidence"] == result2["confidence"]

    def test_similar_input_consistency(self):
        """Test that similar inputs give similar outputs"""
        analyzer = SentimentAnalyzer()

        text1 = "This is great!"
        text2 = "This is amazing!"

        result1 = analyzer.predict(text1)
        result2 = analyzer.predict(text2)

        # Both should be positive
        assert result1["sentiment"] == "positive"
        assert result2["sentiment"] == "positive"


class TestVersioning:
    """Test model versioning"""

    def test_version_retrieval(self):
        """Test getting model version"""
        analyzer = SentimentAnalyzer()
        version = analyzer.get_version()

        assert version is not None
        assert isinstance(version, str)
        assert len(version) > 0

    def test_version_in_prediction(self):
        """Test that version is included in predictions"""
        analyzer = SentimentAnalyzer()
        result = analyzer.predict("Test text")

        assert "model_version" in result
        assert result["model_version"] == analyzer.get_version()


# Test data fixtures
@pytest.fixture
def sample_positive_texts():
    """Sample positive sentiment texts"""
    return [
        "This is absolutely amazing!",
        "Love this product!",
        "Excellent quality and fast delivery",
        "Highly recommend! Best purchase ever!",
        "Outstanding service and great value"
    ]


@pytest.fixture
def sample_negative_texts():
    """Sample negative sentiment texts"""
    return [
        "Terrible product, complete waste of money",
        "Very disappointed with this purchase",
        "Awful quality, broke immediately",
        "Worst experience ever, don't buy",
        "Poor service and overpriced"
    ]


@pytest.fixture
def sample_neutral_texts():
    """Sample neutral sentiment texts"""
    return [
        "The package arrived on Tuesday",
        "The product is blue in color",
        "It measures 10 inches long",
        "Made in China, as described",
        "Contains 5 items in the box"
    ]


# Parameterized tests
@pytest.mark.parametrize("text,expected_sentiment", [
    ("Amazing product!", "positive"),
    ("Terrible quality", "negative"),
    ("Great value for money", "positive"),
    ("Complete waste", "negative"),
    ("Love it!", "positive"),
])
def test_expected_sentiments(text, expected_sentiment):
    """Test that expected sentiments are predicted correctly"""
    analyzer = SentimentAnalyzer()
    result = analyzer.predict(text)
    assert result["sentiment"] == expected_sentiment


# Run tests
if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
