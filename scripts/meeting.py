import panel as pn

title = pn.pane.Markdown("NCC Meeting 20200615")
app_bar = pn.Column(title, background="green", style={"color": "white"})

app = pn.Column(
    app_bar,
    sizing_mode="stretch_both"
)
pn.config.sizing_mode="stretch_width"
app.servable()