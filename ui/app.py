import streamlit as st

# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------

st.set_page_config(
    page_title="FinSight AI",
    page_icon="📈",
    layout="wide",
)

# ---------------------------------------------------
# Sidebar
# ---------------------------------------------------

st.sidebar.title("📈 FinSight AI")

ticker = st.sidebar.selectbox(
    "Select Stock",
    [
        "AAPL",
        "MSFT",
        "NVDA",
        "AMZN",
        "GOOGL",
        "META",
        "TSLA",
    ],
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

# ---------------------------------------------------
# Main Page
# ---------------------------------------------------

st.title("🏦 FinSight AI")

st.markdown(
    """
Welcome to **FinSight AI**.

This platform combines:

- 🤖 Multi-Agent AI
- 📄 Retrieval-Augmented Generation (RAG)
- 📈 Machine Learning Stock Prediction
- 🏛️ Macroeconomic Analysis
- 📊 Interactive Financial Visualizations

Select a stock from the sidebar and click **Run Analysis**.
"""
)

st.divider()

st.subheader("Current Selection")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Selected Ticker",
        ticker,
    )

with col2:
    st.metric(
        "Question",
        question if question else "No question entered",
    )

if run_analysis:

    st.info(
        "Backend integration will be added in the next step."
    )