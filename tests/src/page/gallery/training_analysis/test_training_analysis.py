"""Test of the training_analysis module"""
import pathlib

import pandas as pd

# pylint: disable=redefined-outer-name,protected-access
from src.pages.gallery.training_analysis.training_analysis import TrainingServices

FIT_FILE = pathlib.Path(__file__).parent / "files/zwift_watopia.fit"


def test__convert_units():
    """The numbers of the fit file is not in standard units. So we need to convert"""
    # Given
    data = [
        {
            "speed": 10000.0,
            "enhanced_speed": 10.0,
            "altitude": 3097,
            "position_long": 1978097408,
            "position_lat": -123884640,
        }
    ]
    dataframe = pd.DataFrame(data)
    expected_data = [
        {
            "speed": 10000.0 * 0.0036,
            "enhanced_speed": 10.0 * 3.6,
            "altitude": 119.4,
            "position_long": 165.802209,
            "position_lat": -10.383891,
        }
    ]
    expected_dataframe = pd.DataFrame(expected_data)
    # When
    TrainingServices._convert_units(dataframe)
    # Then
    pd.testing.assert_frame_equal(dataframe, expected_dataframe)


def test_parse_fit_file():
    """The system can parse the bytes of a fit file"""
    # Given
    fit_file = FIT_FILE.read_bytes()

    # When
    actual = TrainingServices.parse_fit_file(fit_file)
    # Then
    assert isinstance(actual, pd.DataFrame)
    assert not actual.empty


def test_plot_layout_none():
    """The plot_layout function can handle None as input"""
    assert TrainingServices.plot_layout(None) is None


def test_plot_layout_empty():
    """The plot_layout function can handle an empty DataFrame as input"""
    assert TrainingServices.plot_layout(pd.DataFrame()) is None


def test_plot_map_none():
    """The plot_map function can handle None as input"""
    assert TrainingServices.plot_map(None) is None


def test_plot_map_empty():
    """The plot_map function can handle an empty DataFrame as input"""
    assert TrainingServices.plot_map(pd.DataFrame()) is None
