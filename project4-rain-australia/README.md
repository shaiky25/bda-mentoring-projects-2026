# Project 4 — Weather Pattern Analysis: Rain Prediction (Australia)

**Dataset:** Rain in Australia
https://www.kaggle.com/datasets/jsphyg/weather-dataset-rattle-package
Download and place `weatherAUS.csv` in this folder. ~145k rows — filter to 1-3 `Location`s to stay within the 10-hour budget.

**Task:** data clean-up, feature selection, visualization. Optional stretch: logistic regression predicting `RainTomorrow`.

**R packages:** `install.packages(c("tidyverse","lubridate","naniar","caret"))`
**Python packages:** `pip install pandas numpy matplotlib seaborn missingno scikit-learn`

**Run:**
- R: `source("analysis.R"); run_pipeline("weatherAUS.csv")`
- Python: `python analysis.py`

Fill in every function marked "Not implemented" — do not change function signatures.
