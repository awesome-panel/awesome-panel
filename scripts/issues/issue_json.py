import panel as pn

response = {"value": "panel is great! " * 10}

pn.Column(
    pn.pane.JSON(response, depth=1, theme="light"), width=800, background="lightgray",
).servable()
