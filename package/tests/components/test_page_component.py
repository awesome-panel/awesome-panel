## # pylint: disable=redefined-outer-name,protected-access, missing-function-docstring
from awesome_panel.components import PageComponent
import param
import panel as pn
import pytest

def test_can_construct_page_component(page_component):
    assert isinstance(page_component, PageComponent)
    assert callable(page_component.view)

def test_can_create_page_component_from_parameterized_class_with_view():
    # Given
    content = pn.pane.Markdown("Hello World")
    class ParamClassWithView(param.Parameterized):
        def view(self):
            return content
    page = ParamClassWithView()
    # When
    component = PageComponent.create(page)
    # Then
    isinstance(component, PageComponent)
    assert component.view() == page.view()

@pytest.mark.parametrize(["reactive"], [
    (pn.pane.Markdown("# Page"), ),
    (pn.Column("# Page"), ),
])
def test_can_create_page_component_from_reactive(reactive):
    # When
    component = PageComponent.create(reactive)
    # Then
    isinstance(component, PageComponent)
    assert component.view() == reactive