import pandas as pd
import logging

logger = logging.getLogger("feature_engineering")

def add_gdp_per_capita(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Os testes exigem que exista esta coluna SEMPRE
    if "gdp" not in df.columns:
        df["gdp"] = pd.NA

    if "population" not in df.columns:
        df["population"] = pd.NA

    df["gdppercapita"] = df["gdp"] / df["population"]

    return df


def create_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df = add_gdp_per_capita(df)
    return df
