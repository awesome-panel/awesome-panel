from .component import Component
from awesome_panel.models.page import Page
import panel as pn
import param

class PageComponent(Component):
    model = param.ClassSelector(class_=Page)

    def view(self, **params):
        return pn.Column(
            self.model.param.name,
            **params
        )