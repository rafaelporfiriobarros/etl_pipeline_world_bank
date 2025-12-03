"""
Leitura de JSONs:
- suporta orientações do pandas (records, split, index, columns, values)
- fallback para json.load se necessário
"""

import json
import logging
from typing import Optional

import pandas as pd 

logger = logging.getLogger(__name__)

def read_json(path: str, orient: Optional[str] = None, **kwargs) -> pd.DataFrame:
    """
    Lê JSON no caminho informado.

    Params:
        path: caminho do arquivo JSON
        orient: orient para pd.read_json (ex: 'records')
        **kwargs: argumentos adicionais para pd.read_json

    Returns:
        pd.DataFrame
    """
    try:
        if orient:
            df = pd.read_json(path, orient=orient, **kwargs)
            logger.info("JSON lido com orient='%s': %s (shape=%s)", orient, path, df.shape)
            return df
        
        try:
            df = pd.read_json(path, **kwargs)
            logger.info("JSON lido com pandas: %s (shape=%s)", path, df.shape)
            return df
        except ValueError:
            logger.debug("pd.read_json falhou,  tentando json.load fallback.")
            with open(path, "r", encoding=kwargs.get("encoding", "utf-8")) as f:
                data = json.load(f)
            df = pd.DataFrame(data)
            logger.info("JSON lido com json.load fallback: %s (shape=%s)", path, df.shape)
            return df
    except Exception as exc:
        logger.exception("Erro ao ler JSON %s: %s", path, exc)
        raise   