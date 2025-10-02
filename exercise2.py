#! C:\Users\shirw\OneDrive\Documents\Practise\workShop2\workshop\Scripts\python.exe

import pandas as pd
import numpy as np

# === 1) Load monthly FRED data ===
# - Parse DATE as datetime
# - Use DATE as the index
df = pd.read_csv(
    "data/FRED/FRED_monthly.csv",
    parse_dates=["DATE"],
    index_col="DATE"
)

# Print columns and non-missing counts
print("Columns:", df.columns.tolist())
print("\nNon-missing counts:")
print(df.notna().sum())

# === 2) Mean / min / max for UNRATE and LFPART (rounded to 1 decimal) ===
cols = ["UNRATE", "LFPART"]
stats = df[cols].agg(["mean", "min", "max"]).round(1).T
print("\nSummary (mean/min/max):")
print(stats)

# === 3) Average unemployment rate by decade (1950..2010) ===
# a) Add Year and Decade columns
df["Year"] = df.index.year
df["Decade"] = (df["Year"] // 10) * 10

# b) Keep only decades 1950..2010
valid_decades = list(range(1950, 2020, 10))  # 1950, 1960, ..., 2010
df_dec = df[df["Decade"].isin(valid_decades)]

# c) Keep only decades with COMPLETE monthly observations (120 months)
#    (use UNRATE's non-missing count to decide completeness)
counts = df_dec["UNRATE"].notna().groupby(df_dec["Decade"]).sum()
complete_decades = counts[counts == 120].index

# --- Option A: loop (as the exercise asks) ---
print("\nAverage UNRATE by decade (loop, 1950..2010, complete decades only):")
for dec in sorted(complete_decades):
    mean_unrate = df_dec.loc[df_dec["Decade"] == dec, "UNRATE"].mean()
    print(f"{dec}s: {mean_unrate:.1f}")

# --- Option B: tidy one-liner (groupby) ---
decade_avg = (
    df_dec[df_dec["Decade"].isin(complete_decades)]
    .groupby("Decade")["UNRATE"]
    .mean()
    .round(1)
)
print("\nAverage UNRATE by decade (groupby):")
print(decade_avg)