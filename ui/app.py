import streamlit as st

from components.sidebar import render_sidebar
from components.dashboard import render_dashboard
from components.header import render_header
from components.footer import render_footer

st.set_page_config(
    page_title="FinSight AI",
    page_icon="🏦",
    layout="wide",
)

ticker, question, run_analysis = render_sidebar()

render_header()

if run_analysis:

    render_dashboard(
        ticker=ticker,
        question=question,
    )

else:

    st.info(
        "👈 Select a stock, enter a question and click **Run Analysis**."
    )

render_footer()