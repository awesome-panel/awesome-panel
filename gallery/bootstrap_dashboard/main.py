import pathlib

import awesome_panel.express as pnx
import gallery.bootstrap_dashboard.components as components
import panel as pn

LIMITATIONS_PATH = pathlib.Path(__file__).parent / "limitations.md"
PAGES = [
    components.About(),
    components.Dashboard().view(),
    components.plotly_view(),
    components.holoviews_view(),
    pnx.Markdown(path=LIMITATIONS_PATH, name="Limitations"),
]


def main() -> pn.Pane:
    app = pnx.templates.BootstrapDashboardTemplate(app_title="Bootstrap Dashboard")

    navigator = pnx.Navigator(pages=PAGES, page_outlet=app.main)
    app.sidebar.append(navigator.menu)
    return app


if __name__.startswith("bk_script"):
    main().servable()
