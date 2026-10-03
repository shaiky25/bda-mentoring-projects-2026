# analysis.R — Project 3: Crop Recommendation from Soil Data
# Dataset: https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset
library(tidyverse)
library(corrplot)
library(GGally)

#' Load the raw crop recommendation dataset
#'
#' @param path Path to the crop recommendation CSV file.
#' @return The raw, unmodified data frame.
load_data <- function(path) {
  read_csv(path)
}

#' Check value ranges and drop/impute out-of-range or NA rows
#'
#' @param df Raw data frame returned by load_data.
#' @return Cleaned data frame with the same columns (e.g. ph constrained to
#'   the valid 0-14 range).
#' @note Currently unimplemented; always stops with "Not implemented".
clean_data <- function(df) {
  stop("Not implemented: clean_data")
}

#' Derive ratios/bins useful downstream
#'
#' @param df Cleaned data frame returned by clean_data.
#' @return Data frame with additional engineered columns (e.g. npk_ratio,
#'   rainfall_level).
#' @note Currently unimplemented; always stops with "Not implemented".
engineer_features <- function(df) {
  stop("Not implemented: engineer_features")
}

#' Select the numeric feature columns to carry forward
#'
#' @param df Engineered data frame returned by engineer_features.
#' @param target Name of the crop label column. Defaults to "label".
#' @return Character vector of selected column names.
#' @note Currently unimplemented; always stops with "Not implemented".
select_features <- function(df, target = "label") {
  stop("Not implemented: select_features")
}

#' Plot histograms of N, P, and K
#'
#' @param df Data frame to visualize.
#' @return None; produces a plot as a side effect.
#' @note Currently unimplemented; always stops with "Not implemented".
plot_nutrient_distributions <- function(df) {
  stop("Not implemented: plot_nutrient_distributions")
}

#' Plot a correlation matrix heatmap across numeric features
#'
#' @param df Data frame to visualize.
#' @return None; produces a plot as a side effect.
#' @note Currently unimplemented; always stops with "Not implemented".
plot_correlation_heatmap <- function(df) {
  stop("Not implemented: plot_correlation_heatmap")
}

#' Plot a bar chart of crop (label) frequency
#'
#' @param df Data frame to visualize.
#' @return None; produces a plot as a side effect.
#' @note Currently unimplemented; always stops with "Not implemented".
plot_crop_counts <- function(df) {
  stop("Not implemented: plot_crop_counts")
}

#' Plot a scatter of pH vs rainfall, colored by crop
#'
#' @param df Data frame to visualize.
#' @return None; produces a plot as a side effect.
#' @note Currently unimplemented; always stops with "Not implemented".
plot_ph_vs_rainfall_by_crop <- function(df) {
  stop("Not implemented: plot_ph_vs_rainfall_by_crop")
}

#' (Stretch) Train a kNN or random forest classifier predicting crop label
#'
#' @param df Selected-feature data frame.
#' @param features Character vector of feature column names to use.
#' @param target Name of the crop label column. Defaults to "label".
#' @return A fitted model object.
#' @note Currently unimplemented; always stops with "Not implemented".
train_baseline_model <- function(df, features, target = "label") {
  stop("Not implemented: train_baseline_model")
}

#' (Stretch) Score the crop classifier
#'
#' @param model A fitted model object from train_baseline_model.
#' @param df Data frame to evaluate against.
#' @param features Character vector of feature columns used by the model.
#' @param target Name of the crop label column. Defaults to "label".
#' @return Named list/vector of metrics (e.g. accuracy).
#' @note Currently unimplemented; always stops with "Not implemented".
evaluate_model <- function(model, df, features, target = "label") {
  stop("Not implemented: evaluate_model")
}

#' Run the full analysis pipeline end-to-end
#'
#' Loads the dataset, cleans it, engineers features, selects features,
#' and produces each required visualization in order.
#'
#' @param path Path to the crop recommendation CSV file.
#' @return The cleaned, feature-engineered data frame (invisibly).
run_pipeline <- function(path) {
  df <- load_data(path)
  df <- clean_data(df)
  df <- engineer_features(df)
  features <- select_features(df)
  plot_nutrient_distributions(df)
  plot_correlation_heatmap(df)
  plot_crop_counts(df)
  plot_ph_vs_rainfall_by_crop(df)
  invisible(df)
}
