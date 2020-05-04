import holoviews as hv
import param
from bokeh.themes.theme import Theme as BokehTheme
from holoviews import Cycle

from awesome_panel.application import assets
hv.extension('bokeh')

_COLOR_CYCLE = tuple(Cycle.default_cycles["Category20"])

class Theme(param.Parameterized):
    spinner_static_url = param.String(assets.SPINNER_PANEL_STATIC_LIGHT_400_340)
    spinner_url = param.String(assets.SPINNER_PANEL_BREATH_LIGHT_400_340)
    css = param.String()
    color_cycle = param.Tuple(_COLOR_CYCLE)
    bokeh_disable_logo = param.Boolean(True)
    bokeh_theme_json = param.Dict()

    @property
    def holoviews_color_cycle(self) -> Cycle:
        if self.color_cycle:
            color_cycle = self.color_cycle
        else:
            color_cycle = _COLOR_CYCLE
        return Cycle(list(color_cycle))

    @property
    def bokeh_theme(self) -> BokehTheme:
        if self.bokeh_theme_json:
            return BokehTheme(json=self.bokeh_theme_json)
        else:
            return BokehTheme(json={})
