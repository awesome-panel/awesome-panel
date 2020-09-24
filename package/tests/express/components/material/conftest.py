# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
import pytest
from awesome_panel.express.components import material


@pytest.fixture
def mwc_select():
    return material.MWCSelect(name="Select Me", options=["a", "b", "c"])
