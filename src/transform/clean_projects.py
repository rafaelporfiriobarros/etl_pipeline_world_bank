import pandas as pd

def clean_projects_df(df_projects: pd.DataFrame) -> pd.DataFrame:
    df = df_projects.copy()
    df.columns = df.columns.str.lower().str.strip()

    # Encontrar coluna de país
    country_candidates = ["countryname", "country", "country_name"]
    col_country = next((c for c in country_candidates if c in df.columns), None)
    if col_country is None:
        raise ValueError("Nenhuma coluna de país encontrada no dataset de projetos.")

    df = df.rename(columns={col_country: "countryname"})

    # Encontrar coluna de data
    date_candidates = ["boardapprovaldate", "board_approval_date"]
    col_date = next((c for c in date_candidates if c in df.columns), None)
    if col_date is None:
        raise ValueError("Nenhuma coluna de data encontrada para extrair o ano.")

    df[col_date] = pd.to_datetime(df[col_date], errors="coerce")

    # O teste EXIGE year numérico
    df["year"] = df[col_date].dt.year.astype(float)

    df = df.dropna(subset=["year"])

    return df
