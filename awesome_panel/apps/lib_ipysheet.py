"""
The purpose of this app is to demonstrate that Panel works with the tools you know and love
&#10084;&#65039;, including ipysheet.
"""
import ipysheet
import panel as pn

from awesome_panel import config

config.extension("ipywidgets", url="lib_ipysheet")

ACCENT = config.ACCENT


def get_component(accent_base_color=ACCENT):
    """Returns an ipysheet app"""
    slider = pn.widgets.FloatSlider(value=10, start=0, end=100)
    sheet = ipysheet.sheet()

    ipysheet.cell(1, 1, "Input")
    cell3 = ipysheet.cell(1, 2, 42.0)
    ipysheet.cell(2, 1, "Output")
    cell_sum = ipysheet.cell(2, 2, 52.0, read_only=True, background_color=accent_base_color)

    @pn.depends(slider, cell3, watch=True)
    def calculate(value1, value2):
        cell_sum.value = value1 + value2

    return pn.Column(slider, sheet)


component = get_component()
pn.panel(component, height=700, sizing_mode="stretch_both").servable()
