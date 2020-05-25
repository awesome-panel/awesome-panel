"""
# Perspective Viewer

[Perspective](https://github.com/finos/perspective#readme) is an interactive visualization
component for large, real-time datasets. It comes with the `perspective-viewer` web component.

It enables analysts and traders at large banks like J.P.Morgan to understand their data. But it is
also very usefull for analysts, engineers, scientists, data engineers and data scientists in
general.

[Panel](https://panel.holoviz.org/) is a powerfull framework for creating awesome analytics apps
in Python.

In this example we demonstrate how to use the `perspective-viewer` web component with Panel.

If you want Perspective supported in Panel, then go to GitHub and upvote

- [Panel Feature 1107](https://github.com/holoviz/panel/issues/1107): Add Perspective widget.
- [Perspective Feature 942](https://github.com/finos/perspective/issues/942): Enable Perspective in
Panel.
- [Panel PR 1261](https://github.com/holoviz/panel/pull/1261): Perspective-Viewer WebComponent
Example.

**Author:** [Marc Skov Madsen](https://datamodelanalytics.com)
([awesome-panel.org](https://awesome-panel.org))

**Tags:**
[Perspective](https://github.com/finos/perspective#readme),
[Panel](https://panel.holoviz.org/),
[Python](https://www.python.org/)

**Resources:**
[Code](https://github.com/MarcSkovMadsen/awesome-panel/blob/master/application/pages/\
awesome_panel_express_tests/test_perspective.py),
[Data](https://datahub.io/core/s-and-p-500-companies-financials)
"""

import pathlib

import pandas as pd
import panel as pn

from awesome_panel.express.components import PerspectiveViewer

DARK_BACKGROUND = "rgb(42, 44, 47)"
DARK_COLOR = "white"
PERSPECTIVE_LOGO = "https://perspective.finos.org/img/logo.png"
PANEL_LOGO = "https://panel.holoviz.org/_static/logo_horizontal.png"
ROOT = pathlib.Path(__file__).parent
# Source: https://datahub.io/core/s-and-p-500-companies-financials
DATA = ROOT / "PerspectiveViewerData.csv"

dataframe = pd.read_csv(DATA)


def create_app(**params) -> pn.Column:
    """Returns app using PerspectiveViewer

    Returns:
        pn.Column: The app
    """

    perspective_viewer = PerspectiveViewer(sizing_mode="stretch_both", data=dataframe)

    top_app_bar = pn.Row(
        pn.pane.PNG(PERSPECTIVE_LOGO, height=50, margin=(10, 25, 10, 10)),
        # pn.pane.PNG(PANEL_LOGO, height=40, margin=(10, 0, 10, 0)),
        pn.layout.HSpacer(),
        margin=0,
        background=DARK_BACKGROUND,
    )

    settings_parameters = [
        "theme",
        "row_pivots",
        "plugin",
        "columns",
        "aggregates",
        "filters",
        "sort",
        "rows",
        "column_pivots",
    ]

    settings_pane = pn.Param(
        perspective_viewer,
        parameters=settings_parameters,
        width=200,
        sizing_mode="stretch_height",
        background="#9E9E9E",
    )

    return pn.Column(
        pn.pane.Markdown(__doc__),
        top_app_bar,
        pn.Row(
            perspective_viewer,
            pn.layout.VSpacer(width=10),
            settings_pane,
            sizing_mode="stretch_both",
            margin=0,
            background=DARK_BACKGROUND,
        ),
        pn.layout.HSpacer(height=50),
        **params
    )


def view() -> pn.Column:
    """Return a PerspectiveViewer Test App for inclusion in the Gallery at awesome-panel.org

    Returns:
        pn.Column: The app
    """
    return create_app(height=800, sizing_mode="stretch_width")


if __name__.startswith("bokeh"):
    PerspectiveViewer.config()
    view().servable()
