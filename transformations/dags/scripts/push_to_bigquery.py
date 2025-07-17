# load_to_bigquery.py

import sys
import os
import pandas as pd
import psycopg2
from dotenv import load_dotenv
from pandas_gbq import to_gbq
import logging
import warnings
from google.oauth2 import service_account

# Add root path to allow relative imports (for utils)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils.quality_checks import check_not_empty, check_no_nulls, check_unique

warnings.filterwarnings("ignore", category=UserWarning, module="pandas_gbq")

# Setup logging
os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler("logs/push_to_bigquery.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

load_dotenv()


def get_postgres_connection():
    return psycopg2.connect(
        host=os.getenv("DBT_HOST"),
        dbname=os.getenv("DBT_DBNAME"),
        user=os.getenv("DBT_USER"),
        password=os.getenv("DBT_PASSWORD"),
        port=os.getenv("DBT_PORT")
    )


def load_tables_to_bigquery():
    schema = os.getenv("DBT_SCHEMA")
    project_id = os.getenv("BQ_PROJECT_ID")
    dataset = os.getenv("BQ_DATASET")
    credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS", "/opt/airflow/credentials/auth.json")
    credentials = service_account.Credentials.from_service_account_file(credentials_path)

    conn = get_postgres_connection()

    with conn.cursor() as cur:
        cur.execute("""
            SELECT table_name 
            FROM information_schema.tables
            WHERE table_schema = %s AND table_type = 'BASE TABLE'
        """, (schema,))
        tables = cur.fetchall()

    for (table_name,) in tables:
        logger.info(f"🔍 Loading table: {table_name}")
        query = f"SELECT * FROM {schema}.{table_name}"
        df = pd.read_sql(query, conn)

        try:
            logger.info(check_not_empty(df, table_name))
            if "user_id" in df.columns and table_name != "mock_orders":
                logger.info(check_unique(df, "user_id", table_name))

            if "email" in df.columns:
                logger.info(check_no_nulls(df, ["email"], table_name))

            logger.info(f"⬆️ Uploading {table_name} to BigQuery...")
            to_gbq(df, 
                   destination_table=f"{dataset}.{table_name}",
                   project_id=project_id,
                   if_exists="replace",
                   credentials=credentials)
            logger.info(f"✅ {table_name} uploaded successfully!")

        except Exception as e:
            logger.error(f"❌ Error processing table '{table_name}': {e}")

    conn.close()
    logger.info("🎉 All eligible tables have been processed.")
