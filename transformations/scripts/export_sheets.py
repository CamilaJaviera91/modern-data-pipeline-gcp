# export_to_sheets.py
import os
import pandas as pd
import gspread
from dotenv import load_dotenv
from gspread_dataframe import set_with_dataframe
from oauth2client.service_account import ServiceAccountCredentials

load_dotenv()


def authorize_google_sheets():
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]
    creds_path = os.getenv("GOOGLE_CREDENTIALS_PATH")
    if not creds_path:
        raise ValueError("❌ GOOGLE_CREDENTIALS_PATH is not set.")
    creds = ServiceAccountCredentials.from_json_keyfile_name(creds_path, scope)
    return gspread.authorize(creds)


def upload_csvs_to_google_sheets(folder="data", spreadsheet_title="DBT Exported Tables"):
    client = authorize_google_sheets()
    spreadsheet = client.create(spreadsheet_title)
    spreadsheet.share('', perm_type='anyone', role='writer')

    for filename in os.listdir(folder):
        if filename.endswith(".csv"):
            table_name = filename.replace(".csv", "")
            df = pd.read_csv(os.path.join(folder, filename))

            worksheet = spreadsheet.add_worksheet(
                title=table_name,
                rows=str(len(df) + 1),
                cols=str(len(df.columns))
            )
            set_with_dataframe(worksheet, df)
            print(f"✅ Uploaded `{filename}` to Google Sheets")

    print(f"✅ All CSVs uploaded: {spreadsheet.url}")
