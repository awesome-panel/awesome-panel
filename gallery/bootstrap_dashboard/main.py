import panel as pn
import views
import awesome_panel.express as pnx


def main() -> pn.Pane:
    page = views.PageView()
    app = pnx.templates.BootStrapDashboardTemplate(app_title="Company Name")
    app.sidebar.append(page.select)
    app.main.append(page.view)
    return app


if __name__ == "__main__" or __name__.startswith("bk_script"):
    main().servable()
