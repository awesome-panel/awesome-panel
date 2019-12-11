"""# BootstrapDashboard App.

Creates a Bootstrap Dashboard App

- inspired by the [GetBoostrap Dashboard Template]
(https://getbootstrap.com/docs/4.4/examples/dashboard/)
- implemented using the `awesome_panel' python package and in particular the
`awesome_panel.express.templates.BootstrapDashboardTemplate`
- Start the app by using `panel serve` on this file.
"""
import panel as pn

import gallery.bootstrap_dashboard.components as components


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
    tabs = pn.Tabs(
        components.About(),
        components.dashboard_view(),
        # components.plotly_view(),
        # components.holoviews_view(),
        # components.dataframe_view(),
        sizing_mode="stretch_width",
    )
    app = pn.Column(tabs, name="Bootstrap Dashboard", sizing_mode="stretch_width")
    return app
