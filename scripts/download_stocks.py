import yfinance as yf

TICKERS = [
    "AAPL",
    "MSFT",
    "NVDA",
    "AMZN",
    "GOOGL",
    "META",
    "TSLA"
]

for ticker in TICKERS:

    print(f"\nDownloading {ticker}...")

    df = yf.download(
        ticker,
        period="2y",
        auto_adjust=True,
        progress=False
    )

    if hasattr(df.columns, "levels"):
        df.columns = df.columns.get_level_values(0)

    df = df.reset_index()

    df.columns = [
        col.lower()
        for col in df.columns
    ]

    output_path = (
        f"data/raw/"
        f"{ticker.lower()}_stock_data.csv"
    )

    df.to_csv(
        output_path,
        index=False
    )

    print(
        f"Saved {ticker} -> {output_path}"
    )

print("\nAll downloads complete.")