# Reference Output — Project 2: Amazon Fine Food Reviews Sentiment

These images show the **shape of output** your 4 required visualizations should produce once `clean_data`, `engineer_features`, `select_features`, and the `plot_*` functions are implemented. They were generated from a synthetic stand-in dataset with the same columns as the real one — **your numbers, exact distributions, and word lists will differ**. Use these to check you built the *right kind of chart on the right columns*, not to match values.

No solution code is included here — this is the target, not the path to it.

| Image | Function | What to check |
|---|---|---|
| `01_score_distribution.png` | `plot_score_distribution` | One bar per star rating, 1 through 5. Real Amazon review data skews heavily toward 5 stars — if your bars are roughly flat, check you subsampled without accidentally filtering by score. |
| `02_review_length_distribution.png` | `plot_review_length_distribution` | A single histogram of `review_length`, right-skewed (most reviews short, a long tail of longer ones). |
| `03_wordcloud_by_sentiment.png` | `plot_wordcloud_by_sentiment` | Two word clouds (or equivalent), one for positive (score ≥ 4) and one for negative (score ≤ 2) reviews, built from their actual review text — not the same words in both. This reference uses a horizontal bar chart of top words as a stand-in; an actual word cloud image is also acceptable and is what FR-203 asks for. |
| `04_sentiment_over_time.png` | `plot_sentiment_over_time` | Review volume and/or average score plotted against `Time`, at a sensible granularity (e.g. monthly) — not a scatter of every raw row. |

If your plots look structurally different from these (wrong chart type, wrong columns, no color grouping where one's required), that's the signal to revisit that function — not necessarily wrong data.
