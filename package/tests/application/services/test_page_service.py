# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring

from awesome_panel.application.models import Page
from awesome_panel.application.services import PageService


def test_can_construct_page_service(page_service):
    assert hasattr(page_service, "pages")
    assert hasattr(page_service, "default_page")


def test_can_create_page(page):
    # Given
    page_service = PageService()
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


def test_can_bulk_create_and_is_sorted():
    # Given
    page_service = PageService()
    page_a = Page(name="a", url="", github_url="", github_avatar_url="")
    page_b = Page(name="b", url="", github_url="", github_avatar_url="")
    page_c = Page(name="c", url="", github_url="", github_avatar_url="")
    page_service.create(page_b)
    pages = [page_a, page_c]
    # When
    page_service.bulk_create(pages)
    actual = page_service.pages
    # Then
    assert actual == [page_a, page_b, page_c]


def test_can_load_default_page(page_service, gallery_page):
    # Given
    page_service.page = gallery_page
    # When
    page_service.load_default_page()
    # Then
    assert page_service.page == page_service.default_page
