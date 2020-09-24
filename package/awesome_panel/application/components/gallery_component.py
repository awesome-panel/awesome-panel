"""In this module we implement the GalleryComponent

The GalleryComponent enables the user to view the pages in a columnar format and navigate to one.
"""
import param
from awesome_panel.application.components.gallery_page_component import GalleryPageComponent
from awesome_panel.application.components.page_component import PageComponent
from awesome_panel.application.models import Page
from awesome_panel.application.services import PageService
from awesome_panel.application.views.gallery_view import GalleryView


class GalleryComponent(PageComponent):
    """The GalleryComponent enables the user to view the pages in a columnar format and navigate to
    one."""

    pages = param.List()
    page_service = param.ClassSelector(class_=PageService, constant=True)
    view = param.ClassSelector(class_=GalleryView)

    def __init__(self, pages, page_service, **params):
        params["pages"] = pages
        params["page_service"] = page_service
        gallery_page_views = self._create_gallery_page_views(pages=pages, page_service=page_service)
        params["main"] = GalleryView(gallery_page_views=gallery_page_views)
        params["view"] = params["main"]
        super().__init__(**params)

    @staticmethod
    def _create_gallery_page_views(pages, page_service):
        gallery_page_views = []
        for page in pages:
            component = GalleryPageComponent(page=page, page_service=page_service)
            view = component.view
            gallery_page_views.append(view)
        return gallery_page_views

    @classmethod
    def _create_view_func(cls, pages, page_service):
        def view_func():
            return cls(pages=pages, page_service=page_service).view

        return view_func

    @classmethod
    def create_gallery_component(cls, pages, page_service):
        """Method use to create a new GalleryComponent for an application"""
        return Page(
            name="Gallery",
            show_loading_page=True,
            component=cls._create_view_func(pages=pages, page_service=page_service),
        )
