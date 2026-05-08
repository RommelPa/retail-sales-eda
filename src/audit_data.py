from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw" / "online_retail.csv"


def load_raw_data(path: Path = RAW_DATA_PATH) -> pd.DataFrame:
    """
    Load the raw Online Retail dataset.
    """
    if not path.exists():
        raise FileNotFoundError(
            f"Raw data file not found at {path}. "
            "Run 'python src/load_data.py' first."
        )

    df = pd.read_csv(path)
    df["InvoiceNo"] = df["InvoiceNo"].astype(str)
    df["StockCode"] = df["StockCode"].astype(str)
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"], errors="coerce")

    return df


def audit_data(df: pd.DataFrame) -> None:
    """
    Print a basic data quality audit.
    """
    print("=" * 80)
    print("ONLINE RETAIL DATA QUALITY AUDIT")
    print("=" * 80)

    print("\n1. Dataset shape")
    print(f"Rows: {df.shape[0]:,}")
    print(f"Columns: {df.shape[1]:,}")

    print("\n2. Column names")
    print(list(df.columns))

    print("\n3. Data types")
    print(df.dtypes)

    print("\n4. Missing values")
    missing_values = df.isna().sum().sort_values(ascending=False)
    missing_percent = (df.isna().mean() * 100).sort_values(ascending=False)

    missing_report = pd.DataFrame(
        {
            "missing_count": missing_values,
            "missing_percent": missing_percent.round(2),
        }
    )

    print(missing_report)

    print("\n5. Duplicate rows")
    print(f"Duplicate rows: {df.duplicated().sum():,}")

    print("\n6. Date range")
    print(f"Minimum InvoiceDate: {df['InvoiceDate'].min()}")
    print(f"Maximum InvoiceDate: {df['InvoiceDate'].max()}")

    print("\n7. Invoice analysis")
    total_invoices = df["InvoiceNo"].nunique()
    cancellation_rows = df["InvoiceNo"].str.startswith("C").sum()
    cancellation_invoices = df.loc[
        df["InvoiceNo"].str.startswith("C"), "InvoiceNo"
    ].nunique()

    print(f"Unique invoices: {total_invoices:,}")
    print(f"Cancellation rows: {cancellation_rows:,}")
    print(f"Cancellation invoices: {cancellation_invoices:,}")

    print("\n8. Quantity analysis")
    print(df["Quantity"].describe())
    print(f"Rows with Quantity <= 0: {(df['Quantity'] <= 0).sum():,}")

    print("\n9. UnitPrice analysis")
    print(df["UnitPrice"].describe())
    print(f"Rows with UnitPrice <= 0: {(df['UnitPrice'] <= 0).sum():,}")

    print("\n10. Country analysis")
    print(f"Unique countries: {df['Country'].nunique():,}")
    print(df["Country"].value_counts().head(10))

    print("\n11. Customer analysis")
    print(f"Unique customers: {df['CustomerID'].nunique():,}")
    print(f"Rows without CustomerID: {df['CustomerID'].isna().sum():,}")

    print("\n12. Sample rows")
    print(df.head())


if __name__ == "__main__":
    data = load_raw_data()
    audit_data(data)