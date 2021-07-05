"""*Linked Brushing* is a very powerful technique. It's also often called *Linked Selections* or
*Crossfiltering*.

This example is inspired by the HoloViews [Linked Brushing Reference Guide]\
(http://holoviews.org/user_guide/Linked_Brushing.html) and the Plotly blog post
[Introducing Dash HoloViews]\
(https://medium.com/plotly/introducing-dash-holoviews-6a05c088ebe5).

This example uses the *Iris* dataset.
"""
from typing import Any, Dict, Tuple

import holoviews as hv
import panel as pn
import param
import plotly.io as pio
from holoviews import opts
from panel.template import FastGridTemplate
from plotly.data import iris

from awesome_panel_extensions.site import site
pn.extension("plotly")
hv.extension("bokeh", "plotly")

APPLICATION = site.create_application(
    url="holoviews-linked-brushing",
    name="HoloViews Linked Brushing",
    author="Marc Skov Madsen",
    description="A demonstration of HoloViews linked brushing for Bokeh and Plotly backends",
    description_long=__doc__,
    thumbnail="https://raw.githubusercontent.com/MarcSkovMadsen/awesome-panel/master/assets/images/thumbnails/holoviews-linked-brushing.png",
    resources = {
        "code": "https://github.com/MarcSkovMadsen/awesome-panel/tree/master/application/pages/holoviews_linked_brushing.py",
        "mp4": "https://raw.githubusercontent.com/MarcSkovMadsen/awesome-panel-assets/master/awesome-panel/applications/holoviews-linked-brushing.mp4",
    },
    tags=["Panel", "Bokeh", "Plotly", "HoloViews", "Linked Brushing", "Cross Filter"],
)


def _plotly_hooks(plot, element):
    """Used by HoloViews to give plots plotly plots special treatment"""
    fig = plot.state
    # Use plot hook to set the default drag mode to box selection
    fig["layout"]["dragmode"] = "select"

    fig["layout"]["autosize"] = True
    fig["config"]["responsive"] = True
    fig["config"]["displayModeBar"] = True
    if isinstance(element, hv.Histogram):
        # Constrain histogram selection direction to horizontal
        fig["layout"]["selectdirection"] = "h"


IRIS_DATASET = iris()
ACCENT_COLOR = "#E1477E"
OPTS: Dict[str, Dict[str, Any]] = {
    "all": {
        "scatter": {"color": ACCENT_COLOR, "responsive": True, "size": 10},
        "hist": {"color": ACCENT_COLOR, "responsive": True},
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

        self.scatter_panel = pn.pane.HoloViews(sizing_mode="stretch_both")
        self.hist_panel = pn.pane.HoloViews(sizing_mode="stretch_both")
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
        template = FastGridTemplate(title="HoloViews Linked Brushing", row_height=100)
        template.sidebar[:] = [pn.pane.Markdown("## Settings"), self.settings_panel]
        template.main[0:4, :] = APPLICATION.intro_section()
        template.main[4:8, :] = pn.Column(self.scatter_panel, sizing_mode="stretch_both")
        template.main[8:12, :] = pn.Column(self.hist_panel, sizing_mode="stretch_both")

        if "dark" in str(template.theme).lower():
            self._theme = "dark"
        else:
            self._theme = "default"

        return template

    @param.depends("backend", watch=True)
    def _update_plot_panels(self, *_):
        backend = self.backend.lower()
        hv.extension(backend)
        if backend == "plotly":
            if self._theme == "dark":
                pio.templates.default = "plotly_dark"
            else:
                pio.templates.default = "plotly_white"
        scatter, hist = _get_linked_plots(backend)
        self.scatter_panel.object = scatter
        self.hist_panel.object = hist


@site.add(APPLICATION)
def view():
    """Returns the view of the LinkedBrushingApp for use in the site"""
    pn.config.sizing_mode = "stretch_width"
    return LinkedBrushingApp().view


if __name__.startswith("bokeh"):
    # Enables running the app via the command
    # python -m panel serve 'application\pages\linked_selections.py' --dev
    view().servable()
