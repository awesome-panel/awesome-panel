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

from application.config import site

DARK_BACKGROUND = "rgb(42, 44, 47)"
DARK_COLOR = "white"
PERSPECTIVE_LOGO = "https://perspective.finos.org/img/logo.png"
PANEL_LOGO = "https://panel.holoviz.org/_static/logo_horizontal.png"
ROOT = pathlib.Path(__file__).parent
# Source: https://datahub.io/core/s-and-p-500-companies-financials
DATA = ROOT / "PerspectiveViewerData.csv"
VIDEO = """<iframe width="100%" height="400" src="https://www.youtube.com/embed/IO-HJsGdleE" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>"""
INFO = """**You can also use the `Perspective` pane in your apps**. Check out the [Perspective Reference Guide]\
(https://panel.holoviz.org/reference/panes/Perspective.html) or the video below.
"""

APPLICATION = site.create_application(
    url="perspective",
    name="Perspective Viewer",
    author="Marc Skov Madsen",
    introduction="""Demonstrates that you can use the awesome Perspective pane""",
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
    """Returns app using Perspective

    Returns:
        pn.Column: The app
    """
    pn.config.sizing_mode = "stretch_width"
    template = site.create_template(title="Test Perspective")
    if "dark" in str(template.theme).lower():
        background = DARK_BACKGROUND
        theme = "material-dark"
    else:
        background = "white"
        theme = "material"
    perspective_viewer = Perspective(
        object=DATAFRAME, columns=COLUMNS, theme=theme, sizing_mode="stretch_both"
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
    template.main[:] = [
        APPLICATION.intro_section(),
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
    ]
    return template


@site.add(APPLICATION)
def view() -> pn.Column:
    """Return a Perspective Test App for inclusion in the Gallery at awesome-panel.org

    Returns:
        pn.Column: The app
    """
    return create_app()


if __name__.startswith("bokeh"):
    pn.extension("perspective")
    view().servable()
