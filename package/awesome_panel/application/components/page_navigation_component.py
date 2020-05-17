"""This module implements the PageNavigationComponent"""
import panel as pn
import param

from awesome_panel.application.models import Application
from awesome_panel.application.services import PageService


class PageNavigationComponent(pn.Row):
    """The PageNavigationComponent enables the user to select and navigate to
    - any page
    - the default page
    """

    def __init__(self, application: Application, page_service: PageService, **params):
        super().__init__(self, **params)

        with param.edit_constant(self):
            self.application = application
            self.page_service = page_service

        self[:] = self._get_view_objects()

    def _get_view_objects(self):
        load_default_page_pane = pn.Param(
            self.page_service,
            parameters=["load_default_page"],
            widgets={
                "load_default_page": {"type": pn.widgets.Button, "name": self.application.title}
            },
            show_name=False,
            show_labels=False,
            sizing_mode="stretch_width",
        )
        seperator_pane = pn.pane.Markdown("/", sizing_mode="fixed", width=5)

        page_pane = pn.Param(
            self.page_service,
            parameters=["page"],
            expand_button=False,
            show_name=False,
            show_labels=False,
            sizing_mode="stretch_width",
        )

        return [
            load_default_page_pane,
            seperator_pane,
            page_pane,
        ]
