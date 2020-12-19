import panel as pn

view = pn.pane.Markdown("Hello Panel World")

pn.serve({"": view}, port=80, prefix="my-panel-apps")
