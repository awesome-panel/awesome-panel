"""Test of the app functionality"""
import pytest
import awesome_panel.app as app
from panel.layout import Column


@pytest.mark.panel
def test_title_awesome():
    """Test that we can write awesome title with the awesome badge

    - one with additional text
    - one with additional 'Test' text
    """
    title_none = app.title_awesome("")
    title_test = app.title_awesome("Test")
    Column(title_none, title_test, sizing_mode="stretch_width").servable()


if __name__.startswith("bk"):
    test_title_awesome()
