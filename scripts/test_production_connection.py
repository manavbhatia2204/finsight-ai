import sys
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

from sqlalchemy import text
from api.database.connection import engine

try:
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))

    print("✅ Production Database Connection Successful")

except Exception as e:
    print("❌ Connection Failed")
    print(e)