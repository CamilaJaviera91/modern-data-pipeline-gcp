# script/run_pipeline.py
from scripts.export_tables import export_all_tables

# Call when needed in your DAG or script
if __name__ == "__main__":
    
    print("🚀 Starting pipeline...")
    export_all_tables()
    print("✅ Pipeline completed.")