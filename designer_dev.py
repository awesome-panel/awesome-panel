from awesome_panel.designer import Designer, ReloadService

from application.pages.pandas_profiling_app.pandas_profiling_app import PandasProfilingApp


def show():
    pandas_profiling_app = ReloadService(PandasProfilingApp)
    reload_services = [pandas_profiling_app]
    Designer(reload_services=reload_services).show()


if __name__ == "__main__":
    show()
