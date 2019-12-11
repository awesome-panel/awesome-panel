"""# BootstrapDashboard App.

Creates a Bootstrap Dashboard App

- inspired by the [GetBoostrap Dashboard Template]
(https://getbootstrap.com/docs/4.4/examples/dashboard/)
- implemented using the `awesome_panel' python package and in particular the
`awesome_panel.express.templates.BootstrapDashboardTemplate`
- Start the app by using `panel serve` on this file.
"""
import panel as pn

import awesome_panel.express as pnx
from src.pages import home, resources, about, issues, gallery


MENU_BUTTON_CSS_CLASSES = [
    ["navigation", "pas", "pa-home"],
    ["navigation", "pas", "pa-link"],
    ["navigation", "pas", "pa-images"],
    ["navigation", "pas", "pa-bug"],
    ["navigation", "pas", "pa-address-card"],
]

CONTACT = """\
    <a href="https://github.com/marcskovmadsen/awesome-panel"><i class="fab fa-github"></i></a>"""


def main() -> pn.Pane:
    """## Bootstrap Dashboard App

    Creates a Bootstrap Dashboard App

    - inspired by the [GetBoostrap Dashboard Template]
    (https://getbootstrap.com/docs/4.4/examples/dashboard/)
    - implemented using the `awesome_panel' python package and in particular the
    `awesome_panel.express.templates.BootstrapDashboardTemplate`

    Returns:
        pn.Pane -- The Bootstrap Dashboard App
    """
    pnx.fontawesome.extend()

    app = pnx.templates.BootstrapDashboardTemplate(app_title="Awesome Panel")

    PAGES = [
        # Hack for some reason I need to instantiate this otherwise the layout is not nice
        home.view(),
        resources.view,
        gallery.Gallery(app.main).view,
        issues.view,
        about.view,
    ]
    navigation_menu = pnx.NavigationMenu(
        pages=PAGES, page_outlet=app.main, css_classes=MENU_BUTTON_CSS_CLASSES
    )
    app.sidebar.append(navigation_menu)

    contact = pn.pane.HTML(CONTACT)
    app.header.append(contact)
    app.header.append(pn.layout.HSpacer(width=50))
    return app


if __name__.startswith("bk_script"):
    main().servable()

