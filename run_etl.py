import os
from src.config.settings import Settings
from src.config.paths import Paths
from src.pipeline.etl_pipeline import ETLPipeline
from src.pipeline.logger import logger


def main():
    # Criar pastas necessárias (data/, logs/, etc.)
    Paths.create_folders()

    # Carrega configurações
    settings = Settings()

    logger.info("=== Iniciando execução do run_etl.py ===")
    logger.info(f"Caminho projetos: {settings.projects_path}")
    logger.info(f"Caminho indicadores: {settings.indicators_path}")
    logger.info(f"Arquivo final: {settings.output_csv}")

    # Inicializar pipeline
    pipeline = ETLPipeline(
        projects_path=settings.projects_path,
        indicators_path=settings.indicators_path,
        output_path=settings.output_csv
    )

    # Rodar ETL
    pipeline.run()

    logger.info("=== ETL finalizado com sucesso! ===")


if __name__ == "__main__":
    main()
