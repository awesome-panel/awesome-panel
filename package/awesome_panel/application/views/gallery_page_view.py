"""In this module we define the GalleryPageView

The GalleryPageView shows (a thumbnail of) the page and enables the user to navigate to it.
"""
import panel as pn
import param
from awesome_panel.application.models import Page


class GalleryPageView(pn.Column):
    """The GalleryPageView shows (a thumbnail of) the page and enables the user to navigate to
    it."""

    clicks = param.Integer()

    def __init__(self, page: Page, **params):
        self._rename["clicks"] = None
        params["name"] = "gallery-item-" + page.name
        params["sizing_mode"] = "fixed"
        params["width"] = 400
        params["height"] = 332
        super().__init__(**params)

        show_button = pn.widgets.Button(
            name=page.name.upper(), button_type="primary", margin=0, sizing_mode="stretch_width"
        )
        show_button.on_click(self._increment_click)
        thumbnail_pane = pn.pane.PNG(
            page.thumbnail_png_url,
            alt_text=page.description,
            margin=0,
            sizing_mode="fixed",
            width=400,
            height=300,
            embed=False,
        )

        self[:] = [
            thumbnail_pane,
            show_button,
        ]

    def _increment_click(self, _=None):
        self.clicks += 1
