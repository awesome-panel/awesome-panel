"""Here we test the functionality of font awesome"""
# pylint: disable=protected-access
import pathlib

import pytest

from awesome_panel.express import fontawesome

OUT = pathlib.Path(__file__).parent / "out"


def test_get_fontawesome_panel_express_css():
    "Test that get_fontawesome_panel_express can return a text string without error"
    # When
    actual = fontawesome.fontawesome.get_fontawesome_panel_express()
    # Then
    assert actual
    assert fontawesome.fontawesome._FONTAWESOME_PANEL_EXPRESS_HEADER in actual
    assert 'div.bk.pa-bus div.bk *::before{content:"\\f207"}' in actual

    with open(
        OUT / "test_fontawesome_panel_express.css",
        "w",
    ) as file:
        file.write(actual)


@pytest.mark.parametrize(
    [
        "css",
        "expected",
    ],
    [
        (
            r'.fa-bus:before{content:"\f207"}.fa-bus-alt:before{content:"\f55e"}',
            'div.bk.pa-bus div.bk *::before{content:"\\f207"}\ndiv.bk.pa-bus-alt div.bk *::before'
            '{content:"\\f55e"}',
        ),
    ],
)
def test__to_fontawesome_panel_express_css(
    css,
    expected,
):
    "Test that _to_fontawesome_panel_express can return a text string without error"
    # When
    actual = fontawesome.fontawesome._to_fontawesome_panel_express(css)
    # Then

    assert actual == fontawesome.fontawesome._FONTAWESOME_PANEL_EXPRESS_HEADER + expected
