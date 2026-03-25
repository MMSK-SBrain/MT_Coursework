"""
Dataset Download Script for Module 3: Regression
ML for Engineers

This script downloads all datasets needed for Module 3 regression projects:
1. Stock price data (multiple tickers)
2. House price dataset (California Housing)
3. Sales forecasting data (generated)
4. Energy consumption data (generated)
5. Salary dataset (from sklearn)

Created: 2026-01-05
"""

import os
import pandas as pd
import numpy as np
import yfinance as yf
from sklearn.datasets import fetch_california_housing, make_regression
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')


def create_directory():
    """Create data directory if it doesn't exist"""
    if not os.path.exists('data'):
        os.makedirs('data')
        print("✅ Created 'data' directory")
    else:
        print("✅ 'data' directory already exists")


def download_stock_data():
    """
    Download stock price data for multiple companies

    Downloads:
    - US stocks: AAPL, GOOGL, MSFT, TSLA, AMZN
    - Indian stocks: INFY.NS, TCS.NS, RELIANCE.NS
    """
    print("\n" + "=" * 70)
    print("1. DOWNLOADING STOCK PRICE DATA")
    print("=" * 70)

    # Stock tickers to download
    us_tickers = ['AAPL', 'GOOGL', 'MSFT', 'TSLA', 'AMZN']
    indian_tickers = ['INFY.NS', 'TCS.NS', 'RELIANCE.NS']
    all_tickers = us_tickers + indian_tickers

    # Date range: 5 years
    start_date = "2019-01-01"
    end_date = "2024-01-01"

    print(f"\nDownloading {len(all_tickers)} stocks from {start_date} to {end_date}...")

    for ticker in all_tickers:
        try:
            print(f"\n  Downloading {ticker}...", end=" ")
            data = yf.download(ticker, start=start_date, end=end_date, progress=False)

            if len(data) > 0:
                filename = f"data/stock_{ticker.replace('.', '_')}_5y.csv"
                data.to_csv(filename)
                print(f"✅ Saved ({len(data)} days)")
            else:
                print(f"❌ No data available")

        except Exception as e:
            print(f"❌ Error: {str(e)}")

    print(f"\n✅ Stock data download complete!")


def download_house_prices():
    """
    Download California Housing dataset

    Features: 8 features including median income, house age, rooms, location
    Target: Median house value
    """
    print("\n" + "=" * 70)
    print("2. DOWNLOADING HOUSE PRICE DATA")
    print("=" * 70)

    print("\nFetching California Housing dataset...")

    try:
        # Load dataset
        housing = fetch_california_housing(as_frame=True)
        df = housing.frame

        # Add feature names for clarity
        print(f"\n  Features: {list(df.columns)}")
        print(f"  Samples: {len(df)}")
        print(f"  Target: MedHouseVal (median house value in $100k)")

        # Save to CSV
        filename = "data/california_housing.csv"
        df.to_csv(filename, index=False)
        print(f"\n✅ Saved as {filename}")

        # Create data dictionary
        data_dict = """
California Housing Dataset - Data Dictionary

Source: sklearn.datasets (from 1990 California census)

Features:
1. MedInc      - Median income in block group (in $10,000s)
2. HouseAge    - Median house age in block group
3. AveRooms    - Average number of rooms per household
4. AveBedrms   - Average number of bedrooms per household
5. Population  - Block group population
6. AveOccup    - Average number of household members
7. Latitude    - Block group latitude
8. Longitude   - Block group longitude

Target:
MedHouseVal    - Median house value in block group (in $100,000s)

Total Samples: 20,640
Task: Predict median house value based on demographic and location features
"""

        with open("data/california_housing_dictionary.txt", "w") as f:
            f.write(data_dict)

        print("✅ Data dictionary saved")

    except Exception as e:
        print(f"❌ Error: {str(e)}")


def generate_sales_data():
    """
    Generate synthetic sales forecasting dataset

    Features: Month, marketing spend, seasonality, previous sales
    Target: Monthly sales
    """
    print("\n" + "=" * 70)
    print("3. GENERATING SALES FORECASTING DATA")
    print("=" * 70)

    print("\nGenerating 5 years of monthly sales data...")

    try:
        # Generate 60 months of data (5 years)
        np.random.seed(42)
        n_months = 60

        # Date range
        start_date = pd.date_range('2019-01-01', periods=n_months, freq='MS')

        # Features
        months = np.arange(1, n_months + 1)

        # Trend component (growing business)
        trend = 50000 + months * 500

        # Seasonal component (higher sales in Q4)
        seasonal = 5000 * np.sin(2 * np.pi * months / 12 + np.pi/2)

        # Marketing spend (varies month to month)
        marketing_spend = np.random.uniform(5000, 15000, n_months)
        marketing_effect = marketing_spend * 0.5

        # Random noise
        noise = np.random.normal(0, 3000, n_months)

        # Sales = trend + seasonal + marketing effect + noise
        sales = trend + seasonal + marketing_effect + noise
        sales = np.maximum(sales, 0)  # No negative sales

        # Create dataframe
        df = pd.DataFrame({
            'Date': start_date,
            'Month': months,
            'Quarter': ((months - 1) // 3) + 1,
            'MarketingSpend': marketing_spend.round(2),
            'PreviousMonthSales': np.concatenate([[np.nan], sales[:-1]]),
            'Sales': sales.round(2)
        })

        # Add rolling averages as features
        df['Sales_MA3'] = df['Sales'].rolling(window=3, min_periods=1).mean()
        df['Sales_MA6'] = df['Sales'].rolling(window=6, min_periods=1).mean()

        # Save
        filename = "data/sales_forecasting.csv"
        df.to_csv(filename, index=False)
        print(f"\n✅ Generated {len(df)} months of sales data")
        print(f"   Sales range: ${df['Sales'].min():,.0f} - ${df['Sales'].max():,.0f}")
        print(f"   Saved as {filename}")

    except Exception as e:
        print(f"❌ Error: {str(e)}")


def generate_energy_data():
    """
    Generate synthetic energy consumption dataset

    Features: Temperature, production level, day of week, time features
    Target: Energy consumption (kWh)
    """
    print("\n" + "=" * 70)
    print("4. GENERATING ENERGY CONSUMPTION DATA")
    print("=" * 70)

    print("\nGenerating 2 years of daily energy consumption data...")

    try:
        np.random.seed(42)
        n_days = 730  # 2 years

        # Date range
        dates = pd.date_range('2022-01-01', periods=n_days, freq='D')

        # Features
        day_of_year = np.arange(1, n_days + 1)

        # Temperature (sinusoidal pattern for seasons)
        temperature = 20 + 15 * np.sin(2 * np.pi * day_of_year / 365)
        temperature += np.random.normal(0, 3, n_days)

        # Production level (5 day work week)
        is_weekday = np.array([d.weekday() < 5 for d in dates])
        production_level = np.where(is_weekday,
                                    np.random.uniform(70, 100, n_days),
                                    np.random.uniform(10, 30, n_days))

        # Energy consumption
        # Base load
        base_energy = 5000

        # Temperature effect (AC in summer, heating in winter)
        temp_effect = 50 * np.abs(temperature - 20)

        # Production effect
        prod_effect = production_level * 30

        # Weekend reduction
        weekend_reduction = np.where(is_weekday, 0, -1000)

        # Noise
        noise = np.random.normal(0, 200, n_days)

        energy = base_energy + temp_effect + prod_effect + weekend_reduction + noise
        energy = np.maximum(energy, 1000)  # Minimum consumption

        # Create dataframe
        df = pd.DataFrame({
            'Date': dates,
            'Temperature': temperature.round(1),
            'IsWeekday': is_weekday.astype(int),
            'DayOfWeek': [d.weekday() for d in dates],
            'Month': [d.month for d in dates],
            'ProductionLevel': production_level.round(1),
            'EnergyConsumption': energy.round(2)
        })

        # Add lagged features
        df['Energy_Lag1'] = df['EnergyConsumption'].shift(1)
        df['Energy_Lag7'] = df['EnergyConsumption'].shift(7)

        # Save
        filename = "data/energy_consumption.csv"
        df.to_csv(filename, index=False)
        print(f"\n✅ Generated {len(df)} days of energy data")
        print(f"   Energy range: {df['EnergyConsumption'].min():,.0f} - {df['EnergyConsumption'].max():,.0f} kWh")
        print(f"   Saved as {filename}")

    except Exception as e:
        print(f"❌ Error: {str(e)}")


def generate_salary_data():
    """
    Generate synthetic salary dataset

    Features: Years experience, education level, job role, location
    Target: Annual salary
    """
    print("\n" + "=" * 70)
    print("5. GENERATING SALARY DATA")
    print("=" * 70)

    print("\nGenerating salary dataset...")

    try:
        np.random.seed(42)
        n_samples = 5000

        # Features
        years_experience = np.random.uniform(0, 30, n_samples)

        education_level = np.random.choice(['Bachelors', 'Masters', 'PhD'],
                                          size=n_samples,
                                          p=[0.6, 0.3, 0.1])

        job_role = np.random.choice(['Engineer', 'Manager', 'Analyst', 'Senior Engineer', 'Director'],
                                   size=n_samples,
                                   p=[0.35, 0.25, 0.25, 0.1, 0.05])

        location = np.random.choice(['Urban', 'Suburban', 'Rural'],
                                   size=n_samples,
                                   p=[0.5, 0.35, 0.15])

        # Salary calculation
        base_salary = 50000

        # Experience effect
        exp_effect = years_experience * 2000

        # Education effect
        edu_effect = {'Bachelors': 0, 'Masters': 15000, 'PhD': 30000}
        edu_bonus = np.array([edu_effect[e] for e in education_level])

        # Role effect
        role_effect = {'Analyst': 0, 'Engineer': 10000, 'Senior Engineer': 30000,
                      'Manager': 40000, 'Director': 70000}
        role_bonus = np.array([role_effect[r] for r in job_role])

        # Location effect
        loc_effect = {'Rural': 0, 'Suburban': 10000, 'Urban': 25000}
        loc_bonus = np.array([loc_effect[l] for l in location])

        # Noise
        noise = np.random.normal(0, 5000, n_samples)

        salary = base_salary + exp_effect + edu_bonus + role_bonus + loc_bonus + noise
        salary = np.maximum(salary, 30000)  # Minimum salary

        # Create dataframe
        df = pd.DataFrame({
            'YearsExperience': years_experience.round(1),
            'EducationLevel': education_level,
            'JobRole': job_role,
            'Location': location,
            'AnnualSalary': salary.round(2)
        })

        # Save
        filename = "data/salary_data.csv"
        df.to_csv(filename, index=False)
        print(f"\n✅ Generated {len(df)} salary records")
        print(f"   Salary range: ${df['AnnualSalary'].min():,.0f} - ${df['AnnualSalary'].max():,.0f}")
        print(f"   Saved as {filename}")

    except Exception as e:
        print(f"❌ Error: {str(e)}")


def create_master_readme():
    """Create README with information about all datasets"""
    readme_content = """# Module 3 Regression Datasets
## ML for Engineers

This directory contains all datasets for Module 3: Regression projects.

---

## Datasets Included

### 1. Stock Price Data
**Files:** `stock_AAPL_5y.csv`, `stock_GOOGL_5y.csv`, etc.
**Source:** Yahoo Finance (via yfinance)
**Period:** 2019-2024 (5 years)
**Features:** Open, High, Low, Close, Volume, Adj Close
**Use Case:** Stock price prediction (THE PAYOFF PROJECT!)
**Stocks Included:**
- US: AAPL, GOOGL, MSFT, TSLA, AMZN
- India: INFY.NS, TCS.NS, RELIANCE.NS

### 2. California Housing
**File:** `california_housing.csv`
**Source:** sklearn (1990 CA census)
**Samples:** 20,640
**Features:** 8 (income, house age, rooms, location, etc.)
**Target:** Median house value
**Use Case:** House price prediction

### 3. Sales Forecasting
**File:** `sales_forecasting.csv`
**Source:** Synthetic (generated)
**Samples:** 60 months (5 years)
**Features:** Marketing spend, seasonality, previous sales
**Target:** Monthly sales
**Use Case:** Business forecasting

### 4. Energy Consumption
**File:** `energy_consumption.csv`
**Source:** Synthetic (generated)
**Samples:** 730 days (2 years)
**Features:** Temperature, production level, day of week
**Target:** Energy consumption (kWh)
**Use Case:** Manufacturing energy prediction

### 5. Salary Data
**File:** `salary_data.csv`
**Source:** Synthetic (generated)
**Samples:** 5,000
**Features:** Experience, education, role, location
**Target:** Annual salary
**Use Case:** Salary prediction

---

## How to Download

### Option 1: Run Download Script (Recommended)
```bash
python download_all_datasets.py
```

### Option 2: Manual Download
Run individual sections of the download script for specific datasets.

### Option 3: Use in Notebook
```python
import pandas as pd

# Load stock data
aapl = pd.read_csv('data/stock_AAPL_5y.csv', index_col=0, parse_dates=True)

# Load house prices
housing = pd.read_csv('data/california_housing.csv')

# etc.
```

---

## Requirements

```bash
pip install pandas numpy yfinance scikit-learn
```

---

## Dataset Statistics

| Dataset | Samples | Features | Target Range | Task Type |
|---------|---------|----------|--------------|-----------|
| Stock (AAPL) | ~1,250 | 6 (OHLCV) | $30-200 | Time Series |
| California Housing | 20,640 | 8 | $15k-500k | Cross-sectional |
| Sales | 60 | 7 | $40k-90k | Time Series |
| Energy | 730 | 7 | 3k-12k kWh | Time Series |
| Salary | 5,000 | 4 | $30k-300k | Cross-sectional |

---

## License Information

- **Stock Data:** Yahoo Finance data subject to their terms of use
- **California Housing:** Public domain (US Census data)
- **Synthetic Datasets:** Free to use for educational purposes

---

## Data Quality Notes

### Stock Data
- ✅ Real market data
- ⚠️  May have missing days (market closures)
- ⚠️  Subject to market volatility

### Synthetic Data (Sales, Energy, Salary)
- ✅ Clean, no missing values
- ✅ Designed for learning
- ⚠️  Not real data (for practice only)

---

## Support

For issues with datasets:
1. Ensure you have internet connection (for stock download)
2. Check that required libraries are installed
3. Re-run download script
4. Consult course forums

---

**Created:** 2026-01-05
**Module:** 3 - Regression
**Course:** ML for Engineers
"""

    with open("data/README.md", "w") as f:
        f.write(readme_content)

    print("\n✅ Master README created")


def main():
    """Main function to download all datasets"""
    print("=" * 70)
    print("MODULE 3 REGRESSION DATASETS DOWNLOAD")
    print("ML for Engineers")
    print("=" * 70)
    print("\nThis script will download all datasets needed for Module 3.")
    print("Estimated time: 2-5 minutes")
    print("Internet connection required for stock data.")

    input("\nPress Enter to start downloading...")

    # Create directory
    create_directory()

    # Download/generate all datasets
    download_stock_data()
    download_house_prices()
    generate_sales_data()
    generate_energy_data()
    generate_salary_data()

    # Create README
    create_master_readme()

    # Summary
    print("\n" + "=" * 70)
    print("DOWNLOAD COMPLETE! 🎉")
    print("=" * 70)
    print("\nAll datasets are ready in the 'data/' directory:")
    print("  📊 Stock data (8 files)")
    print("  🏠 California housing (1 file)")
    print("  💰 Sales forecasting (1 file)")
    print("  ⚡ Energy consumption (1 file)")
    print("  💵 Salary data (1 file)")
    print("  📖 README and documentation")

    print("\n✅ You're ready to build regression models!")
    print("\nNext steps:")
    print("  1. Explore the datasets")
    print("  2. Try the feature engineering library")
    print("  3. Build the stock predictor!")
    print("\n" + "=" * 70)


if __name__ == "__main__":
    main()
