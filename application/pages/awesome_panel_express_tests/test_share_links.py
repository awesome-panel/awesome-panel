"""
I wanted to enable easy sharing of [awesome-panel.org](https://awesome-panel.org) on social media,
so I've implemented the functionality and made it available via the
[awesome_panel package](https://pypi.org/project/awesome-panel/) in the
`awesome_panel.express.bootstrap.share_link` module"""

import panel as pn

from awesome_panel.express import fontawesome
from awesome_panel.express.fontawesome.share_link import (
    ShareOnFacebook,
    ShareOnLinkedIn,
    ShareOnMail,
    ShareOnReddit,
    ShareOnTwitter,
)
from awesome_panel.express.testing import TestApp

STYLE = """
<style>
.bk a.button-share-link {
    font-size: 2rem;
    color: black;
}
</style>
"""
fontawesome.extend()


def test_facebook():
    """The ShareOnFacebook link enables sharing a link to an url on Facebook. Here we test that

    - The link can be instantiated with a link to https://awesome-panel.org
    - It works when clicked
    """
    return TestApp(
        test_facebook,
        ShareOnFacebook(url="https://awesome-panel.org").view(),
    )


def test_linkedin():
    """The ShareOnLinkedIn link enables sharing a link to an url on LinkedIn. Here we test that

    - The link can be instantiated with a link to https://awesome-panel.org
    - It works when clicked
    """
    return TestApp(
        test_linkedin,
        ShareOnLinkedIn(url="https://awesome-panel.org").view(),
    )


def test_mail():
    """The ShareOnMail link enables sharing a link to an url via mail. Here we test that

    - The link can be instantiated with a link to https://awesome-panel.org
    - It works when clicked
    """
    return TestApp(
        test_mail,
        ShareOnMail(url="https://awesome-panel.org").view(),
    )


def test_twitter():
    """The ShareOnTwitter link enables sharing a link to an url on Twitter. Here we test that

    - The link can be instantiated with a link to https://awesome-panel.org
    - It works when clicked
    """
    return TestApp(
        test_twitter,
        ShareOnTwitter(url="https://awesome-panel.org").view(),
    )


def test_reddit():
    """The ShareOnReddit link enables sharing a link to an url on Reddit. Here we test that

    - The link can be instantiated with a link to https://awesome-panel.org
    - It works when clicked
    """
    return TestApp(
        test_reddit,
        ShareOnReddit(url="https://awesome-panel.org").view(),
    )


def view() -> pn.Column:
    """Wraps all tests in a Column that can be included in the Gallery or served independently

    Returns:
        pn.Column -- A Column containing all the tests
    """
    return pn.Column(
        pn.pane.HTML(STYLE),
        __doc__,
        test_facebook(),
        test_linkedin(),
        test_mail(),
        test_twitter(),
        test_reddit(),
    )


if __name__.startswith("bokeh"):
    view().servable()
