# src/extract/extract_sql.py
"""
Leitura de bases SQL:
- sqlite (sqlite3/pandas)
- engines via SQLAlchemy (Postgres, MySQL, etc.)

As funções retornam DataFrames.
"""
import logging
import sqlite3
from typing import Optional

import pandas as pd
from sqlalchemy.engine import Engine
from sqlalchemy import create_engine

logger = logging.getLogger(__name__)


def read_sqlite(path: str, query: str, params: Optional[dict] = None) -> pd.DataFrame:
    """
    Lê uma query de um arquivo sqlite (.db) e retorna DataFrame.
    """
    try:
        conn = sqlite3.connect(path)
        df = pd.read_sql(query, conn, params=params)
        conn.close()
        logger.info("Consulta sqlite executada: %s -> rows=%d", path, df.shape[0])
        return df
    except Exception as exc:
        logger.exception("Erro ao ler sqlite %s: %s", path, exc)
        raise


def read_sqlalchemy(connection_string: str, query: str, **engine_kwargs) -> pd.DataFrame:
    """
    Lê uma query utilizando SQLAlchemy (útil para Postgres/MySQL).
    Exemplo de connection_string:
        'postgresql+psycopg2://user:pass@host:5432/dbname'
    """
    try:
        engine: Engine = create_engine(connection_string, **engine_kwargs)
        with engine.connect() as conn:
            df = pd.read_sql(query, conn)
        logger.info("Consulta SQLAlchemy executada: %s -> rows=%d", connection_string, df.shape[0])
        return df
    except Exception as exc:
        logger.exception("Erro ao executar query via SQLAlchemy: %s", exc)
        raise
