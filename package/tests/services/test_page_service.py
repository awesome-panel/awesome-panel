# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
import pytest

from awesome_panel.models import Page
from awesome_panel.services.page_service import PageService


@pytest.fixture
def page_service():
    return PageService()

def test_can_construct_page_service(page_service):
    assert hasattr(page_service, "pages")
    assert hasattr(page_service, "default_page")

    assert page_service.default_page
    assert page_service.default_page in page_service.pages

def test_can_create_page(page_service, page):
    # Given
    assert page not in page_service.pages
    # When
    page_service.create(page)
    # Then
    assert page in page_service.pages

def test_can_read_page_by_name(page_service, page):
    # Given
    name = page.name
    page_service.create(page)
    # When
    actual = page_service.read(name)
    # Then
    assert actual == page

def test_can_delete_page(page_service, page):
    # When
    page_service.create(page)
    page_service.delete(page)
    # Then
    assert page not in page_service.pages

def test_can_bulk_create_and_is_sorted(page_service):
    # Given
    page_a = Page(name="a", url="", github_url="", github_avatar_url="")
    page_b = Page(name="b", url="", github_url="", github_avatar_url="")
    page_c = Page(name="c", url="", github_url="", github_avatar_url="")
    page_service.create(page_b)
    pages = [page_a, page_c]
    # When
    page_service.bulk_create(pages)
    actual = page_service.pages
    # Then
    assert actual == [page_a, page_b, page_c, page_service.default_page]

def test_a_common_page_service_exists():
    # pylint: disable=import-outside-toplevel, unused-import
    from awesome_panel.services import PAGE_SERVICE
