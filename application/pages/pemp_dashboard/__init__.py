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

STYLE = """

body {

    margin: 0px;

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

Tool = pn.widgets.Select(name="Tool", options=["S1_1", "S2_1"], sizing_mode="fixed")

Variable = pn.widgets.RadioBoxGroup(
    name="Variable",
    options=["Cut Distance", "Removed Volume", "Av. uncut chip thickness"],
    inline=True,
    align="center",
)

# Insert plot


@pn.depends(Tool.param.value, Variable.param.value)
def insert_plot(tool_value, variable_value):

    plot_data = data_A.loc[tool_value]

    return plot_data.hvplot(
        x="Xo", y="Yo", kind="paths", line_width=4, tools=["hover"], colorbar=True
    ).opts(cmap="winter")

    # xs = data_A.loc[tool_value]["Xo"]

    # ys = data_A.loc[tool_value]["Yo"]

    # zs = data_A.loc[tool_value][variable_value]

    # plot = hv.Path([{"x": xs, "y": ys, "z": zs}], vdims="z")

    # return plot.opts(

    #     colorbar=True,

    #     color="z",

    #     cmap="winter",

    #     line_width=4,

    #     height=300,

    #     width=400,

    #     tools=["hover"],

    # )


# Edge plot


@pn.depends(Tool.param.value, Variable.param.value)
def edge_plot(tool_value, variable_value):

    plot_data = data_A.loc[tool_value]

    return plot_data.hvplot(
        x="Number", y=variable_value, height=300, kind="area", alpha=0.6, tools=["hover"]
    )


# History plot


@pn.depends(Tool.param.value)
def history_plot(tool_value):

    plot_data = data_B.loc[tool_value]

    return plot_data.hvplot(x="Cut Distance", y="Feed", kind="line", height=300, line_width=4).opts(
        tools=["hover"]
    )


dashboard = pn.Column(
    pn.Row(
        pn.pane.Markdown("# Welcome to the Panel Community! ", margin=(10, 5, 10, 25)),
        css_classes=["app-bar"],
    ),
    pn.Row(Tool, Variable, css_classes=["app-container"], margin=(50, 25, 25, 25)),
    pn.Row(
        pn.Column(insert_plot, css_classes=["app-container"], margin=25),
        pn.Column(edge_plot, css_classes=["app-container"], margin=25),
    ),
    pn.Row(history_plot, css_classes=["app-container"], margin=25),
    pn.Spacer(),
    css_classes=["app-body"],
    sizing_mode="stretch_both",
)

if __name__.startswith("bokeh"):

    dashboard.servable()

else:

    dashboard.show(port=5007)
