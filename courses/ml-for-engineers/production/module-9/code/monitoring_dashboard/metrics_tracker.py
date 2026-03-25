"""
Metrics Tracker
Performance tracking and alerting for ML models in production.

Author: ML for Engineers Course
Date: 2024
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
from scipy import stats
import warnings


class MetricsTracker:
    """
    Track and analyze ML model performance metrics.

    Features:
    - Calculate performance metrics
    - Detect drift (data and concept)
    - Generate alerts
    - Track model degradation
    """

    def __init__(self, logger):
        """
        Initialize metrics tracker.

        Args:
            logger: PredictionLogger instance
        """
        self.logger = logger
        self.alerts = []

    def calculate_daily_metrics(
        self,
        start_date: str,
        end_date: str
    ) -> pd.DataFrame:
        """
        Calculate daily aggregated metrics.

        Args:
            start_date: Start date (ISO format)
            end_date: End date (ISO format)

        Returns:
            DataFrame with daily metrics
        """
        df = self.logger.get_predictions_by_date_range(start_date, end_date)

        if len(df) == 0:
            return pd.DataFrame()

        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df['date'] = df['timestamp'].dt.date

        # Aggregate by date
        daily_metrics = df.groupby('date').agg({
            'prediction': ['count', 'mean', 'std', 'min', 'max'],
            'confidence': ['mean', 'std', 'min'],
            'response_time_ms': ['mean', 'median', lambda x: x.quantile(0.95), lambda x: x.quantile(0.99)]
        }).reset_index()

        # Flatten column names
        daily_metrics.columns = [
            'date',
            'prediction_count', 'prediction_mean', 'prediction_std', 'prediction_min', 'prediction_max',
            'confidence_mean', 'confidence_std', 'confidence_min',
            'response_mean', 'response_median', 'response_p95', 'response_p99'
        ]

        return daily_metrics

    def detect_data_drift(
        self,
        baseline_days: int = 7,
        recent_days: int = 7,
        significance_level: float = 0.05
    ) -> Dict[str, any]:
        """
        Detect data drift using statistical tests.

        Args:
            baseline_days: Number of days for baseline period
            recent_days: Number of days for recent period
            significance_level: P-value threshold for significance

        Returns:
            Dictionary with drift detection results
        """
        end_date = datetime.now()
        recent_start = end_date - timedelta(days=recent_days)
        baseline_end = recent_start
        baseline_start = baseline_end - timedelta(days=baseline_days)

        # Get data
        df_baseline = self.logger.get_predictions_by_date_range(
            baseline_start.isoformat(),
            baseline_end.isoformat()
        )
        df_recent = self.logger.get_predictions_by_date_range(
            recent_start.isoformat(),
            end_date.isoformat()
        )

        if len(df_baseline) < 30 or len(df_recent) < 30:
            return {
                'drift_detected': None,
                'message': 'Insufficient data for drift detection (minimum 30 predictions per period)'
            }

        # Kolmogorov-Smirnov test for distribution difference
        ks_statistic, ks_pvalue = stats.ks_2samp(
            df_baseline['prediction'],
            df_recent['prediction']
        )

        # T-test for mean difference
        t_statistic, t_pvalue = stats.ttest_ind(
            df_baseline['prediction'],
            df_recent['prediction']
        )

        # Effect size (Cohen's d)
        mean_diff = df_recent['prediction'].mean() - df_baseline['prediction'].mean()
        pooled_std = np.sqrt(
            (df_baseline['prediction'].std()**2 + df_recent['prediction'].std()**2) / 2
        )
        cohens_d = mean_diff / pooled_std if pooled_std > 0 else 0

        drift_detected = ks_pvalue < significance_level or t_pvalue < significance_level

        result = {
            'drift_detected': drift_detected,
            'ks_test': {
                'statistic': float(ks_statistic),
                'pvalue': float(ks_pvalue),
                'significant': ks_pvalue < significance_level
            },
            't_test': {
                'statistic': float(t_statistic),
                'pvalue': float(t_pvalue),
                'significant': t_pvalue < significance_level
            },
            'effect_size': {
                'cohens_d': float(cohens_d),
                'interpretation': self._interpret_cohens_d(cohens_d)
            },
            'baseline': {
                'n': len(df_baseline),
                'mean': float(df_baseline['prediction'].mean()),
                'std': float(df_baseline['prediction'].std()),
                'period': f"{baseline_start.date()} to {baseline_end.date()}"
            },
            'recent': {
                'n': len(df_recent),
                'mean': float(df_recent['prediction'].mean()),
                'std': float(df_recent['prediction'].std()),
                'period': f"{recent_start.date()} to {end_date.date()}"
            },
            'mean_shift': {
                'absolute': float(mean_diff),
                'relative_pct': float(mean_diff / df_baseline['prediction'].mean() * 100) if df_baseline['prediction'].mean() != 0 else 0
            }
        }

        return result

    def check_confidence_degradation(
        self,
        window_days: int = 7,
        threshold: float = 0.7,
        drop_threshold: float = 0.15
    ) -> Dict[str, any]:
        """
        Check if model confidence has degraded.

        Args:
            window_days: Days to analyze
            threshold: Minimum acceptable average confidence
            drop_threshold: Maximum acceptable drop from baseline

        Returns:
            Dictionary with confidence analysis
        """
        end_date = datetime.now()
        start_date = end_date - timedelta(days=window_days)
        baseline_start = start_date - timedelta(days=window_days)

        df_current = self.logger.get_predictions_by_date_range(
            start_date.isoformat(),
            end_date.isoformat()
        )

        df_baseline = self.logger.get_predictions_by_date_range(
            baseline_start.isoformat(),
            start_date.isoformat()
        )

        if len(df_current) == 0:
            return {
                'degradation_detected': None,
                'message': 'No recent data available'
            }

        current_avg = df_current['confidence'].mean()
        baseline_avg = df_baseline['confidence'].mean() if len(df_baseline) > 0 else current_avg

        drop = baseline_avg - current_avg
        drop_pct = drop / baseline_avg if baseline_avg > 0 else 0

        degradation_detected = current_avg < threshold or drop_pct > drop_threshold

        return {
            'degradation_detected': degradation_detected,
            'current_confidence': float(current_avg),
            'baseline_confidence': float(baseline_avg),
            'drop': {
                'absolute': float(drop),
                'relative_pct': float(drop_pct * 100)
            },
            'thresholds': {
                'minimum_confidence': threshold,
                'maximum_drop_pct': drop_threshold * 100
            },
            'severity': 'HIGH' if current_avg < 0.6 else 'MEDIUM' if current_avg < threshold else 'LOW'
        }

    def check_volume_anomaly(
        self,
        window_days: int = 7,
        std_threshold: float = 2.5
    ) -> Dict[str, any]:
        """
        Detect anomalies in request volume.

        Args:
            window_days: Days to analyze
            std_threshold: Number of standard deviations for anomaly

        Returns:
            Dictionary with volume analysis
        """
        end_date = datetime.now()
        start_date = end_date - timedelta(days=window_days)

        df = self.logger.get_predictions_by_date_range(
            start_date.isoformat(),
            end_date.isoformat()
        )

        if len(df) == 0:
            return {
                'anomaly_detected': None,
                'message': 'No data available'
            }

        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df['date'] = df['timestamp'].dt.date
        daily_counts = df.groupby('date').size()

        if len(daily_counts) < 2:
            return {
                'anomaly_detected': None,
                'message': 'Insufficient data for anomaly detection'
            }

        mean_count = daily_counts.mean()
        std_count = daily_counts.std()
        today_count = daily_counts.iloc[-1]

        z_score = abs(today_count - mean_count) / (std_count + 1e-6)
        anomaly_detected = z_score > std_threshold

        return {
            'anomaly_detected': anomaly_detected,
            'today_count': int(today_count),
            'historical_mean': float(mean_count),
            'historical_std': float(std_count),
            'z_score': float(z_score),
            'threshold': std_threshold,
            'severity': 'HIGH' if z_score > 3 else 'MEDIUM' if z_score > std_threshold else 'LOW',
            'anomaly_type': 'SPIKE' if today_count > mean_count else 'DROP'
        }

    def check_response_time(
        self,
        window_days: int = 1,
        p95_threshold_ms: float = 1000,
        p99_threshold_ms: float = 2000
    ) -> Dict[str, any]:
        """
        Check if response times are acceptable.

        Args:
            window_days: Days to analyze
            p95_threshold_ms: P95 threshold in milliseconds
            p99_threshold_ms: P99 threshold in milliseconds

        Returns:
            Dictionary with response time analysis
        """
        end_date = datetime.now()
        start_date = end_date - timedelta(days=window_days)

        df = self.logger.get_predictions_by_date_range(
            start_date.isoformat(),
            end_date.isoformat()
        )

        if len(df) == 0 or 'response_time_ms' not in df.columns:
            return {
                'issue_detected': None,
                'message': 'No response time data available'
            }

        p50 = df['response_time_ms'].quantile(0.50)
        p95 = df['response_time_ms'].quantile(0.95)
        p99 = df['response_time_ms'].quantile(0.99)
        mean_time = df['response_time_ms'].mean()

        p95_issue = p95 > p95_threshold_ms
        p99_issue = p99 > p99_threshold_ms

        return {
            'issue_detected': p95_issue or p99_issue,
            'metrics': {
                'mean': float(mean_time),
                'p50': float(p50),
                'p95': float(p95),
                'p99': float(p99)
            },
            'thresholds': {
                'p95': p95_threshold_ms,
                'p99': p99_threshold_ms
            },
            'violations': {
                'p95_exceeded': p95_issue,
                'p99_exceeded': p99_issue
            },
            'severity': 'HIGH' if p99_issue else 'MEDIUM' if p95_issue else 'LOW'
        }

    def generate_health_report(self) -> Dict[str, any]:
        """
        Generate comprehensive health report for the model.

        Returns:
            Dictionary with complete health assessment
        """
        print("Generating health report...")

        # Run all checks
        drift_result = self.detect_data_drift()
        confidence_result = self.check_confidence_degradation()
        volume_result = self.check_volume_anomaly()
        response_result = self.check_response_time()

        # Determine overall status
        issues = []
        if drift_result.get('drift_detected'):
            issues.append('DATA_DRIFT')
        if confidence_result.get('degradation_detected'):
            issues.append('CONFIDENCE_DEGRADATION')
        if volume_result.get('anomaly_detected'):
            issues.append('VOLUME_ANOMALY')
        if response_result.get('issue_detected'):
            issues.append('SLOW_RESPONSE')

        overall_status = 'CRITICAL' if len(issues) >= 3 else 'WARNING' if len(issues) > 0 else 'HEALTHY'

        report = {
            'timestamp': datetime.now().isoformat(),
            'overall_status': overall_status,
            'issues_detected': issues,
            'checks': {
                'drift_detection': drift_result,
                'confidence_check': confidence_result,
                'volume_check': volume_result,
                'response_time_check': response_result
            },
            'recommendations': self._generate_recommendations(issues)
        }

        return report

    @staticmethod
    def _interpret_cohens_d(d: float) -> str:
        """Interpret Cohen's d effect size."""
        abs_d = abs(d)
        if abs_d < 0.2:
            return "negligible"
        elif abs_d < 0.5:
            return "small"
        elif abs_d < 0.8:
            return "medium"
        else:
            return "large"

    @staticmethod
    def _generate_recommendations(issues: List[str]) -> List[str]:
        """Generate recommendations based on detected issues."""
        recommendations = []

        if 'DATA_DRIFT' in issues:
            recommendations.append("Consider retraining the model with recent data")
            recommendations.append("Investigate what caused the distribution shift")

        if 'CONFIDENCE_DEGRADATION' in issues:
            recommendations.append("Model confidence is low - retrain with more diverse data")
            recommendations.append("Consider adding new features or improving data quality")

        if 'VOLUME_ANOMALY' in issues:
            recommendations.append("Investigate sudden change in request volume")
            recommendations.append("Check for system issues or unusual traffic patterns")

        if 'SLOW_RESPONSE' in issues:
            recommendations.append("Optimize model inference time")
            recommendations.append("Consider model compression or hardware upgrade")
            recommendations.append("Check for infrastructure bottlenecks")

        if not recommendations:
            recommendations.append("System is healthy - continue monitoring")

        return recommendations


# Example usage
if __name__ == "__main__":
    from logger import PredictionLogger

    # Initialize
    logger = PredictionLogger('test_predictions.db')
    tracker = MetricsTracker(logger)

    # Generate health report
    report = tracker.generate_health_report()

    print("\n" + "="*60)
    print("MODEL HEALTH REPORT")
    print("="*60)
    print(f"Status: {report['overall_status']}")
    print(f"Issues: {', '.join(report['issues_detected']) if report['issues_detected'] else 'None'}")
    print(f"\nRecommendations:")
    for rec in report['recommendations']:
        print(f"  • {rec}")
    print("="*60)
