# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
from awesome_panel.application.components import PageNavigationComponent


def test_can_construct(page_navigation_component, page_service):
    assert isinstance(page_navigation_component, PageNavigationComponent)
    assert page_navigation_component.page_service == page_service


def test_can_show(page_navigation_component, show=False):
    if show:
        page_navigation_component.show()
