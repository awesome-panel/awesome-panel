import panel as pn
import awesome_panel.express as pnx
import pathlib

ABOUT_PATH = pathlib.Path(__file__).parent / "about.md"
IMAGE_URL = "https://getbootstrap.com/docs/4.4/assets/img/examples/dashboard.png"


class About(pn.Column):
    """The About Page tells why we build the BootStrap Dashboard App"""

    def __init__(self):
        about = pnx.Markdown(path=ABOUT_PATH)
        image = pn.pane.PNG(IMAGE_URL)
        info = pnx.InfoAlert(
            """\
Navigate to the **Dashboard Page** via the **Sidebar** to see the result.
Or Navigate to the **Limitations Page** to learn of some of the limitations of Panel that
I've experienced.""",
        )
        super().__init__(
            about, image, info, sizing_mode="stretch_width", name="About",
        )

