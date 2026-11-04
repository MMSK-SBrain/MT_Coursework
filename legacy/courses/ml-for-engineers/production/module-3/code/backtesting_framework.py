"""
Backtesting Framework for Time Series Regression
ML for Engineers - Module 3: Regression

This framework provides tools for properly testing time series models
to avoid data leakage and get realistic performance estimates.

Created: 2026-01-05
"""

import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns


class TimeSeriesBacktester:
    """
    Backtesting framework for time series regression models

    Features:
    - Walk-forward validation
    - Rolling window backtesting
    - Expanding window backtesting
    - Performance tracking over time
    - Visual analytics
    """

    def __init__(self, model, window_size=250, step_size=20):
        """
        Initialize backtester

        Parameters:
        -----------
        model : sklearn model
            ML model with fit() and predict() methods
        window_size : int
            Size of training window (default: 250 trading days ≈ 1 year)
        step_size : int
            Number of days to step forward (default: 20 ≈ 1 month)
        """
        self.model = model
        self.window_size = window_size
        self.step_size = step_size
        self.results = []

    def rolling_window_backtest(self, X, y, verbose=True):
        """
        Perform rolling window backtest

        Train on fixed window, predict next period, move window forward.

        Parameters:
        -----------
        X : pd.DataFrame
            Features (with datetime index)
        y : pd.Series
            Target variable (with datetime index)
        verbose : bool
            Print progress (default: True)

        Returns:
        --------
        pd.DataFrame
            Results with predictions and metrics
        """
        if verbose:
            print("=" * 70)
            print("ROLLING WINDOW BACKTEST")
            print("=" * 70)
            print(f"\nWindow size: {self.window_size} days")
            print(f"Step size: {self.step_size} days")

        # Store all predictions
        all_predictions = []

        # Starting point
        start_idx = self.window_size

        while start_idx + self.step_size <= len(X):
            # Define windows
            train_start = start_idx - self.window_size
            train_end = start_idx
            test_start = start_idx
            test_end = min(start_idx + self.step_size, len(X))

            # Get train and test data
            X_train = X.iloc[train_start:train_end]
            y_train = y.iloc[train_start:train_end]
            X_test = X.iloc[test_start:test_end]
            y_test = y.iloc[test_start:test_end]

            # Train model
            self.model.fit(X_train, y_train)

            # Make predictions
            predictions = self.model.predict(X_test)

            # Store results
            for i, (date, actual, pred) in enumerate(zip(y_test.index, y_test.values, predictions)):
                all_predictions.append({
                    'Date': date,
                    'Actual': actual,
                    'Predicted': pred,
                    'Error': actual - pred,
                    'Abs_Error': abs(actual - pred),
                    'Squared_Error': (actual - pred) ** 2,
                    'Train_Start': X_train.index[0],
                    'Train_End': X_train.index[-1]
                })

            if verbose and len(all_predictions) % 100 == 0:
                print(f"  Processed {len(all_predictions)} predictions...")

            # Move window forward
            start_idx += self.step_size

        # Create results dataframe
        results_df = pd.DataFrame(all_predictions)
        results_df.set_index('Date', inplace=True)

        # Calculate overall metrics
        mae = mean_absolute_error(results_df['Actual'], results_df['Predicted'])
        rmse = np.sqrt(mean_squared_error(results_df['Actual'], results_df['Predicted']))
        r2 = r2_score(results_df['Actual'], results_df['Predicted'])

        if verbose:
            print(f"\n✅ Backtest complete!")
            print(f"   Total predictions: {len(results_df)}")
            print(f"   Date range: {results_df.index[0].date()} to {results_df.index[-1].date()}")
            print(f"\n📊 Overall Performance:")
            print(f"   MAE:  ${mae:.2f}")
            print(f"   RMSE: ${rmse:.2f}")
            print(f"   R²:   {r2:.4f}")

        self.results = results_df
        return results_df

    def expanding_window_backtest(self, X, y, initial_window=250, verbose=True):
        """
        Perform expanding window backtest

        Train on all data up to point, predict next period, expand window.

        Parameters:
        -----------
        X : pd.DataFrame
            Features (with datetime index)
        y : pd.Series
            Target variable
        initial_window : int
            Initial training window size
        verbose : bool
            Print progress

        Returns:
        --------
        pd.DataFrame
            Results with predictions
        """
        if verbose:
            print("=" * 70)
            print("EXPANDING WINDOW BACKTEST")
            print("=" * 70)
            print(f"\nInitial window: {initial_window} days")
            print(f"Step size: {self.step_size} days")

        all_predictions = []
        start_idx = initial_window

        while start_idx + self.step_size <= len(X):
            # Train on all data from beginning to current point
            X_train = X.iloc[:start_idx]
            y_train = y.iloc[:start_idx]

            # Test on next period
            test_end = min(start_idx + self.step_size, len(X))
            X_test = X.iloc[start_idx:test_end]
            y_test = y.iloc[start_idx:test_end]

            # Train and predict
            self.model.fit(X_train, y_train)
            predictions = self.model.predict(X_test)

            # Store results
            for date, actual, pred in zip(y_test.index, y_test.values, predictions):
                all_predictions.append({
                    'Date': date,
                    'Actual': actual,
                    'Predicted': pred,
                    'Error': actual - pred,
                    'Train_Size': len(X_train)
                })

            if verbose and len(all_predictions) % 100 == 0:
                print(f"  Processed {len(all_predictions)} predictions...")

            start_idx += self.step_size

        results_df = pd.DataFrame(all_predictions)
        results_df.set_index('Date', inplace=True)

        # Metrics
        mae = mean_absolute_error(results_df['Actual'], results_df['Predicted'])
        rmse = np.sqrt(mean_squared_error(results_df['Actual'], results_df['Predicted']))
        r2 = r2_score(results_df['Actual'], results_df['Predicted'])

        if verbose:
            print(f"\n✅ Backtest complete!")
            print(f"   Total predictions: {len(results_df)}")
            print(f"\n📊 Overall Performance:")
            print(f"   MAE:  ${mae:.2f}")
            print(f"   RMSE: ${rmse:.2f}")
            print(f"   R²:   {r2:.4f}")

        self.results = results_df
        return results_df

    def plot_results(self, title="Backtest Results"):
        """
        Visualize backtest results

        Parameters:
        -----------
        title : str
            Plot title
        """
        if len(self.results) == 0:
            print("⚠️  No results to plot. Run backtest first!")
            return

        fig, axes = plt.subplots(3, 1, figsize=(15, 12), sharex=True)

        # 1. Actual vs Predicted
        axes[0].plot(self.results.index, self.results['Actual'],
                    label='Actual', linewidth=2, alpha=0.8)
        axes[0].plot(self.results.index, self.results['Predicted'],
                    label='Predicted', linewidth=2, alpha=0.7, linestyle='--')
        axes[0].set_title(title, fontsize=16, fontweight='bold')
        axes[0].set_ylabel('Price ($)', fontsize=12)
        axes[0].legend(fontsize=11)
        axes[0].grid(True, alpha=0.3)

        # 2. Prediction Errors
        axes[1].scatter(self.results.index, self.results['Error'],
                       alpha=0.5, s=30)
        axes[1].axhline(y=0, color='red', linestyle='--', linewidth=2)
        axes[1].set_title('Prediction Errors (Residuals)', fontsize=14, fontweight='bold')
        axes[1].set_ylabel('Error ($)', fontsize=12)
        axes[1].grid(True, alpha=0.3)

        # 3. Rolling RMSE
        window = 20  # 20-day rolling window
        rolling_rmse = np.sqrt(
            self.results['Squared_Error'].rolling(window=window).mean()
        )
        axes[2].plot(self.results.index, rolling_rmse,
                    linewidth=2, color='red')
        axes[2].set_title(f'Rolling RMSE ({window}-day window)',
                         fontsize=14, fontweight='bold')
        axes[2].set_ylabel('RMSE ($)', fontsize=12)
        axes[2].set_xlabel('Date', fontsize=12)
        axes[2].grid(True, alpha=0.3)

        plt.tight_layout()
        plt.show()

    def calculate_metrics_by_period(self, period='M'):
        """
        Calculate metrics by time period

        Parameters:
        -----------
        period : str
            Pandas resample period ('D', 'W', 'M', 'Q', 'Y')

        Returns:
        --------
        pd.DataFrame
            Metrics by period
        """
        if len(self.results) == 0:
            print("⚠️  No results. Run backtest first!")
            return None

        # Group by period
        period_metrics = self.results.groupby(pd.Grouper(freq=period)).agg({
            'Abs_Error': 'mean',
            'Squared_Error': lambda x: np.sqrt(x.mean()),
            'Error': ['mean', 'std', 'min', 'max']
        })

        period_metrics.columns = ['MAE', 'RMSE', 'Mean_Error', 'Std_Error',
                                  'Min_Error', 'Max_Error']

        # Calculate R² per period
        r2_by_period = []
        for period_start in period_metrics.index:
            period_data = self.results[self.results.index >= period_start]
            if len(period_data) > 0:
                period_end = period_data.index[0] + pd.DateOffset(months=1)
                period_data = period_data[period_data.index < period_end]
                if len(period_data) > 1:
                    r2 = r2_score(period_data['Actual'], period_data['Predicted'])
                else:
                    r2 = np.nan
            else:
                r2 = np.nan
            r2_by_period.append(r2)

        period_metrics['R2'] = r2_by_period

        return period_metrics

    def compare_to_baseline(self):
        """
        Compare model performance to baseline (predict yesterday's price)

        Returns:
        --------
        dict
            Comparison metrics
        """
        if len(self.results) == 0:
            print("⚠️  No results. Run backtest first!")
            return None

        # Baseline: Predict yesterday's price (shift actual by 1)
        # This is a naive forecast
        baseline_predictions = self.results['Actual'].shift(1).dropna()
        actuals = self.results['Actual'].loc[baseline_predictions.index]

        baseline_mae = mean_absolute_error(actuals, baseline_predictions)
        baseline_rmse = np.sqrt(mean_squared_error(actuals, baseline_predictions))
        baseline_r2 = r2_score(actuals, baseline_predictions)

        model_mae = mean_absolute_error(self.results['Actual'], self.results['Predicted'])
        model_rmse = np.sqrt(mean_squared_error(self.results['Actual'], self.results['Predicted']))
        model_r2 = r2_score(self.results['Actual'], self.results['Predicted'])

        print("=" * 70)
        print("MODEL vs BASELINE COMPARISON")
        print("=" * 70)
        print(f"\n📊 Baseline (Yesterday's Price):")
        print(f"   MAE:  ${baseline_mae:.2f}")
        print(f"   RMSE: ${baseline_rmse:.2f}")
        print(f"   R²:   {baseline_r2:.4f}")

        print(f"\n📊 Our Model:")
        print(f"   MAE:  ${model_mae:.2f}")
        print(f"   RMSE: ${model_rmse:.2f}")
        print(f"   R²:   {model_r2:.4f}")

        improvement = ((baseline_rmse - model_rmse) / baseline_rmse) * 100
        print(f"\n🎯 Improvement:")
        print(f"   RMSE: {improvement:.2f}%")
        print(f"   {'✅ Model beats baseline!' if model_rmse < baseline_rmse else '❌ Baseline is better'}")

        return {
            'baseline_mae': baseline_mae,
            'baseline_rmse': baseline_rmse,
            'baseline_r2': baseline_r2,
            'model_mae': model_mae,
            'model_rmse': model_rmse,
            'model_r2': model_r2,
            'improvement_pct': improvement
        }


def prevent_data_leakage_guide():
    """
    Print guide on preventing data leakage in time series
    """
    print("=" * 70)
    print("PREVENTING DATA LEAKAGE IN TIME SERIES")
    print("=" * 70)

    print("\n❌ WRONG: Using future data to predict past")
    print("   Example: Using today's price to predict yesterday")

    print("\n❌ WRONG: Shuffling time series data")
    print("   Example: train_test_split(X, y, shuffle=True)")

    print("\n❌ WRONG: Feature engineering with future information")
    print("   Example: Calculating moving average including future points")

    print("\n✅ RIGHT: Time-aware splitting")
    print("   Example: Train on 2019-2022, test on 2023")

    print("\n✅ RIGHT: Proper feature engineering")
    print("   Example: MA only uses past values, shift target forward")

    print("\n✅ RIGHT: Walk-forward validation")
    print("   Example: Rolling window backtest")

    print("\n✅ RIGHT: Check for data leakage")
    print("   Question: 'Could I have known this at prediction time?'")

    print("\n" + "=" * 70)


if __name__ == "__main__":
    print("Backtesting Framework for Time Series")
    print("=" * 70)
    print("\nAvailable classes and functions:")
    print("  - TimeSeriesBacktester(model, window_size, step_size)")
    print("  - rolling_window_backtest()")
    print("  - expanding_window_backtest()")
    print("  - plot_results()")
    print("  - calculate_metrics_by_period()")
    print("  - compare_to_baseline()")
    print("  - prevent_data_leakage_guide()")
    print("\nFor detailed usage, see documentation and examples.")
    print("\nRemember: NEVER use future data to predict the past!")
