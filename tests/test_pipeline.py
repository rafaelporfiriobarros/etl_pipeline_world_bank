# tests/test_pipeline.py

from src.pipeline.etl_pipeline import ETLPipeline
import pandas as pd


def test_etl_pipeline(tmp_path, sample_projects_df, sample_indicators_df):
    # Criar arquivos temporários
    proj_path = tmp_path / "projects.csv"
    ind_path = tmp_path / "indicators.csv"

    sample_projects_df.to_csv(proj_path, index=False)
    sample_indicators_df.to_csv(ind_path, index=False)

    out = tmp_path / "output.csv"

    pipeline = ETLPipeline(
        projects_path=str(proj_path),
        indicators_path=str(ind_path),
        output_path=str(out)
    )

    pipeline.run()

    assert out.exists()
    df = pd.read_csv(out)
    assert not df.empty
