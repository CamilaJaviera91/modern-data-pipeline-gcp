import os
import pandas as pd
import psycopg2
from dotenv import load_dotenv
import gspread
from gspread_dataframe import set_with_dataframe
from oauth2client.service_account import ServiceAccountCredentials

load_dotenv()


def get_db_connection():
    return psycopg2.connect(
        host=os.getenv("DBT_HOST"),
        dbname=os.getenv("DBT_DBNAME"),
        user=os.getenv("DBT_USER"),
        password=os.getenv("DBT_PASSWORD"),
        port=os.getenv("DBT_PORT")
    )


def authorize_google_sheets():
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]
    creds_path = os.getenv("GOOGLE_CREDENTIALS_PATH")
    if not creds_path:
        raise ValueError("❌ GOOGLE_CREDENTIALS_PATH is not set. Check your .env file.")
    creds = ServiceAccountCredentials.from_json_keyfile_name(creds_path, scope)
    return gspread.authorize(creds)


def export_all_tables(schema: str = None, spreadsheet_title: str = "DBT Exported Tables"):
    conn = get_db_connection()
    schema = schema or os.getenv("DBT_SCHEMA")
    client = authorize_google_sheets()

    spreadsheet = client.create(spreadsheet_title)
    spreadsheet.share('', perm_type='anyone', role='writer')
    print(f"🔗 Google Sheet created: {spreadsheet.url}")

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

        worksheet = spreadsheet.add_worksheet(
            title=table_name,
            rows=str(len(df) + 1),
            cols=str(len(df.columns))
        )
        set_with_dataframe(worksheet, df)
        print(f"✅ Uploaded to Google Sheets: {table_name}")

    conn.close()
    print(f"✅ Export of all tables completed into {spreadsheet.url}")