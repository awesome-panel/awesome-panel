"""# BootstrapDashboard App.

Creates a Bootstrap Dashboard App

- inspired by the [GetBoostrap Dashboard Template]
(https://getbootstrap.com/docs/4.4/examples/dashboard/)
- implemented using the `awesome_panel' python package and in particular the
`awesome_panel.express.templates.BootstrapDashboardTemplate`
- Start the app by using `panel serve` on this file.
"""
import pathlib

import awesome_panel.express as pnx
import gallery.bootstrap_dashboard.components as components
import panel as pn

LIMITATIONS_PATH = pathlib.Path(__file__).parent / "limitations.md"
PAGES = [
    components.About(),
    components.dashboard_view(),
    components.plotly_view(),
    components.holoviews_view(),
    components.dataframe_view(),
    components.Limitations(),
]
MENU_BUTTON_CSS_CLASSES = [
    ["navigation", "pas", "pa-home"],
    ["navigation", "pas", "pa-chart-line"],
    ["navigation", "pas", "pa-chart-bar"],
    ["navigation", "pas", "pa-chart-pie"],
    ["navigation", "pas", "pa-table"],
    ["navigation", "pas", "pa-bug"],
]


def main() -> pn.Pane:
    """## Bootstrap Dashboard App

    Creates a Bootstrap Dashboard App

    - inspired by the [GetBoostrap Dashboard Template]
    (https://getbootstrap.com/docs/4.4/examples/dashboard/)
    - implemented using the `awesome_panel' python package and in particular the
    `awesome_panel.express.templates.BootstrapDashboardTemplate`

    Returns:
        pn.Pane -- The Bootstrap Dashboard App
    """
    pnx.fontawesome.extend()

    app = pnx.templates.BootstrapDashboardTemplate(app_title="Bootstrap Dashboard")
    navigation_menu = pnx.NavigationMenu(
        pages=PAGES, page_outlet=app.main, css_classes=MENU_BUTTON_CSS_CLASSES
    )
    app.sidebar.append(navigation_menu)
    return app


if __name__.startswith("bk_script"):
    main().servable()
