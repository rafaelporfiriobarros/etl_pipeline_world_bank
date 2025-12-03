# src/transform/fill_missing_values.py
import pandas as pd

def fill_missing(df: pd.DataFrame, column: str, method: str = "mean") -> pd.DataFrame:
    """
    Preenche valores ausentes com:
    - mean → média do grupo
    - ffill → forward fill por país
    - bfill → backward fill
    - ff_bf → ffill + bfill

    Baseado exatamente no notebook.
    """
    df = df.copy()

    if method == "mean":
        df[column] = df.groupby("Country Name")[column].transform(
            lambda x: x.fillna(x.mean())
        )

    elif method == "ffill":
        df[column] = df.sort_values("year").groupby("Country Name")[column].fillna(method="ffill")

    elif method == "bfill":
        df[column] = df.sort_values("year").groupby("Country Name")[column].fillna(method="bfill")

    elif method == "ff_bf":
        df[column] = (
            df.sort_values("year")
            .groupby("Country Name")[column]
            .fillna(method="ffill")
            .fillna(method="bfill")
        )

    else:
        raise ValueError("Método inválido: use mean, ffill, bfill ou ff_bf")

    return df
