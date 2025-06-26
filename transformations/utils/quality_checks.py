import pandas as pd

def check_not_empty(df: pd.DataFrame, table_name: str):
    if df.empty:
        raise ValueError(f"❌ Table '{table_name}' is empty!")
    return f"✅ Table '{table_name}' is not empty."

def check_no_nulls(df: pd.DataFrame, columns: list, table_name: str):
    nulls = df[columns].isnull().sum()
    issues = [f"'{col}' has {nulls[col]} nulls" for col in columns if nulls[col] > 0]
    if issues:
        raise ValueError(f"❌ Null check failed for {table_name}: " + ", ".join(issues))
    return f"✅ No nulls in columns {columns} for table '{table_name}'."