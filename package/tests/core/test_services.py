"""Test of the services functionality"""
from awesome_panel.core import services
from awesome_panel.shared.models import Author


def test_module_to_github_url():
    """As a GalleryButton I need functionality to get link to page module"""
    # When
    actual = services.module_to_github_url(services)
    # Then
    assert actual == (
        "https://github.com/MarcSkovMadsen/awesome-panel/blob/master/"
        "package/awesome_panel/core/services.py"
    )


def test_author_to_github_link_with_image():
    """On the Gallery App Page I need functionality to show and link to the Author"""
    # Given
    author = Author(
        name="Marc Skov Madsen",
        url="https://datamodelsanalytics.com",
        github_url="https://github.com/marcskovmadsen",
        github_avatar_url="https://avatars0.githubusercontent.com/u/42288570",
    )
    # When
    actual = services.author_to_github_link_with_image(author)
    # Then
    assert actual == (
        '<a href="https://github.com/marcskovmadsen" target="_blank">'
        '<img src="https://avatars0.githubusercontent.com/u/42288570" title="Marc Skov Madsen">'
        "</img></a>"
    )

