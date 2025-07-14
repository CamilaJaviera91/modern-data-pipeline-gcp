import os
import pandas as pd
import psycopg2
from dotenv import load_dotenv
import warnings

warnings.filterwarnings("ignore", category=UserWarning, module="pandas.io.sql")

load_dotenv()

def get_psycopg2_connection():
    return psycopg2.connect(
        host=os.getenv("DBT_HOST"),
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
        """,

        "sales_by_clients": """
            SELECT 
                CONCAT(mu.first_name,' ',mu.last_name) AS name, 
                mu.status,
                COUNT(mo.order_id) AS orders,
                ROUND(SUM(mo.amount * er.rate)) AS total
            FROM mock_schema.mock_users mu
            JOIN mock_schema.mock_orders mo ON mo.user_id = mu.user_id
            CROSS JOIN (
            SELECT rate
            FROM mock_schema.exchange_rates
            WHERE currency = 'CLP'
            LIMIT 1
            ) er
            GROUP BY 
                mu.first_name, 
                mu.last_name, 
                mu.status
            ORDER BY total DESC;
        """
    }

    os.makedirs("reports", exist_ok=True)

    try:
        for name, query in reports.items():
            df = pd.read_sql_query(query, conn)
            df.to_csv(f"./reports/{name}.csv", index=False)
    finally:
        conn.close()