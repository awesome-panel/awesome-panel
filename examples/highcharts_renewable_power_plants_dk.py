"""Demo of complex data app using panel-highcharts with linked charts"""
import pandas as pd
import panel as pn
import panel_highcharts as ph
import param

from awesome_panel import config
from awesome_panel.assets.csv import RENEWABLE_POWER_PLANTS_DK

ph.config.js_files(
    mapdata=["countries/dk/dk-all"], highcharts_marker_clusters=True, highcharts_coloraxis=True
)
pn.config.js_files["proj4"] = "https://cdnjs.cloudflare.com/ajax/libs/proj4js/2.3.6/proj4.js"
ph.config.theme("auto")
config.extension("highchart", "highmap", "tabulator", url="highcharts_renewable_power_plants_dk")

MAX_SAMPLES = 1000
MAP_DATA_TRESHOLD = 1000

ACCENT_BASE_COLOR = config.ACCENT
SELECTED_COLOR = "#2c6b98"

if not "renewable_power_plants_dk" in pn.state.cache:
    pn.state.cache["renewable_power_plants_dk"] = pd.read_csv(RENEWABLE_POWER_PLANTS_DK)

DATA = pn.state.cache["renewable_power_plants_dk"]

tabulator = pn.widgets.Tabulator(
    value=DATA,
    theme="fast",
    page_size=25,
    pagination="remote",
    min_height=500,
    sizing_mode="stretch_both",
)

_, download_button = tabulator.download_menu(
    text_kwargs={"name": "Enter filename", "value": "source_data.csv"},
    button_kwargs={"name": "Download CSV", "button_type": "primary", "margin": (15, 10)},
)

DIMENSIONS = [
    "energy_source_level_2",
    "technology",
    "data_source",
    "nuts_2_region",
    "nuts_3_region",
    "manufacturer",
]
DIMENSION = DIMENSIONS[0]
MEASURE = "electrical_capacity"


def to_grouped_chart_data(dimension=DIMENSION, measure=MEASURE, data=DATA):
    """Returns a DataFrame for the grouped chart"""
    return (
        data[[dimension, measure]]
        .groupby(dimension)
        .sum()
        .round(0)
        .sort_values(measure, ascending=False)
        .reset_index()
    )


grouped_chart_data = to_grouped_chart_data()


def _to_grouped_chart_series_data(series, selected_index=-1):
    return [
        {"y": value, "color": SELECTED_COLOR if index == selected_index else ACCENT_BASE_COLOR}
        for index, value in series.items()
    ]


def to_grouped_chart_config(data, dimension=DIMENSION, measure=MEASURE, selected_index=-1):
    """Returns a HighCharts chart dict"""
    measure_data = _to_grouped_chart_series_data(data[MEASURE], selected_index)

    return {
        "chart": {"type": "bar"},
        "title": {"text": measure + " grouped by " + dimension},
        "subtitle": {
            "text": 'Source: <a href="https://data.open-power-system-data.org/renewable_power_plants/">open-power-system-data.org</a>'  # pylint: disable=line-too-long
        },
        "xAxis": {"categories": list(data[dimension]), "title": {"text": dimension}},
        "yAxis": {"min": 0, "labels": {"overflow": "justify"}},
        "tooltip": {"valueSuffix": " MW"},
        "plotOptions": {
            "bar": {"dataLabels": {"enabled": True}},
            "series": {"cursor": "pointer", "point": {"events": {"click": """@click"""}}},
        },
        "series": [
            {
                "name": measure,
                "data": measure_data,
            }
        ],
    }


class GroupByDimensionChartWithSelection(param.Parameterized):
    """Component for exploring grouped data for different dimensions"""

    dimension = param.ObjectSelector(DIMENSIONS[0], objects=DIMENSIONS)
    selected_value = param.String()
    selected_index = param.Integer()
    data = param.DataFrame()
    config = param.Dict()
    chart = param.ClassSelector(class_=ph.HighChart)
    view = param.Parameter()

    def __init__(self, **params):
        if "chart" not in params:
            params["chart"] = ph.HighChart(sizing_mode="stretch_both", margin=(25, 10))

        super().__init__(**params)

        self._update_chart()

        self.view = pn.Column(self.param.dimension, self.chart, sizing_mode="stretch_both")

    @param.depends("dimension", watch=True)
    def _update_chart(self):
        self.data = to_grouped_chart_data(self.dimension)
        self.selected_index = -1
        self.selected_value = ""
        self.config = to_grouped_chart_config(
            self.data, self.dimension, selected_index=self.selected_index
        )
        self.chart.object = self.config

    @param.depends("chart.event", watch=True)
    def _color_selection(self):
        index = self.chart.event["point"]["index"]
        if self.selected_index == index:
            self.selected_index = -1
            self.selected_value = ""
        else:
            self.selected_index = index
            self.selected_value = self.data[self.dimension][index]

        chart_config = {
            "series": [
                {
                    "data": _to_grouped_chart_series_data(
                        self.data["electrical_capacity"], self.selected_index
                    ),
                }
            ]
        }
        self.chart.object_update = chart_config


bar_chart_component = GroupByDimensionChartWithSelection()


def to_map_data(dimension=DIMENSIONS[0], selected_value=""):
    """Returns DataFrame of map data"""
    if selected_value:
        map_filter = DATA[dimension] == selected_value
        data = DATA[map_filter]
    else:
        data = DATA
    data = data[["address", "municipality", "lat", "lon", "manufacturer"]].copy()
    data["name"] = (
        data["address"].astype(str) + ", " + data["municipality"]
    )  # + ", " + data.index.astype(str)
    data = data.fillna("NA")
    samples = min(len(data), MAX_SAMPLES)
    records = (
        data[["name", "lat", "lon", "manufacturer"]]
        .sample(samples)
        .dropna(subset=["lat", "lon"])
        .to_dict("records")
    )
    return records


def get_map_chart_config(dimension=DIMENSION, selected_value=""):
    """Returns Highcharts map configuration dict"""
    series_data = to_map_data(dimension=dimension, selected_value=selected_value)
    return {
        "chart": {"map": "countries/dk/dk-all"},
        "title": {
            "text": "Renewable Power Plants DK",
        },
        "subtitle": {
            "text": f"Sample of {len(series_data)} plants only",
        },
        "mapNavigation": {"enabled": True},
        "tooltip": {
            "headerFormat": "",
            "pointFormat": "<b>{point.name}</b><br><b>{point.manufacturer}</b><br>Lat: {point.lat:.2f}, Lon: {point.lon:.2f}",  # pylint: disable=line-too-long
        },
        "colorAxis": {"min": 0, "max": 1000},
        "plotOptions": {
            "series": {
                "turboThreshold": MAP_DATA_TRESHOLD,
            },
            "mappoint": {
                "cluster": {
                    "enabled": True,
                    "allowOverlap": False,
                    "animation": {"duration": 450},
                    "layoutAlgorithm": {"type": "grid", "gridSize": 70},
                    "zones": [
                        {"from": 1, "to": 4, "marker": {"radius": 13}},
                        {"from": 5, "to": 9, "marker": {"radius": 15}},
                        {"from": 10, "to": 15, "marker": {"radius": 17}},
                        {"from": 16, "to": 20, "marker": {"radius": 19}},
                        {"from": 21, "to": 100, "marker": {"radius": 21}},
                    ],
                }
            },
        },
        "xAxis": {
            "minRange": 1,
        },
        "yAxis": {
            "minRange": 1,
        },
        "series": [
            {
                "name": "Basemap",
                "borderColor": "#A0A0A0",
                "backgroundColor": "yellow",
                "nullColor": "rgba(177, 244, 177, 0.5)",
                "showInLegend": False,
            },
            {
                "type": "mappoint",
                "enableMouseTracking": True,
                "colorKey": "clusterPointsAmount",
                "name": "Power Plants",
                "data": series_data,
            },
        ],
    }


map_chart_config = get_map_chart_config()
map_chart = ph.HighMap(map_chart_config, sizing_mode="stretch_both", margin=(25, 10))


def _update_map_chart(dimension=DIMENSIONS[0], selected_value=-1):
    map_chart.object = get_map_chart_config(dimension=dimension, selected_value=selected_value)


pn.bind(
    _update_map_chart,
    dimension=bar_chart_component.param.dimension,
    selected_value=bar_chart_component.param.selected_value,
    watch=True,
)

visualization_panel = pn.Row(
    bar_chart_component.view,
    pn.Column(pn.layout.HSpacer(height=51), map_chart, sizing_mode="stretch_both"),
    sizing_mode="stretch_both",
    name="VISUALIZATION",
)

source_data_panel = pn.Column(
    tabulator,
    download_button,
    """[The data](https://data.open-power-system-data.org/renewable_power_plants/) is from
[open-power-system-data.org](https://data.open-power-system-data.org/renewable_power_plants/).""",
    name="SOURCE DATA",
)

pn.Tabs(visualization_panel, source_data_panel, dynamic=True).servable()
