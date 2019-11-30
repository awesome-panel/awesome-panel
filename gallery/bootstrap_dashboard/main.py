import pathlib

import awesome_panel.express as pnx
import gallery.bootstrap_dashboard.components as components
import panel as pn

ABOUT_PATH = pathlib.Path(__file__).parent / "about.md"
PAGES = [
    pnx.Markdown(path=ABOUT_PATH, name="About"),
    components.Dashboard().view(),
    components.Products().view(),
    components.customers_view(),
    components.plotly_view(),
    components.holoviews_view(),
    pnx.Markdown("## Reports", name="Reports"),
    pnx.Markdown("## Integrations", name="Integrations"),
]


def main() -> pn.Pane:
    app = pnx.templates.BasicTemplate(app_title="Company Name")

    navigator = pnx.Navigator(pages=PAGES)
    app.sidebar.append(navigator.menu)
    app.main.append(navigator.selected_page)
    return app


if __name__.startswith("bk_script"):
    main().servable()
