"""Test of the app services"""
from gallery.bootstrap_dashboard import main
from awesome_panel.app import services


def test_module_to_github_url():
    # When
    actual = services.module_to_github_url(main)
    # Then
    assert actual == (
        "https://github.com/MarcSkovMadsen/awesome-panel/blob/master/"
        "gallery/bootstrap_dashboard/main.py"
    )
