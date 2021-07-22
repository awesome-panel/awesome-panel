"""
Javier asked in [discourse 1478]\
(https://discourse.holoviz.org/t/use-two-different-widgets-to-update-same-plot/1478)
how to provide multiple ways to the user to select a value and then update a plot.
"""
import holoviews as hv
import numpy as np
import panel as pn

CONTINENTS = ["Asia", "Europe", "America"]
CITIES = {
    "Asia": ["Singapore", "Seoul", "Shanghai"],
    "America": ["Boston", "Toronto", "Quito", "Santiago"],
    "Europe": ["Madrid", "London", "Paris", "Lisbon"],
}


def _transform(_cities):
    continents_lookup = {}
    cities_list = []
    for continent, cities in _cities.items():
        for city in cities:
            continents_lookup[city] = continent
    cities_list = list(continents_lookup.keys())
    return continents_lookup, cities_list


CONTINENTS_LOOKUP, CITIES_LIST = _transform(CITIES)


def view():
    """Returns the app in a nice template for use at awesome-panel.org"""
    pn.config.sizing_mode = "stretch_width"
    from awesome_panel_extensions.site import site

    template = pn.template.FastListTemplate(
        main_max_width="1024px",
    )

    select_continent = pn.widgets.Select(name="Continent", options=CONTINENTS, value=CONTINENTS[0])
    select_city = pn.widgets.Select(
        name="City", options=CITIES[select_continent.value], value=CITIES[select_continent.value][0]
    )
    select_city_auto = pn.widgets.AutocompleteInput(
        name="City", options=CITIES_LIST, value=select_city.value
    )

    @pn.depends(select_continent.param.value, watch=True)
    def _update_cities(continent):
        cities = CITIES[continent]
        select_city.options = cities
        select_city.value = cities[0]

    @pn.depends(select_city_auto.param.value, watch=True)
    def _update_from_auto_complete(city):
        select_continent.value = CONTINENTS_LOOKUP[city]
        select_city.value = city

    @pn.depends(select_city.param.value, watch=True)
    def _update_auto_complete(city):
        select_city_auto.value = city

    plot_panel = pn.pane.HoloViews(sizing_mode="stretch_width")

    accent_base_color = template.theme.style.accent_base_color

    @pn.depends(select_city.param.value, watch=True)
    def _update_plot(*_):
        city = select_city.value
        data = np.random.rand(100)
        plot_panel.object = hv.Curve(data).opts(
            title=city, color=accent_base_color, responsive=True, height=400
        )

    _update_plot()
    main = [
        pn.Column(
            pn.Tabs(
                pn.Row(select_continent, select_city, name="By Continent", margin=(25, 5, 10, 5)),
                pn.Row(select_city_auto, name="By City and Autocomplete", margin=(10, 5, 25, 5)),
            ),
            plot_panel,
        ),
    ]
    template.main[:] = main
    return template


if __name__.startswith("bokeh"):
    view().servable()
