"""The ProgressSpinnerComponent view method shows a spinner if there is Progress"""
import panel as pn
import param
from awesome_panel.application import assets
from awesome_panel.application.services import ProgressService, ThemeService


class ProgressSpinnerComponent(pn.pane.HTML):
    """The ProgressSpinnerComponent view method shows a spinner if there is Progress"""

    progress_service = param.ClassSelector(
        class_=ProgressService, instantiate=False, allow_None=False
    )
    theme_service = param.ClassSelector(class_=ThemeService, instantiate=False, allow_None=False)
    view = param.Parameter(constant=True, allow_None=False)

    def __init__(self, **params):
        params["view"] = pn.pane.HTML()

        super().__init__(**params)

        self._update()

    @param.depends("progress_service.progress", "theme_service.theme", watch=True)
    def _update(self, _=None):
        # pylint: disable=no-member
        if self.theme_service.theme:
            if self.progress_service.progress.active:
                url = self.theme_service.theme.spinner_url
            else:
                url = self.theme_service.theme.spinner_static_url
        else:
            if self.progress_service.progress.active:
                url = assets.SPINNER_PANEL_BREATH_LIGHT_400_340
            else:
                url = assets.SPINNER_PANEL_STATIC_LIGHT_400_340

        self.view.object = self._to_img_html(url)

    def _to_img_html(self, url):
        # pylint: disable=no-member
        return (
            f"<img src='{url}' style='height:100%' "
            f"title='{self.progress_service.progress.message}'></img>"
        )
