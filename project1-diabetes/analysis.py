# analysis.py — Project 1: Diabetes Risk Screening
# Dataset: https://www.kaggle.com/datasets/jamaltariqcheema/pima-indians-diabetes-dataset
from typing import List, Dict, Any
import pandas as pd


def load_data(path: str) -> pd.DataFrame:
    """Loads the raw Pima Indians Diabetes dataset from a CSV file.

    Args:
        path (str): Path to the diabetes CSV file.

    Returns:
        pd.DataFrame: The raw, unmodified dataset.
    """
    return pd.read_csv(path)


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Handles missing or impossible values in the raw dataset.

    Columns such as Glucose and BMI record 0 for missing measurements,
    not a true zero, and must be treated as missing here.

    Args:
        df (pd.DataFrame): Raw data frame returned by load_data.

    Returns:
        pd.DataFrame: Cleaned data frame with the same columns.

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
            (e.g. bmi_category, age_group).

    Raises:
        NotImplementedError: Always, until implemented by the student.
    """
    raise NotImplementedError("engineer_features")


def select_features(df: pd.DataFrame, target: str = "Outcome") -> List[str]:
    """Chooses the feature columns to carry into visualization/modeling.

    Args:
        df (pd.DataFrame): Engineered data frame returned by engineer_features.
        target (str, optional): Name of the outcome column. Defaults to
            "Outcome".

    Returns:
        List[str]: Names of the selected feature columns.

    Raises:
        NotImplementedError: Always, until implemented by the student.
    """
    raise NotImplementedError("select_features")


def plot_feature_distributions(df: pd.DataFrame) -> None:
    """Plots faceted histograms of all numeric features.

    Args:
        df (pd.DataFrame): Data frame to visualize.

    Returns:
        None.

    Raises:
        NotImplementedError: Always, until implemented by the student.
    """
    raise NotImplementedError("plot_feature_distributions")


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


def plot_outcome_balance(df: pd.DataFrame) -> None:
    """Plots a bar chart of Outcome class counts (0/1).

    Args:
        df (pd.DataFrame): Data frame to visualize.

    Returns:
        None.

    Raises:
        NotImplementedError: Always, until implemented by the student.
    """
    raise NotImplementedError("plot_outcome_balance")


def plot_glucose_vs_bmi_by_outcome(df: pd.DataFrame) -> None:
    """Plots a scatter of Glucose vs BMI, colored by Outcome.

    Args:
        df (pd.DataFrame): Data frame to visualize.

    Returns:
        None.

    Raises:
        NotImplementedError: Always, until implemented by the student.
    """
    raise NotImplementedError("plot_glucose_vs_bmi_by_outcome")


def train_baseline_model(df: pd.DataFrame, features: List[str], target: str = "Outcome") -> Any:
    """(Stretch) Trains a baseline classifier on the selected features.

    Args:
        df (pd.DataFrame): Selected-feature data frame.
        features (List[str]): Names of the feature columns to use.
        target (str, optional): Name of the outcome column. Defaults to
            "Outcome".

    Returns:
        Any: A fitted model object.

    Raises:
        NotImplementedError: Always, until implemented by the student.
    """
    raise NotImplementedError("train_baseline_model")


def evaluate_model(model: Any, df: pd.DataFrame, features: List[str], target: str = "Outcome") -> Dict[str, float]:
    """(Stretch) Scores the trained model.

    Args:
        model (Any): A fitted model object from train_baseline_model.
        df (pd.DataFrame): Data frame to evaluate against.
        features (List[str]): Names of the feature columns used by the model.
        target (str, optional): Name of the outcome column. Defaults to
            "Outcome".

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
        path (str): Path to the diabetes CSV file.

    Returns:
        pd.DataFrame: The cleaned, feature-engineered data frame.
    """
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
