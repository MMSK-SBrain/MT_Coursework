"""
Data augmentation and preprocessing utilities for cricket shot images
"""

import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import numpy as np
import matplotlib.pyplot as plt

# Class names
CLASS_NAMES = [
    'cover_drive',
    'straight_drive',
    'pull',
    'hook',
    'sweep',
    'defensive'
]

def create_data_generators(train_dir, val_dir, batch_size=32, img_size=(224, 224)):
    """
    Create training and validation data generators with augmentation.

    Args:
        train_dir (str): Path to training data directory
        val_dir (str): Path to validation data directory
        batch_size (int): Batch size for generators
        img_size (tuple): Target image size

    Returns:
        train_gen, val_gen: Data generators
    """

    # Training data augmentation
    train_datagen = ImageDataGenerator(
        rescale=1./255,
        rotation_range=30,          # Cricket shots at various angles
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.15,
        zoom_range=0.2,
        horizontal_flip=True,       # Left/right handed batsmen
        brightness_range=[0.8, 1.2],
        fill_mode='nearest'
    )

    # Validation data (only rescaling)
    val_datagen = ImageDataGenerator(rescale=1./255)

    # Create generators
    train_generator = train_datagen.flow_from_directory(
        train_dir,
        target_size=img_size,
        batch_size=batch_size,
        class_mode='categorical',
        shuffle=True,
        seed=42
    )

    val_generator = val_datagen.flow_from_directory(
        val_dir,
        target_size=img_size,
        batch_size=batch_size,
        class_mode='categorical',
        shuffle=False
    )

    print(f"Training samples: {train_generator.samples}")
    print(f"Validation samples: {val_generator.samples}")
    print(f"Classes: {train_generator.class_indices}")

    return train_generator, val_generator


def preprocess_single_image(img_path, img_size=(224, 224)):
    """
    Preprocess a single image for prediction.

    Args:
        img_path (str): Path to image file
        img_size (tuple): Target image size

    Returns:
        np.array: Preprocessed image array
    """
    from tensorflow.keras.preprocessing import image

    img = image.load_img(img_path, target_size=img_size)
    img_array = image.img_to_array(img)
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    return img_array


def visualize_augmentation(train_generator, num_samples=9):
    """
    Visualize data augmentation effects.

    Args:
        train_generator: Training data generator
        num_samples (int): Number of augmented samples to show
    """
    # Get a batch
    images, labels = next(train_generator)

    # Plot
    fig, axes = plt.subplots(3, 3, figsize=(12, 12))
    fig.suptitle('Data Augmentation Examples', fontsize=16, fontweight='bold')

    for i, ax in enumerate(axes.flat):
        if i < num_samples:
            ax.imshow(images[i])
            class_idx = np.argmax(labels[i])
            class_name = CLASS_NAMES[class_idx]
            ax.set_title(f'{class_name}', fontsize=10)
            ax.axis('off')

    plt.tight_layout()
    plt.show()


def check_class_balance(generator):
    """
    Check and visualize class distribution.

    Args:
        generator: Data generator to check
    """
    class_counts = {}
    for class_name, class_idx in generator.class_indices.items():
        class_counts[class_name] = np.sum(generator.classes == class_idx)

    # Plot
    plt.figure(figsize=(12, 6))
    plt.bar(class_counts.keys(), class_counts.values(), color='steelblue', edgecolor='black')
    plt.title('Class Distribution', fontsize=14, fontweight='bold')
    plt.xlabel('Shot Type')
    plt.ylabel('Number of Images')
    plt.xticks(rotation=45)
    plt.grid(axis='y', alpha=0.3)

    for i, (name, count) in enumerate(class_counts.items()):
        plt.text(i, count + 5, str(count), ha='center', va='bottom')

    plt.tight_layout()
    plt.show()

    # Print statistics
    print("\nClass Distribution:")
    print("="*40)
    for name, count in class_counts.items():
        percentage = (count / generator.samples) * 100
        print(f"{name:20s}: {count:4d} ({percentage:5.1f}%)")
    print("="*40)
    print(f"Total: {generator.samples}")

    # Check balance
    min_count = min(class_counts.values())
    max_count = max(class_counts.values())
    imbalance_ratio = max_count / min_count

    if imbalance_ratio > 1.5:
        print(f"\n⚠ Warning: Class imbalance detected (ratio: {imbalance_ratio:.2f})")
        print("Consider collecting more data for underrepresented classes.")
    else:
        print(f"\n✓ Classes are reasonably balanced (ratio: {imbalance_ratio:.2f})")


def create_test_time_augmentation(model, image, num_augmentations=10):
    """
    Apply test-time augmentation for more robust predictions.

    Args:
        model: Trained model
        image (np.array): Input image
        num_augmentations (int): Number of augmented predictions to average

    Returns:
        np.array: Averaged predictions
    """
    datagen = ImageDataGenerator(
        rotation_range=15,
        width_shift_range=0.1,
        height_shift_range=0.1,
        horizontal_flip=True,
        zoom_range=0.1
    )

    predictions = []

    for _ in range(num_augmentations):
        augmented = datagen.random_transform(image[0])
        augmented = np.expand_dims(augmented, axis=0)
        pred = model.predict(augmented, verbose=0)
        predictions.append(pred)

    # Average predictions
    avg_prediction = np.mean(predictions, axis=0)

    return avg_prediction


if __name__ == "__main__":
    print("Data augmentation utilities loaded successfully.")
    print(f"\nSupported shot types: {CLASS_NAMES}")
