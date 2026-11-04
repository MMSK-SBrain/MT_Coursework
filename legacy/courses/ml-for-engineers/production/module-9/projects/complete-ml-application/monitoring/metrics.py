"""
Metrics Calculation Module

Calculates performance metrics, detects drift, and generates
alerts for ML model monitoring.
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
from collections import Counter
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class MetricsCalculator:
    """
    Calculate metrics for ML model monitoring

    Provides methods for performance metrics, drift detection,
    and alerting based on various thresholds.
    """

    def __init__(self):
        """Initialize metrics calculator"""
        self.baseline_metrics = None
        self.alert_thresholds = {
            'min_confidence': 0.5,
            'max_error_rate': 0.1,
            'min_predictions_per_hour': 1,
            'max_drift_score': 0.3
        }

    def calculate_performance_metrics(self, df: pd.DataFrame) -> Dict:
        """
        Calculate comprehensive performance metrics

        Args:
            df: DataFrame with prediction logs

        Returns:
            Dictionary with performance metrics
        """
        if df.empty:
            return {}

        try:
            metrics = {}

            # Basic counts
            metrics['total_predictions'] = len(df)

            # Confidence metrics
            if 'confidence' in df.columns:
                metrics['avg_confidence'] = df['confidence'].mean()
                metrics['median_confidence'] = df['confidence'].median()
                metrics['min_confidence'] = df['confidence'].min()
                metrics['max_confidence'] = df['confidence'].max()
                metrics['std_confidence'] = df['confidence'].std()

                # High/low confidence rates
                metrics['high_confidence_rate'] = (df['confidence'] > 0.8).sum() / len(df)
                metrics['low_confidence_rate'] = (df['confidence'] < 0.5).sum() / len(df)

            # Sentiment distribution
            if 'sentiment' in df.columns:
                sentiment_counts = df['sentiment'].value_counts()
                total = len(df)

                metrics['positive_rate'] = sentiment_counts.get('positive', 0) / total
                metrics['negative_rate'] = sentiment_counts.get('negative', 0) / total
                metrics['neutral_rate'] = sentiment_counts.get('neutral', 0) / total

                # Sentiment diversity (Shannon entropy)
                metrics['diversity_score'] = self._calculate_entropy(
                    sentiment_counts.values
                )

            # Text characteristics
            if 'text_length' in df.columns:
                metrics['avg_text_length'] = df['text_length'].mean()
                metrics['median_text_length'] = df['text_length'].median()

            if 'word_count' in df.columns:
                metrics['avg_word_count'] = df['word_count'].mean()
                metrics['median_word_count'] = df['word_count'].median()

            # Time-based metrics
            if 'timestamp' in df.columns:
                df['timestamp'] = pd.to_datetime(df['timestamp'])
                time_span = (df['timestamp'].max() - df['timestamp'].min()).total_seconds() / 3600
                if time_span > 0:
                    metrics['predictions_per_hour'] = len(df) / time_span
                else:
                    metrics['predictions_per_hour'] = 0

            return metrics

        except Exception as e:
            logger.error(f"Failed to calculate performance metrics: {e}")
            return {}

    def _calculate_entropy(self, counts: np.ndarray) -> float:
        """
        Calculate Shannon entropy for diversity measurement

        Args:
            counts: Array of counts

        Returns:
            Entropy value
        """
        total = np.sum(counts)
        if total == 0:
            return 0.0

        probabilities = counts / total
        # Remove zero probabilities
        probabilities = probabilities[probabilities > 0]

        entropy = -np.sum(probabilities * np.log2(probabilities))
        return float(entropy)

    def detect_drift(
        self,
        current_df: pd.DataFrame,
        baseline_df: pd.DataFrame,
        threshold: float = 0.1
    ) -> Dict:
        """
        Detect distribution drift between current and baseline data

        Args:
            current_df: Current prediction logs
            baseline_df: Baseline prediction logs
            threshold: Drift detection threshold

        Returns:
            Dictionary with drift detection results
        """
        try:
            drift_results = {
                'drift_detected': False,
                'drift_score': 0.0,
                'metrics': {}
            }

            if current_df.empty or baseline_df.empty:
                return drift_results

            # Sentiment distribution drift
            if 'sentiment' in current_df.columns and 'sentiment' in baseline_df.columns:
                current_dist = current_df['sentiment'].value_counts(normalize=True)
                baseline_dist = baseline_df['sentiment'].value_counts(normalize=True)

                # KL divergence approximation
                sentiment_drift = self._calculate_distribution_drift(
                    current_dist, baseline_dist
                )
                drift_results['metrics']['sentiment_drift'] = sentiment_drift

                if sentiment_drift > threshold:
                    drift_results['drift_detected'] = True
                    drift_results['drift_score'] = max(
                        drift_results['drift_score'], sentiment_drift
                    )

            # Confidence distribution drift
            if 'confidence' in current_df.columns and 'confidence' in baseline_df.columns:
                confidence_drift = abs(
                    current_df['confidence'].mean() - baseline_df['confidence'].mean()
                )
                drift_results['metrics']['confidence_drift'] = confidence_drift

                if confidence_drift > threshold:
                    drift_results['drift_detected'] = True
                    drift_results['drift_score'] = max(
                        drift_results['drift_score'], confidence_drift
                    )

            # Text length drift
            if 'text_length' in current_df.columns and 'text_length' in baseline_df.columns:
                length_drift = abs(
                    current_df['text_length'].mean() - baseline_df['text_length'].mean()
                ) / baseline_df['text_length'].mean()

                drift_results['metrics']['text_length_drift'] = length_drift

                if length_drift > threshold:
                    drift_results['drift_detected'] = True

            return drift_results

        except Exception as e:
            logger.error(f"Failed to detect drift: {e}")
            return {'drift_detected': False, 'drift_score': 0.0, 'metrics': {}}

    def _calculate_distribution_drift(
        self,
        current: pd.Series,
        baseline: pd.Series
    ) -> float:
        """
        Calculate distribution drift using simplified KL divergence

        Args:
            current: Current distribution
            baseline: Baseline distribution

        Returns:
            Drift score
        """
        # Ensure same categories
        all_categories = set(current.index) | set(baseline.index)

        current_probs = []
        baseline_probs = []

        for cat in all_categories:
            current_probs.append(current.get(cat, 1e-10))
            baseline_probs.append(baseline.get(cat, 1e-10))

        current_probs = np.array(current_probs)
        baseline_probs = np.array(baseline_probs)

        # Normalize
        current_probs = current_probs / current_probs.sum()
        baseline_probs = baseline_probs / baseline_probs.sum()

        # Calculate KL divergence
        kl_div = np.sum(current_probs * np.log(current_probs / baseline_probs))

        return float(kl_div)

    def generate_alerts(
        self,
        current_metrics: Dict,
        thresholds: Optional[Dict] = None
    ) -> List[Dict]:
        """
        Generate alerts based on metrics and thresholds

        Args:
            current_metrics: Current performance metrics
            thresholds: Custom alert thresholds (optional)

        Returns:
            List of alert dictionaries
        """
        if thresholds is None:
            thresholds = self.alert_thresholds

        alerts = []

        # Low confidence alert
        if 'avg_confidence' in current_metrics:
            if current_metrics['avg_confidence'] < thresholds['min_confidence']:
                alerts.append({
                    'type': 'warning',
                    'severity': 'medium',
                    'metric': 'avg_confidence',
                    'value': current_metrics['avg_confidence'],
                    'threshold': thresholds['min_confidence'],
                    'message': f"Average confidence ({current_metrics['avg_confidence']:.2%}) below threshold ({thresholds['min_confidence']:.2%})"
                })

        # High low-confidence rate
        if 'low_confidence_rate' in current_metrics:
            if current_metrics['low_confidence_rate'] > 0.3:
                alerts.append({
                    'type': 'warning',
                    'severity': 'high',
                    'metric': 'low_confidence_rate',
                    'value': current_metrics['low_confidence_rate'],
                    'threshold': 0.3,
                    'message': f"High rate of low-confidence predictions ({current_metrics['low_confidence_rate']:.1%})"
                })

        # Sentiment imbalance
        if 'diversity_score' in current_metrics:
            if current_metrics['diversity_score'] < 0.5:
                alerts.append({
                    'type': 'info',
                    'severity': 'low',
                    'metric': 'diversity_score',
                    'value': current_metrics['diversity_score'],
                    'threshold': 0.5,
                    'message': f"Low sentiment diversity ({current_metrics['diversity_score']:.2f})"
                })

        # Low prediction rate
        if 'predictions_per_hour' in current_metrics:
            if current_metrics['predictions_per_hour'] < thresholds['min_predictions_per_hour']:
                alerts.append({
                    'type': 'info',
                    'severity': 'low',
                    'metric': 'predictions_per_hour',
                    'value': current_metrics['predictions_per_hour'],
                    'threshold': thresholds['min_predictions_per_hour'],
                    'message': f"Low prediction rate ({current_metrics['predictions_per_hour']:.1f}/hour)"
                })

        return alerts

    def calculate_trend(
        self,
        df: pd.DataFrame,
        metric: str,
        window_hours: int = 24
    ) -> Dict:
        """
        Calculate trend for a specific metric

        Args:
            df: DataFrame with prediction logs
            metric: Metric to analyze
            window_hours: Time window in hours

        Returns:
            Dictionary with trend information
        """
        try:
            if df.empty or metric not in df.columns:
                return {'trend': 'unknown', 'change': 0.0}

            # Ensure timestamp is datetime
            df['timestamp'] = pd.to_datetime(df['timestamp'])

            # Sort by timestamp
            df = df.sort_values('timestamp')

            # Calculate time window
            cutoff = df['timestamp'].max() - timedelta(hours=window_hours)
            recent_df = df[df['timestamp'] > cutoff]

            if len(recent_df) < 2:
                return {'trend': 'insufficient_data', 'change': 0.0}

            # Split into two halves
            mid_point = len(recent_df) // 2
            first_half = recent_df.iloc[:mid_point]
            second_half = recent_df.iloc[mid_point:]

            # Calculate means
            first_mean = first_half[metric].mean()
            second_mean = second_half[metric].mean()

            # Calculate change
            if first_mean != 0:
                change = (second_mean - first_mean) / first_mean
            else:
                change = 0.0

            # Determine trend
            if abs(change) < 0.05:
                trend = 'stable'
            elif change > 0:
                trend = 'increasing'
            else:
                trend = 'decreasing'

            return {
                'trend': trend,
                'change': change,
                'first_half_mean': first_mean,
                'second_half_mean': second_mean
            }

        except Exception as e:
            logger.error(f"Failed to calculate trend: {e}")
            return {'trend': 'error', 'change': 0.0}

    def set_baseline(self, df: pd.DataFrame):
        """
        Set baseline metrics for drift detection

        Args:
            df: DataFrame to use as baseline
        """
        self.baseline_metrics = self.calculate_performance_metrics(df)
        logger.info("Baseline metrics set")

    def get_summary_report(self, df: pd.DataFrame) -> Dict:
        """
        Generate comprehensive summary report

        Args:
            df: DataFrame with prediction logs

        Returns:
            Dictionary with summary report
        """
        try:
            report = {
                'timestamp': datetime.now().isoformat(),
                'time_range': {},
                'performance': {},
                'alerts': [],
                'trends': {}
            }

            if df.empty:
                report['status'] = 'no_data'
                return report

            # Time range
            if 'timestamp' in df.columns:
                df['timestamp'] = pd.to_datetime(df['timestamp'])
                report['time_range'] = {
                    'start': df['timestamp'].min().isoformat(),
                    'end': df['timestamp'].max().isoformat(),
                    'duration_hours': (df['timestamp'].max() - df['timestamp'].min()).total_seconds() / 3600
                }

            # Performance metrics
            report['performance'] = self.calculate_performance_metrics(df)

            # Generate alerts
            report['alerts'] = self.generate_alerts(report['performance'])

            # Calculate trends
            if 'confidence' in df.columns:
                report['trends']['confidence'] = self.calculate_trend(df, 'confidence')

            report['status'] = 'success'
            return report

        except Exception as e:
            logger.error(f"Failed to generate summary report: {e}")
            return {'status': 'error', 'error': str(e)}


# Example usage and testing
if __name__ == "__main__":
    # Create sample data
    sample_data = {
        'timestamp': pd.date_range(start='2024-01-01', periods=100, freq='H'),
        'sentiment': np.random.choice(['positive', 'negative', 'neutral'], 100, p=[0.5, 0.3, 0.2]),
        'confidence': np.random.beta(8, 2, 100),
        'text_length': np.random.randint(50, 500, 100),
        'word_count': np.random.randint(10, 100, 100)
    }

    df = pd.DataFrame(sample_data)

    # Initialize calculator
    calc = MetricsCalculator()

    # Calculate metrics
    print("Performance Metrics:")
    metrics = calc.calculate_performance_metrics(df)
    for key, value in metrics.items():
        if isinstance(value, float):
            print(f"  {key}: {value:.4f}")
        else:
            print(f"  {key}: {value}")

    # Generate alerts
    print("\nAlerts:")
    alerts = calc.generate_alerts(metrics)
    if alerts:
        for alert in alerts:
            print(f"  [{alert['severity'].upper()}] {alert['message']}")
    else:
        print("  No alerts")

    # Calculate trends
    print("\nTrends:")
    confidence_trend = calc.calculate_trend(df, 'confidence')
    print(f"  Confidence trend: {confidence_trend['trend']} ({confidence_trend['change']:.2%})")

    # Generate summary report
    print("\nSummary Report:")
    report = calc.get_summary_report(df)
    print(f"  Status: {report['status']}")
    print(f"  Total predictions: {report['performance'].get('total_predictions', 0)}")
    print(f"  Avg confidence: {report['performance'].get('avg_confidence', 0):.2%}")
