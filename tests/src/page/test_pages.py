"""Test of the pages"""
import pytest
from panel.layout import Column

import awesome_panel.express as pnx
from awesome_panel.express.testing import TestApp
from src.pages import gallery, home, resources

pnx.bootstrap.extend()


@pytest.mark.panel
def test_home():
    """Test that we can see the home page

    """
    return TestApp(test_home, home.view())


@pytest.mark.panel
def test_resources():
    """Test that we can see the resources page

    """
    return TestApp(test_resources, resources.view())


@pytest.mark.panel
def test_gallery():
    """Test that we can see the gallery page

    """
    page_outlet = Column()
    page = gallery.Gallery(page_outlet=page_outlet).view()
    page_outlet[:] = [page]
    return TestApp(test_gallery, page_outlet)


if __name__.startswith("bk"):
    test_home().servable()
    test_resources().servable()
    test_gallery().servable()
