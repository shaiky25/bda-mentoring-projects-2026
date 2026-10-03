# Reference Output — Project 4: Rain Prediction (Australia)

These images show the **shape of output** your 4 required visualizations should produce once `clean_data`, `engineer_features`, `select_features`, and the `plot_*` functions are implemented. They were generated from a synthetic stand-in dataset with the same columns as the real one — **your numbers, exact distributions, and missingness levels will differ**. Use these to check you built the *right kind of chart on the right columns*, not to match values.

No solution code is included here — this is the target, not the path to it.

| Image | Function | What to check |
|---|---|---|
| `01_missingness.png` | `plot_missingness` | A bar (or heatmap) of % missing per column, run on the **raw** data before `clean_data` drops anything — this chart exists to justify which columns you drop. Columns like `Evaporation`, `Sunshine`, `Cloud9am/3pm` are known to be heavily missing in the real dataset. |
| `02_temp_trend_over_time.png` | `plot_temp_trend_over_time` | MinTemp and MaxTemp plotted as lines against `Date`, both on the same axes (ideally with a legend) — not two separate unlabeled lines. |
| `03_rain_tomorrow_balance.png` | `plot_rain_tomorrow_balance` | Two bars, Yes vs No. The real dataset is imbalanced (~78% No) — if yours is near 50/50 you likely resampled by accident. |
| `04_humidity_vs_pressure_by_rain.png` | `plot_humidity_vs_pressure_by_rain` | Scatter of a humidity column (x) vs a pressure column (y), colored by `RainTomorrow`, with a legend. Expect a lot of overlap — that's normal, not a bug. |

If your plots look structurally different from these (wrong chart type, wrong columns, no color grouping where one's required), that's the signal to revisit that function — not necessarily wrong data.
