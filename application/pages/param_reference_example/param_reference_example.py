"""
This app illustrates the usage of the **`pn.Param`** function. The `pn.Param` function is used to
layout, style and configure the widgets of a `param.Parameterized` class when using it in Panel.

It took me some time to get my head around how to use it. So I've created this app
that I hope can help you.

I have also contributed a **guided walk through** of this example to the Panel Reference Gallery.
You can find it [here](https://panel.holoviz.org/reference/panes/Param.html#panes-gallery-param).

In this app we build **a model a cycling Athlete and his PowerCurve**.

The PowerCurve is a recording of the athletes maximum power output in Watt per kg for fixed
durations of time.
"""

from application.template import get_template
import datetime

import hvplot.pandas  # pylint: disable=unused-import
import pandas as pd
import panel as pn
import param

DATE_BOUNDS = (
    datetime.date(
        1900,
        1,
        1,
    ),
    datetime.datetime.now().date(),
)

STYLE = """
<style>
.bk.app{
    border: 1px solid rgba(0,0,0,.125);
    border-radius: 0.25rem;
    box-shadow: 5px 5px 20px grey;
}
</style>
"""


def view() -> pn.viewable.Viewable:
    """A View of an Athlete and his Power Curve

    Returns:
        pn.viewable.Viewable: The main Viewable of the app.
    """
    pn.config.sizing_mode="stretch_width"
    athlete = Athlete()

    athlete_view = pn.Param(
        athlete,
        widgets={
            "birthday": pn.widgets.DatePicker,
            "weight": {
                "type": pn.widgets.LiteralInput,
                "width": 100,
            },
        },
        parameters=[
            "name_",
            "birthday",
            "weight",
        ],
        show_name=False,
        default_layout=pn.Row,
        width=600,
    )

    power_curve_two_columns_view = pn.Param(
        athlete.power_curve,
        default_layout=GridBoxWithTwoColumns,
        show_name=False,
        widgets={
            "ten_sec_date": pn.widgets.DatePicker,
            "one_min_date": pn.widgets.DatePicker,
            "ten_min_date": pn.widgets.DatePicker,
            "twenty_min_date": pn.widgets.DatePicker,
            "one_hour_date": pn.widgets.DatePicker,
        },
    )

    power_curve_with_plot_view = pn.Row(
        power_curve_two_columns_view,
        pn.layout.VSpacer(width=25),
        athlete.power_curve.plot,
        pn.layout.VSpacer(width=10),
    )

    main = [
        STYLE,
        pn.layout.Card(
            pn.pane.Markdown(__doc__), title="Param Reference Example",
        ),
        pn.layout.HSpacer(height=25),
        pn.Column(
            pn.Column(
                pn.pane.Markdown("### Athlete"),
                athlete_view,
                pn.pane.Markdown("#### Power Curve"),
                power_curve_with_plot_view,
                margin=20,
            ),
            css_classes=["app"],
        ),
    ]
    return get_template(title="Param Reference Example", main=main)


class PowerCurve(param.Parameterized):
    """A Model of a Power Curve of an Athlete

    The PowerCurve is a recording of the athletes maximum power output in Watt per kg for fixed
    durations.
    """

    ten_sec = param.Number(1079)
    ten_sec_date = param.Date(
        datetime.date(
            2018,
            8,
            21,
        ),
        bounds=DATE_BOUNDS,
    )
    one_min = param.Number(684)
    one_min_date = param.Date(
        datetime.date(
            2017,
            8,
            31,
        ),
        bounds=DATE_BOUNDS,
    )
    ten_min = param.Number(419)
    ten_min_date = param.Date(
        datetime.date(
            2017,
            9,
            22,
        ),
        bounds=DATE_BOUNDS,
    )
    twenty_min = param.Number(398)
    twenty_min_date = param.Date(
        datetime.date(
            2017,
            9,
            22,
        ),
        bounds=DATE_BOUNDS,
    )
    one_hour = param.Number(319)
    one_hour_date = param.Date(
        datetime.date(
            2017,
            8,
            6,
        ),
        bounds=DATE_BOUNDS,
    )

    @param.depends(
        "ten_sec",
        "one_min",
        "ten_min",
        "twenty_min",
        "one_hour",
    )
    def plot(
        self,
    ):
        """A plot of the power curve: duration vs power"""
        data = {
            "duration": [
                10 / 60,
                1,
                10,
                20,
                60,
            ],
            "power": [
                self.ten_sec,
                self.one_min,
                self.ten_min,
                self.twenty_min,
                self.one_hour,
            ],
        }
        dataframe = pd.DataFrame(data)
        line_plot = dataframe.hvplot.line(
            x="duration",
            y="power",
            width=300,
            line_color="#007BFF",
            line_width=3,
        )
        scatter_plot = dataframe.hvplot.scatter(x="duration", y="power", width=300,).opts(
            marker="o",
            size=6,
            color="#007BFF",
        )
        fig = line_plot * scatter_plot
        gridstyle = {
            "grid_line_color": "black",
            "grid_line_width": 0.1,
        }
        fig = fig.opts(
            responsive=True,
            toolbar=None,
            yticks=list(
                range(
                    0,
                    1600,
                    200,
                )
            ),
            ylim=(
                0,
                1500,
            ),
            gridstyle=gridstyle,
            show_grid=True,
        )
        return fig


class Athlete(param.Parameterized):
    """A model of an Athlete"""

    name_ = param.String("P.A. Nelson")
    birthday = param.Date(
        datetime.date(
            1976,
            9,
            17,
        ),
        bounds=DATE_BOUNDS,
    )
    weight = param.Number(
        default=82,
        bounds=(
            20,
            300,
        ),
    )
    power_curve = param.ClassSelector(
        class_=PowerCurve,
        default=PowerCurve(),
    )


class GridBoxWithTwoColumns(pn.GridBox):
    """A Custom Gridbox with 2 columns"""

    def __init__(self, *objects, **params):
        super().__init__(*objects, **params, ncols=2)


if __name__.startswith("bokeh"):
    view().servable()
