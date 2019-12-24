"""In this example we show how to construct an interactive
[Choropleth](ps://en.wikipedia.org/wiki/Choropleth_map) map.

The example is heavily inspired by the article
[Choropleth maps with geopandas, Bokeh and Panel](https://dmnfarrell.github.io/bioinformatics/bokeh-maps)
by [Damian Farrell](https://github.com/dmnfarrell). See also his
[Notebook](https://github.com/dmnfarrell/teaching/blob/master/geo/maps_python.ipynb)

If you wan't to `pip install geopandas` on Windows then please follow the
[using-geopandas-windows](https://geoffboeing.com/2014/09/using-geopandas-windows/) article.
"""

import json
import pathlib

import geopandas as gpd
import pandas as pd
import panel as pn
import panel.widgets as pnw
from bokeh.io import export_png, output_file, output_notebook, show
from bokeh.models import (ColorBar, ColumnDataSource, GeoJSONDataSource,
                          LinearColorMapper)
from bokeh.models.widgets import DataTable
from bokeh.palettes import brewer
from bokeh.plotting import figure

FILE_DIR = pathlib.Path(__file__).parent
shapefile = FILE_DIR / "data/ne_110m_admin_0_countries.shp"
# Read shapefile using Geopandas
gdf = gpd.read_file(shapefile)[["ADMIN", "ADM0_A3", "geometry"]]
# Rename columns.
gdf.columns = ["country", "country_code", "geometry"]
gdf = gdf.drop(gdf.index[159])

owid = pd.read_csv(FILE_DIR / "data/owid.csv").set_index("name")

def get_dataset(name, key=None, year=None):
    url = owid.loc[name].url
    df = pd.read_csv(url)
    if year is not None:
        df = df[df["Year"] == year]
    # Merge dataframes gdf and df_2016.
    if key is None:
        key = df.columns[2]
    merged = gdf.merge(df, left_on="country", right_on="Entity", how="left")
    merged[key] = merged[key].fillna(0)
    return merged, key


def get_geodatasource(gdf):
    """Get getjsondatasource from geopandas object"""
    json_data = json.dumps(json.loads(gdf.to_json()))
    return GeoJSONDataSource(geojson=json_data)


def bokeh_plot_map(gdf, column=None, title=""):
    """Plot bokeh map from GeoJSONDataSource """

    geosource = get_geodatasource(gdf)
    palette = brewer["OrRd"][8]
    palette = palette[::-1]
    vals = gdf[column]
    # Instantiate LinearColorMapper that linearly maps numbers in a range, into a sequence of colors.
    color_mapper = LinearColorMapper(palette=palette, low=vals.min(), high=vals.max())
    color_bar = ColorBar(
        color_mapper=color_mapper,
        label_standoff=8,
        width=500,
        height=20,
        location=(0, 0),
        orientation="horizontal",
    )

    tools = "wheel_zoom,pan,reset"
    p = figure(title=title, plot_height=400, plot_width=850, toolbar_location="right", tools=tools)
    p.xgrid.grid_line_color = None
    p.ygrid.grid_line_color = None
    # Add patch renderer to figure
    p.patches(
        "xs",
        "ys",
        source=geosource,
        fill_alpha=1,
        line_width=0.5,
        line_color="black",
        fill_color={"field": column, "transform": color_mapper},
    )
    # Specify figure layout.
    p.add_layout(color_bar, "below")
    return p

def view():
    """Map dashboard"""



    map_pane = pn.pane.Bokeh(width=400)
    data_select = pnw.Select(name="dataset", options=list(owid.index))
    year_slider = pnw.IntSlider(start=1950, end=2018, value=2010)

    def update_map(event):
        gdf, key = get_dataset(name=data_select.value, year=year_slider.value)
        map_pane.object = bokeh_plot_map(gdf, key)
        return

    year_slider.param.watch(update_map, "value")
    year_slider.param.trigger("value")
    data_select.param.watch(update_map, "value")
    app = pn.Column(pn.Row(data_select, year_slider), map_pane)
    return app


if __name__.startswith("bk"):
    view().servable()
