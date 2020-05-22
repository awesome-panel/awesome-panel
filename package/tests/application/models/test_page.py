# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
from awesome_panel.application.models import Author, Page


def test_can_construct_page(page):
    assert issubclass(type(page), Page)
    assert isinstance(page.name, str)
    assert isinstance(page.description, str)
    assert isinstance(page.author, Author)
    assert isinstance(page.description, str)
    assert isinstance(page.tags, list)
    assert isinstance(page.source_code_url, str)
    assert isinstance(page.thumbnail_png_url, str)
    assert hasattr(page, "component")
    assert page.show_loading_page is False
    assert page.restrict_max_width is True
