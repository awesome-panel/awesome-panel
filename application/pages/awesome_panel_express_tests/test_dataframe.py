"""Panel does not style a `panel.widgets.DataFrame` by default.

A user can specify some Formatters like `Numberformatter`, `Stringformater` etc
`from bokeh.models.widgets.tables` manually. But this takes time, so I consider this *friction*.

In the [`awesome_panel_extensions.widgets.dataframe`](https://pypi.org/project/awesome-panel-extensions/#:~:text=Panel%20is%20a%20framework%20for,to%20the%20power%20of%20Panel.&text=If%20you%20wan't%20to%20learn%20more%20checkout%20the%20Package%20Documentation.)
module we lower the friction by providing functionality for sensible defaults.

If you want Panel to support sensible defaults automatically please upvote [Issue 940]\
(https://github.com/holoviz/panel/issues/940).
"""

import awesome_panel.express as pnx
import pandas as pd
import panel as pn
from awesome_panel.express.testing import TestApp
from awesome_panel_extensions.widgets import dataframe

from application.config import site

APPLICATION = site.create_application(
    url="dataframe-formatting",
    name="Dataframe Formatting",
    author="Marc Skov Madsen",
    introduction="""This app demonstrates the use of the easy to use dataframe
    formatters from the awesome-panel-extensions package""",
    description=__doc__,
    thumbnail_url="test_dataframe.png",
    documentation_url="",
    code_url="awesome_panel_express_tests/test_dataframe.py",
    gif_url="",
    mp4_url="",
    tags=["DataFrame"],
)


def test_get_default_formatters():
    """We test the `awesome_panel_extensions.widgets.dataframe.get_default_formatters` function
    applied to a DataFrame.

    We expect to see to see a `pn.widgets.DataFrame` with

    - ints aligned right, with zero decimals and ',' as thousands separator
    - floats aligned right, with two decimals and ',' as thousands separator
    - strings aligned left

    """
    data = pd.DataFrame(
        {
            "int": [
                1,
                2,
                3000,
            ],
            "float": [
                3.14,
                6.28,
                9000.42,
            ],
            "str": [
                "A",
                "B",
                "C",
            ],
        },
        index=[
            1,
            2,
            3,
        ],
    )
    formatters = dataframe.get_default_formatters(data)
    code = pnx.Code(
        """\
data = pd.DataFrame(
    {"int": [1, 2, 3000], "float": [3.14, 6.28, 9000.42], "str": ["A", "B", "C"]},
    index=[1, 2, 3],
)
formatters = dataframe.get_default_formatters(data)"""
    )
    return TestApp(
        test_get_default_formatters,
        pn.widgets.DataFrame(
            data,
            formatters=formatters,
        ),
        code,
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
        test_get_default_formatters,
    ]
    return site.create_template(title="Test DataFrame", main=main)


if __name__.startswith("bokeh"):
    view().servable("test_dataframe")
