"""I wanted to enable easy sharing of [awesome-panel.org](https://awesome-panel.org) on social media,
so implemented social sharing buttons."""

import panel as pn
from awesome_panel_extensions.widgets.link_buttons.share_buttons import (
    ShareOnFacebook,
    ShareOnLinkedIn,
    ShareOnMail,
    ShareOnReddit,
    ShareOnTwitter,
)

from application.config import site

APPLICATION = site.create_application(
    url="share-on-social-buttons",
    name="Share On Social Buttons",
    author="Marc Skov Madsen",
    introduction="""These widgets makes it easy to add "share on social" buttons to your
    apps""",
    description=__doc__,
    thumbnail_url="test_share_links.png",
    documentation_url="",
    code_url="awesome_panel_express_tests/test_share_links.py",
    gif_url="",
    mp4_url="",
    tags=["Social Media", "Buttons"],
)


@site.add(APPLICATION)
def view() -> pn.Column:
    """Wraps all tests in a Column that can be included in the Gallery or served independently

    Returns:
        pn.Column -- A Column containing all the tests
    """
    pn.config.sizing_mode = "stretch_width"
    main = [
        APPLICATION.intro_section(),
        pn.pane.Alert(
            """**You can also use the Social Sharing Buttons** in your site via the
[`awesome_panel_extensions`](https://pypi.org/project/awesome-panel-extensions/) package.

Please click and share if you like awesome-panel.org or the `awesome-panel-extensions`. Thanks.""",
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
    return pn.template.FastListTemplate(title="Share Links", main=main)


if __name__.startswith("bokeh"):
    view().servable()
