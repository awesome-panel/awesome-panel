"""An App Template based on Bootstrap with a header, sidebar and main section"""
import pathlib

import panel as pn

import awesome_panel.express as pnx
from awesome_panel.express.assets import SCROLLBAR_PANEL_EXPRESS_CSS

BOOTSTRAP_DASHBOARD_CSS = pathlib.Path(__file__).parent / "bootstrap_dashboard.css"
BOOTSTRAP_DASHBOARD_TEMPLATE = pathlib.Path(__file__).parent / "bootstrap_dashboard.html"

HEADER_HEIGHT = 58
SIDEBAR_WIDTH = 200

# Hack to make dynamically adding plotly work:
# See https://github.com/holoviz/panel/issues/840
pn.extension("plotly")


class BootstrapDashboardTemplate(pn.Template):
    """A Basic App Template"""

    def __init__(
        self,
        app_title: str = "App Name",
        app_url="#",
    ):
        pn.config.raw_css.append(BOOTSTRAP_DASHBOARD_CSS.read_text())
        pn.config.raw_css.append(SCROLLBAR_PANEL_EXPRESS_CSS.read_text())
        pnx.bootstrap.extend()
        pnx.fontawesome.extend()
        template = BOOTSTRAP_DASHBOARD_TEMPLATE.read_text()

        app_title = pn.Row(
            pn.pane.Markdown(
                f"[{app_title}]({app_url})",
                css_classes=["app-title"],
            ),
            width=SIDEBAR_WIDTH,
            sizing_mode="stretch_height",
        )
        header = pn.Row(
            app_title,
            pn.layout.HSpacer(),
            sizing_mode="stretch_width",
            height=HEADER_HEIGHT,
        )
        top_spacer = pn.layout.HSpacer(height=15)
        self.header = header
        self.sidebar = pn.Column(
            top_spacer,
            height_policy="max",
            width=SIDEBAR_WIDTH,
        )
        self.main = pn.Column(
            sizing_mode="stretch_width",
            margin=(
                25,
                50,
                25,
                50,
            ),
        )

        items = {
            "header": header,
            "sidebar": self.sidebar,
            "main": self.main,
        }
        super().__init__(
            template=template,
            items=items,
        )
