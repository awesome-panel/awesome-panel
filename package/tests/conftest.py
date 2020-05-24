"""
A module containing testing utilities and fixtures.
"""
# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
from __future__ import absolute_import, division, unicode_literals

import os
import re
import shutil

import pytest

from contextlib import contextmanager

from bokeh.document import Document
from bokeh.client import pull_session
from pyviz_comms import Comm

from panel.pane import HTML, Markdown
from panel.io import state


@pytest.fixture
def document():
    return Document()


@pytest.fixture
def comm():
    return Comm()


@pytest.fixture
def dataframe():
    import pandas as pd
    return pd.DataFrame({
        'int': [1, 2, 3],
        'float': [3.14, 6.28, 9.42],
        'str': ['A', 'B', 'C']
    }, index=[1, 2, 3], columns=['int', 'float', 'str'])