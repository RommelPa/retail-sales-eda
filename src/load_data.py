from pathlib import Path
from urllib.request import urlretrieve
from zipfile import ZipFile

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"

DATASET_URL = "https://archive.ics.uci.edu/static/public/352/online+retail.zip"
RAW_ZIP_PATH = RAW_DATA_DIR / "online_retail.zip"
RAW_CSV_PATH = RAW_DATA_DIR / "online_retail.csv"

EXPECTED_COLUMNS = [
    "InvoiceNo",
    "StockCode",
    "Description",
    "Quantity",
    "InvoiceDate",
    "UnitPrice",
    "CustomerID",
    "Country",
]


def download_online_retail() -> pd.DataFrame:
    """
    Download the Online Retail dataset from the UCI Machine Learning Repository,
    extract the Excel file, load it into pandas, and save it as CSV.
    """
    RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

    print("Downloading dataset...")
    urlretrieve(DATASET_URL, RAW_ZIP_PATH)

    print("Extracting Excel file...")
    with ZipFile(RAW_ZIP_PATH, "r") as zip_file:
        excel_files = [
            file_name
            for file_name in zip_file.namelist()
            if file_name.lower().endswith(".xlsx")
        ]

        if not excel_files:
            raise FileNotFoundError("No Excel file found inside the downloaded ZIP.")

        excel_file_name = excel_files[0]

        with zip_file.open(excel_file_name) as excel_file:
            df = pd.read_excel(excel_file, engine="openpyxl")

    missing_columns = [col for col in EXPECTED_COLUMNS if col not in df.columns]

    if missing_columns:
        raise ValueError(f"Missing expected columns: {missing_columns}")

    df.to_csv(RAW_CSV_PATH, index=False)

    return df


if __name__ == "__main__":
    data = download_online_retail()

    print("Dataset downloaded successfully.")
    print(f"Saved to: {RAW_CSV_PATH}")
    print(f"Rows: {data.shape[0]:,}")
    print(f"Columns: {data.shape[1]:,}")
    print("Column names:")
    print(list(data.columns))