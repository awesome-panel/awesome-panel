"""The module tests the improved headings classes"""
import panel as pn
import pytest

import awesome_panel.express as pnx


@pytest.mark.panel
def test_headings():
    """## test_headings

We test that we can show

- headers: title, header, subheader
- aligned: left, center
"""
    app = pn.Column(
        pn.pane.Markdown(test_headings.__doc__),
        pnx.Title("Title Left"),
        pnx.Header("Header Left"),
        pnx.SubHeader("SubHeader Left"),
        pnx.Title("Title Center", text_align="center"),
        pnx.Header("Header Center", text_align="center"),
        pnx.SubHeader("SubHeader Center", text_align="center"),
        sizing_mode="stretch_width",
        background="lightgray",
    )
    app.servable(test_headings.__name__)


@pytest.mark.panel
def test_title_centered_white():
    """## test_title_centered_white

We test that we can show a centered Title, Header and SubHeader with a white text color
"""
    app = pn.Column(
        pn.pane.Markdown(test_title_centered_white.__doc__),
        pnx.Title("Title Center", text_align="center", style={"color": "white"}),
        pnx.Header("Header Center", text_align="center", style={"color": "white"}),
        pnx.SubHeader("SubHeader Center", text_align="center", style={"color": "white"}),
        sizing_mode="stretch_width",
        background="lightgray",
    )
    app.servable(test_title_centered_white.__name__)


@pytest.mark.panel
def test_with_url():
    """## test_with_url

We test that we can show a Title with a link
"""
    app = pn.Column(
        pn.pane.Markdown(test_with_url.__doc__),
        pnx.Title("Title with url", url="https://awesome-panel.org"),
        pnx.Header("Header with url", url="https://awesome-panel.org"),
        pnx.SubHeader("SubHeader with url", url="https://awesome-panel.org"),
        sizing_mode="stretch_width",
        background="lightgray",
    )
    app.servable(test_with_url.__name__)


if __name__.startswith("bk"):
    test_headings()
    test_title_centered_white()
    test_with_url()
