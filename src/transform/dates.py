# src/transform/dates.py
import pandas as pd


def parse_date_columns(df: pd.DataFrame, columns) -> pd.DataFrame:
    df = df.copy()
    for col in columns:
        df[col] = pd.to_datetime(df[col], errors="coerce")
    return df


def create_date_features(df: pd.DataFrame, date_col: str) -> pd.DataFrame:
    """
    Cria:
    - year
    - day
    - weekday
    """
    df = df.copy()
    df[f"{date_col}_year"] = df[date_col].dt.year
    df[f"{date_col}_day"] = df[date_col].dt.day
    df[f"{date_col}_weekday"] = df[date_col].dt.weekday

    return df
