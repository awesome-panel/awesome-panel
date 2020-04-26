from awesome_panel.models import Application
from .component import Component
import panel as pn
import param

class ApplicationComponent(Component):
    model = param.ClassSelector(class_=Application)

    def __init__(self, **params):
        super().__init__(**params)

        self.menu = pn.Column()
        self.sidebar = pn.Column()
        self.main = pn.Column()
        self.theme_css = pn.pane.HTML()

    def _settings_pane(self):
        return pn.Param(
            self.model, parameters=[
                "template",
                "theme",
                "title",
                "logo",
                "url",
                "page",
                "menu_item",
                "source_link",
                "social_link",
                "progress",
                "message",
            ],
            sizing_mode="stretch_height",
            width=300,
            background="lightgray",
            expand_button=None,
        )

    def view(self, sizing_mode="stretch_width", **params):
        pn.config.sizing_mode = sizing_mode
        return self.model.template(application=self)
