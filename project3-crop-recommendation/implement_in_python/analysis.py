# analysis.py — Project 3: Crop Recommendation from Soil Data
# Dataset: https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset
from typing import List, Dict, Any
import pandas as pd


def load_data(path: str) -> pd.DataFrame:
    """Loads the raw crop recommendation dataset from a CSV file.

    Args:
        path (str): Path to the crop recommendation CSV file.

    Returns:
        pd.DataFrame: The raw, unmodified dataset.
    """
    return pd.read_csv(path)


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Checks value ranges and drops/imputes out-of-range or NA rows.

    Args:
        df (pd.DataFrame): Raw data frame returned by load_data.

    Returns:
        pd.DataFrame: Cleaned data frame with the same columns (e.g. ph
            constrained to the valid 0-14 range).

    Raises:
        NotImplementedError: Always, until implemented by the student.
    """
    raise NotImplementedError("clean_data")


def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    """Derives ratios/bins useful downstream.

    Args:
        df (pd.DataFrame): Cleaned data frame returned by clean_data.

    Returns:
        pd.DataFrame: Data frame with additional engineered columns
            (e.g. npk_ratio, rainfall_level).

    Raises:
        NotImplementedError: Always, until implemented by the student.
    """
    raise NotImplementedError("engineer_features")


def select_features(df: pd.DataFrame, target: str = "label") -> List[str]:
    """Selects the numeric feature columns to carry forward.

    Args:
        df (pd.DataFrame): Engineered data frame returned by engineer_features.
        target (str, optional): Name of the crop label column. Defaults to
            "label".

    Returns:
        List[str]: Names of the selected feature columns.

    Raises:
        NotImplementedError: Always, until implemented by the student.
    """
    raise NotImplementedError("select_features")


def plot_nutrient_distributions(df: pd.DataFrame) -> None:
    """Plots histograms of N, P, and K.

    Args:
        df (pd.DataFrame): Data frame to visualize.

    Returns:
        None.

    Raises:
        NotImplementedError: Always, until implemented by the student.
    """
    raise NotImplementedError("plot_nutrient_distributions")


def plot_correlation_heatmap(df: pd.DataFrame) -> None:
    """Plots a correlation matrix heatmap across numeric features.

    Args:
        df (pd.DataFrame): Data frame to visualize.

    Returns:
        None.

    Raises:
        NotImplementedError: Always, until implemented by the student.
    """
    raise NotImplementedError("plot_correlation_heatmap")


def plot_crop_counts(df: pd.DataFrame) -> None:
    """Plots a bar chart of crop (label) frequency.

    Args:
        df (pd.DataFrame): Data frame to visualize.

    Returns:
        None.

    Raises:
        NotImplementedError: Always, until implemented by the student.
    """
    raise NotImplementedError("plot_crop_counts")


def plot_ph_vs_rainfall_by_crop(df: pd.DataFrame) -> None:
    """Plots a scatter of pH vs rainfall, colored by crop.

    Args:
        df (pd.DataFrame): Data frame to visualize.

    Returns:
        None.

    Raises:
        NotImplementedError: Always, until implemented by the student.
    """
    raise NotImplementedError("plot_ph_vs_rainfall_by_crop")


def train_baseline_model(df: pd.DataFrame, features: List[str], target: str = "label") -> Any:
    """(Stretch) Trains a kNN or random forest classifier predicting crop label.

    Args:
        df (pd.DataFrame): Selected-feature data frame.
        features (List[str]): Names of the feature columns to use.
        target (str, optional): Name of the crop label column. Defaults to
            "label".

    Returns:
        Any: A fitted model object.

    Raises:
        NotImplementedError: Always, until implemented by the student.
    """
    raise NotImplementedError("train_baseline_model")


def evaluate_model(model: Any, df: pd.DataFrame, features: List[str], target: str = "label") -> Dict[str, float]:
    """(Stretch) Scores the crop classifier.

    Args:
        model (Any): A fitted model object from train_baseline_model.
        df (pd.DataFrame): Data frame to evaluate against.
        features (List[str]): Names of the feature columns used by the model.
        target (str, optional): Name of the crop label column. Defaults to
            "label".

    Returns:
        Dict[str, float]: Metric name to value (e.g. accuracy).

    Raises:
        NotImplementedError: Always, until implemented by the student.
    """
    raise NotImplementedError("evaluate_model")


def run_pipeline(path: str) -> pd.DataFrame:
    """Runs the full analysis pipeline end-to-end.

    Loads the dataset, cleans it, engineers features, selects features,
    and produces each required visualization in order.

    Args:
        path (str): Path to the crop recommendation CSV file.

    Returns:
        pd.DataFrame: The cleaned, feature-engineered data frame.
    """
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
