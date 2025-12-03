# tests/conftest.py

import pytest
import pandas as pd


@pytest.fixture
def sample_projects_df():
    return pd.DataFrame({
        "id": ["P1", "P2"],
        "countryname": ["Brazil", "Chile"],
        "totalamt": ["1,000", "2,000"],
        "boardapprovaldate": ["2017-01-01", "2018-05-10"],
        "countrycode": ["BRA", "CHL"],
        "year": ["2017", "2018"]
    })


@pytest.fixture
def sample_indicators_df():
    return pd.DataFrame({
        "countryname": ["Brazil", "Chile"],
        "countrycode": ["BRA", "CHL"],
        "year": ["2017", "2018"],
        "gdp": [1500000, 900000],
        "population": [210000000, 18000000]
    })


@pytest.fixture
def merged_df(sample_projects_df, sample_indicators_df):
    return pd.merge(
        sample_projects_df,
        sample_indicators_df,
        on=["countrycode", "year"],
        how="left"
    )
