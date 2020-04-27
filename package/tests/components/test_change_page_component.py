# pylint: disable=redefined-outer-name,protected-access,missing-function-docstring
import param
from awesome_panel.components import PageComponent
import panel as pn


def test_can_construct_change_page_component(change_page_component, page_component):
    assert change_page_component.page_component == page_component
    assert isinstance(change_page_component.param.page_component, param.ClassSelector)
    assert change_page_component.param.page_component.class_ == PageComponent
    assert change_page_component.view()

def test_text_changes_when_page_component_changes(change_page_component, home_page_component):
    # Given
    text = change_page_component._text.object
    # When
    change_page_component.page_component = home_page_component
    # Then
    assert change_page_component._text.object != text

def test_can_handle_none_page_component(change_page_component):
    # When
    change_page_component.page_component = None
    # Then
    assert change_page_component._text.object == ""

def test_can_show(change_page_component):
    pn.Column(
        change_page_component.view(), width=1000, height=1000, background="gray",
    ).show()
