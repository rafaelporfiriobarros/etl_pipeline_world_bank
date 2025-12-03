# src/load/load_sqlite.py
import logging
import sqlite3
import pandas as pd
from .utils import ensure_output_dir

logger = logging.getLogger(__name__)


def save_to_sqlite(
    df: pd.DataFrame,
    db_path: str,
    table_name: str,
    if_exists: str = "replace",
    index: bool = False,
) -> None:
    """
    Salva DataFrame em um banco SQLite.

    Params:
        db_path: caminho do arquivo .db
        table_name: nome da tabela
        if_exists: replace, append ou fail
    """
    try:
        ensure_output_dir(db_path)
        conn = sqlite3.connect(db_path)
        df.to_sql(table_name, conn, if_exists=if_exists, index=index)
        conn.close()
        logger.info(
            "Tabela '%s' salva no SQLite (%s). Rows=%d",
            table_name, db_path, len(df)
        )
    except Exception as exc:
        logger.exception("Erro ao salvar no SQLite %s: %s", db_path, exc)
        raise
