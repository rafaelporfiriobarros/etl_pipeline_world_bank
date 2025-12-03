# src/pipeline/etl_pipeline.py

import pandas as pd
from typing import Optional

from ..extract.extract_csv import read_csv
from ..extract.extract_json import read_json
from ..extract.extract_xml import read_xml_records
from ..extract.extract_sql import read_sqlite, read_sqlalchemy
from ..extract.extract_api import fetch_worldbank_indicator, fetch_url_json

from ..transform.clean_projects import clean_projects_df
from ..transform.clean_indicators import clean_indicators_df
from ..transform.merge import merge_projects_indicators
from ..transform.outliers import remove_outliers
from ..transform.scaling import Normalizer
from ..transform.feature_engineering import create_features

from ..load.load_csv import save_csv
from ..load.load_json import save_json
from ..load.load_sqlite import save_to_sqlite

from .logger import logger
from .utils import print_step


class ETLPipeline:
    """
    Pipeline ETL completo baseado no notebook do Banco Mundial.
    TODO: 
      - parametrização por YAML
      - execução via Airflow
    """

    def __init__(
        self,
        projects_path: Optional[str] = None,
        indicators_path: Optional[str] = None,
        output_path: str = "data/final/etl_output.csv"
    ):
        self.projects_path = projects_path
        self.indicators_path = indicators_path
        self.output_path = output_path

        self.df_projects = None
        self.df_indicators = None
        self.df_merged = None

    # ========================
    # EXTRACT
    # ========================
    def extract(self):
        print_step("Extract")

        if self.projects_path.endswith(".csv"):
            self.df_projects = read_csv(self.projects_path, dtype=str)
        else:
            raise ValueError("Formato de projetos não suportado")

        if self.indicators_path.endswith(".csv"):
            self.df_indicators = read_csv(self.indicators_path)
        else:
            raise ValueError("Formato de indicadores não suportado")

        logger.info("Extração concluída")

    # ========================
    # TRANSFORM
    # ========================
    def transform(self):
        print_step("Transform")

        # Limpeza dos dois datasets
        self.df_projects = clean_projects_df(self.df_projects)
        self.df_indicators = clean_indicators_df(self.df_indicators)

        # Merge usando countrycode + year
        self.df_merged = merge_projects_indicators(
            self.df_projects,
            self.df_indicators
        )

        # Remoção de outliers
        self.df_merged = remove_outliers(
            df=self.df_merged,
            columns=["population"]   # apenas esta existe
        )


        # Feature engineering
        self.df_merged = create_features(self.df_merged)

        logger.info("Transformação concluída")

    # ========================
    # LOAD
    # ========================
    def load(self):
        print_step("Load")

        # Salva CSV
        save_csv(self.df_merged, self.output_path)

        # Salva JSON paralelo
        json_path = self.output_path.replace(".csv", ".json")
        save_json(self.df_merged, json_path)

        # Salva em SQLite
        sqlite_path = "data/final/worldbank.db"
        save_to_sqlite(self.df_merged, sqlite_path, table_name="merged")

        logger.info("Carga concluída")

    # ========================
    # EXECUTAR ETL COMPLETO
    # ========================
    def run(self):
        logger.info("Iniciando pipeline ETL")

        self.extract()
        self.transform()
        self.load()

        logger.info("Pipeline concluído com sucesso!")
