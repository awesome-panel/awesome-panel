"""This module contains functionality to model an Athlete

To keep track of things like weight, ftp, power curve etc.
"""
import datetime

import param

from .performance_curve import PerformanceCurve

DEFAULT_NAME = "Marc Skov Madsen"
DEFAULT_BIRTHDAY = datetime.date(1976, 9, 17)
DEFAULT_WEIGHT = 82  # kgs


class Athlete(param.Parameterized):
    """This module contains functionality to model an Athlete

    To keep track of things like weight, ftp, power curve etc.
    """

    name_ = param.String(DEFAULT_NAME)
    birthday = param.Date(DEFAULT_BIRTHDAY)
    weight = param.Number(default=DEFAULT_WEIGHT)
    power_curve = PerformanceCurve()
