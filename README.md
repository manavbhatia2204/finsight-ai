# FinSight AI

Multi-agent financial intelligence platform that combines financial data ingestion, semantic document search, machine learning forecasting, and AI-powered report generation.

## Overview

FinSight AI is designed as a production-grade AI system that orchestrates multiple specialized agents to answer complex financial questions and generate analyst-style reports.

Users can ask a single question and receive insights generated from:

* Financial market data
* Macroeconomic indicators
* Financial documents
* Machine learning forecasts

## Planned Architecture

### Data Agent

* Collects stock market data
* Collects macroeconomic indicators
* Cleans and stores data

### Research Agent

* Performs semantic search over financial documents
* Retrieves relevant context

### Forecasting Agent

* Generates predictive insights using machine learning models

### Report Agent

* Produces analyst-style reports and summaries

### Orchestrator Agent

* Coordinates all agents using LangGraph

## Tech Stack

* Python
* FastAPI
* PostgreSQL
* SQLAlchemy
* LangGraph
* LangChain
* FAISS
* XGBoost
* Docker
* Kubernetes
* Prometheus
* Grafana

## Week 1 Goal

Build the data foundation:

* PostgreSQL setup
* Stock market data ingestion
* Macroeconomic data ingestion
* Data cleaning
* Data validation
* Database loading

## Status

🚧 In Development
