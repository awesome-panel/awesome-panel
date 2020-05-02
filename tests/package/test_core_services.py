"""Test of the app services"""
from awesome_panel.core.services import other
from application.pages.bootstrap_dashboard import bootstrap_dashboard


def test_module_to_github_url():
    """An extrac test of the module_to_github_url function as I had problems making it work"""
    # When
    actual = other.module_to_github_url(bootstrap_dashboard)
    # Then
    assert actual == (
        "https://github.com/MarcSkovMadsen/awesome-panel/blob/master/"
        "application/pages/bootstrap_dashboard/bootstrap_dashboard.py"
    )
