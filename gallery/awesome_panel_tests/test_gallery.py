"""Test of the gallery functionality"""
import panel as pn

import awesome_panel.express as pnx
from awesome_panel.express.testing import TestApp
from src.pages import gallery


def test_gallery_button():
    app = pn.Column(name="app", width=400, height=400)

    def page():
        return pn.Column("Test Page", name="Test Page")

    gallery_button = gallery.GalleryButton("test", page, app)
    app[:] = [gallery_button]
    return app


def view() -> pn.Column:
    """A Column of a tests"""
    return pn.Column(test_gallery_button(),)


if __name__.startswith("bk"):
    view().servable()
