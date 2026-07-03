<div align="center">

# 📈 FinSight AI

### Multi-Agent Financial Intelligence Platform

*AI agents that research, predict, and reason about the market — grounded in real data.*

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?style=flat-square&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://streamlit.io)
[![LangGraph](https://img.shields.io/badge/LangGraph-Multi--Agent-1C3C3C?style=flat-square)](https://langchain-ai.github.io/langgraph/)
[![XGBoost](https://img.shields.io/badge/XGBoost-ML-2C8EBB?style=flat-square)](https://xgboost.ai)
[![FAISS](https://img.shields.io/badge/FAISS-Vector%20Search-purple?style=flat-square)](https://faiss.ai)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Supabase-336791?style=flat-square&logo=postgresql&logoColor=white)](https://supabase.com)
[![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?style=flat-square&logo=docker&logoColor=white)](https://docker.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)

[**Live Demo**](https://finsight-ai-manav.streamlit.app/) · [**API Docs**](https://manav2204-finsight-ai-api.hf.space/docs) · [**Report Bug**](#) · [**Request Feature**](#)

</div>

---

FinSight AI is an end-to-end financial intelligence platform powered by four coordinated AI agents. It combines Retrieval-Augmented Generation over financial documents, XGBoost-based stock movement prediction, and real-time macroeconomic data — deployed as a live, cloud-hosted production system rather than a local notebook demo.

---

## 🚀 Live Demo

| | |
|---|---|
| 🌐 **Web App** | [finsight-ai-manav.streamlit.app](https://finsight-ai-manav.streamlit.app/) |
| ⚡ **API** | [manav2204-finsight-ai-api.hf.space](https://manav2204-finsight-ai-api.hf.space/) |
| 📚 **API Docs (Swagger)** | [manav2204-finsight-ai-api.hf.space/docs](https://manav2204-finsight-ai-api.hf.space/docs) |

---

## 📸 Screenshots

<div align="center">

**Home Dashboard**
<img src="assets/screenshots/home.png" width="800"/>

**AI Prediction & Financial Research**
<img src="assets/screenshots/prediction.png" width="800"/>

**Market Intelligence Dashboard**
<img src="assets/screenshots/dashboard.png" width="800"/>

**Interactive Stock Charts**
<img src="assets\screenshots\chart.png" width="800"/>

**REST API Documentation**
<img src="assets/screenshots/swagger.png" width="800"/>

</div>

---

## ✨ Project Highlights

- 🤖 **Multi-Agent Architecture** — Four specialized AI agents orchestrated with LangGraph
- 📚 **Retrieval-Augmented Generation** — Semantic search over financial documents using FAISS
- 📈 **ML Stock Prediction** — XGBoost models trained on technical + macroeconomic features
- 🌍 **Macroeconomic Integration** — Live indicators from the FRED API feed directly into predictions
- ⚡ **Production REST API** — FastAPI backend with full Swagger documentation
- 📊 **Interactive Dashboard** — Streamlit frontend for exploring predictions and research
- ☁️ **Fully Cloud Deployed** — Live across three platforms, not just a local demo
- 🐳 **Containerized** — Reproducible local development with Docker Compose
- 🗄️ **Persistent Storage** — PostgreSQL on Supabase for market data and history

---

## 📊 Project Statistics

<div align="center">

| Metric | Value |
|:---|:---:|
| 🤖 AI Agents | 4 |
| 📈 ML Models | 7 (XGBoost) |
| 📄 Financial Documents | 5 |
| 📊 Supported Stocks | 7 |
| 🔍 Vector Database | FAISS |
| ⚡ REST API Endpoints | 6 |
| 🗄️ Database | PostgreSQL (Supabase) |
| ☁️ Cloud Platforms | 3 |
| 🐳 Dockerized | ✅ |
| 🌐 Live Deployments | 2 |

</div>

---

## 🏗️ Architecture

FinSight AI follows a modular, agent-based architecture. A central orchestrator routes each user query to one or more specialized agents, which independently retrieve data, run models, or perform semantic search before their outputs are combined into a final response.

### AI Agents

| Agent | Responsibility | Technologies |
|---|---|---|
| 🧭 **Orchestrator Agent** | Determines which agent(s) should handle a given query | LangGraph |
| 📥 **Ingestion Agent** | Retrieves and prepares market data, documents, and macro indicators | yfinance, FRED API |
| 📚 **Research Agent** | Performs semantic search and generates grounded research via RAG | FAISS, Sentence Transformers, Groq LLM |
| 📈 **ML Prediction Agent** | Predicts next-day stock movement with confidence scoring | XGBoost, Scikit-learn |

### System Flow

```
┌──────────┐     ┌────────────────┐     ┌──────────────┐
│   User   │────▶│  Streamlit UI  │────▶│  FastAPI API │
└──────────┘     └────────────────┘     └──────┬───────┘
                                                │
                                                ▼
                                    ┌───────────────────────┐
                                    │   Orchestrator Agent   │
                                    │       (LangGraph)      │
                                    └────────────┬────────────┘
                                                │
                       ┌────────────────────────┼────────────────────────┐
                       ▼                        ▼                        ▼
              ┌─────────────────┐     ┌─────────────────┐     ┌─────────────────────┐
              │ Ingestion Agent │     │  Research Agent │     │ ML Prediction Agent │
              └────────┬────────┘     └────────┬────────┘     └──────────┬──────────┘
                       ▼                        ▼                        ▼
              yfinance / FRED API      FAISS + Groq LLM           XGBoost Models
                       │                        │                        │
                       └────────────────────────┼────────────────────────┘
                                                ▼
                                    ┌───────────────────────┐
                                    │  PostgreSQL (Supabase) │
                                    └────────────┬────────────┘
                                                ▼
                                          Final Response
                                                │
                                                ▼
                                              User
```

---

## 🔑 Features

### 🧠 Multi-Agent Financial Intelligence
Four specialized agents coordinate through LangGraph to reason, retrieve, predict, and respond — rather than relying on a single LLM call to do everything.

### 📚 Retrieval-Augmented Generation
The Research Agent grounds its answers in real financial documents using FAISS semantic search before generating a response, reducing hallucination and improving factual accuracy.

**Indexed document types:**
- SEC 10-K Reports
- Federal Reserve Monetary Policy Reports
- FOMC Meeting Minutes

### 📈 ML-Powered Stock Prediction
The ML Prediction Agent uses XGBoost classifiers trained on technical indicators and macroeconomic features to estimate next-day price movement, with a confidence score and feature importance breakdown.

**Supported tickers:** AAPL · MSFT · NVDA · AMZN · GOOGL · META · TSLA

### 🌍 Macroeconomic Awareness
Live indicators from the FRED API — CPI, interest rates, unemployment, GDP, inflation — feed directly into the prediction pipeline's feature engineering.

### 📊 Interactive Dashboard
The Streamlit frontend lets users select a company, explore historical candlestick charts and volume, and view AI-generated predictions and research side by side.

### ⚡ Production REST API
A FastAPI backend exposes every capability — research, prediction, historical data — as documented, testable REST endpoints via Swagger.

---

## 🛠️ Tech Stack

| Category | Technologies |
|---|---|
| **Language** | Python 3.12, SQL |
| **AI / Orchestration** | LangGraph, LangChain, Groq LLM, RAG |
| **Machine Learning** | XGBoost, Scikit-learn, Pandas, NumPy |
| **Vector Search** | FAISS, Sentence Transformers, Hugging Face Embeddings |
| **Backend** | FastAPI, SQLAlchemy, Pydantic, Uvicorn |
| **Frontend** | Streamlit, Plotly |
| **Database** | PostgreSQL (Supabase) |
| **Financial Data** | Yahoo Finance, FRED API |
| **Deployment** | Docker, Docker Compose, Git LFS |
| **Cloud** | Streamlit Community Cloud, Hugging Face Spaces, Supabase |

---

## 📁 Project Structure

```
finsight-ai
│
├── agents/
│   ├── orchestrator_agent/
│   ├── ingestion_agent/
│   ├── research_agent/
│   └── ml_prediction_agent/
│
├── api/
│   ├── database/
│   ├── models/
│   └── main.py
│
├── rag/
│   ├── ingestion/
│   ├── embeddings/
│   ├── vectorstore/
│   ├── retrieval/
│   └── qa/
│
├── ui/
├── scripts/
├── config/
├── data/
│   ├── raw/
│   └── processed/
├── tests/
├── assets/
│   └── screenshots/
│
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── startup.py
├── README.md
└── LICENSE
```

| Folder | Purpose |
|---|---|
| `agents/` | The four specialized AI agents |
| `api/` | FastAPI backend, REST endpoints, database models |
| `rag/` | End-to-end RAG pipeline — ingestion, embeddings, FAISS indexing, retrieval |
| `ui/` | Streamlit dashboard |
| `scripts/` | Data download, model training, DB initialization utilities |
| `config/` | Ticker lists and environment-specific settings |
| `assets/` | Screenshots used in this README |

---

## 🔄 AI Workflow

This shows how a single user request is processed, from query to final response.

```
 User submits a question
          │
          ▼
   FastAPI receives request
          │
          ▼
  Orchestrator Agent (LangGraph)
   evaluates query intent
          │
          ├──────────────┬──────────────────┐
          ▼              ▼                  ▼
   Research-only   Prediction-only     Requires both
          │              │                  │
          ▼              ▼                  ▼
   Research Agent   ML Prediction     Research + ML
   retrieves &        Agent runs      Prediction Agents
   generates          XGBoost model    run in sequence
   grounded answer     inference
          │              │                  │
          └──────────────┴──────────────────┘
                          ▼
                 Combined response
                    assembled
                          │
                          ▼
                  Returned to user
                  via API / Dashboard
```

**Example routing:**

| Query Type | Example | Agents Invoked |
|---|---|---|
| Research only | *"What did the Fed say about rate cuts?"* | Research Agent |
| Prediction only | *"Will TSLA go up tomorrow?"* | ML Prediction Agent |
| Combined | *"Should I invest in Apple based on current conditions?"* | Research + ML Prediction |

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/manavbhatia2204/finsight-ai.git
cd finsight-ai
```

### Create a virtual environment

```bash
python -m venv venv
```

**Windows**
```bash
venv\Scripts\activate
```

**Linux / macOS**
```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure environment variables

Create a `.env` file in the project root:

```env
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=
DB_NAME=

GROQ_API_KEY=
FRED_API_KEY=

GROQ_MODEL=
FASTAPI_URL=
```

### Run locally

```bash
# Start all services with Docker
docker compose up --build
```

```bash
# Or run the dashboard directly
streamlit run ui/app.py
```

Once running:
- Dashboard → `http://localhost:8501`
- API → `http://localhost:8000`
- Swagger Docs → `http://localhost:8000/docs`

---

## ☁️ Deployment

FinSight AI is fully deployed to production across three cloud platforms — this isn't just a local demo.

```
        User
         │
         ▼
Streamlit Community Cloud   (Frontend)
         │
         ▼
FastAPI on Hugging Face Spaces   (Backend)
         │
         ▼
Supabase PostgreSQL   (Database)
```

| Layer | Platform | Notes |
|---|---|---|
| Frontend | Streamlit Community Cloud | Live dashboard, auto-deployed from `main` |
| Backend | Hugging Face Spaces | FastAPI REST API + Swagger docs |
| Database | Supabase | Managed PostgreSQL |
| Local Dev | Docker Compose | Full stack runs locally for development |
| Large Files | Git LFS | Tracks XGBoost models (`.pkl`), FAISS indexes, and PDFs |

### REST API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | API status |
| `GET` | `/health` | Health check |
| `GET` | `/ready` | Readiness check |
| `POST` | `/ask` | Query the multi-agent system |
| `GET` | `/predict/{ticker}` | Predict next-day stock movement |
| `GET` | `/stocks/{ticker}/history` | Retrieve historical stock prices |

Full interactive documentation is available via [Swagger UI](https://manav2204-finsight-ai-api.hf.space/docs).

### Deployment Engineering Note

Getting a multi-service AI system (agents, ML models, vector index, database) running reliably across three separate free-tier cloud platforms required solving binary asset management with Git LFS, and working around memory constraints during deployment.

---

## 🗺️ Roadmap

FinSight AI v1 delivers a complete, cloud-deployed multi-agent financial platform. Planned enhancements for v2:

### Data Platform
- [ ] Live market data integration
- [ ] Automated data refresh pipeline
- [ ] Support for additional companies
- [ ] Expanded document repository with automated ingestion

### AI & Agents
- [ ] Multi-step agent planning
- [ ] Portfolio analysis agent
- [ ] Risk analysis agent
- [ ] Company comparison agent
- [ ] Explainable AI for predictions

### Machine Learning
- [ ] Time-series forecasting models
- [ ] Hyperparameter optimization
- [ ] Automated model retraining
- [ ] Experiment tracking

### Platform Engineering
- [ ] CI/CD pipeline
- [ ] Kubernetes orchestration
- [ ] Monitoring & logging
- [ ] Model registry

---

## 👤 About Me

**Manav Bhatia**

AI Engineer based in Dublin, Ireland, currently completing an M.Sc. in Computing (Artificial Intelligence) at Dublin City University. Previously worked as an AI/ML Engineer at Iris Business Service Limited, and holds a B.Tech in AI & ML.

FinSight AI was built as an end-to-end, self-directed project to demonstrate practical experience across multi-agent systems, RAG pipelines, machine learning, and production deployment.

[![GitHub](https://img.shields.io/badge/GitHub-manavbhatia2204-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/manavbhatia2204)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Manav%20Bhatia-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://linkedin.com/in/manav-bhatia-569995267)

---

⭐ If you found this project interesting, consider giving the repository a star.

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
