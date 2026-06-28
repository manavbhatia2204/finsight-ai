import streamlit as st


def render_prediction_card(prediction: dict):
    """
    Render a professional stock prediction card.
    """

    direction = prediction["prediction"]

    confidence_up = prediction["confidence_up"]
    confidence_down = prediction["confidence_down"]

    confidence = max(
        confidence_up,
        confidence_down
    )

    bullish = direction == "UP"

    badge = "🟢 BULLISH" if bullish else "🔴 BEARISH"

    st.subheader("📈 Stock Prediction")

    with st.container(border=True):

        st.markdown(
            f"""
# {badge}

### {prediction["ticker"]}
"""
        )

        st.progress(
            confidence / 100
        )

        st.markdown(
            f"### Confidence: **{confidence:.2f}%**"
        )

        st.divider()

        col1, col2 = st.columns(2)

        col1.metric(
            "Bullish",
            f"{confidence_up:.2f}%"
        )

        col2.metric(
            "Bearish",
            f"{confidence_down:.2f}%"
        )