"""Tests of the material components"""
# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
import param
import pytest

from awesome_panel.express.components.material import MWCSelect


class ParameterizedMock(param.Parameterized):
    pass


def test_mwc_select_fixture(mwc_select):
    assert isinstance(mwc_select, MWCSelect)


@pytest.mark.parametrize(
    ["options"],
    [
        (["a", "b", "c"],),
        ({"a": "aaa", "b": "bbb", "c": "ccc"},),
    ],
)
def test_mwc_select_can_set_value(options):
    # Given
    mwc_select = MWCSelect(options=options)
    # When
    mwc_select.value = "b"
    # Then
    assert mwc_select._index == "1"


@pytest.mark.parametrize(
    ["options"],
    [
        (["a", "b", "c"],),
        ({"a": "aaa", "b": "bbb", "c": "ccc"},),
    ],
)
def test_mwc_select_can_get_value(options):
    # Given
    mwc_select = MWCSelect(options=options)
    # When
    mwc_select._index = "1"
    # Then
    assert mwc_select.value == "b"


@pytest.mark.parametrize(
    ["options", "expected"],
    [
        (["a"], '<mwc-select><mwc-list-item value="0">a</mwc-list-item></mwc-select>'),
        ({"a": "aaa"}, '<mwc-select><mwc-list-item value="0">aaa</mwc-list-item></mwc-select>'),
        (
            [ParameterizedMock(name="abc")],
            '<mwc-select><mwc-list-item value="0">abc</mwc-list-item></mwc-select>',
        ),
    ],
)
def test_mwc_select_can_format_options(options, expected):
    # Given
    mwc_select = MWCSelect()
    # When
    actual = mwc_select._get_html_from_parameters_to_watch(options=options)
    # Then
    assert actual == expected
