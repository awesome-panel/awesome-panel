import param
import panel as pn
from awesome_panel.models import Application
import pathlib


class ApplicationTemplate(pn.Template):
    application = param.ClassSelector(class_=Application)
    template_path = param.ClassSelector(class_=pathlib.Path)
    css_path = param.ClassSelector(class_=pathlib.Path)

    def __init__(self, **params):
        params["template"] = params["template_path"].read_text()

        super().__init__(**params)

        if self.css_path:
            pn.config.css_files.append(self.css_path.resolve())

        self.menu = pn.Param(self.application.param.menu_item)
        self.sidebar = pn.Column()
        self.main = pn.Column(self.application.page.view, sizing_mode="stretch_both",)
        self.theme_css = pn.pane.HTML(height=0, width=0, sizing_mode="fixed", margin=0)
        self.add_panel(name="menu_item", panel=self.menu)
        self.add_panel(name="main", panel=self.main)
        self.add_panel(name="theme_css", panel=self.theme_css)

    @param.depends("application.title", "application.url", watch=True)
    def _set_app_title_pane(self):
        self.app_title_pane.object = self._get_app_title()

    def _get_app_title(self):
        return f"<a href='{self.application.url}'><h1>{self.application.title}</h1></a>"

    @param.depends("application.page", watch=True)
    def _set_main_objects(self):
        self.main[:] = [self.application.page.view]
