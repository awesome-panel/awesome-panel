"""
The purpose of this app is to demonstrate that Panel works with the tools you know and love
&#10084;&#65039;, including PyDeck. It supports both light and dark theme.
"""
import panel as pn
import pydeck

from awesome_panel import config

config.extension("deckgl", url="lib_pydeck")

ACCENT = config.ACCENT
THEME = config.get_theme()
JSON_THEME = config.get_json_theme()


def get_plot(theme=THEME, accent_base_color=ACCENT):
    """Returns a PyDeck plot"""
    land_cover = [[[-123.0, 49.196], [-123.0, 49.324], [-123.306, 49.324], [-123.306, 49.196]]]
    polygon = pydeck.Layer(
        "PolygonLayer",
        land_cover,
        stroked=False,
        # processes the data as a flat longitude-latitude pair
        get_polygon="-",
        get_fill_color=[0, 0, 0, 20],
    )

    data_url = "https://raw.githubusercontent.com/uber-common/deck.gl-data/master/examples/geojson/vancouver-blocks.json"  # pylint: disable=line-too-long
    geojson = pydeck.Layer(
        "GeoJsonLayer",
        data_url,
        opacity=0.8,
        stroked=False,
        filled=True,
        extruded=True,
        wireframe=True,
        get_elevation="properties.valuePerSqm / 20",
        get_fill_color="[255, 255, properties.growth * 255]",
        get_line_color=[255, 255, 255],
        pickable=True,
    )

    if theme == "dark":
        deckgl_map_style = "mapbox://styles/mapbox/dark-v9"
    else:
        deckgl_map_style = "mapbox://styles/mapbox/light-v9"
    initial_view_state = pydeck.ViewState(
        latitude=49.254, longitude=-123.13, zoom=11, max_zoom=16, pitch=45, bearing=0
    )

    deck = pydeck.Deck(
        layers=[polygon, geojson],
        initial_view_state=initial_view_state,
        map_style=deckgl_map_style,
    )

    # Tooltip (you can get the id directly from the layer object)
    geojson_tooltip = {
        "html": """
        <b>Value per Square meter:</b> {properties.valuePerSqm}<br>
        <b>Growth:</b> {properties.growth}
        """,
        "style": {"backgroundColor": accent_base_color, "color": "white"},
    }
    tooltips = {geojson.id: geojson_tooltip}
    return deck, tooltips


PLOT, TOOLTIPS = get_plot()

deckgl_pane = pn.pane.DeckGL(
    PLOT, tooltips=TOOLTIPS, height=800, sizing_mode="stretch_both"
).servable()


def hover_data(value, theme=JSON_THEME):
    """Returns the hover data"""
    if not value:
        value = {}
    return pn.pane.JSON(value, theme=theme, name="Hover Data", depth=3, height=200)


pn.Column(
    "## Hover data",
    pn.bind(hover_data, deckgl_pane.param.hover_state),  # type: ignore
).servable()
