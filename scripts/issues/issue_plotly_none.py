"""Example illustrating bug in Panel.

The plotly plot does not update when data is set! HoloViews does"""

import hvplot.pandas
import pandas as pd
import panel as pn
import param
import plotly.express as px

pn.extension("plotly")


class App(param.Parameterized):
    data_is_set = param.Boolean(default=False)
    data = param.DataFrame()

    @pn.depends(
        "data_is_set", watch=True,
    )
    def set_data(self,):
        if self.data_is_set:
            rows = [
                (1, 2,),
                (3, 4,),
            ]
            self.data = pd.DataFrame(rows, columns=["x", "y",],)
        else:
            self.data = None

    @pn.depends("data")
    def plot_holoviews(self,):
        if self.data is None or self.data.empty:
            return None

        return self.data.hvplot(x="x", y="y",)

    @pn.depends("data")
    def plot_plotly(self,):
        if self.data is None or self.data.empty:
            return None

        return px.scatter(self.data, x="x", y="y",)

    def view(self,):
        return pn.Column(
            self.param.data_is_set,
            pn.pane.Markdown("## Holoviews"),
            self.plot_holoviews,
            pn.pane.Markdown("## Plotly"),
            self.plot_plotly,
            width=800,
        )


if __name__.startswith("bk"):
    App().view().servable()
