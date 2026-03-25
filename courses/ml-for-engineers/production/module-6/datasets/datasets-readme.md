# Module 6 Datasets Guide
## Neural Networks & Deep Learning

This guide covers all datasets used in Module 6.

---

## Quick Start

```bash
# Download all datasets
python download_module6_datasets.py

# Or manually install required packages
pip install tensorflow scikit-learn yfinance pandas numpy matplotlib
```

---

## Dataset 1: MNIST Handwritten Digits

**Source:** Built into Keras (automatically downloaded)
**Size:** ~11 MB
**Samples:** 70,000 images (60,000 train, 10,000 test)
**Format:** 28×28 grayscale images
**Classes:** 10 (digits 0-9)

### Usage:
```python
from tensorflow.keras.datasets import mnist
(X_train, y_train), (X_test, y_test) = mnist.load_data()
```

### Used in:
- Session 2: `mnist-digit-recognition.ipynb` (baseline >95%)
- Session 4: `mnist-optimized-98plus.ipynb` (optimized >98%)

---

## Dataset 2: Fashion MNIST

**Source:** Built into Keras
**Size:** ~25 MB
**Samples:** 70,000 images (60,000 train, 10,000 test)
**Format:** 28×28 grayscale images
**Classes:** 10 fashion items

### Classes:
0. T-shirt/top
1. Trouser
2. Pullover
3. Dress
4. Coat
5. Sandal
6. Shirt
7. Sneaker
8. Bag
9. Ankle boot

### Usage:
```python
from tensorflow.keras.datasets import fashion_mnist
(X_train, y_train), (X_test, y_test) = fashion_mnist.load_data()
```

### Used in:
- Session 3: `fashion-mnist-training.ipynb` (>85% accuracy)

---

## Dataset 3: Iris

**Source:** Built into scikit-learn
**Size:** <1 MB
**Samples:** 150
**Features:** 4 (sepal length, sepal width, petal length, petal width)
**Classes:** 3 (setosa, versicolor, virginica)

### Usage:
```python
from sklearn.datasets import load_iris
iris = load_iris()
X, y = iris.data, iris.target
```

### Used in:
- Session 1: `iris-neural-network.ipynb` (NN vs Traditional ML comparison)

---

## Dataset 4: Stock Price Data

**Source:** Yahoo Finance (via yfinance)
**Size:** ~2 MB
**Samples:** ~1,260 days per stock (5 years)
**Stocks:** AAPL, GOOGL, MSFT (can add more)
**Features:** Open, High, Low, Close, Volume, Adjusted Close

### Usage:
```python
import yfinance as yf
df = yf.download('AAPL', period='5y')
```

### Alternative:
Reuse stock data from Module 3:
```python
# Copy from Module 3
cp ../../module-3/datasets/stock/*.csv ./data/stock/
```

### Feature Engineering:
Use Module 3's `feature_engineering.py` library to add technical indicators:
- Moving Averages (SMA, EMA)
- RSI, MACD, Bollinger Bands
- Momentum and volatility indicators

### Used in:
- Session 6: `stock-predictor-neural-network.ipynb` (CAPSTONE)

---

## Dataset 5: Transfer Learning Images

**Note:** Manual download required

### Option 1: TensorFlow Flowers Dataset (Recommended)

**Source:** TensorFlow Datasets
**Size:** ~218 MB
**Samples:** ~3,670 images
**Classes:** 5 (daisy, dandelion, roses, sunflowers, tulips)

```python
pip install tensorflow-datasets

import tensorflow_datasets as tfds
dataset = tfds.load('tf_flowers', split='train', as_supervised=True)
```

### Option 2: Kaggle Cats vs Dogs

**Source:** Kaggle Competition
**Size:** ~800 MB
**Samples:** 25,000 images
**Classes:** 2 (cats, dogs)

**Steps:**
1. Install Kaggle API:
   ```bash
   pip install kaggle
   ```

2. Setup API credentials:
   - Go to https://www.kaggle.com/account
   - Create new API token
   - Save to ~/.kaggle/kaggle.json
   - Set permissions: `chmod 600 ~/.kaggle/kaggle.json`

3. Download:
   ```bash
   kaggle competitions download -c dogs-vs-cats
   unzip dogs-vs-cats.zip -d data/cats-vs-dogs/
   ```

### Option 3: Custom Dataset

Place your own images in this structure:
```
data/custom/
├── class1/
│   ├── image1.jpg
│   ├── image2.jpg
│   └── ...
├── class2/
│   ├── image1.jpg
│   └── ...
```

Use ImageDataGenerator:
```python
from tensorflow.keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)
train_generator = train_datagen.flow_from_directory(
    'data/custom',
    target_size=(224, 224),
    batch_size=32,
    class_mode='categorical',
    subset='training'
)
```

### Used in:
- Session 5: `transfer-learning-vgg16.ipynb` (>90% accuracy)

---

## System Requirements

### Minimum:
- **RAM:** 8 GB
- **Disk Space:** 2 GB (without transfer learning data)
- **Python:** 3.7+
- **CPU:** Multi-core recommended

### Recommended:
- **RAM:** 16 GB+
- **Disk Space:** 5 GB
- **GPU:** NVIDIA GPU with CUDA support
- **Python:** 3.8-3.10

---

## Package Requirements

```txt
tensorflow>=2.8.0
scikit-learn>=1.0.0
pandas>=1.3.0
numpy>=1.21.0
matplotlib>=3.4.0
seaborn>=0.11.0
yfinance>=0.1.70
tensorflow-datasets>=4.5.0  # Optional for flowers
kaggle>=1.5.0  # Optional for cats-vs-dogs
```

Install all:
```bash
pip install tensorflow scikit-learn pandas numpy matplotlib seaborn yfinance
```

---

## GPU Setup (Optional but Recommended)

### Check GPU Availability:
```python
import tensorflow as tf
print(f"GPUs Available: {len(tf.config.list_physical_devices('GPU'))}")
```

### NVIDIA GPU Setup:
1. Install CUDA Toolkit (11.2+)
2. Install cuDNN (8.1+)
3. Install TensorFlow GPU:
   ```bash
   pip install tensorflow[and-cuda]
   ```

### Apple Silicon (M1/M2):
```bash
pip install tensorflow-macos tensorflow-metal
```

### Google Colab:
Free GPU available! No setup needed.
- Runtime → Change runtime type → GPU

---

## Troubleshooting

### Issue: MNIST/Fashion MNIST won't download
**Solution:** Check internet connection, try again
```python
# Manual download location
~/.keras/datasets/
```

### Issue: Stock data download fails
**Solution:**
1. Check yfinance is installed: `pip install yfinance`
2. Try different ticker: `yf.download('MSFT')`
3. Check Yahoo Finance is accessible
4. Reuse Module 3 data

### Issue: Out of memory during training
**Solution:**
1. Reduce batch size: `batch_size=16` instead of 32
2. Reduce model size: Fewer neurons
3. Close other applications
4. Use Google Colab (free GPU!)

### Issue: Training is very slow
**Solution:**
1. Enable GPU if available
2. Reduce image size for transfer learning
3. Reduce number of epochs
4. Use Google Colab

### Issue: TensorFlow import error
**Solution:**
```bash
pip uninstall tensorflow
pip install tensorflow==2.12.0
```

---

## Data Preprocessing Notes

### For All Datasets:
1. **Normalize pixel values:** 0-255 → 0-1
   ```python
   X = X.astype('float32') / 255.0
   ```

2. **One-hot encode labels:**
   ```python
   from tensorflow.keras.utils import to_categorical
   y = to_categorical(y, num_classes)
   ```

3. **Flatten images for Dense networks:**
   ```python
   X = X.reshape(-1, 784)  # 28×28 → 784
   ```

### For Stock Data:
1. **Feature scaling (CRITICAL for NNs!):**
   ```python
   from sklearn.preprocessing import StandardScaler
   scaler = StandardScaler()
   X_scaled = scaler.fit_transform(X)
   ```

2. **Time series split (NO shuffling!):**
   ```python
   split = int(len(X) * 0.8)
   X_train, X_test = X[:split], X[split:]
   ```

3. **Create sequences for LSTM:**
   ```python
   def create_sequences(data, seq_length=60):
       X, y = [], []
       for i in range(seq_length, len(data)):
           X.append(data[i-seq_length:i])
           y.append(data[i])
       return np.array(X), np.array(Y)
   ```

---

## Dataset Usage Summary

| Session | Dataset | Notebook | Target Accuracy |
|---------|---------|----------|-----------------|
| 1 | Iris | iris-neural-network.ipynb | 95%+ |
| 2 | MNIST | mnist-digit-recognition.ipynb | >95% |
| 3 | Fashion MNIST | fashion-mnist-training.ipynb | >85% |
| 4 | MNIST | mnist-optimized-98plus.ipynb | >98% |
| 5 | Flowers/Cats-Dogs | transfer-learning-vgg16.ipynb | >90% |
| 6 | Stock Data | stock-predictor-neural-network.ipynb | R² >0.70 |

---

## Next Steps

1. ✅ Run `python download_module6_datasets.py`
2. ✅ Verify all datasets downloaded successfully
3. ✅ Start with Session 1: Iris neural network
4. ✅ Progress through sessions 2-6
5. ✅ Complete capstone: Stock predictor with NN

**Good luck with Module 6!** 🚀
