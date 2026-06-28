import streamlit as st


def render_footer():

    st.divider()

    col1, col2 = st.columns(
        [4, 1]
    )

    with col1:

        st.caption(
            "FinSight AI • Built by Manav Bhatia"
        )

    with col2:

        st.caption(
            "Version 1.0"
        )