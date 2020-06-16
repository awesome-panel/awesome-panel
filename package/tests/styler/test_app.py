# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
from awesome_panel.styler.app import (
    InfoCard,
    PrettyContainer,
    PRETTY_CONTAINER_CSS_CLASS,
    PRETTY_CONTAINER_MARGIN,
)
import panel as pn
import pytest

# from awesome_panel.styler.app import AppBar InfoCard, PrettyContainer, SettingsContainer


@pytest.fixture
def info_card():
    return InfoCard(value=62000, text="Downloads", background="white", color="black")


@pytest.fixture
def pretty_container():
    return PrettyContainer("Test")


def test_pretty_container_can_be_constructed(pretty_container):
    assert isinstance(pretty_container, pn.Column)
    assert PRETTY_CONTAINER_CSS_CLASS in pretty_container.css_classes
    assert pretty_container.margin == PRETTY_CONTAINER_MARGIN
    assert pretty_container.sizing_mode == "stretch_both"


def test_info_card_can_be_constructed(info_card):
    assert isinstance(info_card, PrettyContainer)
    assert info_card.value == 62000
    assert info_card.text == "Downloads"


def test_info_card_get_text():
    expected = """\
#### 62000

Downloads
"""
    assert InfoCard._get_text(62000, "Downloads") == expected
