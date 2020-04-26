import inspect

import panel as pn
import param

from .component import Component


class PageComponent(Component):
    page = param.Parameter()

    def __init__(self, name, page, **params):
        params["name"]=name
        params["page"]=page
        super().__init__(**params)

        self._view = None

    def view(self, **params):
        if not self._view:
            page = self.page
            self._view = self._to_view(page)

        return self._view

    @staticmethod
    def _to_view(page):
        if inspect.isclass(page):
                page = page()

        if callable(page):
            return page()
        if hasattr(page, "view"):
            if callable(page.view):
                return page.view()
            return page.view
        return page
