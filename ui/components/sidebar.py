import sys
from pathlib import Path

import streamlit as st

project_root = (
    Path(__file__)
    .resolve()
    .parent.parent.parent
)

sys.path.append(
    str(project_root)
)

from config.settings import CONFIG


TICKERS = [
    ticker["symbol"]
    for ticker in CONFIG["tickers"]
]


def render_sidebar():
    """
    Render the Streamlit sidebar.

    Returns
    -------
    tuple
        (ticker, question, run_analysis)
    """

    st.sidebar.title("📈 FinSight AI")

    ticker = st.sidebar.selectbox(
        "Select Stock",
        TICKERS,
    )

    question = st.sidebar.text_area(
        "Ask a Financial Question",
        placeholder="Will TSLA stock go up tomorrow?",
        height=120,
    )

    run_analysis = st.sidebar.button(
        "🚀 Run Analysis",
        use_container_width=True,
    )

    with st.sidebar.expander("❓ What can I ask?", expanded=False):
        st.markdown("""
- **Fundamentals:** "What is Apple's P/E ratio?"
- **Risk:** "What is Tesla's volatility?"
- **Prediction:** "Will TSLA go up tomorrow?"
- **Comparison:** "Compare Apple and Microsoft"
- **Research:** "What did the Fed say about rates?"

Supported: AAPL, MSFT, NVDA, AMZN, GOOGL, META, TSLA
        """)

    return ticker, question, run_analysis