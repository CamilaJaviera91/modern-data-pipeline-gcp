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
creds_path = os.getenv("GOOGLE_CREDENTIALS_PATH")
if not creds_path:
    raise ValueError("❌ GOOGLE_SHEETS_CREDS_PATH is not set. Check your .env file.")
creds = ServiceAccountCredentials.from_json_keyfile_name(creds_path, scope)
client = gspread.authorize(creds)

# Create new spreadsheet
spreadsheet = client.create("DBT Exported Tables")
spreadsheet.share('', perm_type='anyone', role='writer')  # Optional: public access
print(f"🔗 Google Sheet created: {spreadsheet.url}")

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

    # Upload to Google Sheets
    worksheet = spreadsheet.add_worksheet(title=table_name, rows=str(len(df)+1), cols=str(len(df.columns)))
    set_with_dataframe(worksheet, df)
    print(f"✅ Uploaded to Google Sheets: {table_name}")

conn.close()
print("✅ Export of all tables completed.")