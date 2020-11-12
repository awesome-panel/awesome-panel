import hvplot.pandas
import numpy as np
import pandas as pd
import panel as pn

hvplot_pane = pn.pane.HoloViews(sizing_mode="stretch_both")


def update_hvplot(data):
    data = pd.concat(data).reset_index()
    plot = data.hvplot(y="y")
    hvplot_pane.object = plot


def emit(*args):
    data = [
        pd.DataFrame({"y": [np.random.randn()]}, index=pd.DatetimeIndex([pd.datetime.now()]))
        for i in range(0, 50)
    ]
    update_hvplot(data)


emit()

emit_button = pn.widgets.Button(name="EMIT")
emit_button.on_click(emit)

layout = pn.template.ReactTemplate(
    site="Awesome Panel",
    title="HoloViews",
    theme=pn.template.react.DarkTheme,
    row_height=200,
)
layout.main[0:2, 0:12] = hvplot_pane
layout.main[2:3, 0:12] = pn.Row(emit_button, sizing_mode="stretch_width")
layout.servable()
