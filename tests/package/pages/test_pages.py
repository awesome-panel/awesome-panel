"""Test of the pages"""
import awesome_panel.express as pnx
import pytest
from awesome_panel.express.testing import TestApp

from application.pages import home

pnx.bootstrap.extend()


@pytest.mark.panel
def test_home():
    """Test that we can see the home page"""
    return TestApp(
        test_home,
        home.view(),
    )


if __name__.startswith("bokeh"):
    test_home().servable()
