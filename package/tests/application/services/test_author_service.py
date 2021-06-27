# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
import pytest
from awesome_panel.application.models import Author
from awesome_panel.application.services import AuthorService


@pytest.fixture
def author_service():
    return AuthorService()


def test_can_construct_author_service(author_service):
    assert hasattr(author_service, "authors")
    assert hasattr(author_service, "default_author")

    assert author_service.default_author
    assert author_service.default_author in author_service.authors


def test_can_create_author(author_service, author):
    # Given
    assert author not in author_service.authors
    # When
    author_service.create(author)
    # Then
    assert author in author_service.authors


def test_can_read_author_by_name(author_service, author):
    # Given
    name = author.name
    author_service.create(author)
    # When
    actual = author_service.read(name)
    # Then
    assert actual == author


def test_can_delete_author(author_service, author):
    # When
    author_service.create(author)
    author_service.delete(author)
    # Then
    assert author not in author_service.authors


def test_can_bulk_create_and_is_sorted(author_service):
    # Given
    author_a = Author(name="a", url="", github_url="", github_avatar="")
    author_b = Author(name="b", url="", github_url="", github_avatar="")
    author_c = Author(name="c", url="", github_url="", github_avatar="")
    author_service.create(author_b)
    authors = [author_a, author_c]
    # When
    author_service.bulk_create(authors)
    actual = author_service.authors
    # Then
    assert actual == [author_a, author_b, author_c, author_service.default_author]
