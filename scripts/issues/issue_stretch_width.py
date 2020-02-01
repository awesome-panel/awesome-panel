import panel as pn

pn.config.sizing_mode = "stretch_width"

button = pn.widgets.Button(name="click me")
spacer = pn.layout.HSpacer(height=5)
svg = pn.pane.SVG(
    "https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg",
    width=360,
    height=100,
    align="center",
)

app = pn.Column(
    spacer, svg, button, spacer, name="gallery-item", width=400, margin=10, sizing_mode="fixed",
)

app.servable()
