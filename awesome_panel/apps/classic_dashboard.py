"""
The Dashboard app shows how to create a **Classic Dashboard** in **Panel** with

- Classic Layout and awesome design
- Responsiveness
- User Selections
- [Linked Brushing](http://holoviews.org/user_guide/Linked_Brushing.html) (Not yet supported)

This app was kick started by [Pemp](https://discourse.holoviz.org/u/pemp) in a
[discussion on Discourse]\
(https://discourse.holoviz.org/t/error-not-supported-between-instances-of-select-and-select/929).
"""
import pathlib

import holoviews as hv
import hvplot.pandas  # pylint: disable=unused-import
import pandas as pd
import panel as pn
import param
from holoviews.plotting.util import process_cmap

from awesome_panel import config
from awesome_panel.assets.csv import DASHBOARD_A_PATH, DASHBOARD_B_PATH

EMPTY_PLOT = None
COLOR_MAPS = hv.plotting.util.list_cmaps()
STYLE = """
.bk.app-body {
    background: #f2f2f2;
    color: #000000;
    font-family: roboto, sans-serif, Verdana;
}
.bk.app-bar {
    background: #212121;
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

if not STYLE in pn.config.raw_css:
    pn.config.raw_css.append(STYLE)

ROOT = pathlib.Path(__file__).parent
DATA_A = pd.read_csv(DASHBOARD_A_PATH, index_col=0)
DATA_B = pd.read_csv(DASHBOARD_B_PATH, index_col=0)


class Dashboard(param.Parameterized):
    """This application show cases how to build a Classic Dashboard
    in Panel.
    """

    tool = param.ObjectSelector(label="Tool", default="S1_1", objects=["S1_1", "S2_1"])
    variable = param.ObjectSelector(
        label="Variable",
        default="Cut Distance",
        objects=["Cut Distance", "Removed Volume", "Av. uncut chip thickness"],
    )
    color_map = param.ObjectSelector(default="gist_rainbow", objects=COLOR_MAPS)

    insert_plot_pane = param.ClassSelector(class_=pn.pane.HoloViews)
    edge_plot_pane = param.ClassSelector(class_=pn.pane.HoloViews)
    history_plot_pane = param.ClassSelector(class_=pn.pane.HoloViews)

    view = param.ClassSelector(class_=pn.Column)

    def __init__(self, **params):
        params["insert_plot_pane"] = pn.pane.HoloViews(
            EMPTY_PLOT, sizing_mode="stretch_width", margin=10, height=300
        )
        params["edge_plot_pane"] = pn.pane.HoloViews(
            EMPTY_PLOT, sizing_mode="stretch_width", margin=10, height=300
        )
        params["history_plot_pane"] = pn.pane.HoloViews(
            EMPTY_PLOT, sizing_mode="stretch_width", margin=10, height=300
        )
        params["view"] = pn.Column(sizing_mode="stretch_both")

        super().__init__(**params)

        self._init_view()
        self._update_insert_plot()
        self._update_edge_plot()
        self._update_history_plot()

    def _init_view(self):
        appbar = pn.Row(
            pn.pane.Markdown(
                "#### Classic Dashboard in Panel ",
                margin=(10, 5, 10, 25),
                sizing_mode="stretch_width",
                align="center",
            ),
            pn.layout.HSpacer(height=0),
            pn.pane.PNG(
                "https://panel.holoviz.org/_static/logo_horizontal.png",
                width=200,
                align="center",
                sizing_mode="fixed",
                margin=(10, 50, 10, 5),
                embed=False,
            ),
            sizing_mode="stretch_width",
            css_classes=["app-bar"],
        )
        settings_bar = pn.Column(
            pn.Param(
                self,
                parameters=["tool", "variable", "color_map"],
                widgets={
                    "tool": {"align": "center", "width": 75, "sizing_mode": "fixed"},
                    "variable": {
                        "type": pn.widgets.RadioBoxGroup,
                        "inline": True,
                        "align": "end",
                        "sizing_mode": "stretch_width",
                    },
                },
                default_layout=pn.Row,
                show_name=False,
                sizing_mode="stretch_width",
            ),
            pn.layout.HSpacer(height=0),
            sizing_mode="stretch_width",
            css_classes=["app-container"],
            margin=(50, 25, 25, 25),
        )

        self.view[:] = [  # pylint: disable=unsupported-assignment-operation
            pn.Column(
                appbar,
                settings_bar,
                pn.Row(
                    pn.Column(
                        self.insert_plot_pane,
                        css_classes=["app-container"],
                        margin=25,
                        sizing_mode="stretch_both",
                    ),
                    pn.Column(
                        self.edge_plot_pane,
                        css_classes=["app-container"],
                        margin=25,
                        sizing_mode="stretch_both",
                    ),
                    sizing_mode="stretch_both",
                    min_height=300,
                ),
                pn.Row(
                    self.history_plot_pane,
                    css_classes=["app-container"],
                    margin=25,
                    min_height=300,
                    sizing_mode="stretch_both",
                ),
                css_classes=["app-body"],
                sizing_mode="stretch_both",
            ),
            pn.layout.HSpacer(height=25),
        ]

    @pn.depends("tool", "variable", "color_map", watch=True)
    def _update_insert_plot(self):
        plot_data = DATA_A.loc[self.tool]
        data = [(plot_data["Xo"], plot_data["Yo"], plot_data[self.variable])]
        self.insert_plot_pane.object = hv.Path(data, vdims=self.variable).opts(
            cmap=self.color_map, color=self.variable, line_width=4, colorbar=True, responsive=True
        )

    @pn.depends("tool", "variable", "color_map", watch=True)
    def _update_edge_plot(self):
        plot_data = DATA_A.loc[self.tool]
        self.edge_plot_pane.object = plot_data.hvplot(
            x="Number", y=self.variable, kind="area", alpha=0.6, color=self._color, responsive=True
        )

    @pn.depends("tool", "color_map", watch=True)
    def _update_history_plot(self):
        plot_data = DATA_B.loc[self.tool]
        self.history_plot_pane.object = plot_data.hvplot(
            x="Cut Distance", y="Feed", kind="line", line_width=4, responsive=True
        ).opts(color=self._color)

    @property
    def _color(self):
        return process_cmap(self.color_map, 1)[0]


if __name__.startswith("bokeh") or __name__ == "__main__":
    pn.config.raw_css.append(
        """
    body {
        margin: 0px;
        min-height: 100vh;
        overflow-x: hidden;
        width: 100%;
    }
    """
    )
    config.extension(url="classic_dashboard", main_max_width="80%")
    Dashboard().view.servable()
