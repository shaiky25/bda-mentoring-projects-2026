# analysis.py — Project 5: Customer Spending Pattern Analysis
# Dataset: https://archive.ics.uci.edu/dataset/352/online+retail (Online Retail.xlsx)
from typing import List, Dict, Any, Optional
import pandas as pd


def load_data(path: str) -> pd.DataFrame:
    """Loads the raw Online Retail dataset from its Excel workbook.

    Args:
        path (str): Path to the online_retail.xlsx file.

    Returns:
        pd.DataFrame: The raw dataset from the "Online Retail" sheet, with
            InvoiceDate parsed as a date.
    """
    return pd.read_excel(path, sheet_name="Online Retail", parse_dates=["InvoiceDate"])


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Drops cancelled orders and invalid rows.

    Args:
        df (pd.DataFrame): Raw data frame returned by load_data.

    Returns:
        pd.DataFrame: Cleaned data frame with cancelled orders
            (InvoiceNo starting with "C"), missing CustomerID, and
            non-positive Quantity/UnitPrice rows removed.

    Raises:
        NotImplementedError: Always, until implemented by the student.
    """
    raise NotImplementedError("clean_data")


def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    """Derives TotalPrice and per-customer RFM features.

    Args:
        df (pd.DataFrame): Cleaned data frame returned by clean_data.

    Returns:
        pd.DataFrame: Data frame with TotalPrice (Quantity * UnitPrice) and
            per-customer Recency, Frequency, and Monetary columns.

    Raises:
        NotImplementedError: Always, until implemented by the student.
    """
    raise NotImplementedError("engineer_features")


def select_features(df: pd.DataFrame, target: Optional[str] = None) -> List[str]:
    """Selects the RFM/derived feature columns to carry forward.

    Args:
        df (pd.DataFrame): Engineered data frame returned by engineer_features.
        target (str, optional): Unused; this is an unsupervised task, so
            there is no target column. Defaults to None.

    Returns:
        List[str]: Names of the selected feature columns.

    Raises:
        NotImplementedError: Always, until implemented by the student.
    """
    raise NotImplementedError("select_features")


def plot_monthly_revenue_trend(df: pd.DataFrame) -> None:
    """Plots total revenue (Quantity * UnitPrice) by month.

    Args:
        df (pd.DataFrame): Data frame to visualize.

    Returns:
        None.

    Raises:
        NotImplementedError: Always, until implemented by the student.
    """
    raise NotImplementedError("plot_monthly_revenue_trend")


def plot_top_countries_by_revenue(df: pd.DataFrame) -> None:
    """Plots a bar chart of the top N countries by revenue.

    Args:
        df (pd.DataFrame): Data frame to visualize.

    Returns:
        None.

    Raises:
        NotImplementedError: Always, until implemented by the student.
    """
    raise NotImplementedError("plot_top_countries_by_revenue")


def plot_rfm_distributions(df: pd.DataFrame) -> None:
    """Plots histograms of Recency, Frequency, and Monetary per customer.

    Args:
        df (pd.DataFrame): Data frame to visualize.

    Returns:
        None.

    Raises:
        NotImplementedError: Always, until implemented by the student.
    """
    raise NotImplementedError("plot_rfm_distributions")


def plot_customer_segments(df: pd.DataFrame) -> None:
    """Plots a scatter of Frequency vs Monetary, colored by segment.

    Args:
        df (pd.DataFrame): Data frame to visualize.

    Returns:
        None.

    Raises:
        NotImplementedError: Always, until implemented by the student.
    """
    raise NotImplementedError("plot_customer_segments")


def train_baseline_model(df: pd.DataFrame, features: List[str], target: Optional[str] = None) -> Any:
    """(Stretch) Runs KMeans clustering on RFM features (unsupervised).

    Args:
        df (pd.DataFrame): Selected-feature data frame.
        features (List[str]): Names of the feature columns to use.
        target (str, optional): Unused; clustering is unsupervised. Defaults
            to None.

    Returns:
        Any: A fitted clustering model object.

    Raises:
        NotImplementedError: Always, until implemented by the student.
    """
    raise NotImplementedError("train_baseline_model")


def evaluate_model(model: Any, df: pd.DataFrame, features: List[str], target: Optional[str] = None) -> Dict[str, float]:
    """(Stretch) Scores the clustering.

    Args:
        model (Any): A fitted clustering model from train_baseline_model.
        df (pd.DataFrame): Data frame to evaluate against.
        features (List[str]): Names of the feature columns used by the model.
        target (str, optional): Unused; clustering is unsupervised. Defaults
            to None.

    Returns:
        Dict[str, float]: Metric name to value (e.g. silhouette width).

    Raises:
        NotImplementedError: Always, until implemented by the student.
    """
    raise NotImplementedError("evaluate_model")


def run_pipeline(path: str) -> pd.DataFrame:
    """Runs the full analysis pipeline end-to-end.

    Loads the dataset, cleans it, engineers features, selects features,
    and produces each required visualization in order.

    Args:
        path (str): Path to the online_retail.xlsx file.

    Returns:
        pd.DataFrame: The cleaned, feature-engineered data frame.
    """
    df = load_data(path)
    df = clean_data(df)
    df = engineer_features(df)
    features = select_features(df)
    plot_monthly_revenue_trend(df)
    plot_top_countries_by_revenue(df)
    plot_rfm_distributions(df)
    plot_customer_segments(df)
    return df


if __name__ == "__main__":
    run_pipeline("online_retail.xlsx")
