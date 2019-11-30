"""An App Template based on Bootstrap with a header, sidebar and main section"""
import pathlib

import panel as pn

CSS_URL = pathlib.Path(__file__).parent / "_basic.css"
CSS_MARKER = "<!-- _basic.css -->"
TEMPLATE_URL = pathlib.Path(__file__).parent / "_basic.html"

HEADER_HEIGHT = 58
SIDEBAR_WIDTH = 300


class BasicTemplate(pn.Template):
    """A Basic App Template"""

    def __init__(self, app_title: str = "App Name"):
        template = TEMPLATE_URL.read_text()
        css = CSS_URL.read_text()
        template = template.replace(CSS_MARKER, "<style>" + css + "</style>")

        app_title = pn.Row(
            "### " + app_title, width=SIDEBAR_WIDTH, height_policy="max", css_classes=["app-title"],
        )
        header = pn.Row(
            app_title,
            pn.layout.HSpacer(),
            css_classes=["header"],
            sizing_mode="stretch_width",
            height=HEADER_HEIGHT,
        )
        top_spacer = pn.layout.HSpacer(height=15)
        self.sidebar = pn.Column(top_spacer, css_classes=["sidebar"], height_policy="max", width=SIDEBAR_WIDTH)
        self.main = pn.Column(css_classes=["main"], width_policy="max", height_policy="max", margin=(0, 50, 0, 25))

        app = pn.Column(
            header,
            pn.Row(
                self.sidebar,
                self.main, css_classes=["mid"]),
            sizing_mode="stretch_width",
        )

        items = {
            "app": app,
        }
        super().__init__(template=template, items=items)
