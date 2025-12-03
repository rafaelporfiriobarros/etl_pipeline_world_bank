# src/load/load_json.py

import json
import logging

logger = logging.getLogger("src.load.load_json")

def save_json(df, path):
    """
    Salva JSON em streaming evitando MemoryError.
    """

    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write("[\n")

            first = True
            for record in df.to_dict(orient="records"):
                if not first:
                    f.write(",\n")
                json.dump(record, f, ensure_ascii=False)
                first = False

            f.write("\n]")
        
        logger.info(f"JSON salvo com sucesso em {path}")

    except Exception as e:
        logger.error(f"Erro ao salvar JSON {path}: {e}")
