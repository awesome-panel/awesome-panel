"""The ProgressSpinnerComponent view method shows a spinner if there is Progress"""
import panel as pn
import param

from awesome_panel.application.models import Theme
from awesome_panel.application.services import ProgressService, progress_service


class ProgressSpinnerComponent(pn.pane.HTML):
    """The ProgressSpinnerComponent view method shows a spinner if there is Progress"""

    progress_service = param.ClassSelector(class_=ProgressService, instantiate=False)
    theme = param.ClassSelector(class_=Theme, instantiate=False)
    view = param.Parameter(constant=True)

    def __init__(self, **params):
        self.param.progress_service.default = progress_service
        self.param.theme.default = Theme()
        params["view"] = pn.pane.HTML()

        super().__init__(**params)

        self._update()

    @param.depends("progress_service.progress", "theme", watch=True)
    def _update(self, _=None):
        # pylint: disable=no-member
        if self.progress_service.progress.active:
            url = self.theme.spinner_url
        else:
            url = self.theme.spinner_static_url
        self.view.object = self._to_img_html(url)

    def _to_img_html(self, url):
        # pylint: disable=no-member
        return (
            f"<img src='{url}' style='height:100%' "
            f"title='{self.progress_service.progress.message}'></img>"
        )
