"""Tests of the BootStrapDashboardTemplate"""
import importlib

import panel as pn
import pytest
from selenium import webdriver

import awesome_panel.express as pnx


def test_app_attributes():
    """Test of the attributes of the Template"""
    app = pnx.templates.BootstrapDashboardTemplate()

    assert hasattr(app, "header")
    assert hasattr(app, "main")
    assert hasattr(app, "sidebar")

    assert isinstance(app.header, pn.layout.Panel)
    assert isinstance(app.main, pn.layout.Panel)
    assert isinstance(app.sidebar, pn.layout.Panel)


def test_app_with_content():
    """Basic test of the layout. Manually test that

    - The layout is divided into a header, sidebar and main area.
    - There is only vertical scroll in the sidebar and main area.
    - The vertical scroll is independent.
    """
    app = pnx.templates.BootstrapDashboardTemplate("awesome-panel.org", "https://awesome-panel.org")
    app.header.append(pn.layout.HSpacer(background="red"))
    app.header.append(pn.Row("Header", background="orange"))
    app.sidebar[:] = ["Sidebar", pn.layout.HSpacer(background="blue", height=200)]
    app.main[:] = ["Main", pn.layout.HSpacer(background="green", height=4000)]
    return app


if __name__.startswith("bk"):
    test_app_with_content().servable("test_app_with_content")
