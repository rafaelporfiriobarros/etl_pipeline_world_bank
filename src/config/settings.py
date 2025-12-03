# src/config/settings.py

from dataclasses import dataclass
from .env import load_env
from .paths import Paths
from .constants import DEFAULT_ENCODING


@dataclass
class Settings:
    """
    Classe principal de configurações do projeto.
    """

    # Configurações gerais
    encoding: str = DEFAULT_ENCODING
    debug: bool = load_env("DEBUG", "false").lower() == "true"

    # Arquivos padrão
    projects_path: str = Paths.PROJECTS_DEFAULT
    indicators_path: str = Paths.INDICATORS_DEFAULT

    # Banco SQLite
    sqlite_path: str = Paths.SQLITE_DB

    # Caminho final do CSV
    output_csv: str = f"{Paths.DATA_FINAL}/etl_output.csv"

    # API World Bank (exemplo)
    api_base_url: str = "http://api.worldbank.org/v2"

    def show(self):
        """
        Imprime todas as configs de forma organizada.
        """
        print("\n=== SETTINGS ===")
        for attr, value in self.__dict__.items():
            print(f"{attr}: {value}")
