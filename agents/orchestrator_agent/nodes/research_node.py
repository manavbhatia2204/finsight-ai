from agents.research_agent.research_agent_v2 import (
    ask_research_agent
)


def research_node(
    state
):
    print(
        "\nResearch Node Executed"
    )

    result = ask_research_agent(
        state["query"]
    )

    return {
        "research_result": result
    }