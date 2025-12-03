# src/transform/validation.py
import pandas as pd

def validate_dataframe(df: pd.DataFrame, required_columns=None):
    required_columns = required_columns or []
    missing = [c for c in required_columns if c not in df.columns]
    if missing:
        raise ValueError(f"Colunas ausentes: {missing}")
    return True
