"""Test of the app services"""
from awesome_panel.core.services import other
from src.pages.gallery.bootstrap_dashboard import main


def test_module_to_github_url():
    """An extrac test of the module_to_github_url function as I had problems making it work"""
    # When
    actual = other.module_to_github_url(main)
    # Then
    assert actual == (
        "https://github.com/MarcSkovMadsen/awesome-panel/blob/master/"
        "src/pages/gallery/bootstrap_dashboard/main.py"
    )
