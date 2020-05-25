"""
A module containing testing utilities and fixtures.
"""
# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
from __future__ import absolute_import, division, unicode_literals

import pandas as pd
import pytest
from bokeh.document import Document
from pyviz_comms import Comm


@pytest.fixture
def document():
    return Document()


@pytest.fixture
def comm():
    return Comm()


@pytest.fixture
def dataframe():
    return pd.DataFrame(
        {"int": [1, 2, 3], "float": [3.14, 6.28, 9.42], "str": ["A", "B", "C"]},
        index=[1, 2, 3],
        columns=["int", "float", "str"],
    )
