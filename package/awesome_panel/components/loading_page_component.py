import panel as pn
import param
from awesome_panel.models import Page
from awesome_panel.components.page_component import PageComponent
from awesome_panel.services import author_service

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

        if "page" not in params:
            params["page"] = self._get_page()

        super().__init__(**params)

    def _get_main(self):
        _spinner_pane = pn.pane.GIF(
            SPINNER_URL, embed=False, sizing_mode="fixed", height=200, width=200
        )

        return pn.Column(
            pn.Row(
                pn.layout.HSpacer(), _spinner_pane, pn.layout.HSpacer(), margin=(300, 0, 0, 0)
            ),
        )

    def _get_page(self):
        return Page(
            author = author_service.get_default_author(),
            description = "This Page is shown when changing a page. It shows a spinner by default"
        )
