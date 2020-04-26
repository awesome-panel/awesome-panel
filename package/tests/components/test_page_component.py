## # pylint: disable=redefined-outer-name,protected-access, missing-function-docstring
from awesome_panel.components import PageComponent

def test_can_construct_page_component(page_component):
    assert isinstance(page_component, PageComponent)
    assert callable(page_component.view)