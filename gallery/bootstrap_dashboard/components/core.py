import inspect
from typing import List, NamedTuple

import holoviews as hv
import hvplot.pandas
import panel as pn
from plotly import express as px

import awesome_panel.express as pnx
from gallery.bootstrap_dashboard import services

pn.extension()

# See also https://holoext.readthedocs.io/en/latest/examples/modifying_toolbar_tools.html#Hide-toolbar
def disable_logo(plot, element):
    plot.state.toolbar.logo = None


hv.plotting.bokeh.ElementPlot.finalize_hooks.append(disable_logo)


def holoviews_chart():
    data = services.get_chart_data()
    line_plot = data.hvplot.line(
        x="Day", y="Orders", width=None, height=500, line_color="#007BFF", line_width=6,
    )
    scatter_plot = data.hvplot.scatter(x="Day", y="Orders", height=300).opts(
        marker="o", size=10, color="#007BFF"
    )
    fig = line_plot * scatter_plot
    gridstyle = {"grid_line_color": "black", "grid_line_width": 0.1}
    fig = fig.opts(
        responsive=True,
        toolbar=None,
        yticks=list(range(12000, 26000, 2000)),
        ylim=(12000, 26000),
        gridstyle=gridstyle,
        show_grid=True,
    )
    return fig


def holoviews_view() -> pn.Column:
    fig = holoviews_chart()
    return pn.Column(
        pnx.Header("Holoviews"),
        fig,
        pnx.Code(inspect.getsource(holoviews_chart)),
        name="Holoviews",
        sizing_mode="stretch_both",
    )


def plotly_chart():
    fig = px.line(services.get_chart_data(), x="Day", y="Orders")
    fig.update_traces(mode="lines+markers", marker=dict(size=10), line=dict(width=4))
    fig.layout.paper_bgcolor = "rgba(0,0,0,0)"
    fig.layout.plot_bgcolor = "rgba(0,0,0,0)"
    fig.layout.width = 1000
    fig.layout.autosize = True
    return fig


def plotly_view(*args, **kwargs) -> pn.Column:
    fig = plotly_chart()
    return pn.Column(
        pnx.Header("Plotly"),
        pn.Row(pn.layout.HSpacer(), fig, pn.layout.HSpacer(),),
        pn.pane.HTML("Plotly cannot currently auto size to full width and be responsive"),
        pnx.Code(code=inspect.getsource(plotly_chart)),
        sizing_mode="stretch_width",
        name="Plotly",
        *args,
        **kwargs,
    )


if __name__.startswith("bk"):
    # holoviews_view().servable()
    plotly_view().servable()
