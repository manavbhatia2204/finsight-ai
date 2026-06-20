import json
from pathlib import Path


METADATA_PATH = (
    Path(__file__).parent
    / "metadata.json"
)


def save_metadata(
    metadata: list
):
    with open(
        METADATA_PATH,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            metadata,
            file,
            ensure_ascii=False,
            indent=4
        )


def load_metadata():

    with open(
        METADATA_PATH,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)