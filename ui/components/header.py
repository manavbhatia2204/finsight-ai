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

        st.markdown(
        """
<div style="
    background-color:#1f2937;
    padding:18px;
    border-radius:12px;
    text-align:center;
    border:1px solid #374151;
">

<b>Backend</b>

<br><br>

<span style="font-size:22px;color:#22c55e;">
● Online
</span>

</div>
""",
        unsafe_allow_html=True
    )