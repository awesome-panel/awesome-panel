"""Tests of the awesome_panel functionality"""
import awesome_panel.express as pnx
import panel as pn


def test_app():
    app = pnx.templates.BootStrapDashboardTemplate()

    assert hasattr(app, "top")
    assert hasattr(app, "main")
    assert hasattr(app, "sidebar")
    assert hasattr(app, "footer")

    assert isinstance(app.top, pn.layout.Panel)


def test_panel():
    pnx.PanelExpress()

