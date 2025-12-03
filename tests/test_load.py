# tests/test_load.py

from src.load.load_csv import save_csv
from src.load.load_json import save_json
from src.load.load_sqlite import save_to_sqlite
import sqlite3


def test_save_csv(tmp_path, merged_df):
    path = tmp_path / "out.csv"
    save_csv(merged_df, str(path))
    assert path.exists()


def test_save_json(tmp_path, merged_df):
    path = tmp_path / "out.json"
    save_json(merged_df, str(path))
    assert path.exists()


def test_save_sqlite(tmp_path, merged_df):
    db_path = tmp_path / "test.db"
    save_to_sqlite(merged_df, str(db_path), "merged")

    conn = sqlite3.connect(db_path)
    df = conn.execute("SELECT * FROM merged").fetchall()
    assert len(df) == merged_df.shape[0]
    conn.close()
