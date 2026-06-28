import sys
from pathlib import Path

import yfinance as yf

project_root = (
    Path(__file__)
    .resolve()
    .parent.parent
)

sys.path.append(
    str(project_root)
)

from config.settings import TICKERS


def download_stock_data():
    """
    Download historical stock data for all configured tickers.
    """

    output_dir = (
        project_root
        / "data"
        / "raw"
    )

    output_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    for ticker in TICKERS:

        print(
            f"\nDownloading {ticker}..."
        )

        df = yf.download(
            ticker,
            period="2y",
            auto_adjust=True,
            progress=False
        )

        if df.empty:

            print(
                f"⚠ No data found for {ticker}. Skipping..."
            )

            continue

        if hasattr(
            df.columns,
            "levels"
        ):

            df.columns = (
                df.columns
                .get_level_values(0)
            )

        df = df.reset_index()

        df.columns = [
            column.lower()
            for column in df.columns
        ]

        output_path = (
            output_dir
            / f"{ticker.lower()}_stock_data.csv"
        )

        df.to_csv(
            output_path,
            index=False
        )

        print(
            f"✓ Saved {ticker} -> {output_path}"
        )

    print(
        "\n✅ All downloads complete."
    )


if __name__ == "__main__":

    download_stock_data()