"""This module contains a navigation menu to be used to select between different pages"""
from typing import List
import panel as pn
import param


class Navigator(param.Parameterized):
    """## Navigation Widget

    Can be used to select/ navigate between pages"""

    _selected_page = param.ObjectSelector()

    def __init__(self, pages, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pages = pages
        self.params()["_selected_page"].objects = pages
        self._selected_page = pages[0]

    def menu(self) -> pn.Pane:
        """The Menu

        Add this to a sidebar

        Returns:
            pn.Pane -- A Menu Pane
        """

        def set_selected_page(event):
            self._selected_page = [page for page in self.pages if page.name == event.obj.name][0]

        menuitems = []
        for page in self.pages:
            button = pn.widgets.Button(name=page.name)
            button.on_click(set_selected_page)
            menuitems.append(button)

        return pn.WidgetBox(
            *menuitems, sizing_mode="stretch_width", css_classes=["select-selected_page-page"]
        )

    @param.depends("_selected_page")
    def selected_page(self) -> pn.Column:
        """The selected page

        Returns:
            pn.Column -- The selected page wrapped in a Column
        """
        # Hack: For some reason returning self._selected_page does not work
        # When all pages have been shown once then the page shown stops changing
        return pn.Column(self._selected_page, sizing_mode="stretch_width")
