# src/load/load_database.py
import logging
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from .utils import ensure_output_dir

logger = logging.getLogger(__name__)


def _create_engine(db_url: str, **engine_kwargs) -> Engine:
    """
    db_url exemplo:
        postgresql+psycopg2://user:pass@localhost:5432/dbname
        mysql+pymysql://user:pass@localhost:3306/dbname
    """
    try:
        engine = create_engine(db_url, **engine_kwargs)
        return engine
    except Exception as exc:
        logger.exception("Erro ao criar engine: %s", exc)
        raise


def save_to_database(
    df: pd.DataFrame,
    db_url: str,
    table_name: str,
    if_exists: str = "replace",
    index: bool = False,
    **engine_kwargs,
) -> None:
    """
    Salva DataFrame em banco SQL (Postgres, MySQL, etc.).
    """
    try:
        engine = _create_engine(db_url, **engine_kwargs)

        with engine.connect() as conn:
            df.to_sql(table_name, conn, if_exists=if_exists, index=index)

        logger.info(
            "Tabela '%s' salva no banco SQL (%s). Rows=%d",
            table_name, db_url, len(df)
        )
    except Exception as exc:
        logger.exception("Erro ao salvar no banco SQL %s: %s", db_url, exc)
        raise
