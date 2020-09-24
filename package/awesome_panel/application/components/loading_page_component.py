"""The LoadingPageComponent provides a Page to show while loading a new Page that takes
considerable time to load"""
import panel as pn
import param
from awesome_panel.application.components.page_component import PageComponent
from awesome_panel.application.components.progress_spinner_component import ProgressSpinnerComponent
from awesome_panel.application.services import ProgressService, ThemeService


class LoadingPageComponent(PageComponent):
    """The LoadingPageComponent provides a Page to show while loading a new Page that takes
    considerable time to load"""

    name = param.String("Loading")
    progress_service = param.ClassSelector(
        class_=ProgressService, instantiate=False, allow_None=False
    )
    theme_service = param.ClassSelector(class_=ThemeService, instantiate=False, allow_None=False)

    def __init__(self, **params):
        if "main" not in params:
            params["main"] = self._get_main(
                progress_service=params["progress_service"], theme_service=params["theme_service"]
            )

        super().__init__(**params)

    @staticmethod
    def _get_main(progress_service, theme_service):
        spinner = ProgressSpinnerComponent(
            progress_service=progress_service, theme_service=theme_service
        ).view
        spinner.sizing_mode = "fixed"
        spinner.height = 200
        spinner.width = 200

        return pn.Column(
            pn.Row(pn.layout.HSpacer(), spinner, pn.layout.HSpacer(), margin=(300, 0, 0, 0)),
            sizing_mode="stretch_width",
        )
