# analysis.py — Project 5: Customer Spending Pattern Analysis
# Dataset: https://archive.ics.uci.edu/dataset/352/online+retail (Online Retail.xlsx)
from typing import List, Dict, Any, Optional
import pandas as pd


def load_data(path: str) -> pd.DataFrame:
    return pd.read_excel(path, sheet_name="Online Retail", parse_dates=["InvoiceDate"])


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Drop cancelled orders (InvoiceNo starting with 'C'), missing CustomerID, non-positive Quantity/UnitPrice."""
    raise NotImplementedError("clean_data")


def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    """Derive TotalPrice = Quantity * UnitPrice, and per-customer Recency/Frequency/Monetary (RFM)."""
    raise NotImplementedError("engineer_features")


def select_features(df: pd.DataFrame, target: Optional[str] = None) -> List[str]:
    """Return the selected RFM/derived feature columns."""
    raise NotImplementedError("select_features")


def plot_monthly_revenue_trend(df: pd.DataFrame) -> None:
    """Total revenue (Quantity * UnitPrice) by month."""
    raise NotImplementedError("plot_monthly_revenue_trend")


def plot_top_countries_by_revenue(df: pd.DataFrame) -> None:
    """Bar chart, top N countries by revenue."""
    raise NotImplementedError("plot_top_countries_by_revenue")


def plot_rfm_distributions(df: pd.DataFrame) -> None:
    """Histograms of Recency, Frequency, Monetary per customer."""
    raise NotImplementedError("plot_rfm_distributions")


def plot_customer_segments(df: pd.DataFrame) -> None:
    """Scatter of Frequency vs Monetary, colored by segment."""
    raise NotImplementedError("plot_customer_segments")


def train_baseline_model(df: pd.DataFrame, features: List[str], target: Optional[str] = None) -> Any:
    """(Stretch) KMeans clustering on RFM features (unsupervised)."""
    raise NotImplementedError("train_baseline_model")


def evaluate_model(model: Any, df: pd.DataFrame, features: List[str], target: Optional[str] = None) -> Dict[str, float]:
    """(Stretch) Score the clustering (e.g. silhouette width)."""
    raise NotImplementedError("evaluate_model")


def run_pipeline(path: str) -> pd.DataFrame:
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
