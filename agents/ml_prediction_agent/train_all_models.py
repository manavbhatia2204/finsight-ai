import sys
from pathlib import Path

project_root = (
    Path(__file__)
    .resolve()
    .parent.parent.parent
)

sys.path.append(
    str(project_root)
)

from config.settings import TICKERS

from agents.ml_prediction_agent.train_model import (
    train_model
)


def train_all_models():
    """
    Train an ML model for every configured ticker.
    """

    successful = 0
    failed = 0

    for ticker in TICKERS:

        print(
            f"\n{'=' * 60}"
        )

        print(
            f"TRAINING {ticker}"
        )

        print(
            f"{'=' * 60}"
        )

        try:

            train_model(
                ticker
            )

            successful += 1

            print(
                f"\nSUCCESS: {ticker}"
            )

        except Exception as e:

            failed += 1

            print(
                f"\nFAILED: {ticker}"
            )

            print(str(e))

    print("\n" + "=" * 60)
    print("TRAINING SUMMARY")
    print("=" * 60)
    print(f"Successful : {successful}")
    print(f"Failed     : {failed}")
    print(f"Total      : {len(TICKERS)}")


if __name__ == "__main__":

    train_all_models()