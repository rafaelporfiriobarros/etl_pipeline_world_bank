# src/transform/scaling.py
import pandas as pd

def min_max_scale(x, x_min, x_max):
    return (x - x_min) / (x_max - x_min)


class Normalizer:
    """
    Guarda min/max e normaliza novos dados.
    Versão baseada no seu notebook.
    """
    def __init__(self, df: pd.DataFrame):
        self.params = []
        for column in df.columns:
            mn, mx = df[column].min(), df[column].max()
            self.params.append((mn, mx))

    def normalize(self, row):
        result = []
        for i, value in enumerate(row):
            mn, mx = self.params[i]
            result.append((value - mn) / (mx - mn))
        return result
