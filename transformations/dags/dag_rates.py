from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from scripts.load_exchange_rates import run_exchange_rates_load as rates

default_args = {
    'owner': 'camila',
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'start_date': datetime(2025, 7, 3),
}

with DAG(
    dag_id='1. dag_rates',
    description='Add rates',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
    max_active_runs=1,
    tags=['pipeline', 'rates', 'postgres']
) as dag:

    task_rates = PythonOperator(
        task_id='load_exchange_rates',
        python_callable=rates,
        )

    task_rates