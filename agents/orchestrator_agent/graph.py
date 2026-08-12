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

from agents.orchestrator_agent.nodes.financial_metrics_node import (
    financial_metrics_node
)

from agents.orchestrator_agent.nodes.risk_analysis_node import (
    risk_analysis_node
)

from agents.orchestrator_agent.nodes.comparison_node import (
    comparison_node
)

from agents.orchestrator_agent.nodes.off_topic_node import (
    off_topic_node
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
    "financial_metrics",
    financial_metrics_node
)

builder.add_node(
    "risk_analysis",
    risk_analysis_node
)

builder.add_node(
    "comparison",
    comparison_node
)

builder.add_node(
    "off_topic",
    off_topic_node
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
        "financial_metrics": "financial_metrics",
        "risk_analysis": "risk_analysis",
        "comparison": "comparison",
        "off_topic": "off_topic",
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
    "financial_metrics",
    "report"
)

builder.add_edge(
    "risk_analysis",
    "report"
)

builder.add_edge(
    "comparison",
    "report"
)

builder.add_edge(
    "off_topic",
    "report"
)

builder.add_edge(
    "report",
    END
)

graph = builder.compile()