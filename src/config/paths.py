# src/config/paths.py

import os

class Paths:
    """
    Centraliza caminhos utilizados no projeto.
    """

    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))

    # ----- Dados -----
    DATA_RAW = os.path.join(BASE_DIR, "data/raw")
    DATA_PROCESSED = os.path.join(BASE_DIR, "data/processed")
    DATA_FINAL = os.path.join(BASE_DIR, "data/final")

    # arquivos esperados
    PROJECTS_DEFAULT = os.path.join(DATA_RAW, "projects_data.csv")
    INDICATORS_DEFAULT = os.path.join(DATA_RAW, "population_data.csv")

    # banco SQLite final
    SQLITE_DB = os.path.join(DATA_FINAL, "worldbank.db")

    # logs
    LOGS = os.path.join(BASE_DIR, "logs/etl.log")

    @staticmethod
    def create_folders():
        for folder in [
            Paths.DATA_RAW,
            Paths.DATA_PROCESSED,
            Paths.DATA_FINAL,
            os.path.dirname(Paths.LOGS)
        ]:
            os.makedirs(folder, exist_ok=True)
