# script/run_pipeline.py
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from scripts.export_tables import export_all_tables
from scripts.load_exchange_rates import run_exchange_rates_load

# Call when needed in your DAG or script
if __name__ == "__main__":
    
    print("🚀 Starting pipeline...")
    export_all_tables()
    run_exchange_rates_load()
    print("✅ Pipeline completed.")