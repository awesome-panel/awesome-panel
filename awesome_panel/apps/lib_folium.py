"""
The purpose of this app is to demonstrate that Panel works with the tools you know and love
&#10084;&#65039;, including Folium.
"""
from html import escape  # noqa

import folium
import panel as pn

from awesome_panel import config

config.extension(url="lib_folium")

# pylint: disable=protected-access


def get_plot():
    """Returns a Folium plot"""
    plot = folium.Map(
        location=[45.372, -121.6972], zoom_start=12, tiles="Stamen Terrain"
    )  # ,  width='100%', height="50%")

    folium.Marker(
        location=[45.3288, -121.6625],
        popup="Mt. Hood Meadows",
        icon=folium.Icon(icon="cloud"),
    ).add_to(plot)

    folium.Marker(
        location=[45.3311, -121.7113],
        popup="Timberline Lodge",
        icon=folium.Icon(color="green"),
    ).add_to(plot)

    folium.Marker(
        location=[45.3300, -121.6823],
        popup="Some Other Location",
        icon=folium.Icon(color="red", icon="info-sign"),
    ).add_to(plot)
    return plot


PLOT = get_plot()


def _get_properties(self):
    properties = pn.pane.HTML._get_properties(self)
    text = "" if self.object is None else self.object
    if hasattr(text, "_repr_html_"):
        text = text._repr_html_()
        # pylint: disable=line-too-long
        before = '<div style="width:100%;"><div style="position:relative;width:100%;height:0;padding-bottom:60%;">'
        after = '<div style="width:100%;height:100%"><div style="position:relative;width:100%;height:100%;padding-bottom:0%;">'
        text = text.replace(before, after)
    return dict(properties, text=escape(text))


# A Hack to be able to get responsive Folium plots
pn.pane.plot.Folium._get_properties = _get_properties

pn.pane.plot.Folium(PLOT, min_height=700, sizing_mode="stretch_both").servable()
