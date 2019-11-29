from gallery.bootstrap_dashboard import components
import panel as pn


def test_dashboard_plot():
    """Manual test that the width of the chart is full width"""
    dashboard = components.Dashboard()
    column = pn.Column(dashboard._chart(), width_policy="max", background="red")
    column.servable("test_dashboard_blot")


if __name__.startswith("bk"):
    import importlib

    importlib.reload(components)
    test_dashboard_plot()
