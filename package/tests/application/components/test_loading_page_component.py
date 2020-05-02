# pylint: disable=redefined-outer-name,protected-access,missing-function-docstring
import param
from awesome_panel.application.components import LoadingPageComponent, PageComponent
import panel as pn


def test_can_construct_loading_page_component(loading_page_component):
    assert isinstance(loading_page_component, LoadingPageComponent)
    assert issubclass(type(loading_page_component), PageComponent)
    assert loading_page_component.main is not None

def test_can_show(loading_page_component):
    pn.Column(
        loading_page_component.main, width=1000, height=1000, background="gray",
    )

