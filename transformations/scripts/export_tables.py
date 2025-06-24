import os
import pandas as pd
import psycopg2
from dotenv import load_dotenv
import gspread
from gspread_dataframe import set_with_dataframe
from oauth2client.service_account import ServiceAccountCredentials

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

# Set up Google Sheets API
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds_path = os.getenv("GOOGLE_SHEETS_CREDS_PATH")
creds = ServiceAccountCredentials.from_json_keyfile_name(creds_path, scope)
client = gspread.authorize(creds)

# Create new spreadsheet
spreadsheet = client.create("DBT Exported Tables")
spreadsheet.share('', perm_type='anyone', role='writer')  # Optional: public access

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