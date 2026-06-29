import logging
import os
import sys
import time

from sqlalchemy import text
from sqlalchemy.exc import OperationalError

from api.database.connection import engine
from scripts.create_tables import create_all_tables

logging.basicConfig(
    level=logging.INFO
)

logger = logging.getLogger(
    "startup"
)


def wait_for_postgres():

    """
    Wait until PostgreSQL
    is accepting connections.
    """

    retries = 30
    delay = 2

    for attempt in range(
        1,
        retries + 1
    ):

        try:

            with engine.connect() as connection:

                connection.execute(
                    text("SELECT 1")
                )

            logger.info(
                "✅ PostgreSQL is ready."
            )

            return

        except OperationalError as e:

            logger.error(
        f"PostgreSQL connection failed: {e}"
    )

    logger.info(
        f"Waiting for PostgreSQL "
        f"({attempt}/{retries})..."
    )

    time.sleep(delay)

    logger.error(
        "❌ PostgreSQL did not become ready."
    )

    sys.exit(1)


def initialize_database():

    """
    Create all database tables.
    """

    logger.info(
        "Creating database tables..."
    )

    create_all_tables()

    logger.info(
        "✅ Database initialized."
    )


def start_api():

    """
    Replace current process
    with Uvicorn.
    """

    logger.info(
        "Starting FastAPI..."
    )

    os.execvp(
        "uvicorn",
        [
            "uvicorn",
            "api.main:app",
            "--host",
            "0.0.0.0",
            "--port",
            "8000"
        ]
    )


if __name__ == "__main__":

    wait_for_postgres()

    initialize_database()

    start_api()