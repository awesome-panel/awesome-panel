import panel as pn
import pathlib
from awesome_panel.models import Application
import param

ROOT_PATH = pathlib.Path(__file__).parent
HTML_PATH = ROOT_PATH / "material.html"
CSS_PATH = ROOT_PATH / "material.css"
DEFAULT_NAME = "Material"

THEME_CSS = """
<style>
:root {
    --mdc-theme-primary: green;
    --mdc-theme-on-primary: white;
    --mdc-theme-secondary: purple;
    --mdc-theme-on-secondary: white;
    --mdc-theme-background: #121212;
}
mwc-drawer {
    color: white;
    background: var(--mdc-theme-background);
}
</style>
"""

class MaterialTemplate(pn.Template):
    application = param.ClassSelector(class_=Application)

    def __init__(self, **params):
        if not "template" in params:
            params["template"]=HTML_PATH.read_text()
        if not "name" in params:
            params["name"]=DEFAULT_NAME

        super().__init__(**params)

        pn.config.css_files.append(CSS_PATH.resolve())

        menu_item = pn.Param(self.application.param.menu_item)
        self.main = pn.Column(
            self.application.page.view(),
            sizing_mode="stretch_both",
        )
        self.theme_css = pn.pane.HTML(THEME_CSS, height=0, width=0, sizing_mode="fixed", margin=0)
        self.app_title_pane = pn.pane.HTML(self._get_app_title())
        self.add_panel(name="menu_item", panel=menu_item)
        self.add_panel(name="main", panel=self.main)
        self.add_panel(name="app_title", panel=self.app_title_pane)
        self.add_panel(name="theme_css", panel=self.theme_css)

    @param.depends("application.title", "application.url", watch=True)
    def _set_app_title_pane(self):
        self.app_title_pane.object = self._get_app_title()

    def _get_app_title(self):
        return f"<a href='{self.application.url}'><h1>{self.application.title}</h1></a>"



