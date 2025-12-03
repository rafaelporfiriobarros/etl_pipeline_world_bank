# src/load/utils.py
import os


def ensure_output_dir(path: str):
    """
    Cria pasta automaticamente se não existir.
    """
    folder = os.path.dirname(path)
    if folder and not os.path.exists(folder):
        os.makedirs(folder, exist_ok=True)
