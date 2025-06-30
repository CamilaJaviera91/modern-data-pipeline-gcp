# script/run_pipeline.py
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from scripts.load_exchange_rates import run_exchange_rates_load as rates
from scripts.upload_tables import run_dbt_mock_models as upload

# Call when needed in your DAG or script
if __name__ == "__main__":
    
    print("🚀 Starting pipeline...")
    rates()
    upload()
    print("✅ Pipeline completed.")