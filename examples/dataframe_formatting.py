# pylint: disable=line-too-long
"""Panel does not style a `panel.widgets.DataFrame` by default.

A user can specify some Formatters like `Numberformatter`, `Stringformater` etc
`from bokeh.models.widgets.tables` manually. But this takes time, so I consider this *friction*.

In the [`awesome_panel_extensions.widgets.dataframe`](https://pypi.org/project/awesome-panel-extensions/#:~:text=Panel%20is%20a%20framework%20for,to%20the%20power%20of%20Panel.&text=If%20you%20wan't%20to%20learn%20more%20checkout%20the%20Package%20Documentation.)
module we lower the friction by providing functionality for sensible defaults.

If you want Panel to support sensible defaults automatically please upvote [Issue 940]\
(https://github.com/holoviz/panel/issues/940).
"""
# pylint: enable=line-too-long

import pandas as pd
import panel as pn
from awesome_panel_extensions.widgets import dataframe

from awesome_panel import config

config.extension(url="dataframe_formatting")

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
code = pn.pane.Markdown(
    """## Code

```python
import pandas as pd
import panel as pn
from awesome_panel_extensions.widgets import dataframe

data = pd.DataFrame(
    {"int": [1, 2, 3000], "float": [3.14, 6.28, 9000.42], "str": ["A", "B", "C"]}, index=[1, 2, 3],
)
formatters = dataframe.get_default_formatters(data)
pn.widgets.DataFrame(data, formatters=formatters)
```

## Result
"""
)


pn.Column(code, pn.widgets.DataFrame(data, formatters=formatters)).servable()
