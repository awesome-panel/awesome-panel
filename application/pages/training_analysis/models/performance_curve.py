"""This module contains functionality to model a Performance Curve

An example is a Power Curve
"""
import datetime

import param

DATE_BOUNDS = (
    datetime.date(1980, 1, 1,),
    datetime.datetime.now().date(),
)


class PerformanceCurve(param.Parameterized):
    """A Model of a Performance Curve

    The default values are from the Power Curve of Marc Skov Madsen as of 2020-01-05
    """

    one_sec = param.Number(2582)
    one_sec_date = param.Date(datetime.date(2017, 11, 23,), bounds=DATE_BOUNDS,)
    two_sec = param.Number(2582)
    two_sec_date = param.Date(datetime.date(2017, 11, 23,), bounds=DATE_BOUNDS,)
    five_sec = param.Number(1707)
    five_sec_date = param.Date(datetime.date(2017, 11, 23,), bounds=DATE_BOUNDS,)
    ten_sec = param.Number(1079)
    ten_sec_date = param.Date(datetime.date(2018, 8, 21,), bounds=DATE_BOUNDS,)
    twenty_sec = param.Number(892)
    twenty_sec_date = param.Date(datetime.date(2018, 7, 29,), bounds=DATE_BOUNDS,)
    thirty_sec = param.Number(811)
    thirty_sec_date = param.Date(datetime.date(2017, 8, 31,), bounds=DATE_BOUNDS,)
    one_min = param.Number(684)
    one_min_date = param.Date(datetime.date(2017, 8, 31,), bounds=DATE_BOUNDS,)
    two_min = param.Number(511)
    two_min_date = param.Date(datetime.date(2017, 7, 27,), bounds=DATE_BOUNDS,)
    five_min = param.Number(424)
    five_min_date = param.Date(datetime.date(2017, 9, 22,), bounds=DATE_BOUNDS,)
    ten_min = param.Number(419)
    ten_min_date = param.Date(datetime.date(2017, 9, 22,), bounds=DATE_BOUNDS,)
    twenty_min = param.Number(398)
    twenty_min_date = param.Date(datetime.date(2017, 9, 22,), bounds=DATE_BOUNDS,)
    thirty_min = param.Number(362)
    thirty_min_date = param.Date(datetime.date(2017, 9, 22,), bounds=DATE_BOUNDS,)
    one_hour = param.Number(319)
    one_hour_date = param.Date(datetime.date(2017, 8, 6,), bounds=DATE_BOUNDS,)
    two_hour = param.Number(281)
    two_hour_date = param.Date(datetime.date(2018, 10, 28,), bounds=DATE_BOUNDS,)
    five_hour = param.Number(251)
    five_hour_date = param.Date(datetime.date(2017, 6, 5,), bounds=DATE_BOUNDS,)
