import streamlit as st


def render_faq():
    """
    Render a FAQ section explaining what FinSight AI can do.
    """
    st.divider()

    with st.expander("❓ Frequently Asked Questions"):
        st.markdown("""
**What can I ask FinSight AI?**
Questions about company fundamentals (P/E, margins, growth), risk metrics
(volatility, Sharpe ratio, beta), stock price predictions, comparisons
between two companies, and research grounded in SEC filings and Fed reports.

**Which companies are supported?**
Apple, Microsoft, NVIDIA, Amazon, Google, Meta, and Tesla.

**How current is the data?**
Historical prices and fundamentals refresh weekly via an automated pipeline.
Live prices are fetched on demand and reflect the current market.

**How does the prediction work?**
An XGBoost model trained on technical indicators and macroeconomic data
estimates next-day price direction with a confidence score. This is a
statistical estimate, not financial advice.

**Can I ask about things unrelated to finance?**
FinSight AI is a specialized financial assistant and will redirect
off-topic questions back to its supported capabilities.

**Is this real-time trading data?**
No — this is for research and educational purposes, not live trading.
        """)