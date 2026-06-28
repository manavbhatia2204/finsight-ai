import requests
import streamlit as st

from components.market_snapshot import render_market_snapshot
from components.prediction_card import render_prediction_card
from components.research_card import render_research_card
from components.stock_chart import render_stock_chart

from pdf.report_generator import generate_pdf

from utils.api_client import (
    ask_question,
    get_stock_history,
    predict_stock,
)


def render_dashboard(
    ticker: str,
    question: str,
):
    """
    Render complete FinSight AI dashboard.
    """

    if not question.strip():

        st.warning(
            "Please enter a financial question."
        )

        return

    with st.spinner("Running FinSight AI Analysis..."):

        try:

            prediction = predict_stock(
                ticker
            )

            report = ask_question(
                question
            )

            history = get_stock_history(
                ticker
            )

        except requests.exceptions.ConnectionError:

            st.error(
                "Unable to connect to FastAPI backend."
            )

            return

        except Exception as e:

            st.error(
                str(e)
            )

            return

    # ----------------------------------
    # Market Snapshot
    # ----------------------------------

    render_market_snapshot(
        prediction,
        history
    )

    # ----------------------------------
    # Market Chart
    # ----------------------------------

    render_stock_chart(
        history
    )

    st.divider()

    # ----------------------------------
    # Prediction + Research
    # ----------------------------------

    left, right = st.columns(
        [1, 2],
        gap="large"
    )

    with left:

        render_prediction_card(
            prediction
        )

    with right:

        render_research_card(
            report["report"]
        )

    st.divider()

    # ----------------------------------
    # PDF Export
    # ----------------------------------

    pdf = generate_pdf(
        prediction,
        history,
        report["report"]
    )

    st.download_button(
        label="📥 Download PDF Report",
        data=pdf,
        file_name=f"FinSight_Report_{prediction['ticker']}.pdf",
        mime="application/pdf",
        use_container_width=True,
    )