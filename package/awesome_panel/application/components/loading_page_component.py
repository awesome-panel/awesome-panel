"""The LoadingPageComponent provides a Page to show while loading a new Page that takes
considerable time to load"""
import panel as pn
import param

from awesome_panel.application.components.page_component import PageComponent
from awesome_panel.application.components.progress_spinner_component import ProgressSpinnerComponent

class LoadingPageComponent(PageComponent):
    """The LoadingPageComponent provides a Page to show while loading a new Page that takes
    considerable time to load"""
    name = param.String("Loading")

    def __init__(self, **params):
        if "main" not in params:
            params["main"] = self._get_main()

        super().__init__(**params)

    @staticmethod
    def _get_main():
        spinner = ProgressSpinnerComponent().view
        spinner.sizing_mode = "fixed"
        spinner.height = 200
        spinner.width = 200

        return pn.Column(
            pn.Row(pn.layout.HSpacer(), spinner, pn.layout.HSpacer(), margin=(300, 0, 0, 0)),
            sizing_mode="stretch_width",
        )
