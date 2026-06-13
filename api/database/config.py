import os
from pathlib import Path

from dotenv import load_dotenv

# Locate project root
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Load .env explicitly
load_dotenv(BASE_DIR / ".env")

DB_CONFIG = {
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
    "database": os.getenv("DB_NAME"),
}
print(DB_CONFIG)