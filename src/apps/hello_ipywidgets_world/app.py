"""Minimal Ipywidgets Hello World Example"""
import panel as pn
from ipywidgets import HTML

pn.config.sizing_mode = "stretch_width"

app = HTML("<h1>Hello Ipywidgets World from .py Python File</h1>")

# C.f. https://panel.holoviz.org/reference/panes/IPyWidget.html
pn.pane.IPyWidget(app).servable()
