"""[Deck.gl](https://deck.gl/#/) is an awesome WebGL-powered framework for visual exploratory data
analysis of large datasets. And PyDeck provides Python bindings via
[PyDeck](https://deckgl.readthedocs.io/en/latest/)


It would be so nice to be able to use in Panel. See
[Feature Request 957](https://github.com/holoviz/panel/issues/957).

For now i've implemented a first, very simple, one way communication.
I.e. you can declare your visualisation in Python using PyDeck and display it in your browser.
"""
import panel as pn
import pydeck as pdk

import awesome_panel.express as pnx
from awesome_panel.express.testing import TestApp

UK_ACCIDENTS_DATA = (
    "https://raw.githubusercontent.com/uber-common/"
    "deck.gl-data/master/examples/3d-heatmap/heatmap-data.csv"
)

pnx.PyDeck.extend()
MAPBOX_KEY = (
    "pk.eyJ1IjoibWFyY3Nrb3ZtYWRzZW4iLCJhIjoiY2s1anMzcG5rMDYzazNvcm10NTFybTE4cSJ9."
    "TV1XBgaMfR-iTLvAXM_Iew"
)


def uk_accidents_example() -> pdk.Deck:
    """The UK Accidents Deck

    See [PyDec Docs](https://deckgl.readthedocs.io/en/latest/layer.html)

    Returns:
        pdk.Deck: The UK Accidents Deck
    """
    # 2014 location of car accidents in the UK

    # Define a layer to display on a map
    layer = pdk.Layer(
        "HexagonLayer",
        UK_ACCIDENTS_DATA,
        get_position=["lng", "lat",],
        auto_highlight=True,
        elevation_scale=50,
        pickable=True,
        elevation_range=[0, 3000,],
        extruded=True,
        coverage=1,
    )

    # Set the viewport location
    view_state = pdk.ViewState(
        longitude=-1.415,
        latitude=52.2323,
        zoom=6,
        min_zoom=5,
        max_zoom=15,
        pitch=40.5,
        bearing=-27.36,
    )

    # Combined all of it and render a viewport
    return pdk.Deck(layers=[layer], initial_view_state=view_state, mapbox_key=MAPBOX_KEY,)


def test_pydeck_pane():
    """We test that we can display the UK Accidents Data example from the
    [PyDec Docs](https://deckgl.readthedocs.io/en/latest/layer.html) in Panel."""
    deck = uk_accidents_example()
    # deck.to_html("test.html", open_browser=True, notebook_display=False)
    return TestApp(test_pydeck_pane, pnx.PyDeck(deck).as_pane, width=500, height=400,)


def view() -> pn.Column:
    """Wraps all tests in a Column that can be included in the Gallery or served independently

    Returns:
        pn.Column -- A Column containing all the tests
    """
    return pn.Column(pn.pane.Markdown(__doc__), test_pydeck_pane,)


if __name__.startswith("bk"):
    view().servable("test_deck_gl")
