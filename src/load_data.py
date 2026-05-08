from pathlib import Path

import pandas as pd
from ucimlrepo import fetch_ucirepo


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"
RAW_DATA_PATH = RAW_DATA_DIR / "online_retail.csv"


def download_online_retail(output_path: Path = RAW_DATA_PATH) -> pd.DataFrame:
    """
    Download the Online Retail dataset from the UCI Machine Learning Repository
    and save it as a CSV file in the raw data folder.
    """
    RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

    try:
        dataset = fetch_ucirepo(id=352)
    except Exception as exc:
        raise RuntimeError(
            "Could not download the dataset. Check your internet connection "
            "or the UCI repository availability."
        ) from exc

    data = dataset.data.features.copy()
    data.to_csv(output_path, index=False)

    return data


if __name__ == "__main__":
    df = download_online_retail()

    print("Dataset downloaded successfully.")
    print(f"Saved to: {RAW_DATA_PATH}")
    print(f"Rows: {df.shape[0]:,}")
    print(f"Columns: {df.shape[1]:,}")
    print("Column names:")
    print(list(df.columns))