"""In this app we provide visual insights into the worlds power plants using
DeckGL and PyDeck"""

import pathlib
from typing import Optional

import pandas as pd
import panel as pn
import param
import pydeck as pdk

POWER_PLANT_URL = (
    "https://raw.githubusercontent.com/MarcSkovMadsen/awesome-streamlit/master/"
    "gallery/global_power_plant_database/global_power_plant_database.csv"
)
ROOT = pathlib.Path(__file__).parent
POWER_PLANT_PATH = ROOT / "global_power_plant_database.csv"

MAPBOX_KEY = (
    "pk.eyJ1IjoibWFyY3Nrb3ZtYWRzZW4iLCJhIjoiY2s1anMzcG5rMDYzazNvcm10NTFybTE4cSJ9."
    "TV1XBgaMfR-iTLvAXM_Iew"
)

FUEL_COLORS = {
    "Oil": "black",
    "Solar": "green",
    "Gas": "black",
    "Other": "gray",
    "Hydro": "blue",
    "Coal": "black",
    "Petcoke": "black",
    "Biomass": "green",
    "Waste": "green",
    "Cogeneration": "gray",
    "Storage": "orange",
    "Wind": "green",
}

COLORS_R = {"black": 0, "green": 0, "blue": 0, "orange": 255, "gray": 128}
COLORS_G = {"black": 0, "green": 128, "blue": 0, "orange": 165, "gray": 128}
COLORS_B = {"black": 0, "green": 0, "blue": 255, "orange": 0, "gray": 128}

VIEW_STATES = {
    "World": pdk.ViewState(latitude=52.2323, longitude=-1.415, zoom=1),
    "Gentofte, DK": pdk.ViewState(latitude=55.7578314, longitude=12.5140001, zoom=6),
    "Skærbæk, DK": pdk.ViewState(latitude=55.5158503, longitude=9.6207391, zoom=6),
    "Taipei, Taiwan": pdk.ViewState(latitude=25.0318932, longitude=121.5661063, zoom=6),
    "Horns Rev 2, DK": pdk.ViewState(latitude=55.5333558, longitude=7.9658237, zoom=6),
    "Kuala Lumpur, Malaysis": pdk.ViewState(latitude=3.1116255, longitude=101.663948, zoom=6),
    "Anholt, DK": pdk.ViewState(latitude=56.5975418, longitude=11.1720228, zoom=6),
    "Borkum Riffgrund 1, DE": pdk.ViewState(latitude=53.8333333, longitude=5.3793945, zoom=6),
    "Gode Wind 2, DE": pdk.ViewState(latitude=54.041, longitude=6.995, zoom=6),
    "London Array, UK": pdk.ViewState(latitude=51.3285692, longitude=1.4211854, zoom=6),
    "Lincs, UK": pdk.ViewState(latitude=53.1518117, longitude=0.5247279, zoom=6),
    "Walney": pdk.ViewState(latitude=54.0373667, longitude=-2.9673396, zoom=6),
    "West of Duddon Sands": pdk.ViewState(latitude=54.106667, longitude=-3.3870134, zoom=6),
    "Westermost Rough, UK": pdk.ViewState(latitude=53.7810064, longitude=0.2126456, zoom=6),
    "Race Bank, UK": pdk.ViewState(latitude=53.242301, longitude=0.8377461, zoom=6),
}


class GlobalPowerPlantDatabaseApp(param.Parameterized):

    data = param.DataFrame(precedence=-1)

    opacity = param.Number(default=0.8, step=0.05, bounds=(0, 1))

    pitch = param.Number(default=0, bounds=(0, 90))

    zoom = param.Integer(default=1, bounds=(1, 22))

    view_state = param.ObjectSelector(default=VIEW_STATES["World"], objects=VIEW_STATES)

    def __init__(self, nrows: Optional[int] = None, **params):
        if "data" not in params:
            if nrows:
                params["data"] = self._get_pp_data(nrows=nrows)
            else:
                params["data"] = self._get_pp_data()

        super(GlobalPowerPlantDatabaseApp, self).__init__(**params)

        self._view_state = pdk.ViewState(
            latitude=52.2323,
            longitude=-1.415,
            zoom=self.zoom,
            min_zoom=self.param.zoom.bounds[0],
            max_zoom=self.param.zoom.bounds[1],
        )
        self._scatter = pdk.Layer(
            "ScatterplotLayer",
            data=self.data,
            get_position=["longitude", "latitude"],
            get_fill_color="[color_r, color_g, color_b, color_a]",
            get_radius="capacity_mw*10",
            pickable=True,
            opacity=self.opacity,
            filled=True,
            wireframe=True,
        )
        self._deck = pdk.Deck(
            map_style="mapbox://styles/mapbox/light-v9",
            initial_view_state=self._view_state,
            layers=[self._scatter],
            tooltip=True,
            mapbox_key=MAPBOX_KEY,
        )
        self.pane = pn.pane.DeckGL(self._deck, sizing_mode="stretch_width", height=700)
        self.param.watch(self._update, ["data", "opacity", "pitch", "zoom"])

    @staticmethod
    def _get_pp_data(nrows: Optional[int] = None):
        pp_data = pd.read_csv(POWER_PLANT_PATH, nrows=nrows)

        pp_data["primary_fuel_color"] = pp_data.primary_fuel.map(FUEL_COLORS)
        pp_data["primary_fuel_color"] = pp_data["primary_fuel_color"].fillna("gray")
        pp_data["color_r"] = pp_data["primary_fuel_color"].map(COLORS_R)
        pp_data["color_g"] = pp_data["primary_fuel_color"].map(COLORS_G)
        pp_data["color_b"] = pp_data["primary_fuel_color"].map(COLORS_B)
        pp_data["color_a"] = 140

        # "name", "primary_fuel", "capacity_mw",
        pp_data = pp_data[
            [
                "latitude",
                "longitude",
                "name",
                "capacity_mw",
                "color_r",
                "color_g",
                "color_b",
                "color_a",
            ]
        ]
        return pp_data

    @pn.depends("pane.hover_state", "data")
    def _info_pane(self):
        index = self.pane.hover_state.get("index", -1)
        if index == -1:
            index = slice(0, 0)
        return self.data.iloc[index][["name", "capacity_mw"]]

    @pn.depends("view_state", watch=True)
    def _update_view_state_from_selection(self):
        self._view_state.latitude = self.view_state.latitude
        self._view_state.longitude = self.view_state.longitude
        self._view_state.zoom = self.view_state.zoom
        self.pane.param.trigger("object")

    @pn.depends("pane.view_State", watch=True)
    def _update(self):
        state = self.pane.view_state
        self._view_state.longitude = state["longitude"]
        self._view_state.latitude = state["latitude"]

    def _update2(self, event):
        if event.name == "data":
            self._scatter.data = self.data
        if event.name == "opacity":
            self._scatter.opacity = self.opacity
        if event.name == "zoom":
            self._view_state.zoom = self.zoom
        if event.name == "pitch":
            self._view_state.pitch = self.pitch
        self.pane.param.trigger("object")

    def _view_state_pane(self):
        return pn.Param(
            self,
            parameters=["view_state"],
            show_name=False,
            widgets={"view_state": pn.widgets.RadioButtonGroup},
            default_layout=pn.Column,
        )

    def _settings_pane(self):
        return pn.Param(
            self,
            parameters=["opacity", "pitch", "zoom"],
            show_name=False,
            widgets={"view_state": pn.widgets.RadioButtonGroup},
        )

    def view(self):
        # self._info_pane,  does not work
        return pn.Row(
            pn.Column(self._view_state_pane, self.pane),
            pn.Column(self._settings_pane, width=300, sizing_mode="fixed"),
        )


def view(nrows: Optional[int] = None):
    app = GlobalPowerPlantDatabaseApp(nrows=nrows)
    return app.view()


if __name__.startswith("bokeh"):
    pn.config.sizing_mode = "stretch_width"
    NROWS = None
    view(nrows=NROWS).servable()
