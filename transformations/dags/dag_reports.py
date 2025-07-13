from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys
import os

# Add project root to sys.path to allow imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Import the function
from scripts.export_csv import export_tables_to_csv as csv
from scripts.report_generator import generate_reports as reports

# Define DAG
default_args = {
    "owner": "camila",
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="3_generate_reports_dag",
    default_args=default_args,
    description="Generate CSV reports from PostgreSQL tables",
    schedule_interval="@daily",
    start_date=datetime(2025, 7, 1),
    catchup=False,
    tags=["reporting", "postgres"],
) as dag:

    task_csv = PythonOperator(
        task_id='export_tables_to_csv',
        python_callable=csv,
    )

    task_report = PythonOperator(
        task_id="generate_reports",
        python_callable=reports
    )

    task_csv >> task_report