from pathlib import Path

import yaml


CONFIG_PATH = (
    Path(__file__).parent
    / "tickers.yaml"
)


def load_config():
    """
    Load project configuration.
    """

    with open(
        CONFIG_PATH,
        "r",
        encoding="utf-8"
    ) as f:

        return yaml.safe_load(f)


CONFIG = load_config()

TICKERS = [
    ticker["symbol"]
    for ticker in CONFIG["tickers"]
]

COMPANIES = {
    ticker["symbol"]: ticker["company"]
    for ticker in CONFIG["tickers"]
}

SETTINGS = CONFIG["settings"]