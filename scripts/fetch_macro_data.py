import os
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv
from fredapi import Fred

# Load .env from project root
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

fred = Fred(api_key=os.getenv("FRED_API_KEY"))

# CPI = Consumer Price Index
series_id = "CPIAUCSL"

print(f"Downloading {series_id} data...")

data = fred.get_series(series_id)

df = pd.DataFrame({
    "date": data.index,
    "value": data.values
})

df["indicator_name"] = "Consumer Price Index"
df["indicator_code"] = series_id

# Reorder columns
df = df[
    [
        "indicator_name",
        "indicator_code",
        "date",
        "value"
    ]
]

print("\nPreview:")
print(df.head())

print("\nShape:")
print(df.shape)

output_path = "data/raw/cpi_data.csv"

df.to_csv(output_path, index=False)

print(f"\n✅ Saved to {output_path}")