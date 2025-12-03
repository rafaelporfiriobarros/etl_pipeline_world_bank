# src/transform/create_dummies.py
import pandas as pd

def create_dummies(df: pd.DataFrame, column: str) -> pd.DataFrame:
    dummies = pd.get_dummies(df[column], prefix=column)
    return pd.concat([df.drop(columns=[column]), dummies], axis=1)
