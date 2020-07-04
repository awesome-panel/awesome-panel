from logging import setLogRecordFactory
import param
import numpy as np
import pandas as pd
import panel as pn
import holoviews as hv
import bokeh
from bokeh.resources import INLINE
import hvplot.pandas

hv.extension("bokeh")
pn.extension()
pn.config.sizing_mode = "stretch_width"

EMPTY_PLOT = hv.Curve({})

STYLE = """
body {
    margin: 0px;
    min_height: 100vh;
}
.bk.app-body {
    background: #f2f2f2;
    color: #000000;
    font-family: roboto, sans-serif, Verdana;
}
.bk.app-bar {
    background: #2196F3;
    border-color: white;
    box-shadow: 5px 5px 20px #9E9E9E;
    color: #ffffff;
    z-index: 50;
}
.bk.app-container {
    background: #ffffff;
    border-radius: 5px;
    box-shadow: 2px 2px 2px lightgrey;
    color: #000000;
}

.bk.app-settings {
    background: #e0e0e0;
    color: #000000;
}

"""

pn.config.raw_css.append(STYLE)

try:
    data_A = pd.read_csv("data_A.csv", index_col=0)
except Exception as e:
    data_A = pd.read_csv(
        "https://discourse.holoviz.org/uploads/short-url/ceLgCS43UtYgICERGGnBpTxG4UX.csv",
        index_col=0,
    )
    data_A.to_csv("data_A.csv")

try:
    data_B = pd.read_csv("data_B.csv", index_col=0)
except Exception as e:
    data_B = pd.read_csv(
        "https://discourse.holoviz.org/uploads/short-url/mLsBXvpSQTex5rU6RZpzsaxOe5b.csv",
        index_col=0,
    )
    data_B.to_csv("data_B.csv")

Variable = pn.widgets.RadioBoxGroup(
    name="Variable",
    options=["Cut Distance", "Removed Volume", "Av. uncut chip thickness"],
    inline=True,
    align="center",
)

# Insert plot
class PempDashoardApp(param.Parameterized):
    tool = param.ObjectSelector(label="Tool", default="S1_1", objects=["S1_1", "S2_1"])
    variable = param.ObjectSelector(
        label="Variable",
        default="Cut Distance",
        objects=["Cut Distance", "Removed Volume", "Av. uncut chip thickness"],
    )

    insert_plot_pane = param.ClassSelector(class_=pn.pane.HoloViews)
    edge_plot_pane = param.ClassSelector(class_=pn.pane.HoloViews)
    history_plot_pane = param.ClassSelector(class_=pn.pane.HoloViews)

    view = param.ClassSelector(class_=pn.Column)

    def __init__(self, **params):
        params["insert_plot_pane"] = pn.pane.HoloViews(EMPTY_PLOT, sizing_mode="stretch_both")
        params["edge_plot_pane"] = pn.pane.HoloViews(EMPTY_PLOT, sizing_mode="stretch_both")
        params["history_plot_pane"] = pn.pane.HoloViews(EMPTY_PLOT, sizing_mode="stretch_both")
        params["view"] = pn.Column(css_classes=["app-body"], sizing_mode="stretch_both", margin=0)

        super().__init__(**params)

        self._init_view()
        self._update_insert_plot()
        self._update_edge_plot()
        self._update_history_plot()

    def _init_view(self):
        appbar = pn.Row(
            pn.pane.Markdown("# Classic Dashboard in Panel ", margin=(10, 5, 10, 25)),
            css_classes=["app-bar"],
        )
        settings_bar = pn.Row(
            pn.pane.Markdown("Tool & Variable: ", width=100, sizing_mode="fixed", margin=(10, 5, 10, 25)),
            pn.Param(
                self,
                parameters=["tool", "variable"],
                widgets={
                    "tool": {"align": "center", "width": 75, "sizing_mode": "fixed"},
                    "variable": {"type": pn.widgets.RadioBoxGroup, "inline": True, "align": "center"}
                },
                default_layout=pn.Row,
                show_name=False,
                show_labels=False,
                align="center",
            ),
            css_classes=["app-container"],
            margin=(50, 25, 25, 25),
        )

        self.view[:] = [
            appbar,
            settings_bar,
            pn.Row(
                pn.Column(self.insert_plot_pane, css_classes=["app-container"], margin=25),
                pn.Column(self.edge_plot_pane, css_classes=["app-container"], margin=25),
            ),
            pn.Row(self.history_plot_pane, css_classes=["app-container"], margin=25),
            pn.layout.VSpacer(),
            pn.layout.VSpacer(),
        ]

    @pn.depends("tool", "variable", watch=True)
    def _update_insert_plot(self):
        plot_data = data_A.loc[self.tool]
        self.insert_plot_pane.object = plot_data.hvplot(
            x="Xo", y="Yo", kind="paths", line_width=4, tools=["hover"], colorbar=True
        ).opts(cmap="winter")

    @pn.depends("tool", "variable", watch=True)
    def _update_edge_plot(self):
        plot_data = data_A.loc[self.tool]
        self.edge_plot_pane.object = plot_data.hvplot(
            x="Number", y=self.variable, kind="area", alpha=0.6, tools=["hover"]
        )

    @pn.depends("tool", watch=True)
    def _update_history_plot(self):
        plot_data = data_B.loc[self.tool]
        self.history_plot_pane.object = plot_data.hvplot(
            x="Cut Distance", y="Feed", kind="line", line_width=4
        ).opts(tools=["hover"])


def view():
    return PempDashoardApp().view


if __name__.startswith("bokeh"):
    view().servable()
else:
    view().show(port=5007)
