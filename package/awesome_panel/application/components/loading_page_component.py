import panel as pn
import param
from awesome_panel.application.models import Page, Theme
from awesome_panel.application.components.page_component import PageComponent
from awesome_panel.application.components.progress_spinner_component import ProgressSpinnerComponent

from awesome_panel.application.services import author_service, progress_service, ProgressService

ROOT_URL = (
    "https://raw.githubusercontent.com/MarcSkovMadsen/awesome-panel/master/assets/images/spinners/"
)
SPINNER_URL = ROOT_URL + "spinner_panel_rotate_400_400.gif"
SPINNER_STATIC_URL = ROOT_URL + "spinner_panel_static_light_400_340.gif"

class LoadingPageComponent(PageComponent):
    name = param.String("Loading")

    def __init__(self, **params):
        if "main" not in params:
            params["main"] = self._get_main()

        super().__init__(**params)

    def _get_main(self):
        spinner = ProgressSpinnerComponent().view
        spinner.sizing_mode="fixed"
        spinner.height=200
        spinner.width=200

        return pn.Column(
            pn.Row(
                pn.layout.HSpacer(), spinner, pn.layout.HSpacer(), margin=(300, 0, 0, 0)
            ),
        )
