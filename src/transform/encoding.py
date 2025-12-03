# src/transform/encoding.py
from .utils import detect_encoding

def ensure_utf8(path: str) -> str:
    enc = detect_encoding(path)
    return enc or "utf-8"
