import os
import pandas as pd
import psycopg2
from dotenv import load_dotenv

load_dotenv()


def get_db_connection():
    return psycopg2.connect(
        host=os.getenv("DBT_HOST"),
        dbname=os.getenv("DBT_DBNAME"),
        user=os.getenv("DBT_USER"),
        password=os.getenv("DBT_PASSWORD"),
        port=os.getenv("DBT_PORT")
    )


def export_tables_to_csv(schema: str = None):
    conn = get_db_connection()
    schema = schema or os.getenv("DBT_SCHEMA")
    os.makedirs("data", exist_ok=True)

    with conn.cursor() as cur:
        cur.execute("""
            SELECT table_name 
            FROM information_schema.tables
            WHERE table_schema = %s AND table_type = 'BASE TABLE'
        """, (schema,))
        tables = cur.fetchall()

    for (table_name,) in tables:
        print(f"📦 Exporting table `{table_name}`...")
        query = f"SELECT * FROM {schema}.{table_name}"
        df = pd.read_sql(query, conn)

        csv_path = f"data/{table_name}.csv"
        df.to_csv(csv_path, index=False)
        print(f"💾 Saved to {csv_path}")

    conn.close()
    print("✅ CSV export completed.")


if __name__ == "__main__":
    export_tables_to_csv()
