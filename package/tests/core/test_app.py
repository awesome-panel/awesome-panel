"""Test of the core functionality"""
import pytest
from awesome_panel.utils.title_awesome import title_awesome
from panel.layout import Column


@pytest.mark.panel
def test_title_awesome():
    """Test that we can write awesome title with the awesome badge

    - one with additional text
    - one with additional 'Test' text
    """
    title_none = title_awesome("")
    title_test = title_awesome("Test")
    Column(
        title_none,
        title_test,
        sizing_mode="stretch_width",
    ).servable()


if __name__.startswith("bokeh"):
    test_title_awesome()
