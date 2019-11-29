"""An App Template based on Bootstrap with a header, sidebar and main section"""
import pathlib

import panel as pn

CSS_URL = pathlib.Path(__file__).parent / "_bootstrap_dashboard.css"
CSS_MARKER = "<!-- _boostrap_dashboard.css -->"
TEMPLATE_URL = pathlib.Path(__file__).parent / "_bootstrap_dashboard.html"


class BootStrapDashboardTemplate(pn.Template):
    """An App Template based on Bootstrap with a header, sidebar and main section"""

    def __init__(self, app_title: str = "App Name"):
        template = TEMPLATE_URL.read_text()
        css = CSS_URL.read_text()
        template = template.replace(CSS_MARKER, "<style>" + css + "</style>")

        self.sidebar = pn.Column()
        self.main = pn.Column(sizing_mode="stretch_width")

        items = {
            "sidebar": self.sidebar,
            "main": self.main,
            "app_title": pn.Row(pn.layout.HSpacer(), pn.pane.HTML(app_title), pn.layout.HSpacer()),
        }
        super().__init__(template=template, items=items)
