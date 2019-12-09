"""Test of the pages"""
import pytest
from panel.layout import Column

from src.pages import home, resources
from awesome_panel.express import bootstrap

bootstrap.extend()


@pytest.mark.panel
def test_home():
    """Test that we can see the home page

    """
    Column(home.view(), sizing_mode="stretch_width").servable()


@pytest.mark.panel
def test_resources():
    """Test that we can see the resources page

    """
    Column(resources.view(), sizing_mode="stretch_width").servable()


if __name__.startswith("bk"):
    test_home()
    test_resources()
