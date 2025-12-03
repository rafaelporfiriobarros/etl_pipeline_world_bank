# src/config/env.py

import os
from dotenv import load_dotenv

# Carregar .env automaticamente
load_dotenv()


def load_env(var: str, default=None):
    """
    Lê variáveis do ambiente. Retorna default se não encontrar.
    """
    return os.getenv(var, default)
