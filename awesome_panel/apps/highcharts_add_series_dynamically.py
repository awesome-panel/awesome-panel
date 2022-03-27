"""Data app showing how to add an extra series to an existing HighCharts chart"""
import panel as pn
import panel_highcharts as ph

from awesome_panel import config

ph.config.theme("auto")

config.extension("highchart", url="highcharts_add_series_dynamically")

PRIMARY = config.ACCENT
SECONDARY = config.PALETTE[1]

CONFIGURATION = {
    "xAxis": {
        "categories": [
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
            "Oct",
            "Nov",
            "Dec",
        ]
    },
    "series": [
        {
            "data": [
                29.9,
                71.5,
                106.4,
                129.2,
                144.0,
                176.0,
                135.6,
                148.5,
                216.4,
                194.1,
                95.6,
                54.4,
            ],
            "color": PRIMARY,
        }
    ],
}

OPTIONS = {
    "data": [
        194.1,
        95.6,
        54.4,
        29.9,
        71.5,
        106.4,
        129.2,
        144.0,
        176.0,
        135.6,
        148.5,
        216.4,
    ]
}


button = pn.widgets.Button(name="Add Series", button_type="primary")


chart = ph.HighChart(object=CONFIGURATION, sizing_mode="stretch_both")


pn.Column(button, chart, sizing_mode="stretch_both").servable()


def handle_button_click(_):
    """Will add a series or reset the chart"""
    if button.name == "Add Series":
        chart.add_series(options=OPTIONS.copy(), redraw=True, animation=True)
        button.name = "Reset Chart"
    else:
        chart.object = {}  # Hack to get it to update
        chart.object = CONFIGURATION
        button.name = "Add Series"


button.on_click(handle_button_click)
