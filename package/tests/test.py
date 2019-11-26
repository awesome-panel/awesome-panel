"""Tests of the awesome_panel functionality"""
import importlib

import param
import pytest
from selenium import webdriver

import awesome_panel.express as pnx
import panel as pn

importlib.reload(pnx)


@pytest.mark.fixture
def chrome_driver() -> webdriver.Chrome:
    """The Chrome Web Driver Configured for Download

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
    app = pnx.templates.BootStrapDashboardTemplate()

    assert hasattr(app, "main")
    assert hasattr(app, "sidebar")

    assert isinstance(app.main, pn.layout.Panel)
    assert isinstance(app.sidebar, pn.layout.Panel)


class _Country(pnx.widgets.Url, param.Parameterized):
    country = param.String()

    @param.depends("country")
    def set_url_parameters(self):
        return super().set_url_parameters()


def test_url():
    country_url = _Country()
    country_url.country = "Denmark"

    assert country_url._parameter_dict() == {"country": "Denmark"}
    assert country_url._urlencode() == "country=Denmark"


def test_pn_url_view():
    country_url = _Country()
    country_url.country = "Norway"
    panel = pn.Column(country_url.param, country_url.set_url_parameters)
    panel.servable()


if __name__.startswith("bk_script"):
    test_pn_url_view()
