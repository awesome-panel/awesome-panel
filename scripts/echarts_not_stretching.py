import panel as pn
from panel.pane import ECharts

echart = {
    "title": {"text": "Echart Chart"},
    "tooltip": {},
    "legend": {"data": ["Sales"]},
    "xAxis": {"data": ["shirt", "cardign", "chiffon shirt", "pants", "heels", "socks"]},
    "yAxis": {},
    "series": [
        {
            "name": "Sales",
            "type": "bar",
            "data": [
                10,
                10,
                10,
                10,
                10,
                10,
            ],
        }
    ],
    "responsive": True,
}
plot = ECharts(echart, min_height=300, min_width=300, sizing_mode="stretch_width")

pn.Column(
    plot,
    sizing_mode="stretch_width",
    background="gray",
).servable()
