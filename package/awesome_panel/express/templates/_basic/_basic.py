"""An App Template based on Bootstrap with a header, sidebar and main section"""
import pathlib

import panel as pn

CSS_URL = pathlib.Path(__file__).parent / "_basic.css"
CSS_MARKER = "<!-- _basic.css -->"
TEMPLATE_URL = pathlib.Path(__file__).parent / "_basic.html"

HEADER_HEIGHT = 48


class BasicTemplate(pn.Template):
    """A Basic App Template"""

    def __init__(self, app_title: str = "App Name"):
        template = TEMPLATE_URL.read_text()
        css = CSS_URL.read_text()
        template = template.replace(CSS_MARKER, "<style>" + css + "</style>")

        left_header = pn.Row(
            pn.layout.HSpacer(),
            app_title,
            pn.layout.HSpacer(),
            css_classes=["left-header"],
            height=HEADER_HEIGHT,
        )
        right_header = pn.Row(
            pn.layout.HSpacer(),
            css_classes=["right-header"],
            height=HEADER_HEIGHT,
        )
        self.sidebar = pn.Column(css_classes=["sidebar"], height_policy="max")
        self.main = pn.Column(css_classes=["main"], width_policy="max", margin=(10, 10, 25, 25))

        left_column = pn.Column(
            left_header, self.sidebar, height_policy="max", css_classes=["left-column"]
        )
        right_column = pn.Column(
            right_header, self.main, width_policy="max", css_classes=["right-column"],
        )

        app = pn.Row(left_column, right_column, css_classes=["app"])

        items = {
            "app": app,
        }
        super().__init__(template=template, items=items)
