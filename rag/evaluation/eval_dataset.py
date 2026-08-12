# rag/evaluation/eval_dataset.py

"""
Fixed evaluation dataset for RAG pipeline testing.
Each question includes expected keywords that should appear in a correct
retrieval/answer, and the source document it should be grounded in.
This dataset should NOT be regenerated per-run - it's a fixed benchmark
so results are comparable over time.
"""

EVAL_QUESTIONS = [
    # Apple 10-K questions
    {
        "id": "apple_1",
        "question": "What are the main risks Apple faces related to its supply chain?",
        "expected_source": "apple_10k.pdf",
        "expected_keywords": ["supply chain", "manufacturing", "suppliers"],
    },
    {
        "id": "apple_2",
        "question": "How does Apple generate revenue from services?",
        "expected_source": "apple_10k.pdf",
        "expected_keywords": ["services", "App Store", "subscription"],
    },
    {
        "id": "apple_3",
        "question": "What competitive risks does Apple mention in its filing?",
        "expected_source": "apple_10k.pdf",
        "expected_keywords": ["competition", "competitive", "market"],
    },

    # Microsoft 10-K questions
    {
        "id": "msft_1",
        "question": "What is Microsoft's strategy for cloud computing growth?",
        "expected_source": "microsoft_10k.pdf",
        "expected_keywords": ["cloud", "Azure", "growth"],
    },
    {
        "id": "msft_2",
        "question": "What risks does Microsoft identify related to cybersecurity?",
        "expected_source": "microsoft_10k.pdf",
        "expected_keywords": ["cybersecurity", "security", "breach"],
    },
    {
        "id": "msft_3",
        "question": "How does Microsoft describe its AI investments?",
        "expected_source": "microsoft_10k.pdf",
        "expected_keywords": ["AI", "artificial intelligence", "investment"],
    },

    # NVIDIA 10-K questions
    {
        "id": "nvda_1",
        "question": "What does NVIDIA say about demand for its data center products?",
        "expected_source": "nvidia_10k.pdf",
        "expected_keywords": ["data center", "demand", "GPU"],
    },
    {
        "id": "nvda_2",
        "question": "What risks does NVIDIA mention about semiconductor supply?",
        "expected_source": "nvidia_10k.pdf",
        "expected_keywords": ["semiconductor", "supply", "manufacturing"],
    },
    {
        "id": "nvda_3",
        "question": "How does NVIDIA describe competition in the AI chip market?",
        "expected_source": "nvidia_10k.pdf",
        "expected_keywords": ["competition", "AI chip", "market"],
    },

    # FOMC minutes questions
    {
        "id": "fomc_1",
        "question": "What did the Federal Reserve discuss about interest rates?",
        "expected_source": None,
        "expected_keywords": ["interest rate", "federal funds", "rate"],
    },
    {
        "id": "fomc_2",
        "question": "What economic indicators did the Fed committee review?",
        "expected_source": "fomc_minutes.pdf",
        "expected_keywords": ["inflation", "employment", "economic"],
    },

    # Monetary policy report questions
    {
        "id": "mpr_1",
        "question": "What does the monetary policy report say about inflation trends?",
        "expected_source": "monetary_policy_report.pdf",
        "expected_keywords": ["inflation", "price", "trend"],
    },
    {
        "id": "mpr_2",
        "question": "What does the report say about labor market conditions?",
        "expected_source": "monetary_policy_report.pdf",
        "expected_keywords": ["labor market", "employment", "unemployment"],
    },

    # Cross-document / harder questions
    {
        "id": "cross_1",
        "question": "How do Apple and Microsoft each describe their approach to services revenue?",
        "expected_source": None,  # could match either
        "expected_keywords": ["services", "revenue"],
    },
    {
        "id": "hard_1",
        "question": "What specific dollar figures does NVIDIA report for R&D spending?",
        "expected_source": "nvidia_10k.pdf",
        "expected_keywords": ["research and development", "R&D"],
    },
]