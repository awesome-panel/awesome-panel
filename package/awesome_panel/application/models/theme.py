"""In this module we implement the Theme Model

Use the Theme model to

- Provide theming to your Template and Application
- implements a custom subclass Theme
"""

import holoviews as hv
import param
from awesome_panel.application import assets
from bokeh.themes.theme import Theme as BokehTheme
from holoviews import Cycle

hv.extension("bokeh")

_COLOR_CYCLE = tuple(Cycle.default_cycles["Category20"])


class Theme(param.Parameterized):
    """The Theme model provides parameters and functionality like links to spinner images and css.

    - Provide theming to your Template and Application
    - implement a custom subclass Theme"""

    spinner_static_url = param.String(assets.SPINNER_PANEL_STATIC_LIGHT_400_340)
    spinner_url = param.String(assets.SPINNER_PANEL_BREATH_LIGHT_400_340)
    css = param.String()
    color_cycle = param.Tuple(_COLOR_CYCLE)
    bokeh_disable_logo = param.Boolean(True)
    bokeh_theme_json = param.Dict()

    @property
    def holoviews_color_cycle(self) -> Cycle:
        """Returns the HoloViews color Cycle to be used when plotting with the Theme as the active
        Theme.

        Returns:
            Cycle: A HoloViews color Cyle.
        """
        if self.color_cycle:
            color_cycle = self.color_cycle
        else:
            color_cycle = _COLOR_CYCLE
        return Cycle(list(color_cycle))

    @property
    def bokeh_theme(self) -> BokehTheme:
        """Returns the Bokeh Theme to be used when plotting with the Theme as the active Theme.

        Returns:
            BokehTheme: A Bokeh Theme
        """
        if self.bokeh_theme_json:
            return BokehTheme(json=self.bokeh_theme_json)
        return BokehTheme(json={})
