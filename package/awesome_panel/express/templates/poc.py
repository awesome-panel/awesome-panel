import panel as pn

top = pn.Row(
    pn.pane.Markdown("[title](/)", style={"color": "white"}, width=285),
    pn.layout.HSpacer(),
    background="rgb(52,58,64)",
    sizing_mode="stretch_width",
)
sidebar = pn.Column(width=300, min_height=2800, background="#f8f9fa")
main = pn.Column("test")
content = pn.Row(sidebar, main)

app = pn.Column(top, content, sizing_mode="stretch_both")

app.servable()
