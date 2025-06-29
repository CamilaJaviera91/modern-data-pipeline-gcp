import os
import requests
import psycopg2
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("EXCHANGE_API_KEY")
DB_HOST = os.getenv("DBT_HOST")
DB_NAME = os.getenv("DBT_DBNAME")
DB_USER = os.getenv("DBT_USER")
DB_PASSWORD = os.getenv("DBT_PASSWORD")
DB_PORT = os.getenv("DBT_PORT")
DB_SCHEMA = os.getenv("DBT_SCHEMA", "raw")  # Default to "raw" if not set

def fetch_exchange_rates():
    url = f"https://data.fixer.io/api/latest?access_key={API_KEY}&format=1"
    response = requests.get(url)

    if response.status_code != 200:
        print("❌ Response content:", response.text)
        raise Exception(f"Failed to fetch rates: HTTP {response.status_code}")
    
    data = response.json()

    if not data.get("success", False):
        raise Exception(f"❌ API error: {data.get('error')}")

    return data.get("rates", {})

def load_rates_to_db(rates: dict):
    conn = psycopg2.connect(
        host=DB_HOST, database=DB_NAME, user=DB_USER,
        password=DB_PASSWORD, port=DB_PORT
    )
    cur = conn.cursor()

    # Ensure schema and table exist
    cur.execute(f"CREATE SCHEMA IF NOT EXISTS {DB_SCHEMA};")
    cur.execute(f"""
        CREATE TABLE IF NOT EXISTS {DB_SCHEMA}.exchange_rates (
            currency VARCHAR PRIMARY KEY,
            rate FLOAT,
            date DATE
        );
    """)

    today = datetime.utcnow().date()

    for currency, rate in rates.items():
        cur.execute(f"""
            INSERT INTO {DB_SCHEMA}.exchange_rates (currency, rate, date)
            VALUES (%s, %s, %s)
            ON CONFLICT (currency) DO UPDATE
            SET rate = EXCLUDED.rate, date = EXCLUDED.date;
        """, (currency, rate, today))

    conn.commit()
    cur.close()
    conn.close()
    print(f"✅ Loaded {len(rates)} exchange rates into {DB_SCHEMA}.exchange_rates")

def run_exchange_rates_load():
    print("📡 Fetching exchange rates...")
    rates = fetch_exchange_rates()
    print("📥 Loading rates into database...")
    load_rates_to_db(rates)
    print("✅ Exchange rates pipeline finished.")
