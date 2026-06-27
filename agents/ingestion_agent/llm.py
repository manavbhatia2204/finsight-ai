import os
from pathlib import Path

from dotenv import load_dotenv
from langchain_groq import ChatGroq

BASE_DIR = Path(__file__).resolve().parent.parent.parent

load_dotenv(BASE_DIR / ".env")

llm = ChatGroq(
    model=os.getenv(
        "GROQ_MODEL",
        "gpt-oss-20b"
    ),
    api_key=os.getenv(
        "GROQ_API_KEY"
    ),
    temperature=0
)