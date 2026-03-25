---
course_code: ML-ENG-M0
module_number: 0
module_title: "The Hook - Welcome to Machine Learning"
duration: "1 week"
video_content: "~4.5 hours"
hands_on_time: "~2-3 hours"
theory_practice_ratio: "70% / 30%"
last_updated: 2026-01-05
version: 2.0
---

# Module 0: The Hook - Welcome to Machine Learning

Welcome to the exciting world of Machine Learning! This introductory module will show you why ML matters and get you hands-on with real applications.

## Session 1: The 5 Amazing Demos

In this session, we'll explore five practical ML applications that demonstrate the power and versatility of machine learning.

### Demo 1: Stock Price Predictor

See how ML can analyze historical stock data to predict future trends.

![Stock Predictor Dashboard](../images/module-0/demo-stock-predictor.png "Interactive stock prediction interface")

Key features:
- Historical data visualization
- Trend analysis
- Future price predictions
- Confidence intervals

```python
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Load stock data
data = pd.read_csv('stock_prices.csv')

# Create model
model = LinearRegression()
model.fit(data[['day']], data['price'])

# Predict next day
next_price = model.predict([[len(data) + 1]])
print(f"Predicted price: ${next_price[0]:.2f}")
```

### Demo 2: Cricket Match Predictor

Predict cricket match outcomes using team statistics and historical performance data.

Features:
- Team performance analysis
- Head-to-head statistics
- Weather and venue factors
- Real-time predictions

### Demo 3: Face Detection

Real-time face detection using computer vision and deep learning.

![Face Detection Demo](../images/module-0/demo-face-detection.png)

This demo shows how ML can:
- Detect faces in images
- Identify facial features
- Work with live camera feeds
- Handle multiple faces

## Session 2: Setting Up Your Environment

Let's get you set up with the tools you'll need for this course.

### Google Colab Setup

Google Colab provides free cloud-based Jupyter notebooks with GPU access.

Steps to get started:
1. Visit [Google Colab](https://colab.research.google.com)
2. Sign in with your Google account
3. Create a new notebook
4. You're ready to code!

![Google Colab Interface](../images/module-0/colab-interface.png "Clean and intuitive interface")

#### Why Colab?

- **Free GPU Access**: Train models faster
- **No Installation**: Everything runs in the browser
- **Pre-installed Libraries**: Most ML libraries already available
- **Easy Sharing**: Share notebooks with teammates

### Installing Required Libraries

While Colab comes with many libraries pre-installed, you may need to install additional packages:

```python
# Install additional packages
!pip install scikit-learn
!pip install matplotlib
!pip install seaborn
```

## Session 3: GPU Computing Introduction

Understanding GPU acceleration for machine learning.

### What is a GPU?

A Graphics Processing Unit (GPU) is designed for parallel processing, making it ideal for ML computations.

| Feature | CPU | GPU |
|---------|-----|-----|
| Cores | 4-16 | 1000+ |
| Speed | High per core | Lower per core |
| Best For | Sequential tasks | Parallel tasks |
| ML Training | Slow | Fast |

### Enabling GPU in Colab

To enable GPU acceleration:
1. Go to Runtime > Change runtime type
2. Select "GPU" from Hardware accelerator dropdown
3. Click Save

Your models will now train significantly faster!

## Module Summary

Congratulations! You've completed Module 0. You should now:

- Understand what ML can do (through demos)
- Have a working Colab environment
- Know how to use GPU acceleration
- Be excited to learn more!

<!-- INSTRUCTOR ONLY -->
## Video Production Notes

- Keep demo sessions under 10 minutes each
- Show live demos, not just screenshots
- Encourage students to try demos themselves

### For Instructors

Remember to emphasize the practical applications in Session 1. Students should leave feeling excited and motivated.
<!-- END INSTRUCTOR ONLY -->

## Next Steps

In Module 1, we'll dive into data exploration and learn how to work with datasets using Python and Pandas.

Ready to continue? Let's go!
