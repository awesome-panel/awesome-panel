import panel as pn
import param

from awesome_panel.application.components import PageComponent, ProgressSpinnerComponent
from awesome_panel.application.services import progress_service
from awesome_panel.application.models import Progress

BREATH = "<img src='https://github.com/MarcSkovMadsen/awesome-panel/raw/master/assets/images/spinners/spinner_panel_breath_light_400_340.gif' style='height:100%' title=''></img>"

class TestProgressServicePageComponent(PageComponent):
    progress = param.ClassSelector(class_=Progress)
    reset = param.Action()

    def __init__(self, **params):
        self.param.progress.default = Progress()
        self.html_pane = pn.pane.HTML("0")
        self.param.main.default = self._main()


        super().__init__(**params)

        self.reset = progress_service.reset()

        self._update()

    @param.depends("progress", "progress.value", "progress.message", "progress.value_max", "progress.active_count", watch=True)
    def _update(self):
        progress = self.progress
        progress_service.update(
            value=progress.value,
            value_max=progress.value_max,
            message=progress.message,
            active_count=progress.active_count
        )
        if progress.active_count>0:
            self.html_pane.object = str(BREATH)
        else:
            self.html_pane.object = "0"

    def _main(self):
        spinner = ProgressSpinnerComponent()
        return pn.Column(
            pn.Param(
                self
            ),
            self.html_pane,
            progress_service.param.progress,
            "Hellow",
            "Hello",
            spinner,
            spinner.param.object,
        )

print("\nstarting\n")

if __name__.startswith("__main__"):
    pn.config.sizing_mode="stretch_width"
    TestProgressServicePageComponent().main.show()

if __name__.startswith("bokeh"):
    pn.config.sizing_mode="stretch_width"
    TestProgressServicePageComponent().main.servable()
