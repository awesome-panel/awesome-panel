"""Here we demonstrate how create a custom Leaflet component using
[ReactiveHTML](https://panel.holoviz.org/user_guide/Custom_Components.html#reactivehtml-components).
"""
import panel as pn
import param

from awesome_panel import config

config.extension(url="reactive_leaflet")


class LeafletMap(pn.reactive.ReactiveHTML):  # pylint: disable = too-many-ancestors
    """Custom Leaflet Component"""

    marker1_clicks = param.Integer()
    marker2_clicks = param.Integer()
    marker3_clicks = param.Integer()

    _template = """<div id="mapid" style="height:100%"></div>"""

    __css__ = ["https://unpkg.com/leaflet@1.7.1/dist/leaflet.css"]
    __javascript__ = ["https://unpkg.com/leaflet@1.7.1/dist/leaflet.js"]

    _scripts = {
        "render": """
var mymap = L.map(mapid).setView([50, 0], 6);
state.map=mymap

var tileLayer = L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: 'pk.eyJ1IjoibWFyY3Nrb3ZtYWRzZW4iLCJhIjoiY2s1anMzcG5rMDYzazNvcm10NTFybTE4cSJ9.TV1XBgaMfR-iTLvAXM_Iew'
}).addTo(mymap)

var marker1 = L.marker([48, -2], name='marker1');
marker1.on('click', (e) => { data.marker1_clicks =  data.marker1_clicks + 1 })

var marker2 = L.marker([50, 0], name='marker2');
marker2.on('click', (e) => { data.marker2_clicks =  data.marker2_clicks + 1 })

var marker3 = L.marker([52, 2], name='marker3');
marker3.on('click', (e) => { data.marker3_clicks = data.marker3_clicks + 1 })

var layer1 = L.layerGroup([marker1, marker2, marker3]);
layer1.addTo(mymap)
L.control.layers({"tile1": tileLayer},{"layer1": layer1}).addTo(mymap);
""",
        # Need to resize leaflet map to size of outer container
        "after_layout": """
            state.map.invalidateSize();console.log("invalidated");
        """,
    }


leaflet_map = LeafletMap(min_height=700, sizing_mode="stretch_both")
clicks = pn.Param(
    leaflet_map,
    parameters=["marker1_clicks", "marker2_clicks", "marker3_clicks"],
    sizing_mode="fixed",
)

pn.Row(leaflet_map, clicks, sizing_mode="stretch_both").servable()
