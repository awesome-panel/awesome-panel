import time
from random import randint

import hvplot.pandas
import pandas as pd
import panel as pn
import param


class DataHolder(param.Parameterized):
    value_a = param.ObjectSelector(default=1, objects=[1, 2, 3], label="A")
    value_b = param.ObjectSelector(default=4, objects=[4, 5, 6], label="B")
    value_c = param.ObjectSelector(default=7, objects=[7, 8, 9], label="C")

    data = param.DataFrame()
    view = param.Parameter()

    def __init__(self, **params):
        super().__init__(**params)

        self._sleep = 0

        self._create_view()
        self._update_data()
        self._update_plot()

        self._sleep = 5

    def _create_view(self):
        self.settings_panel = pn.Param(self, parameters=["value_a", "value_b", "value_c"])
        self.plot_panel = pn.pane.HoloViews(sizing_mode="stretch_width")
        self.progress = pn.widgets.Progress(sizing_mode="stretch_width", bar_color="primary")
        self.view = pn.Column(
            self.progress,
            pn.Row(pn.WidgetBox(self.settings_panel), self.plot_panel, sizing_mode="stretch_width"),
        )

    @param.depends("value_a", "value_b", watch=True)
    def _update_data(self, *event):
        self.progress.active = True
        time.sleep(self._sleep)
        self.data = pd.DataFrame(
            {
                "x": [i for i in range(0, 10)],
                "y": [self.value_a + randint(0, 10) * self.value_b for i in range(0, 10)],
            }
        )
        print("data updated")
        self.progress.active = False

    @param.depends("data", "value_c", watch=True)
    def _update_plot(self, *event):
        if self.data is None:
            return

        data = self.data.copy()
        data.loc[self.value_c, "y"] = self.value_c + data.loc[self.value_c, "y"]
        self.plot_panel.object = data.hvplot(x="x", y="y")
        print("plot updated")


DataHolder().view.servable()
