from awesome_panel.models import Application as ApplicationModel
from .component import Component
import panel as pn

class Application(ApplicationModel, Component):
    def _settings_pane(self):
        return pn.Param(
            self, parameters=[
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

        return self.template(application=self)
