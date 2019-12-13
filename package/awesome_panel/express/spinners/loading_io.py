"""A Collection of free spinners from https://loading.io/css/"""
import panel as pn
from awesome_panel.express.assets import LOADING_IO_PANEL_EXPRESS_CSS

EXTENDED = False
COLOR = "black"


def extend():
    global EXTENDED
    if not EXTENDED:
        EXTENDED = True
        pn.config.css_files.append(LOADING_IO_PANEL_EXPRESS_CSS)


class SpinnerBase(pn.pane.HTML):
    def __init__(self, css_class: str, color=COLOR, **kwargs):
        text = f'<div class="{css_class}" style="background:{color};"></div>'
        super().__init__(text, **kwargs)


class Circle(SpinnerBase):
    def __init__(self, color=COLOR, **kwargs):
        super().__init__(css_class="lds-circle", color=color, **kwargs)


class Facebook(pn.pane.HTML):
    def __init__(self, color=COLOR, **kwargs):
        div = f'<div style="background: {color};"></div>'
        text = f'<div class="lds-facebook">' + div * 3
        super().__init__(text, **kwargs)
