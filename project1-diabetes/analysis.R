# analysis.R — Project 1: Diabetes Risk Screening
# Dataset: https://www.kaggle.com/datasets/jamaltariqcheema/pima-indians-diabetes-dataset
library(tidyverse)
library(corrplot)
library(caret)

load_data <- function(path) {
  read_csv(path)
}

#' Handle missing/impossible values (e.g. glucose/bmi == 0 is missing, not real)
#' @param df raw data frame from load_data
#' @return cleaned data frame, same columns
clean_data <- function(df) {
  stop("Not implemented: clean_data")
}

#' Derive any new columns useful for analysis (e.g. bmi_category, age_group)
#' @param df cleaned data frame
#' @return data frame with additional engineered columns
engineer_features <- function(df) {
  stop("Not implemented: engineer_features")
}

#' Choose the feature columns to carry into visualization/modeling
#' @param df engineered data frame
#' @param target name of the outcome column, default "Outcome"
#' @return character vector of selected column names
select_features <- function(df, target = "Outcome") {
  stop("Not implemented: select_features")
}

#' Faceted histograms of all numeric features
plot_feature_distributions <- function(df) {
  stop("Not implemented: plot_feature_distributions")
}

#' Correlation matrix heatmap across numeric features
plot_correlation_heatmap <- function(df) {
  stop("Not implemented: plot_correlation_heatmap")
}

#' Bar chart of Outcome class counts (0/1)
plot_outcome_balance <- function(df) {
  stop("Not implemented: plot_outcome_balance")
}

#' Scatter of Glucose vs BMI, colored by Outcome
plot_glucose_vs_bmi_by_outcome <- function(df) {
  stop("Not implemented: plot_glucose_vs_bmi_by_outcome")
}

#' (Stretch) Train a baseline classifier
#' @param df selected-feature data frame
#' @param features character vector of feature column names
#' @param target outcome column name
#' @return a fitted model object
train_baseline_model <- function(df, features, target = "Outcome") {
  stop("Not implemented: train_baseline_model")
}

#' (Stretch) Score the model
#' @return named list/vector of metrics (e.g. accuracy, auc)
evaluate_model <- function(model, df, features, target = "Outcome") {
  stop("Not implemented: evaluate_model")
}

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
