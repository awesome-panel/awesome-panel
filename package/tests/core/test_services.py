"""Test of the services functionality"""
from awesome_panel.core.services import other


def test_module_to_github_url():
    """As a GalleryButton I need functionality to get link to page module"""
    # When
    actual = other.module_to_github_url(other)
    # Then
    assert actual == (
        "https://github.com/MarcSkovMadsen/awesome-panel/blob/master/"
        "package/awesome_panel/core/services/other.py"
    )
