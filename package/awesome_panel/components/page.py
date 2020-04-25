from .component import Component
from awesome_panel.models.page import Page as PageModel
import panel as pn

class Page(PageModel, Component):
    def view(self, **params):
        return pn.Column(
            self.param.name,
            **params
        )