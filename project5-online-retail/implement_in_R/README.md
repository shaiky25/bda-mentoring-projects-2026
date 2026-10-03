# Implement in R — Project 5: Customer Spending Pattern Analysis

1. Install packages: `install.packages(c("tidyverse","lubridate","scales","readxl"))`
2. Download the dataset (see the project's top-level README) and place `online_retail.xlsx` (sheet "Online Retail") in this folder.
3. Open `analysis.R`. Every function except `load_data` and `run_pipeline` calls `stop("Not implemented: ...")` — fill in the body of each, following its roxygen comment. Do not change any function signature.
4. Run it: `source("analysis.R"); run_pipeline("online_retail.xlsx")`. It will stop at the first unimplemented function — that's expected. Keep filling functions in order (`clean_data` → `engineer_features` → `select_features` → the `plot_*` functions) until `run_pipeline` completes without error.
5. The optional `train_baseline_model` / `evaluate_model` stretch functions (KMeans clustering on RFM features) are not required for grading.
