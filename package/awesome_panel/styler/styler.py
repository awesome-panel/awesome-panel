import copy

import holoviews as hv
import hvplot.pandas
import panel as pn
import param
from bokeh import themes
from bokeh.themes import Theme
import pandas as pd
import holoviews as hv

MATERIAL_LIGHT = "material-light"
MATERIAL_DARK = "material-dark"

WHITE = "#ffffff"
DARK_100 = "#303030"
DARK_75 = "#393939"
DARK_50 = "#424242"
DARK_25 = "#4d4d4d"
TEXT_DIGITAL_DARK = "#ececec"

MATERIAL_DARK_JSON = {
    "attrs": {
        "Figure": {
            "background_fill_color": DARK_50,
            "border_fill_color": DARK_100,
            "outline_line_color": DARK_75,
            "outline_line_alpha": 0.25,
        },
        "Grid": {"grid_line_color": TEXT_DIGITAL_DARK, "grid_line_alpha": 0.25},
        "Axis": {
            "major_tick_line_alpha": 0,
            "major_tick_line_color": TEXT_DIGITAL_DARK,
            "minor_tick_line_alpha": 0,
            "minor_tick_line_color": TEXT_DIGITAL_DARK,
            "axis_line_alpha": 0,
            "axis_line_color": TEXT_DIGITAL_DARK,
            "major_label_text_color": TEXT_DIGITAL_DARK,
            "major_label_text_font": "roboto, sans-serif, Verdana",
            "major_label_text_font_size": "1.025em",
            "axis_label_standoff": 10,
            "axis_label_text_color": TEXT_DIGITAL_DARK,
            "axis_label_text_font": "roboto, sans-serif, Verdana",
            "axis_label_text_font_size": "1.25em",
            "axis_label_text_font_style": "normal",
        },
        "Legend": {
            "spacing": 8,
            "glyph_width": 15,
            "label_standoff": 8,
            "label_text_color": TEXT_DIGITAL_DARK,
            "label_text_font": "roboto, sans-serif, Verdana",
            "label_text_font_size": "1.025em",
            "border_line_alpha": 0,
            "background_fill_alpha": 0.25,
            "background_fill_color": DARK_75,
        },
        "ColorBar": {
            "title_text_color": TEXT_DIGITAL_DARK,
            "title_text_font": "roboto, sans-serif, Verdana",
            "title_text_font_size": "1.025em",
            "title_text_font_style": "normal",
            "major_label_text_color": TEXT_DIGITAL_DARK,
            "major_label_text_font": "roboto, sans-serif, Verdana",
            "major_label_text_font_size": "1.025em",
            "background_fill_color": DARK_75,
            "major_tick_line_alpha": 0,
            "bar_line_alpha": 0,
        },
        "Title": {
            "text_color": TEXT_DIGITAL_DARK,
            "text_font": "roboto, sans-serif, Verdana",
            "text_font_size": "1.15em",
        },
    }
}

CSS_STYLES = {
    "None": "",
    "caliber": """
.app-container {
    border-radius: 5px;
    box-shadow: 2px 2px 2px lightgrey;
}
.app-bar {
    color:white;
    box-shadow: 5px 5px 20px #9E9E9E;
    z-index: 50;
}
    """,
    "material-light": """
.app-container {
    border-radius: 5px;
    box-shadow: 2px 2px 2px lightgrey;
}
.app-bar {
    color:white
    font-family:roboto;
    box-shadow: 5px 5px 20px #9E9E9E;
    z-index: 50;
}
    """,
    "material-dark": """
.app-container {
    border-radius: 5px;
    box-shadow: 2px 2px 2px lightgrey;
}
.app-bar {
    color:white;
    font-family:roboto;
}
    """,
}

MATERIAL_LIGHT_JSON = {
    "attrs": {
        "Axis": {
            "major_label_text_font": "roboto, sans-serif, Verdana",
            "major_label_text_font_size": "1.025em",
            "axis_label_standoff": 10,
            "axis_label_text_font": "roboto, sans-serif, Verdana",
            "axis_label_text_font_size": "1.25em",
            "axis_label_text_font_style": "normal",
        },
        "Legend": {
            "spacing": 8,
            "glyph_width": 15,
            "label_standoff": 8,
            "label_text_font": "roboto, sans-serif, Verdana",
            "label_text_font_size": "1.025em",
        },
        "ColorBar": {
            "title_text_font": "roboto, sans-serif, Verdana",
            "title_text_font_size": "1.025em",
            "title_text_font_style": "normal",
            "major_label_text_font": "roboto, sans-serif, Verdana",
            "major_label_text_font_size": "1.025em",
        },
        "Title": {"text_font": "roboto, sans-serif, Verdana", "text_font_size": "1.15em",},
    }
}

KINDS = ["area", "bar", "barh", "line", "scatter", "step", "table"]
BACKGROUND_COLORS = {"caliber": "#f2f2f2", "material-light": "#f2f2f2", "material-dark": "#f2f2f2"}


class HvPlotOptions(param.Parameterized):
    x = param.String()
    y = param.String()


class AwesomePanelStylerView(pn.Column):
    _designer = param.Parameter()

    def __init__(self, designer, **params):
        self._rename["_designer"] = None
        params["_designer"] = designer
        params["sizing_mode"] = params.get("sizing_mode", "stretch_both")
        self._js_pane = pn.pane.HTML(
            """\
<script type="module" src="https://cdn.jsdelivr.net/gh/marcskovmadsen/awesome-panel@be59521090b7c9d9ba5eb16e936034e412e2c86b/assets/js/mwc.bundled.js"></script>
<link href="https://fonts.googleapis.com/css?family=Roboto:300,400,500" rel="stylesheet">
<link href="https://fonts.googleapis.com/css?family=Material+Icons&display=block" rel="stylesheet">
<link rel="stylesheet" type="text/css" href="https://use.fontawesome.com/releases/v5.11.2/css/all.css"/>""",
            width=0,
            height=0,
            margin=0,
            sizing_mode="fixed",
        )
        self._css_pane = pn.pane.HTML(
            "<style>" + designer.css + "</style>", width=0, height=0, margin=0, sizing_mode="fixed"
        )

        self._progress_widget = pn.widgets.Progress()
        # self._curve_pane = pn.Param()
        self._options_pane = pn.Pane(designer.options)
        self._bar_pane = pn.Row(
            pn.pane.Markdown(
                "## Awesome Panel - Styler", sizing_mode="stretch_width", margin=(10, 5, 10, 25)
            ),
            background="green",
            sizing_mode="stretch_width",
            css_classes=["app-bar"],
        )
        self._data_pane = pn.pane.DataFrame(
            designer.data, sizing_mode="stretch_both", margin=10
        )
        self._data_container = pn.Column(
            pn.Row(pn.pane.Markdown("#### DataFrame"), sizing_mode="stretch_width", align="center"),
            self._data_pane,
            sizing_mode="stretch_both",
            css_classes=["app-container"],
            margin=25,
            background="white",
        )
        self._bokeh_settings_pane = pn.Column(
            designer.param.custom_theme, "Logo", name="Bokeh", sizing_mode="stretch_width",
        )
        self._app_container_settings_pane = pn.Column(
            "Round", "Shadow", "Background", "Color", name="Container", sizing_mode="stretch_width",
        )
        self._app_settings_settings_pane = pn.Column(
            "Background", "Color", "Divider", name="Settings", sizing_mode="stretch_width",
        )
        self._app_info_settings_pane = pn.Column(
            name="Info", sizing_mode="stretch_width",
        )
        self._app_bar_settings_pane = pn.Column(
            "Background", "Color", "Shadow", name="Bar", sizing_mode="stretch_width",
        )
        self._app_settings_pane = pn.Column(
            designer.param.background_color,
            pn.Tabs(
                self._app_bar_settings_pane,
                self._app_container_settings_pane,
                self._app_info_settings_pane,
                self._app_settings_settings_pane,
                sizing_mode="stretch_width",
            ),
            name="App",
            sizing_mode="stretch_width",
        )
        self._hvplot_settings_pane = pn.Column(
            designer.param.kind,
            # self._curve_pane,
            self._options_pane,
            "Logo",
            "Toolbar",
            "Tools",
            # designer.param.update_plot,
            name="HvPlot",
            sizing_mode="stretch_width",
        )
        self._dataframe_settings_pane = pn.Column(name="DataFrame", sizing_mode="stretch_width",)
        self._panel_settings_pane = pn.Column(
            self._dataframe_settings_pane, name="Panel", sizing_mode="stretch_width",
        )
        self._material_settings_pane = pn.Column(name="Material", sizing_mode="stretch_width",)
        self.setting_tab_pane = pn.Tabs(
            self._app_settings_pane,
            self._bokeh_settings_pane,
            self._hvplot_settings_pane,
            self._material_settings_pane,
            self._panel_settings_pane,
            sizing_mode="stretch_width",
            margin=(15, 5, 10, 5),
        )
        self.setting_tab_pane.active = 2 # HvPlot
        self._settings_pane = pn.Column(
            pn.pane.Markdown("### Theme"),
            pn.Param(designer, parameters=["theme"], show_name=False, show_labels=False, sizing_mode="stretch_width"),
            pn.pane.Markdown("### Style"),
            self.setting_tab_pane,
            width=400,
            sizing_mode="stretch_height",
            css_classes=["app-settings-container"],
            margin=(25, 5, 10, 5),
        )
        self._plot_pane = pn.pane.HoloViews(
            hv.Curve({}), sizing_mode="stretch_both", css_classes=["hvplot"], margin=10
        )
        self._plot_container = pn.Column(
            pn.Row(pn.pane.Markdown("#### HvPlot"), sizing_mode="stretch_width", align="center"),
            self._plot_pane,
            margin=25,
            sizing_mode="stretch_both",
            css_classes=["app-container"],
            background="white",
        )
        info = []
        for i in range(0, 4):
            info_container = pn.Column(
                pn.pane.Markdown(
                    """\
#### 62.000

Downloads per Month
""",
                    sizing_mode="stretch_width",
                    margin=15,
                ),
                sizing_mode="stretch_both",
                css_classes=["app-container"],
                margin=25,
                background="white",
            )
            info.append(info_container)

        self._info_row = pn.Row(*info, sizing_mode="stretch_width")
        self._widgets_tab = pn.Tabs("Button", "Checkboxgroup", sizing_mode="stretch_width",)
        self._material_widgets_tab = pn.Tabs(
            "Button", "Checkboxgroup", sizing_mode="stretch_width",
        )
        self._widgets_container = pn.Column(
            pn.Row(pn.pane.Markdown("### Widgets", sizing_mode="stretch_width", align="center"), align="center", sizing_mode="stretch_width"),
            self._widgets_tab,
            css_classes=["app-container"],
            margin=25,
            background="white",
            sizing_mode="stretch_width",
        )
        self._material_widgets_container = pn.Column(
            pn.Row(pn.pane.Markdown("### Material", sizing_mode="stretch_width", align="center"), align="center", sizing_mode="stretch_width"),
            self._material_widgets_tab,
            css_classes=["app-container"],
            margin=25,
            background="white",
            sizing_mode="stretch_width",
        )
        self._widgets_row = pn.Row(
            self._widgets_container, self._material_widgets_container, sizing_mode="stretch_width"
        )
        self._main_pane = pn.Row(
            self._settings_pane,
            pn.Column(
                self._info_row,
                pn.Row(self._plot_container, self._data_container, sizing_mode="stretch_width"),
                self._widgets_row,
                sizing_mode="stretch_both",
            ),
            sizing_mode="stretch_both",
        )

        super().__init__(
            self._js_pane,
            self._css_pane,
            self._bar_pane,
            pn.layout.HSpacer(height=10),
            self._main_pane,
            background=designer.background_color,
            **params
        )

    @param.depends("_designer.background_color", watch=True)
    def _update_background_color(self):
        self.background = self._designer.background_color

    @param.depends("_designer.active", watch=True)
    def _update_progress(self):
        print("view: update progress")
        self._progress_widget.active = self._designer.active

    @param.depends("_designer.plot", watch=True)
    def _update_plot(self):
        print("view: update plot")
        self._plot_pane.object = self._designer.plot

    @param.depends("_designer.css", watch=True)
    def _update_css(self):
        self._css_pane.object = "<style>" + self._designer.css + "</style>"


class AwesomePanelStyler(param.Parameterized):
    data = param.DataFrame()
    theme = param.ObjectSelector()
    custom_theme = param.Dict()
    active = param.Boolean()
    plot = plot = param.ClassSelector(class_=(hv.Element, hv.Layout, hv.Overlay, hv.NdOverlay))
    kind = param.ObjectSelector(default="bar", objects=KINDS)
    options = param.ClassSelector(class_=HvPlotOptions)
    css = param.String()
    background_color = param.Color(default=WHITE)

    update_plot = param.Action(label="UPDATE")

    view = param.ClassSelector(class_=pn.layout.Reactive)

    def __init__(self, **params):
        default_data = pd.DataFrame()
        default_theme = themes.CALIBER
        objects_theme = self.get_bokeh_themes().keys()

        self.param.data.default = default_data
        self.param.theme.objects = objects_theme
        self.param.theme.default = default_theme

        params["options"] = params.get("options", HvPlotOptions())
        params["update_plot"] = self._update_plot

        super().__init__(**params)

        self.view = AwesomePanelStylerView(self)
        self._update_custom_theme()
        self._update_plot()

    @staticmethod
    def get_bokeh_themes():
        return {
            themes.CALIBER: copy.deepcopy(themes._caliber.json),
            themes.DARK_MINIMAL: copy.deepcopy(themes._dark_minimal.json),
            themes.LIGHT_MINIMAL: copy.deepcopy(themes._caliber.json),
            MATERIAL_LIGHT: copy.deepcopy(MATERIAL_LIGHT_JSON),
            MATERIAL_DARK: copy.deepcopy(MATERIAL_DARK_JSON),
        }

    @param.depends("custom_theme", "kind", "options.x", "options.y", watch=True)
    def _update_plot(self, _=None):
        self.active = True

        org_theme = hv.renderer("bokeh").theme
        hv.renderer("bokeh").theme = Theme(json=self.custom_theme)
        if self.options.x and self.options.x in self.data.columns:
            self.data = self.data.sort_values(self.options.x)
        self.css = CSS_STYLES.get(self.theme, "")
        self.background_color = BACKGROUND_COLORS.get(self.theme, WHITE)
        self.plot = self.data.hvplot(
            x=self.options.x,
            y=self.options.y,
            kind=self.kind,
            alpha=0.4,
            # responsive=True,
        )
        hv.renderer("bokeh").theme = org_theme
        self.active = False

    @param.depends("theme", watch=True)
    def _update_custom_theme(self):
        self.custom_theme = self.get_bokeh_themes()[self.theme]
