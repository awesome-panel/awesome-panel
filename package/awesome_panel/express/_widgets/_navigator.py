"""This module contains a navigation menu to be used to select between different pages"""
import param

import panel as pn


class Navigator(param.Parameterized):
    """## Navigation Widget

    Can be used to select/ navigate between pages"""

    page = param.ObjectSelector()

    def __init__(self, pages, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pages = pages
        self.params()["page"].objects = pages
        self.page = pages[0]

    def menu(self) -> pn.WidgetBox:
        """The Menu

        Add this to a sidebar

        Returns:
            pn.WidgetBox -- A Vertical Menu
        """

        def setpage(event):
            self.page = [page for page in self.pages if page.name == event.obj.name][0]

        menuitems = []
        for page in self.pages:
            button = pn.widgets.Button(name=page.name)
            button.on_click(setpage)
            menuitems.append(button)

        return pn.Column(*menuitems, width=300)

    @param.depends("page")
    def selected_page(self) -> pn.Column:
        """The selected page

        Returns:
            pn.Column -- The selected page wrapped in a Column
        """
        # Hack: For some reason returning self.page does not work
        # When all pages have been shown once then the page shown stops changing
        return pn.Column(self.page, sizing_mode="stretch_width")
