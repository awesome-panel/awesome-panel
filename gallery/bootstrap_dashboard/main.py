import panel as pn
import param
import pathlib
import views
import awesome_panel.express as pnx

# Todo: Readme https://docs.bokeh.org/en/latest/docs/user_guide/server.html#directory-format

TEMPLATES_ROOT = pathlib.Path(__file__).parent / "templates"
BOOTSTRAP_DASHBOARD_TEMPLATE = TEMPLATES_ROOT / "bootstrap_dashboard.html"


def main() -> pn.Pane:
    page = views.PageView()
    app = pnx.templates.BootStrapDashboardTemplate(app_title="Company Name")
    app.sidebar.append(page.select)
    app.main.append(page.view)
    return app


if __name__ == "__main__" or __name__.startswith("bk_script"):
    main().servable()
