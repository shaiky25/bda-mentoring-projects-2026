# Implement in Python — Project 5: Customer Spending Pattern Analysis

1. Install packages: `pip install pandas numpy matplotlib seaborn scikit-learn openpyxl`
2. Download the dataset (see the project's top-level README) and place `online_retail.xlsx` (sheet "Online Retail") in this folder.
3. Open `analysis.py`. Every function except `load_data` and `run_pipeline` raises `NotImplementedError` — fill in the body of each, following its docstring. Do not change any function signature.
4. Run it: `python analysis.py`. It will fail at the first unimplemented function — that's expected. Keep filling functions in order (`clean_data` → `engineer_features` → `select_features` → the `plot_*` functions) until `run_pipeline` completes without error.
5. The optional `train_baseline_model` / `evaluate_model` stretch functions (KMeans clustering on RFM features) are not required for grading.
