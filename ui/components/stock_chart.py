import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st


def render_stock_chart(history: dict):
    """
    Render professional financial chart with
    candlesticks and volume.
    """

    records = history.get("records", [])

    if not records:
        st.warning("No historical stock data available.")
        return

    df = pd.DataFrame(records)

    df["date"] = pd.to_datetime(df["date"])

    df = df.sort_values("date")

    fig = make_subplots(
        rows=2,
        cols=1,
        shared_xaxes=True,
        vertical_spacing=0.02,
        row_heights=[0.75, 0.25],
        subplot_titles=(
            f"{history['ticker']} Stock Price",
            "Trading Volume"
        )
    )

    fig.add_trace(
        go.Candlestick(
            x=df["date"],
            open=df["open"],
            high=df["high"],
            low=df["low"],
            close=df["close"],
            increasing_line_color="#00C853",
            decreasing_line_color="#FF5252",
            increasing_fillcolor="#00C853",
            decreasing_fillcolor="#FF5252",
            name="Price"
        ),
        row=1,
        col=1
    )

    colors = []

    for _, row in df.iterrows():

        if row["close"] >= row["open"]:
            colors.append("#00C853")
        else:
            colors.append("#FF5252")

    fig.add_trace(
        go.Bar(
            x=df["date"],
            y=df["volume"],
            marker_color=colors,
            name="Volume"
        ),
        row=2,
        col=1
    )

    fig.update_layout(

        template="plotly_dark",

        height=720,

        margin=dict(
            l=10,
            r=10,
            t=45,
            b=10
        ),

        hovermode="x unified",

        showlegend=False,

        dragmode="zoom",

        font=dict(
            size=14
        ),

        xaxis_rangeslider_visible=False,

        modebar_remove=[
            "lasso2d",
            "select2d",
            "zoomIn2d",
            "zoomOut2d",
            "autoScale2d"
        ]
    )

    fig.update_xaxes(

        showgrid=False,

        rangeselector=dict(

            buttons=[

                dict(
                    count=1,
                    label="1M",
                    step="month",
                    stepmode="backward"
                ),

                dict(
                    count=3,
                    label="3M",
                    step="month",
                    stepmode="backward"
                ),

                dict(
                    count=6,
                    label="6M",
                    step="month",
                    stepmode="backward"
                ),

                dict(
                    step="all",
                    label="All"
                )
            ]
        )
    )

    fig.update_yaxes(
        showgrid=True,
        gridcolor="#2C2C2C"
    )

    st.subheader("📊 Market Chart")

    st.plotly_chart(
        fig,
        use_container_width=True,
        config={
            "displaylogo": False,
            "responsive": True,
            "scrollZoom": True
        }
    )