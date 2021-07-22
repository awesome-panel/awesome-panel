"""The Loading Spinners helps provide a nice user experience by indicating activity.

This app showcases the look and feel of the loading spinners and provides you functionality to
customize the look and feel of your loading spinner.

- You can select the look and color of the loading spinner in the sidebar.
- If you end up with a design you would like to add in your app, then you can just copy the
`style` css and `append` it to `pn.config.raw_css` in your app.
"""
import random
import time

import holoviews as hv
import panel as pn
import param
from awesome_panel_extensions.site import site
from panel.io.loading import start_loading_spinner, stop_loading_spinner

from application.pages.loading_spinners import config

COLOR = "#E1477E"
# pylint: disable=line-too-long
DEFAULT_URL = "https://raw.githubusercontent.com/holoviz/panel/5ea166fdda6e1f958d2d9929ae2ed2b8e962156c/panel/assets/spinner_default.svg"
# pylint: enable=line-too-long
APPLICATION = site.create_application(
    url="loading-spinners",
    name="Loading Spinners",
    author="Marc Skov Madsen",
    description="Demonstrates the look and feel of the Loading Spinners",
    description_long=__doc__,
    thumbnail="loading-spinners.png",
    resources={
        "code": "loading_spinners/loading_spinners.py",
        "gif": "loading-spinners.gif",
        "mp4": "loading-spinners.mp4",
    },
    tags=["UX"],
)


class LoadingStyler(param.Parameterized):
    """A utility that can be used to select and style the loading spinner"""

    spinner = param.ObjectSelector(
        default=DEFAULT_URL, objects=config.SPINNERS, doc="The loading spinner to use"
    )
    spinner_height = param.Integer(50, bounds=(1, 100))
    background_rgb = param.Tuple((255, 255, 255))
    background_alpha = param.Number(0.5, bounds=(0.0, 1.0), step=0.01, doc="The background alpha")
    color = param.Color(config.DEFAULT_COLOR)
    style = param.String("", doc="The CSS Style applied to the loading spinner")

    settings_panel = param.Parameter(doc="A panel containing the settings of the LoadingStyler")
    style_panel = param.Parameter(doc="An 'invisible' HTML pane containing the css style")

    def __init__(self, **params):
        super().__init__(**params)

        self.settings_panel = pn.Param(
            self,
            parameters=[
                "spinner",
                "spinner_height",
                "background_alpha",
                "color",
                "style",
            ],
            widgets={
                "style": {
                    "type": pn.widgets.TextAreaInput,
                    "sizing_mode": "stretch_both",
                    "disabled": True,
                }
            },
        )

        self.style_panel = pn.pane.HTML(sizing_mode="fixed", width=0, height=0, margin=0)
        self._toggle_color()
        self._update_style()

    @property
    def _spinner_url(self):
        spinner = self.spinner
        if callable(spinner):
            return spinner(self.color)  # pylint: disable=not-callable
        return spinner

    @param.depends("spinner", watch=True)
    def _toggle_color(self):
        color_picker: pn.widgets.ColorPicker = [
            widget for widget in self.settings_panel if isinstance(widget, pn.widgets.ColorPicker)
        ][0]
        color_picker.disabled = not callable(self.spinner)

    @param.depends(
        "spinner", "spinner_height", "color", "background_rgb", "background_alpha", watch=True
    )
    def _update_style(self):
        self.style = f"""
.bk.pn-loading.arcs:before {{
background-image: url('{self._spinner_url}');
background-size: auto {self.spinner_height}%;
background-color: rgb({self.background_rgb[0]},{self.background_rgb[1]},{self.background_rgb[2]},{self.background_alpha});
}}"""

    @param.depends("style", watch=True)
    def _update_loading_spinner_css(self):
        self.style_panel.object = f"""<style>{self.style}</style>"""


class LoadingApp(param.Parameterized):  # pylint: disable=too-many-instance-attributes
    """An app which show cases the loading spinner and enables the user to style it."""

    start_loading = param.Action(label="START LOADING", doc="Start the loading spinner")
    stop_loading = param.Action(label="STOP LOADING", doc="Stop the loading spinner")
    sleep = param.Number(
        1,
        bounds=(0.1, 10),
        label="Update time in seconds",
        doc="The time it takes to update the plot",
    )
    show_shared_spinner = param.Boolean(default=False, label="Show one shared loading spinner?")

    loading = param.Boolean(default=False, doc="""Whether or not to show the loading indicator""")
    update_plot = param.Action(label="UPDATE PLOT", doc="Update the plot")

    panels = param.List()

    view = param.Parameter()
    styler = param.ClassSelector(class_=LoadingStyler)

    def __init__(self, **params):
        super().__init__(**params)

        self.start_loading = self._start_loading
        self.stop_loading = self._stop_loading

        self.update_plot = self._update_plot

        hv_plot = self._get_plot()
        self.hv_plot_panel = pn.pane.HoloViews(hv_plot, min_height=300, sizing_mode="stretch_both")
        self.styler = LoadingStyler(name="Styles")

        self.panels = [
            pn.Param(
                self.param.update_plot,
                widgets={"update_plot": {"button_type": "primary"}},
            ),
            self.hv_plot_panel,
        ]

        self.settings_panel = pn.Column(
            pn.pane.Markdown("## Settings"),
            pn.Param(
                self,
                parameters=[
                    "start_loading",
                    "stop_loading",
                    "sleep",
                    "show_shared_spinner",
                ],
                widgets={
                    "style": {
                        "type": pn.widgets.TextAreaInput,
                        "sizing_mode": "stretch_width",
                        "height": 100,
                        "disabled": True,
                    }
                },
                show_name=False,
            ),
            self.styler.settings_panel,
            sizing_mode="stretch_width",
        )
        self.main = pn.Column(*self.panels, self.styler.style_panel, sizing_mode="stretch_both")
        self.view = pn.Row(self.settings_panel, self.main)

    def _start_loading(self, *_):
        self.loading = True

    def _stop_loading(self, *_):
        self.loading = False

    @staticmethod
    def _get_plot():
        xxs = ["one", "two", "tree", "four", "five", "six"]
        data = []
        for item in xxs:
            data.append((item, random.randint(0, 10)))
        return hv.Bars(data, hv.Dimension("Car occupants"), "Count").opts(
            height=500,
            responsive=True,
            color=COLOR,
        )

    def _update_plot(self, *_):
        self.loading = True
        time.sleep(self.sleep)
        self.hv_plot_panel.object = self._get_plot()
        self.loading = False

    @param.depends("loading", "show_shared_spinner", watch=True)
    def _update_loading_spinner(self):
        if self.loading:
            self._start_loading_spinner()
        else:
            self._stop_loading_spinner()

    def _start_loading_spinner(self, *_):
        # Only nescessary in this demo app to be able to toggle show_shared_spinner
        self._stop_loading_spinner()
        if self.show_shared_spinner:
            start_loading_spinner(self.main)
        else:
            for panel in self.panels:
                start_loading_spinner(panel)

    def _stop_loading_spinner(self, *_):
        stop_loading_spinner(self.main)
        for panel in self.panels:
            stop_loading_spinner(panel)


@site.add(APPLICATION)
def view():
    """Returns the app in a Template"""
    pn.config.sizing_mode = "stretch_width"
    template = pn.template.FastListTemplate(title="Loading Spinners")
    app = LoadingApp(name="Loading Spinner App")
    template.sidebar[:] = [app.settings_panel]
    template.main[:] = [APPLICATION.intro_section(), app.main]
    if not issubclass(template.theme, pn.template.base.DefaultTheme):
        app.styler.background_rgb = (0, 0, 0)
    return template


if __name__.startswith("bokeh"):
    view().servable()
