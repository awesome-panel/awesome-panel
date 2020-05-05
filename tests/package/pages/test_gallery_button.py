"""Test of the gallery functionality"""
import panel as pn
import pytest

import awesome_panel.express as pnx
from application.pages.gallery import gallery
from awesome_panel.express.testing import TestApp

pnx.fontawesome.extend()


@pytest.mark.xfail
def test_gallery_button(page):
    """Test of the Gallery Button"""

    app = pn.Column(name="app", sizing_mode="stretch_width",)

    gallery_button = gallery.GalleryButton(page, app,)
    app[:] = [gallery_button]
    return TestApp(test_gallery_button, app,)
