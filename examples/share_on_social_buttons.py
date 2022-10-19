"""I wanted to enable easy sharing of
[awesome-panel.org](https://awesome-panel.org) on social media,
so implemented social sharing buttons."""

import panel as pn
from awesome_panel_extensions.widgets.link_buttons.share_buttons import (
    ShareOnFacebook,
    ShareOnLinkedIn,
    ShareOnMail,
    ShareOnReddit,
    ShareOnTwitter,
)

from awesome_panel import config


def components() -> pn.Column:
    """Wraps all tests in a Column that can be included in the Gallery or served independently

    Returns:
        pn.Column -- A Column containing all the tests
    """

    return [  # type: ignore
        pn.pane.Alert(
            """
Please **click and share** if you like awesome-panel.org or the
`awesome-panel-extensions`. Thanks.""",
            margin=0,
        ),
        pn.Row(
            pn.Spacer(),
            ShareOnTwitter(url="https://awesome-panel.org", size=6),
            ShareOnLinkedIn(url="https://awesome-panel.org", size=6),
            ShareOnReddit(url="https://awesome-panel.org", size=6),
            ShareOnFacebook(url="https://awesome-panel.org", size=6),
            ShareOnMail(url="https://awesome-panel.org", size=6),
        ),
    ]


if __name__.startswith("bokeh"):
    config.extension(url="share_on_social_buttons")

    for component in components():
        component.servable()
