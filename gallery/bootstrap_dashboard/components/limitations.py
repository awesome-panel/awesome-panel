import panel as pn
import awesome_panel.express as pnx
import pathlib

LIMITATIONS_PATH = pathlib.Path(__file__).parent / "limitations.md"


class Limitations(pn.Column):
    """The Limitations Page tells what limitations i've seen when building the BootStrap
    Dashboard App"""

    def __init__(self):
        title = pnx.Title("Current Limitations")
        warning = pnx.WarningAlert(
            """\
Please **resize this window** in order to see the full content. Panel/ Bokeh does not identifying
the  page height correctly when showing markdown with images. It's a limitation of Panel :-)""",
        )
        limitations = pnx.Markdown(path=LIMITATIONS_PATH)

        super().__init__(
            title, warning, limitations, sizing_mode="stretch_width", name="Limitations",
        )

