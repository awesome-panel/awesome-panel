import panel as pn

pn.extension("echarts")

STYLE = """
.react-grid-item {
    border: 1px solid lightgray;
}
"""
pn.config.raw_css.append(STYLE)

template = pn.template.ReactTemplate(row_height=200)

template.main[0:3, 0:3] = pn.Row(
    pn.layout.HSpacer(),
    pn.indicators.Gauge(
        name="Failure Rate",
        value=10,
        bounds=(0, 100),
        background="whitesmoke",
        align="center"
    ),
    pn.layout.HSpacer(),
    sizing_mode="stretch_width"
)

for row in range(0, 3):
    for col in range(3, 12):
        template.main[row, col] = pn.indicators.Gauge(
            name="Failure Rate",
            value=10,
            bounds=(0, 100),
            sizing_mode="stretch_both",
            background="whitesmoke",
        )

template.servable()
