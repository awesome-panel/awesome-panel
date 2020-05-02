"""In this module we define the Views of the PerformanceCurve"""
from typing import Optional

import panel as pn

from ..models.performance_curve import PerformanceCurve


class PerformanceCurveUpdateView(pn.Column):
    """A View for editing/ updating the Performance Curve"""

    def __init__(self, performance_curve: Optional[PerformanceCurve] = None, **kwargs):
        if performance_curve:
            self.performance_curve = performance_curve
        else:
            self.performance_curve = PerformanceCurve()

        super().__init__(
            pn.Row(
                self.performance_curve.param.one_sec,
                pn.Param(
                    self.performance_curve.param.one_sec_date,
                    widgets={"one_sec_date": pn.widgets.DatePicker},
                    align="center",
                ),
            ),
            pn.Row(
                self.performance_curve.param.two_sec,
                pn.Param(
                    self.performance_curve.param.two_sec_date,
                    widgets={"two_sec_date": pn.widgets.DatePicker},
                ),
            ),
            pn.Row(
                self.performance_curve.param.five_sec,
                pn.Param(
                    self.performance_curve.param.five_sec_date,
                    widgets={"five_sec_date": pn.widgets.DatePicker},
                ),
            ),
            pn.Row(
                self.performance_curve.param.ten_sec,
                pn.Param(
                    self.performance_curve.param.ten_sec_date,
                    widgets={"ten_sec_date": pn.widgets.DatePicker},
                ),
            ),
            pn.Row(
                self.performance_curve.param.twenty_sec,
                pn.Param(
                    self.performance_curve.param.twenty_sec_date,
                    widgets={"twenty_sec_date": pn.widgets.DatePicker},
                ),
            ),
            pn.Row(
                self.performance_curve.param.thirty_sec,
                pn.Param(
                    self.performance_curve.param.thirty_sec_date,
                    widgets={"thirty_sec_date": pn.widgets.DatePicker},
                ),
            ),
            pn.Row(
                self.performance_curve.param.one_min,
                pn.Param(
                    self.performance_curve.param.one_min_date,
                    widgets={"one_min_date": pn.widgets.DatePicker},
                ),
            ),
            pn.Row(
                self.performance_curve.param.two_min,
                pn.Param(
                    self.performance_curve.param.two_min_date,
                    widgets={"two_min_date": pn.widgets.DatePicker},
                ),
            ),
            pn.Row(
                self.performance_curve.param.five_min,
                pn.Param(
                    self.performance_curve.param.five_min_date,
                    widgets={"five_min_date": pn.widgets.DatePicker},
                ),
            ),
            pn.Row(
                self.performance_curve.param.ten_min,
                pn.Param(
                    self.performance_curve.param.ten_min_date,
                    widgets={"ten_min_date": pn.widgets.DatePicker},
                ),
            ),
            pn.Row(
                self.performance_curve.param.twenty_min,
                pn.Param(
                    self.performance_curve.param.twenty_min_date,
                    widgets={"twenty_min_date": pn.widgets.DatePicker},
                ),
            ),
            pn.Row(
                self.performance_curve.param.thirty_min,
                pn.Param(
                    self.performance_curve.param.thirty_min_date,
                    widgets={"thirty_min_date": pn.widgets.DatePicker},
                ),
            ),
            pn.Row(
                self.performance_curve.param.one_hour,
                pn.Param(
                    self.performance_curve.param.one_hour_date,
                    widgets={"one_hour_date": pn.widgets.DatePicker},
                ),
            ),
            pn.Row(
                self.performance_curve.param.two_hour,
                pn.Param(
                    self.performance_curve.param.two_hour_date,
                    widgets={"two_hour_date": pn.widgets.DatePicker},
                ),
            ),
            pn.Row(
                self.performance_curve.param.five_hour,
                pn.Param(
                    self.performance_curve.param.five_hour_date,
                    widgets={"five_hour_date": pn.widgets.DatePicker},
                ),
            ),
            **kwargs,
        )
