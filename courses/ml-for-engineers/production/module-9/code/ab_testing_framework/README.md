# A/B Testing Framework for ML Models

A comprehensive framework for safely deploying and testing machine learning model updates in production.

## Overview

This framework provides tools and procedures for:
- Running A/B tests between model versions
- Statistical comparison of model performance
- Gradual rollout strategies (canary deployment)
- Automated rollback on performance degradation
- Multi-armed bandit optimization

## Features

### Core Capabilities

1. **A/B Testing**
   - Multi-variant support (A/B/C/... testing)
   - Weighted traffic splitting
   - Sticky sessions (consistent user assignment)
   - Result tracking and analysis

2. **Statistical Analysis**
   - T-tests, KS tests for significance
   - Effect size calculation (Cohen's d)
   - Bootstrap resampling
   - Sample size calculation

3. **Deployment Strategies**
   - Canary deployment (5% → 25% → 50% → 100%)
   - Blue-green deployment
   - Multi-armed bandit optimization
   - Automated rollback

4. **Performance Monitoring**
   - Prediction tracking
   - Error rate monitoring
   - Latency measurement
   - Business metric tracking

## Installation

```bash
# Core dependencies
pip install numpy scipy pandas scikit-learn

# Optional: for visualization
pip install matplotlib seaborn plotly
```

## Quick Start

### 1. Basic A/B Test

```python
from ab_test import ABTest
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import Ridge

# Train models
model_v1 = Ridge(alpha=1.0)
model_v1.fit(X_train, y_train)

model_v2 = RandomForestRegressor(n_estimators=100)
model_v2.fit(X_train, y_train)

# Create A/B test
ab_test = ABTest(
    experiment_name='model_v1_vs_v2',
    variants={
        'v1.0.0': model_v1,
        'v1.1.0': model_v2
    },
    weights={
        'v1.0.0': 0.5,
        'v1.1.0': 0.5
    }
)

# Make predictions
for user_id, features in user_requests:
    prediction, variant = ab_test.predict(features, user_id=user_id)

    # Record result when ground truth available
    if ground_truth is not None:
        ab_test.record_result(variant, prediction, ground_truth)

# Get statistics
stats = ab_test.get_statistics()
print(stats)

# Save results
ab_test.save_results('experiment_results.json')
```

### 2. Statistical Comparison

```python
from model_comparison import ModelComparison

# Compare models
comparison = ModelComparison.compare_two_models(
    predictions_a=predictions_v1,
    predictions_b=predictions_v2,
    ground_truth_a=actual_values_v1,
    ground_truth_b=actual_values_v2
)

# View results
print(f"Winner: {comparison['error_comparison']['winner']}")
print(f"Improvement: {comparison['error_comparison']['improvement_pct']:.1f}%")
print(f"Recommendation: {comparison['recommendation']}")
```

### 3. Canary Deployment

```python
from ab_test import ABTest

# Start with 5% canary traffic
canary = ABTest(
    experiment_name='v2_canary',
    variants={'v1': model_v1, 'v2': model_v2},
    weights={'v1': 0.95, 'v2': 0.05}
)

# After monitoring, increase traffic
canary.weights = {'v1': 0.75, 'v2': 0.25}

# Continue monitoring and increase
canary.weights = {'v1': 0.50, 'v2': 0.50}

# Finally, full rollout
canary.weights = {'v1': 0.00, 'v2': 1.00}
```

## Components

### ab_test.py

Main A/B testing class with traffic routing and experiment tracking.

**Key Classes:**
- `ABTest`: Core A/B testing framework
- `MultiArmedBandit`: Dynamic traffic allocation

**Features:**
- Sticky sessions (consistent user assignment)
- Weighted random selection
- Result tracking with metadata
- JSON export/import

### model_comparison.py

Statistical tools for comparing model performance.

**Key Functions:**
- `compare_two_models()`: Comprehensive statistical comparison
- `calculate_sample_size()`: Power analysis
- `bootstrap_comparison()`: Resampling-based comparison

**Statistical Tests:**
- T-test for mean differences
- Kolmogorov-Smirnov test for distribution differences
- Cohen's d effect size
- Bootstrap confidence intervals

### deployment_strategy.md

Comprehensive guide for production model deployment.

**Covers:**
- 4-phase deployment process
- Rollback procedures
- Decision frameworks
- Communication templates
- Risk assessment

## Usage Examples

### Example 1: Simple 50/50 A/B Test

```python
import numpy as np
from ab_test import ABTest
from model_comparison import ModelComparison

# Setup
ab_test = ABTest(
    experiment_name='homepage_model_test',
    variants={'control': model_a, 'treatment': model_b},
    weights={'control': 0.5, 'treatment': 0.5}
)

# Run test
for i in range(1000):
    user_id = f"user_{i}"
    features = generate_features()

    prediction, variant = ab_test.predict(features, user_id)

    # Simulate getting ground truth
    actual_value = simulate_user_behavior()
    ab_test.record_result(variant, prediction, actual_value)

# Analyze
stats = ab_test.get_statistics()

# Statistical comparison
predictions_a = [r['prediction'] for r in ab_test.results['control']]
predictions_b = [r['prediction'] for r in ab_test.results['treatment']]
truth_a = [r['ground_truth'] for r in ab_test.results['control']]
truth_b = [r['ground_truth'] for r in ab_test.results['treatment']]

comparison = ModelComparison.compare_two_models(
    predictions_a, predictions_b,
    truth_a, truth_b
)

print(comparison['recommendation'])
```

### Example 2: Canary Deployment with Monitoring

```python
from ab_test import ABTest
import time

class CanaryDeployment:
    def __init__(self, old_model, new_model):
        self.ab_test = ABTest(
            experiment_name='canary',
            variants={'old': old_model, 'new': new_model},
            weights={'old': 0.95, 'new': 0.05}
        )
        self.stages = [0.05, 0.25, 0.50, 1.00]
        self.current_stage = 0

    def check_metrics(self):
        """Check if metrics are healthy."""
        stats = self.ab_test.get_statistics()

        # Check error rates, latency, etc.
        if 'mae' in stats['new']:
            new_mae = stats['new']['mae']
            old_mae = stats['old']['mae']

            # Rollback if new model is significantly worse
            if new_mae > old_mae * 1.1:
                return False, "New model has 10%+ worse MAE"

        return True, "Metrics healthy"

    def increase_traffic(self):
        """Move to next deployment stage."""
        if self.current_stage >= len(self.stages):
            print("Already at 100%")
            return

        # Check metrics before increasing
        healthy, reason = self.check_metrics()
        if not healthy:
            print(f"❌ Rollback: {reason}")
            self.rollback()
            return

        # Increase traffic
        new_weight = self.stages[self.current_stage]
        self.ab_test.weights = {
            'old': 1.0 - new_weight,
            'new': new_weight
        }

        self.current_stage += 1
        print(f"✅ Increased to {new_weight*100:.0f}% new model traffic")

    def rollback(self):
        """Emergency rollback to old model."""
        self.ab_test.weights = {'old': 1.0, 'new': 0.0}
        print("🔄 Rolled back to old model")

# Usage
canary = CanaryDeployment(old_model, new_model)

# Gradually increase over days
for day in range(7):
    print(f"\nDay {day+1}:")

    # Simulate traffic
    for _ in range(100):
        pred, variant = canary.ab_test.predict(features)
        canary.ab_test.record_result(variant, pred, actual)

    # Check and possibly increase traffic
    if day % 2 == 1:  # Every other day
        canary.increase_traffic()
```

### Example 3: Multi-Armed Bandit

```python
from ab_test import MultiArmedBandit

# Create bandit with 3 models
bandit = MultiArmedBandit(
    variants={
        'model_a': model_a,
        'model_b': model_b,
        'model_c': model_c
    },
    epsilon=0.1  # 10% exploration, 90% exploitation
)

# Run traffic
for i in range(1000):
    # Select variant (automatically balances exploration/exploitation)
    variant = bandit.select_variant()
    model = bandit.variants[variant]

    # Make prediction
    prediction = model.predict([features])[0]

    # Get reward (negative error = higher reward)
    error = abs(prediction - actual_value)
    reward = -error

    # Update bandit
    bandit.update(variant, reward)

# Check final distribution
stats = bandit.get_statistics()
for variant, s in stats.items():
    print(f"{variant}: {s['selection_rate']*100:.1f}% traffic, "
          f"avg reward: {s['avg_reward']:.3f}")
```

## Best Practices

### 1. Sample Size

Always calculate required sample size before starting:

```python
required_n = ModelComparison.calculate_sample_size(
    baseline_mean=current_mae,
    min_detectable_effect=0.05,  # Want to detect 5% improvement
    std=current_std,
    alpha=0.05,
    power=0.8
)

print(f"Need {required_n} samples per variant")
print(f"Total: {required_n * 2} predictions")
```

### 2. Sticky Sessions

Use sticky sessions to ensure users get consistent experience:

```python
ab_test = ABTest(
    experiment_name='test',
    variants={'a': model_a, 'b': model_b},
    weights={'a': 0.5, 'b': 0.5},
    sticky=True  # Same user always gets same variant
)
```

### 3. Monitor Continuously

Set up automated monitoring:

```python
def check_ab_test_health(ab_test):
    """Check if A/B test is healthy."""
    stats = ab_test.get_statistics()

    issues = []

    # Check sample sizes
    for variant, s in stats.items():
        if s['count'] < 100:
            issues.append(f"{variant} has insufficient samples")

    # Check for anomalies
    if 'error_comparison' in stats:
        if stats['error_comparison']['model_b_mae'] > stats['error_comparison']['model_a_mae'] * 1.2:
            issues.append("New model is 20%+ worse")

    return len(issues) == 0, issues

# Run periodically
healthy, issues = check_ab_test_health(ab_test)
if not healthy:
    alert_team(issues)
```

### 4. Document Everything

Always save experiment results:

```python
# Save results with metadata
ab_test.metadata.update({
    'hypothesis': 'New model will improve MAE by 5%',
    'owner': 'ML Team',
    'start_date': '2024-01-15',
    'end_date': '2024-01-22',
    'decision': 'Deploy new model',
    'reason': 'Statistically significant 7% improvement'
})

ab_test.save_results('experiments/2024-01-15_model_v2_test.json')
```

## Deployment Workflow

Follow this workflow for safe deployments:

```
1. Offline Evaluation
   ├─ Train new model
   ├─ Validate on test set
   └─ Meets baseline? → Continue

2. Canary (5% traffic, 1-2 days)
   ├─ Monitor error rates
   ├─ Check latency
   └─ No issues? → Continue

3. A/B Test (50% traffic, 3-7 days)
   ├─ Collect sufficient samples
   ├─ Statistical analysis
   └─ Significantly better? → Continue

4. Gradual Rollout
   ├─ 75% (1 day)
   ├─ 90% (1 day)
   └─ 100% (monitor for 2 weeks)

5. Production
   ├─ Update documentation
   ├─ Archive old model
   └─ Plan next iteration
```

See `deployment_strategy.md` for detailed procedures.

## Rollback Procedures

### Automatic Rollback

Automatically rollback on critical issues:

```python
class AutoRollback:
    def __init__(self, ab_test, thresholds):
        self.ab_test = ab_test
        self.thresholds = thresholds

    def check_and_rollback(self):
        stats = self.ab_test.get_statistics()

        # Check error rate
        if stats['new']['mae'] > stats['old']['mae'] * self.thresholds['max_mae_ratio']:
            self.rollback("MAE degradation")
            return True

        # Check sample count (traffic drop)
        if stats['new']['count'] < self.thresholds['min_samples']:
            self.rollback("Insufficient traffic")
            return True

        return False

    def rollback(self, reason):
        self.ab_test.weights = {'old': 1.0, 'new': 0.0}
        print(f"🚨 ROLLBACK: {reason}")
        # Send alert, log incident, etc.

# Usage
rollback_system = AutoRollback(
    ab_test,
    thresholds={
        'max_mae_ratio': 1.1,  # Max 10% worse
        'min_samples': 50
    }
)

# Check periodically
if rollback_system.check_and_rollback():
    # Handle rollback
    notify_team()
```

## Troubleshooting

### Issue: Not enough statistical power

**Solution:** Calculate and wait for required sample size

```python
# Check current power
from scipy.stats import ttest_ind_from_stats

current_power = calculate_power(
    mean1=stats['a']['mean'],
    std1=stats['a']['std'],
    n1=stats['a']['count'],
    mean2=stats['b']['mean'],
    std2=stats['b']['std'],
    n2=stats['b']['count'],
    alpha=0.05
)

if current_power < 0.8:
    print(f"Current power: {current_power:.2f}, need more data")
```

### Issue: Inconsistent user experience

**Solution:** Enable sticky sessions

```python
ab_test = ABTest(..., sticky=True)
```

### Issue: Can't decide winner

**Solution:** Use bootstrap comparison for robust analysis

```python
bootstrap_result = ModelComparison.bootstrap_comparison(
    predictions_a,
    predictions_b,
    metric_fn=np.mean,
    n_bootstrap=10000
)

print(bootstrap_result['interpretation'])
```

## Resources

- [A/B Testing Methodology](https://www.exp-platform.com/)
- [Statistical Power Analysis](https://www.statsmodels.org/stable/stats.html)
- [Multi-Armed Bandits](https://lilianweng.github.io/posts/2018-01-23-multi-armed-bandit/)
- Course: Session 9.6 - A/B Testing & Model Updates

## License

MIT License - see course materials for details.
