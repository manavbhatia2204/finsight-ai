# FinSight AI

## Overview

FinSight AI is a multi-agent financial intelligence platform designed to automate financial data collection, document understanding, market research, stock prediction, and AI-driven financial analysis.

The platform combines:

* Financial data ingestion
* Retrieval-Augmented Generation (RAG)
* Financial research agents
* Machine learning prediction agents
* Multi-agent orchestration
* REST API integration

The long-term goal is to provide institutional-style financial research through a coordinated AI system.

---

# Current Status

## Agent 1 – Ingestion Agent ✅

### Responsibilities

* Collect stock market data
* Collect macroeconomic data
* Maintain database freshness

### Data Sources

#### Stock Data

Yahoo Finance (yfinance)

Supported tickers:

* AAPL
* MSFT
* NVDA
* AMZN
* GOOGL
* META
* TSLA

#### Macroeconomic Data

FRED

Supported indicators:

* CPIAUCSL
* UNRATE
* GDP
* FEDFUNDS

### Features

* Automatic data ingestion
* Duplicate prevention
* Data freshness validation
* Smart refresh logic
* PostgreSQL storage

---

## Agent 2 – Research Agent (RAG) ✅

### Responsibilities

* Understand financial documents
* Answer financial questions
* Retrieve company-specific information
* Generate grounded financial responses

### Documents Indexed

* Apple 10-K
* Microsoft 10-K
* Nvidia 10-K
* FOMC Minutes
* Federal Reserve Monetary Policy Reports

### RAG Pipeline

User Question

↓

Query Rewriter

↓

Retriever (FAISS)

↓

Relevant Chunks

↓

Groq LLM

↓

Grounded Financial Answer

### Features

* Multi-document semantic search
* Context-aware follow-up questions
* Citation generation
* Conversation memory
* Query rewriting

### Example

Question:

What did Apple say about Services revenue?

Answer:

Apple reported Services revenue of approximately $109.2 billion in FY2025, representing significant growth compared to FY2024.

---

## Agent 3 – ML Prediction Agent ✅

### Responsibilities

Predict next-day stock direction using technical indicators and macroeconomic features.

### Supported Tickers

* AAPL
* MSFT
* NVDA
* AMZN
* GOOGL
* META
* TSLA

### Technical Indicators

* RSI
* MACD
* MACD Signal
* MACD Histogram
* Bollinger Bands
* SMA 20
* SMA 50
* Volume Moving Average

### Macroeconomic Features

* CPI
* GDP
* Federal Funds Rate
* Unemployment Rate

### Machine Learning

Model:

* XGBoost Classifier

Validation:

* TimeSeriesSplit

Evaluation Metrics:

* Accuracy
* Precision
* Recall
* F1 Score

### Model Persistence

Models are saved using:

* joblib

Generated models:

* xgboost_AAPL.pkl
* xgboost_MSFT.pkl
* xgboost_NVDA.pkl
* xgboost_AMZN.pkl
* xgboost_GOOGL.pkl
* xgboost_META.pkl
* xgboost_TSLA.pkl

### Example Prediction

Prediction Result

Ticker: TSLA

Direction: DOWN

Confidence UP: 40.57%

Confidence DOWN: 59.43%

### Features

* Multi-ticker prediction support
* Confidence scoring
* Model persistence
* Error handling
* Reproducible predictions

---

## Agent 4 – Orchestrator Agent ✅

### Responsibilities

Coordinate multiple AI agents and route user requests to the appropriate workflow.

### Built Using

* LangGraph

### Supported Routes

#### Research Route

User Query

↓

Research Agent

↓

Report Agent

#### Prediction Route

User Query

↓

Prediction Agent

↓

Report Agent

#### Investment Analysis Route

User Query

↓

Research Agent

↓

Prediction Agent

↓

Report Agent

### Example Queries

* What did Apple say about Services revenue?
* Will TSLA stock go up?
* Analyze Tesla and tell me if it is a good investment

### Features

* Shared graph state
* Conditional routing
* Multi-agent workflows
* Company name detection
* Ticker extraction
* Error handling
* Report generation

### Error Handling

Supported scenarios:

* Unsupported tickers
* Missing model files
* Prediction failures
* Research failures

The graph completes gracefully without crashing.

---

# FastAPI Integration ✅

FinSight AI is now exposed through a REST API.

### Endpoints

#### GET /

Returns service status.

#### GET /health

Health check endpoint.

Example Response:

{
"status": "healthy"
}

#### POST /ask

Main FinSight endpoint.

Example Request:

{
"query": "Will TSLA stock go up?"
}

Example Response:

{
"query": "Will TSLA stock go up?",
"report": "Prediction Report..."
}

---

# Database Architecture

## stocks

Stores:

* ticker
* company_name
* sector
* exchange

## stock_prices

Stores:

* open
* high
* low
* close
* volume
* date

## macro_indicators

Stores:

* indicator_name
* indicator_code
* value
* date

---

# Technology Stack

## Backend

* Python
* FastAPI

## Database

* PostgreSQL
* SQLAlchemy

## AI / LLM

* LangChain
* Groq
* Llama 3.1

## RAG

* FAISS
* Sentence Transformers
* PyPDF

## Machine Learning

* XGBoost
* Scikit-Learn
* TA-Lib

## Workflow Orchestration

* LangGraph

## Data Sources

* Yahoo Finance
* FRED API

## DevOps (Upcoming)

* Docker
* Kubernetes
* Prometheus
* Grafana

---

# Current Architecture

User

↓

FastAPI

↓

Orchestrator Agent

↓

Router Node

↓

Research Agent ─────┐
│
Prediction Agent ───┤
│
▼

Report Agent

↓

Final Response

---

# Project Roadmap

## Week 7

* Dockerization
* Docker Compose
* Kubernetes Deployment
* Prometheus Monitoring
* Grafana Dashboards

## Week 8

* Streamlit UI
* Portfolio Dashboard
* Live Deployment
* Enhanced Reporting

## Future Enhancements

* Portfolio Analysis
* News Intelligence Agent
* Sentiment Analysis
* Watchlists
* Earnings Analysis
* Additional Company Filings
* Advanced Investment Reports

---

# Author

Manav Bhatia