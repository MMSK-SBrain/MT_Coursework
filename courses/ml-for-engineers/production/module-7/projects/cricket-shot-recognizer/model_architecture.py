"""
Cricket Shot Recognition Model Architecture
Uses ResNet50 transfer learning for 6-class classification
"""

import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.applications import ResNet50

def create_cricket_shot_model(num_classes=6, input_shape=(224, 224, 3)):
    """
    Create cricket shot classification model using ResNet50.

    Args:
        num_classes (int): Number of shot types to classify (default: 6)
        input_shape (tuple): Input image shape (default: 224x224x3)

    Returns:
        model: Compiled Keras model
    """

    # Load pre-trained ResNet50 without top layers
    base_model = ResNet50(
        weights='imagenet',
        include_top=False,
        input_shape=input_shape
    )

    # Freeze base model initially
    base_model.trainable = False

    # Build custom classifier on top
    model = models.Sequential([
        base_model,

        # Global pooling
        layers.GlobalAveragePooling2D(),

        # First dense block
        layers.Dense(512, activation='relu'),
        layers.BatchNormalization(),
        layers.Dropout(0.5),

        # Second dense block
        layers.Dense(256, activation='relu'),
        layers.BatchNormalization(),
        layers.Dropout(0.3),

        # Output layer
        layers.Dense(num_classes, activation='softmax')
    ], name='CricketShotClassifier')

    return model, base_model


def compile_model(model, learning_rate=0.001):
    """
    Compile model with optimizer and metrics.

    Args:
        model: Keras model to compile
        learning_rate (float): Learning rate for optimizer
    """
    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=learning_rate),
        loss='categorical_crossentropy',
        metrics=['accuracy', tf.keras.metrics.TopKCategoricalAccuracy(k=3, name='top3_acc')]
    )
    return model


def unfreeze_model(base_model, num_layers_to_unfreeze=30):
    """
    Unfreeze top layers for fine-tuning.

    Args:
        base_model: Base ResNet50 model
        num_layers_to_unfreeze (int): Number of top layers to unfreeze
    """
    base_model.trainable = True

    # Freeze all except top layers
    for layer in base_model.layers[:-num_layers_to_unfreeze]:
        layer.trainable = False

    num_trainable = sum([1 for layer in base_model.layers if layer.trainable])
    print(f"Unfroze {num_trainable} layers for fine-tuning")

    return base_model


def get_callbacks(checkpoint_path='models/cricket_shot_model.h5'):
    """
    Get training callbacks.

    Args:
        checkpoint_path (str): Path to save best model

    Returns:
        list: List of Keras callbacks
    """
    callbacks = [
        tf.keras.callbacks.EarlyStopping(
            monitor='val_loss',
            patience=10,
            restore_best_weights=True,
            verbose=1
        ),
        tf.keras.callbacks.ReduceLROnPlateau(
            monitor='val_loss',
            factor=0.5,
            patience=5,
            min_lr=1e-7,
            verbose=1
        ),
        tf.keras.callbacks.ModelCheckpoint(
            filepath=checkpoint_path,
            monitor='val_accuracy',
            save_best_only=True,
            verbose=1
        )
    ]

    return callbacks


def print_model_info(model):
    """Print model architecture summary."""
    print("\n" + "="*50)
    print("MODEL ARCHITECTURE")
    print("="*50)
    model.summary()

    total_params = model.count_params()
    trainable_params = sum([tf.keras.backend.count_params(w) for w in model.trainable_weights])
    non_trainable_params = total_params - trainable_params

    print("\n" + "="*50)
    print("MODEL PARAMETERS")
    print("="*50)
    print(f"Total parameters: {total_params:,}")
    print(f"Trainable parameters: {trainable_params:,}")
    print(f"Non-trainable parameters: {non_trainable_params:,}")
    print("="*50 + "\n")


if __name__ == "__main__":
    # Test model creation
    print("Creating cricket shot classification model...\n")

    model, base_model = create_cricket_shot_model()
    model = compile_model(model)
    print_model_info(model)

    print("\nModel created successfully!")
    print("Ready for training on cricket shot dataset.")
