"""Minimal Hello World Example"""
import panel as pn

app = pn.pane.Markdown("# Hello Panel World from .py Python File")
app.servable()
