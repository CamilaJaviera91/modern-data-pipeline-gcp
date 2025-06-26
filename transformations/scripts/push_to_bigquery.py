import os
import pandas as pd
import psycopg2
from dotenv import load_dotenv
from pandas_gbq import to_gbq
import warnings

warnings.filterwarnings("ignore", category=UserWarning, module="pandas_gbq")

load_dotenv()

# Validate env variables
required_env_vars = [
    "DBT_HOST", "DBT_DBNAME", "DBT_USER", "DBT_PASSWORD", "DBT_PORT",
    "DBT_SCHEMA", "BQ_PROJECT_ID", "BQ_DATASET"
]
for var in required_env_vars:
    if not os.getenv(var):
        raise EnvironmentError(f"❌ Missing environment variable: {var}")

def main():
    # PostgreSQL connection
    conn = psycopg2.connect(
        host=os.getenv("DBT_HOST"),
        dbname=os.getenv("DBT_DBNAME"),
        user=os.getenv("DBT_USER"),
        password=os.getenv("DBT_PASSWORD"),
        port=os.getenv("DBT_PORT")
    )

    schema = os.getenv("DBT_SCHEMA")
    project_id = os.getenv("BQ_PROJECT_ID")
    dataset = os.getenv("BQ_DATASET")

    with conn.cursor() as cur:
        cur.execute("""
            SELECT table_name 
            FROM information_schema.tables
            WHERE table_schema = %s AND table_type = 'BASE TABLE'
        """, (schema,))
        tables = cur.fetchall()

    for (table_name,) in tables:
        try:
            print(f"⬆️ Uploading {table_name} to BigQuery...")
            query = f"SELECT * FROM {schema}.{table_name}"
            df = pd.read_sql(query, conn)

            to_gbq(df, destination_table=f"{dataset}.{table_name}", project_id=project_id, if_exists='replace')
            print(f"✅ {table_name} uploaded successfully!")
        except Exception as e:
            print(f"❌ Failed to upload {table_name}: {e}")

    conn.close()

if __name__ == "__main__":
    main()
