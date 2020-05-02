"""Test of the services functionality"""
from awesome_panel.utils import module_to_github_url


def test_module_to_github_url():
    """As a GalleryButton I need functionality to get link to page module"""
    # When
    actual = module_to_github_url.module_to_github_url(module_to_github_url)
    # Then
    assert actual == (
        "https://github.com/MarcSkovMadsen/awesome-panel/blob/master/"
        "package/awesome_panel/utils/module_to_github_url.py"
    )
