"""*Linked Brushing* is a very powerful technique. It's also often called *Linked Selections* or
*Crossfiltering*.

This example is a copy of [awesome-panel.org/holoviews-linked-brushing]\
(https://awesome-panel.org/holoviews-linked-brushing)
"""
# Currently I cannot get the Plotly Hist plot to be full width+height+responsive
from typing import Any, Dict, Tuple

import holoviews as hv
import panel as pn
import param
import plotly.io as pio
from holoviews import opts
from plotly.data import iris

from src.shared import config
from src.shared.templates import ListTemplate

pn.extension("plotly")
hv.extension("bokeh", "plotly")


def _plotly_hooks(plot, element):
    """Used by HoloViews to give plots plotly plots special treatment"""
    fig = plot.state
    # Use plot hook to set the default drag mode to box selection
    fig["layout"]["dragmode"] = "select"

    fig["layout"]["autosize"] = False
    fig["config"]["responsive"] = False
    fig["config"]["displayModeBar"] = True
    if isinstance(element, hv.Histogram):
        # Constrain histogram selection direction to horizontal
        fig["layout"]["selectdirection"] = "h"


IRIS_DATASET = iris()
OPTS: Dict[str, Dict[str, Any]] = {
    "all": {
        "scatter": {"color": config.color_primary, "responsive": True, "size": 10, "height": 400},
        "hist": {"color": config.color_primary, "responsive": True, "height": 400},
    },
    "bokeh": {
        "scatter": {"tools": ["hover"], "active_tools": ["box_select"]},
        "hist": {"tools": ["hover"], "active_tools": ["box_select"]},
    },
    "plotly": {
        "scatter": {"hooks": [_plotly_hooks]},
        "hist": {"hooks": [_plotly_hooks]},
    },
}


def _get_linked_plots(backend: str = "plotly") -> Tuple:
    """Returns a tuple (scatter, hist) of linked plots

    Args:
        backend (str, optional): "plotly" or "bokeh". Defaults to "plotly".

    Returns:
        [Tuple]: Returns a tuple (scatter, hist) of linked plots
    """

    dataset = hv.Dataset(IRIS_DATASET)

    scatter = hv.Scatter(dataset, kdims=["sepal_length"], vdims=["sepal_width"])
    hist = hv.operation.histogram(dataset, dimension="petal_width", normed=False)

    # pylint: disable=no-value-for-parameter
    selection_linker = hv.selection.link_selections.instance()
    # pylint: disable=no-member
    scatter = selection_linker(scatter).opts(
        opts.Scatter(**OPTS["all"]["scatter"], **OPTS[backend]["scatter"])
    )
    hist = selection_linker(hist).opts(
        opts.Histogram(**OPTS["all"]["hist"], **OPTS[backend]["hist"])
    )

    return scatter, hist


class LinkedBrushingApp(param.Parameterized):
    """Linked Brushing App that enables using the backend (Plotly or Bokeh) of choice"""

    backend = param.ObjectSelector("BOKEH", objects=["BOKEH", "PLOTLY"])
    reset_plots = param.Action(
        label="RESET",
        doc="Resets the plot. Needed because Plotly has no way of removing the linked selections",
    )

    settings_panel = param.Parameter()
    scatter_panel = param.Parameter()
    hist_panel = param.Parameter()

    view = param.Parameter()

    def __init__(self, **params):
        super().__init__(**params)

        self.scatter_panel = pn.pane.HoloViews(sizing_mode="stretch_width", height=400)
        self.hist_panel = pn.pane.HoloViews(sizing_mode="stretch_width", height=400)
        self.reset_plots = self._update_plot_panels

        self.settings_panel = pn.Param(
            self,
            parameters=["backend", "reset_plots"],
            widgets={
                "backend": {"type": pn.widgets.RadioButtonGroup, "button_type": "success"},
                "reset_plots": {"type": pn.widgets.Button, "button_type": "default"},
            },
            show_name=False,
        )
        self.view = self._create_view()

        pn.state.onload(self._update_plot_panels)

    def _create_view(self):
        template = ListTemplate(title="Linked Selections")
        template.sidebar[:] = [pn.pane.Markdown("## Settings"), self.settings_panel]
        template.main[:] = [
            pn.Column(self.scatter_panel, sizing_mode="stretch_both"),
            pn.Column(self.hist_panel, sizing_mode="stretch_both"),
        ]

        if "dark" in str(template.theme).lower():
            self._theme = "dark"
        else:
            self._theme = "default"

        return template

    @param.depends("backend", watch=True)
    def _update_plot_panels(self, *_):
        backend = self.backend.lower()  # pylint: disable=no-member
        hv.extension(backend)
        if backend == "plotly":
            if self._theme == "dark":
                pio.templates.default = "plotly_dark"
            else:
                pio.templates.default = "plotly_white"
        scatter, hist = _get_linked_plots(backend)
        self.scatter_panel.object = scatter
        self.hist_panel.object = hist


def view():
    """Returns the view of the LinkedBrushingApp for use in the site"""
    pn.config.sizing_mode = "stretch_width"
    return LinkedBrushingApp().view


if __name__.startswith("bokeh"):
    # Run the development server
    # python -m panel serve 'src/apps/holoviews_linked_selections.py' --dev --show
    view().servable()
if __name__ == "__main__":
    # Run the server. Useful for integrated debugging in your Editor or IDE.
    # python 'src/apps/holoviews_linked_selections.py'
    view().show(port=5007)
