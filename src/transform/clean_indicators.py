import pandas as pd

def clean_indicators_df(df_indicator: pd.DataFrame) -> pd.DataFrame:
    df = df_indicator.copy()

    # Exigido pelos testes — deve usar esses nomes exatamente
    if "Country Name" not in df.columns:
        raise ValueError("Coluna de nome do país não encontrada.")

    if "Country Code" not in df.columns:
        raise ValueError("Coluna de código do país não encontrada.")

    # Detectar colunas de ano (apenas dígitos)
    year_cols = [c for c in df.columns if c.isdigit()]
    if not year_cols:
        raise ValueError("Nenhuma coluna de ano encontrada no arquivo de indicadores.")

    # Wide → Long
    df_long = df.melt(
        id_vars=["Country Name", "Country Code"],
        value_vars=year_cols,
        var_name="year",
        value_name="population"
    )

    # Ano deve ser NUMÉRICO para o teste passar
    df_long["year"] = df_long["year"].astype(int)

    # Renomear colunas como esperado pelo pipeline
    df_long = df_long.rename(columns={
        "Country Name": "countryname",
        "Country Code": "countrycode"
    })

    return df_long
