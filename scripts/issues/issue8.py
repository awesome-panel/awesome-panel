import panel as pn

ABOUT = """\
# About

[Panel](https://panel.pyviz.org/) is a pwerful framework for building awesome-analytics apps in [Python](https://www.python.org/).

The purpose of this app is to test that a **multi-page Dashboard Layout** similar to the [bootstrap dashboard template](https://getbootstrap.com/docs/4.3/examples/dashboard/) from [getboostrap.com](https://getbootstrap.com/) can be implemented in [Panel](https://panel.pyviz.org/).
"""

IMAGE = "https://getbootstrap.com/docs/4.4/assets/img/examples/dashboard.png"

INFO = """\
Navigate to the **Dashboard Page** via the **Sidebar** to see the result.
Or Navigate to the **Limitations Page** to learn of some of the limitations of Panel that
I've experienced."""

about = pn.layout.Row(pn.pane.Markdown(ABOUT))
image = pn.pane.PNG(IMAGE)
info = pn.layout.Row(
    pn.pane.Markdown(
        INFO,
        background="#d1ecf1",
    )
)
app = pn.Column(
    about,
    image,
    info,
)
app.servable()
