# analysis.R — Project 5: Customer Spending Pattern Analysis
# Dataset: https://archive.ics.uci.edu/dataset/352/online+retail (Online Retail.xlsx)
library(tidyverse)
library(lubridate)
library(scales)
library(readxl)

load_data <- function(path) {
  read_excel(path, sheet = "Online Retail")
}

#' Drop cancelled orders (InvoiceNo starting with "C"), missing CustomerID, non-positive Quantity/UnitPrice
clean_data <- function(df) {
  stop("Not implemented: clean_data")
}

#' Derive TotalPrice = Quantity * UnitPrice, and per-customer Recency/Frequency/Monetary (RFM)
engineer_features <- function(df) {
  stop("Not implemented: engineer_features")
}

#' @return character vector of selected RFM/derived feature columns
select_features <- function(df, target = NULL) {
  stop("Not implemented: select_features")
}

#' Total revenue (Quantity * UnitPrice) by month
plot_monthly_revenue_trend <- function(df) {
  stop("Not implemented: plot_monthly_revenue_trend")
}

#' Bar chart, top N countries by revenue
plot_top_countries_by_revenue <- function(df) {
  stop("Not implemented: plot_top_countries_by_revenue")
}

#' Histograms of Recency, Frequency, Monetary per customer
plot_rfm_distributions <- function(df) {
  stop("Not implemented: plot_rfm_distributions")
}

#' Scatter of Frequency vs Monetary, colored by segment
plot_customer_segments <- function(df) {
  stop("Not implemented: plot_customer_segments")
}

#' (Stretch) KMeans clustering on RFM features (unsupervised)
train_baseline_model <- function(df, features, target = NULL) {
  stop("Not implemented: train_baseline_model")
}

#' (Stretch) Score the clustering (e.g. silhouette width)
#' @return named list/vector of metrics
evaluate_model <- function(model, df, features, target = NULL) {
  stop("Not implemented: evaluate_model")
}

run_pipeline <- function(path) {
  df <- load_data(path)
  df <- clean_data(df)
  df <- engineer_features(df)
  features <- select_features(df)
  plot_monthly_revenue_trend(df)
  plot_top_countries_by_revenue(df)
  plot_rfm_distributions(df)
  plot_customer_segments(df)
  invisible(df)
}
