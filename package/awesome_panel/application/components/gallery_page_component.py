"""In this module we define the GalleryPageComponent"""
import panel as pn
import param

from awesome_panel.application.models import Page
from awesome_panel.application.services import PageService
from awesome_panel.application.views.gallery_page_view import GalleryPageView


class GalleryPageComponent(param.Parameterized):
    """The GalleryPageComponent shows thumbnail of the page and enables the user to navigate to
    the page"""

    page = param.ClassSelector(class_=Page, constant=True)
    page_service = param.ClassSelector(class_=PageService, constant=True)

    view = param.ClassSelector(class_=pn.Column)

    def __init__(self, page, **params):
        params["view"] = GalleryPageView(page=page)
        params["page"] = page
        if "page_service" not in params:
            params["page_service"] = PageService()

        super().__init__(**params)

    @param.depends("view.clicks", watch=True)
    def _load_page(self, _=None):
        self.page_service.page = self.page
        print(self.page.name)
