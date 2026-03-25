"""
API Client Module for Sentiment Analysis Frontend

Handles all communication with the FastAPI backend,
including error handling, retries, and response parsing.
"""

import requests
import os
from typing import Dict, Optional, List
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class SentimentAPIClient:
    """
    Client for interacting with the Sentiment Analysis API

    Provides methods for making predictions, checking health,
    and retrieving statistics from the backend service.
    """

    def __init__(self, base_url: Optional[str] = None):
        """
        Initialize the API client

        Args:
            base_url: Base URL of the API (defaults to localhost or env variable)
        """
        # Get API URL from environment or use default
        self.base_url = base_url or os.getenv(
            'SENTIMENT_API_URL',
            'http://localhost:8000'
        )

        # Remove trailing slash if present
        self.base_url = self.base_url.rstrip('/')

        # Configure session for connection pooling
        self.session = requests.Session()
        self.session.headers.update({
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        })

        # Timeout settings (connect timeout, read timeout)
        self.timeout = (5, 30)

        logger.info(f"API Client initialized with base URL: {self.base_url}")

    def _make_request(
        self,
        method: str,
        endpoint: str,
        data: Optional[Dict] = None,
        params: Optional[Dict] = None
    ) -> Optional[Dict]:
        """
        Make HTTP request to the API

        Args:
            method: HTTP method (GET, POST, etc.)
            endpoint: API endpoint (e.g., '/predict')
            data: Request body data (for POST)
            params: Query parameters (for GET)

        Returns:
            Response JSON or None if request fails
        """
        url = f"{self.base_url}{endpoint}"

        try:
            response = self.session.request(
                method=method,
                url=url,
                json=data,
                params=params,
                timeout=self.timeout
            )

            # Raise exception for bad status codes
            response.raise_for_status()

            return response.json()

        except requests.exceptions.Timeout:
            logger.error(f"Request timeout for {endpoint}")
            return None

        except requests.exceptions.ConnectionError:
            logger.error(f"Connection error for {endpoint}. Is the API running?")
            return None

        except requests.exceptions.HTTPError as e:
            logger.error(f"HTTP error for {endpoint}: {e}")
            # Try to get error details from response
            try:
                error_detail = e.response.json().get('detail', str(e))
                logger.error(f"Error details: {error_detail}")
            except:
                pass
            return None

        except Exception as e:
            logger.error(f"Unexpected error for {endpoint}: {e}")
            return None

    def check_health(self) -> Optional[Dict]:
        """
        Check API health status

        Returns:
            Health status dict or None if unavailable
        """
        return self._make_request('GET', '/health')

    def get_version(self) -> Optional[Dict]:
        """
        Get API and model version information

        Returns:
            Version information dict or None if unavailable
        """
        return self._make_request('GET', '/version')

    def predict_sentiment(
        self,
        text: str,
        include_details: bool = False
    ) -> Optional[Dict]:
        """
        Predict sentiment for given text

        Args:
            text: Input text to analyze
            include_details: Whether to include detailed analysis

        Returns:
            Prediction result or None if request fails
        """
        if not text or not text.strip():
            logger.error("Text cannot be empty")
            return None

        data = {
            'text': text,
            'include_details': include_details
        }

        return self._make_request('POST', '/predict', data=data)

    def get_statistics(self) -> Optional[Dict]:
        """
        Get prediction statistics

        Returns:
            Statistics dict or None if unavailable
        """
        return self._make_request('GET', '/stats')

    def reset_statistics(self) -> Optional[Dict]:
        """
        Reset prediction statistics

        Returns:
            Confirmation message or None if request fails
        """
        return self._make_request('POST', '/reset-stats')

    def batch_predict(
        self,
        texts: List[str],
        include_details: bool = False
    ) -> List[Optional[Dict]]:
        """
        Predict sentiment for multiple texts

        Args:
            texts: List of texts to analyze
            include_details: Whether to include detailed analysis

        Returns:
            List of prediction results
        """
        results = []

        for text in texts:
            result = self.predict_sentiment(text, include_details)
            results.append(result)

        return results

    def is_api_available(self) -> bool:
        """
        Check if API is available and responding

        Returns:
            True if API is healthy, False otherwise
        """
        health = self.check_health()
        return health is not None and health.get('status') == 'healthy'

    def get_api_info(self) -> Optional[Dict]:
        """
        Get general API information

        Returns:
            API info dict or None if unavailable
        """
        return self._make_request('GET', '/')

    def update_base_url(self, new_url: str):
        """
        Update the base URL for the API

        Args:
            new_url: New base URL
        """
        self.base_url = new_url.rstrip('/')
        logger.info(f"Base URL updated to: {self.base_url}")

    def close(self):
        """Close the session"""
        self.session.close()
        logger.info("API client session closed")


# Example usage and testing
if __name__ == "__main__":
    # Initialize client
    client = SentimentAPIClient()

    # Check health
    print("Checking API health...")
    health = client.check_health()
    if health:
        print(f"Health Status: {health}")
    else:
        print("API is not available")

    # Get version
    print("\nGetting version info...")
    version = client.get_version()
    if version:
        print(f"Version Info: {version}")

    # Test prediction
    print("\nTesting sentiment prediction...")
    test_texts = [
        "This is absolutely amazing! I love it!",
        "Terrible product. Complete waste of money.",
        "It's okay, nothing special."
    ]

    for text in test_texts:
        result = client.predict_sentiment(text, include_details=True)
        if result:
            print(f"\nText: {text}")
            print(f"Sentiment: {result.get('sentiment')}")
            print(f"Confidence: {result.get('confidence'):.2%}")

    # Get statistics
    print("\nGetting statistics...")
    stats = client.get_statistics()
    if stats:
        print(f"Total Predictions: {stats.get('total_predictions')}")
        print(f"Positive: {stats.get('positive_count')} ({stats.get('positive_percentage'):.1f}%)")
        print(f"Negative: {stats.get('negative_count')} ({stats.get('negative_percentage'):.1f}%)")
        print(f"Neutral: {stats.get('neutral_count')} ({stats.get('neutral_percentage'):.1f}%)")

    # Close session
    client.close()
