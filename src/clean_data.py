from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]

RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw" / "online_retail.csv"
PROCESSED_DATA_DIR = PROJECT_ROOT / "data" / "processed"

CLEAN_DATA_PATH = PROCESSED_DATA_DIR / "online_retail_clean.csv"
VALID_SALES_PATH = PROCESSED_DATA_DIR / "online_retail_valid_sales.csv"
CUSTOMER_SALES_PATH = PROCESSED_DATA_DIR / "online_retail_customer_sales.csv"


def load_raw_data(path: Path = RAW_DATA_PATH) -> pd.DataFrame:
    """
    Load raw Online Retail data.
    """
    if not path.exists():
        raise FileNotFoundError(
            f"Raw data file not found at {path}. "
            "Run 'python src/load_data.py' first."
        )

    df = pd.read_csv(path)

    return df


def clean_online_retail_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and enrich the Online Retail dataset.

    This function does not remove all unusual records blindly.
    It creates flags that preserve business meaning, especially cancellations.
    """
    df = df.copy()

    initial_rows = len(df)

    # Standardize text and types
    df["InvoiceNo"] = df["InvoiceNo"].astype(str).str.strip()
    df["StockCode"] = df["StockCode"].astype(str).str.strip()
    df["Description"] = df["Description"].astype("string").str.strip()
    df["Country"] = df["Country"].astype("string").str.strip()
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"], errors="coerce")

    # CustomerID comes with decimals because of missing values.
    # We keep it as a nullable string identifier, not as a numeric variable.
    df["CustomerID"] = df["CustomerID"].apply(
        lambda value: str(int(value)) if pd.notna(value) else pd.NA
    )
    df["CustomerID"] = df["CustomerID"].astype("string")

    # Remove exact duplicate rows
    duplicate_rows = df.duplicated().sum()
    df = df.drop_duplicates().reset_index(drop=True)

    # Business flags
    df["is_cancellation"] = df["InvoiceNo"].str.startswith("C")
    df["has_missing_customer"] = df["CustomerID"].isna()
    df["has_missing_description"] = df["Description"].isna()
    df["has_non_positive_quantity"] = df["Quantity"] <= 0
    df["has_non_positive_unit_price"] = df["UnitPrice"] <= 0

    # Revenue can be negative for cancellations or adjustments.
    df["Revenue"] = df["Quantity"] * df["UnitPrice"]

    # Time features
    df["InvoiceYear"] = df["InvoiceDate"].dt.year
    df["InvoiceMonth"] = df["InvoiceDate"].dt.to_period("M").astype(str)
    df["InvoiceDateOnly"] = df["InvoiceDate"].dt.date
    df["InvoiceHour"] = df["InvoiceDate"].dt.hour
    df["InvoiceDayOfWeek"] = df["InvoiceDate"].dt.day_name()

    print("Cleaning summary")
    print("-" * 80)
    print(f"Initial rows: {initial_rows:,}")
    print(f"Exact duplicate rows removed: {duplicate_rows:,}")
    print(f"Rows after removing duplicates: {len(df):,}")

    return df


def create_valid_sales_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create a dataset containing only valid sales transactions.
    """
    valid_sales = df[
        (~df["is_cancellation"])
        & (df["Quantity"] > 0)
        & (df["UnitPrice"] > 0)
        & (~df["Description"].isna())
        & (~df["InvoiceDate"].isna())
    ].copy()

    return valid_sales.reset_index(drop=True)


def create_customer_sales_dataset(valid_sales: pd.DataFrame) -> pd.DataFrame:
    """
    Create a valid sales dataset restricted to identified customers.
    """
    customer_sales = valid_sales[~valid_sales["CustomerID"].isna()].copy()

    return customer_sales.reset_index(drop=True)


def save_processed_data(
    clean_data: pd.DataFrame,
    valid_sales: pd.DataFrame,
    customer_sales: pd.DataFrame,
) -> None:
    """
    Save processed datasets.
    """
    PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)

    clean_data.to_csv(CLEAN_DATA_PATH, index=False)
    valid_sales.to_csv(VALID_SALES_PATH, index=False)
    customer_sales.to_csv(CUSTOMER_SALES_PATH, index=False)

    print("\nProcessed files saved")
    print("-" * 80)
    print(f"Clean data: {CLEAN_DATA_PATH}")
    print(f"Valid sales: {VALID_SALES_PATH}")
    print(f"Customer sales: {CUSTOMER_SALES_PATH}")


if __name__ == "__main__":
    raw_data = load_raw_data()
    clean_data = clean_online_retail_data(raw_data)
    valid_sales = create_valid_sales_dataset(clean_data)
    customer_sales = create_customer_sales_dataset(valid_sales)

    print("\nDataset shapes")
    print("-" * 80)
    print(f"Clean data: {clean_data.shape[0]:,} rows, {clean_data.shape[1]:,} columns")
    print(f"Valid sales: {valid_sales.shape[0]:,} rows, {valid_sales.shape[1]:,} columns")
    print(
        f"Customer sales: {customer_sales.shape[0]:,} rows, "
        f"{customer_sales.shape[1]:,} columns"
    )

    print("\nRevenue check")
    print("-" * 80)
    print(f"Valid sales revenue: {valid_sales['Revenue'].sum():,.2f}")
    print(f"Customer sales revenue: {customer_sales['Revenue'].sum():,.2f}")

    save_processed_data(clean_data, valid_sales, customer_sales)