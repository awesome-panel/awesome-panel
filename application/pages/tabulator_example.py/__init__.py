import numpy as np
import holoviews as hv
import pandas as pd, datetime as dt

from bokeh.models.widgets.tables import NumberFormatter, BooleanFormatter

import panel as pn
pn.extension()

TABULATOR_THEME = {
    pn.template.theme.DefaultTheme: "site",
    pn.template.theme.DarkTheme: "midnight",
}
ACCENT_COLOR = "#E1477E"

template = pn.template.FastGridTemplate(title='FastGridTemplate')
template.compact = 'both'
pn.config.sizing_mode = 'stretch_width'

xs = np.linspace(0, np.pi)
freq = pn.widgets.FloatSlider(name="Frequency", start=0, end=10, value=2)
phase = pn.widgets.FloatSlider(name="Phase", start=0, end=np.pi)

@pn.depends(freq=freq, phase=phase)
def sine(freq, phase):
    return hv.Curve((xs, np.sin(xs*freq+phase))).opts(
        responsive=True, min_height=400, title="Sine", color=ACCENT_COLOR)

@pn.depends(freq=freq, phase=phase)
def cosine(freq, phase):
    return hv.Curve((xs, np.cos(xs*freq+phase))).opts(
        responsive=True, min_height=400, title="Cosine", color=ACCENT_COLOR)

col = pn.Column (pn.pane.Markdown("## Settings"),
                           freq,
                          phase)

template.sidebar.append(col)

df = pd.DataFrame({
    'int': [1, 2, 3],
    'float': [3.14, 6.28, 9.42],
    'str': ['A', 'B', 'C'],
    'bool': [True, False, True],
    'date': [dt.date(2019, 1, 1), dt.date(2020, 1, 1), dt.date(2020, 1, 10)]
}, index=[1, 2, 3])

bokeh_formatters = {
    'float': NumberFormatter(format='0.00'),
    'bool': BooleanFormatter(),
}

theme = TABULATOR_THEME.get(template.theme, "site")
df_widget = pn.widgets.Tabulator(df, formatters=bokeh_formatters, theme=theme, sizing_mode="stretch_both")
# layout:"fitDataFill",
df_widget._configuration['layout'] = 'fitDataFill'
df_widget._configuration['responsiveLayout'] = 'collapse'
df_widget._configuration['columns'] = [
   {'int':'Name', 'field':'name', 'responsive':0},
   {'float':'Name', 'field':'name', 'responsive':1},
   {'str':'Name', 'field':'name', 'responsive':2},
   {'bool':'Name', 'field':'name', 'responsive':3},
   {'date':'Name', 'field':'name', 'responsive':0},
]

print (df_widget._get_configuration(''))
template.main[:3, :6] = hv.DynamicMap(sine)
template.main[:3, 6:] = pn.Column(df_widget, sizing_mode='stretch_both')
template.sidebar.append(df_widget.param.theme)

# template.servable()

pn.Column(
    df_widget.param.theme, df_widget, sizing_mode="stretch_both", background="lightgray"
).servable()