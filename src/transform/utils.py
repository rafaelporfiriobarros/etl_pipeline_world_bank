import chardet

def detect_encoding(file_path: str) -> str:
    """
    Detecta a codificação de um arquivo usando chardet.
    """
    with open(file_path, "rb") as f:
        result = chardet.detect(f.read())
    return result["encoding"]
