# FinSight AI

## Overview

FinSight AI is an AI-powered financial intelligence platform designed to automate financial data collection, document understanding, market research, and investment analysis.

The long-term vision is to build a multi-agent financial assistant capable of:

* Fetching and maintaining market data automatically
* Understanding financial filings and macroeconomic reports
* Answering financial questions using Retrieval-Augmented Generation (RAG)
* Generating market summaries and research reports
* Coordinating multiple specialized agents through a central orchestrator

---

# Current Project Status

## Week 1 — Foundation & Database Layer ✅

### Objectives

Build the core backend infrastructure and financial database.

### Completed

#### Database Setup

* PostgreSQL database configured
* SQLAlchemy ORM configured
* Database connection management implemented
* Session handling implemented

#### Data Models

##### Stock

Stores:

* Ticker
* Company Name
* Exchange
* Sector

##### StockPrice

Stores:

* Open
* High
* Low
* Close
* Volume
* Date

##### MacroIndicator

Stores:

* Indicator Name
* Indicator Code
* Value
* Date

Supported indicators include:

* UNRATE
* CPIAUCSL
* GDP
* FEDFUNDS

### Outcome

A working financial database capable of storing stock and macroeconomic time-series data.

---

# Week 2 — Ingestion Agent ✅

### Objectives

Build an AI agent responsible for collecting and refreshing financial data.

### Completed

#### Stock Data Ingestion

Implemented:

* fetch_stock_data()

Features:

* Downloads stock data using yfinance
* Stores data in PostgreSQL
* Prevents duplicate records
* Returns human-readable status messages

#### Macroeconomic Data Ingestion

Implemented:

* fetch_macro_data()

Features:

* Downloads FRED economic data
* Stores data in PostgreSQL
* Prevents duplicate records

Supported indicators:

* UNRATE
* CPIAUCSL
* GDP
* FEDFUNDS

#### Data Freshness Validation

Implemented:

* check_last_updated()

Features:

* Checks latest stored records
* Determines whether refresh is required
* Applies different freshness rules for stocks and macroeconomic indicators

Example:

```python
MACRO_FRESHNESS = {
    "UNRATE": 45,
    "CPIAUCSL": 45,
    "FEDFUNDS": 45,
    "GDP": 120
}
```

#### Smart Refresh Wrappers

Implemented:

##### refresh_stock_if_needed()

Flow:

Check freshness → Refresh only if stale

##### refresh_macro_if_needed()

Flow:

Check freshness → Refresh only if stale

#### Ingestion Agent

Built using LangChain create_agent().

Capabilities:

* Check whether data is current
* Refresh stock data
* Refresh macroeconomic data

Restrictions:

* Does not perform financial analysis
* Does not generate market summaries
* Does not provide investment advice

### Outcome

A functioning ingestion layer capable of maintaining an up-to-date financial database.

---

# Week 3 — Financial RAG Pipeline ✅

### Objectives

Build a document intelligence layer capable of understanding financial reports and answering questions.

### Documents Indexed

* Apple 10-K
* Microsoft 10-K
* Nvidia 10-K
* FOMC Minutes
* Federal Reserve Monetary Policy Report

### Completed

#### PDF Loader

Implemented:

* pdf_loader.py

Features:

* Reads PDF files
* Extracts raw text

---

#### Text Chunking

Implemented:

* text_chunker.py

Features:

* Splits documents into overlapping chunks
* Uses RecursiveCharacterTextSplitter

Configuration:

* Chunk Size: 3000
* Chunk Overlap: 300

---

#### Embedding Generation

Implemented:

* embedding_generator.py

Model:

* sentence-transformers/all-MiniLM-L6-v2

Output:

* 384-dimensional embeddings

---

#### Vector Database

Implemented:

* FAISS Vector Store

Features:

* Stores document embeddings
* Supports semantic similarity search
* Persists vector index to disk

---

#### Metadata Store

Implemented:

* metadata.json

Stores:

* Chunk ID
* Source Document
* Company
* Document Type
* Chunk Text

Example:

```json
{
  "chunk_id": 0,
  "source": "apple_10k.pdf",
  "company": "Apple",
  "document_type": "10-K"
}
```

---

#### Multi-Document Indexing

Implemented:

* build_vector_store.py

Features:

* Automatically processes all PDFs
* Generates embeddings
* Builds FAISS index
* Creates metadata store

---

#### Semantic Retriever

Implemented:

* retriever.py

Capabilities:

* Converts user query into embeddings
* Retrieves top relevant document chunks

Example Queries:

* What did Apple say about iPhone revenue?
* What did Nvidia say about AI demand?
* What did the Federal Reserve say about inflation?
* What did Microsoft say about cloud growth?

---

#### Retrieval-Augmented Question Answering (RAG)

Implemented:

* rag_qa.py

Pipeline:

User Question
↓
Retriever
↓
Relevant Chunks
↓
Groq LLM
↓
Grounded Answer

Example:

Question:
What did Apple say about iPhone revenue?

Answer:
Apple reported iPhone net sales of $209.6 billion in FY2025, representing a 4% increase compared to FY2024.

### Outcome

A working Financial RAG system capable of answering questions from multiple financial documents using semantic search and LLM reasoning.

---

# Current Architecture

Database Layer

PostgreSQL
↓
Financial Data Storage

Document Intelligence Layer

Financial PDFs
↓
PDF Loader
↓
Chunking
↓
Embeddings
↓
FAISS
↓
Retriever
↓
RAG QA

Agent Layer

Ingestion Agent
↓
Financial Database

---

# Planned Work

## Week 4 — Research Agent

Planned Features:

* Query financial knowledge base
* Generate research answers
* Compare companies
* Analyze filings
* Summarize earnings and reports

---

## Week 5 — Market Summary Agent

Planned Features:

* Daily market summaries
* Economic event summaries
* Macro trend analysis

---

## Week 6 — Orchestrator

Planned Features:

* Route requests to correct agents
* Coordinate multiple agents
* Handle complex financial workflows

---

## Future Roadmap

* Portfolio Analysis
* Financial Dashboard UI
* Watchlists
* News Analysis
* Sentiment Analysis
* Multi-Agent Collaboration
* Investment Research Workflows

---

# Technology Stack

Backend

* Python

Database

* PostgreSQL
* SQLAlchemy

Data Sources

* Yahoo Finance (yfinance)
* FRED API

AI & LLM

* LangChain
* Groq
* Llama 3

RAG

* Sentence Transformers
* FAISS
* PyPDF

Version Control

* Git
* GitHub

---
