"""
The purpose of this app is to demonstrate that Panel works with the tools you know and love
&#10084;&#65039;, including Deck.gl. It supports both light and dark theme.
"""
from typing import Dict

import panel as pn

from awesome_panel import config

config.extension("deckgl", url="lib_deckgl")

THEME = config.get_theme()
JSON_THEME = config.get_json_theme()

# Please create your own access token one your own Access tokens page
# https://account.mapbox.com/access-tokens/
MAPBOX_KEY = (
    "pk.eyJ1IjoicGFuZWxvcmciLCJhIjoiY2s1enA3ejhyMWhmZjNobjM1NXhtbWRrMyJ9.B_frQsAVepGIe-HiOJeqvQ"
)


def get_plot(theme=THEME) -> Dict:
    """Returns a Deck.gl plot"""
    if theme == "dark":
        deckgl_map_style = "mapbox://styles/mapbox/dark-v9"
    else:
        deckgl_map_style = "mapbox://styles/mapbox/light-v9"
    # pylint: disable=line-too-long
    return {
        "initialViewState": {
            "bearing": -27.36,
            "latitude": 52.2323,
            "longitude": -1.415,
            "maxZoom": 15,
            "minZoom": 5,
            "pitch": 40.5,
            "zoom": 6,
        },
        "layers": [
            {
                "@@type": "HexagonLayer",
                "autoHighlight": True,
                "coverage": 1,
                "data": "https://raw.githubusercontent.com/uber-common/deck.gl-data/master/examples/3d-heatmap/heatmap-data.csv",
                "elevationRange": [0, 3000],
                "elevationScale": 50,
                "extruded": True,
                "getPosition": "@@=[lng, lat]",
                "id": "8a553b25-ef3a-489c-bbe2-e102d18a3211",
                "pickable": True,
            }
        ],
        "mapStyle": deckgl_map_style,
        "views": [{"@@type": "MapView", "controller": True}],
    }


plot = get_plot()
deckgl_pane = pn.pane.DeckGL(
    plot, mapbox_api_key=MAPBOX_KEY, sizing_mode="stretch_both", height=700
).servable()


def hover_data(value, theme=JSON_THEME):
    """Returns the hover data"""
    if not value:
        value = {}
    return pn.pane.JSON(value, theme=theme, name="Hover Data", depth=3, height=200)


pn.Column(
    "## Hover data",
    pn.bind(hover_data, deckgl_pane.param.hover_state),
).servable()
