# pylint: disable=redefined-outer-name,protected-access,missing-function-docstring
import param
from awesome_panel.components import PageComponent
import panel as pn


def test_can_construct_loading_page_component(loading_page_component, page_component):
    assert loading_page_component.page_component == page_component
    assert isinstance(loading_page_component.param.page_component, param.ClassSelector)
    assert loading_page_component.param.page_component.class_ == PageComponent
    assert loading_page_component.view()

def test_can_show(loading_page_component):
    pn.Column(
        loading_page_component.view(), width=1000, height=1000, background="gray",
    )
