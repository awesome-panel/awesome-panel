"""Test of the training_analysis module"""
import datetime

# pylint: disable=redefined-outer-name,protected-access
from src.pages.gallery.training_analysis.training_analysis import TrainingServices
import pathlib
import pandas as pd
import holoviews as hv

FIT_FILE = pathlib.Path(__file__).parent / "files/4394446039.fit"


def test__convert_units():
    # Given
    data = [{"speed": 10000.0, "enhanced_speed": 10.0, "altitude": 3097}]
    dataframe = pd.DataFrame(data)
    expected_data = [{"speed": 10000.0 * 0.0036, "enhanced_speed": 10.0 * 3.6, "altitude": 119.4}]
    expected_dataframe = pd.DataFrame(expected_data)
    # When
    TrainingServices._convert_units(dataframe)
    # Then
    pd.testing.assert_frame_equal(dataframe, expected_dataframe)


def test_parse_fit_file():
    # Given
    fit_file = FIT_FILE.read_bytes()

    # When
    actual = TrainingServices.parse_fit_file(fit_file)
    # Then
    assert isinstance(actual, pd.DataFrame)
    assert not actual.empty


def test_plot_layout_none():
    assert TrainingServices.plot_layout(None) is None

def test_plot_layout_empty():
    assert TrainingServices.plot_layout(pd.DataFrame()) is None

def test_plot_map_none():
    assert TrainingServices.plot_map(None) is None

def test_plot_map_empty():
    assert TrainingServices.plot_map(pd.DataFrame()) is None
