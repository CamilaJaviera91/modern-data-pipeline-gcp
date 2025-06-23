import os
import pandas as pd
import psycopg2
from dotenv import load_dotenv

load_dotenv()

# Load DB credentials
conn = psycopg2.connect(
    host=os.getenv("DBT_HOST"),
    dbname=os.getenv("DBT_DBNAME"),
    user=os.getenv("DBT_USER"),
    password=os.getenv("DBT_PASSWORD"),
    port=os.getenv("DBT_PORT")
)

schema=os.getenv("DBT_SCHEMA")

# Load data from the final DBT table
query = f"""
SELECT 
    user_id, 
    concat(first_name, ' ', last_name) as name, 
    email, 
    date(created_at) as created_date,
    date(terminated_at) as termitation_date,
    status
FROM {schema}.mock_users
"""
df = pd.read_sql(query, conn)
conn.close()

# crete folder 'data' if it not exists
os.makedirs("data", exist_ok=True)  
df.to_csv("data/final_report.csv", index=False)

# ✅ Export to CSV
df.to_csv("data/final_report.csv", index=False)
print("✅ CSV export done")