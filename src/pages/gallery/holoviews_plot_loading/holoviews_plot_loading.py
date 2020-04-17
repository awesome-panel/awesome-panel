"""This example was created by as response to
<a href=https://discourse.holoviz.org/t/how-to-show-a-loading-indication-during-computation/508"
target="_blank"> Discourse 508</a> <strong>How to show a loading indication during
computation</strong>.

You can find a live version in the Gallery at
<a href="https://awesome-panel.org">awesome-panel.org</a>.
"""

import math
import time

import holoviews as hv
import hvplot.pandas
import pandas as pd
import panel as pn
import param

EMPTY_DATAFRAME = pd.DataFrame(columns=["x", "y"])
EMPTY_PLOT = hv.Div(__doc__)


class DataExplorer(param.Parameterized):
    load_time = param.Integer(default=1, bounds=(0, 10), label="Load Time (seconds)")
    data = param.DataFrame()

    def __init__(self, **params):
        super().__init__(**params)

        self.plot_pane = pn.pane.HoloViews(EMPTY_PLOT, sizing_mode="stretch_both")

    def set_hv_loading_message(self, message: str):
        self.plot_pane.object = hv.Div(message)

    @param.depends("load_time", watch="True")
    def load_data(self):
        x=[]
        y=[]
        for i in range(0, self.load_time):
            for j in range(0, self.load_time):
                x.append(i * j)
                y.append(math.sin(i * j ** math.pi / 4))

            message = f"Loading ({i+1}/{self.load_time})"
            self.set_hv_loading_message(message)
            time.sleep(1)

        self.data = pd.DataFrame({"x": x, "y": y})
        print(self.data.head())

    @param.depends("data", watch=True)
    def update_plot(self):
        plot = self.data.hvplot(x="x", y="y").opts(responsive=True)
        self.plot_pane.object = plot

    def view(self):
        return pn.Column(pn.Param(self, parameters=["load_time"]), self.plot_pane, sizing_mode="stretch_both")


component = DataExplorer()
app = component.view()
app.servable()
