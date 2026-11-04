"""
Prediction Logger
Utilities for logging ML predictions to a database for monitoring.

Author: ML for Engineers Course
Date: 2024
"""

import sqlite3
import json
from datetime import datetime
from typing import Dict, Any, Optional, List
import pandas as pd
import hashlib


class PredictionLogger:
    """
    Logger for ML predictions with SQLite backend.

    Features:
    - Log predictions with metadata
    - Query predictions by date range
    - Support for batch logging
    - Privacy-preserving user ID hashing
    """

    def __init__(self, db_path: str = 'predictions.db'):
        """
        Initialize the logger.

        Args:
            db_path: Path to SQLite database file
        """
        self.db_path = db_path
        self.init_database()

    def init_database(self):
        """Initialize SQLite database with schema."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Create predictions table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS predictions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL,
                model_version TEXT NOT NULL,
                input_features TEXT NOT NULL,
                prediction REAL NOT NULL,
                confidence REAL,
                response_time_ms REAL,
                user_id TEXT,
                ground_truth REAL,
                error_message TEXT,
                metadata TEXT
            )
        ''')

        # Create indexes for faster queries
        cursor.execute('''
            CREATE INDEX IF NOT EXISTS idx_timestamp
            ON predictions(timestamp)
        ''')

        cursor.execute('''
            CREATE INDEX IF NOT EXISTS idx_model_version
            ON predictions(model_version)
        ''')

        cursor.execute('''
            CREATE INDEX IF NOT EXISTS idx_date
            ON predictions(date(timestamp))
        ''')

        conn.commit()
        conn.close()

    def log_prediction(
        self,
        model_version: str,
        input_features: Dict[str, Any],
        prediction: float,
        confidence: Optional[float] = None,
        response_time_ms: Optional[float] = None,
        user_id: Optional[str] = None,
        ground_truth: Optional[float] = None,
        error_message: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        anonymize_user: bool = True
    ):
        """
        Log a single prediction.

        Args:
            model_version: Version of the model (e.g., 'v1.0.0')
            input_features: Dictionary of input features
            prediction: Model prediction value
            confidence: Confidence/probability score (0-1)
            response_time_ms: Response time in milliseconds
            user_id: User identifier (will be hashed if anonymize_user=True)
            ground_truth: Actual value (if available)
            error_message: Error message if prediction failed
            metadata: Additional metadata as dictionary
            anonymize_user: Whether to hash user_id for privacy
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Anonymize user ID if requested
        if user_id and anonymize_user:
            user_id = self._hash_user_id(user_id)

        try:
            cursor.execute('''
                INSERT INTO predictions
                (timestamp, model_version, input_features, prediction, confidence,
                 response_time_ms, user_id, ground_truth, error_message, metadata)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                datetime.now().isoformat(),
                model_version,
                json.dumps(input_features),
                float(prediction),
                float(confidence) if confidence is not None else None,
                float(response_time_ms) if response_time_ms is not None else None,
                user_id,
                float(ground_truth) if ground_truth is not None else None,
                error_message,
                json.dumps(metadata) if metadata else None
            ))

            conn.commit()
        except Exception as e:
            conn.rollback()
            raise Exception(f"Failed to log prediction: {e}")
        finally:
            conn.close()

    def log_batch(
        self,
        predictions: List[Dict[str, Any]],
        anonymize_user: bool = True
    ):
        """
        Log multiple predictions in a batch.

        Args:
            predictions: List of dictionaries with prediction data
            anonymize_user: Whether to hash user IDs for privacy

        Example:
            predictions = [
                {
                    'model_version': 'v1.0.0',
                    'input_features': {...},
                    'prediction': 123.45,
                    'confidence': 0.89
                },
                ...
            ]
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        try:
            for pred in predictions:
                user_id = pred.get('user_id')
                if user_id and anonymize_user:
                    user_id = self._hash_user_id(user_id)

                cursor.execute('''
                    INSERT INTO predictions
                    (timestamp, model_version, input_features, prediction, confidence,
                     response_time_ms, user_id, ground_truth, error_message, metadata)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    pred.get('timestamp', datetime.now().isoformat()),
                    pred['model_version'],
                    json.dumps(pred['input_features']),
                    float(pred['prediction']),
                    float(pred['confidence']) if pred.get('confidence') is not None else None,
                    float(pred['response_time_ms']) if pred.get('response_time_ms') is not None else None,
                    user_id,
                    float(pred['ground_truth']) if pred.get('ground_truth') is not None else None,
                    pred.get('error_message'),
                    json.dumps(pred['metadata']) if pred.get('metadata') else None
                ))

            conn.commit()
        except Exception as e:
            conn.rollback()
            raise Exception(f"Failed to log batch: {e}")
        finally:
            conn.close()

    def get_recent_predictions(self, limit: int = 100) -> pd.DataFrame:
        """
        Retrieve recent predictions.

        Args:
            limit: Maximum number of predictions to return

        Returns:
            DataFrame with predictions
        """
        conn = sqlite3.connect(self.db_path)
        df = pd.read_sql_query(
            f'SELECT * FROM predictions ORDER BY timestamp DESC LIMIT {limit}',
            conn
        )
        conn.close()
        return df

    def get_predictions_by_date_range(
        self,
        start_date: str,
        end_date: str
    ) -> pd.DataFrame:
        """
        Get predictions within date range.

        Args:
            start_date: Start date (ISO format: '2024-01-01')
            end_date: End date (ISO format: '2024-01-31')

        Returns:
            DataFrame with predictions
        """
        conn = sqlite3.connect(self.db_path)
        df = pd.read_sql_query(
            '''SELECT * FROM predictions
               WHERE timestamp BETWEEN ? AND ?
               ORDER BY timestamp''',
            conn,
            params=(start_date, end_date)
        )
        conn.close()
        return df

    def get_predictions_by_model_version(
        self,
        model_version: str,
        limit: Optional[int] = None
    ) -> pd.DataFrame:
        """
        Get predictions for a specific model version.

        Args:
            model_version: Model version string (e.g., 'v1.0.0')
            limit: Optional limit on number of results

        Returns:
            DataFrame with predictions
        """
        conn = sqlite3.connect(self.db_path)

        if limit:
            query = f'''SELECT * FROM predictions
                       WHERE model_version = ?
                       ORDER BY timestamp DESC
                       LIMIT {limit}'''
        else:
            query = '''SELECT * FROM predictions
                       WHERE model_version = ?
                       ORDER BY timestamp DESC'''

        df = pd.read_sql_query(query, conn, params=(model_version,))
        conn.close()
        return df

    def get_statistics(
        self,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Get summary statistics for predictions.

        Args:
            start_date: Optional start date filter
            end_date: Optional end date filter

        Returns:
            Dictionary with statistics
        """
        if start_date and end_date:
            df = self.get_predictions_by_date_range(start_date, end_date)
        else:
            df = self.get_recent_predictions(limit=10000)

        if len(df) == 0:
            return {}

        stats = {
            'total_predictions': len(df),
            'date_range': {
                'start': df['timestamp'].min(),
                'end': df['timestamp'].max()
            },
            'predictions': {
                'mean': float(df['prediction'].mean()),
                'std': float(df['prediction'].std()),
                'min': float(df['prediction'].min()),
                'max': float(df['prediction'].max()),
                'median': float(df['prediction'].median())
            }
        }

        if 'confidence' in df.columns and df['confidence'].notna().any():
            stats['confidence'] = {
                'mean': float(df['confidence'].mean()),
                'std': float(df['confidence'].std()),
                'min': float(df['confidence'].min()),
                'max': float(df['confidence'].max())
            }

        if 'response_time_ms' in df.columns and df['response_time_ms'].notna().any():
            stats['response_time'] = {
                'mean': float(df['response_time_ms'].mean()),
                'p50': float(df['response_time_ms'].quantile(0.50)),
                'p95': float(df['response_time_ms'].quantile(0.95)),
                'p99': float(df['response_time_ms'].quantile(0.99))
            }

        # Model version breakdown
        stats['model_versions'] = df['model_version'].value_counts().to_dict()

        return stats

    def update_ground_truth(
        self,
        prediction_id: int,
        ground_truth: float
    ):
        """
        Update ground truth for a prediction (for accuracy tracking).

        Args:
            prediction_id: ID of the prediction to update
            ground_truth: Actual value
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        try:
            cursor.execute(
                'UPDATE predictions SET ground_truth = ? WHERE id = ?',
                (float(ground_truth), prediction_id)
            )
            conn.commit()
        except Exception as e:
            conn.rollback()
            raise Exception(f"Failed to update ground truth: {e}")
        finally:
            conn.close()

    def delete_old_predictions(self, days: int = 90):
        """
        Delete predictions older than specified days (for data retention).

        Args:
            days: Number of days to keep
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cutoff_date = (datetime.now() - pd.Timedelta(days=days)).isoformat()

        try:
            cursor.execute(
                'DELETE FROM predictions WHERE timestamp < ?',
                (cutoff_date,)
            )
            deleted_count = cursor.rowcount
            conn.commit()
            return deleted_count
        except Exception as e:
            conn.rollback()
            raise Exception(f"Failed to delete old predictions: {e}")
        finally:
            conn.close()

    @staticmethod
    def _hash_user_id(user_id: str) -> str:
        """
        Hash user ID for privacy.

        Args:
            user_id: Original user ID

        Returns:
            Hashed user ID (first 16 characters of SHA256 hash)
        """
        return hashlib.sha256(str(user_id).encode()).hexdigest()[:16]


# Example usage
if __name__ == "__main__":
    import numpy as np
    import time

    # Initialize logger
    logger = PredictionLogger('test_predictions.db')

    print("Logging test predictions...")

    # Log individual predictions
    for i in range(10):
        logger.log_prediction(
            model_version='v1.0.0',
            input_features={
                'feature1': np.random.rand(),
                'feature2': np.random.randint(0, 100),
                'feature3': np.random.choice(['A', 'B', 'C'])
            },
            prediction=100 + np.random.randn() * 10,
            confidence=np.random.uniform(0.7, 0.99),
            response_time_ms=np.random.uniform(50, 200),
            user_id=f"user_{i % 3}"  # Will be hashed
        )
        time.sleep(0.1)

    print("✓ Logged 10 predictions")

    # Get recent predictions
    recent = logger.get_recent_predictions(5)
    print(f"\n✓ Retrieved {len(recent)} recent predictions")
    print(recent[['timestamp', 'model_version', 'prediction', 'confidence']])

    # Get statistics
    stats = logger.get_statistics()
    print(f"\n✓ Statistics:")
    print(f"  Total predictions: {stats['total_predictions']}")
    print(f"  Mean prediction: {stats['predictions']['mean']:.2f}")
    print(f"  Mean confidence: {stats['confidence']['mean']:.3f}")
    print(f"  P95 response time: {stats['response_time']['p95']:.1f}ms")
