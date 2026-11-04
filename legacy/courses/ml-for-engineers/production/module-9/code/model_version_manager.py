"""
Model Version Manager
=====================

A production-ready model versioning system with metadata tracking,
version comparison, and safe loading/saving operations.

Author: ML for Engineers Course
Date: 2026-01-06
"""

import os
import json
import joblib
from datetime import datetime
from typing import Dict, List, Tuple, Optional, Any


class ModelVersion:
    """Semantic versioning for ML models"""

    def __init__(self, major: int = 1, minor: int = 0, patch: int = 0):
        self.major = major
        self.minor = minor
        self.patch = patch

    def __str__(self) -> str:
        return f"v{self.major}.{self.minor}.{self.patch}"

    def increment_major(self):
        """
        Increment major version (breaking changes, complete retrain)
        Resets minor and patch to 0
        """
        self.major += 1
        self.minor = 0
        self.patch = 0

    def increment_minor(self):
        """
        Increment minor version (new features, significant improvements)
        Resets patch to 0
        """
        self.minor += 1
        self.patch = 0

    def increment_patch(self):
        """Increment patch version (bug fixes, minor improvements)"""
        self.patch += 1


class ModelManager:
    """
    Complete model management system with versioning, metadata, and error handling.

    Features:
    - Save/load models with automatic versioning
    - Metadata tracking (metrics, timestamp, description)
    - Model comparison between versions
    - List all available models
    - Safe error handling

    Example:
        >>> manager = ModelManager()
        >>> manager.save(model, 'spam_detector', 'v1.0.0',
        ...             {'accuracy': 0.95}, 'Initial model')
        >>> model, meta = manager.load('spam_detector', 'latest')
    """

    def __init__(self, base_dir: str = 'saved_models'):
        """
        Initialize ModelManager

        Args:
            base_dir: Base directory for storing models
        """
        self.base_dir = base_dir
        os.makedirs(base_dir, exist_ok=True)

    def save(self,
             model: Any,
             name: str,
             version: str,
             metrics: Dict[str, float],
             description: str = "",
             additional_metadata: Optional[Dict] = None) -> str:
        """
        Save model with version and metadata

        Args:
            model: Trained model object (sklearn, keras, etc.)
            name: Model name (e.g., 'spam_detector')
            version: Version string (e.g., 'v1.0.0')
            metrics: Performance metrics dict
            description: Human-readable description
            additional_metadata: Any extra metadata to store

        Returns:
            str: Path to saved model directory
        """
        # Create directory structure
        model_dir = os.path.join(self.base_dir, name, version)
        os.makedirs(model_dir, exist_ok=True)

        # Save model
        model_path = os.path.join(model_dir, 'model.pkl')
        joblib.dump(model, model_path)

        # Create metadata
        metadata = {
            'name': name,
            'version': version,
            'created_at': datetime.now().isoformat(),
            'metrics': metrics,
            'description': description,
            'model_type': type(model).__name__,
            'model_class': str(type(model))
        }

        # Add additional metadata if provided
        if additional_metadata:
            metadata.update(additional_metadata)

        # Save metadata
        metadata_path = os.path.join(model_dir, 'metadata.json')
        with open(metadata_path, 'w') as f:
            json.dump(metadata, f, indent=2)

        print(f"✓ Model saved: {name} {version}")
        print(f"  Location: {model_path}")
        print(f"  Metrics: {metrics}")

        return model_dir

    def load(self,
             name: str,
             version: str = 'latest') -> Tuple[Optional[Any], Optional[Dict]]:
        """
        Load model by name and version

        Args:
            name: Model name
            version: Version string or 'latest' for most recent

        Returns:
            tuple: (model, metadata) or (None, None) if error
        """
        try:
            if version == 'latest':
                # Find latest version
                model_base = os.path.join(self.base_dir, name)
                if not os.path.exists(model_base):
                    raise FileNotFoundError(f"No model found: {name}")

                # Get all version directories
                versions = [d for d in os.listdir(model_base)
                           if os.path.isdir(os.path.join(model_base, d))]

                if not versions:
                    raise FileNotFoundError(f"No versions found for: {name}")

                version = sorted(versions)[-1]  # Get latest
                print(f"Loading latest version: {version}")

            # Load model
            model_path = os.path.join(self.base_dir, name, version, 'model.pkl')
            model = joblib.load(model_path)

            # Load metadata
            metadata_path = os.path.join(self.base_dir, name, version, 'metadata.json')
            with open(metadata_path, 'r') as f:
                metadata = json.load(f)

            print(f"✓ Model loaded: {name} {version}")
            return model, metadata

        except FileNotFoundError as e:
            print(f"✗ Error: {str(e)}")
            return None, None
        except Exception as e:
            print(f"✗ Error loading model: {str(e)}")
            return None, None

    def list_models(self) -> List[Dict[str, Any]]:
        """
        List all saved models and their versions

        Returns:
            List of dicts with model names and versions
        """
        models = []

        if not os.path.exists(self.base_dir):
            return models

        for model_name in os.listdir(self.base_dir):
            model_path = os.path.join(self.base_dir, model_name)

            # Skip files, only process directories
            if not os.path.isdir(model_path):
                continue

            versions = [d for d in os.listdir(model_path)
                       if os.path.isdir(os.path.join(model_path, d))]

            if versions:
                models.append({
                    'name': model_name,
                    'versions': sorted(versions),
                    'latest': sorted(versions)[-1]
                })

        return models

    def compare_versions(self, name: str, version1: str, version2: str) -> None:
        """
        Compare metrics between two model versions

        Args:
            name: Model name
            version1: First version to compare
            version2: Second version to compare
        """
        try:
            # Load metadata for both versions
            meta1_path = os.path.join(self.base_dir, name, version1, 'metadata.json')
            meta2_path = os.path.join(self.base_dir, name, version2, 'metadata.json')

            with open(meta1_path, 'r') as f:
                meta1 = json.load(f)

            with open(meta2_path, 'r') as f:
                meta2 = json.load(f)

            print(f"\n{'='*60}")
            print(f"Comparing {name}: {version1} vs {version2}")
            print(f"{'='*60}")

            # Compare creation dates
            print(f"\nCreated:")
            print(f"  {version1}: {meta1.get('created_at', 'Unknown')}")
            print(f"  {version2}: {meta2.get('created_at', 'Unknown')}")

            # Compare descriptions
            print(f"\nDescription:")
            print(f"  {version1}: {meta1.get('description', 'N/A')}")
            print(f"  {version2}: {meta2.get('description', 'N/A')}")

            # Compare metrics
            print(f"\nMetrics Comparison:")
            metrics1 = meta1.get('metrics', {})
            metrics2 = meta2.get('metrics', {})

            all_metrics = set(metrics1.keys()) | set(metrics2.keys())

            for metric in sorted(all_metrics):
                val1 = metrics1.get(metric, 'N/A')
                val2 = metrics2.get(metric, 'N/A')

                if val1 != 'N/A' and val2 != 'N/A':
                    diff = val2 - val1
                    pct_change = (diff / val1 * 100) if val1 != 0 else 0
                    symbol = '↑' if diff > 0 else '↓' if diff < 0 else '→'
                    print(f"  {metric:15s}: {val1:8.4f} → {val2:8.4f} "
                          f"{symbol} ({pct_change:+6.2f}%)")
                else:
                    print(f"  {metric:15s}: {val1} → {val2}")

            print(f"{'='*60}\n")

        except Exception as e:
            print(f"✗ Error comparing versions: {str(e)}")

    def delete_version(self, name: str, version: str, confirm: bool = False) -> bool:
        """
        Delete a specific model version

        Args:
            name: Model name
            version: Version to delete
            confirm: Must be True to actually delete

        Returns:
            bool: True if deleted successfully
        """
        if not confirm:
            print("⚠ Set confirm=True to actually delete the model")
            return False

        try:
            version_path = os.path.join(self.base_dir, name, version)

            if not os.path.exists(version_path):
                print(f"✗ Version not found: {name} {version}")
                return False

            # Delete directory and all contents
            import shutil
            shutil.rmtree(version_path)

            print(f"✓ Deleted: {name} {version}")
            return True

        except Exception as e:
            print(f"✗ Error deleting version: {str(e)}")
            return False

    def export_metadata(self, name: str, version: str, output_file: str) -> bool:
        """
        Export model metadata to a separate file

        Args:
            name: Model name
            version: Version string
            output_file: Path to output file

        Returns:
            bool: True if exported successfully
        """
        try:
            metadata_path = os.path.join(self.base_dir, name, version, 'metadata.json')

            with open(metadata_path, 'r') as f:
                metadata = json.load(f)

            with open(output_file, 'w') as f:
                json.dump(metadata, f, indent=2)

            print(f"✓ Metadata exported to: {output_file}")
            return True

        except Exception as e:
            print(f"✗ Error exporting metadata: {str(e)}")
            return False


def create_model_card(name: str,
                     version: str,
                     model_info: Dict[str, Any],
                     output_file: Optional[str] = None) -> str:
    """
    Create a model card (documentation) for a model

    Args:
        name: Model name
        version: Version string
        model_info: Dictionary with model information
        output_file: Optional path to save the card

    Returns:
        str: Model card content
    """
    card = f"""# {name} - {version}

## Model Overview
{model_info.get('description', 'No description provided')}

## Model Details
- **Model Type:** {model_info.get('model_type', 'Unknown')}
- **Version:** {version}
- **Created:** {model_info.get('created_at', 'Unknown')}
- **Framework:** {model_info.get('framework', 'scikit-learn')}

## Performance
### Training Metrics
"""

    if 'metrics' in model_info:
        for metric, value in model_info['metrics'].items():
            if isinstance(value, (int, float)):
                card += f"- **{metric}:** {value:.4f}\n"
            else:
                card += f"- **{metric}:** {value}\n"

    card += f"""
## Intended Use
{model_info.get('intended_use', 'General purpose classification/regression')}

## Limitations
{model_info.get('limitations', 'Model may not generalize to data outside training distribution')}

## How to Use
```python
import joblib

# Load model
model = joblib.load('model.pkl')

# Make predictions
predictions = model.predict(X_new)
```

## Training Data
{model_info.get('training_data', 'See documentation for details')}

## Ethical Considerations
{model_info.get('ethical_considerations', 'Standard ML ethical considerations apply')}

## License
{model_info.get('license', 'MIT')}

## Contact
For questions or issues, please contact the model maintainer.
"""

    if output_file:
        with open(output_file, 'w') as f:
            f.write(card)
        print(f"✓ Model card saved to: {output_file}")

    return card


# Example usage
if __name__ == "__main__":
    print("Model Version Manager - Example Usage\n")

    # Create manager
    manager = ModelManager('example_models')

    # Example: Save a dummy model
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.datasets import make_classification

    X, y = make_classification(n_samples=100, n_features=10, random_state=42)
    model = RandomForestClassifier(n_estimators=10, random_state=42)
    model.fit(X, y)

    # Save model
    manager.save(
        model=model,
        name='example_classifier',
        version='v1.0.0',
        metrics={'accuracy': 0.95, 'precision': 0.94, 'recall': 0.93},
        description='Example random forest classifier'
    )

    # List models
    print("\nAll saved models:")
    models = manager.list_models()
    for m in models:
        print(f"  {m['name']}: {', '.join(m['versions'])} (latest: {m['latest']})")

    # Load model
    print("\nLoading model...")
    loaded_model, metadata = manager.load('example_classifier', 'latest')

    if loaded_model:
        print(f"Model type: {type(loaded_model).__name__}")
        print(f"Metrics: {metadata.get('metrics')}")
