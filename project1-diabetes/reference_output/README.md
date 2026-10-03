# Reference Output — Project 1: Diabetes Risk Screening

These images show the **shape of output** your 4 required visualizations should produce once `clean_data`, `engineer_features`, `select_features`, and the `plot_*` functions are implemented. They were generated from a synthetic stand-in dataset with the same columns as the real one — **your numbers, exact distributions, and class balance will differ**. Use these to check you built the *right kind of chart on the right columns*, not to match values.

No solution code is included here — this is the target, not the path to it.

| Image | Function | What to check |
|---|---|---|
| `01_feature_distributions.png` | `plot_feature_distributions` | One histogram per numeric column, faceted/arranged in a grid (not overlaid in one axes). After cleaning, there should be no suspicious spike at 0 for Glucose/BMI/BloodPressure/SkinThickness/Insulin — a spike there means `clean_data` didn't handle the "0 = missing" issue. |
| `02_correlation_heatmap.png` | `plot_correlation_heatmap` | A square matrix, numeric features + Outcome, annotated or color-scaled. Glucose and BMI should show the strongest positive correlation with Outcome — if your heatmap shows no clear pattern, double check `clean_data` ran before this. |
| `03_outcome_balance.png` | `plot_outcome_balance` | Two bars (Outcome 0 vs 1) with counts labeled or readable off the axis. Real Pima data is imbalanced (~65/35) — if your bars are near 50/50, you may have resampled by accident. |
| `04_glucose_vs_bmi_by_outcome.png` | `plot_glucose_vs_bmi_by_outcome` | Scatter of Glucose (x) vs BMI (y), points colored/grouped by Outcome, with a legend. You should see the Outcome=1 points skew toward higher Glucose. |

If your plots look structurally different from these (wrong chart type, wrong columns, no color grouping where one's required), that's the signal to revisit that function — not necessarily wrong data.
