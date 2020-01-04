"""# BootstrapDashboard App.

Creates a Bootstrap Dashboard App

- inspired by the [GetBoostrap Dashboard Template]
(https://getbootstrap.com/docs/4.4/examples/dashboard/)
- implemented using the `awesome_panel' Python package and in particular the
`awesome_panel.express.templates.BootstrapDashboardTemplate`
- Start the app by using `panel serve` on this file.
"""
import panel as pn

import awesome_panel.express as pnx
from awesome_panel.database.apps_in_gallery import APPS_IN_GALLERY
from src.pages import about, gallery, home, issues, resources
from typing import Optional, List

MENU_BUTTON_CSS_CLASSES: Optional[List[Optional[List[str]]]] = [
    ["navigation", "pas", "pa-home"],
    ["navigation", "pas", "pa-link"],
    ["navigation", "pas", "pa-images"],
    ["navigation", "pas", "pa-bug"],
    ["navigation", "pas", "pa-address-card"],
]

CONTACT = """<p>
<a href="https://github.com/marcskovmadsen/awesome-panel" target="_blank"><i class="fab fa-github" title="GitHub"></i></a>
<a Docs" href="https://awesome-panel.readthedocs.io/en/latest/" target="_blank"><i class="fas fa-book" title="Read the Docs"></i></a>
<a href="https://pypi.org/project/awesome-panel/" target="_blank"><i class="fas fa-cubes" title="PyPi"></i></a>
<a href="https://hub.docker.com/r/marcskovmadsen/awesome-panel" target="_blank"><i class="fab fa-docker" title="Docker"></i></a>
</p>"""

INFO = """\
#### Contribute

This an **open source project** and you are very welcome to contribute your awesome comments,
questions, resources and apps as
[issues and feature requests](https://github.com/MarcSkovMadsen/awesome-panel/issues/new/choose)
or
[pull requests](https://github.com/marcskovmadsen/awesome-panel/pulls).
"""

SHARE_LINK_STYLE = """
nav .bk a.button-share-link {
    font-size: 1rem;
    color: #343a40;
    margin-left: 2px;
}
"""


def main() -> pn.Pane:
    """## Bootstrap Dashboard App

    Creates a Bootstrap Dashboard App

    - inspired by the [GetBoostrap Dashboard Template]
    (https://getbootstrap.com/docs/4.4/examples/dashboard/)
    - implemented using the `awesome_panel' Python package and in particular the
    `awesome_panel.express.templates.BootstrapDashboardTemplate`

    Returns:
        pn.Pane -- The Bootstrap Dashboard App
    """
    pn.extension("vega")
    pnx.fontawesome.extend()
    pn.config.raw_css.append(SHARE_LINK_STYLE)

    app = pnx.templates.BootstrapDashboardTemplate(app_title="Awesome Panel")

    pages = [
        # Hack for some reason I need to instantiate this otherwise the layout is not nice
        home.view(),
        resources.view,
        gallery.Gallery(page_outlet=app.main, apps_in_gallery=APPS_IN_GALLERY).view,
        issues.view,
        about.view,
    ]
    navigation_menu = pnx.NavigationMenu(
        pages=pages, page_outlet=app.main, css_classes=MENU_BUTTON_CSS_CLASSES
    )
    share = pn.Column(
        pnx.Markdown("#### Share"),
        pn.Row(
            pnx.fontawesome.share_link.ShareOnTwitter().view(),
            pnx.fontawesome.share_link.ShareOnLinkedIn().view(),
            pnx.fontawesome.share_link.ShareOnReddit().view(),
            pnx.fontawesome.share_link.ShareOnFacebook().view(),
            pnx.fontawesome.share_link.ShareOnMail().view(),
        ),
        margin=(10, 10, 0, 10),
    )
    info = pn.Column(pnx.Markdown(INFO), margin=(0, 10, 0, 10), sizing_mode="stretch_width")
    app.sidebar[:] = [navigation_menu, share, info]

    contact = pn.Row(pn.pane.HTML(CONTACT))
    app.header.append(contact)
    app.header.append(pn.layout.VSpacer(width=25))
    return app


if __name__.startswith("bk_script"):
    main().servable("Awesome Panel")
