"""Tests of the BootStrapDashboardTemplate"""
import importlib

import panel as pn
import pytest
from selenium import webdriver

import awesome_panel.express as pnx

importlib.reload(pnx)


@pytest.fixture
def chrome_driver() -> webdriver.Chrome:
    r"""The Chrome Web Driver Configured for Download

    You can download the Chrome driver from https://chromedriver.chromium.org/ and move
    chromedriver.exe to c:\Windows\System32 or an alternative location in the PATH

    Returns:
        webdriver.Chrome -- The Chrome Web Driver
    """
    options = webdriver.ChromeOptions()
    # Maybe add this later
    # options.add_argument('headless')
    options.add_experimental_option("useAutomationExtension", False)

    return webdriver.Chrome(options=options)


def test_app():
    """Test of the attributes of the Template"""
    app = pnx.templates.BootstrapDashboardTemplate()

    assert hasattr(app, "main")
    assert hasattr(app, "sidebar")

    assert isinstance(app.main, pn.layout.Panel)
    assert isinstance(app.sidebar, pn.layout.Panel)


def test_markdown_image_width_max_100_percent():
    """We test that the markdown image width cannot be more than 100%.

    This is usefull in order to reduce the friction of using the template and Panel in general"""
