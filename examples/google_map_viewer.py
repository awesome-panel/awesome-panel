"""In [Discourse 1533]\
(https://discourse.holoviz.org/t/example-of-using-template-with-param-classes/1533) Andrew
showcased this example of using the ReactTemplate with Google Maps. Here it is
reproduced using the `FastGridTemplate`.

The Google Maps example was initially described in the [Param User Guide]\
(https://panel.holoviz.org/user_guide/Param.html).
"""
import panel as pn
import param

from awesome_panel import config


class GoogleMapViewer(param.Parameterized):
    """An app showcasing how Param and Google Maps can be composed into an app
    using the FastGridTemplate"""

    continent = param.ObjectSelector(default="Asia", objects=["Africa", "Asia", "Europe"])

    country = param.ObjectSelector(default="China", objects=["China", "Thailand", "Japan"])

    settings_panel = param.Parameter()
    map_panel = param.Parameter()

    _countries = {
        "Africa": ["Ghana", "Togo", "South Africa", "Tanzania"],
        "Asia": ["China", "Thailand", "Japan"],
        "Europe": ["Austria", "Bulgaria", "Greece", "Portugal", "Switzerland"],
    }

    def __init__(self, **params):
        super().__init__(**params)
        self.settings_panel = pn.Param(self, parameters=["continent", "country"])
        self.map_panel = pn.pane.HTML(sizing_mode="stretch_both", height=616, margin=0)
        self._update_map()

    @param.depends("continent", watch=True)
    def _update_countries(self):
        countries = self._countries[self.continent]
        self.param["country"].objects = countries
        self.country = countries[0]

    @param.depends("country", watch=True)
    def _update_map(self):
        iframe = f"""
        <iframe width="100%" height="100%" src="https://maps.google.com/maps?q={self.country}&z=6&output=embed"
        frameborder="0" scrolling="no" marginheight="0" marginwidth="0"></iframe>
        """
        self.map_panel.object = iframe


config.extension(url="google_map_viewer")
viewer = GoogleMapViewer(name="Google Map Viewer")
viewer.settings_panel.servable(area="sidebar")
viewer.map_panel.servable()
