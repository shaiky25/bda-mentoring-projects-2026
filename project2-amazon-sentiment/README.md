# Project 2 — Sentiment Analysis: Amazon Fine Food Reviews

**Dataset:** Amazon Fine Food Reviews
https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews
Download and place `amazon_fine_food_reviews.csv` in this folder. Dataset is ~568k rows — subsample to ~5k-10k rows to stay within the 10-hour budget.

**Task:** data clean-up, feature selection, visualization. Optional stretch: TF-IDF + Naive Bayes sentiment classifier.

**R packages:** `install.packages(c("tidyverse","tidytext","textdata","wordcloud","tm"))`
**Python packages:** `pip install pandas matplotlib seaborn nltk wordcloud scikit-learn`

**Run:**
- R: `source("analysis.R"); run_pipeline("amazon_fine_food_reviews.csv")`
- Python: `python analysis.py`

Fill in every function marked "Not implemented" — do not change function signatures.
