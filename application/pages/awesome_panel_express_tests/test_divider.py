"""This test is here for legacy reasons. Originally the `pn.layout.divider` was no documented
so I created my own because I did not know better.

The `pn.layout.divider` reference example is now available
(here)[https://panel.holoviz.org/reference/layouts/Divider.html#layouts-gallery-divider]
"""
import panel as pn

import awesome_panel.express as pnx
from awesome_panel.express.testing import TestApp


def test_divider():
    """A manual test of the horizontal divider stretching to full width"""
    return TestApp(test_divider, pn.layout.Divider())


def view() -> pn.Column:
    """Wraps all tests in a Column that can be included in the Gallery or served independently

    Returns:
        pn.Column -- A Column containing all the tests
    """
    return pn.Column(
        pn.pane.Markdown(__doc__),
        test_divider(),
    )


if __name__.startswith("bokeh"):
    pn.config.sizing_mode = "stretch_width"

    view().servable("test_divider")
