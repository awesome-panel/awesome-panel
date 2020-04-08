"""Test of the gallery functionality"""
import panel as pn

import awesome_panel.express as pnx
from awesome_panel.database.apps_in_gallery import APPS_IN_GALLERY
from awesome_panel.express.testing import TestApp
from src.pages import gallery

pnx.fontawesome.extend()


def test_gallery_button():
    """Test of the Gallery Button"""

    app = pn.Column(name="app", sizing_mode="stretch_width",)

    gallery_button = gallery.GalleryButton(APPS_IN_GALLERY[0], app,)
    app[:] = [gallery_button]
    return TestApp(test_gallery_button, app,)


def view() -> pn.Column:
    """A Column of a tests"""
    return pn.Column(test_gallery_button(), sizing_mode="stretch_width",)


if __name__.startswith("bokeh"):
    view().servable()
