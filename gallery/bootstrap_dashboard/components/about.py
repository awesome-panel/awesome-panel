"""## About Page

The About Page tells why we build the BootStrap Dashboard App.

The content is from the markdown file located at ABOUT_PATH combined with an image from thumbnail_path.
"""
import pathlib

import panel as pn

import awesome_panel.express as pnx

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
Navigate to the **Dashboard Page** via the **Tab** to see the result. The other tabs are comments on
what alternative layouts and widgets I could have used.""",
        )
        super().__init__(
            about, image, info, sizing_mode="stretch_both", name="About",
        )
