"""Copy of the Bokeh Movie Explorer App."""
import pathlib
import sqlite3 as sql
from os.path import dirname, join

import numpy as np
import pandas.io.sql as psql
import panel as pn
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, Div, Select, Slider, TextInput
from bokeh.plotting import figure
from bokeh.sampledata.movies_data import movie_path

from src.shared.templates import ListTemplate

ROOT = pathlib.Path(__file__).parent
DESCRIPTION = ROOT / "description.html"
TOOLTIPS = [("Title", "@title"), ("Year", "@year"), ("$", "@revenue")]


def _load_movies():
    if not "movies" in pn.state.cache:
        try:
            conn = sql.connect(movie_path)
            query = open(join(dirname(__file__), "query.sql")).read()
            movies = psql.read_sql(query, conn)
            pn.state.cache["movies"] = movies
        except Exception as ex:
            raise ValueError(
                "Run 'bokeh sampledata' to download the data needed for this application"
            ) from ex


def _get_movies():
    _load_movies()
    return pn.state.cache["movies"]


def _get_movie_app():  # pylint: disable=too-many-locals
    movies = _get_movies()

    movies["color"] = np.where(movies["Oscars"] > 0, "orange", "grey")
    movies["alpha"] = np.where(movies["Oscars"] > 0, 0.9, 0.25)
    movies.fillna(0, inplace=True)  # just replace missing values with zero
    movies["revenue"] = movies.BoxOffice.apply(lambda x: "{:,d}".format(int(x)))

    with open(join(dirname(__file__), "razzies-clean.csv")) as file:
        razzies = file.read().splitlines()
    movies.loc[movies.imdbID.isin(razzies), "color"] = "purple"
    movies.loc[movies.imdbID.isin(razzies), "alpha"] = 0.9

    axis_map = {
        "Tomato Meter": "Meter",
        "Numeric Rating": "numericRating",
        "Number of Reviews": "Reviews",
        "Box Office (dollars)": "BoxOffice",
        "Length (minutes)": "Runtime",
        "Year": "Year",
    }

    desc = Div(text=open(DESCRIPTION).read(), sizing_mode="stretch_width")

    # Create Input controls
    reviews = Slider(title="Minimum number of reviews", value=80, start=10, end=300, step=10)
    min_year = Slider(title="Year released", start=1940, end=2014, value=1970, step=1)
    max_year = Slider(title="End Year released", start=1940, end=2014, value=2014, step=1)
    oscars = Slider(title="Minimum number of Oscar wins", start=0, end=4, value=0, step=1)
    boxoffice = Slider(title="Dollars at Box Office (millions)", start=0, end=800, value=0, step=1)
    genre = Select(
        title="Genre",
        value="All",
        options=open(join(dirname(__file__), "genres.txt")).read().split(),
    )
    director = TextInput(title="Director name contains")
    cast = TextInput(title="Cast names contains")
    x_axis = Select(title="X Axis", options=sorted(axis_map.keys()), value="Tomato Meter")
    y_axis = Select(title="Y Axis", options=sorted(axis_map.keys()), value="Number of Reviews")

    # Create Column Data Source that will be used by the plot
    source = ColumnDataSource(
        data=dict(x=[], y=[], color=[], title=[], year=[], revenue=[], alpha=[])
    )

    plot = figure(
        plot_height=400,
        plot_width=700,
        title="",
        toolbar_location=None,
        tooltips=TOOLTIPS,
        sizing_mode="scale_both",
    )
    plot.circle(
        x="x", y="y", source=source, size=7, color="color", line_color=None, fill_alpha="alpha"
    )

    def select_movies():
        genre_val = genre.value
        director_val = director.value.strip()  # pylint: disable=no-member
        cast_val = cast.value.strip()  # pylint: disable=no-member
        selected = movies[
            (movies.Reviews >= reviews.value)
            & (movies.BoxOffice >= (boxoffice.value * 1e6))
            & (movies.Year >= min_year.value)
            & (movies.Year <= max_year.value)
            & (movies.Oscars >= oscars.value)
        ]
        if genre_val != "All":
            selected = selected[selected.Genre.str.contains(genre_val)]
        if director_val != "":
            selected = selected[selected.Director.str.contains(director_val)]
        if cast_val != "":
            selected = selected[selected.Cast.str.contains(cast_val)]
        return selected

    def update():
        selection_df = select_movies()
        x_name = axis_map[x_axis.value]
        y_name = axis_map[y_axis.value]

        plot.xaxis.axis_label = x_axis.value
        plot.yaxis.axis_label = y_axis.value
        plot.title.text = "%d movies selected" % len(selection_df)
        source.data = dict(
            x=selection_df[x_name],
            y=selection_df[y_name],
            color=selection_df["color"],
            title=selection_df["Title"],
            year=selection_df["Year"],
            revenue=selection_df["revenue"],
            alpha=selection_df["alpha"],
        )

    controls = [
        reviews,
        boxoffice,
        genre,
        min_year,
        max_year,
        oscars,
        director,
        cast,
        x_axis,
        y_axis,
    ]
    for control in controls:
        control.on_change("value", lambda attr, old, new: update())

    inputs = column(*controls, sizing_mode="stretch_width")
    update()  # initial load of the data
    return desc, inputs, plot


def view():
    """Returns the Bokeh Movie Explorer app wrapped in a nice template"""
    template = ListTemplate(
        title="Bokeh Movie Explorer",
    )
    pn.state.curdoc.theme = template.theme.bokeh_theme
    desc, inputs, plot = _get_movie_app()
    template.main[:] = [desc, pn.pane.Bokeh(plot, margin=25)]
    template.sidebar[:] = [pn.pane.Markdown("## Settings"), inputs, pn.Spacer(height=25)]
    return template


if __name__.startswith("bokeh"):
    view().servable()