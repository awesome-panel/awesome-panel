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
import pandas as pd
import panel as pn
from holoviews import opts
from panel.template import FastListTemplate


@pn.cache
def get_iris_data():
    return pd.read_csv("https://cdn.awesome-panel.org/resources/crossfiltering_holoviews/iris.csv.gz")


ACCENT = "#F08080"

CSS = """
.main .card-margin.stretch_both {
    height: calc(50vh - 65px) !important;
}
"""
if not CSS in pn.config.raw_css:
    pn.config.raw_css.append(CSS)

BOKEH_TOOLS = {
    "tools": ["hover"], "active_tools": ["box_select"]
}


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
        opts.Scatter(color=ACCENT, responsive=True, size=10, **BOKEH_TOOLS),
    )
    hist = selection_linker(hist).opts(
        opts.Histogram(color=ACCENT, responsive=True, **BOKEH_TOOLS)
    )

    return scatter, hist


def create_app():
    """Returns the app in a nice FastListTemplate"""
    scatter, hist = get_linked_plots()
    scatter_panel = pn.pane.HoloViews(scatter, sizing_mode="stretch_both")
    hist_panel = pn.pane.HoloViews(hist, sizing_mode="stretch_both")
    
    template = FastListTemplate(
        site="Awesome Panel",
        site_url="https://awesome-panel.org",
        title="Crossfiltering with HoloViews and Bokeh",
        accent=ACCENT,
        main=[
            # We need to wrap in Columns to get them to stretch properly
            pn.Column(scatter_panel, sizing_mode="stretch_both"),
            pn.Column(hist_panel, sizing_mode="stretch_both"),
        ],
    )
    return template

pn.extension()
hv.extension("bokeh")
create_app().servable()
