from awesome_panel.styler.stylers.app_styler import AppStyler
from awesome_panel.styler import AwesomePanelStyler
from awesome_panel.designer import Designer, ReloadService
from awesome_panel.styler import app
from awesome_panel.styler.stylers import app_styler
from awesome_panel.styler.stylers import AppStyler
import pandas as pd
import pathlib


def test_designer():
    path = pathlib.Path.cwd() / "application/pages/kickstarter_dashboard/kickstarter-cleaned.csv"

    data = pd.read_csv(path).sample(10)
    app_styler_service = ReloadService(component=AppStyler)
    styler_service = ReloadService(
        component=AwesomePanelStyler,
        component_parameters={"data": data},
        modules_to_reload=[app, app_styler],
    )

    reload_services = [
        app_styler_service,
        styler_service,
    ]
    return Designer(reload_services=reload_services)


if __name__.startswith("__main__"):
    test_designer().show()
