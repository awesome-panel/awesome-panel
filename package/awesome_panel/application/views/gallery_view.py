"""In this module we implement the GalleryView

The GalleryView display the pages in a columnar view and enables the user to navigate to a page.
"""
import panel as pn


class GalleryView(pn.layout.GridBox):
    """The GalleryView display the pages in a columnar view and enables the user to navigate to a
    page."""

    def __init__(self, gallery_page_views, ncols=2, **params):
        gallery_page_views = [self._update_gallery_page_view(view) for view in gallery_page_views]

        params["ncols"] = ncols
        super().__init__(*gallery_page_views, **params)

    @staticmethod
    def _update_gallery_page_view(gallery_page_view):
        gallery_page_view.margin = 20
        return gallery_page_view
