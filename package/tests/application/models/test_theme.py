# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
from bokeh.themes.theme import Theme as BokehTheme
from holoviews import Cycle as HoloviewsCycle

def test_can_construct(theme):
    assert isinstance(theme.spinner_static_url, str)
    assert theme.spinner_static_url

    assert isinstance(theme.spinner_url, str)
    assert theme.spinner_url

    assert isinstance(theme.loading_page_url, str)
    assert theme.loading_page_url

    assert isinstance(theme.css, str)
    assert isinstance(theme.color_cycle, tuple)
    assert theme.bokeh_disable_logo is True
    assert hasattr(theme, "bokeh_theme_json")

    assert isinstance(theme.bokeh_theme, BokehTheme)
    assert isinstance(theme.holoviews_color_cycle, HoloviewsCycle)
