# tests/test_extract.py

import pandas as pd
from src.extract.extract_csv import read_csv



def test_extract_csv(tmp_path):
    # criar CSV temporário
    f = tmp_path / "temp.csv"
    df = pd.DataFrame({"a": [1, 2], "b": ["x", "y"]})
    df.to_csv(f, index=False)

    df_loaded = read_csv(str(f))
    
    assert not df_loaded.empty
    assert df_loaded.shape == (2, 2)
