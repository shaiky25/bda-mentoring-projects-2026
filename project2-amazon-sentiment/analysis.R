# analysis.R — Project 2: Amazon Fine Food Reviews Sentiment
# Dataset: https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews
library(tidyverse)
library(tidytext)
library(textdata)
library(wordcloud)
library(tm)

load_data <- function(path) {
  read_csv(path)
}

#' Drop duplicate/empty reviews, normalize encoding, coerce Time to a date
clean_data <- function(df) {
  stop("Not implemented: clean_data")
}

#' Derive review_length, helpfulness_ratio, and a positive/negative sentiment_label from Score
engineer_features <- function(df) {
  stop("Not implemented: engineer_features")
}

#' Select the numeric/derived columns (not raw text) to carry forward
#' @return character vector of selected column names
select_features <- function(df, target = "sentiment_label") {
  stop("Not implemented: select_features")
}

#' Bar chart of star ratings (1-5)
plot_score_distribution <- function(df) {
  stop("Not implemented: plot_score_distribution")
}

#' Histogram of review text length
plot_review_length_distribution <- function(df) {
  stop("Not implemented: plot_review_length_distribution")
}

#' Word clouds for positive (score >= 4) vs negative (score <= 2) reviews
plot_wordcloud_by_sentiment <- function(df) {
  stop("Not implemented: plot_wordcloud_by_sentiment")
}

#' Review volume/sentiment trend over Time
plot_sentiment_over_time <- function(df) {
  stop("Not implemented: plot_sentiment_over_time")
}

#' (Stretch) TF-IDF + Naive Bayes baseline on Text -> sentiment_label
train_baseline_model <- function(df, features, target = "sentiment_label") {
  stop("Not implemented: train_baseline_model")
}

#' (Stretch) Score the sentiment classifier
#' @return named list/vector of metrics (e.g. accuracy, f1)
evaluate_model <- function(model, df, features, target = "sentiment_label") {
  stop("Not implemented: evaluate_model")
}

run_pipeline <- function(path) {
  df <- load_data(path)
  df <- clean_data(df)
  df <- engineer_features(df)
  features <- select_features(df)
  plot_score_distribution(df)
  plot_review_length_distribution(df)
  plot_wordcloud_by_sentiment(df)
  plot_sentiment_over_time(df)
  invisible(df)
}
