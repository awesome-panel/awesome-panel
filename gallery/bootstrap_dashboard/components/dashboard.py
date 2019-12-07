"""# Bootstrap Dashboard Template inspired functionality"""
import awesome_panel.express as pnx
import panel as pn
from gallery.bootstrap_dashboard import services
from gallery.bootstrap_dashboard.components.core import holoviews_chart


def dashboard_view() -> pn.Column:
    """## Bootstrap Dashboard Template inspired by Page with orders chart and table

    Returns:
        pn.Column -- The Orders View
    """
    table = pn.Pane(services.get_table_data(), sizing_mode="stretch_width")
    return pn.Column(
        pnx.Title("Dashboard"),
        pnx.Divider(),
        holoviews_chart(),
        pnx.Title("Section Title"),
        pnx.Divider(),
        table,
        sizing_mode="stretch_width",
        name="Dashboard",
    )
