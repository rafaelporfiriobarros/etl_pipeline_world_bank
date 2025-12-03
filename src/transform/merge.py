# src/transform/merge.py

import pandas as pd
import unicodedata
import re


# ====================================================
# NORMALIZAÇÃO DE NOMES DE PAÍS
# ====================================================
def normalize_country(name: str) -> str:
    if pd.isna(name):
        return ""

    name = name.lower().strip()

    # Remover acentos
    name = unicodedata.normalize("NFD", name)
    name = name.encode("ascii", "ignore").decode("utf-8")

    # Remover caracteres não alfabéticos
    name = re.sub(r"[^a-z ]", "", name)
    name = re.sub(r"\s+", " ", name).strip()

    return name


# ====================================================
# FUNÇÃO DE MERGE PRINCIPAL (ROBUSTA)
# ====================================================
def merge_projects_indicators(df_projects: pd.DataFrame, df_indicators: pd.DataFrame) -> pd.DataFrame:

    dfp = df_projects.copy()
    dfi = df_indicators.copy()

    # Padronizar nomes
    dfp.columns = dfp.columns.str.lower().str.strip()
    dfi.columns = dfi.columns.str.lower().str.strip()

    # ------------------------------------------------
    # MÉTODO 1 — MERGE POR countryname_norm + year
    # ------------------------------------------------
    if "countryname" in dfp.columns and "countryname" in dfi.columns \
       and "year" in dfp.columns and "year" in dfi.columns:

        dfp["countryname_norm"] = dfp["countryname"].apply(normalize_country)
        dfi["countryname_norm"] = dfi["countryname"].apply(normalize_country)

        m1 = pd.merge(
            dfp,
            dfi,
            how="left",
            on=["countryname_norm", "year"],
            suffixes=("", "_ind")
        )

        # Se encontrou populações, usamos este merge
        if m1["population"].notna().sum() > 0:
            m1 = m1.drop(columns=[c for c in m1.columns if c.endswith("_ind")], errors="ignore")
            m1 = m1.drop(columns=["countryname_norm"], errors="ignore")
            m1 = m1.loc[:, ~m1.columns.duplicated()]
            return m1

    # ------------------------------------------------
    # MÉTODO 2 — MERGE POR countrycode + year
    # ------------------------------------------------
    if "countrycode" in dfp.columns and "countrycode" in dfi.columns \
       and "year" in dfp.columns and "year" in dfi.columns:

        m2 = pd.merge(
            dfp,
            dfi,
            how="left",
            on=["countrycode", "year"],
            suffixes=("", "_ind")
        )

        if m2["population"].notna().sum() > 0:
            m2 = m2.drop(columns=[c for c in m2.columns if c.endswith("_ind")], errors="ignore")
            m2 = m2.loc[:, ~m2.columns.duplicated()]
            return m2

    # ------------------------------------------------
    # MÉTODO 3 — MERGE POR ANO APENAS (fallback final)
    # ------------------------------------------------
    if "year" in dfp.columns and "year" in dfi.columns:
        m3 = pd.merge(
            dfp,
            dfi,
            how="left",
            on="year",
            suffixes=("", "_ind")
        )
        m3 = m3.drop(columns=[c for c in m3.columns if c.endswith("_ind")], errors="ignore")
        m3 = m3.loc[:, ~m3.columns.duplicated()]
        return m3

    # ------------------------------------------------
    # ÚLTIMO RECURSO — retorna apenas projetos
    # (melhor do que retornar vazio)
    # ------------------------------------------------
    return dfp
