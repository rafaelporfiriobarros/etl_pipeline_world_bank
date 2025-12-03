# src/extract/extract_xml.py
"""
Leitura de XMLs usando BeautifulSoup.
Fornece uma função helper para extrair registros de XML com tag <record><field name=...>...
Adaptável para outros formatos XML com parse personalizado.
"""
import logging
from typing import List, Dict, Iterable, Optional

import pandas as pd

logger = logging.getLogger(__name__)


def read_xml_records(path: str, record_tag: str = "record", field_tag: str = "field", parser: str = "lxml") -> pd.DataFrame:
    """
    Lê um XML que contém múltiplos <record> ... </record> e retorna DataFrame.
    Cada <field name="X">valor</field> vira coluna 'X'.

    Params:
        path: caminho para o arquivo XML
        record_tag: nome da tag que agrupa um registro (ex: 'record')
        field_tag: nome da tag de campo (ex: 'field')
        parser: parser para BeautifulSoup (ex: 'lxml', 'html.parser')

    Returns:
        pd.DataFrame
    """
    try:
        from bs4 import BeautifulSoup  # local import para permitir import opcional
    except Exception as exc:
        logger.error("BeautifulSoup (bs4) não está instalado. Instale com `pip install beautifulsoup4 lxml`.")
        raise

    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    soup = BeautifulSoup(content, parser)
    records = []
    for rec in soup.find_all(record_tag):
        row = {}
        for field in rec.find_all(field_tag):
            # muitos XMLs usam 'name' no atributo ou 'key', pegamos o que existir
            name = field.get("name") or field.get("key") or field.name
            row[name] = field.text
        records.append(row)

    df = pd.DataFrame(records)
    logger.info("XML lido: %s (registros=%d, cols=%d)", path, len(records), len(df.columns))
    return df
