import pandas as pd
import ta

from sqlalchemy import text

from api.database.connection import engine


def get_training_data(
    ticker: str,
    lookback_days: int = 365
) -> pd.DataFrame:
    """
    Build a training dataset containing:

    - Stock price history
    - Technical indicators
    - Macroeconomic indicators
    """

    stock_query = text("""
        SELECT
            sp.date,
            sp.open,
            sp.high,
            sp.low,
            sp.close,
            sp.volume
        FROM stock_prices sp
        JOIN stocks s
            ON sp.stock_id = s.id
        WHERE s.ticker = :ticker
        ORDER BY sp.date ASC
    """)

    prices = pd.read_sql(
        stock_query,
        engine,
        params={
            "ticker": ticker.upper()
        }
    )

    if prices.empty:

        raise ValueError(
            f"No stock price data found for {ticker}"
        )

    prices["date"] = pd.to_datetime(
        prices["date"]
    )

    # -----------------------------
    # Technical Indicators
    # -----------------------------

    prices["rsi"] = ta.momentum.RSIIndicator(
        close=prices["close"],
        window=14
    ).rsi()

    prices["macd"] = ta.trend.MACD(
        close=prices["close"]
    ).macd()

    prices["macd_signal"] = ta.trend.MACD(
        close=prices["close"]
    ).macd_signal()

    prices["macd_diff"] = ta.trend.MACD(
        close=prices["close"]
    ).macd_diff()

    bollinger = ta.volatility.BollingerBands(
        close=prices["close"],
        window=20
    )

    prices["bb_upper"] = (
        bollinger.bollinger_hband()
    )

    prices["bb_lower"] = (
        bollinger.bollinger_lband()
    )

    prices["sma_20"] = (
        prices["close"]
        .rolling(20)
        .mean()
    )

    prices["sma_50"] = (
        prices["close"]
        .rolling(50)
        .mean()
    )

    prices["volume_ma"] = (
        prices["volume"]
        .rolling(20)
        .mean()
    )

    # -----------------------------
    # Macro Indicators
    # -----------------------------

    macro_query = text("""
        SELECT
            date,
            indicator_code,
            value
        FROM macro_indicators
        ORDER BY date ASC
    """)

    macro = pd.read_sql(
        macro_query,
        engine
    )

    macro["date"] = pd.to_datetime(
        macro["date"]
    )

    macro_pivot = (
        macro
        .pivot(
            index="date",
            columns="indicator_code",
            values="value"
        )
    )

    macro_pivot.columns = [
        f"macro_{col.lower()}"
        for col in macro_pivot.columns
    ]

    df = (
        prices
        .set_index("date")
        .join(
            macro_pivot,
            how="left"
        )
    )

    df = (
        df
        .ffill()
        .dropna()
    )
    df = (
    df
    .ffill()
    .dropna()
)
# -----------------------------
# Prediction Target
# -----------------------------

    df["target"] = (
        df["close"]
        .shift(-1)
        > df["close"]
        ).astype(int)

    df = df.dropna()

    return df.reset_index()

