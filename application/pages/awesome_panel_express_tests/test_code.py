"""Panel does not have a pane for code. I've created a `Code` pane in `awesome_panel.express`"""

import panel as pn

import awesome_panel.express as pnx
from awesome_panel.express.testing import TestApp


def test_code():
    """A manual test of the Code pane.

    We expect to see nicely formatted Python code inside a gray box."""

    code = """\
def my_add(a,b):
    return a+b
"""

    return TestApp(test_code, pnx.Code(code, language="python",), sizing_mode="stretch_width",)


def view() -> pn.Column:
    """Wraps all tests in a Column that can be included in the Gallery or served independently

    Returns:
        pn.Column -- A Column containing all the tests
    """
    return pn.Column(pn.pane.Markdown(__doc__), test_code(),)


if __name__.startswith("bokeh"):
    view().servable("test_code")
