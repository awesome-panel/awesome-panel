"""This module provides functionality for using the DataFrame widget like for example
custom styling"""
from typing import Dict

import pandas as pd
from bokeh.models.widgets.tables import NumberFormatter

INT_DTYPE = "int64"
INT_FORMAT = "0,0"
INT_ALIGN = "right"
FLOAT_DTYPE = "float64"
FLOAT_FORMAT = "0,0.00"
FLOAT_ALIGN = "right"


def get_default_formatters(
    data: pd.DataFrame,
    int_format: str = INT_FORMAT,
    int_align: str = INT_ALIGN,
    float_format: str = FLOAT_FORMAT,
    float_align: str = FLOAT_ALIGN,
) -> Dict:
    """A dictionary of columns and formats for the Pandas DataFrame Styler

    Note if the index is 1-dimensional and the name is None we rename to 'index' in order to be able
    to format the index.

    For the complete formattings specification see [numbrojs](http://numbrojs.com/format.html)

    Args:
        data (pd.DataFrame): A DataFrame of data
        int_format (str, optional): The int format string. Defaults to INT_FORMAT.
        int_align (str, optional): [description]. Defaults to INT_ALIGN.
        float_format (str, optional): [description]. Defaults to FLOAT_FORMAT.
        float_align (str, optional): [description]. Defaults to FLOAT_ALIGN.

    Returns:
        Dict[str,str] -- A dictionary of default formats for the columns
    """
    formatters = {}
    for column in data.columns:
        if data[column].dtype == INT_DTYPE:
            formatters[column] = NumberFormatter(format=int_format, text_align=int_align)
        elif data[column].dtype == FLOAT_DTYPE:
            formatters[column] = NumberFormatter(format=float_format, text_align=float_align)

    if len(data.index.names) == 1 and not data.index.name:
        data.index.name = "index"

    for index, name in enumerate(data.index.names):
        if name:
            if data.index[index].dtype == INT_DTYPE:
                formatters[name] = NumberFormatter(format=int_format, text_align=int_align)
            elif data.index[index].dtype == FLOAT_DTYPE:
                formatters[name] = NumberFormatter(format=float_format, text_align=float_align)

    return formatters
