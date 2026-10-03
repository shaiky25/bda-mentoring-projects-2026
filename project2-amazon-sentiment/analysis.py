# analysis.py — Project 2: Amazon Fine Food Reviews Sentiment
# Dataset: https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews
from typing import List, Dict, Any
import pandas as pd


def load_data(path: str) -> pd.DataFrame:
    """Loads the raw Amazon Fine Food Reviews dataset from a CSV file.

    Args:
        path (str): Path to the reviews CSV file.

    Returns:
        pd.DataFrame: The raw, unmodified dataset.
    """
    return pd.read_csv(path)


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Drops duplicate/empty reviews, normalizes encoding, and coerces Time.

    Args:
        df (pd.DataFrame): Raw data frame returned by load_data.

    Returns:
        pd.DataFrame: Cleaned data frame with Time coerced to a date.

    Raises:
        NotImplementedError: Always, until implemented by the student.
    """
    raise NotImplementedError("clean_data")


def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    """Derives review length, helpfulness ratio, and a sentiment label.

    Args:
        df (pd.DataFrame): Cleaned data frame returned by clean_data.

    Returns:
        pd.DataFrame: Data frame with added review_length, helpfulness_ratio,
            and sentiment_label (positive/negative, derived from Score)
            columns.

    Raises:
        NotImplementedError: Always, until implemented by the student.
    """
    raise NotImplementedError("engineer_features")


def select_features(df: pd.DataFrame, target: str = "sentiment_label") -> List[str]:
    """Selects the numeric/derived columns (not raw text) to carry forward.

    Args:
        df (pd.DataFrame): Engineered data frame returned by engineer_features.
        target (str, optional): Name of the sentiment label column. Defaults
            to "sentiment_label".

    Returns:
        List[str]: Names of the selected feature columns.

    Raises:
        NotImplementedError: Always, until implemented by the student.
    """
    raise NotImplementedError("select_features")


def plot_score_distribution(df: pd.DataFrame) -> None:
    """Plots a bar chart of star ratings (1-5).

    Args:
        df (pd.DataFrame): Data frame to visualize.

    Returns:
        None.

    Raises:
        NotImplementedError: Always, until implemented by the student.
    """
    raise NotImplementedError("plot_score_distribution")


def plot_review_length_distribution(df: pd.DataFrame) -> None:
    """Plots a histogram of review text length.

    Args:
        df (pd.DataFrame): Data frame to visualize.

    Returns:
        None.

    Raises:
        NotImplementedError: Always, until implemented by the student.
    """
    raise NotImplementedError("plot_review_length_distribution")


def plot_wordcloud_by_sentiment(df: pd.DataFrame) -> None:
    """Plots word clouds for positive (score >= 4) vs negative (score <= 2) reviews.

    Args:
        df (pd.DataFrame): Data frame to visualize.

    Returns:
        None.

    Raises:
        NotImplementedError: Always, until implemented by the student.
    """
    raise NotImplementedError("plot_wordcloud_by_sentiment")


def plot_sentiment_over_time(df: pd.DataFrame) -> None:
    """Plots review volume/sentiment trend over Time.

    Args:
        df (pd.DataFrame): Data frame to visualize.

    Returns:
        None.

    Raises:
        NotImplementedError: Always, until implemented by the student.
    """
    raise NotImplementedError("plot_sentiment_over_time")


def train_baseline_model(df: pd.DataFrame, features: List[str], target: str = "sentiment_label") -> Any:
    """(Stretch) Trains a TF-IDF + Naive Bayes baseline on Text -> sentiment_label.

    Args:
        df (pd.DataFrame): Selected-feature data frame.
        features (List[str]): Names of the feature columns to use.
        target (str, optional): Name of the sentiment label column. Defaults
            to "sentiment_label".

    Returns:
        Any: A fitted model object.

    Raises:
        NotImplementedError: Always, until implemented by the student.
    """
    raise NotImplementedError("train_baseline_model")


def evaluate_model(model: Any, df: pd.DataFrame, features: List[str], target: str = "sentiment_label") -> Dict[str, float]:
    """(Stretch) Scores the sentiment classifier.

    Args:
        model (Any): A fitted model object from train_baseline_model.
        df (pd.DataFrame): Data frame to evaluate against.
        features (List[str]): Names of the feature columns used by the model.
        target (str, optional): Name of the sentiment label column. Defaults
            to "sentiment_label".

    Returns:
        Dict[str, float]: Metric name to value (e.g. accuracy, f1).

    Raises:
        NotImplementedError: Always, until implemented by the student.
    """
    raise NotImplementedError("evaluate_model")


def run_pipeline(path: str) -> pd.DataFrame:
    """Runs the full analysis pipeline end-to-end.

    Loads the dataset, cleans it, engineers features, selects features,
    and produces each required visualization in order.

    Args:
        path (str): Path to the reviews CSV file.

    Returns:
        pd.DataFrame: The cleaned, feature-engineered data frame.
    """
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
