"""Tests of the awesome_panel functionality"""
import awesome_panel.express as pnx
import panel as pn

# pylint: disable=protected-access
import param


class _Country(
    pnx.BrowserUrlMixin,
    param.Parameterized,
):
    country = param.String()

    @param.depends("country")
    def set_browser_url_parameters(
        self,
    ):
        return super().set_browser_url_parameters()


def test_url():
    """Test of the pnx.BrowserUrlMixin"""
    country_url = _Country()
    country_url.country = "Denmark"

    assert country_url._parameter_dict() == {"country": "Denmark"}
    assert country_url._urlencode() == "country=Denmark"
    assert (
        country_url._browser_url_parameters_script()
        == '<script>window.history.replaceState({param: "country=Denmark"},"","?country=Denmark");</script>'  # pylint: disable=line-too-long
    )


def test_pn_url():
    """
    Manual Tests

    - opening
    [http://localhost:5006/test_browser_url](http://localhost:5006/test_browser_url)
    works without error
    - opening
    [http://localhost:5006/test_browser_url?country=]\
(http://localhost:5006/test_browser_url?country=)
    works without error
    - opening
    [http://localhost:5006/test_browser_url?country=Denmark]
    (http://localhost:5006/test_browser_url?country=Denmark)
    then the country widget parameter is set to Denmark
    - Changing the country widget parameter to Norway changes the browser url to
    [http://localhost:5006/test_browser_url?country=Norway]
    (http://localhost:5006/test_browser_url?country=Norway)
    """
    # Given
    country_url = _Country()

    panel = pn.Column(
        test_pn_url.__doc__,
        country_url.param,
        country_url.set_browser_url_parameters,
    )
    panel.servable("test")


if __name__.startswith("bk_script"):
    test_pn_url()
