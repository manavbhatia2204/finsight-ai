from pathlib import Path

import streamlit as st


def render_header():
    """
    Render application header.
    """

    css_path = (
        Path(__file__).parent.parent
        / "assets"
        / "style.css"
    )

    with open(css_path) as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

    left, right = st.columns(
        [5, 1]
    )

    with left:

        st.title("🏦 FinSight AI")

        st.markdown(
            """
### AI-Powered Financial Intelligence Platform

Multi-Agent AI • RAG • XGBoost • FastAPI • PostgreSQL
"""
        )

    with right:

        st.metric(
            "Backend",
            "🟢 Online"
        )

    st.divider()