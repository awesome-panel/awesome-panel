"""[Perspective](https://github.com/finos/perspective#readme) is an interactive visualization
component for large, real-time datasets. It enables analysts and traders at large banks like
J.P.Morgan to understand their data in real time.

In this example we demonstrate how to use the `perspective-viewer` web component with Panel.
"""

import pathlib

import pandas as pd
import panel as pn
from awesome_panel_extensions.widgets.perspective_viewer import PerspectiveViewer

from application.config import site

DARK_BACKGROUND = "rgb(42, 44, 47)"
DARK_COLOR = "white"
PERSPECTIVE_LOGO = "https://perspective.finos.org/img/logo.png"
PANEL_LOGO = "https://panel.holoviz.org/_static/logo_horizontal.png"
ROOT = pathlib.Path(__file__).parent
# Source: https://datahub.io/core/s-and-p-500-companies-financials
DATA = ROOT / "PerspectiveViewerData.csv"
VIDEO = """<iframe width="100%" height="400" src="https://www.youtube.com/embed/IO-HJsGdleE" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>"""
INFO = """
**You can also use the `perspective-viewer` component in your apps**. It is a part of the
[`awesome-panel-extensions`](https://pypi.org/project/awesome-panel-extensions/) package.

Checkout the
[Reference Notebook](https://mybinder.org/v2/gh/MarcSkovMadsen/awesome-panel-extensions/master?filepath=examples%2Freference%2Fwidgets%2FPerspectiveViewer.ipynb)
on Binder.

If you want Perspective supported in Panel, then go to GitHub and upvote
[Panel Feature 1107](https://github.com/holoviz/panel/issues/1107),
[Panel PR 1690](https://github.com/holoviz/panel/pull/1690),
[Perspective Feature 942](https://github.com/finos/perspective/issues/942) and
[Panel PR 1261](https://github.com/holoviz/panel/pull/1261)
"""

APPLICATION = site.create_application(
    url="perspective",
    name="Perspective Viewer",
    author="Marc Skov Madsen",
    introduction="""Demonstrates that you can use the awesome PerspectiveViewer with Panel""",
    description=__doc__,
    thumbnail_url="test_perspective.png",
    documentation_url="",
    code_url="awesome_panel_express_tests/test_perspective.py",
    gif_url="",
    mp4_url="",
    tags=["Perspective", "Streaming"],
)
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
DATAFRAME = pd.read_csv(DATA)[COLUMNS]


def create_app(**params) -> pn.Column:
    """Returns app using PerspectiveViewer

    Returns:
        pn.Column: The app
    """
    pn.config.sizing_mode = "stretch_width"
    perspective_viewer = PerspectiveViewer(
        value=DATAFRAME, columns=COLUMNS, theme="material-dark", sizing_mode="stretch_both"
    )

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

    main = [
        APPLICATION.intro_section(),
        pn.pane.Alert(INFO),
        top_app_bar,
        pn.Row(
            perspective_viewer,
            pn.layout.VSpacer(width=10),
            settings_pane,
            sizing_mode="stretch_both",
            margin=0,
            background=DARK_BACKGROUND,
        ),
        pn.Column(
            "For more inspiration checkout",
            pn.pane.HTML(VIDEO),
            pn.layout.HSpacer(height=50),
        ),
    ]
    return site.create_template(title="Test Perspective", main=main)


@site.add(APPLICATION)
def view() -> pn.Column:
    """Return a PerspectiveViewer Test App for inclusion in the Gallery at awesome-panel.org

    Returns:
        pn.Column: The app
    """
    return create_app()


if __name__.startswith("bokeh"):
    pn.extension("perspective")
    view().servable()
