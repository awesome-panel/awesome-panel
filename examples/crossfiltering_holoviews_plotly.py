"""*Linked Brushing* is a very powerful technique. It's also often called
*Linked Selections* or *Crossfiltering*.

This example is inspired by the HoloViews [Linked Brushing Reference Guide]\
(http://holoviews.org/user_guide/Linked_Brushing.html) and the Plotly blog post
[Introducing Dash HoloViews]\
(https://medium.com/plotly/introducing-dash-holoviews-6a05c088ebe5).

This example uses the *Iris* dataset.
"""
from typing import Tuple

import holoviews as hv
import panel as pn
from holoviews import opts
from panel.template import FastListTemplate
import plotly.io as pio
import pandas as pd

@pn.cache
def get_iris_data():
    return pd.read_csv("https://cdn.awesome-panel.org/resources/crossfiltering_holoviews/iris.csv.gz")


ACCENT = "#F08080"

CSS = """
.main .card-margin.stretch_both {
    height: calc(100vh - 125px) !important;
}
"""

def _plotly_hooks(plot, element):
    """Used by HoloViews to give plots plotly plots special treatment"""
    fig = plot.state
    
    fig["layout"]["dragmode"] = "select"
    fig["config"]["displayModeBar"] = True
    if isinstance(element, hv.Histogram):
        # Constrain histogram selection direction to horizontal
        fig["layout"]["selectdirection"] = "h"


def get_linked_plots() -> Tuple:
    """Returns a tuple (scatter, hist) of linked plots
    
    See http://holoviews.org/user_guide/Linked_Brushing.html
    """

    dataset = hv.Dataset(get_iris_data())

    scatter = hv.Scatter(dataset, kdims=["sepal_length"], vdims=["sepal_width"])
    hist = hv.operation.histogram(dataset, dimension="petal_width", normed=False)

    # pylint: disable=no-value-for-parameter
    selection_linker = hv.selection.link_selections.instance()
    # pylint: disable=no-member
    scatter = selection_linker(scatter).opts(
        opts.Scatter(color=ACCENT, size=10, hooks=[_plotly_hooks], width=700, height=400),
    )
    hist = selection_linker(hist).opts(
        opts.Histogram(color=ACCENT, hooks=[_plotly_hooks], width=700, height=400)
    )

    return scatter, hist


def create_app():
    """Returns the app in a nice FastListTemplate"""
    if pn.config.theme == "dark":
        pio.templates.default = "plotly_dark"
    else:
        pio.templates.default = "plotly_white"
    scatter, hist = get_linked_plots()
    scatter_panel = pn.pane.HoloViews(scatter, sizing_mode="stretch_both", backend="plotly")
    hist_panel = pn.pane.HoloViews(hist, sizing_mode="stretch_both", backend="plotly")

    def reset(event):
        scatter, hist = get_linked_plots()
        scatter_panel.object=scatter
        hist_panel.object=hist

    reset_button = pn.widgets.Button(name="RESET PLOTS", on_click=reset, description="Resets the plots. Plotly does not have a built in way to do this.")
    
    template = FastListTemplate(
        site="Awesome Panel",
        site_url="https://awesome-panel.org",
        title="Crossfiltering with HoloViews and Plotly",
        accent=ACCENT,
        main=[
            # We need to wrap in Columns to get them to stretch properly
            pn.Column(reset_button, scatter_panel, pn.layout.Spacer(height=20), hist_panel, height=870, sizing_mode="stretch_width"),
        ],
        main_max_width="850px",
    )
    return template

pn.extension("plotly", raw_css=[CSS])
hv.extension("plotly")
create_app().servable()
