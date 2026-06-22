# FinSight AI

## Overview

FinSight AI is a multi-agent financial intelligence platform designed to automate financial data collection, document understanding, market research, and stock prediction.

The platform combines:

* Financial data ingestion
* Retrieval-Augmented Generation (RAG)
* Financial research agents
* Machine learning prediction agents
* Multi-agent orchestration (coming in Week 6)

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

* Yahoo Finance (yfinance)

Supported tickers:

* AAPL
* MSFT
* NVDA
* AMZN
* GOOGL
* META
* TSLA

#### Macroeconomic Data

FRED:

* CPIAUCSL
* UNRATE
* GDP
* FEDFUNDS

### Features

* Automatic data ingestion
* Duplicate prevention
* Freshness validation
* Smart refresh logic

---

## Agent 2 – Research Agent (RAG) ✅

### Responsibilities

* Understand financial documents
* Answer financial questions
* Retrieve company-specific information

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

Example:

Question:

What did Apple say about Services revenue?

Answer:

Apple reported Services revenue of $109.2 billion in FY2025, representing a 14% increase compared to FY2024.

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

### Features

#### Technical Indicators

* RSI
* MACD
* MACD Signal
* MACD Histogram
* Bollinger Bands
* SMA 20
* SMA 50
* Volume Moving Average

#### Macroeconomic Features

* CPI
* GDP
* Federal Funds Rate
* Unemployment Rate

### Machine Learning

Model:

* XGBoost Classifier

Validation:

* TimeSeriesSplit

Metrics:

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

Ticker: MSFT

Direction: UP

Confidence UP: 76.93%

Confidence DOWN: 23.07%

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
* TA Library

## Data Sources

* Yahoo Finance
* FRED API

## DevOps (Planned)

* Docker
* Kubernetes
* Prometheus
* Grafana

---

# Current Architecture

User
↓
FinSight AI

├── Ingestion Agent
│ ├── Yahoo Finance
│ └── FRED
│
├── Research Agent
│ ├── Financial PDFs
│ ├── FAISS
│ └── Groq LLM
│
└── ML Prediction Agent
├── Feature Engineering
├── XGBoost Models
└── Prediction Tools

---

# Roadmap

## Week 6

* Multi-Agent Orchestrator
* Agent Routing
* Agent Collaboration
* LangGraph Integration

## Week 7

* Dockerization
* Kubernetes Deployment
* Prometheus Monitoring
* Grafana Dashboards

## Week 8

* Streamlit UI
* Portfolio Dashboard
* Live Deployment

---

# Author

Manav Bhatia

