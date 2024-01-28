import os

import mapwidget.cesium as mapwidget

import panel as pn

pn.extension("ipywidgets")

try:
    token = os.environ["CESIUM_TOKEN"]
except KeyError as ex:
    raise EnvironmentError(
        "CESIUM_TOKEN environment variable not set. "
        "Sign up for free and get a free Cesium token here https://ion.cesium.com/signup/"
    ) from ex

cesium_map = mapwidget.Map(
    center=[40.70605, -74.01177], height="650px", altitude=600, token=token
)

component = pn.panel(cesium_map, sizing_mode="stretch_width")

description = """# MapWidget
Custom Jupyter widgets for creating interactive 2D/3D maps using popular JavaScript libraries with bidirectional communication, such as `Cesium`, `Mapbox`, `MapLibre`, `Leaflet`, and `OpenLayers`.
By **Qiusheng Wu**
<img src="https://avatars.githubusercontent.com/u/5016453?v=4" style="width:100%;"> 
# Cesium
Cesium is the open platform for software applications designed to unleash the power of 3D data.
<img src="https://images.prismic.io/cesium/a4dc3936-e083-4337-ba48-bb5bba78b2a1_ion_color_white.png" style="width:100%;"> 
"""

pn.template.FastListTemplate(
    site="Awesome Panel",
    site_url="https://awesome-panel.org",
    logo="https://panel.holoviz.org/_static/logo_horizontal_dark_theme.png",
    title="mapwidget.cesium",
    main=[component],
    sidebar=[description],
).servable()