import os

import requests
from dotenv import load_dotenv


load_dotenv()

BASE_URL = os.getenv(
    "FASTAPI_URL",
    "http://localhost:8000"
)


def predict_stock(ticker: str):
    """
    Fetch stock prediction from FastAPI.
    """

    response = requests.get(
        f"{BASE_URL}/predict/{ticker}"
    )

    response.raise_for_status()

    return response.json()


def ask_question(question: str):
    """
    Send financial question to FinSight AI.
    """

    response = requests.post(
        f"{BASE_URL}/ask",
        json={
            "query": question
        }
    )

    response.raise_for_status()

    return response.json()


def get_stock_history(
    ticker: str,
    limit: int = 60
):
    """
    Fetch historical stock prices.
    """

    response = requests.get(
        f"{BASE_URL}/stocks/{ticker}/history",
        params={
            "limit": limit
        }
    )

    response.raise_for_status()

    return response.json()