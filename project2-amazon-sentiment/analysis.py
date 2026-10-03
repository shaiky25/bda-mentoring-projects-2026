# analysis.py — Project 2: Amazon Fine Food Reviews Sentiment
# Dataset: https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews
from typing import List, Dict, Any
import pandas as pd


def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Drop duplicate/empty reviews, normalize encoding, coerce Time to a date."""
    raise NotImplementedError("clean_data")


def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    """Derive review_length, helpfulness_ratio, and a positive/negative sentiment_label from Score."""
    raise NotImplementedError("engineer_features")


def select_features(df: pd.DataFrame, target: str = "sentiment_label") -> List[str]:
    """Select the numeric/derived columns (not raw text) to carry forward."""
    raise NotImplementedError("select_features")


def plot_score_distribution(df: pd.DataFrame) -> None:
    """Bar chart of star ratings (1-5)."""
    raise NotImplementedError("plot_score_distribution")


def plot_review_length_distribution(df: pd.DataFrame) -> None:
    """Histogram of review text length."""
    raise NotImplementedError("plot_review_length_distribution")


def plot_wordcloud_by_sentiment(df: pd.DataFrame) -> None:
    """Word clouds for positive (score >= 4) vs negative (score <= 2) reviews."""
    raise NotImplementedError("plot_wordcloud_by_sentiment")


def plot_sentiment_over_time(df: pd.DataFrame) -> None:
    """Review volume/sentiment trend over Time."""
    raise NotImplementedError("plot_sentiment_over_time")


def train_baseline_model(df: pd.DataFrame, features: List[str], target: str = "sentiment_label") -> Any:
    """(Stretch) TF-IDF + Naive Bayes baseline on Text -> sentiment_label."""
    raise NotImplementedError("train_baseline_model")


def evaluate_model(model: Any, df: pd.DataFrame, features: List[str], target: str = "sentiment_label") -> Dict[str, float]:
    """(Stretch) Score the sentiment classifier; return e.g. {'accuracy': ..., 'f1': ...}."""
    raise NotImplementedError("evaluate_model")


def run_pipeline(path: str) -> pd.DataFrame:
    df = load_data(path)
    df = clean_data(df)
    df = engineer_features(df)
    features = select_features(df)
    plot_score_distribution(df)
    plot_review_length_distribution(df)
    plot_wordcloud_by_sentiment(df)
    plot_sentiment_over_time(df)
    return df


if __name__ == "__main__":
    run_pipeline("amazon_fine_food_reviews.csv")
