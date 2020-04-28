from awesome_panel.models import Page, Resource

def test_can_construct_page(page):
    assert issubclass(type(page), Resource)
    assert isinstance(page.description, str)

