# Capstone Project: Dataset Sources

## General Dataset Repositories

### 1. Kaggle (kaggle.com/datasets)
**Best for:** All types of ML projects
- 50,000+ datasets
- Competitions with prize money
- Kernels (code examples)
- **Popular datasets:** Titanic, House Prices, MNIST, CIFAR-10

### 2. UCI Machine Learning Repository
**URL:** archive.ics.uci.edu/ml
**Best for:** Classic ML datasets, academic research
- 500+ datasets
- Well-documented
- Frequently cited in research

### 3. Google Dataset Search
**URL:** datasetsearch.research.google.com
**Best for:** Finding datasets across the web
- Searches billions of datasets
- Links to original sources

### 4. AWS Open Data Registry
**URL:** registry.opendata.aws
**Best for:** Large-scale datasets
- Petabyte-scale datasets
- Free to use on AWS

### 5. Papers With Code
**URL:** paperswithcode.com/datasets
**Best for:** State-of-the-art models and benchmarks
- Datasets from research papers
- Benchmarks included

---

## Domain-Specific Sources

### Finance & Trading
- **Yahoo Finance:** yfinance library (stock data)
- **Alpha Vantage:** Free stock API
- **Quandl:** Financial and economic data
- **Federal Reserve (FRED):** Economic data
- **Kaggle:** Credit card fraud, stock prices

### Sports (Cricket, Football, etc.)
- **Cricsheet.org:** Cricket ball-by-ball data
- **ESPN Cricinfo:** Stats (scraping required)
- **Football-Data.co.uk:** Football match results
- **Kaggle:** IPL, sports prediction datasets

### Healthcare & Medical
- **NIH Data Sharing:** health data
- **Kaggle:** Chest X-rays, diabetes, heart disease
- **PhysioNet:** Medical time series data
- **ISIC:** Skin lesion images
- **MIMIC:** ICU patient data (requires approval)

### E-commerce & Retail
- **Kaggle:** Online Retail, Brazilian E-commerce
- **Instacart:** Grocery shopping dataset
- **Amazon Reviews:** Product reviews
- **TheLook E-commerce:** Synthetic e-commerce data

### Manufacturing & IoT
- **NASA:** Turbofan engine degradation
- **Microsoft Azure:** Predictive maintenance
- **Kaggle:** Steel defects, casting defects
- **PHM Society:** Prognostics datasets

### Images (Computer Vision)
- **ImageNet:** 14M+ images (requires registration)
- **COCO:** Object detection dataset
- **Open Images:** 9M+ images by Google
- **Kaggle:** Dogs vs Cats, CIFAR-10, Fashion MNIST

### Text (NLP)
- **Hugging Face Datasets:** 10,000+ datasets
- **Common Crawl:** Web crawl data
- **Wikipedia Dumps:** Full Wikipedia text
- **Kaggle:** IMDB reviews, Twitter sentiment
- **Stanford NLP:** Various text datasets

---

## Quick Reference by Project Type

### Stock Trading System
- Yahoo Finance (yfinance)
- Alpha Vantage API
- Kaggle: Stock Price Prediction datasets

### Cricket Analytics
- Cricsheet.org (ball-by-ball)
- Kaggle: IPL datasets
- ESPN Cricinfo (web scraping)

### Healthcare Diagnostic
- Kaggle: Chest X-ray Pneumonia
- Kaggle: Diabetes/Heart Disease
- ISIC: Skin Cancer

### E-commerce Intelligence
- UCI: Online Retail Dataset
- Kaggle: Brazilian E-commerce
- Instacart Market Basket

### Manufacturing QC
- Kaggle: Casting Product Defects
- Kaggle: Steel Surface Defects
- NASA: Turbofan Engine Data

---

## Dataset Evaluation Checklist

Before committing to a dataset:
- [ ] Download a sample to verify access
- [ ] Check size (enough samples?)
- [ ] Verify features (relevant to problem?)
- [ ] Review license (can you use it?)
- [ ] Check quality (missing data < 30%?)
- [ ] Find documentation or data dictionary
- [ ] Identify backup source if primary fails

---

## Creating Synthetic Data

If you can't find a dataset, consider generating synthetic data:

```python
from sklearn.datasets import make_classification, make_regression
import pandas as pd
import numpy as np

# Classification data
X, y = make_classification(
    n_samples=10000,
    n_features=20,
    n_informative=15,
    n_redundant=5,
    random_state=42
)

# Regression data
X, y = make_regression(
    n_samples=5000,
    n_features=10,
    noise=0.1,
    random_state=42
)

# Time series
dates = pd.date_range('2020-01-01', periods=1000)
values = np.cumsum(np.random.randn(1000)) + 100
df = pd.DataFrame({'date': dates, 'value': values})
```

---

## Web Scraping (Use Responsibly!)

**Legal & Ethical Guidelines:**
- Check robots.txt
- Respect rate limits
- Don't overload servers
- Verify terms of service
- Consider API first

**Tools:**
- Beautiful Soup
- Scrapy
- Selenium (for JavaScript sites)

**When to scrape:**
- Data not available elsewhere
- For educational purposes
- With proper attribution

---

## Data Licenses to Look For

- **CC0 (Public Domain):** Use freely
- **CC-BY:** Use with attribution
- **MIT:** Permissive
- **Open Database License:** Free to use
- **Academic Use Only:** OK for capstone
- **Commercial Use Prohibited:** Usually OK for education

**Avoid:**
- Proprietary data without permission
- Personal data (GDPR concerns)
- Data requiring payment

---

*Remember: Verify data access BEFORE choosing your project!*
