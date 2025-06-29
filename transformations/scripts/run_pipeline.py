# script/run_pipeline.py
from scripts.export_tables import export_all_tables

# Call when needed in your DAG or script
export_all_tables()