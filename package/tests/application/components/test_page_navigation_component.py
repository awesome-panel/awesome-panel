from awesome_panel.application.components import PageNavigationComponent

def test_can_construct(page_navigation_component, page_service):
    assert isinstance(page_navigation_component, PageNavigationComponent)
    assert page_navigation_component.page_service == page_service

def test_can_show(page_navigation_component, show=True):
    if show:
        page_navigation_component.show()