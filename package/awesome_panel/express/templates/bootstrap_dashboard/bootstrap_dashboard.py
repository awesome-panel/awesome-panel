"""An App Template based on Bootstrap with a header, sidebar and main section"""
import pathlib

import panel as pn
from awesome_panel.express._pane._headings import SubHeader
from awesome_panel.express.assets import CODE_HILITE_CSS, BOOTSTRAP_CSS, SCROLLBAR_CSS

BOOTSTRAP_DASHBOARD_CSS = pathlib.Path(__file__).parent / "bootstrap_dashboard.css"
BOOTSTRAP_DASHBOARD_TEMPLATE = pathlib.Path(__file__).parent / "bootstrap_dashboard.html"

HEADER_HEIGHT = 58
SIDEBAR_WIDTH = 200

# Hack to make dynamically adding plotly work:
# See https://github.com/holoviz/panel/issues/840
pn.extension("plotly")

class BootstrapDashboardTemplate(pn.Template):
    """A Basic App Template"""

    def __init__(self, app_title: str = "App Name", app_url="#"):
        pn.config.raw_css.append(CODE_HILITE_CSS.read_text())
        pn.config.raw_css.append(BOOTSTRAP_CSS.read_text())
        pn.config.raw_css.append(BOOTSTRAP_DASHBOARD_CSS.read_text())
        pn.config.raw_css.append(SCROLLBAR_CSS.read_text())
        template = BOOTSTRAP_DASHBOARD_TEMPLATE.read_text()

        app_title = pn.Row(
            pn.layout.HSpacer(),
            pn.pane.Markdown(f"[{app_title}]({app_url})", css_classes=["app-title"],),
            pn.layout.HSpacer(),
            width=SIDEBAR_WIDTH,
        )
        header = pn.Row(
            app_title,
            pn.layout.HSpacer(),
            css_classes=["header"],
            sizing_mode="stretch_width",
            height=HEADER_HEIGHT,
        )
        top_spacer = pn.layout.HSpacer(height=15)
        self.sidebar = pn.Column(
            top_spacer, css_classes=["sidebar"], height_policy="max", width=SIDEBAR_WIDTH
        )
        self.main = pn.Column(
            css_classes=["main"], sizing_mode="stretch_both", margin=(25, 50, 25, 50)
        )

        app = pn.Column(
            header,
            pn.Row(self.sidebar, self.main, css_classes=["mid"]),
            sizing_mode="stretch_width",
        )

        items = {
            "app": app,
        }
        super().__init__(template=template, items=items)
