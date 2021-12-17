"""Implementation of a PyDeck pane"""
# Inspired by PyDeck
# Jinja: https://github.com/uber/deck.gl/blob/master/bindings/pydeck/pydeck/io/templates/index.j2

import panel as pn
import param
import pydeck as pdk
from awesome_panel.express.assets import DECK_GL_PANEL_EXPRESS_CSS

_EXTENDED = False


DECK_GL_PANEL_EXPRESS_JS = (
    "https://cdn.jsdelivr.net/npm/@deck.gl/jupyter-widget@^8.0.0/dist/index.js"
)
MAPBOX_GL_JS = "https://api.tiles.mapbox.com/mapbox-gl-js/v0.50.0/mapbox-gl.js"

# Right now this is not implemented as a Pane
# But eventually it should be
class PyDeck(param.Parameterized):
    """A PyDeck Pane

    This Pane can be used to convert a PyDeck object to a Panel in Panel.
    """

    object = param.Parameter(
        default=None,
        doc="""
        The pydeck Deck object being wrapped.""",
    )

    def __init__(
        self,
        object: pdk.Deck = None,
        **params,  # pylint: disable=redefined-builtin
    ):
        self.object = object
        super().__init__(**params)

    def _get_js(
        self,
        container: str = "deck-container",
    ):
        # Get
        json_input = self.object.to_json()
        mapbox_key = self.object.mapbox_key
        tooltip = self.object.deck_widget.tooltip

        # Clean
        if isinstance(
            json_input,
            str,
        ):
            json_input = json_input.replace(
                '"',
                "'",
            )
        if not isinstance(
            mapbox_key,
            str,
        ):
            mapbox_key = ""
        if isinstance(
            tooltip,
            bool,
        ):
            tooltip = str(tooltip).lower()

        return f"""\
const jsonInput = {json_input};
const MAPBOX_API_KEY = '{mapbox_key}';
const tooltip = {tooltip};

const deck = createDeck({{
    mapboxApiKey: MAPBOX_API_KEY,
    container: document.getElementById('{container}'),
    jsonInput,
    tooltip
}});"""

    @param.depends("object")
    def _repr_html_(
        self,
    ):
        # Inspired by the implementation of pydeck.Deck.to_html
        # See https://github.com/uber/deck.gl/blob/master/bindings/pydeck/pydeck/bindings/deck.py
        if not self.object:
            return ""

        js_code = self._get_js()

        html = f"""\
<div id="deck-container"></div>
<script>
{js_code}
</script>"""
        return html

    @property
    def as_pane(
        self,
    ) -> pn.pane.HTML:
        """Converts the _repr_html_ to a HTML pane"""
        return pn.pane.HTML(self._repr_html_())

    @staticmethod
    def extend():
        """## Extends Panel with CSS and JS functionality to use PyDeck and Deck.Gl."""
        global _EXTENDED  # pylint: disable=global-statement
        if not _EXTENDED:
            pn.config.raw_css.append(DECK_GL_PANEL_EXPRESS_CSS.read_text(encoding="utf8"))
            pn.config.js_files["deck"] = DECK_GL_PANEL_EXPRESS_JS
            pn.config.js_files["mapbox"] = MAPBOX_GL_JS
            _EXTENDED = True
