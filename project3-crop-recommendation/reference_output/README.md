# Reference Output — Project 3: Crop Recommendation from Soil Data

These images show the **shape of output** your 4 required visualizations should produce once `clean_data`, `engineer_features`, `select_features`, and the `plot_*` functions are implemented. They were generated from a synthetic stand-in dataset with the same columns as the real one — **your numbers, exact distributions, and crop clusters will differ**. Use these to check you built the *right kind of chart on the right columns*, not to match values.

No solution code is included here — this is the target, not the path to it.

| Image | Function | What to check |
|---|---|---|
| `01_nutrient_distributions.png` | `plot_nutrient_distributions` | Three histograms side by side (or faceted), one each for N, P, K — not combined into one overlapping histogram. |
| `02_correlation_heatmap.png` | `plot_correlation_heatmap` | A square matrix across all 7 numeric soil/climate columns (N, P, K, temperature, humidity, ph, rainfall), annotated or color-scaled. |
| `03_crop_counts.png` | `plot_crop_counts` | One bar per distinct crop in `label`, showing frequency. The real dataset is close to balanced across 22 crops — wildly uneven bars likely mean a filtering bug upstream. |
| `04_ph_vs_rainfall_by_crop.png` | `plot_ph_vs_rainfall_by_crop` | Scatter of ph (x) vs rainfall (y), points colored by crop, with a legend. You don't need every crop perfectly separated — some overlap is expected and correct. |

If your plots look structurally different from these (wrong chart type, wrong columns, no color grouping where one's required), that's the signal to revisit that function — not necessarily wrong data.
