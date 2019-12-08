# Awesome Panel Package

This package supports the [Awesome Panel Project](https://github.com/MarcSkovMadsen/awesome-panel) and provides features that are not yet and maybe never will be provided by the [Panel package](https://pypi.org/project/panel/).

This package is currently **highly experimental** and

- The **api might change** dramatically and often!
    - If the Panel package starts providing the functionality, then it should be removed from this package.
- If you find a version that works for you, then please **pin the version number**!
    - An example of pinning the version number is `awesome-panel==20191014.2`.

You can install it using

```bash
pip install awesome-panel
```

The **express** module contains improved widgets and extensions like *fontawesome* and *bootstrap* as well as the *Bootstrap Dashboard Template* used by [awesome-panel.org](https://awesome-panel.org). It should be imported as `pnx`.

```python
import awesome_panel.experiments as pnx
```

For example the code below is used to configure the Bootstrap Dashboard App in the Gallery at awesome-panel.org.

```python
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
import gallery.bootstrap_dashboard.components as components

PAGES = [
    components.About(),
    components.dashboard_view(),
    components.plotly_view(),
    components.holoviews_view(),
    components.dataframe_view(),
    components.Limitations(),
]
MENU_BUTTON_CSS_CLASSES = [
    ["navigation", "pas", "pa-home"],
    ["navigation", "pas", "pa-chart-line"],
    ["navigation", "pas", "pa-chart-bar"],
    ["navigation", "pas", "pa-chart-pie"],
    ["navigation", "pas", "pa-table"],
    ["navigation", "pas", "pa-bug"],
]


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

    app = pnx.templates.BootstrapDashboardTemplate(app_title="Bootstrap Dashboard")
    navigation_menu = pnx.NavigationMenu(
        pages=PAGES, page_outlet=app.main, css_classes=MENU_BUTTON_CSS_CLASSES
    )
    app.sidebar.append(navigation_menu)
    return app


if __name__.startswith("bk_script"):
    main().servable()
```

For more information please visit the [Awesome Panel Project](https://github.com/MarcSkovMadsen/awesome-panel) on GitHub.
