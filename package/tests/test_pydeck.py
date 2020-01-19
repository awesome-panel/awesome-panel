"""In this module we test the pydeck functionaly"""
import pydeck as pdk

# pylint: disable=redefined-outer-name,protected-access
from awesome_panel.express import PyDeck


def test__repr_html():
    """We need a way to convert a pydeck.Deck into HTML that can be shown in a Pane in Panel.

    We test that functionality here.
    """
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
const jsonInput = {'layers': [], 'mapStyle': 'mapbox://styles/mapbox/dark-v9', 'views': [{'@@type': 'MapView', 'controller': true}]};
const MAPBOX_API_KEY = '';
const tooltip = true;

const deck = createDeck({
    mapboxApiKey: MAPBOX_API_KEY,
    container: document.getElementById('deck-container'),
    jsonInput,
    tooltip
});
</script>"""
    )


def test__repr_html_none():
    """If no pydeck.Deck is specified then the _repr_html should be the empty string"""
    # Given
    deck = PyDeck()
    # When
    actual = deck._repr_html_()
    # Then
    assert actual == ""
