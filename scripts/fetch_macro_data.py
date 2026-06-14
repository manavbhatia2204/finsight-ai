import pandas as pd
from fredapi import Fred
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get FRED API Key
FRED_API_KEY = os.getenv("FRED_API_KEY")

# Initialize FRED client
fred = Fred(api_key=FRED_API_KEY)

# Indicators to download
INDICATORS = {
    "CPIAUCSL": "Consumer Price Index",
    "GDP": "Gross Domestic Product",
    "FEDFUNDS": "Federal Funds Rate",
    "UNRATE": "Unemployment Rate"
}

all_data = []

# Download each indicator
for series_id, indicator_name in INDICATORS.items():

    print(f"\nDownloading {indicator_name} ({series_id})...")

    data = fred.get_series(series_id)

    df = pd.DataFrame({
        "date": data.index,
        "value": data.values
    })

    df["indicator_name"] = indicator_name
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

    all_data.append(df)

# Combine all indicators
final_df = pd.concat(all_data, ignore_index=True)

print("\nPreview:")
print(final_df.head())

print("\nShape:")
print(final_df.shape)

# Create directory if it doesn't exist
os.makedirs("data/raw", exist_ok=True)

# Save CSV
output_path = "data/raw/macro_data.csv"

final_df.to_csv(output_path, index=False)

print(f"\n✅ Saved to {output_path}")