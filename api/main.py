from pathlib import Path
import sys

project_root = (
    Path(__file__)
    .resolve()
    .parent.parent
)

sys.path.append(
    str(project_root)
)

from fastapi import FastAPI
from pydantic import BaseModel

from agents.orchestrator_agent.orchestrator_agent import (
    run_orchestrator
)

app = FastAPI(
    title="FinSight AI API",
    version="1.0.0"
)


class QueryRequest(
    BaseModel
):
    query: str


@app.get("/")
def health_check():

    return {
        "status": "running",
        "service": "FinSight AI"
    }


@app.post("/ask")
def ask_finsight(
    request: QueryRequest
):

    result = run_orchestrator(
        request.query
    )

    return {
        "query": request.query,
        "report": result
    }

@app.get("/health")
def health():

    return {
        "status": "healthy"
    }