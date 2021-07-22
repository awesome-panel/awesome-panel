"""Panel does not have a pane for code. I've created a `Code` pane in the
[`awesome_panel_extensions`](https://pypi.org/project/awesome-panel-extensions/) package.

Use via

```python
from awesome_panel_extensions.pane import Code
```
"""

import panel as pn
from awesome_panel.express.testing import TestApp
from awesome_panel_extensions.pane import Code
from awesome_panel_extensions.site import site

APPLICATION = site.create_application(
    url="code-pane",
    name="Code Pane",
    author="Marc Skov Madsen",
    description="Demonstrates the Code pane from the awesome-panel-extensions package",
    description_long=__doc__,
    thumbnail="test_code.png",
    resources={
        "code": "awesome_panel_express_tests/test_code.py",
    },
    tags=["awesome-panel-extensions", "Pane"],
)


def test_code():
    """A manual test of the Code pane.

    We expect to see nicely formatted Python code"""

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
    pn.config.sizing_mode = "stretch_width"
    main = [
        APPLICATION.intro_section(),
        test_code(),
    ]
    return pn.template.FastListTemplate(title="Test Code", main=main)


if __name__.startswith("bokeh"):
    view().servable("test_code")
