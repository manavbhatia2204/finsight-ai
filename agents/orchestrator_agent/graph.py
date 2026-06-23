from langgraph.graph import (
    StateGraph,
    END
)

from agents.orchestrator_agent.state import (
    GraphState
)

from agents.orchestrator_agent.nodes.router_node import (
    router_node
)

from agents.orchestrator_agent.nodes.research_node import (
    research_node
)

from agents.orchestrator_agent.nodes.prediction_node import (
    prediction_node
)

from agents.orchestrator_agent.nodes.report_node import (
    report_node
)

builder = StateGraph(
    GraphState
)

builder.add_node(
    "router",
    router_node
)

builder.add_node(
    "research",
    research_node
)

builder.add_node(
    "prediction",
    prediction_node
)

builder.add_node(
    "report",
    report_node
)

builder.set_entry_point(
    "router"
)


def route_decision(
    state
):
    return state["route"]


builder.add_conditional_edges(
    "router",
    route_decision,
    {
        "research": "research",
        "prediction": "prediction",
        "both": "research"
    }
)


def research_decision(
    state
):
    if state["route"] == "both":
        return "prediction"

    return "report"


builder.add_conditional_edges(
    "research",
    research_decision,
    {
        "prediction": "prediction",
        "report": "report"
    }
)

builder.add_edge(
    "prediction",
    "report"
)

builder.add_edge(
    "report",
    END
)

graph = builder.compile()