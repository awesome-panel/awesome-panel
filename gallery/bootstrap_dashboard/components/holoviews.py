from typing import List, NamedTuple

import holoviews as hv
import hvplot.pandas
from gallery.bootstrap_dashboard import services
import panel as pn

pn.extension()

# See also https://holoext.readthedocs.io/en/latest/examples/modifying_toolbar_tools.html#Hide-toolbar
def disable_logo(plot, element):
    plot.state.toolbar.logo = None


hv.plotting.bokeh.ElementPlot.finalize_hooks.append(disable_logo)


def holoviews_view():
    data = services.get_chart_data()
    fig = data.hvplot.scatter(width=None, height=None).opts(
        "Scatter", min_height=300, min_width=200, responsive=True
    )
    return pn.Column("# Holoviews", fig, name="Holoviews", sizing_mode="stretch_width")
