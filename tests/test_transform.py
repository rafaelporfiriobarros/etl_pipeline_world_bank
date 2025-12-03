# tests/test_transform.py

import pandas as pd
from src.transform.clean_projects import clean_projects_df
from src.transform.clean_indicators import clean_indicators_df
from src.transform.merge import merge_projects_indicators
from src.transform.feature_engineering import create_features
from src.transform.outliers import remove_outliers


def test_clean_projects(sample_projects_df):
    df = clean_projects_df(sample_projects_df)
    assert "totalamt" in df.columns
    assert df["totalamt"].dtype in [float, int]


def test_clean_indicators(sample_indicators_df):
    df = clean_indicators_df(sample_indicators_df)
    assert "gdp" in df.columns
    assert "population" in df.columns


def test_merge(sample_projects_df, sample_indicators_df):
    df = merge_projects_indicators(sample_projects_df, sample_indicators_df)
    assert df.shape[0] == 2
    assert "gdp" in df.columns


def test_outliers(merged_df):
    df = remove_outliers(merged_df, columns=["gdp"])
    assert not df.empty   # com dados simples, nada deve ser removido


def test_features(merged_df):
    df = create_features(merged_df)
    assert "gdppercapita" in df.columns
