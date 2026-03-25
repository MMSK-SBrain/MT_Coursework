"""
A/B Testing Framework for ML Models
Handles traffic splitting, experiment tracking, and statistical analysis.

Author: ML for Engineers Course
Date: 2024
"""

import random
import json
from datetime import datetime
from typing import Dict, Any, List, Optional, Tuple
from collections import defaultdict
import numpy as np
from scipy import stats
import hashlib


class ABTest:
    """
    A/B testing framework for machine learning models.

    Features:
    - Multiple variant support (A/B/C/... testing)
    - Weighted traffic splitting
    - Consistent user assignment (sticky sessions)
    - Experiment tracking and results storage
    - Statistical significance testing
    """

    def __init__(
        self,
        experiment_name: str,
        variants: Dict[str, Any],
        weights: Optional[Dict[str, float]] = None,
        sticky: bool = True
    ):
        """
        Initialize A/B test.

        Args:
            experiment_name: Unique name for this experiment
            variants: Dictionary of {variant_name: model/config}
            weights: Dictionary of {variant_name: weight} (must sum to 1.0)
            sticky: If True, same user_id always gets same variant
        """
        self.experiment_name = experiment_name
        self.variants = variants
        self.sticky = sticky

        # Default to equal weights
        if weights is None:
            n = len(variants)
            self.weights = {v: 1.0/n for v in variants}
        else:
            self.weights = weights

        # Validate weights
        if abs(sum(self.weights.values()) - 1.0) > 1e-6:
            raise ValueError(f"Weights must sum to 1.0, got {sum(self.weights.values())}")

        # Tracking
        self.results = {v: [] for v in variants}
        self.assignments = {}  # user_id -> variant
        self.metadata = {
            'experiment_name': experiment_name,
            'created_at': datetime.now().isoformat(),
            'variants': list(variants.keys()),
            'weights': self.weights
        }

    def assign_variant(self, user_id: Optional[str] = None) -> str:
        """
        Assign a variant for this request.

        Args:
            user_id: Optional user identifier for sticky sessions

        Returns:
            variant_name: Assigned variant
        """
        # Sticky assignment: check if user was assigned before
        if self.sticky and user_id is not None:
            if user_id in self.assignments:
                return self.assignments[user_id]

        # Deterministic assignment based on user_id hash
        if self.sticky and user_id is not None:
            # Hash user_id to get consistent random value
            hash_val = int(hashlib.md5(str(user_id).encode()).hexdigest(), 16)
            rand = (hash_val % 10000) / 10000.0
        else:
            # Random assignment
            rand = random.random()

        # Weighted random selection
        cumsum = 0.0
        for variant, weight in self.weights.items():
            cumsum += weight
            if rand < cumsum:
                if self.sticky and user_id is not None:
                    self.assignments[user_id] = variant
                return variant

        # Fallback (shouldn't happen)
        return list(self.variants.keys())[-1]

    def predict(self, X: Any, user_id: Optional[str] = None) -> Tuple[Any, str]:
        """
        Make prediction using assigned variant.

        Args:
            X: Input features
            user_id: Optional user identifier

        Returns:
            (prediction, variant_used)
        """
        variant = self.assign_variant(user_id)
        model = self.variants[variant]

        # Make prediction (assumes model has predict method)
        if hasattr(model, 'predict'):
            prediction = model.predict([X])[0]
        else:
            # Fallback for non-sklearn models
            prediction = model(X)

        return prediction, variant

    def record_result(
        self,
        variant: str,
        prediction: Any,
        ground_truth: Optional[Any] = None,
        metadata: Optional[Dict] = None
    ):
        """
        Record result for a variant.

        Args:
            variant: Variant name
            prediction: Model prediction
            ground_truth: Actual value (if available)
            metadata: Additional metadata
        """
        result = {
            'timestamp': datetime.now().isoformat(),
            'prediction': float(prediction),
            'ground_truth': float(ground_truth) if ground_truth is not None else None,
            'metadata': metadata
        }
        self.results[variant].append(result)

    def get_statistics(self) -> Dict[str, Any]:
        """
        Get statistics for each variant.

        Returns:
            Dictionary with statistics per variant
        """
        stats_dict = {}

        for variant, results in self.results.items():
            if not results:
                stats_dict[variant] = {'count': 0}
                continue

            predictions = [r['prediction'] for r in results]

            stats_dict[variant] = {
                'count': len(results),
                'mean': float(np.mean(predictions)),
                'std': float(np.std(predictions)),
                'min': float(np.min(predictions)),
                'max': float(np.max(predictions)),
                'median': float(np.median(predictions))
            }

            # If ground truth available, calculate errors
            ground_truths = [r['ground_truth'] for r in results if r['ground_truth'] is not None]
            if ground_truths:
                predictions_with_truth = [r['prediction'] for r in results if r['ground_truth'] is not None]
                errors = np.abs(np.array(predictions_with_truth) - np.array(ground_truths))

                stats_dict[variant]['mae'] = float(np.mean(errors))
                stats_dict[variant]['rmse'] = float(np.sqrt(np.mean(errors**2)))

        return stats_dict

    def save_results(self, filepath: str):
        """Save experiment results to JSON file."""
        results_data = {
            'metadata': self.metadata,
            'statistics': self.get_statistics(),
            'results': self.results,
            'total_assignments': sum(len(r) for r in self.results.values())
        }

        with open(filepath, 'w') as f:
            json.dump(results_data, f, indent=2)

        print(f"Results saved to {filepath}")

    @classmethod
    def load_results(cls, filepath: str) -> Dict[str, Any]:
        """Load experiment results from JSON file."""
        with open(filepath, 'r') as f:
            return json.load(f)


class MultiArmedBandit:
    """
    Multi-armed bandit for dynamic traffic allocation.
    Automatically shifts traffic to better-performing variants.
    """

    def __init__(
        self,
        variants: Dict[str, Any],
        epsilon: float = 0.1,
        window_size: int = 100
    ):
        """
        Initialize multi-armed bandit.

        Args:
            variants: Dictionary of {variant_name: model}
            epsilon: Exploration rate (0-1)
            window_size: Number of recent results to consider
        """
        self.variants = variants
        self.epsilon = epsilon
        self.window_size = window_size
        self.results = {v: [] for v in variants}
        self.pulls = {v: 0 for v in variants}

    def select_variant(self) -> str:
        """
        Select variant using epsilon-greedy strategy.

        Returns:
            variant_name: Selected variant
        """
        # Exploration: random selection
        if random.random() < self.epsilon:
            return random.choice(list(self.variants.keys()))

        # Exploitation: choose best performing
        # If not enough data, return random
        if all(self.pulls[v] < 10 for v in self.variants):
            return random.choice(list(self.variants.keys()))

        # Calculate average reward (negative error = reward)
        avg_rewards = {}
        for variant in self.variants:
            if self.results[variant]:
                recent = self.results[variant][-self.window_size:]
                avg_rewards[variant] = np.mean(recent)
            else:
                avg_rewards[variant] = float('-inf')

        # Return variant with highest reward
        return max(avg_rewards, key=avg_rewards.get)

    def update(self, variant: str, reward: float):
        """
        Update bandit with result.

        Args:
            variant: Variant that was used
            reward: Reward value (higher is better)
        """
        self.pulls[variant] += 1
        self.results[variant].append(reward)

    def get_statistics(self) -> Dict[str, Any]:
        """Get statistics for each variant."""
        stats = {}
        for variant in self.variants:
            if self.results[variant]:
                stats[variant] = {
                    'pulls': self.pulls[variant],
                    'avg_reward': float(np.mean(self.results[variant])),
                    'std_reward': float(np.std(self.results[variant])),
                    'selection_rate': self.pulls[variant] / sum(self.pulls.values())
                }
            else:
                stats[variant] = {
                    'pulls': 0,
                    'avg_reward': 0.0,
                    'std_reward': 0.0,
                    'selection_rate': 0.0
                }
        return stats


# Example usage
if __name__ == "__main__":
    from sklearn.linear_model import Ridge
    from sklearn.ensemble import RandomForestRegressor
    import numpy as np

    # Generate sample data
    np.random.seed(42)
    X_train = np.random.randn(1000, 5)
    y_train = X_train[:, 0] * 2 + X_train[:, 1] * -1 + np.random.randn(1000) * 0.5

    # Train models
    model_a = Ridge(alpha=1.0)
    model_a.fit(X_train, y_train)

    model_b = RandomForestRegressor(n_estimators=50, random_state=42)
    model_b.fit(X_train, y_train)

    # Create A/B test
    ab_test = ABTest(
        experiment_name='model_comparison_v1_v2',
        variants={'v1.0.0': model_a, 'v1.1.0': model_b},
        weights={'v1.0.0': 0.5, 'v1.1.0': 0.5},
        sticky=True
    )

    print("Running A/B test simulation...\n")

    # Simulate traffic
    for i in range(500):
        user_id = f"user_{i % 100}"  # 100 unique users
        x_test = np.random.randn(5)
        y_test = x_test[0] * 2 + x_test[1] * -1 + np.random.randn() * 0.5

        # Make prediction
        pred, variant = ab_test.predict(x_test, user_id=user_id)

        # Record result
        ab_test.record_result(variant, pred, ground_truth=y_test)

    # Get statistics
    print("A/B Test Results:")
    print("=" * 60)
    stats = ab_test.get_statistics()
    for variant, s in stats.items():
        print(f"\n{variant}:")
        print(f"  Count: {s['count']}")
        print(f"  Mean prediction: {s['mean']:.3f}")
        if 'mae' in s:
            print(f"  MAE: {s['mae']:.3f}")
            print(f"  RMSE: {s['rmse']:.3f}")

    # Save results
    ab_test.save_results('ab_test_results.json')
    print("\n" + "=" * 60)
