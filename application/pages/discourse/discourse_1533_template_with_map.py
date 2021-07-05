"""In [Discourse 1533]\
(https://discourse.holoviz.org/t/example-of-using-template-with-param-classes/1533) Andrew
showcased this example of using the ReactTemplate with Google Maps. Here it is
reproduced using the `FastGridTemplate`.

The Google Maps example was initially described in the [Param User Guide]\
(https://panel.holoviz.org/user_guide/Param.html).
"""
import panel as pn
import param
from panel.template import FastGridTemplate

from awesome_panel_extensions.site import site

APPLICATION = site.create_application(
    url="google-map-viewer",
    name="Google Map Viewer",
    author="Andrew Huang",
    description="An app showcasing the use of Google Maps and the FastGridTemplate",
    description_long=__doc__,
    thumbnail="https://raw.githubusercontent.com/MarcSkovMadsen/awesome-panel/master/assets/images/thumbnails/google-map-viewer.png",
    resources={
        "code": "https://github.com/MarcSkovMadsen/awesome-panel/tree/master/application/pages/discourse/discourse_1533_template_with_map.py",
        "mp4": "https://raw.githubusercontent.com/MarcSkovMadsen/awesome-panel-assets/master/awesome-panel/applications/google-map-viewer.mp4",
    },
    tags=["Panel", "Param", "Grid", "Google", "Map"],
)


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
        iframe = """
        <iframe width="100%" height="100%" src="https://maps.google.com/maps?q={country}&z=6&output=embed"
        frameborder="0" scrolling="no" marginheight="0" marginwidth="0"></iframe>
        """.format(
            country=self.country
        )
        self.map_panel.object = iframe


@site.add(APPLICATION)
def view():
    """Returns the GoogleMapViewer in the FastGridTemplate"""
    pn.config.sizing_mode = "stretch_width"
    viewer = GoogleMapViewer(name="Google Map Viewer")
    template = FastGridTemplate(title="Google Map Viewer", row_height=100)
    template.sidebar.append(viewer.settings_panel)
    template.main[0:3, :] = APPLICATION.intro_section()
    template.main[3:10, :] = viewer.map_panel
    return template


if __name__.startswith("bokeh"):
    view().servable()
