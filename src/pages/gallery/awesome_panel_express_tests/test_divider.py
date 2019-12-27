"""Here we test the Divider provided by `awesome_panel.express`."""
import panel as pn

import awesome_panel.express as pnx
from awesome_panel.express.testing import TestApp


def test_divider():
    """A manual test of the horizontal divider stretching to full width"""
    return TestApp(test_divider, pnx.Divider(), sizing_mode="stretch_width")


def view() -> pn.Column:
    """Wraps all tests in a Column that can be included in the Gallery or served independently

    Returns:
        pn.Column -- A Column containing all the tests
    """
    return pn.Column(pnx.Markdown(__doc__), test_divider())


if __name__.startswith("bk"):
    view().servable("test_divider")
