"""
Model Comparison Tools
Statistical analysis and comparison of ML model performance.

Author: ML for Engineers Course
Date: 2024
"""

import numpy as np
from scipy import stats
from typing import Dict, List, Tuple, Any, Optional
import pandas as pd


class ModelComparison:
    """Compare multiple ML models statistically."""

    @staticmethod
    def compare_two_models(
        predictions_a: List[float],
        predictions_b: List[float],
        ground_truth_a: Optional[List[float]] = None,
        ground_truth_b: Optional[List[float]] = None,
        alpha: float = 0.05
    ) -> Dict[str, Any]:
        """
        Compare two models statistically.

        Args:
            predictions_a: Predictions from model A
            predictions_b: Predictions from model B
            ground_truth_a: Actual values for A (optional)
            ground_truth_b: Actual values for B (optional)
            alpha: Significance level

        Returns:
            Dictionary with comparison results
        """
        results = {}

        # Convert to numpy arrays
        preds_a = np.array(predictions_a)
        preds_b = np.array(predictions_b)

        # Basic statistics
        results['descriptive'] = {
            'model_a': {
                'n': len(preds_a),
                'mean': float(np.mean(preds_a)),
                'std': float(np.std(preds_a)),
                'median': float(np.median(preds_a)),
                'min': float(np.min(preds_a)),
                'max': float(np.max(preds_a))
            },
            'model_b': {
                'n': len(preds_b),
                'mean': float(np.mean(preds_b)),
                'std': float(np.std(preds_b)),
                'median': float(np.median(preds_b)),
                'min': float(np.min(preds_b)),
                'max': float(np.max(preds_b))
            }
        }

        # T-test for mean difference
        t_stat, p_value = stats.ttest_ind(preds_a, preds_b)

        results['t_test'] = {
            'statistic': float(t_stat),
            'p_value': float(p_value),
            'significant': p_value < alpha,
            'alpha': alpha,
            'interpretation': 'Significant difference' if p_value < alpha else 'No significant difference'
        }

        # Effect size (Cohen's d)
        mean_diff = np.mean(preds_b) - np.mean(preds_a)
        pooled_std = np.sqrt((np.var(preds_a) + np.var(preds_b)) / 2)
        cohens_d = mean_diff / pooled_std if pooled_std > 0 else 0

        results['effect_size'] = {
            'cohens_d': float(cohens_d),
            'interpretation': ModelComparison._interpret_cohens_d(cohens_d),
            'mean_difference': float(mean_diff),
            'relative_change_pct': float(mean_diff / np.mean(preds_a) * 100) if np.mean(preds_a) != 0 else 0
        }

        # Kolmogorov-Smirnov test (distribution difference)
        ks_stat, ks_p = stats.ks_2samp(preds_a, preds_b)

        results['ks_test'] = {
            'statistic': float(ks_stat),
            'p_value': float(ks_p),
            'significant': ks_p < alpha,
            'interpretation': 'Different distributions' if ks_p < alpha else 'Similar distributions'
        }

        # If ground truth available, compare errors
        if ground_truth_a is not None and ground_truth_b is not None:
            truth_a = np.array(ground_truth_a)
            truth_b = np.array(ground_truth_b)

            errors_a = np.abs(preds_a - truth_a)
            errors_b = np.abs(preds_b - truth_b)

            # T-test on errors
            t_stat_err, p_value_err = stats.ttest_ind(errors_a, errors_b)

            results['error_comparison'] = {
                'model_a_mae': float(np.mean(errors_a)),
                'model_a_rmse': float(np.sqrt(np.mean(errors_a**2))),
                'model_b_mae': float(np.mean(errors_b)),
                'model_b_rmse': float(np.sqrt(np.mean(errors_b**2))),
                't_statistic': float(t_stat_err),
                'p_value': float(p_value_err),
                'significant': p_value_err < alpha,
                'winner': 'Model B' if np.mean(errors_b) < np.mean(errors_a) else 'Model A',
                'improvement_pct': float((np.mean(errors_a) - np.mean(errors_b)) / np.mean(errors_a) * 100)
            }

        # Recommendation
        results['recommendation'] = ModelComparison._generate_recommendation(results)

        return results

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
    def _generate_recommendation(results: Dict[str, Any]) -> str:
        """Generate deployment recommendation based on results."""
        # Check if there's ground truth comparison
        if 'error_comparison' in results:
            err_comp = results['error_comparison']
            if err_comp['significant'] and err_comp['winner'] == 'Model B':
                improvement = err_comp['improvement_pct']
                if improvement > 10:
                    return f"✅ DEPLOY Model B - Significant improvement ({improvement:.1f}% better MAE)"
                elif improvement > 5:
                    return f"✅ DEPLOY Model B - Moderate improvement ({improvement:.1f}% better MAE)"
                else:
                    return f"⚖️ CONSIDER Model B - Small improvement ({improvement:.1f}% better MAE)"
            elif err_comp['significant'] and err_comp['winner'] == 'Model A':
                return "❌ KEEP Model A - Model B performs worse"
            else:
                return "⚖️ NO CLEAR WINNER - Consider other factors (complexity, cost, latency)"
        else:
            # No ground truth, use prediction comparison
            if results['t_test']['significant']:
                effect = results['effect_size']['interpretation']
                return f"⚠️ SIGNIFICANT DIFFERENCE detected ({effect} effect) - Need ground truth for final decision"
            else:
                return "⚖️ NO SIGNIFICANT DIFFERENCE - Consider keeping simpler model"

    @staticmethod
    def calculate_sample_size(
        baseline_mean: float,
        min_detectable_effect: float,
        std: float,
        alpha: float = 0.05,
        power: float = 0.8
    ) -> int:
        """
        Calculate required sample size for A/B test.

        Args:
            baseline_mean: Current model's mean metric
            min_detectable_effect: Minimum relative improvement to detect (e.g., 0.05 for 5%)
            std: Standard deviation of metric
            alpha: Significance level
            power: Statistical power (1 - beta)

        Returns:
            Required sample size per variant
        """
        from scipy.stats import norm

        # Effect size
        effect_size = (baseline_mean * min_detectable_effect) / std

        # Z-scores
        z_alpha = norm.ppf(1 - alpha/2)
        z_beta = norm.ppf(power)

        # Sample size formula
        n = 2 * ((z_alpha + z_beta) / effect_size) ** 2

        return int(np.ceil(n))

    @staticmethod
    def bootstrap_comparison(
        predictions_a: List[float],
        predictions_b: List[float],
        metric_fn: callable,
        n_bootstrap: int = 1000,
        confidence_level: float = 0.95
    ) -> Dict[str, Any]:
        """
        Compare models using bootstrap resampling.

        Args:
            predictions_a: Predictions from model A
            predictions_b: Predictions from model B
            metric_fn: Function to calculate metric (e.g., np.mean, np.std)
            n_bootstrap: Number of bootstrap samples
            confidence_level: Confidence level for intervals

        Returns:
            Dictionary with bootstrap comparison results
        """
        preds_a = np.array(predictions_a)
        preds_b = np.array(predictions_b)

        # Bootstrap sampling
        bootstrap_diffs = []
        for _ in range(n_bootstrap):
            # Resample with replacement
            sample_a = np.random.choice(preds_a, size=len(preds_a), replace=True)
            sample_b = np.random.choice(preds_b, size=len(preds_b), replace=True)

            # Calculate metric difference
            diff = metric_fn(sample_b) - metric_fn(sample_a)
            bootstrap_diffs.append(diff)

        bootstrap_diffs = np.array(bootstrap_diffs)

        # Confidence interval
        lower_percentile = (1 - confidence_level) / 2 * 100
        upper_percentile = (1 - (1 - confidence_level) / 2) * 100

        ci_lower = np.percentile(bootstrap_diffs, lower_percentile)
        ci_upper = np.percentile(bootstrap_diffs, upper_percentile)

        # P-value (proportion of bootstrap samples where B is not better than A)
        p_value = np.mean(bootstrap_diffs <= 0)

        return {
            'mean_difference': float(np.mean(bootstrap_diffs)),
            'std_difference': float(np.std(bootstrap_diffs)),
            'confidence_interval': {
                'level': confidence_level,
                'lower': float(ci_lower),
                'upper': float(ci_upper)
            },
            'p_value': float(p_value),
            'significant': not (ci_lower <= 0 <= ci_upper),
            'interpretation': 'Model B is significantly better' if ci_lower > 0 else
                            'Model A is significantly better' if ci_upper < 0 else
                            'No significant difference'
        }


# Example usage
if __name__ == "__main__":
    # Generate sample data
    np.random.seed(42)

    # Model A predictions (baseline)
    predictions_a = np.random.normal(100, 10, 500)
    ground_truth_a = np.random.normal(100, 5, 500)

    # Model B predictions (slightly better)
    predictions_b = np.random.normal(102, 9, 500)  # Closer to truth
    ground_truth_b = ground_truth_a  # Same ground truth

    # Compare models
    print("Model Comparison Analysis")
    print("=" * 60)

    comparison = ModelComparison.compare_two_models(
        predictions_a,
        predictions_b,
        ground_truth_a,
        ground_truth_b
    )

    print("\n📊 Descriptive Statistics:")
    print(f"\nModel A:")
    print(f"  Mean: {comparison['descriptive']['model_a']['mean']:.3f}")
    print(f"  Std: {comparison['descriptive']['model_a']['std']:.3f}")

    print(f"\nModel B:")
    print(f"  Mean: {comparison['descriptive']['model_b']['mean']:.3f}")
    print(f"  Std: {comparison['descriptive']['model_b']['std']:.3f}")

    print("\n📈 Statistical Tests:")
    print(f"\nT-Test: {comparison['t_test']['interpretation']}")
    print(f"  p-value: {comparison['t_test']['p_value']:.4f}")

    print(f"\nEffect Size: {comparison['effect_size']['interpretation']}")
    print(f"  Cohen's d: {comparison['effect_size']['cohens_d']:.3f}")

    if 'error_comparison' in comparison:
        print("\n🎯 Error Comparison:")
        print(f"  Model A MAE: {comparison['error_comparison']['model_a_mae']:.3f}")
        print(f"  Model B MAE: {comparison['error_comparison']['model_b_mae']:.3f}")
        print(f"  Winner: {comparison['error_comparison']['winner']}")
        print(f"  Improvement: {comparison['error_comparison']['improvement_pct']:.1f}%")

    print(f"\n💡 Recommendation:")
    print(f"  {comparison['recommendation']}")

    # Bootstrap comparison
    print("\n\n🔄 Bootstrap Analysis:")
    bootstrap_result = ModelComparison.bootstrap_comparison(
        predictions_a,
        predictions_b,
        metric_fn=np.mean,
        n_bootstrap=1000
    )

    print(f"  Mean difference: {bootstrap_result['mean_difference']:.3f}")
    print(f"  95% CI: [{bootstrap_result['confidence_interval']['lower']:.3f}, {bootstrap_result['confidence_interval']['upper']:.3f}]")
    print(f"  Interpretation: {bootstrap_result['interpretation']}")

    print("\n" + "=" * 60)
