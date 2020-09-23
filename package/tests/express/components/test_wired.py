"""Test of the wired components"""
# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
import datetime as dt
from collections import OrderedDict

import panel as pn
import pytest

from awesome_panel.express.components import wired


def test_base():
    base = wired.WiredBase()

    assert not base.disabled
    assert "disabled" in base._child_parameters()


def test_button_constructor():
    button = wired.Button()

    # pylint: disable=unsupported-membership-test
    assert "disabled" in button.attributes_to_watch
    assert "elevation" in button.attributes_to_watch
    assert "name" in button.parameters_to_watch
    # pylint: enable=unsupported-membership-test

    assert button.html.startswith("<wired-button")
    assert button.html.endswith("</wired-button>")
    assert 'elevation="0"' in button.html
    assert "disabled" not in button.html


def test_button_disabled():
    button = wired.Button()

    # When/Then
    button.disabled = True
    assert button.attributes_last_change == {"disabled": ""}
    button.update_html_from_attributes_to_watch()
    assert "disabled" in button.html

    # When/Then
    button.disabled = False
    assert button.attributes_last_change == {"disabled": None}
    button.update_html_from_attributes_to_watch()
    assert "disabled" not in button.html


def test_button_elevation():
    button = wired.Button()
    # When/Then: Elevation
    button.elevation = 1
    assert button.attributes_last_change == {"elevation": "1"}


def test_button_name():
    button = wired.Button()
    # When/ Then
    button.name = "Click Test"
    assert ">Click Test</wired-button" in button.html


@pytest.mark.parametrize(
    ["value", "expected"],
    [
        (dt.date(2020, 5, 3), "May 3, 2020"),
        (dt.date(2020, 5, 13), "May 13, 2020"),
    ],
)
def test_datepicker_to_string(value, expected):
    assert wired.DatePicker._to_string(value) == expected


def test_datepicker():
    calendar = wired.DatePicker()

    calendar.selected = "Jul 4, 2019"
    assert calendar.value == dt.date(2019, 7, 4)

    calendar.value = dt.date(2020, 5, 3)
    assert calendar.selected == "May 3, 2020"

    calendar.firstdate = "Jul 14, 2019"
    assert calendar.start == dt.date(2019, 7, 14)

    calendar.start = dt.date(2020, 5, 13)
    assert calendar.firstdate == "May 13, 2020"

    calendar.lastdate = "May 31, 2021"
    assert calendar.end == dt.date(2021, 5, 31)

    calendar.end = dt.date(2021, 10, 28)
    assert calendar.lastdate == "Oct 28, 2021"


def test_checkbox():
    checkbox = wired.Checkbox(name="Test CheckBox")

    assert "disabled" in checkbox.attributes_to_watch
    assert checkbox.html.startswith("<wired-checkbox")
    assert checkbox.html.endswith("</wired-checkbox>")

    # When/Then
    checkbox.disabled = True
    assert checkbox.attributes_last_change == {"disabled": ""}
    checkbox.update_html_from_attributes_to_watch()
    assert "disabled" in checkbox.html

    # When/Then
    checkbox.disabled = False
    assert checkbox.attributes_last_change == {"disabled": None}
    checkbox.update_html_from_attributes_to_watch()
    assert "disabled" not in checkbox.html


def test_checkbox_constructor_checked():
    checkbox = wired.Checkbox(value=True)
    assert checkbox.properties_last_change == {"checked": True}


def test_checkbox_name():
    checkbox = wired.Checkbox()

    checkbox.name = "Testing"
    assert ">Testing<" in checkbox.html


def test_dialog():
    dialog = wired.Dialog(text="a")

    # When/ Then
    assert dialog.text == "a"
    assert dialog.html == "<wired-dialog>a</wired-dialog>"

    # When/ Then
    dialog.text = "b"
    assert dialog.html == "<wired-dialog>b</wired-dialog>"


def test_fab():
    fab = wired.Fab(icon="fast_rewind")

    # When/ Then
    assert fab.icon == "fast_rewind"
    assert fab.html == "<wired-fab><mwc-icon>fast_rewind</mwc-icon></wired-fab>"

    # When/ Then
    fab.icon = "favorite"
    assert fab.html == "<wired-fab><mwc-icon>favorite</mwc-icon></wired-fab>"


def test_icon_button():
    icon = wired.IconButton(icon="fast_rewind")

    # When/ Then
    assert icon.icon == "fast_rewind"
    assert icon.html == "<wired-icon-button><mwc-icon>fast_rewind</mwc-icon></wired-icon-button>"

    # When/ Then
    icon.icon = "favorite"
    assert icon.html == "<wired-icon-button><mwc-icon>favorite</mwc-icon></wired-icon-button>"


def test_float_slider():
    # When/ Then
    slider = wired.FloatSlider(attributes_to_watch={"value": "value"})
    slider.html = (
        '<wired-slider id="slider" value="40.507407407407406" knobradius="15" '
        'class="wired-rendered" style="margin: 0px"></wired-slider>'
    )
    assert slider.value == 40.507407407407406


def test_int_slider():
    # When/ Then
    slider = wired.IntSlider(attributes_to_watch={"value": "value"})
    slider.html = (
        '<wired-slider id="slider" value="2" knobradius="15" class="wired-rendered" '
        'style="margin: 0px"></wired-slider>'
    )
    assert slider.value == 2


def test_int_slider_properties_last_change():
    slider = wired.IntSlider()

    # When/ Then
    slider.properties_last_change = {"input.value": "13"}
    assert slider.value == 13


def test_float_slider_properties_last_change():
    slider = wired.FloatSlider()

    # When/ Then
    slider.properties_last_change = {"input.value": "13.7"}
    assert slider.value == 13.7


def test_input():
    # Given
    wired_input = wired.TextInput()

    # When/ Then
    wired_input.type_ = "password"
    assert wired_input.attributes_last_change == {"type": "password"}
    wired_input.update_html_from_attributes_to_watch()
    assert "password" in wired_input.html


def test_progress():
    progress = wired.Progress(value=4, max=9)

    # Then
    assert progress.value == 4
    assert progress.max == 9
    assert progress.param.value.bounds == (0, 9)

    # # When/ Then
    progress.max = 5
    assert progress.value == 4
    assert progress.max == 5
    assert progress.param.value.bounds == (0, 5)


def test_searchinput():
    # Given
    search = wired.SearchInput()
    # When/ Then
    search.placeholder = "New Search"
    assert search.attributes_last_change == {"placeholder": "New Search"}
    search.disabled = True
    assert search.attributes_last_change == {"disabled": ""}
    search.autocomplete = "on"
    assert search.attributes_last_change == {"autocomplete": "on"}
    search.update_html_from_attributes_to_watch()
    assert search.html == (
        '<wired-search-input placeholder="New Search" autocomplete="on" '
        "disabled></wired-search-input>"
    )


def test_select():
    """Supports dict."""
    options = OrderedDict([("red", "red"), ("yellow", "yellow"), ("green", "green")])
    wired.Select(options=options)


def test_select_something():
    component = wired.Select(value="a", options=["a"])
    pn.Param(component, parameters=["options"])


def test_text_area():
    # When/ Then
    text_area = wired.TextAreaInput(placeholder="a", rows=3)
    assert text_area.html == '<wired-textarea placeholder="a"></wired-textarea>'

    # When/ Then
    text_area.placeholder = "b"
    assert text_area.attributes_last_change == {"placeholder": "b"}


def test_link():
    # Given
    wired_link = wired.Link(href="www.google.com", target="_blank", text="link")

    # Then
    assert wired_link.href == "www.google.com"
    assert wired_link.target == "_blank"
    assert wired_link.text == "link"
    assert wired_link.html == '<wired-link href="www.google.com" target="_blank">link</wired-link>'

    # When/ Then
    wired_link.text = "another link"
    assert wired_link.href == "www.google.com"
    assert wired_link.target == "_blank"
    assert wired_link.text == "another link"
    assert (
        wired_link.html
        == '<wired-link href="www.google.com" target="_blank">another link</wired-link>'
    )


def test_toggle():
    # When/ Then
    toggle = wired.Toggle()
    assert toggle.html == "<wired-toggle></wired-toggle>"
    assert toggle.disabled is False


def test_literal_input_value_from_client():
    # Given
    literal_input = wired.LiteralInput()
    # When
    literal_input.properties_last_change = {"textInput.value": "{'2': 2, 'b': 18}"}
    # Then
    assert literal_input.value == {"2": 2, "b": 18}


def test_literal_input_value_to_client():
    # Given
    literal_input = wired.LiteralInput()
    # When
    literal_input.value = {"2": 2, "b": 18}
    # Then
    assert literal_input.properties_last_change == {"textInput.value": "{'2': 2, 'b': 18}"}
