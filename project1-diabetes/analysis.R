# analysis.R — Project 1: Diabetes Risk Screening
# Dataset: https://www.kaggle.com/datasets/jamaltariqcheema/pima-indians-diabetes-dataset
library(tidyverse)
library(corrplot)
library(caret)

#' Load the raw Pima Indians Diabetes dataset
#'
#' @param path Path to the diabetes CSV file.
#' @return The raw, unmodified data frame.
load_data <- function(path) {
  read_csv(path)
}

#' Handle missing or impossible values in the raw dataset
#'
#' Columns such as Glucose and BMI record 0 for missing measurements,
#' not a true zero, and must be treated as missing here.
#'
#' @param df Raw data frame returned by load_data.
#' @return Cleaned data frame with the same columns.
#' @note Currently unimplemented; always stops with "Not implemented".
clean_data <- function(df) {
  stop("Not implemented: clean_data")
}

#' Derive new columns useful for analysis
#'
#' @param df Cleaned data frame returned by clean_data.
#' @return Data frame with additional engineered columns (e.g. bmi_category,
#'   age_group).
#' @note Currently unimplemented; always stops with "Not implemented".
engineer_features <- function(df) {
  stop("Not implemented: engineer_features")
}

#' Choose the feature columns to carry into visualization/modeling
#'
#' @param df Engineered data frame returned by engineer_features.
#' @param target Name of the outcome column. Defaults to "Outcome".
#' @return Character vector of selected column names.
#' @note Currently unimplemented; always stops with "Not implemented".
select_features <- function(df, target = "Outcome") {
  stop("Not implemented: select_features")
}

#' Plot faceted histograms of all numeric features
#'
#' @param df Data frame to visualize.
#' @return None; produces a plot as a side effect.
#' @note Currently unimplemented; always stops with "Not implemented".
plot_feature_distributions <- function(df) {
  stop("Not implemented: plot_feature_distributions")
}

#' Plot a correlation matrix heatmap across numeric features
#'
#' @param df Data frame to visualize.
#' @return None; produces a plot as a side effect.
#' @note Currently unimplemented; always stops with "Not implemented".
plot_correlation_heatmap <- function(df) {
  stop("Not implemented: plot_correlation_heatmap")
}

#' Plot a bar chart of Outcome class counts (0/1)
#'
#' @param df Data frame to visualize.
#' @return None; produces a plot as a side effect.
#' @note Currently unimplemented; always stops with "Not implemented".
plot_outcome_balance <- function(df) {
  stop("Not implemented: plot_outcome_balance")
}

#' Plot a scatter of Glucose vs BMI, colored by Outcome
#'
#' @param df Data frame to visualize.
#' @return None; produces a plot as a side effect.
#' @note Currently unimplemented; always stops with "Not implemented".
plot_glucose_vs_bmi_by_outcome <- function(df) {
  stop("Not implemented: plot_glucose_vs_bmi_by_outcome")
}

#' (Stretch) Train a baseline classifier on the selected features
#'
#' @param df Selected-feature data frame.
#' @param features Character vector of feature column names to use.
#' @param target Name of the outcome column. Defaults to "Outcome".
#' @return A fitted model object.
#' @note Currently unimplemented; always stops with "Not implemented".
train_baseline_model <- function(df, features, target = "Outcome") {
  stop("Not implemented: train_baseline_model")
}

#' (Stretch) Score the trained model
#'
#' @param model A fitted model object from train_baseline_model.
#' @param df Data frame to evaluate against.
#' @param features Character vector of feature columns used by the model.
#' @param target Name of the outcome column. Defaults to "Outcome".
#' @return Named list/vector of metrics (e.g. accuracy, auc).
#' @note Currently unimplemented; always stops with "Not implemented".
evaluate_model <- function(model, df, features, target = "Outcome") {
  stop("Not implemented: evaluate_model")
}

#' Run the full analysis pipeline end-to-end
#'
#' Loads the dataset, cleans it, engineers features, selects features,
#' and produces each required visualization in order.
#'
#' @param path Path to the diabetes CSV file.
#' @return The cleaned, feature-engineered data frame (invisibly).
run_pipeline <- function(path) {
  df <- load_data(path)
  df <- clean_data(df)
  df <- engineer_features(df)
  features <- select_features(df)
  plot_feature_distributions(df)
  plot_correlation_heatmap(df)
  plot_outcome_balance(df)
  plot_glucose_vs_bmi_by_outcome(df)
  invisible(df)
}
