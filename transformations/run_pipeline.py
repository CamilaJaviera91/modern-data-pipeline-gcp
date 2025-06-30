# script/run_pipeline.py
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from scripts.load_exchange_rates import run_exchange_rates_load as rates
from scripts.upload_tables import run_dbt_mock_models as upload
from scripts.export_csv import export_tables_to_csv as csv
from scripts.export_sheets import upload_csvs_to_google_sheets as sheets

# Call when needed in your DAG or script
if __name__ == "__main__":
    
    print("🚀 Starting pipeline...")

    rates()
    upload()
    csv()
    sheets()
    
    print("✅ Pipeline completed.")