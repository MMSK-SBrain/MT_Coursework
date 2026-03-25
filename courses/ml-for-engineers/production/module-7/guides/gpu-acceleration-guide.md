# GPU Acceleration Guide for Deep Learning

Speed up your Module 7 CNN training with GPU acceleration.

---

## Quick Facts

**CPU vs GPU Training Time:**
- MNIST (Session 7.1): CPU 5 min vs GPU 1 min
- CIFAR-10 (Session 7.2): CPU 45 min vs GPU 8 min
- Transfer Learning (7.3): CPU 2 hours vs GPU 20 min
- Cricket Capstone: CPU 4 hours vs GPU 40 min

**GPU gives 5-10x speedup for deep learning!**

---

## Check GPU Availability

```python
import tensorflow as tf

print("TensorFlow version:", tf.__version__)
print("GPU Available:", tf.test.is_gpu_available())
print("GPU Devices:", tf.config.list_physical_devices('GPU'))

# For TensorFlow 2.x
gpus = tf.config.list_physical_devices('GPU')
if gpus:
    print(f"✓ GPU found: {gpus}")
else:
    print("⚠ No GPU detected - using CPU")
```

---

## GPU Setup Options

### Option 1: Google Colab (Easiest - Free GPU!)

**Advantages:**
- Free Tesla T4/K80 GPU
- No installation needed
- Pre-installed TensorFlow/Keras
- Jupyter notebook interface

**Steps:**
1. Go to https://colab.research.google.com
2. Runtime → Change runtime type → GPU
3. Upload/import your notebook
4. Run!

**Limits:**
- 12 hour session limit
- May disconnect if idle
- Limited RAM (12-25GB)

### Option 2: Local GPU (NVIDIA)

**Requirements:**
- NVIDIA GPU (GTX 1050 or better recommended)
- CUDA-compatible drivers
- CUDA Toolkit
- cuDNN library

**Installation (Windows):**

1. **Check GPU compatibility:**
   - Visit: https://developer.nvidia.com/cuda-gpus
   - Ensure your GPU is listed

2. **Install NVIDIA drivers:**
   - Download from: https://www.nvidia.com/Download/index.aspx
   - Install latest Game Ready Driver

3. **Install CUDA Toolkit:**
   - Download: https://developer.nvidia.com/cuda-downloads
   - Install CUDA 11.8 (recommended for TF 2.13)

4. **Install cuDNN:**
   - Download: https://developer.nvidia.com/cudnn
   - Extract to CUDA directory
   - Add to system PATH

5. **Install TensorFlow with GPU support:**
   ```bash
   pip install tensorflow==2.13.0
   ```

6. **Verify:**
   ```python
   import tensorflow as tf
   print(tf.config.list_physical_devices('GPU'))
   ```

**Installation (Linux):**

```bash
# 1. Install NVIDIA drivers
sudo apt-get install nvidia-driver-525

# 2. Install CUDA
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-ubuntu2204.pin
sudo mv cuda-ubuntu2204.pin /etc/apt/preferences.d/cuda-repository-pin-600
wget https://developer.download.nvidia.com/compute/cuda/11.8.0/local_installers/cuda-repo-ubuntu2204-11-8-local_11.8.0-520.61.05-1_amd64.deb
sudo dpkg -i cuda-repo-ubuntu2204-11-8-local_11.8.0-520.61.05-1_amd64.deb
sudo cp /var/cuda-repo-ubuntu2204-11-8-local/cuda-*-keyring.gpg /usr/share/keyrings/
sudo apt-get update
sudo apt-get install cuda

# 3. Install cuDNN
# Download from NVIDIA website, then:
sudo dpkg -i libcudnn8_8.6.0.163-1+cuda11.8_amd64.deb

# 4. Add to PATH
echo 'export PATH=/usr/local/cuda/bin:$PATH' >> ~/.bashrc
echo 'export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH' >> ~/.bashrc
source ~/.bashrc

# 5. Install TensorFlow
pip install tensorflow==2.13.0
```

### Option 3: Cloud Platforms

**AWS EC2 (p2.xlarge):**
- Tesla K80 GPU
- $0.90/hour
- Pre-configured Deep Learning AMIs

**Google Cloud (n1-standard-4 + T4):**
- NVIDIA Tesla T4
- ~$0.50/hour
- Pre-installed ML frameworks

**Azure (NC6):**
- Tesla K80
- ~$0.90/hour
- Data Science VM images

---

## Optimizing GPU Usage

### 1. Memory Management

```python
# Limit GPU memory growth (prevent OOM)
gpus = tf.config.list_physical_devices('GPU')
if gpus:
    try:
        for gpu in gpus:
            tf.config.experimental.set_memory_growth(gpu, True)
    except RuntimeError as e:
        print(e)
```

### 2. Batch Size Tuning

```python
# Larger batch size = better GPU utilization
# But don't exceed GPU memory!

# Start with 32, increase if possible
batch_sizes_to_try = [32, 64, 128, 256]

for batch_size in batch_sizes_to_try:
    try:
        model.fit(X_train, y_train, batch_size=batch_size, epochs=1)
        print(f"✓ Batch size {batch_size} works")
    except:
        print(f"✗ Batch size {batch_size} too large")
        break
```

### 3. Mixed Precision Training

```python
# Use float16 instead of float32 for faster training
from tensorflow.keras import mixed_precision

policy = mixed_precision.Policy('mixed_float16')
mixed_precision.set_global_policy(policy)

# 2x faster training, half memory usage!
```

### 4. Data Pipeline Optimization

```python
# Use tf.data for efficient data loading
AUTOTUNE = tf.data.AUTOTUNE

train_ds = tf.data.Dataset.from_tensor_slices((X_train, y_train))
train_ds = train_ds.cache()  # Cache in memory
train_ds = train_ds.shuffle(1000)
train_ds = train_ds.batch(batch_size)
train_ds = train_ds.prefetch(AUTOTUNE)  # Prefetch next batch
```

---

## Troubleshooting

### Issue 1: "Could not load dynamic library 'cudart64_*.dll'"

**Solution (Windows):**
```bash
# Add CUDA bin to PATH
set PATH=%PATH%;C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8\bin
```

**Solution (Linux):**
```bash
export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH
```

### Issue 2: Out of Memory (OOM)

**Solutions:**
1. Reduce batch size
2. Reduce model size
3. Enable memory growth
4. Use gradient accumulation

```python
# Enable memory growth
gpus = tf.config.list_physical_devices('GPU')
for gpu in gpus:
    tf.config.experimental.set_memory_growth(gpu, True)

# Or set memory limit
tf.config.set_logical_device_configuration(
    gpus[0],
    [tf.config.LogicalDeviceConfiguration(memory_limit=4096)]  # 4GB
)
```

### Issue 3: GPU Not Being Used

**Check:**
```python
# During training, run this
with tf.device('/GPU:0'):
    model.fit(X_train, y_train)

# Monitor GPU usage
# Windows: Task Manager → Performance → GPU
# Linux: nvidia-smi
```

### Issue 4: Slow First Epoch

**Cause:** TensorFlow compiling graph

**Solution:** This is normal! Subsequent epochs will be faster.

---

## Monitoring GPU Usage

### NVIDIA System Management Interface

```bash
# Check GPU status
nvidia-smi

# Continuous monitoring (update every 2s)
nvidia-smi -l 2

# Specific GPU
nvidia-smi -i 0
```

### Python Monitoring

```python
import subprocess

def get_gpu_memory():
    result = subprocess.check_output(
        ['nvidia-smi', '--query-gpu=memory.used,memory.total',
         '--format=csv,nounits,noheader']
    )
    gpu_memory = [int(x) for x in result.decode().strip().split(',')]
    return gpu_memory

# Check during training
used, total = get_gpu_memory()
print(f"GPU Memory: {used}MB / {total}MB ({used/total*100:.1f}%)")
```

---

## Free GPU Resources

### Google Colab
- **Cost:** Free
- **GPU:** Tesla K80/T4
- **Limit:** 12 hours/session
- **Best for:** All Module 7 sessions

### Kaggle Kernels
- **Cost:** Free
- **GPU:** Tesla P100
- **Limit:** 30 hours/week
- **Best for:** Longer training sessions

### Gradient (Paperspace)
- **Cost:** Free tier available
- **GPU:** Various options
- **Limit:** 6 hours/month (free)

---

## Performance Comparison

### MNIST Training (10 epochs)

| Hardware | Time | Speedup |
|----------|------|---------|
| CPU (Intel i5) | 5:30 | 1x |
| GPU (GTX 1050) | 1:10 | 4.7x |
| GPU (RTX 3060) | 0:35 | 9.4x |
| GPU (Tesla T4 - Colab) | 0:55 | 6x |

### CIFAR-10 Training (50 epochs)

| Hardware | Time | Speedup |
|----------|------|---------|
| CPU (Intel i7) | 45:00 | 1x |
| GPU (GTX 1050) | 9:30 | 4.7x |
| GPU (RTX 3060) | 4:20 | 10.4x |
| GPU (Tesla T4 - Colab) | 6:15 | 7.2x |

### Transfer Learning (Cricket Capstone)

| Hardware | Time | Speedup |
|----------|------|---------|
| CPU | 4:00:00 | 1x |
| GPU (GTX 1050) | 50:00 | 4.8x |
| GPU (RTX 3060) | 22:00 | 10.9x |
| GPU (Tesla T4 - Colab) | 35:00 | 6.9x |

---

## Recommendations by Session

| Session | Recommended | Why |
|---------|-------------|-----|
| 7.1 (MNIST) | CPU OK | Small, trains in 5 min |
| 7.2 (CIFAR-10) | GPU preferred | 50 epochs, much faster |
| 7.3 (Transfer Learning) | GPU recommended | Large pre-trained models |
| 7.4 (Object Detection) | CPU OK | Uses OpenCV, not training-heavy |
| 7.5 (Medical) | GPU recommended | Fine-tuning required |
| 7.6 (Defects) | GPU recommended | Transfer learning |
| **Capstone** | **GPU highly recommended** | Large training time |

---

## Quick Start for Colab

```python
# 1. Check GPU
import tensorflow as tf
print("GPU:", "Available" if tf.test.is_gpu_available() else "Not Available")

# 2. Enable mixed precision (optional, for speed)
from tensorflow.keras import mixed_precision
mixed_precision.set_global_policy('mixed_float16')

# 3. Increase batch size
batch_size = 64  # Instead of 32 on CPU

# 4. Train!
model.fit(
    train_gen,
    epochs=20,
    batch_size=batch_size,
    validation_data=val_gen
)
```

---

## Key Takeaways

1. **Google Colab = Easiest** - Free GPU, no setup
2. **Local GPU = Fastest** - But requires setup
3. **Batch Size** - Larger on GPU (64-256 vs 32)
4. **Memory** - Monitor usage, enable growth
5. **First Epoch Slow** - Normal, subsequent epochs faster
6. **Speedup: 5-10x** - Worth it for larger models

---

**For Module 7:** Use Google Colab with free GPU. It's perfect for all sessions and the capstone project!

Happy accelerated training!
