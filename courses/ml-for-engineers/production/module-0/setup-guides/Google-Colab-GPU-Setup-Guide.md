# Google Colab & GPU Setup Guide

## Complete Step-by-Step Guide for ML for Engineers Course

**Module:** 0 (The Hook)
**Session:** 3
**Time Required:** 15-20 minutes
**Cost:** FREE (Free GPU included!)

---

## Table of Contents

1. [What is Google Colab?](#what-is-google-colab)
2. [Prerequisites](#prerequisites)
3. [Accessing Colab](#accessing-colab)
4. [Creating Your First Notebook](#creating-your-first-notebook)
5. [Interface Tour](#interface-tour)
6. [Enabling GPU](#enabling-gpu)
7. [Installing Libraries](#installing-libraries)
8. [Running Your First ML Code](#running-your-first-ml-code)
9. [Saving and Organizing](#saving-and-organizing)
10. [Troubleshooting](#troubleshooting)
11. [Best Practices](#best-practices)

---

## What is Google Colab?

**Google Colaboratory (Colab)** is a free, cloud-based Jupyter notebook environment.

### Why We Use Colab

✅ **Free GPU access** - Train models 10-100x faster
✅ **No installation needed** - Everything in the browser
✅ **Pre-installed libraries** - pandas, numpy, scikit-learn, TensorFlow ready
✅ **Google Drive integration** - Auto-save your work
✅ **Collaboration** - Share notebooks like Google Docs
✅ **Accessible anywhere** - Any device with browser

### What You Can Do

- Write and execute Python code
- Train machine learning models
- Create visualizations
- Process large datasets
- Use powerful GPUs (for free!)
- Share your work

---

## Prerequisites

Before you begin:

- [ ] Google account (Gmail) - **Required**
- [ ] Modern web browser (Chrome recommended)
- [ ] Internet connection
- [ ] Basic Python knowledge (helpful but not required)

**Note:** Everything happens in the cloud, so no installation needed on your computer!

---

## Accessing Colab

### Method 1: Direct URL

1. Open browser
2. Go to: **https://colab.research.google.com**
3. Sign in with Google account

**Screenshot placeholder:** *Colab homepage*

### Method 2: Google Drive

1. Go to Google Drive: drive.google.com
2. Click **+ New**
3. Click **More** → **Google Colaboratory**
   - If not visible, click **"Connect more apps"**
   - Search "Colaboratory"
   - Install

**Screenshot placeholder:** *Drive new menu*

### Method 3: Direct Link

**Quick Access:** colab.new
- Creates new notebook instantly

---

## Creating Your First Notebook

### Step 1: Start New Notebook

**Option A: From Colab Homepage**
1. Go to colab.research.google.com
2. Click **"New notebook"** or **File → New notebook**

**Option B: From Examples**
1. On Colab homepage, see "Examples"
2. Click "Welcome to Colaboratory"
3. File → Save a copy

**Screenshot placeholder:** *New notebook screen*

### Step 2: Rename Your Notebook

1. Click **"Untitled0.ipynb"** at top
2. Rename to: `M0-Session3-FirstNotebook`
3. Press Enter

**Screenshot placeholder:** *Renaming notebook*

### Step 3: Auto-Save to Google Drive

- Colab automatically saves to: `Google Drive/Colab Notebooks/`
- Saves every few seconds (like Google Docs)
- Look for "Last saved" timestamp

**Screenshot placeholder:** *Auto-save indicator*

---

## Interface Tour

### Main Components

#### 1. **Menu Bar** (Top)
- **File**: New, Open, Save, Download
- **Edit**: Undo, Redo, Find
- **View**: Table of contents, Variables
- **Insert**: Code cell, Text cell
- **Runtime**: Run all, Restart, Change runtime
- **Tools**: Settings, Keyboard shortcuts

**Screenshot placeholder:** *Menu bar*

#### 2. **Toolbar** (Below menu)
- **+ Code**: Add code cell
- **+ Text**: Add markdown/text cell
- **Folder icon**: Files
- **Variables icon**: Variable inspector
- **Connect button**: Connect to runtime

**Screenshot placeholder:** *Toolbar*

#### 3. **Cells** (Main area)

**Two types of cells:**

**Code Cells** (Gray background):
```python
# Python code goes here
print("Hello, ML!")
```

**Text Cells** (White background):
- Markdown formatting
- Headings, lists, links
- Documentation

**Screenshot placeholder:** *Cell types*

#### 4. **Cell Controls**

For each cell:
- **Play button** (▶️): Run cell
- **+ Code/Text**: Add cell below
- **Up/Down arrows**: Move cell
- **Trash icon**: Delete cell
- **Three dots**: More options

**Screenshot placeholder:** *Cell controls*

---

## Your First Code Execution

### Test 1: Hello World

1. Click in a code cell
2. Type:
   ```python
   print("Hello, ML for Engineers!")
   ```
3. Press **Shift + Enter** (or click ▶️)

**Expected Output:**
```
Hello, ML for Engineers!
```

**Screenshot placeholder:** *Hello world execution*

### Test 2: Python Calculation

1. Add new code cell (+ Code)
2. Type:
   ```python
   # Simple calculation
   result = 10 + 20
   print(f"The result is: {result}")
   ```
3. Run (Shift + Enter)

**Expected Output:**
```
The result is: 30
```

### Test 3: Create a List

1. New code cell
2. Type:
   ```python
   # Create and display a list
   numbers = [1, 2, 3, 4, 5]
   print("Numbers:", numbers)
   print("Sum:", sum(numbers))
   print("Average:", sum(numbers) / len(numbers))
   ```
3. Run

**Expected Output:**
```
Numbers: [1, 2, 3, 4, 5]
Sum: 15
Average: 3.0
```

**Screenshot placeholder:** *List example*

### Verification Checklist

- [ ] Code cell executes (green checkmark appears)
- [ ] Output displays below cell
- [ ] Can add multiple cells
- [ ] Can run cells in any order

---

## Enabling GPU

### Why GPU Matters

**Speed Comparison:**
- Training ML model on CPU: 2 hours
- Training same model on GPU: 5 minutes
- **That's 24x faster!**

### Step 1: Check Current Runtime

1. Look at top right
2. See "RAM" and "Disk" indicators
3. Click **Connect** if not connected

**Screenshot placeholder:** *Runtime connection*

### Step 2: Change Runtime Type

1. Click **Runtime** menu
2. Click **"Change runtime type"**

**Screenshot placeholder:** *Runtime menu*

### Step 3: Select GPU

1. In dialog, find **"Hardware accelerator"**
2. Click dropdown
3. Select **"GPU"**
   - Options: None, GPU, TPU
   - Choose: **GPU** (T4)
4. Click **"Save"**

**Screenshot placeholder:** *Runtime settings dialog*

### Step 4: Notebook Restarts

- Notebook will restart (this is normal)
- Variables/outputs will be cleared
- Re-run cells if needed

**Screenshot placeholder:** *Restart notification*

### Step 5: Verify GPU is Enabled

Run this code to verify:

```python
# Method 1: TensorFlow
import tensorflow as tf
print("GPU Available:", tf.config.list_physical_devices('GPU'))
```

**Expected Output:**
```
GPU Available: [PhysicalDevice(name='/physical_device:GPU:0', device_type='GPU')]
```

**Alternative Method:**

```python
# Method 2: nvidia-smi command
!nvidia-smi
```

**Expected Output:**
```
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 525.XX.XX   Driver Version: 525.XX.XX   CUDA Version: 12.0     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  Tesla T4            Off  | 00000000:00:04.0 Off |                    0 |
| N/A   XX°C    P8    XX/70W    |      0MiB / 15360MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
```

**Screenshot placeholder:** *nvidia-smi output*

### GPU Allocation Details

**Free Tier:**
- **GPU Type**: Tesla T4 (15GB memory)
- **Usage Limit**: ~12-15 hours per day
- **Session Timeout**: 12 hours max
- **Idle Timeout**: 90 minutes

**Screenshot placeholder:** *GPU info display*

---

## Installing Libraries

### Pre-installed Libraries

Colab comes with:
- ✅ Python 3.10
- ✅ pandas
- ✅ numpy
- ✅ matplotlib
- ✅ scikit-learn
- ✅ TensorFlow
- ✅ Keras
- ✅ seaborn

### Verify Pre-installed Libraries

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn
import tensorflow as tf

print("✅ All libraries loaded successfully!")
print(f"pandas version: {pd.__version__}")
print(f"numpy version: {np.__version__}")
print(f"scikit-learn version: {sklearn.__version__}")
print(f"TensorFlow version: {tf.__version__}")
```

**Expected Output:**
```
✅ All libraries loaded successfully!
pandas version: 2.0.3
numpy version: 1.23.5
scikit-learn version: 1.2.2
TensorFlow version: 2.15.0
```

**Screenshot placeholder:** *Library versions*

### Installing Additional Libraries

If you need extra libraries:

```python
# Use !pip install
!pip install seaborn
```

**Explanation:**
- `!` = Run as system command (not Python)
- `pip` = Python package installer
- `install` = Install command
- `seaborn` = Library name

**Example: Install plotly**

```python
!pip install plotly
```

**Screenshot placeholder:** *pip install output*

### Checking Installed Libraries

```python
!pip list | grep pandas
```

**Screenshot placeholder:** *pip list output*

---

## Running Your First ML Code

### The Iris Classifier Demo

Copy and run this complete ML example:

```python
# Step 1: Import libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

print("Step 1: Libraries imported ✅")

# Step 2: Load dataset
iris = load_iris()
X = iris.data
y = iris.target

print(f"Step 2: Dataset loaded ✅")
print(f"Number of samples: {len(X)}")
print(f"Number of features: {X.shape[1]}")

# Step 3: Split into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"Step 3: Data split ✅")
print(f"Training samples: {len(X_train)}")
print(f"Testing samples: {len(X_test)}")

# Step 4: Create and train model
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

print("Step 4: Model trained ✅")

# Step 5: Make predictions
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print("Step 5: Predictions made ✅")
print(f"\n🎉 ACCURACY: {accuracy * 100:.1f}%")
print("\n✨ YOU JUST RAN YOUR FIRST MACHINE LEARNING MODEL! ✨")
```

**Expected Output:**
```
Step 1: Libraries imported ✅
Step 2: Dataset loaded ✅
Number of samples: 150
Number of features: 4
Step 3: Data split ✅
Training samples: 120
Testing samples: 30
Step 4: Model trained ✅
Step 5: Predictions made ✅

🎉 ACCURACY: 96.7%

✨ YOU JUST RAN YOUR FIRST MACHINE LEARNING MODEL! ✨
```

**Screenshot placeholder:** *First ML model output*

### Celebration Moment!

**You just:**
1. ✅ Loaded real data (Iris flowers dataset)
2. ✅ Split data for training and testing
3. ✅ Trained a Decision Tree model
4. ✅ Made predictions
5. ✅ Achieved 96.7% accuracy!

**And you didn't need to install anything on your computer!**

---

## Saving and Organizing

### Auto-Save

- Colab auto-saves every 2-3 minutes
- Saved to: `Google Drive/Colab Notebooks/`
- Look for "All changes saved" message

**Screenshot placeholder:** *Auto-save indicator*

### Manual Save

- **File → Save** (or Ctrl/Cmd + S)
- Creates checkpoint

### Download Notebook

**Option 1: .ipynb format** (Jupyter Notebook)
1. File → Download → Download .ipynb
2. Can open in Jupyter, VS Code, etc.

**Option 2: .py format** (Python script)
1. File → Download → Download .py
2. Pure Python code

**Screenshot placeholder:** *Download options*

### Organizing in Google Drive

1. Go to Google Drive
2. Navigate to "Colab Notebooks" folder
3. Create subfolders:
   ```
   Colab Notebooks/
   ├── Module-0/
   ├── Module-1/
   ├── Module-2/
   └── Practice/
   ```
4. Move notebooks into folders

**Screenshot placeholder:** *Drive organization*

### Sharing Notebooks

1. Click **Share** button (top right)
2. Add email addresses
3. Set permissions:
   - **Viewer**: Can only view
   - **Commenter**: Can add comments
   - **Editor**: Can edit code

**Screenshot placeholder:** *Share dialog*

### Creating a Copy

1. File → Save a copy in Drive
2. Creates duplicate
3. Useful for:
   - Starting from template
   - Preserving original
   - Experimenting safely

---

## Troubleshooting

### Issue 1: "Failed to connect to runtime"

**Solutions:**
```
1. Refresh page (F5)
2. Runtime → Disconnect and delete runtime
3. Runtime → Connect
4. Clear browser cache
5. Try incognito mode
```

### Issue 2: "GPU allocation failed"

**Solutions:**
```
1. Too many users - try later
2. Your quota exceeded - wait 24 hours
3. Change to None, then back to GPU
4. Use TPU instead (if suitable)
```

### Issue 3: "Session crashed"

**Solutions:**
```
1. You exceeded RAM/GPU memory
2. Reduce batch size
3. Restart runtime: Runtime → Restart runtime
4. Save work first!
```

### Issue 4: "Cannot save to Drive"

**Solutions:**
```
1. Check Google Drive space
2. Reconnect to Google Drive:
   - Files icon → Mount Drive
3. Check internet connection
```

### Issue 5: "Library not found"

**Solutions:**
```python
# Install the library
!pip install library_name

# Then import
import library_name
```

### Issue 6: "GPU not working"

**Verify:**
```python
# Check GPU availability
import tensorflow as tf
print(tf.config.list_physical_devices('GPU'))

# If empty [], GPU not enabled
# Solution: Runtime → Change runtime type → GPU
```

**Screenshot placeholder:** *Common errors*

---

## Best Practices

### 1. Add Descriptions

Use text cells to document your code:

```markdown
## This section loads the dataset
We use the Iris dataset with 150 samples.
```

### 2. Comment Your Code

```python
# Load dataset
data = load_iris()

# Split into features (X) and target (y)
X = data.data  # 4 features: sepal/petal length/width
y = data.target  # 3 classes: setosa, versicolor, virginica
```

### 3. Print Progress

```python
print("Loading data...")
# code
print("Data loaded ✅")

print("Training model...")
# code
print("Model trained ✅")
```

### 4. Save Checkpoints

For long-running code:

```python
# Save model
import pickle
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)
print("Model saved!")
```

### 5. Use GPU Wisely

```python
# Check if GPU is needed
# For small datasets, CPU is fine
# For large datasets/deep learning, use GPU
```

### 6. Clear Outputs

Before sharing:
1. Edit → Clear all outputs
2. Removes clutter
3. Smaller file size

### 7. Keyboard Shortcuts

Learn these:
- **Shift + Enter**: Run cell and move to next
- **Ctrl + Enter**: Run cell and stay
- **Ctrl + M B**: Insert cell below
- **Ctrl + M A**: Insert cell above
- **Ctrl + M D**: Delete cell

**Screenshot placeholder:** *Keyboard shortcuts*

---

## Environment Verification Checklist

Create a new notebook called **"M0-Setup-Verification"** with:

```python
# ============================================
# ML for Engineers Course - Environment Verification
# Module 0 - Session 3
# ============================================

print("=" * 50)
print("ENVIRONMENT VERIFICATION")
print("=" * 50)

# 1. Check Python version
import sys
print(f"\n✅ Python version: {sys.version.split()[0]}")

# 2. Check GPU
import tensorflow as tf
gpus = tf.config.list_physical_devices('GPU')
if gpus:
    print(f"✅ GPU available: {gpus[0].name}")
else:
    print("❌ GPU not available (Enable: Runtime → Change runtime type → GPU)")

# 3. Check libraries
libraries = {
    'pandas': 'pd',
    'numpy': 'np',
    'sklearn': 'sklearn',
    'matplotlib': 'plt',
    'tensorflow': 'tf'
}

print("\n📚 Library Versions:")
import pandas as pd
import numpy as np
import sklearn
import matplotlib.pyplot as plt

for lib_name, alias in libraries.items():
    module = eval(alias.split('.')[0])
    version = module.__version__
    print(f"  ✅ {lib_name}: {version}")

# 4. Test ML
print("\n🧪 Testing ML Pipeline...")
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.2, random_state=42
)
model = DecisionTreeClassifier()
model.fit(X_train, y_train)
accuracy = accuracy_score(y_test, model.predict(X_test))

print(f"  ✅ ML model trained and tested")
print(f"  ✅ Accuracy: {accuracy * 100:.1f}%")

# 5. Test visualization
print("\n📊 Testing visualization...")
plt.figure(figsize=(6, 4))
plt.plot([1, 2, 3], [1, 4, 9])
plt.title("Test Plot")
plt.show()
print("  ✅ Matplotlib working")

print("\n" + "=" * 50)
print("✨ ALL SYSTEMS READY FOR ML FOR ENGINEERS! ✨")
print("=" * 50)
```

**Screenshot placeholder:** *Verification notebook output*

---

## GPU Usage Limits

### Free Tier Limits

- **Daily Usage**: ~12-15 GPU hours
- **Session Duration**: 12 hours max
- **Idle Timeout**: 90 minutes
- **RAM**: 12-13 GB
- **Disk**: ~78 GB temporary

### Tips to Maximize GPU Time

1. **Disconnect when not using**:
   ```
   Runtime → Disconnect runtime
   ```

2. **Use GPU only when needed**:
   - Small datasets: Use CPU
   - Large models: Use GPU

3. **Save checkpoints**:
   - Don't lose work if session expires

4. **Colab Pro** (Optional):
   - $9.99/month
   - Longer sessions
   - More RAM/GPU
   - Priority access
   - **Not required for this course**

---

## Quick Reference Card

### Essential Actions

| Action | Shortcut | Menu Path |
|--------|----------|-----------|
| Run cell | Shift + Enter | Cell → Run cell |
| Add code cell | Ctrl + M B | + Code button |
| Add text cell | Ctrl + M A | + Text button |
| Delete cell | Ctrl + M D | Three dots → Delete |
| Enable GPU | - | Runtime → Change runtime type |
| Restart runtime | - | Runtime → Restart runtime |
| Save | Ctrl + S | File → Save |

### Important URLs

- **Colab Home**: colab.research.google.com
- **Quick New**: colab.new
- **Colab FAQ**: [research.google.com/colaboratory/faq.html](https://research.google.com/colaboratory/faq.html)

---

## Completion Checklist

Before proceeding to next activity:

- [ ] Accessed Google Colab successfully
- [ ] Created first notebook
- [ ] Renamed and saved notebook
- [ ] Ran "Hello World" code
- [ ] Enabled GPU and verified
- [ ] Checked library versions
- [ ] Ran Iris classifier demo (96%+ accuracy)
- [ ] Created verification notebook
- [ ] Organized notebook in Google Drive
- [ ] Understand auto-save mechanism
- [ ] Know how to restart runtime

**Estimated Setup Time:** 15-20 minutes
**Difficulty:** ⭐⭐ Moderate

---

## Next Steps

1. [ ] Complete Activity 1: GPU Speed Test
2. [ ] Complete Activity 2: Environment Verification
3. [ ] Complete Activity 3: Run 5 Demo Notebooks
4. [ ] Submit verification notebook
5. [ ] Start Module 1!

---

## Version Information

**Guide Version:** 1.0
**Last Updated:** January 2026
**Valid for:** Google Colab
**Course:** ML for Engineers - Module 0

---

**🎓 Congratulations!** You now have access to FREE cloud computing with GPU for machine learning!

**Next:** Start building real ML projects in Module 1 →
