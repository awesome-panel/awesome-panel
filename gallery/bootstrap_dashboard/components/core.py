from typing import List, NamedTuple

import holoviews as hv
import hvplot.pandas
from gallery.bootstrap_dashboard import services
import panel as pn
import awesome_panel.express as pnx

pn.extension()

# See also https://holoext.readthedocs.io/en/latest/examples/modifying_toolbar_tools.html#Hide-toolbar
def disable_logo(plot, element):
    plot.state.toolbar.logo = None


hv.plotting.bokeh.ElementPlot.finalize_hooks.append(disable_logo)


def holoviews_chart():
    data = services.get_chart_data()
    line_plot = data.hvplot.line(
        x="Day", y="Orders", width=None, height=300, line_color="#007BFF", line_width=6,
    )
    scatter_plot = data.hvplot.scatter(x="Day", y="Orders", height=300).opts(
        marker="o", size=10, color="#007BFF"
    )
    fig = line_plot * scatter_plot
    fig = fig.opts(
        responsive=True, toolbar=None, yticks=list(range(12000, 26000, 2000)), ylim=(12000, 26000)
    )
    return fig


def holoviews_view() -> pn.Column:
    fig = holoviews_chart()
    return pn.Column(pnx.Header("Holoviews"), fig, name="Holoviews", sizing_mode="stretch_both")


if __name__.startswith("bk"):
    holoviews_view().servable()
