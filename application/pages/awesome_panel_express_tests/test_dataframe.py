"""Panel does not style a `widgets.DataFrame` by default.

A user can specify some Formatters like `Numberformatter`, `Stringformater` etc
`from bokeh.models.widgets.tables` manually. But this takes time, so I consider this *friction*.

In the `awesome_panel.express.widgets.dataframe` module we lower the friction by providing
functionality for sensible defaults. See also [Issue 940]\
(https://github.com/holoviz/panel/issues/940).
"""

import awesome_panel.express as pnx
import pandas as pd
import panel as pn
from awesome_panel.express.testing import TestApp
from awesome_panel.express.widgets import dataframe

from application.template import get_template


def test_get_default_formatters():
    """A manual test of the `pnx.widgets.dataframe.get_default_formatters` function applied to a
    DataFrame.

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


def view() -> pn.Column:
    """Wraps all tests in a Column that can be included in the Gallery or served independently

    Returns:
        pn.Column -- A Column containing all the tests
    """
    pn.config.sizing_mode = "stretch_width"
    main = [
        pn.pane.Markdown(__doc__),
        test_get_default_formatters,
    ]
    return get_template(title="Test DataFrame", main=main)


if __name__.startswith("bokeh"):
    view().servable("test_dataframe")
