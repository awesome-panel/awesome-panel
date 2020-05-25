"""This example was created by as response to
<a href=https://discourse.holoviz.org/t/how-to-show-a-loading-indication-during-computation/508
target="_blank"> Discourse 508</a> <strong>How to show a loading indication during
computation</strong>.
"""

import math
import time

import holoviews as hv
import hvplot.pandas  # pylint: disable=unused-import
import pandas as pd
import panel as pn
import param

EMPTY_DATAFRAME = pd.DataFrame(columns=["x", "y"])
EMPTY_PLOT = hv.Div("Click UPDATE to load!")
SPINNER_URL = (
    "https://github.com/MarcSkovMadsen/awesome-panel/blob/master/"
    "application/pages/gallery/dataexplorer_loading/spinner.gif?raw=true"
)
SPINNER_HTML = f"<img application='{SPINNER_URL}' style='width:100%'"


class DataExplorer(param.Parameterized):
    """The DataExplorer App illustrates a progress and loading message"""

    load_time = param.Integer(default=8, bounds=(1, 4 * 16), label="Load Time (seconds)")
    data = param.DataFrame()
    update_action = param.Action(label="UPDATE")

    def __init__(self, **params):
        super().__init__(**params)

        self.plot_pane = pn.pane.HoloViews(EMPTY_PLOT, sizing_mode="stretch_both", min_height=300)
        self.update_action = self.load_data
        self.progress_widget = pn.widgets.Progress(
            name="Progress", sizing_mode="stretch_width", value=0
        )

    def set_hv_loading_message(self, message: str):
        """Replaces the plot with a loading message"""
        message_plot = hv.Div(SPINNER_HTML + f"<p align='center'><strong>{message}<strong></p>")

        self.plot_pane.object = message_plot

    def load_data(self, _):
        """Loads the data"""
        steps = self.load_time * 4
        self.progress_widget.max = steps

        xdata = [0]
        ydata = [math.sin(0)]

        for i in range(0, steps):
            xdata.append(i / 16)
            ydata.append(math.sin(i / 16 * 2 * math.pi))

            message = f"Loading ({i+1}/{steps})"
            self.set_hv_loading_message(message)
            self.progress_widget.value = i
            time.sleep(1 / 4)

        self.data = pd.DataFrame({"x": xdata, "y": ydata})
        self.progress_widget.value = 0

    @param.depends("data", watch=True)
    def update_plot(self):
        """Updates the plot"""
        plot = self.data.hvplot.line(x="x", y="y", color="green").opts(
            responsive=True, line_width=4
        )
        self.plot_pane.object = plot

    def view(self):
        """Returns the application view"""
        return pn.Column(
            pn.pane.Markdown(__doc__),
            pn.pane.Markdown("#### Settings"),
            pn.Param(
                self,
                parameters=["load_time", "update_action"],
                show_name=False,
                sizing_mode="stretch_width",
                widgets={"update_action": {"button_type": "success"}},
            ),
            pn.pane.Markdown("#### Progress"),
            self.progress_widget,
            pn.pane.Markdown("#### Plot"),
            self.plot_pane,
            sizing_mode="stretch_both",
        )


def view():
    """Serves the app.

    Needed for inclusion to awesome-panel.org Gallery
    """
    component = DataExplorer()
    return component.view()
