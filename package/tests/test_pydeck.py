"""In this module we test the pydeck functionaly"""
# pylint: disable=redefined-outer-name,protected-access
from awesome_panel.express import PyDeck
import pydeck as pdk


def test__repr_html():
    # Given
    _deck = pdk.Deck()
    deck = PyDeck(_deck)
    # When
    actual = deck._repr_html_()
    # Then
    assert (
        actual
        == """\
<div id="deck-container"></div>
<script>
const jsonInput = {"layers": [], "mapStyle": "mapbox://styles/mapbox/dark-v9", "views": [{"@@type": "MapView", "controller": true}]};
const MAPBOX_API_KEY = 'None';
const tooltip = True;

const deck = createDeck({
    mapboxApiKey: MAPBOX_API_KEY,
    container: document.getElementById('deck-container'),
    jsonInput,
    tooltip
});
</script>"""
    )


def test__repr_html_none():
    # Given
    deck = PyDeck()
    # When
    actual = deck._repr_html_()
    # Then
    assert actual == ""
