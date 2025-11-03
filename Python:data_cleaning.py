import pandas as pd
import os

RAW_PATH = "data/raw/uk_hpi.csv"
OUT_PATH = "data/processed/hpi_cleaned.csv"


def clean_hpi():
    df = pd.read_csv(RAW_PATH)

    # Standardize column names
    df.columns = [c.lower().replace(" ", "_") for c in df.columns]

    # Convert date
    df["date"] = pd.to_datetime(df["date"])

    # Extract year and month
    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month

    # Convert price column to numeric
    if "average_price" in df.columns:
        df["average_price"] = pd.to_numeric(df["average_price"], errors="coerce")

    # Drop missing
    df = df.dropna(subset=["average_price"])

    # Sort
    df = df.sort_values("date")

    # Export
    os.makedirs("data/processed", exist_ok=True)
    df.to_csv(OUT_PATH, index=False)
    print("✅ Cleaned dataset saved to:", OUT_PATH)


if __name__ == "__main__":
    clean_hpi()
