from panel import template
from panel.pane import Markdown

ABOUT = """
# About the Awesome Panel Project
"""

def view() -> template.BaseTemplate:
    """The about view of awesome-panel.org"""
    main = [Markdown(ABOUT, sizing_mode="stretch_width")]
    return template.GoldenTemplate(title="About", main=main)

if __name__.startswith("bokeh"):
    view().servable()