import pandas as pd

def check_not_empty(df: pd.DataFrame, table_name: str):
    if df.empty:
        raise ValueError(f"❌ Table '{table_name}' is empty!")
    return f"✅ Table '{table_name}' is not empty."