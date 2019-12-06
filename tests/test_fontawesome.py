"""Here we test the functionality of font awesome"""
# pylint: disable=protected-access
import pathlib

import panel as pn
import pytest

from awesome_panel.express import fontawesome
from awesome_panel.express._pane._panes import Markdown

fontawesome.extend()

OUT = pathlib.Path(__file__).parent / "out"


@pytest.mark.panel
def test_html_with_font_awesome():
    """## test_html_with_font_awesome

    Manual test of a HTML with font awesome icons"""
    text = """
    <ul style="margin: 0;">
        <li><i class="fas fa-user"></i> Login</li>
        <li><i class="fas fa-newspaper"></i> TPS Reports</li>
        <li><i class="fab fa-twitter"></i> Twitter</li>
    </ul>


    """
    html = pn.pane.HTML(text, sizing_mode="stretch_width")
    app = pn.Column(Markdown(test_html_with_font_awesome.__doc__), html)
    app.servable()


@pytest.mark.panel
def test_button_with_font_awesome():
    """## test_button_with_font_awesome

    Manual test of a buttons with a font awesome icons"""
    button_user = pn.widgets.Button(name=" User", css_classes=["pa-login"],)
    button_newspaper = pn.widgets.Button(name=" News Paper", css_classes=["pa-tps"],)
    button_twitter = pn.widgets.Button(name=" Twitter", css_classes=["pa-twitter"],)

    app = pn.Column(
        Markdown(test_button_with_font_awesome.__doc__),
        button_user,
        button_newspaper,
        button_twitter,
    )
    app.servable()


def test_get_fontawesome_panel_express_css():
    "Test that get_fontawesome_panel_express can return a text string without error"
    # When
    actual = fontawesome.fontawesome.get_fontawesome_panel_express()
    # Then
    assert actual
    assert fontawesome.fontawesome._FONTAWESOME_PANEL_EXPRESS_HEADER in actual
    assert 'div.bk.pa-bus div.bk *::before{content:"\\f207"}' in actual

    with open(OUT / "test_fontawesome_panel_express.css", "w") as file:
        file.write(actual)


@pytest.mark.parametrize(
    ["css", "expected"],
    [
        (
            r'.fa-bus:before{content:"\f207"}.fa-bus-alt:before{content:"\f55e"}',
            'div.bk.pa-bus div.bk *::before{content:"\\f207"}\ndiv.bk.pa-bus-alt div.bk *::before{content:"\\f55e"}',
        ),
    ],
)
def test__to_fontawesome_panel_express_css(css, expected):
    "Test that _to_fontawesome_panel_express can return a text string without error"
    # When
    actual = fontawesome.fontawesome._to_fontawesome_panel_express(css)
    # Then

    assert actual == fontawesome.fontawesome._FONTAWESOME_PANEL_EXPRESS_HEADER + expected


if __name__.startswith("bk"):
    test_html_with_font_awesome()
    test_button_with_font_awesome()
