"""Implementation of the PerspectiveViewer Web Component"""
from enum import Enum
from typing import List

import panel as pn
import param
from bokeh.models import ColumnDataSource

from awesome_panel.express.pane.web_component import WebComponent

# pylint: disable=line-too-long
JS_FILES = {
    "perspective": "https://unpkg.com/@finos/perspective@0.4.7",
    "perspective_viewer": "https://unpkg.com/@finos/perspective-viewer@0.4.7",
    "perspective_viewer_datagrid": "https://unpkg.com/@finos/perspective-viewer-datagrid@0.4.7/dist/umd/perspective-viewer-datagrid.js",
    "perspective_viewer_d3fc": "https://unpkg.com/@finos/perspective-viewer-d3fc@0.4.7",
    "perspective_viewer_hypergrid": "https://unpkg.com/@finos/perspective-viewer-hypergrid@0.4.7",
    # "perspective-jupyterlab": "https://unpkg.com/@finos/perspective-jupyterlab@0.4.7",
}

JS_FILES = {
    "perspective": "https://unpkg.com/@finos/perspective@0.4.7/dist/umd/perspective.js",
    "perspective_viewer": "https://unpkg.com/@finos/perspective-viewer@0.4.7/dist/umd/perspective-viewer.js",
    "perspective_viewer_datagrid": "https://unpkg.com/@finos/perspective-viewer-datagrid@0.4.7/dist/umd/perspective-viewer-datagrid.js",
    "perspective_viewer_hypergrid": "https://unpkg.com/@finos/perspective-viewer-hypergrid@0.4.7/dist/umd/perspective-viewer-hypergrid.js",
    "perspective_viewer_d3fc": "https://unpkg.com/@finos/perspective-viewer-d3fc@0.4.7/dist/umd/perspective-viewer-d3fc.js",
}

CSS_FILES = {
    "all": "https://unpkg.com/@finos/perspective-viewer@0.4.7/dist/umd/all-themes.css",
    "material": "https://unpkg.com/@finos/perspective-viewer@0.4.7/dist/umd/material.css",
    "material_dark": "https://unpkg.com/@finos/perspective-viewer@0.4.7/dist/umd/material.dark.css",
    "material_dense": "https://unpkg.com/@finos/perspective-viewer@0.4.7/dist/umd/material-dense.css",
    "material_dense_dark": "https://unpkg.com/@finos/perspective-viewer@0.4.7/dist/umd/material-dense.dark.css",
    "vaporwave": "https://unpkg.com/@finos/perspective-viewer@0.4.7/dist/umd/vaporwave.css",
}
# pylint: enable=line-too-long

THEMES = {
    "material": "perspective-viewer-material",
    "material-dark": "perspective-viewer-material-dark",
    "material-dense": "perspective-viewer-material-dense",
    "material-dense-dark": "perspective-viewer-material-dense-dark",
    "vaporwave": "perspective-viewer-vaporwave",
}
# Hack: When the user drags some of the columns, then the class attribute contains "dragging" also.
THEMES_DRAGGING = {key + " dragging": value + " dragging" for key, value in THEMES.items()}
THEMES = {**THEMES, **THEMES_DRAGGING}


# Source: https://github.com/finos/perspective/blob/e23988b4b933da6b90fd5767d059a33e70a2493e/python/perspective/perspective/core/plugin.py#L49 # pylint: disable=line-too-long
class Plugin(Enum):
    """The plugins (grids/charts) available in Perspective.  Pass these into
    the `plugin` arg in `PerspectiveWidget` or `PerspectiveViewer`.
    Examples:
        >>> widget = PerspectiveWidget(data, plugin=Plugin.TREEMAP)
    """

    HYPERGRID = "hypergrid"  # hypergrid
    GRID = "datagrid"  # hypergrid

    # YBAR = 'y_bar'  # highcharts
    # XBAR = 'x_bar'  # highcharts
    # YLINE = 'y_line'  # highcharts
    # YAREA = 'y_area'  # highcharts
    # YSCATTER = 'y_scatter'  # highcharts
    # XYLINE = 'xy_line'  # highcharts
    # XYSCATTER = 'xy_scatter'  # highcharts
    # TREEMAP = 'treemap'  # highcharts
    # SUNBURST = 'sunburst'  # highcharts
    # HEATMAP = 'heatmap'  # highcharts

    YBAR_D3 = "d3_y_bar"  # d3fc
    XBAR_D3 = "d3_x_bar"  # d3fc
    YLINE_D3 = "d3_y_line"  # d3fc
    YAREA_D3 = "d3_y_area"  # d3fc
    YSCATTER_D3 = "d3_y_scatter"  # d3fc
    XYSCATTER_D3 = "d3_xy_scatter"  # d3fc
    TREEMAP_D3 = "d3_treemap"  # d3fc
    SUNBURST_D3 = "d3_sunburst"  # d3fc
    HEATMAP_D3 = "d3_heatmap"  # d3fc

    CANDLESTICK = "d3_candlestick"  # d3fc
    CANDLESTICK_D3 = "d3_candlestick"  # d3fc
    OHLC = "d3_ohlc"  # d3fc
    OHLC_D3 = "d3_ohlc"  # d3fc

    @staticmethod
    def options() -> List:
        """Returns the list of options of the PerspectiveViewer, like Hypergrid, Grid etc.

        Returns:
            List: [description]
        """
        return list(c.value for c in Plugin)


class PerspectiveViewer(WebComponent):  # pylint: disable=abstract-method
    """The PerspectiveViewer WebComponent enables exploring large tables of data"""

    html = param.String(
        """
    <perspective-viewer class='perspective-viewer-material-dark' \
style="height:100%;width:100%"></perspective-viewer>
    """
    )
    attributes_to_watch = param.Dict(
        {
            "class": "theme",
            "plugin": "plugin",
            "rows": "rows",
            "row-pivots": "row_pivots",
            "columns": "columns",
            "column-pivots": "column_pivots",
            "sort": "sort",
            "aggregates": "aggregates",  # Have not been able to manually test this one
            "filters": "filters",
        }
    )

    theme = param.ObjectSelector("perspective-viewer-material-dark", objects=THEMES)
    plugin = param.ObjectSelector(Plugin.GRID.value, objects=Plugin.options())
    rows = param.List(None)
    row_pivots = param.List(None)
    column_pivots = param.List(None)
    columns = param.List(None)
    aggregates = param.List(None)
    sort = param.List(None)
    filters = param.List(None)

    data = param.DataFrame(doc="""The data will be reloaded in full when ever it changes.""")

    def __init__(self, **params):
        self.param.column_data_source_orient.default = "records"
        self.param.column_data_source_load_function.default = "load"

        super().__init__(**params)
        self._set_column_data_source()

    @param.depends("data", watch=True)
    def _set_column_data_source(self):
        if not self.data is None:
            self.column_data_source = ColumnDataSource(ColumnDataSource.from_df(self.data))
        else:
            self.column_data_source = ColumnDataSource()

    @staticmethod
    def get_imports() -> str:
        """Returns an HTML string with the required import to use the PerspectiveViewer

        Returns:
            str: [description]
        """
        extension = ""
        for js_ in JS_FILES.values():
            extension += f'<script src="{js_}"></script>'
        for css in CSS_FILES.values():
            extension += f'<link rel="stylesheet" href="{css}" is="custom-style">'

        return extension

    @classmethod
    def get_imports_pane(cls) -> pn.pane.HTML:
        """Returns an HTML pane with the JS and CSS imports required by the perspective-viewer

        Returns:
            pn.pane.HTML: [description]
        """
        imports = cls.get_imports()
        return pn.pane.HTML(imports, width=0, height=0, margin=0, sizing_mode="stretch_width")

    @staticmethod
    def config():
        """Add .js and .css files to configuration"""
        for key, value in JS_FILES.items():
            pn.config.js_files[key] = value
        pn.config.css_files.append(CSS_FILES["all"])
