import pathlib

import panel as pn

import awesome_panel.express as pnx
from typing import List

ABOUT = """\
# About

[Panel](https://panel.pyviz.org/) is a powerfull framework for building awesome-analytics apps in [Python](https://www.python.org/).

The purpose of this app is to test that a **multi-page Dashboard Layout** similar to the [bootstrap dashboard template](https://getbootstrap.com/docs/4.3/examples/dashboard/) from [getboostrap.com](https://getbootstrap.com/) can be implemented in [Panel](https://panel.pyviz.org/).

[![GetBootstrap Dashboard Template](https://getbootstrap.com/docs/4.4/assets/img/examples/dashboard.png)](https://getbootstrap.com/docs/4.3/examples/dashboard/)
"""

INFO = """\
Navigate to the **Dashboard Page** via the **Sidebar** to see the result.
Or Navigate to the **Limitations Page** to learn of some of the limitations of Panel that
I've experienced."""


def main():
    pn.config.raw_css.append(InfoAlert.raw_css)
    about = pn.pane.Markdown(ABOUT)
    info = pnx.InfoAlert(INFO)
    app = pn.Column(about, info)
    return app


class InfoAlert(pn.pane.Markdown):
    """An Info Alert that renders Markdown

    CSS Styling can be done via the classes 'alert' and 'alert-info'. See the raw_css attribute

    Don't set sizing_mode="stretch_width" as this will result in problems.
    See https://github.com/holoviz/panel/issues/829
    """

    def __init__(
        self, text: str, css_classes: List[str] = ["alert", "alert-info"], *args, **kwargs,
    ):
        """An Info Alert that renders Markdown

        CSS Styling can be done via the classes 'alert' and 'alert-info'

        Arguments:
            text {str} -- Some MarkDown text

        KeyWord Arguments:
            css_classes {List[str]} --
        """
        super().__init__(text, css_classes=css_classes)

    raw_css = """
.bk.alert {
    position: relative;
    padding: 0.75rem 1.25rem;
    margin-bottom: 1rem;
    border: 1px solid transparent;
    border-radius: 0.25rem;
}

.bk.alert-info {
    color: #0c5460;
    background-color: #d1ecf1;
    border-color: #bee5eb;
}

.bk.alert-info hr {
    border-top-color: #abdde5;
}
"""


if __name__.startswith("bk"):
    main().servable()
