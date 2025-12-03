import logging
import os
from typing import Optional

logger = logging.getLogger(__name__)

def ensure_path(path: str) -> None:
    """
    Garante que a pasta para o arquivo existe.
    """

    dirname = os.path.dirname(path)
    if dirname and not os.path.exists(dirname):
        os.makedirs(dirname, exist_ok=True)
        logger.debug("Criada pasta: %s", dirname)

def detect_encoding(file_path: str, sample_bytes: int = 20000) -> Optional[str]:
    """
    Tenta detectar a codificação de um arquivo usando chardet, se disponível.
    Retorna None se chardet não estiver instalado ou não puder detectar.

    """

    try:
        import chardet
    except ImportError:
        logger.debug("chardet não instalado; pulando detecção de encoding.")
        return None
    
    with open(file_path, "rb") as f:
        raw = f.read(sample_bytes)
        result = chardet.detect(raw)
        encoding = result.get("encoding")
        logger.debug("Detecção de encoding: %s (confiança=%s)", encoding, result.get("confidence"))
        return encoding 
    
    