"""This module contains a CRUD Service for Pages"""
from typing import List, Optional

import param

from awesome_panel.application.models import Page


class PageService(param.Parameterized):
    """A CRUD Service for Pages

    Notes:

    - The pages list is kept sorted.
    - DON'T change the pages list manually. Use the functions of the service

    """

    pages = param.List(constant=True)
    page = param.ObjectSelector(allow_None=False, doc="The currently active page")
    default_page = param.ClassSelector(class_=Page, constant=True)
    load_default_page = param.Action()

    def __init__(self, **params):
        if "default_page" not in params:
            if "pages" in params and params["pages"]:
                params["default_page"] = params["pages"][0]

        super().__init__(**params)

        self._pages = {page.name: page for page in self.pages}
        self.load_default_page = self._load_default_page

    def create(self, page: Page):
        """Creates the specified Page

        Args:
            page (Page): A Page to create
        """
        self._pages[page.name] = page
        self._update_pages_list()

    def read(self, name: str) -> Optional[Page]:
        """Returns the Page with the given name

        Args:
            name (str): The name of the Page to return

        Returns:
            Optional[Page]: The Page with the given name if it exists. Otherwise None
        """
        if name in self._pages:
            return self._pages[name]
        return None

    def update(self, page: Page):
        """Updates the given page

        Args:
            page (Page): A Page to update
        """
        self.create(page)

    def delete(self, page: Page):
        """Deletes the given page

        Args:
            page (Page): [description]
        """
        if page.name in self._pages:
            self._pages = {key: value for key, value in self._pages.items() if key != page.name}
            self._update_pages_list()

    def _update_pages_list(self):
        with param.edit_constant(self):
            self.pages = sorted(list(self._pages.values()))

    def bulk_create(self, pages: List[Page]):
        """Creates the list of pages

        Args:
            pages (List[Page]): A list of Pages to create
        """
        old_pages = self._pages
        new_pages = {page.name: page for page in pages}
        self._pages = {**old_pages, **new_pages}
        self._update_pages_list()

    def set_default_page(self, page: Page):
        """Change the default_page to the specified page

        Args:
            page (Page): The new default_page
        """
        if not page in self.pages:
            self.create(page)
        with param.edit_constant(self):
            self.default_page = page

    def reset(self):
        """Resets to the defaults"""
        self.pages = []
        self.default_page = self.param.default_page.default

    def _load_default_page(self, _=None):
        self.page = self.default_page
