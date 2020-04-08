"""Test of the core functionality"""
import pytest
from panel.layout import Column

import awesome_panel.core as core


@pytest.mark.panel
def test_title_awesome():
    """Test that we can write awesome title with the awesome badge

    - one with additional text
    - one with additional 'Test' text
    """
    title_none = core.title_awesome("")
    title_test = core.title_awesome("Test")
    Column(title_none, title_test, sizing_mode="stretch_width",).servable()


if __name__.startswith("bokeh"):
    test_title_awesome()
