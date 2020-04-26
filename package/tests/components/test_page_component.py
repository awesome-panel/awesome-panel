## # pylint: disable=redefined-outer-name,protected-access, missing-function-docstring
from awesome_panel.components import PageComponent
import param
import panel as pn
import pytest


def test_can_construct_page_component(page_component):
    assert isinstance(page_component, PageComponent)
    assert callable(page_component.view)
    assert page_component.name == "Page"


def test_can_create_page_component_from_parameterized_class_with_view():
    # Given
    content = pn.pane.Markdown("Hello World")

    class ParamClassWithView(param.Parameterized):
        def view(self):
            return content

    page = ParamClassWithView()
    # When
    component = PageComponent(name="Hello World Page", page=page)
    # Then
    isinstance(component, PageComponent)
    assert component.view() == page.view()
    assert component.name == "Hello World Page"


@pytest.mark.parametrize(
    ["name", "reactive"],
    [("Page 1", pn.pane.Markdown("# Page 1"),), ("Page 2", pn.Column("# Page 2"),),],
)
def test_can_create_page_component_from_reactive(name, reactive):
    # When
    component = PageComponent(name=name, page=reactive)
    # Then
    isinstance(component, PageComponent)
    assert component.view() == reactive
    assert component.name == name
