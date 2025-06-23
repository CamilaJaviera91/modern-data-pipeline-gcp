import os
import pandas as pd
import psycopg2
from dotenv import load_dotenv

load_dotenv()

# Load DB credentials from environment variables
conn = psycopg2.connect(
    host=os.getenv("DBT_HOST"),
    dbname=os.getenv("DBT_DBNAME"),
    user=os.getenv("DBT_USER"),
    password=os.getenv("DBT_PASSWORD"),
    port=os.getenv("DBT_PORT")
)

schema = os.getenv("DBT_SCHEMA")

# Create 'data' folder if it doesn't exist
os.makedirs("data", exist_ok=True)

# Get the list of tables in the schema
with conn.cursor() as cur:
    cur.execute("""
        SELECT table_name 
        FROM information_schema.tables
        WHERE table_schema = %s AND table_type = 'BASE TABLE'
    """, (schema,))
    tables = cur.fetchall()

# Export each table to a CSV file
for (table_name,) in tables:
    print(f"Exporting table {table_name}...")
    query = f"SELECT * FROM {schema}.{table_name}"
    df = pd.read_sql(query, conn)
    csv_path = f"data/{table_name}.csv"
    df.to_csv(csv_path, index=False)
    print(f"Saved {csv_path}")

conn.close()
print("✅ Export of all tables completed.")