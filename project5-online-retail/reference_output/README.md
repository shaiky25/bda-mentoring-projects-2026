# Reference Output — Project 5: Customer Spending Pattern Analysis

These images show the **shape of output** your 4 required visualizations should produce once `clean_data`, `engineer_features`, `select_features`, and the `plot_*` functions are implemented. They were generated from a synthetic stand-in dataset with the same columns as the real one — **your numbers, exact distributions, and country/segment mix will differ**. Use these to check you built the *right kind of chart on the right columns*, not to match values.

No solution code is included here — this is the target, not the path to it.

| Image | Function | What to check |
|---|---|---|
| `01_monthly_revenue_trend.png` | `plot_monthly_revenue_trend` | A line (or bar) of total `TotalPrice` (= Quantity × UnitPrice) aggregated by month — not a plot of every raw transaction. |
| `02_top_countries_by_revenue.png` | `plot_top_countries_by_revenue` | A bar chart of the top N countries by total revenue, sorted descending. The real dataset is dominated by "United Kingdom" — if it's not your tallest bar, double-check your aggregation. |
| `03_rfm_distributions.png` | `plot_rfm_distributions` | Three histograms side by side, one each for the per-customer Recency, Frequency, and Monetary values you engineered — these only exist after `engineer_features` computes them correctly. |
| `04_customer_segments.png` | `plot_customer_segments` | Scatter of Frequency (x) vs Monetary (y), one point per customer, colored by whatever segment scheme you chose (e.g. median-split quadrants, or your own rule) — with a legend naming the segments. |

If your plots look structurally different from these (wrong chart type, wrong columns, no color grouping where one's required), that's the signal to revisit that function — not necessarily wrong data.
