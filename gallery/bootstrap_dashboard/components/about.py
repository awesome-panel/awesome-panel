"""## About Page

The About Page tells why we build the BootStrap Dashboard App.

The content is from the markdown file located at ABOUT_PATH combined with an image from IMAGE_URL.
"""
import pathlib

import awesome_panel.express as pnx
import panel as pn

ABOUT_PATH = pathlib.Path(__file__).parent / "about.md"
IMAGE_PATH = (
    pathlib.Path(__file__).parent.parent
    / "assets"
    / "images"
    / "bootstrap_dashboard_template_original.png"
)


class About(pn.Column):
    """The About Page tells why we build the BootStrap Dashboard App"""

    def __init__(self):
        about = pnx.Markdown(path=ABOUT_PATH)
        image = pn.pane.PNG(str(IMAGE_PATH), max_width=600, sizing_mode="scale_both")
        info = pnx.InfoAlert(
            """\
Navigate to the **Dashboard Page** via the **Sidebar** to see the result.
Or Navigate to the **Limitations Page** to learn of some of the limitations of Panel that
I've experienced.""",
        )
        warning = pnx.WarningAlert(
            """Please note that there is a bug wrt. Chrome making Panel/ Bokeh applications slow in
            general. See [Bokeh Issue 9515](https://github.com/bokeh/bokeh/issues/9515)"""
        )
        super().__init__(
            about, image, info, warning, sizing_mode="stretch_width", name="About",
        )
