"""[Perspective](https://github.com/finos/perspective#readme) is an interactive visualization
component for large, real-time datasets. It enables analysts and traders at large banks like
J.P.Morgan to understand their data in real time.

Panel provides the [`Perspective`](https://panel.holoviz.org/reference/panes/Perspective.html) pane
which was first contributed by awesome-panel.org and then further improved by Philipp.
"""

import pathlib

import pandas as pd
import panel as pn
from panel.pane import Perspective

from awesome_panel import config
from awesome_panel.assets.csv import PERSPECTIVE_VIEWER_DATA_PATH

DARK_BACKGROUND = "rgb(42, 44, 47)"
DARK_COLOR = "white"
PERSPECTIVE_LOGO = (
    "https://github.com/finos/perspective/raw/master/docs/static/img/logo/logo-light.png?raw=true"
)
PANEL_LOGO = "https://panel.holoviz.org/_static/logo_horizontal.png"
ROOT = pathlib.Path(__file__).parent
# Source: https://datahub.io/core/s-and-p-500-companies-financials
DATA = ROOT / "PerspectiveViewerData.csv"
# pylint: disable=line-too-long
VIDEO = """<iframe width="100%" height="400" src="https://www.youtube.com/embed/IO-HJsGdleE" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>"""
# pylint: enable=line-too-long
INFO = """**You can also use the `Perspective` pane in your apps**. For more
inspiration check out the [Perspective Reference Guide]\
(https://panel.holoviz.org/reference/panes/Perspective.html) or the video below.
"""

COLUMNS = [
    "Name",
    "Symbol",
    "Sector",
    "Price",
    "Price/Earnings",
    "Dividend Yield",
    "Earnings/Share",
    "52 Week Low",
    "52 Week High",
    "Market Cap",
    "EBITDA",
    "Price/Sales",
    "Price/Book",
    "SEC Filings",
]


@config.cached
def get_data() -> pd.DataFrame:
    """Returns data for the Perspective app

    Returns:
        pd.DataFrame: Data
    """
    return pd.read_csv(PERSPECTIVE_VIEWER_DATA_PATH)[COLUMNS]


DATA = get_data()


def main(theme: str) -> pn.Column:
    """Returns the main app components

    Returns:
        pn.Column: The main app components
    """
    if "dark" in theme:
        background = DARK_BACKGROUND
        theme = "material-dark"
    else:
        background = "white"
        theme = "material"
    perspective_viewer = Perspective(
        object=DATA, columns=COLUMNS, theme=theme, sizing_mode="stretch_both"
    )

    top_app_bar = pn.Row(
        pn.pane.PNG(
            PERSPECTIVE_LOGO,
            link_url="https://perspective.finos.org",
            height=50,
            margin=(10, 25, 10, 10),
        ),
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
    )
    return pn.Column(
        pn.Column(
            top_app_bar,
            pn.Row(
                perspective_viewer,
                pn.layout.VSpacer(width=10),
                settings_pane,
                sizing_mode="stretch_both",
                background=background,
                margin=0,
            ),
        ),
        pn.pane.Alert(INFO, margin=0),
        pn.Column(
            pn.pane.HTML(VIDEO),
        ),
    )


if __name__.startswith("bokeh"):
    config.extension("perspective", url="perspective")

    for component in main(theme=config.get_theme()):
        component.servable()
