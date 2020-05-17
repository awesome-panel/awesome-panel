"""In this module we implement the GalleryComponent

The GalleryComponent enables the user to view the pages in a columnar format and navigate to one.
"""
import param

from awesome_panel.application.components import PageComponent
from awesome_panel.application.components.gallery_page_component import GalleryPageComponent
from awesome_panel.application.views.gallery_view import GalleryView


class GalleryComponent(PageComponent):
    """The GalleryComponent enables the user to view the pages in a columnar format and navigate to
    one."""

    pages = param.List()
    view = param.ClassSelector(class_=GalleryView)

    def __init__(self, pages, **params):
        params["pages"] = pages
        gallery_page_views = self._create_gallery_page_views(pages=pages)
        params["main"] = GalleryView(gallery_page_views=gallery_page_views)
        params["view"] = params["main"]
        super().__init__(**params)

    @staticmethod
    def _create_gallery_page_views(pages):
        gallery_page_views = []
        for page in pages:
            component = GalleryPageComponent(page=page)
            view = component.view
            gallery_page_views.append(view)
        return gallery_page_views
