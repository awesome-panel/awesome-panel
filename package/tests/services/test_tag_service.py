# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
import pytest

from awesome_panel.models import Tag
from awesome_panel.services.tag_service import TagService


@pytest.fixture
def tag_service():
    return TagService()

def test_can_construct_tag_service(tag_service):
    assert hasattr(tag_service, "tags")

def test_can_create_tag(tag_service, tag):
    # Given
    assert tag not in tag_service.tags
    # When
    tag_service.create(tag)
    # Then
    assert tag in tag_service.tags

def test_can_read_tag_by_name(tag_service, tag):
    # Given
    name = tag.name
    tag_service.create(tag)
    # When
    actual = tag_service.read(name)
    # Then
    assert actual == tag

def test_can_delete_tag(tag_service, tag):
    # When
    tag_service.create(tag)
    tag_service.delete(tag)
    # Then
    assert tag not in tag_service.tags

def test_can_bulk_create_and_is_sorted(tag_service,):
    # Given
    tag_a = Tag(name="a")
    tag_b = Tag(name="b")
    tag_c = Tag(name="c")
    tag_service.create(tag_b)
    tags = [tag_a, tag_c]
    # When
    tag_service.bulk_create(tags)
    actual = tag_service.tags
    # Then
    assert actual == [tag_a, tag_b, tag_c]

def test_a_common_tag_service_exists():
    # pylint: disable=import-outside-toplevel, unused-import
    from awesome_panel.services import TAG_SERVICE
