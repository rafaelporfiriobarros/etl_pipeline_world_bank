# src/extract/extract_api.py
"""
Helpers para extrair dados via HTTP / APIs:
- fetch_url_json: GET simples retornando json
- fetch_worldbank_indicator: wrapper específico para a API do World Bank (paginada)
"""
import logging
from typing import List, Dict, Any, Optional

import requests
import pandas as pd

logger = logging.getLogger(__name__)


def fetch_url_json(url: str, params: Optional[Dict[str, Any]] = None, timeout: int = 30) -> Any:
    """
    Faz GET em uma URL e retorna o JSON decodificado.
    Lança exceção em status != 200.
    """
    try:
        r = requests.get(url, params=params, timeout=timeout)
        r.raise_for_status()
        logger.info("Requisição GET OK: %s", r.url)
        return r.json()
    except Exception as exc:
        logger.exception("Erro na requisição GET %s: %s", url, exc)
        raise


def fetch_worldbank_indicator(countries: List[str], indicator: str, date: str = None, per_page: int = 1000) -> pd.DataFrame:
    """
    Consulta a API World Bank para um indicador e retorna DataFrame.
    Exemplo:
        countries = ['BR','US','CN']
        indicator = 'SP.POP.TOTL'
        date = '1990:2018'  # opcional

    A API retorna um JSON com [metadata, lista_de_resultados]. A função coleta a lista de resultados.
    """
    base = "http://api.worldbank.org/v2/countries/{}/indicators/{}"
    country_str = ";".join(countries)
    url = base.format(country_str, indicator)
    params = {"format": "json", "per_page": per_page}
    if date:
        params["date"] = date

    data = fetch_url_json(url, params=params)
    # data é uma lista: [meta, results]
    if not isinstance(data, list) or len(data) < 2:
        logger.error("Resposta da API inesperada: %s", data)
        raise ValueError("Resposta da API World Bank em formato inesperado")

    results = data[1]
    df = pd.DataFrame(results)
    logger.info("WorldBank API: indicador=%s países=%s rows=%d", indicator, countries, df.shape[0])
    return df
