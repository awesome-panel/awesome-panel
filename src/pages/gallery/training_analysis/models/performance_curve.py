"""This module contains functionality to model Performance Curve

An example is a Power Curve
"""
import datetime

import param


class PerformanceCurve(param.Parameterized):
    """A Model of a Performance Curve

    The default values are from the Power Curve of Marc Skov Madsen as of 2020-01-05
    """
    one_sec = param.Number(2582)
    one_sec_date = param.Date(datetime.date(2017, 11, 23))
    two_sec = param.Number(2582)
    two_sec_date = param.Date(datetime.date(2017, 11, 23))
    five_sec = param.Number(1707)
    five_sec_date = param.Date(datetime.date(2017, 11, 23))
    ten_sec = param.Number(1079)
    ten_sec_date = param.Date(datetime.date(2018, 8, 21))
    twenty_sec = param.Number(892)
    twenty_sec_date = param.Date(datetime.date(2018, 7, 29))
    thirty_sec = param.Number(811)
    thirty_sec_date = param.Date(datetime.date(2017, 8, 31))
    one_min = param.Number(684)
    one_min_date = param.Date(datetime.date(2017, 8, 31))
    two_min = param.Number(511)
    two_min_date = param.Date(datetime.date(2017, 7, 27))
    five_min = param.Number(424)
    five_min_date = param.Date(datetime.date(2017, 9, 22))
    ten_min = param.Number(419)
    ten_min_date = param.Date(datetime.date(2017, 9, 22))
    twenty_min = param.Number(398)
    twenty_min_date = param.Date(datetime.date(2017, 9, 22))
    thirty_min = param.Number(362)
    thirty_min_date = param.Date(datetime.date(2017, 9, 22))
    one_hour = param.Number(319)
    one_hour_date = param.Date(datetime.date(2017, 8, 6))
    two_hour = param.Number(281)
    two_hour_date = param.Date(datetime.date(2018, 10, 28))
    five_hour = param.Number(251)
    five_hour_date = param.Date(datetime.date(2017, 6, 5))
