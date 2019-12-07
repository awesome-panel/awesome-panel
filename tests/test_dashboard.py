import panel as pn
from gallery.bootstrap_dashboard import components


def test_dashboard_plot():
    """Manual test that the width of the chart is full width"""
    dashboard = components.Dashboard()
    column = pn.Column(dashboard._chart_plotly(), width_policy="max", background="red")
    column.servable("test_dashboard_blot")


if __name__.startswith("bk"):
    test_dashboard_plot()
