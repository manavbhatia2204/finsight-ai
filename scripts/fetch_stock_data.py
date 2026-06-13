import yfinance as yf

ticker = "AAPL"

print(f"Downloading data for {ticker}...")

df = yf.download(
    ticker,
    period="2y",
    auto_adjust=True,
    progress=False
)

# Flatten MultiIndex columns if present
if hasattr(df.columns, "levels"):
    df.columns = df.columns.get_level_values(0)

# Reset index so Date becomes a normal column
df = df.reset_index()

# Standardize column names
df.columns = [col.lower() for col in df.columns]

print("\nData Preview:")
print(df.head())

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

output_path = "data/raw/aapl_stock_data.csv"

df.to_csv(output_path, index=False)

print(f"\n✅ Data saved to: {output_path}")