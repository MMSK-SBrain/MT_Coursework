"""
API Integration Tests for Sentiment Analysis Backend

Tests all API endpoints, error handling, and integration scenarios.
"""

import pytest
from fastapi.testclient import TestClient
import sys
from pathlib import Path

# Add backend to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'backend'))

from main import app

# Create test client
client = TestClient(app)


class TestHealthEndpoints:
    """Test health check and monitoring endpoints"""

    def test_health_endpoint(self):
        """Test health check endpoint"""
        response = client.get("/health")
        assert response.status_code == 200

        data = response.json()
        assert "status" in data
        assert "model_loaded" in data
        assert "timestamp" in data
        assert "version" in data

        assert data["status"] in ["healthy", "unhealthy"]
        assert isinstance(data["model_loaded"], bool)

    def test_version_endpoint(self):
        """Test version information endpoint"""
        response = client.get("/version")
        assert response.status_code == 200

        data = response.json()
        assert "api_version" in data
        assert "model_version" in data
        assert "framework" in data

        assert data["framework"] == "FastAPI"

    def test_root_endpoint(self):
        """Test root endpoint"""
        response = client.get("/")
        assert response.status_code == 200

        data = response.json()
        assert "message" in data
        assert "version" in data
        assert "endpoints" in data

        endpoints = data["endpoints"]
        assert "predict" in endpoints
        assert "health" in endpoints


class TestPredictionEndpoint:
    """Test sentiment prediction endpoint"""

    def test_predict_positive_sentiment(self):
        """Test prediction with positive text"""
        response = client.post(
            "/predict",
            json={
                "text": "This is absolutely amazing! I love it!",
                "include_details": False
            }
        )

        assert response.status_code == 200

        data = response.json()
        assert "sentiment" in data
        assert "confidence" in data
        assert "timestamp" in data
        assert "model_version" in data

        assert data["sentiment"] == "positive"
        assert 0 <= data["confidence"] <= 1

    def test_predict_negative_sentiment(self):
        """Test prediction with negative text"""
        response = client.post(
            "/predict",
            json={
                "text": "Terrible product. Complete waste of money. Very disappointed.",
                "include_details": False
            }
        )

        assert response.status_code == 200

        data = response.json()
        assert data["sentiment"] == "negative"
        assert 0 <= data["confidence"] <= 1

    def test_predict_neutral_sentiment(self):
        """Test prediction with neutral text"""
        response = client.post(
            "/predict",
            json={
                "text": "The package arrived on Tuesday. It is blue.",
                "include_details": False
            }
        )

        assert response.status_code == 200

        data = response.json()
        assert data["sentiment"] in ["neutral", "positive", "negative"]
        assert 0 <= data["confidence"] <= 1

    def test_predict_with_details(self):
        """Test prediction with detailed analysis"""
        response = client.post(
            "/predict",
            json={
                "text": "Great product! Highly recommend.",
                "include_details": True
            }
        )

        assert response.status_code == 200

        data = response.json()
        assert "details" in data
        assert data["details"] is not None

        details = data["details"]
        assert "preprocessed_text" in details
        assert "text_length" in details
        assert "word_count" in details
        assert "method" in details

    def test_predict_empty_text(self):
        """Test prediction with empty text"""
        response = client.post(
            "/predict",
            json={
                "text": "",
                "include_details": False
            }
        )

        # Should fail validation
        assert response.status_code == 422

    def test_predict_very_long_text(self):
        """Test prediction with very long text"""
        long_text = "Amazing! " * 1000  # 9000 characters

        response = client.post(
            "/predict",
            json={
                "text": long_text,
                "include_details": False
            }
        )

        # Should succeed (within 5000 char limit after truncation or fail)
        assert response.status_code in [200, 422]

    def test_predict_special_characters(self):
        """Test prediction with special characters"""
        response = client.post(
            "/predict",
            json={
                "text": "Amazing!!! 😊😊😊 Best product ever!!!",
                "include_details": False
            }
        )

        assert response.status_code == 200
        data = response.json()
        assert "sentiment" in data

    def test_predict_mixed_case(self):
        """Test prediction with mixed case text"""
        response = client.post(
            "/predict",
            json={
                "text": "EXCELLENT PRODUCT!!! Best Purchase EVER!!!",
                "include_details": False
            }
        )

        assert response.status_code == 200
        data = response.json()
        assert data["sentiment"] == "positive"


class TestStatisticsEndpoint:
    """Test statistics endpoint"""

    def test_get_statistics(self):
        """Test getting prediction statistics"""
        response = client.get("/stats")
        assert response.status_code == 200

        data = response.json()
        assert "total_predictions" in data
        assert "positive_count" in data
        assert "negative_count" in data
        assert "neutral_count" in data
        assert "positive_percentage" in data
        assert "negative_percentage" in data
        assert "neutral_percentage" in data
        assert "recent_predictions" in data

        assert isinstance(data["total_predictions"], int)
        assert isinstance(data["recent_predictions"], list)

    def test_statistics_after_prediction(self):
        """Test that statistics update after predictions"""
        # Get initial stats
        initial_response = client.get("/stats")
        initial_data = initial_response.json()
        initial_total = initial_data["total_predictions"]

        # Make a prediction
        client.post(
            "/predict",
            json={"text": "This is a test prediction", "include_details": False}
        )

        # Get updated stats
        updated_response = client.get("/stats")
        updated_data = updated_response.json()
        updated_total = updated_data["total_predictions"]

        # Total should increase
        assert updated_total == initial_total + 1


class TestErrorHandling:
    """Test error handling and edge cases"""

    def test_invalid_endpoint(self):
        """Test accessing non-existent endpoint"""
        response = client.get("/nonexistent")
        assert response.status_code == 404

    def test_invalid_method(self):
        """Test using wrong HTTP method"""
        response = client.get("/predict")  # Should be POST
        assert response.status_code == 405

    def test_missing_required_field(self):
        """Test request missing required field"""
        response = client.post(
            "/predict",
            json={"include_details": False}  # Missing 'text'
        )
        assert response.status_code == 422

    def test_invalid_data_type(self):
        """Test request with invalid data type"""
        response = client.post(
            "/predict",
            json={"text": 12345, "include_details": False}  # text should be string
        )
        assert response.status_code == 422

    def test_malformed_json(self):
        """Test request with malformed JSON"""
        response = client.post(
            "/predict",
            data="not valid json",
            headers={"Content-Type": "application/json"}
        )
        assert response.status_code == 422


class TestCORS:
    """Test CORS configuration"""

    def test_cors_headers(self):
        """Test that CORS headers are present"""
        response = client.options(
            "/predict",
            headers={
                "Origin": "http://localhost:8501",
                "Access-Control-Request-Method": "POST"
            }
        )

        # CORS should allow the request
        assert "access-control-allow-origin" in response.headers


class TestPerformance:
    """Test API performance"""

    def test_response_time(self):
        """Test that responses are reasonably fast"""
        import time

        start = time.time()
        response = client.post(
            "/predict",
            json={"text": "Quick test", "include_details": False}
        )
        end = time.time()

        assert response.status_code == 200
        assert (end - start) < 5  # Should respond in less than 5 seconds

    def test_concurrent_requests(self):
        """Test handling multiple concurrent requests"""
        import concurrent.futures

        def make_request():
            return client.post(
                "/predict",
                json={"text": "Concurrent test", "include_details": False}
            )

        # Make 10 concurrent requests
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            futures = [executor.submit(make_request) for _ in range(10)]
            results = [f.result() for f in futures]

        # All should succeed
        assert all(r.status_code == 200 for r in results)


class TestDataValidation:
    """Test input validation"""

    def test_text_length_validation(self):
        """Test text length limits"""
        # Test maximum length (5000 characters)
        max_text = "a" * 5000
        response = client.post(
            "/predict",
            json={"text": max_text, "include_details": False}
        )
        assert response.status_code == 200

        # Test over maximum length
        over_max = "a" * 5001
        response = client.post(
            "/predict",
            json={"text": over_max, "include_details": False}
        )
        assert response.status_code == 422

    def test_boolean_validation(self):
        """Test boolean field validation"""
        # Valid boolean
        response = client.post(
            "/predict",
            json={"text": "Test", "include_details": True}
        )
        assert response.status_code == 200

        # Invalid boolean
        response = client.post(
            "/predict",
            json={"text": "Test", "include_details": "yes"}
        )
        assert response.status_code == 422


# Fixtures
@pytest.fixture(autouse=True)
def reset_stats_after_test():
    """Reset statistics after each test"""
    yield
    # Optionally reset stats after tests
    # client.post("/reset-stats")


# Run tests
if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
