"""Panel does not have a pane for code. I've created a `Code` pane in the
[`awesome_panel_extensions`](https://pypi.org/project/awesome-panel-extensions/) package"""

from awesome_panel_extensions.pane import Code
import panel as pn
from awesome_panel.express.testing import TestApp

from application.config import site

APPLICATION = site.create_application(
    url="code-pane",
    name="Code Pane",
    author="Marc Skov Madsen",
    description=__doc__,
    thumbnail_url="test_code.png",
    documentation_url="",
    code_url="awesome_panel_express_tests/test_code.py",
    gif_url="",
    mp4_url="",
    tags=[
        "awesome-panel-extensions", "Pane"
    ],
)

def test_code():
    """A manual test of the Code pane.

    We expect to see nicely formatted Python code inside a gray box."""

    code = """\
def my_add(a,b):
    return a+b
"""

    return TestApp(
        test_code,
        Code(
            code,
            language="python",
        ),
        sizing_mode="stretch_width",
    )

@site.add(APPLICATION)
def view() -> pn.Column:
    """Wraps all tests in a Column that can be included in the Gallery or served independently

    Returns:
        pn.Column -- A Column containing all the tests
    """
    pn.config.sizing_mode="stretch_width"
    main = [
        APPLICATION.intro_section(),
        test_code(),
    ]
    return site.create_template(title="Test Code", main=main)


if __name__.startswith("bokeh"):
    view().servable("test_code")
