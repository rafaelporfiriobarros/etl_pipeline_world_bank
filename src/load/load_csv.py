# src/load/load_csv.py
import logging
import pandas as pd
from .utils import ensure_output_dir

logger = logging.getLogger(__name__)


def save_csv(df: pd.DataFrame, path: str, index: bool = False) -> None:
    """
    Salva DataFrame em CSV com UTF-8.
    """
    try:
        ensure_output_dir(path)
        df.to_csv(path, index=index, encoding="utf-8")
        logger.info("CSV salvo com sucesso em %s (shape=%s)", path, df.shape)
    except Exception as exc:
        logger.exception("Erro ao salvar CSV %s: %s", path, exc)
        raise
