"""In this example we show how to construct an interactive
[Choropleth](ps://en.wikipedia.org/wiki/Choropleth_map) map.

The example is heavily inspired by the article
[Choropleth maps with geopandas, Bokeh and Panel]\
(https://dmnfarrell.github.io/bioinformatics/bokeh-maps)
by [Damian Farrell](https://github.com/dmnfarrell). See also his
[Notebook](https://github.com/dmnfarrell/teaching/blob/master/geo/maps_python.ipynb)

If you wan't to `pip install geopandas` on Windows then please follow the
[using-geopandas-windows](https://geoffboeing.com/2014/09/using-geopandas-windows/) article.
"""

import json
import pathlib
from typing import Optional

import geopandas as gpd
import pandas as pd
import panel as pn
import panel.widgets as pnw
from bokeh.models import ColorBar, GeoJSONDataSource, LinearColorMapper
from bokeh.palettes import brewer  # pylint: disable=no-name-in-module
from bokeh.plotting import figure

FILE_DIR = pathlib.Path(__file__).parent
SHAPEFILE = FILE_DIR / "data/ne_110m_admin_0_countries.shp"
OWIDDATASETS_FILE = FILE_DIR / "data/owid_datasets.csv"


class OwidDashboard:
    """A Dashboard showing the Owid World Data like 'Annual CO2 Emissions'

        Args:
            shape_data (Optional[gpd.geodataframe.GeoDataFrame], optional): The Map shape data.
            Defaults to None.
            owid_data_sets (Optional[pd.DataFrame], optional): A DataFrame listing the available
            datasets. Defaults to None.
    """
    def __init__(
        self,
        shape_data: Optional[gpd.geodataframe.GeoDataFrame] = None,
        owid_data_sets: Optional[pd.DataFrame] = None,
    ):
        if not shape_data:
            self.shape_data = self.get_shape_data()
        else:
            self.shape_data = shape_data

        if not owid_data_sets:
            self.owid_data_sets = self.get_owid_data_sets()
        else:
            self.owid_data_sets = owid_data_sets

    @staticmethod
    def get_shape_data() -> gpd.geodataframe.GeoDataFrame:
        """Loads the shape data of the map"""
        shape_data = gpd.read_file(SHAPEFILE)[["ADMIN", "ADM0_A3", "geometry"]]
        shape_data.columns = ["country", "country_code", "geometry"]
        shape_data = shape_data.drop(shape_data.index[159])
        return shape_data

    @staticmethod
    def to_geo_json_data_source(shape_data: gpd.geodataframe.GeoDataFrame) -> GeoJSONDataSource:
        """Convert the shape_data to a GeoJSONDataSource

        Args:
            shape_data (gpd.geodataframe.GeoDataFrame): The shape data

        Returns:
            GeoJSONDataSource: The resulting GeoJson Data
        """
        json_data = json.dumps(json.loads(shape_data.to_json()))
        return GeoJSONDataSource(geojson=json_data)

    @staticmethod
    def get_owid_data_sets() -> pd.DataFrame:
        """The list of Owid data sets

        Returns:
            pd.DataFrame: A DataFrame with columns=["name", "url"]
        """
        return pd.read_csv(OWIDDATASETS_FILE).set_index("name")

    @staticmethod
    def get_owid_data(
        owid_data_sets: pd.DataFrame,
        shape_data: gpd.geodataframe.GeoDataFrame,
        name: str,
        year: Optional[int] = None,
        key: Optional[str] = None,
    ) -> gpd.geodataframe.GeoDataFrame:
        """An Owid Data Set combined with the shape_data

        Args:
            owid_data_sets (pd.DataFrame): The list of Owid Data Sets
            shape_data (gpd.geodataframe.GeoDataFrame): The shape data for the map
            name (str): The name of the Owid Data Set to look up.
            year (Optional[int], optional): A year to filter to. Defaults to None.
            key (Optional[str], optional): The name of column containing the values.
            Defaults to None.

        Returns:
            gpd.geodataframe.GeoDataFrame: The Owid Data Sets merged with the shape data
        """
        url = owid_data_sets.loc[name].url
        owid_data = pd.read_csv(url)
        if year is not None:
            owid_data = owid_data[owid_data["Year"] == year]
        merged = shape_data.merge(owid_data, left_on="country", right_on="Entity", how="left")

        if key is None:
            key = owid_data.columns[2]
        merged[key] = merged[key].fillna(0)
        return merged, key

    @classmethod
    def get_map_plot(
        cls,
        shape_data: gpd.geodataframe.GeoDataFrame,
        value_column: Optional[str] = None,
        title: str = "",
    ):
        """Plot GeoDataFrame as a map


        """
        geosource = cls.to_geo_json_data_source(shape_data)
        palette = brewer["OrRd"][8]
        palette = palette[::-1]
        vals = shape_data[value_column]
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
        plot = figure(
            title=title, plot_height=400, plot_width=850, toolbar_location="right", tools=tools
        )
        plot.xgrid.grid_line_color = None
        plot.ygrid.grid_line_color = None
        plot.patches(
            "xs",
            "ys",
            source=geosource,
            fill_alpha=1,
            line_width=0.5,
            line_color="black",
            fill_color={"field": value_column, "transform": color_mapper},
        )
        plot.add_layout(color_bar, "below")
        return plot

    def view(self):
        """Map dashboard"""

        map_pane = pn.pane.Bokeh(width=400)
        dataset_selected = pnw.Select(name="dataset", options=list(self.owid_data_sets.index))
        year_selected = pnw.IntSlider(start=1950, end=2018, value=2010)

        def update_map(event): # pylint: disable=unused-argument
            shape_data, key = self.get_owid_data(
                self.owid_data_sets,
                self.shape_data,
                name=dataset_selected.value,
                year=year_selected.value,
            )
            map_pane.object = self.get_map_plot(shape_data, key)

        year_selected.param.watch(update_map, "value")
        year_selected.param.trigger("value")
        dataset_selected.param.watch(update_map, "value")
        app = pn.Column(
            pn.pane.Markdown(__doc__), pn.Row(dataset_selected, year_selected), map_pane
        )
        return app


def view():
    """A View of the OwidDashboard. Is here so that the OwidDashboard can be included in the
    Gallery"""
    return OwidDashboard().view()


if __name__.startswith("bk"):
    view().servable()
