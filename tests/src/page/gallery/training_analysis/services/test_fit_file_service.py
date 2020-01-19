"""In this module we test the fit_file_service module"""
# pylint: disable=redefined-outer-name,protected-access
import pathlib

import pandas as pd

from src.pages.gallery.training_analysis.services import fit_file_services  # typing: ignore

FIT_FILE = pathlib.Path(fit_file_services.__file__).parent.parent / "assets/files/zwift_watopia.fit"


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
    fit_file_services._convert_units(dataframe)
    # Then
    pd.testing.assert_frame_equal(
        dataframe, expected_dataframe,
    )


def test_parse_fit_file():
    """The system can parse the bytes of a fit file"""
    # Given
    fit_file = FIT_FILE.read_bytes()

    # When
    actual = fit_file_services.parse_fit_file(fit_file)
    # Then
    assert isinstance(actual, pd.DataFrame,)
    assert not actual.empty
