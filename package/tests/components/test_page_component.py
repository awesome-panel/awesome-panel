## # pylint: disable=redefined-outer-name,protected-access, missing-function-docstring
from awesome_panel.components import PageComponent
from awesome_panel.models import Page, Progress, Toast
import param
import panel as pn
import pytest


def test_can_construct_page_component(page_component):
    assert isinstance(page_component, PageComponent)
    assert isinstance(page_component.page, Page)
    assert hasattr(page_component, "main")
    assert hasattr(page_component, "sidebar")
    assert isinstance(page_component.progress, Progress)
    assert isinstance(page_component.toast, Toast)

def test_must_provide_page_on_construction(page_main):
    with pytest.raises(ValueError):
        PageComponent(
            main = page_main
        )