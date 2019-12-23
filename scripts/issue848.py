import panel as pn

ABOUT = """\
# About

[Panel](https://panel.pyviz.org/) is a powerfull framework for building **awesome analytics apps** in [Python](https://www.python.org/).

The purpose of this app is to test that a **multi-page Dashboard Layout** similar to the [bootstrap dashboard template](https://getbootstrap.com/docs/4.3/examples/dashboard/) from [getboostrap.com](https://getbootstrap.com/) can be implemented in [Panel](https://panel.pyviz.org/).
"""


about_sizing_mode_stretch_width = pn.pane.Markdown(
    ABOUT, sizing_mode="stretch_width", background="lightblue"
)
about = pn.pane.Markdown(ABOUT, background="lightgreen")
about_width_policy_max = pn.pane.Markdown(ABOUT, width_policy="max", background="burlywood")
app = pn.Column(
    about_sizing_mode_stretch_width,
    about,
    about_width_policy_max,
    background="lightgray",
    sizing_mode="stretch_both",
)
app.servable()
