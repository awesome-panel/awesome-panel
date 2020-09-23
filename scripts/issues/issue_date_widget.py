"""I cannot set the widget to a Slider for a Parameterized Class"""

import datetime

import panel as pn
import param

start = datetime.date(
    2019,
    1,
    1,
)
end = datetime.date(
    2021,
    1,
    1,
)
default = datetime.date(
    2020,
    1,
    1,
)


class CustomExample(param.Parameterized):
    """An example Parameterized class"""

    select_string = param.Selector(
        objects=[
            "red",
            "yellow",
            "green",
        ]
    )
    date = param.CalendarDate(
        default=default,
        bounds=(
            start,
            end,
        ),
    )
    number = param.Number(
        default=0,
        bounds=(
            -5.0,
            5.0,
        ),
    )


view = pn.Param(
    CustomExample.param,
    widgets={
        "select_string": pn.widgets.RadioButtonGroup,
        "date": pn.widgets.DatePicker,
        "number": pn.widgets.FloatSlider,
    },
)

app = pn.Column(
    __doc__,
    view,
    pn.pane.Markdown("# Stand Alone Widget"),
    width=1000,
)
app.servable()
