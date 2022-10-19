"""This is a slightly updated version of the soccer analysis dashboard developed by
[Stephen Kilcommins](https://www.linkedin.com/in/stephen-kilcommins/) and published in the article
[Panel - Everything you need to know]\
(https://medium.datadriveninvestor.com/panel-everything-you-need-to-know-9bca61532e12)

You can find the original notebook [here](soccer_analytics_dashboard_original.ipynb)
"""

import numpy as np
import pandas as pd
import panel as pn
import plotly.express as px
import plotly.graph_objects as go
import requests
from PIL import Image, ImageOps

from awesome_panel import config
from awesome_panel.assets.csv import EPL_TOP_STRIKERS_2020_2021_PATH
from awesome_panel.config import cached

config.extension("plotly", url="soccer_analytics_dashboard", template=None, intro_section=False)

CSS = """
body {
  background-image: url("https://wallpapercave.com/wp/wc1740690.jpg");
  background-size: cover;
}

.player_select_row {
    color: white;
    font-size: 15px;
}
"""
CSS_PANE = pn.pane.HTML(
    "<style>" + CSS + "</style", height=0, width=0, sizing_mode="fixed", margin=0
)

# convert columns to integers
COLUMNS_TO_CONVERT_TO_INTS = [
    "stats.shots.shots_total",
    "stats.shots.shots_on_goal",
    "stats.goals.scored",
    "stats.passing.total_crosses",
    "stats.passing.crosses_accuracy",
    "stats.passing.passes",
    "stats.passing.accurate_passes",
    "stats.passing.passes_accuracy",
    "stats.passing.key_passes",
    "stats.dribbles.attempts",
    "stats.dribbles.success",
    "stats.dribbles.dribbled_past",
    "stats.other.aerials_won",
    "stats.other.offsides",
    "stats.other.hit_woodwork",
    "stats.other.minutes_played",
]


@cached
def _get_epl_strikers_df():
    epl_strikers_df = pd.read_csv(EPL_TOP_STRIKERS_2020_2021_PATH)
    epl_strikers_df[COLUMNS_TO_CONVERT_TO_INTS] = epl_strikers_df[
        COLUMNS_TO_CONVERT_TO_INTS
    ].astype("Int64")
    return epl_strikers_df


@cached
def _get_and_display_player_image(player):
    data = _get_epl_strikers_df()
    image_url = data[data["player_name"] == player]["player_image_path"].values[0]
    image = ImageOps.expand(
        Image.open(requests.get(image_url, stream=True, timeout=10).raw), border=2, fill="black"
    )
    image = image.resize((200, 200))
    return image


def _apply_consistent_style(fig):
    fig.update_yaxes(showgrid=False)
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(
        title_font=dict(size=16, color="white"),
        tickfont=dict(family="Courier", color="white", size=14),
    )
    fig.update_xaxes(
        title_font=dict(size=16, color="white"),
        tickfont=dict(family="Courier", color="white", size=14),
    )
    fig.update_layout(
        title_font=dict(size=18, family="Arial"),
        title_x=0.5,
        title_font_color="white",
        margin=dict(l=5, r=5, b=10, t=50, pad=0),
    )

    fig.update_layout({"plot_bgcolor": "rgba(0, 0, 0, 0.5)", "paper_bgcolor": "rgba(0, 0, 0, 0.3)"})

    return fig


@cached
def _plot_horizontal_bar(player):
    data = _get_epl_strikers_df()
    data = data.groupby(["player_name"])["stats.goals.scored"].sum().sort_values(ascending=True)
    data = data.reset_index()

    goals_scored = data["stats.goals.scored"].tolist()
    player_names = data["player_name"].tolist()

    fig = px.bar(
        data,
        x=goals_scored,
        y=player_names,
        orientation="h",
        title="Top Goal Scorers - EPL 2020/2021 - Up to Game Week " + str(data.shape[0]),
        height=400,
        width=1300,  # Panel change
        text=goals_scored,
        labels={"x": "Goals", "y": "Player Name"},
    )
    fig.update_traces(hovertemplate=None, hoverinfo="skip")
    fig.update_layout(xaxis_title="Goals Scored", yaxis_title="Player", plot_bgcolor="#FAFAFA")

    fig.update_traces(textposition="outside", textfont={"color": "white"})
    colours = [
        "blue",
    ] * data.shape[0]
    colours[data[data["player_name"] == player].index[0]] = "crimson"
    fig.update_traces(marker_color=colours)

    fig = _apply_consistent_style(fig)

    fig.update_yaxes(
        title_font=dict(size=16, color="white"),
        tickfont=dict(family="Courier", color="white", size=12),
    )
    fig.update_xaxes(
        title_font=dict(size=16, color="white"),
        tickfont=dict(family="Courier", color="white", size=14),
    )

    # Panel change
    return fig


def _plot_line_plot(player):
    data = _get_epl_strikers_df()
    fixture_strings = data[data["player_name"] == player][
        ["stats.shots.shots_total", "fixture_string"]
    ]["fixture_string"]
    shots_total = data[data["player_name"] == player][
        ["stats.shots.shots_total", "fixture_string"]
    ]["stats.shots.shots_total"]
    shots_on_goal = data[data["player_name"] == player][
        ["stats.shots.shots_on_goal", "fixture_string"]
    ]["stats.shots.shots_on_goal"]
    fig = go.Figure()

    fig.add_trace(go.Scatter(x=fixture_strings, y=shots_total, mode="lines+markers", name="Taken"))

    fig.add_trace(
        go.Scatter(x=fixture_strings, y=shots_on_goal, mode="lines+markers", name="On Target")
    )

    fig.update_layout(
        title=player + " Shots Per Game - 2020/2021",
        height=400,
        width=890,  # Panel change
        xaxis_title="Fixture Date",
        yaxis_title="Shots Taken/On Target",
    )

    fig.update_xaxes(
        tickangle=-60,
        tickmode="array",
        tickvals=fixture_strings,
        ticktext=[y[-11:-1] for y in fixture_strings],
    )

    fig.update_layout(hovermode="x unified")
    fig.update_layout(hoverlabel=dict(bgcolor="white", font_size=12, font_family="Rockwell"))
    fig.update_layout(showlegend=False)

    fig = _apply_consistent_style(fig)

    # Panel change
    return fig


@cached
def _plot_scatter_plot(player):
    data = _get_epl_strikers_df()
    accurate_passes = data[data["player_name"] == player]["stats.passing.accurate_passes"]
    passes = data[data["player_name"] == player]["stats.passing.passes"]

    accurate_passes = np.array(accurate_passes.fillna(0), dtype=float)
    passes = np.array(passes.fillna(0), dtype=float)

    fig = px.scatter(
        data,
        x=accurate_passes,
        y=passes,
        title=player + " Attempted Passes vs. Accurate Passes - 2020/2021",
        height=400,
        width=900,  # Panel change
        labels={"x": "Completed", "y": "Attempted"},
        trendline="ols",
        trendline_color_override="red",
    )
    fig.update_layout(xaxis_title="Accurate Passes", yaxis_title="Attempted Passes")
    fig.update_traces(marker_color="blue")
    fig = _apply_consistent_style(fig)
    fig.update_xaxes(showgrid=True)
    fig.update_yaxes(showgrid=True)

    # Panel change
    return fig


def _create_app():
    player_select_widget = pn.widgets.Select(
        options=list(_get_epl_strikers_df()["player_name"].unique()),
        value="Bruno Fernandes",
        min_width=1600,
        max_width=1800,
    )

    # assign css class to achieve better design granularity
    player_select_row = pn.Row(
        pn.pane.Str("Choose A Player for Analysis:", sizing_mode="fixed"),
        player_select_widget,
        align="center",
        css_classes=["player_select_row"],
    )

    # Panel HTML elements can take a 'style' parameter directly.
    # You could alternatively assign a css class as above and include the css code in raw_css
    title_html_pane = pn.pane.HTML(
        """
    <h1>Panel Soccer Analytics Dashboard</h1>
    """,
        style={"color": "white", "width": "90%", "text-align": "center"},
    )

    # bind the 'player_select_widget' to our functions above
    bound_player_png_image_pane = pn.bind(
        _get_and_display_player_image, player=player_select_widget
    )
    plot_horizontal_bar_pane = pn.bind(_plot_horizontal_bar, player=player_select_widget)
    bound_plotly_line_plot_pane = pn.bind(_plot_line_plot, player=player_select_widget)
    bound_plotly_scatter_plot_pane = pn.bind(_plot_scatter_plot, player=player_select_widget)

    # create a new gridspec with 14 columns and 12 rows
    gspec = pn.GridSpec(
        ncols=14, nrows=12, sizing_mode="stretch_both", css_classes=["gspec_container"]
    )

    # place application elements in the grid, using pn.Spacer() for improved layout spacing and
    # control
    gspec[0, :14] = title_html_pane
    gspec[1, :14] = player_select_row

    gspec[3:6, 1:3] = bound_player_png_image_pane
    gspec[2:7, 3] = pn.Spacer()

    gspec[2:7, 4:14] = plot_horizontal_bar_pane
    gspec[7:10, 1:6] = bound_plotly_line_plot_pane
    gspec[7:10, 8:14] = bound_plotly_scatter_plot_pane
    gspec[11, 0:14] = pn.Row(pn.Spacer(), CSS_PANE)

    return gspec


if __name__.startswith("bokeh"):
    # Can be served with 'panel serve soccer_analytics_dashboard.py'
    _create_app().servable()
