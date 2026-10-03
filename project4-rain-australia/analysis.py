# analysis.py — Project 4: Rain Prediction (Australia)
# Dataset: https://www.kaggle.com/datasets/jsphyg/weather-dataset-rattle-package
from typing import List, Dict, Any
import pandas as pd


def load_data(path: str) -> pd.DataFrame:
    """Loads the raw Rain in Australia dataset from a CSV file.

    Args:
        path (str): Path to the weatherAUS CSV file.

    Returns:
        pd.DataFrame: The raw dataset, with Date parsed as a date.
    """
    return pd.read_csv(path, parse_dates=["Date"])


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Drops columns with excessive missingness and handles remaining NAs.

    Args:
        df (pd.DataFrame): Raw data frame returned by load_data.

    Returns:
        pd.DataFrame: Cleaned data frame with high-missingness columns
            dropped and remaining NAs imputed or dropped.

    Raises:
        NotImplementedError: Always, until implemented by the student.
    """
    raise NotImplementedError("clean_data")


def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    """Derives new columns useful for analysis.

    Args:
        df (pd.DataFrame): Cleaned data frame returned by clean_data.

    Returns:
        pd.DataFrame: Data frame with additional engineered columns
            (e.g. temp_range = MaxTemp - MinTemp, month from Date).

    Raises:
        NotImplementedError: Always, until implemented by the student.
    """
    raise NotImplementedError("engineer_features")


def select_features(df: pd.DataFrame, target: str = "RainTomorrow") -> List[str]:
    """Selects feature columns, dropping high-missingness/low-signal ones.

    Args:
        df (pd.DataFrame): Engineered data frame returned by engineer_features.
        target (str, optional): Name of the target column. Defaults to
            "RainTomorrow".

    Returns:
        List[str]: Names of the selected feature columns.

    Raises:
        NotImplementedError: Always, until implemented by the student.
    """
    raise NotImplementedError("select_features")


def plot_missingness(df: pd.DataFrame) -> None:
    """Plots a missing-value bar/heatmap per column.

    Args:
        df (pd.DataFrame): Data frame to visualize.

    Returns:
        None.

    Raises:
        NotImplementedError: Always, until implemented by the student.
    """
    raise NotImplementedError("plot_missingness")


def plot_temp_trend_over_time(df: pd.DataFrame) -> None:
    """Plots a MinTemp/MaxTemp line trend over Date.

    Args:
        df (pd.DataFrame): Data frame to visualize.

    Returns:
        None.

    Raises:
        NotImplementedError: Always, until implemented by the student.
    """
    raise NotImplementedError("plot_temp_trend_over_time")


def plot_rain_tomorrow_balance(df: pd.DataFrame) -> None:
    """Plots a bar chart of RainTomorrow class counts.

    Args:
        df (pd.DataFrame): Data frame to visualize.

    Returns:
        None.

    Raises:
        NotImplementedError: Always, until implemented by the student.
    """
    raise NotImplementedError("plot_rain_tomorrow_balance")


def plot_humidity_vs_pressure_by_rain(df: pd.DataFrame) -> None:
    """Plots a scatter of humidity vs pressure, colored by RainTomorrow.

    Args:
        df (pd.DataFrame): Data frame to visualize.

    Returns:
        None.

    Raises:
        NotImplementedError: Always, until implemented by the student.
    """
    raise NotImplementedError("plot_humidity_vs_pressure_by_rain")


def train_baseline_model(df: pd.DataFrame, features: List[str], target: str = "RainTomorrow") -> Any:
    """(Stretch) Trains a logistic regression predicting RainTomorrow.

    Args:
        df (pd.DataFrame): Selected-feature data frame.
        features (List[str]): Names of the feature columns to use.
        target (str, optional): Name of the target column. Defaults to
            "RainTomorrow".

    Returns:
        Any: A fitted model object.

    Raises:
        NotImplementedError: Always, until implemented by the student.
    """
    raise NotImplementedError("train_baseline_model")


def evaluate_model(model: Any, df: pd.DataFrame, features: List[str], target: str = "RainTomorrow") -> Dict[str, float]:
    """(Stretch) Scores the rain classifier.

    Args:
        model (Any): A fitted model object from train_baseline_model.
        df (pd.DataFrame): Data frame to evaluate against.
        features (List[str]): Names of the feature columns used by the model.
        target (str, optional): Name of the target column. Defaults to
            "RainTomorrow".

    Returns:
        Dict[str, float]: Metric name to value (e.g. accuracy, auc).

    Raises:
        NotImplementedError: Always, until implemented by the student.
    """
    raise NotImplementedError("evaluate_model")


def run_pipeline(path: str) -> pd.DataFrame:
    """Runs the full analysis pipeline end-to-end.

    Loads the dataset, cleans it, engineers features, selects features,
    and produces each required visualization in order.

    Args:
        path (str): Path to the weatherAUS CSV file.

    Returns:
        pd.DataFrame: The cleaned, feature-engineered data frame.
    """
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
