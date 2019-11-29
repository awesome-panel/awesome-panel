"""An App Template based on Bootstrap with a header, sidebar and main section"""
import pathlib

import panel as pn

CSS_URL = pathlib.Path(__file__).parent / "_basic.css"
CSS_MARKER = "<!-- _basic.css -->"
TEMPLATE_URL = pathlib.Path(__file__).parent / "_basic.html"


class BasicTemplate(pn.Template):
    """A Basic App Template"""

    def __init__(self, app_title: str = "App Name"):
        template = TEMPLATE_URL.read_text()
        css = CSS_URL.read_text()
        template = template.replace(CSS_MARKER, "<style>" + css + "</style>")

        left_header = pn.Row(app_title, height=48, css_classes=["left_header"])
        right_header = pn.layout.Row(
            pn.layout.HSpacer(),
            sizing_policy="stretch_width",
            height=48,
            css_classes=["right_header"],
        )
        self.sidebar = pn.Column(
            background="yellow", css_classes=["sidebar"], sizing_policy="stretch_both"
        )
        self.main = pn.Column(css_classes=["main"])

        left_column = pn.Column(
            left_header, self.sidebar, background="lightblue", css_classes=["left-column"]
        )
        right_column = pn.Column(
            right_header,
            self.main,
            background="blue",
            width_policy="max",
            css_classes=["right-column"],
        )

        app = pn.Row(left_column, right_column)

        items = {
            "app": app,
        }
        super().__init__(template=template, items=items)
