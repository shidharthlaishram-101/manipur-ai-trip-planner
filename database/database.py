import sqlite3
import pandas as pd
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

CSV_PATH = BASE_DIR / "data" / "destinations.csv"
DB_PATH = BASE_DIR / "database" / "tourism.db"


def create_database():
    # Read CSV
    df = pd.read_csv(CSV_PATH)

    # Connect to SQLite
    conn = sqlite3.connect(DB_PATH)

    # Store the dataset in SQLite
    df.to_sql(
        "destinations",
        conn,
        if_exists="replace",
        index=False
    )

    conn.close()

    print("Database created successfully!")
    print(f"Database location: {DB_PATH}")
    print(f"Number of destinations: {len(df)}")


if __name__ == "__main__":
    create_database()