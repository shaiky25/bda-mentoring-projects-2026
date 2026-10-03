# analysis.py — Project 3: Crop Recommendation from Soil Data
# Dataset: https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset
from typing import List, Dict, Any
import pandas as pd


def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Check ranges (e.g. ph 0-14), drop/impute out-of-range or NA rows."""
    raise NotImplementedError("clean_data")


def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    """Derive any ratios/bins useful downstream (e.g. npk_ratio, rainfall_level)."""
    raise NotImplementedError("engineer_features")


def select_features(df: pd.DataFrame, target: str = "label") -> List[str]:
    """Return the selected numeric feature columns."""
    raise NotImplementedError("select_features")


def plot_nutrient_distributions(df: pd.DataFrame) -> None:
    """Histograms of N, P, K."""
    raise NotImplementedError("plot_nutrient_distributions")


def plot_correlation_heatmap(df: pd.DataFrame) -> None:
    """Correlation matrix heatmap across numeric features."""
    raise NotImplementedError("plot_correlation_heatmap")


def plot_crop_counts(df: pd.DataFrame) -> None:
    """Bar chart of crop (label) frequency."""
    raise NotImplementedError("plot_crop_counts")


def plot_ph_vs_rainfall_by_crop(df: pd.DataFrame) -> None:
    """Scatter of pH vs rainfall, colored by crop."""
    raise NotImplementedError("plot_ph_vs_rainfall_by_crop")


def train_baseline_model(df: pd.DataFrame, features: List[str], target: str = "label") -> Any:
    """(Stretch) kNN or random forest classifier predicting crop label."""
    raise NotImplementedError("train_baseline_model")


def evaluate_model(model: Any, df: pd.DataFrame, features: List[str], target: str = "label") -> Dict[str, float]:
    """(Stretch) Score the crop classifier; return e.g. {'accuracy': ...}."""
    raise NotImplementedError("evaluate_model")


def run_pipeline(path: str) -> pd.DataFrame:
    df = load_data(path)
    df = clean_data(df)
    df = engineer_features(df)
    features = select_features(df)
    plot_nutrient_distributions(df)
    plot_correlation_heatmap(df)
    plot_crop_counts(df)
    plot_ph_vs_rainfall_by_crop(df)
    return df


if __name__ == "__main__":
    run_pipeline("crop_recommendation.csv")
