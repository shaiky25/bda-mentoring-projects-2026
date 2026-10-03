# analysis.py — Project 4: Rain Prediction (Australia)
# Dataset: https://www.kaggle.com/datasets/jsphyg/weather-dataset-rattle-package
from typing import List, Dict, Any
import pandas as pd


def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path, parse_dates=["Date"])


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Drop columns with excessive missingness, impute/drop remaining NAs."""
    raise NotImplementedError("clean_data")


def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    """Derive e.g. temp_range = MaxTemp - MinTemp, month from Date."""
    raise NotImplementedError("engineer_features")


def select_features(df: pd.DataFrame, target: str = "RainTomorrow") -> List[str]:
    """Select feature columns (drop high-missingness/low-signal ones)."""
    raise NotImplementedError("select_features")


def plot_missingness(df: pd.DataFrame) -> None:
    """Missing-value bar/heatmap per column."""
    raise NotImplementedError("plot_missingness")


def plot_temp_trend_over_time(df: pd.DataFrame) -> None:
    """MinTemp/MaxTemp line trend over Date."""
    raise NotImplementedError("plot_temp_trend_over_time")


def plot_rain_tomorrow_balance(df: pd.DataFrame) -> None:
    """Bar chart of RainTomorrow class counts."""
    raise NotImplementedError("plot_rain_tomorrow_balance")


def plot_humidity_vs_pressure_by_rain(df: pd.DataFrame) -> None:
    """Scatter of humidity vs pressure, colored by RainTomorrow."""
    raise NotImplementedError("plot_humidity_vs_pressure_by_rain")


def train_baseline_model(df: pd.DataFrame, features: List[str], target: str = "RainTomorrow") -> Any:
    """(Stretch) Logistic regression predicting RainTomorrow."""
    raise NotImplementedError("train_baseline_model")


def evaluate_model(model: Any, df: pd.DataFrame, features: List[str], target: str = "RainTomorrow") -> Dict[str, float]:
    """(Stretch) Score the rain classifier; return e.g. {'accuracy': ..., 'auc': ...}."""
    raise NotImplementedError("evaluate_model")


def run_pipeline(path: str) -> pd.DataFrame:
    df = load_data(path)
    df = clean_data(df)
    df = engineer_features(df)
    features = select_features(df)
    plot_missingness(df)
    plot_temp_trend_over_time(df)
    plot_rain_tomorrow_balance(df)
    plot_humidity_vs_pressure_by_rain(df)
    return df


if __name__ == "__main__":
    run_pipeline("weatherAUS.csv")
