import hvplot.pandas
import numpy as np
import pandas as pd
import panel as pn

echarts_pane = pn.pane.ECharts(sizing_mode="stretch_both")


def update_echarts(data):
    data = pd.concat(data).reset_index()
    plot = {
        "xAxis": {"type": "category", "data": list(data.index.values)},
        "yAxis": {"type": "value"},
        "series": [
            {
                "data": list(data["y"]),
                "type": "line",
                "showSymbol": False,
                "hoverAnimation": False,
            },
        ],
        "responsive": True,
    }
    echarts_pane.object = plot


def emit(*args):
    data = [
        pd.DataFrame({"y": [np.random.randn()]}, index=pd.DatetimeIndex([pd.datetime.now()]))
        for i in range(0, 50)
    ]
    update_echarts(data)


emit()

emit_button = pn.widgets.Button(name="EMIT")
emit_button.on_click(emit)
layout = pn.layout.Card(echarts_pane, header="ECHARTS", sizing_mode="stretch_both")
layout.servable()
