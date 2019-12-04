"""This module contains a navigation menu to be used to select between different pages"""
from typing import List, Union

import panel as pn
import param

import awesome_panel.express as pnx


class Navigator(param.Parameterized):
    """## Navigation Object

    Can be used to control navigation between pages
    """

    page = param.ObjectSelector()

    def __init__(
        self,
        pages: List[Union[pn.layout.Panel, pn.pane.Pane]],
        page_outlet: pn.layout.ListPanel,
        *args,
        **kwargs
    ):
        """## Navigation Object

        Can be used to control navigation between pages

        Arguments:
            pages {List[Union[pn.layout.Panel, pn.pane.Pane]]} -- A list of 'pages' to navigate
                between
            page_outlet {pn.layout.ListPanel} -- The ListPanel to update when the user navigates to
                a new page
        """
        super().__init__(*args, **kwargs)
        self.pages = pages
        self.page_outlet = page_outlet
        self.params()["page"].objects = pages
        self.page = pages[0]
        self._update_page_outlet()

    def _update_page_outlet(self):
        """Changes the page_outlet_objects to the selected page"""
        self.page_outlet.clear()
        self.page_outlet.append(self.page)

    def menu(self) -> pn.WidgetBox:
        """## A Menu Widget enabling the user to navigate between pages

        Add this to a sidebar

        Returns:
            pn.WidgetBox -- A Vertical Menu
        """

        def set_page(event):
            self.page = [page for page in self.pages if page.name == event.obj.name][0]
            self._update_page_outlet()

        menuitems = []
        for page in self.pages:
            button = pn.widgets.Button(name=page.name)
            button.on_click(set_page)
            menuitems.append(button)

        title = pnx.SubHeader("Navigation", text_align="center")
        return pn.Column(title, *menuitems, sizing_mode="stretch_width")
