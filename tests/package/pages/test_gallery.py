"""Test of the gallery page"""
import awesome_panel.express as pnx
import pytest
from awesome_panel.application.services import PageService
from awesome_panel.express.testing import TestApp
from panel.layout import Column

from application.pages.gallery import gallery

pnx.bootstrap.extend()
pnx.fontawesome.extend()
APPS_IN_GALLERY = PageService.pages


@pytest.mark.panel
def test_gallery():
    """Test that we can see the gallery page"""
    page_outlet = Column(sizing_mode="stretch_width")
    page = gallery.Gallery(
        page_outlet=page_outlet,
        apps_in_gallery=APPS_IN_GALLERY,
    ).view()
    page_outlet[:] = [page]
    return TestApp(
        test_gallery,
        page_outlet,
    )


if __name__.startswith("bokeh"):
    test_gallery().servable()
