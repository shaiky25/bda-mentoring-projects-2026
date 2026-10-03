# analysis.R — Project 3: Crop Recommendation from Soil Data
# Dataset: https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset
library(tidyverse)
library(corrplot)
library(GGally)

load_data <- function(path) {
  read_csv(path)
}

#' Check ranges (e.g. ph should be 0-14), drop/impute out-of-range or NA rows
clean_data <- function(df) {
  stop("Not implemented: clean_data")
}

#' Derive any ratios/bins useful downstream (e.g. npk_ratio, rainfall_level)
engineer_features <- function(df) {
  stop("Not implemented: engineer_features")
}

#' @return character vector of selected numeric feature columns
select_features <- function(df, target = "label") {
  stop("Not implemented: select_features")
}

#' Histograms of N, P, K
plot_nutrient_distributions <- function(df) {
  stop("Not implemented: plot_nutrient_distributions")
}

#' Correlation matrix heatmap across numeric features
plot_correlation_heatmap <- function(df) {
  stop("Not implemented: plot_correlation_heatmap")
}

#' Bar chart of crop (label) frequency
plot_crop_counts <- function(df) {
  stop("Not implemented: plot_crop_counts")
}

#' Scatter of pH vs rainfall, colored by crop
plot_ph_vs_rainfall_by_crop <- function(df) {
  stop("Not implemented: plot_ph_vs_rainfall_by_crop")
}

#' (Stretch) kNN or random forest classifier predicting crop label
train_baseline_model <- function(df, features, target = "label") {
  stop("Not implemented: train_baseline_model")
}

#' (Stretch) Score the crop classifier
#' @return named list/vector of metrics (e.g. accuracy)
evaluate_model <- function(model, df, features, target = "label") {
  stop("Not implemented: evaluate_model")
}

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
