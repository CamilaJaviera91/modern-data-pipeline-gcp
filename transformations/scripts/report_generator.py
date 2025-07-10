import os
import pandas as pd
import psycopg2
from dotenv import load_dotenv
import warnings

warnings.filterwarnings("ignore", category=UserWarning, module="pandas.io.sql")

load_dotenv()

def get_psycopg2_connection():
    return psycopg2.connect(
        host=os.getenv("DBT_HOST_TEST"),
        dbname=os.getenv("DBT_DBNAME"),
        user=os.getenv("DBT_USER"),
        password=os.getenv("DBT_PASSWORD"),
        port=os.getenv("DBT_PORT")
    )

def generate_reports():
    conn = get_psycopg2_connection()

    reports = {
        "order_by_status": """
            SELECT 
                EXTRACT(YEAR FROM mo.order_date) AS year,
                EXTRACT(MONTH FROM mo.order_date) AS month,
                status, 
                COUNT(*) AS orders
            FROM mock_schema.mock_orders mo 
            GROUP BY 
                mo.status, 
                EXTRACT(YEAR FROM mo.order_date), 
                EXTRACT(MONTH FROM mo.order_date)
            ORDER BY 
                EXTRACT(YEAR FROM mo.order_date), 
                EXTRACT(MONTH FROM mo.order_date), 
                orders DESC;
        """
    }

    os.makedirs("reports", exist_ok=True)

    try:
        for name, query in reports.items():
            df = pd.read_sql_query(query, conn)
            df.to_csv(f"./reports/{name}.csv", index=False)
    finally:
        conn.close()