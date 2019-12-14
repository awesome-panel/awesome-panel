"""Test of the models"""
# pylint: disable=redefined-outer-name,protected-access
import pytest

from awesome_panel.shared.models import Author, Resource, Tag


@pytest.fixture
def tag() -> Tag:
    """Tag fixture"""
    return Tag(name="new tag")


@pytest.fixture
def author() -> Author:
    """Author fixture"""
    return Author(
        name="Marc Skov Madsen",
        url="https://datamodelsanalytics.com",
        github_url="https://github.com/marcskovmadsen",
        github_avatar_url="https://avatars0.githubusercontent.com/u/42288570",
    )


@pytest.fixture
def resource(author, tag) -> Resource:
    """Resource fixture"""
    return Resource(
        name="awesome-panel.org",
        url="https://awesome-panel.org",
        is_awesome=True,
        tags=[tag],
        author=author,
    )


def test_tag__init__(tag):
    """Test Tag __init__"""
    assert tag.name == "new tag"


def test_tag__str__(tag):
    """Test Tag __str__"""
    assert str(tag) == "new tag"


def test_author__init__(author):
    """Test Author __init__"""
    assert author.name == "Marc Skov Madsen"
    assert author.url == "https://datamodelsanalytics.com"
    assert author.github_url == "https://github.com/marcskovmadsen"
    assert author.github_avatar_url == "https://avatars0.githubusercontent.com/u/42288570"


def test_author__str__(author):
    """Test Author __str__"""
    assert str(author) == "Marc Skov Madsen"


def test_resource__init__(resource, author, tag):
    """Test Resource __init__"""
    assert resource.name == "awesome-panel.org"
    assert resource.url == "https://awesome-panel.org"
    assert resource.is_awesome
    assert resource.tags == [tag]
    assert resource.author == author


def test_resource__str__(resource):
    """test of resource.__str__ method"""
    assert str(resource) == resource.name


def test_resource_to_markdown_bullet(resource):
    """I can convert a resource to a a markdown bullet string"""
    assert resource.to_markdown_bullet() == (
        "- [awesome-panel.org](https://awesome-panel.org) by "
        "[Marc Skov Madsen](https://datamodelsanalytics.com) (#new tag)"
    )


def test_screenshot_file(resource):
    """test of resource.screenshot_file"""
    # When:
    resource.name = "Hello-panel deployed on Glitch"
    # Then:
    assert resource.screenshot_file == "hello-panel-deployed-on-glitch.png"
