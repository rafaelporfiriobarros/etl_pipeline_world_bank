"""
Módulo de extração: funções para CSV, JSON e XML, SQL e APIs.
"""
from .extract_csv import read_csv
from .extract_json import read_json
from .extract_xml import read_xml_records
from .extract_sql import read_sqlite, read_sqlalchemy
from .extract_api import fetch_worldbank_indicator, fetch_url_json

__all__ = [
    "read_csv",
    "read_json",
    "read_xml_records",
    "read_sqlite",
    "read_sqlalchemy",
    "fetch_worldbank_indicator",
    "fetch_url_json",
]
