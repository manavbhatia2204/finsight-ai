from agents.research_agent.research_agent_v2 import (
    ask_research_agent
)


def research_node(
    state
):
    print(
        "\nResearch Node Executed"
    )

    try:

        result = ask_research_agent(
            state["query"]
        )

        return {
            "research_result": result
        }

    except Exception as e:

        return {
            "research_result": {
                "error": str(e)
            }
        }