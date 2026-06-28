import streamlit as st


def render_market_snapshot(
    prediction: dict,
    history: dict
):
    """
    Render market snapshot metrics.
    """

    records = history.get("records", [])

    if not records:
        return

    latest = records[0]

    confidence = max(
        prediction["confidence_up"],
        prediction["confidence_down"]
    )

    latest_close = latest["close"]
    latest_high = latest["high"]
    latest_low = latest["low"]
    latest_volume = latest["volume"]

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "📌 Ticker",
        prediction["ticker"]
    )

    col2.metric(
        "💲 Close",
        f"${latest_close:.2f}"
    )

    col3.metric(
        "📈 High",
        f"${latest_high:.2f}"
    )

    col4.metric(
        "📉 Low",
        f"${latest_low:.2f}"
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "📊 Volume",
        f"{latest_volume:,}"
    )

    col2.metric(
        "🤖 Prediction",
        prediction["prediction"]
    )

    col3.metric(
        "🎯 Confidence",
        f"{confidence:.2f}%"
    )

    st.divider()