import datetime as dt

import holoviews as hv
import numpy as np
import pandas as pd
import panel as pn
from bokeh.models.widgets.tables import BooleanFormatter, NumberFormatter

pn.extension()

TABULATOR_THEME = {
    pn.template.theme.DefaultTheme: "site",
    pn.template.theme.DarkTheme: "midnight",
}
ACCENT_COLOR = "#E1477E"

template = pn.template.FastGridTemplate(title="FastGridTemplate")
template.compact = "both"
pn.config.sizing_mode = "stretch_width"

df = pd.DataFrame(
    {
        "int": [1, 2, 3],
        "float": [3.14, 6.28, 9.42],
        "str": ["A", "B", "C"],
        "bool": [True, False, True],
        "date": [dt.date(2019, 1, 1), dt.date(2020, 1, 1), dt.date(2020, 1, 10)],
    },
    index=[1, 2, 3],
)

bokeh_formatters = {
    "float": NumberFormatter(format="0.00"),
    "bool": BooleanFormatter(),
}

theme = TABULATOR_THEME.get(template.theme, "site")
df_widget = pn.widgets.Tabulator(
    df, formatters=bokeh_formatters, theme=theme, sizing_mode="stretch_both"
)
df_widget._configuration["layout"] = "fitDataFill"
df_widget._configuration["responsiveLayout"] = "collapse"
df_widget._configuration["columns"] = [
    {"int": "Name", "field": "name", "responsive": 0},
    {"float": "Name", "field": "name", "responsive": 1},
    {"str": "Name", "field": "name", "responsive": 2},
    {"bool": "Name", "field": "name", "responsive": 3},
    {"date": "Name", "field": "name", "responsive": 0},
]

print(df_widget._get_configuration(""))
template.main[:3, :] = pn.Column(df_widget, sizing_mode="stretch_both")
template.sidebar.append(df_widget.param.theme)

template.servable()
