import sys
from pathlib import Path

project_root = (
    Path(__file__)
    .resolve()
    .parent.parent
)

sys.path.append(
    str(project_root)
)

from api.database.connection import engine
from api.models import *
from api.models.base import Base


def create_all_tables():
    """
    Create all database tables.
    """

    print(
        "Creating database tables..."
    )

    Base.metadata.create_all(
        bind=engine
    )

    print(
        "✅ Tables created successfully"
    )


if __name__ == "__main__":

    create_all_tables()