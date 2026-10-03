# analysis.R — Project 4: Rain Prediction (Australia)
# Dataset: https://www.kaggle.com/datasets/jsphyg/weather-dataset-rattle-package
library(tidyverse)
library(lubridate)
library(naniar)
library(caret)

load_data <- function(path) {
  read_csv(path)
}

#' Parse Date, drop columns with excessive missingness, impute/drop remaining NAs
clean_data <- function(df) {
  stop("Not implemented: clean_data")
}

#' Derive e.g. temp_range = MaxTemp - MinTemp, month from Date
engineer_features <- function(df) {
  stop("Not implemented: engineer_features")
}

#' @return character vector of selected feature columns (drop high-missingness/low-signal ones)
select_features <- function(df, target = "RainTomorrow") {
  stop("Not implemented: select_features")
}

#' Missing-value bar/heatmap per column
plot_missingness <- function(df) {
  stop("Not implemented: plot_missingness")
}

#' MinTemp/MaxTemp line trend over Date
plot_temp_trend_over_time <- function(df) {
  stop("Not implemented: plot_temp_trend_over_time")
}

#' Bar chart of RainTomorrow class counts
plot_rain_tomorrow_balance <- function(df) {
  stop("Not implemented: plot_rain_tomorrow_balance")
}

#' Scatter of humidity vs pressure, colored by RainTomorrow
plot_humidity_vs_pressure_by_rain <- function(df) {
  stop("Not implemented: plot_humidity_vs_pressure_by_rain")
}

#' (Stretch) Logistic regression predicting RainTomorrow
train_baseline_model <- function(df, features, target = "RainTomorrow") {
  stop("Not implemented: train_baseline_model")
}

#' (Stretch) Score the rain classifier
#' @return named list/vector of metrics (e.g. accuracy, auc)
evaluate_model <- function(model, df, features, target = "RainTomorrow") {
  stop("Not implemented: evaluate_model")
}

run_pipeline <- function(path) {
  df <- load_data(path)
  df <- clean_data(df)
  df <- engineer_features(df)
  features <- select_features(df)
  plot_missingness(df)
  plot_temp_trend_over_time(df)
  plot_rain_tomorrow_balance(df)
  plot_humidity_vs_pressure_by_rain(df)
  invisible(df)
}
