"""## Limitations Page Functionality

The Limitations Page tells what limitations i've seen when building the BootStrap Dashboard App
"""
import pathlib

import awesome_panel.express as pnx
import panel as pn

LIMITATIONS_PATH = pathlib.Path(__file__).parent / "limitations.md"


class Limitations(pn.Column):
    """The Limitations Page tells what limitations I've seen when building the BootStrap
    Dashboard App"""

    def __init__(self):
        warning = pnx.WarningAlert(
            """\
You might need to **resize this window** in order to see the full content. The Bokeh layout engine
used by Panel does not always identify the  page height correctly when showing markdown with images.
It's a limitation of Panel :-)""",
        )
        limitations = pnx.Markdown(path=LIMITATIONS_PATH)

        super().__init__(
            warning, limitations, sizing_mode="stretch_width", name="Limitations",
        )
