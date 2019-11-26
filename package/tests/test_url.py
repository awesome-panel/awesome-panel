"""Tests of the awesome_panel functionality"""
import importlib

import param

import awesome_panel.express as pnx
import panel as pn

importlib.reload(pnx)


class _Country(pnx.param.UrlMixin, param.Parameterized):
    country = param.String()

    def __init__(self, **params):
        for key, value in pn.state.session_args.items():
            if key in self._parameter_dict():
                value_str = value[0].decode("utf8")
                self.set_param(key, value_str)
        super().__init__(**params)

    @param.depends("country")
    def set_browser_url_parameters(self):
        return super().set_browser_url_parameters()


def test_url():
    country_url = _Country()
    country_url.country = "Denmark"

    assert country_url._parameter_dict() == {"country": "Denmark"}
    assert country_url._urlencode() == "country=Denmark"


def test_pn_url():
    """Manual Test"""
    # Given
    country_url = _Country()
    panel = pn.Column(
        country_url.param, country_url.set_browser_url_parameters
    )
    panel.servable()
    # When
    # 0. opening http://localhost:5006/test_url works without error
    # 2. opening http://localhost:5006/test_url?country= works without error
    # 3. opening http://localhost:5006/test_url?country=Denmark
    # then the country widget parameter is set to Denmark
    # 4. Changing the country widget parameter to Norway changes the browser url to
    # http://localhost:5006/test_url?country=Norway


if __name__.startswith("bk_script"):
    test_pn_url()
