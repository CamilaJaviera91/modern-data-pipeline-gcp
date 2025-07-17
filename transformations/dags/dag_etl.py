from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scripts.upload_tables import run_dbt_mock_models as upload
from scripts.export_sheets import upload_csvs_to_google_sheets as sheets
from scripts.push_to_bigquery import load_tables_to_bigquery as bigquery

default_args = {
    'owner': 'camila',
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'start_date': datetime(2025, 7, 3),
}

with DAG(
    dag_id='2_dag_etl',
    default_args=default_args,
    schedule_interval='0 * * * *',
    catchup=False,
    max_active_runs=1,
    tags=['dbt', 'gcp', 'pipeline', 'postgres']
) as dag:

    task_upload = PythonOperator(
        task_id='run_dbt_mock_models',
        python_callable=upload,
    )

    task_sheets = PythonOperator(
        task_id='upload_csvs_to_google_sheets',
        python_callable=sheets,
    )

    task_bigquery = PythonOperator(
        task_id='load_tables_to_bigquery',
        python_callable=bigquery,
    )

    task_upload >> task_sheets >> task_bigquery