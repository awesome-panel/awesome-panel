# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring

import pandas as pd
import pytest

from application.pages.pandas_profiling_app.pandas_profiling_app import PandasProfilingApp, view


@pytest.fixture
def csv_url():
    return "http://eforexcel.com/wp/wp-content/uploads/2017/07/100-Sales-Records.zip"


@pytest.fixture
def dataframe():
    return pd.DataFrame({"x": list(range(0, 50)), "y": list(range(50, 100)),})


@pytest.fixture
def app():
    return PandasProfilingApp()


def test_can_be_constructed():
    PandasProfilingApp()


def test_has_title(app):
    assert isinstance(app.title, str)

def test_has_csv_url(app):
    assert isinstance(app.csv_url, str)
    assert app.csv_url

def test_can_be_viewed(app):
    assert app.view


@pytest.mark.skip("slow")
@pytest.mark.integrationtest
def test_can_load_data_from_url(app, csv_url):
    # Given
    app.dataframe = None
    # When
    app.csv_url = csv_url
    app.update_report()
    # Then
    assert isinstance(app.dataframe, pd.DataFrame)
    assert not app.dataframe.empty

@pytest.mark.skip("slow")
@pytest.mark.integrationtest
def test_can_load_random_report(app):
    # Given
    app.dataframe = None
    app.csv_url = ""
    app.report = None
    app.html_report = ""
    # When
    app.random_report()
    # Then
    assert isinstance(app.dataframe, pd.DataFrame)
    assert not app.dataframe.empty
    assert app.report
    assert app.html_report



