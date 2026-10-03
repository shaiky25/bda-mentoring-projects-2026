# analysis.py — Project 1: Diabetes Risk Screening
# Dataset: https://www.kaggle.com/datasets/jamaltariqcheema/pima-indians-diabetes-dataset
from typing import List, Dict, Any
import pandas as pd


def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Handle missing/impossible values (glucose/bmi == 0 is missing, not real)."""
    raise NotImplementedError("clean_data")


def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    """Derive new columns useful for analysis (e.g. bmi_category, age_group)."""
    raise NotImplementedError("engineer_features")


def select_features(df: pd.DataFrame, target: str = "Outcome") -> List[str]:
    """Return the feature column names chosen for downstream analysis/modeling."""
    raise NotImplementedError("select_features")


def plot_feature_distributions(df: pd.DataFrame) -> None:
    """Faceted histograms of all numeric features."""
    raise NotImplementedError("plot_feature_distributions")


def plot_correlation_heatmap(df: pd.DataFrame) -> None:
    """Correlation matrix heatmap across numeric features."""
    raise NotImplementedError("plot_correlation_heatmap")


def plot_outcome_balance(df: pd.DataFrame) -> None:
    """Bar chart of Outcome class counts (0/1)."""
    raise NotImplementedError("plot_outcome_balance")


def plot_glucose_vs_bmi_by_outcome(df: pd.DataFrame) -> None:
    """Scatter of Glucose vs BMI, colored by Outcome."""
    raise NotImplementedError("plot_glucose_vs_bmi_by_outcome")


def train_baseline_model(df: pd.DataFrame, features: List[str], target: str = "Outcome") -> Any:
    """(Stretch) Train a baseline classifier."""
    raise NotImplementedError("train_baseline_model")


def evaluate_model(model: Any, df: pd.DataFrame, features: List[str], target: str = "Outcome") -> Dict[str, float]:
    """(Stretch) Score the model; return e.g. {'accuracy': ..., 'auc': ...}."""
    raise NotImplementedError("evaluate_model")


def run_pipeline(path: str) -> pd.DataFrame:
    df = load_data(path)
    df = clean_data(df)
    df = engineer_features(df)
    features = select_features(df)
    plot_feature_distributions(df)
    plot_correlation_heatmap(df)
    plot_outcome_balance(df)
    plot_glucose_vs_bmi_by_outcome(df)
    return df


if __name__ == "__main__":
    run_pipeline("diabetes.csv")
