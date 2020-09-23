"""In this module we provide services for working with fit files.

Resources

- fitparse package: [GitHub](https://github.com/dtcooper/python-fitparse) and \
    [Docs](http://dtcooper.github.io/python-fitparse/)
- fitdecode pacakge: [GitHub](https://github.com/polyvertex/fitdecode) and \
    [Read the Docs](https://fitdecode.readthedocs.io/en/latest/)
- [FIT on Wikipedia](https://wiki.openstreetmap.org/wiki/FIT)
- [Download FIT SDK](https://www.thisisant.com/resources/fit).
"""

from typing import Union

import fitparse
import pandas as pd

UNIT_CONVERSION = {
    "speed": {
        "from": "10*6m/s",
        "to": "km/h",
        "factor": 0.0036,
    },
    "enhanced_speed": {
        "from": "10*6m/s",
        "to": "km/h",
        "factor": 3.6,
    },
    "altitude": {
        "from": "unknown",
        "to": "m",
        "factor": 0.03855343881175331,
    },
    "position_long": {
        "from": "semicircles",
        "to": "degrees",
        "factor": (180.0 / 2 ** 31),
    },
    "position_lat": {
        "from": "semicircles",
        "to": "degrees",
        "factor": (180.0 / 2 ** 31),
    },
}


def parse_fit_file(
    file: Union[
        fitparse.base.FitFile,
        bytes,
        str,
    ]
) -> pd.DataFrame:
    """Converts a fit_file to a dataframe

    Args:
        file (Union[fitparse.base.FitFile, bytes, str]): The fit file to parse

    Raises:
        ValueError: If the file is not in a supported format

    Returns:
        pd.DataFrame: A DataFrame with the data
    """
    if isinstance(
        file,
        (
            bytes,
            str,
        ),
    ):
        fit_file = fitparse.FitFile(file)
    elif isinstance(
        file,
        fitparse.base.FitFile,
    ):
        fit_file = file
    else:
        raise ValueError(f"{type(file)} is not supported!")

    return _parse_records(fit_file.get_messages("record"))


def _parse_records(
    records,
):
    data = [record.get_values() for record in records]
    training_data = pd.DataFrame(data)
    _convert_units(training_data)
    return training_data


def _convert_units(
    training_data_row: pd.DataFrame,
):
    columns = set(UNIT_CONVERSION.keys()).intersection(set(training_data_row.columns))
    for column in columns:
        training_data_row[column] *= UNIT_CONVERSION[column]["factor"]
