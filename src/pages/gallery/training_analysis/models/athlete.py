"""This module contains functionality to model an Athlete

To keep track of things like weight, ftp, power curve etc.
"""
import datetime

import param

from .performance_curve import PerformanceCurve

# Default Values

NAME = "Marc Skov Madsen"
BIRTHDAY = datetime.date(1976, 9, 17)
BIRTHDAY_BOUNDS = (datetime.date(1900, 1, 1), datetime.datetime.now().date())
WEIGHT = 82  # kgs
WEIGHT_BOUNDS = (20, 200)
POWER_CURVE = PerformanceCurve()


class Athlete(param.Parameterized):
    """This module contains functionality to model an Athlete

    To keep track of things like weight, ftp, power curve etc.
    """

    name_ = param.String(NAME)
    birthday = param.Date(BIRTHDAY, bounds=(BIRTHDAY_BOUNDS))
    weight = param.Number(default=WEIGHT, bounds=WEIGHT_BOUNDS)
    power_curve = param.ClassSelector(class_=PerformanceCurve, default=POWER_CURVE)
