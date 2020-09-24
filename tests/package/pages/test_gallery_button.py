"""Test of the gallery functionality"""
import awesome_panel.express as pnx
import panel as pn
import pytest
from awesome_panel.express.testing import TestApp

from application.pages.gallery import gallery

pnx.fontawesome.extend()


@pytest.mark.xfail
def test_gallery_button(page):
    """Test of the Gallery Button"""

    app = pn.Column(
        name="app",
        sizing_mode="stretch_width",
    )

    gallery_button = gallery.GalleryButton(
        page,
        app,
    )
    app[:] = [gallery_button]
    return TestApp(
        test_gallery_button,
        app,
    )
