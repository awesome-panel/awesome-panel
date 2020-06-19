# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
import holoviews as hv
import pandas as pd
import panel as pn
import pytest

from awesome_panel.styler import AwesomePanelStyler
from awesome_panel.styler.styler import AwesomePanelStylerView, HvPlotOptions


@pytest.fixture
def data():
    return pd.DataFrame([
        {"x": [1,2]},
        {"y": [2,4]},
    ])

@pytest.fixture
def options():
    return HvPlotOptions(x="x", y="y")

@pytest.fixture
def designer(options, data):
    return AwesomePanelStyler(data=data, options=options)

def test_designer_fixture(designer, options, data):
    assert isinstance(designer, AwesomePanelStyler)
    assert designer.options is options
    assert designer.data is data

def test_can_construct():
    AwesomePanelStyler()

def test_has_plot(designer):
    assert isinstance(designer.plot, (hv.Element, hv.Layout, hv.Overlay, hv.NdOverlay))

def test_plot_has_data(designer):
    assert isinstance(designer.data, pd.DataFrame)

def test_can_view(designer):
    assert isinstance(designer.view, AwesomePanelStylerView)

def test_can_change_theme(designer):
    assert isinstance(designer.theme, str)

def test_can_update_plot(designer):
    # Given
    designer.active = True
    # When
    designer.update_plot()
    # Then
    assert designer.active == False

def test_can_select_kind():
    designer.kind = "line"
    designer.bar = "line"

def test_can_select_options(designer):
    assert isinstance(designer.options, HvPlotOptions)

def test_can_select_x(options):
    options.x = ""

def test_can_select_y(options):
    options.y = ""


def test_can_create_bokeh_themes():
    # When
    bokeh_themes = AwesomePanelStyler.get_bokeh_themes()
    # Then
    assert isinstance(bokeh_themes, dict)
    assert "caliber" in bokeh_themes
    assert "dark_minimal" in bokeh_themes
    assert "light_minimal" in bokeh_themes
    assert "material-light" in bokeh_themes
    assert "material-dark" in bokeh_themes

if __name__.startswith("bokeh"):
    import pathlib
    path = pathlib.Path.cwd() / "application/pages/kickstarter_dashboard/kickstarter-cleaned.csv"
    data = pd.read_csv(path).sample(10)
    AwesomePanelStyler(data=data).view.servable()