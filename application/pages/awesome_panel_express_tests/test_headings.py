"""We test the `Title`, `Header` and `Subheader` functionality provided by
`awesome_panel.express`"""
import panel as pn

import awesome_panel.express as pnx
from awesome_panel.express.testing import TestApp


def test_headings():
    """We test that we can show

    - headers: title, header, subheader
    - aligned: left, center"""
    return TestApp(
        test_headings,
        pnx.Title("Title Left"),
        pnx.Header("Header Left"),
        pnx.SubHeader("SubHeader Left"),
        pnx.Title(
            "Title Center",
            text_align="center",
        ),
        pnx.Header(
            "Header Center",
            text_align="center",
        ),
        pnx.SubHeader(
            "SubHeader Center",
            text_align="center",
        ),
        sizing_mode="stretch_width",
    )


def test_title_centered_white():
    """We test that we can show a centered Title, Header and SubHeader with a white text color"""
    return TestApp(
        test_title_centered_white,
        pnx.Title(
            "Title Center",
            text_align="center",
            style={"color": "white"},
        ),
        pnx.Header(
            "Header Center",
            text_align="center",
            style={"color": "white"},
        ),
        pnx.SubHeader(
            "SubHeader Center",
            text_align="center",
            style={"color": "white"},
        ),
        sizing_mode="stretch_width",
        background="lightgray",
    )


def test_with_url():
    """We test that we can show a Title with a link"""
    return TestApp(
        test_with_url,
        pnx.Title(
            "Title with url",
            url="https://awesome-panel.org",
        ),
        pnx.Header(
            "Header with url",
            url="https://awesome-panel.org",
        ),
        pnx.SubHeader(
            "SubHeader with url",
            url="https://awesome-panel.org",
        ),
        sizing_mode="stretch_width",
    )


def view() -> pn.Column:
    """Wraps all tests in a Column that can be included in the Gallery or served independently

    Returns:
        pn.Column -- A Column containing all the tests
    """
    return pn.Column(
        pn.pane.Markdown(__doc__),
        test_headings(),
        test_title_centered_white(),
        test_with_url(),
    )


if __name__.startswith("bokeh"):
    view().servable("test_headings")
