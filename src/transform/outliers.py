import pandas as pd

def remove_outliers(df: pd.DataFrame, columns=None, multiplier=1.5):
    """
    Remove outliers usando método IQR (Tukey).
    columns: lista de colunas numéricas para tratar.
    multiplier: coeficiente do IQR (1.5 padrão).
    """

    if columns is None:
        raise ValueError("Você deve fornecer uma lista de colunas numéricas em 'columns='.")

    df_clean = df.copy()

    for col in columns:
        if col not in df_clean.columns:
            raise ValueError(f"Coluna '{col}' não existe no dataframe")

        # converter para numérico (erros viram NaN)
        df_clean[col] = pd.to_numeric(df_clean[col], errors="coerce")

        q1 = df_clean[col].quantile(0.25)
        q3 = df_clean[col].quantile(0.75)
        iqr = q3 - q1

        lower = q1 - multiplier * iqr
        upper = q3 + multiplier * iqr

        df_clean = df_clean[(df_clean[col] >= lower) & (df_clean[col] <= upper)]

    return df_clean
