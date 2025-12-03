import pandas as pd
import chardet
import logging

logger = logging.getLogger("src.extract.extract_csv")

def read_csv(path: str, **kwargs) -> pd.DataFrame:

    # Detectar encoding
    with open(path, "rb") as f:
        raw = f.read()
    enc = chardet.detect(raw)["encoding"]

    logger.info(f"Tentando ler CSV {path} com encoding={enc}")

    # === CASO ESPECIAL: PROJECTS_DATA.CSV ===
    if "projects_data.csv" in path.lower():
        logger.info("Arquivo de projetos detectado — delimitador personalizado")

        with open(path, "r", encoding=enc, errors="ignore") as f:
            first_line = f.readline()

        possible_delims = ["\t", ";", ","]

        for delim in possible_delims:
            if delim in first_line:
                logger.info(f"Separador detectado: '{delim}'")
                return pd.read_csv(
                    path,
                    encoding=enc,
                    sep=delim,
                    engine="python",
                    on_bad_lines="skip",
                    **kwargs
                )

        logger.info("Usando separador regex por múltiplos espaços")
        return pd.read_csv(
            path,
            encoding=enc,
            sep=r"\s{2,}",
            engine="python",
            on_bad_lines="skip",
            **kwargs
        )

    # === CASO ESPECIAL: POPULATION_DATA.CSV ===
    if "population_data.csv" in path.lower():
        logger.info("Arquivo de indicadores detectado — leitura especial WDI")

        df = pd.read_csv(
            path,
            encoding=enc,
            sep=",",
            skiprows=4,      # pula as 4 linhas iniciais
            header=0,        # linha 5 vira header
            quotechar='"',
            engine="python",
            on_bad_lines="skip",
            **kwargs
        )

        # Remover colunas lixo
        df = df.drop(columns=[c for c in df.columns if "Unnamed" in c], errors="ignore")

        # Normalizar colunas
        df.columns = df.columns.str.replace('"', "", regex=False).str.strip()

        return df

    # === CASO PADRÃO ===
    return pd.read_csv(path, encoding=enc, **kwargs)
