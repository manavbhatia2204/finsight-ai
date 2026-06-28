import re
import streamlit as st


def render_research_card(report: str):
    """
    Render a professional AI research report.
    """

    st.subheader("📄 AI Research")

    with st.container(border=True):

        sections = report.split("Sources:")

        summary = sections[0].strip()

        summary = re.sub(
            r"\n{2,}",
            "\n\n",
            summary
        )

        st.markdown(summary)

        if len(sections) > 1:

            sources = sections[1].strip()

            source_list = [
                s.strip()
                for s in sources.split("\n")
                if s.strip()
            ]

            st.divider()

            with st.expander(
                "📚 View Sources",
                expanded=False
            ):

                for source in source_list:

                    st.markdown(
                        f"- {source}"
                    )