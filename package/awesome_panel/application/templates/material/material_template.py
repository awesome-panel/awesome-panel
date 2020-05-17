"""This module implements an ApplicationTemplate based on Material and the mwc-components"""
import pathlib

import panel as pn
import param

from awesome_panel.application.templates.application_template import ApplicationTemplate
from awesome_panel.utils import holoviews_ext

ROOT_PATH = pathlib.Path(__file__).parent
HTML_PATH = ROOT_PATH / "material_template.html"
CSS_PATH = ROOT_PATH / "material_template.css"
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


class MaterialTemplate(ApplicationTemplate):
    """An ApplicationTemplate based on Material design and the mwc web components
    """

    def __init__(self, **params):
        params["template_path"] = HTML_PATH
        params["css_path"] = CSS_PATH
        super().__init__(**params)

        holoviews_ext.disable_bokeh_logo()

        self.app_title_link_pane = pn.Param(
            self,
            parameters=["select_title_page"],
            show_name=False,
            show_labels=False,
            sizing_mode="fixed",
        )
        self.app_title_page_pane = pn.Param(
            self.services.page_service.param.page,
            expand_button=False,
            show_labels=False,
            sizing_mode="fixed",
        )
        self.app_title_pane = pn.Row(
            self.app_title_link_pane,
            pn.pane.Markdown("/", sizing_mode="fixed", width=5),
            self.app_title_page_pane,
            sizing_mode="fixed",
        )

        self.add_panel(name="app_title", panel=self.app_title_pane)

    @param.depends("application.title", "application.url", watch=True)
    def _set_app_title_link_pane(self):
        self.app_title_link_pane.object = self._get_app_title()

    def _get_app_title(self):
        return (
            f"<h1 id='top-app-bar-title'><a href='{self.application.url}'>"
            f"{self.application.title}</a> &sol;</h1>"
        )
