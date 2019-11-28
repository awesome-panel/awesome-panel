import pathlib

import awesome_panel.express as pnx
import gallery.bootstrap_dashboard.views as views
from gallery.bootstrap_dashboard.products.products import Products
import panel as pn

ABOUT_PATH = pathlib.Path(__file__).parent / "about.md"
PAGES = [
    views.Dashboard().view(),
    Products().view(),
    views.customers_view(),
    pn.pane.Markdown("## Reports", name="Reports"),
    pn.pane.Markdown("## Integrations", name="Integrations"),
    views.markdown_from_file(ABOUT_PATH, name="About"),
]


def main() -> pn.Pane:
    app = pnx.templates.BootStrapDashboardTemplate(app_title="Company Name")

    navigator = pnx.shared.Navigator(pages=PAGES)
    app.sidebar.append(navigator.menu)
    app.main.append(navigator.selected_page)
    return app


if __name__ == "__main__" or __name__.startswith("bk_script"):
    main().servable()
