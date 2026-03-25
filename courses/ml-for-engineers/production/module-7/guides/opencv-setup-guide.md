# OpenCV Setup Guide for Computer Vision

Complete guide to installing and configuring OpenCV for Module 7 projects.

---

## Quick Start

```bash
# Recommended: Install via pip
pip install opencv-python==4.8.0.76

# For full features (including GUI)
pip install opencv-contrib-python==4.8.0.76

# Verify installation
python -c "import cv2; print(cv2.__version__)"
```

---

## Installation Methods

### Method 1: Pip Install (Recommended)

**Basic OpenCV:**
```bash
pip install opencv-python
```

**OpenCV with extra modules:**
```bash
pip install opencv-contrib-python
```

**Specific version:**
```bash
pip install opencv-python==4.8.0.76
```

### Method 2: Conda Install

```bash
conda install -c conda-forge opencv
```

### Method 3: Build from Source (Advanced)

Only if you need custom builds or latest features.

**Ubuntu/Debian:**
```bash
sudo apt-get update
sudo apt-get install build-essential cmake git
sudo apt-get install python3-dev python3-numpy
git clone https://github.com/opencv/opencv.git
cd opencv
mkdir build && cd build
cmake ..
make -j4
sudo make install
```

---

## Platform-Specific Instructions

### Windows

1. **Install Python** (3.8+)
   - Download from python.org
   - Check "Add to PATH" during installation

2. **Install OpenCV:**
   ```cmd
   pip install opencv-python
   ```

3. **Verify:**
   ```cmd
   python -c "import cv2; print(cv2.__version__)"
   ```

**Common Windows Issues:**
- Missing DLL errors → Install Visual C++ Redistributable
- Import errors → Reinstall with `pip install --force-reinstall opencv-python`

### macOS

1. **Install Homebrew** (if not installed):
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. **Install Python:**
   ```bash
   brew install python@3.11
   ```

3. **Install OpenCV:**
   ```bash
   pip3 install opencv-python
   ```

4. **For webcam access**, you may need:
   ```bash
   brew install ffmpeg
   ```

**macOS-Specific Issues:**
- Webcam permissions → System Preferences → Security & Privacy → Camera
- M1/M2 Macs → Use native ARM Python, not Rosetta

### Linux (Ubuntu/Debian)

1. **Update system:**
   ```bash
   sudo apt-get update
   sudo apt-get upgrade
   ```

2. **Install dependencies:**
   ```bash
   sudo apt-get install python3-pip python3-dev
   sudo apt-get install libopencv-dev python3-opencv
   ```

3. **Install via pip:**
   ```bash
   pip3 install opencv-python
   ```

**Linux-Specific Issues:**
- Webcam not detected → Check permissions: `sudo usermod -a -G video $USER`
- GUI issues → Install: `sudo apt-get install libgtk-3-dev`

---

## Troubleshooting Common Issues

### Issue 1: ImportError: No module named 'cv2'

**Symptoms:**
```python
import cv2
ModuleNotFoundError: No module named 'cv2'
```

**Solutions:**
```bash
# Verify Python version
python --version

# Reinstall OpenCV
pip uninstall opencv-python opencv-contrib-python
pip install opencv-python

# Check if installed
pip list | grep opencv
```

### Issue 2: Webcam Not Working

**Symptoms:**
```python
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
# ret is False
```

**Solutions:**

1. **Check camera index:**
   ```python
   # Try different indices
   for i in range(10):
       cap = cv2.VideoCapture(i)
       if cap.isOpened():
           print(f"Camera found at index {i}")
           break
   ```

2. **Check permissions:**
   - Windows: Camera privacy settings
   - macOS: System Preferences → Security → Camera
   - Linux: User must be in 'video' group

3. **External webcam:**
   ```python
   cap = cv2.VideoCapture(1)  # Try index 1 for external
   ```

### Issue 3: Haar Cascade Files Not Found

**Symptoms:**
```python
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# Empty cascade classifier
```

**Solution:**
```python
import cv2

# Use full path from cv2.data
cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(cascade_path)

# Verify loaded
if face_cascade.empty():
    print("Error loading cascade")
else:
    print("Cascade loaded successfully")
```

### Issue 4: Slow Performance

**Solutions:**

1. **Resize images:**
   ```python
   img = cv2.imread('large_image.jpg')
   img = cv2.resize(img, (640, 480))  # Smaller = faster
   ```

2. **Use grayscale:**
   ```python
   gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
   ```

3. **Optimize detection parameters:**
   ```python
   faces = face_cascade.detectMultiScale(
       gray,
       scaleFactor=1.3,  # Larger = faster but less accurate
       minNeighbors=5    # Lower = faster but more false positives
   )
   ```

### Issue 5: Display Window Not Appearing

**Symptoms:**
```python
cv2.imshow('Image', img)
# Window doesn't appear
```

**Solutions:**

1. **Add waitKey:**
   ```python
   cv2.imshow('Image', img)
   cv2.waitKey(0)  # Wait indefinitely
   cv2.destroyAllWindows()
   ```

2. **For Jupyter/Colab:**
   ```python
   from google.colab.patches import cv2_imshow
   cv2_imshow(img)  # Use instead of cv2.imshow
   ```

3. **Use matplotlib:**
   ```python
   import matplotlib.pyplot as plt
   img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
   plt.imshow(img_rgb)
   plt.show()
   ```

### Issue 6: Color Issues (Blue-tinted images)

**Cause:** OpenCV uses BGR, not RGB

**Solution:**
```python
# Reading and displaying
img = cv2.imread('image.jpg')  # Loads as BGR
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# For matplotlib
plt.imshow(img_rgb)  # Now correct colors

# For PIL/Pillow
from PIL import Image
pil_img = Image.fromarray(img_rgb)
```

---

## Useful Code Snippets

### Basic Image Operations

```python
import cv2

# Read image
img = cv2.imread('image.jpg')

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Resize
resized = cv2.resize(img, (640, 480))

# Save image
cv2.imwrite('output.jpg', img)

# Display (desktop only)
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

### Webcam Capture

```python
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow('Webcam', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

### Face Detection

```python
import cv2

# Load cascade
cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(cascade_path)

# Read image
img = cv2.imread('people.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

# Draw rectangles
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow('Faces', img)
cv2.waitKey(0)
```

---

## Advanced Configuration

### GPU Acceleration

Check if OpenCV was built with CUDA:
```python
import cv2
print(cv2.cuda.getCudaEnabledDeviceCount())
```

Build from source with CUDA for GPU acceleration (advanced users).

### Video Codecs

Install additional codecs for video processing:

**Windows:**
```bash
pip install opencv-python-headless  # No GUI
```

**Linux:**
```bash
sudo apt-get install ffmpeg x264 libx264-dev
```

---

## Testing Your Installation

Run this comprehensive test:

```python
import cv2
import numpy as np

print("OpenCV version:", cv2.__version__)
print("NumPy version:", np.__version__)

# Test 1: Basic operations
img = np.zeros((100, 100, 3), dtype=np.uint8)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print("✓ Color conversion works")

# Test 2: Haar Cascade
cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
cascade = cv2.CascadeClassifier(cascade_path)
if not cascade.empty():
    print("✓ Haar Cascade loading works")

# Test 3: Webcam (optional)
cap = cv2.VideoCapture(0)
if cap.isOpened():
    print("✓ Webcam accessible")
    cap.release()
else:
    print("⚠ Webcam not accessible (may be OK)")

print("\nInstallation test complete!")
```

---

## Resources

- **Official Documentation**: https://docs.opencv.org/
- **Python Tutorials**: https://docs.opencv.org/master/d6/d00/tutorial_py_root.html
- **GitHub**: https://github.com/opencv/opencv
- **Stack Overflow**: Tag `opencv` for questions

---

## Quick Reference

| Task | Code |
|------|------|
| Read image | `cv2.imread('img.jpg')` |
| Convert to RGB | `cv2.cvtColor(img, cv2.COLOR_BGR2RGB)` |
| Resize | `cv2.resize(img, (w, h))` |
| Grayscale | `cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)` |
| Save image | `cv2.imwrite('out.jpg', img)` |
| Open webcam | `cv2.VideoCapture(0)` |
| Load Haar Cascade | `cv2.CascadeClassifier(cv2.data.haarcascades + 'file.xml')` |

---

**Need Help?**
- Check Module 7 troubleshooting guide
- Post in course discussion forum
- Search OpenCV documentation
- Stack Overflow with `opencv` tag

Happy computer vision coding!
