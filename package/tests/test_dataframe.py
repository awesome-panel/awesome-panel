"""Tests of the dataframe module"""
import pandas as pd
from bokeh.models.widgets.tables import NumberFormatter

from awesome_panel.express.widgets import dataframe


def test_get_default_formatters():
    """We test that formatters for int, float and str are as expected"""
    # Given
    data = pd.DataFrame(
        {"int": [1, 2, 3000], "float": [3.14, 6.28, 9000.42], "str": ["A", "B", "C"]},
        index=[1, 2, 3],
    )
    assert not data.index.name
    # When
    actual = dataframe.get_default_formatters(data)
    # Then
    print(actual)
    assert isinstance(actual["int"], NumberFormatter)
    assert actual["int"].format == dataframe.INT_FORMAT
    assert actual["int"].text_align == dataframe.INT_ALIGN
    assert isinstance(actual["float"], NumberFormatter)
    assert actual["float"].format == dataframe.FLOAT_FORMAT
    assert actual["float"].text_align == dataframe.FLOAT_ALIGN
    assert "str" not in actual
    assert data.index.name == "index"
    assert actual["index"].format == dataframe.INT_FORMAT
    assert actual["index"].text_align == dataframe.INT_ALIGN


def test_get_default_formatters_multi_level_index():
    """We test that formatters for int, float and str are as expected"""
    # Given
    data = pd.DataFrame(
        {"int": [1, 2, 3000], "float": [3.14, 6.28, 9000.42], "str": ["A", "B", "C"]},
    )
    data = data.set_index(["int", "float"])
    # When
    actual = dataframe.get_default_formatters(data)
    # Then
    print(actual)
    assert isinstance(actual["int"], NumberFormatter)
    assert actual["int"].format == dataframe.INT_FORMAT
    assert actual["int"].text_align == dataframe.INT_ALIGN
    assert isinstance(actual["float"], NumberFormatter)
    assert actual["float"].format == dataframe.FLOAT_FORMAT
    assert actual["float"].text_align == dataframe.FLOAT_ALIGN
    assert "str" not in actual
