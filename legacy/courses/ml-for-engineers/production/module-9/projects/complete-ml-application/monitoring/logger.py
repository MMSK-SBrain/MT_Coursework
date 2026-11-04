"""
Prediction Logger Module

Handles logging of predictions to SQLite database for monitoring
and analysis purposes.
"""

import sqlite3
import pandas as pd
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class PredictionLogger:
    """
    Logger for ML predictions

    Stores predictions in SQLite database for monitoring,
    analysis, and debugging purposes.
    """

    def __init__(self, db_path: Optional[str] = None):
        """
        Initialize the prediction logger

        Args:
            db_path: Path to SQLite database file (default: predictions.db)
        """
        if db_path is None:
            # Store in monitoring directory
            db_path = Path(__file__).parent / "predictions.db"

        self.db_path = str(db_path)
        self.init_database()

    def init_database(self):
        """Initialize database schema"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            # Create predictions table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS predictions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT NOT NULL,
                    text TEXT NOT NULL,
                    text_preview TEXT,
                    sentiment TEXT NOT NULL,
                    confidence REAL NOT NULL,
                    model_version TEXT,
                    method TEXT,
                    positive_score REAL,
                    negative_score REAL,
                    text_length INTEGER,
                    word_count INTEGER,
                    client_ip TEXT,
                    created_at TEXT DEFAULT CURRENT_TIMESTAMP
                )
            """)

            # Create index on timestamp for faster queries
            cursor.execute("""
                CREATE INDEX IF NOT EXISTS idx_timestamp
                ON predictions(timestamp)
            """)

            # Create index on sentiment
            cursor.execute("""
                CREATE INDEX IF NOT EXISTS idx_sentiment
                ON predictions(sentiment)
            """)

            conn.commit()
            conn.close()

            logger.info(f"Database initialized at {self.db_path}")

        except Exception as e:
            logger.error(f"Failed to initialize database: {e}")
            raise

    def log_prediction(
        self,
        text: str,
        sentiment: str,
        confidence: float,
        model_version: str = "1.0.0",
        details: Optional[Dict] = None,
        client_ip: Optional[str] = None
    ) -> bool:
        """
        Log a prediction to the database

        Args:
            text: Input text
            sentiment: Predicted sentiment
            confidence: Confidence score
            model_version: Model version used
            details: Optional detailed analysis
            client_ip: Optional client IP address

        Returns:
            True if successful, False otherwise
        """
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            # Prepare text preview
            text_preview = text[:100] + "..." if len(text) > 100 else text

            # Extract details if provided
            method = details.get('method', 'unknown') if details else 'unknown'
            positive_score = details.get('positive_score') if details else None
            negative_score = details.get('negative_score') if details else None
            text_length = details.get('text_length', len(text)) if details else len(text)
            word_count = details.get('word_count', len(text.split())) if details else len(text.split())

            # Insert record
            cursor.execute("""
                INSERT INTO predictions (
                    timestamp, text, text_preview, sentiment, confidence,
                    model_version, method, positive_score, negative_score,
                    text_length, word_count, client_ip
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                datetime.now().isoformat(),
                text,
                text_preview,
                sentiment,
                confidence,
                model_version,
                method,
                positive_score,
                negative_score,
                text_length,
                word_count,
                client_ip
            ))

            conn.commit()
            conn.close()

            logger.info(f"Logged prediction: {sentiment} ({confidence:.2f})")
            return True

        except Exception as e:
            logger.error(f"Failed to log prediction: {e}")
            return False

    def get_logs(
        self,
        hours_back: Optional[int] = None,
        sentiment_filter: Optional[str] = None,
        min_confidence: Optional[float] = None,
        limit: Optional[int] = None
    ) -> pd.DataFrame:
        """
        Retrieve logs from database

        Args:
            hours_back: Number of hours to look back (None for all)
            sentiment_filter: Filter by sentiment (positive/negative/neutral)
            min_confidence: Minimum confidence threshold
            limit: Maximum number of records to return

        Returns:
            DataFrame with prediction logs
        """
        try:
            conn = sqlite3.connect(self.db_path)

            # Build query
            query = "SELECT * FROM predictions WHERE 1=1"
            params = []

            # Time filter
            if hours_back is not None:
                cutoff_time = datetime.now() - timedelta(hours=hours_back)
                query += " AND timestamp >= ?"
                params.append(cutoff_time.isoformat())

            # Sentiment filter
            if sentiment_filter:
                query += " AND sentiment = ?"
                params.append(sentiment_filter)

            # Confidence filter
            if min_confidence is not None:
                query += " AND confidence >= ?"
                params.append(min_confidence)

            # Order by timestamp descending
            query += " ORDER BY timestamp DESC"

            # Limit
            if limit:
                query += f" LIMIT {limit}"

            # Execute query
            df = pd.read_sql_query(query, conn, params=params)
            conn.close()

            return df

        except Exception as e:
            logger.error(f"Failed to retrieve logs: {e}")
            return pd.DataFrame()

    def get_all_logs(self) -> pd.DataFrame:
        """Get all prediction logs"""
        return self.get_logs()

    def get_statistics(self, hours_back: Optional[int] = None) -> Dict:
        """
        Calculate statistics from logs

        Args:
            hours_back: Number of hours to look back (None for all)

        Returns:
            Dictionary with statistics
        """
        try:
            df = self.get_logs(hours_back=hours_back)

            if df.empty:
                return {
                    'total_predictions': 0,
                    'positive_count': 0,
                    'negative_count': 0,
                    'neutral_count': 0,
                    'avg_confidence': 0.0,
                    'avg_text_length': 0,
                    'avg_word_count': 0
                }

            # Calculate counts
            sentiment_counts = df['sentiment'].value_counts().to_dict()

            total = len(df)

            return {
                'total_predictions': total,
                'positive_count': sentiment_counts.get('positive', 0),
                'negative_count': sentiment_counts.get('negative', 0),
                'neutral_count': sentiment_counts.get('neutral', 0),
                'positive_percentage': (sentiment_counts.get('positive', 0) / total * 100),
                'negative_percentage': (sentiment_counts.get('negative', 0) / total * 100),
                'neutral_percentage': (sentiment_counts.get('neutral', 0) / total * 100),
                'avg_confidence': df['confidence'].mean(),
                'avg_text_length': df['text_length'].mean(),
                'avg_word_count': df['word_count'].mean(),
                'min_confidence': df['confidence'].min(),
                'max_confidence': df['confidence'].max()
            }

        except Exception as e:
            logger.error(f"Failed to calculate statistics: {e}")
            return {}

    def clear_old_logs(self, days_to_keep: int = 30) -> int:
        """
        Delete old logs to manage database size

        Args:
            days_to_keep: Number of days to keep (default: 30)

        Returns:
            Number of records deleted
        """
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            cutoff_date = datetime.now() - timedelta(days=days_to_keep)

            cursor.execute(
                "DELETE FROM predictions WHERE timestamp < ?",
                (cutoff_date.isoformat(),)
            )

            deleted_count = cursor.rowcount
            conn.commit()
            conn.close()

            logger.info(f"Deleted {deleted_count} old log records")
            return deleted_count

        except Exception as e:
            logger.error(f"Failed to clear old logs: {e}")
            return 0

    def delete_all_logs(self) -> bool:
        """
        Delete all logs (use with caution!)

        Returns:
            True if successful
        """
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            cursor.execute("DELETE FROM predictions")
            conn.commit()
            conn.close()

            logger.warning("All logs deleted!")
            return True

        except Exception as e:
            logger.error(f"Failed to delete logs: {e}")
            return False

    def export_logs(self, filepath: str, hours_back: Optional[int] = None) -> bool:
        """
        Export logs to CSV file

        Args:
            filepath: Path to save CSV file
            hours_back: Number of hours to export (None for all)

        Returns:
            True if successful
        """
        try:
            df = self.get_logs(hours_back=hours_back)

            if df.empty:
                logger.warning("No logs to export")
                return False

            df.to_csv(filepath, index=False)
            logger.info(f"Exported {len(df)} logs to {filepath}")
            return True

        except Exception as e:
            logger.error(f"Failed to export logs: {e}")
            return False

    def get_database_size(self) -> int:
        """
        Get database file size in bytes

        Returns:
            File size in bytes
        """
        try:
            return Path(self.db_path).stat().st_size
        except Exception as e:
            logger.error(f"Failed to get database size: {e}")
            return 0

    def get_record_count(self) -> int:
        """
        Get total number of records in database

        Returns:
            Number of records
        """
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            cursor.execute("SELECT COUNT(*) FROM predictions")
            count = cursor.fetchone()[0]

            conn.close()
            return count

        except Exception as e:
            logger.error(f"Failed to get record count: {e}")
            return 0


# Example usage and testing
if __name__ == "__main__":
    # Initialize logger
    pred_logger = PredictionLogger()

    # Log some test predictions
    test_predictions = [
        {
            'text': 'This is absolutely amazing! I love it!',
            'sentiment': 'positive',
            'confidence': 0.92,
            'details': {
                'method': 'rule_based',
                'positive_score': 3.5,
                'negative_score': 0.0
            }
        },
        {
            'text': 'Terrible experience. Complete waste of money.',
            'sentiment': 'negative',
            'confidence': 0.88,
            'details': {
                'method': 'rule_based',
                'positive_score': 0.0,
                'negative_score': 2.5
            }
        },
        {
            'text': "It's okay, nothing special.",
            'sentiment': 'neutral',
            'confidence': 0.65,
            'details': {
                'method': 'rule_based',
                'positive_score': 0.5,
                'negative_score': 0.5
            }
        }
    ]

    print("Logging test predictions...")
    for pred in test_predictions:
        pred_logger.log_prediction(
            text=pred['text'],
            sentiment=pred['sentiment'],
            confidence=pred['confidence'],
            details=pred['details']
        )

    # Get statistics
    print("\nStatistics:")
    stats = pred_logger.get_statistics()
    for key, value in stats.items():
        print(f"  {key}: {value}")

    # Get recent logs
    print("\nRecent logs:")
    logs_df = pred_logger.get_logs(limit=5)
    print(logs_df[['timestamp', 'sentiment', 'confidence', 'text_preview']])

    # Database info
    print(f"\nDatabase size: {pred_logger.get_database_size()} bytes")
    print(f"Total records: {pred_logger.get_record_count()}")
