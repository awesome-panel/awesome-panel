import py3Dmol
import panel as pn

from panel_chemistry.pane import Py3DMol
from awesome_panel import config

config.extension(url="py3dmol")

THEME = config.get_theme()

def _create_app(theme=THEME):
    if theme=="dark":
        background_color = "#181818"
    else:
        background_color = "#eeeeee"
    
    # Basic Example
    basic_view = py3Dmol.view(query="mmtf:1ycr")
    basic_view.setStyle({"cartoon": {"color": "spectrum"}})
    basic_view.setBackgroundColor(background_color)
    basic_viewer = Py3DMol(basic_view, height=400, sizing_mode="stretch_width", name="Basic")
    pn.Column(
        "## Basic Example", basic_viewer
    ).servable()

    # Grid Example
    grid_view = py3Dmol.view(
        query="pdb:1dc9",
        viewergrid=(2, 2),
        style=[
            [
                {"stick": {}},
                {"cartoon": {"arrows": True, "tubes": True, "style": "oval", "color": "white"}},
            ],
            [{"stick": {"colorscheme": "greenCarbon"}}, {"cartoon": {"color": "spectrum"}}],
        ],
    )
    grid_view.setBackgroundColor(background_color)
    grid_viewer=Py3DMol(grid_view, height=400, sizing_mode="stretch_width", name="Grid")
    pn.Column(
        "## Grid Example", grid_viewer
    ).servable()

    # Interactive Example
    xyz = '''4
    * (null), Energy   -1000.0000000
    N     0.000005    0.019779   -0.000003   -0.157114    0.000052   -0.012746
    H     0.931955   -0.364989    0.000003    1.507100   -0.601158   -0.004108
    H    -0.465975   -0.364992    0.807088    0.283368    0.257996   -0.583024
    H    -0.465979   -0.364991   -0.807088    0.392764    0.342436    0.764260
    '''

    interactive_view = py3Dmol.view()
    interactive_view.addModel(xyz,'xyz',{'vibrate': {'frames':10,'amplitude':1}})
    interactive_view.setStyle({'stick':{}})
    interactive_view.setBackgroundColor(background_color)
    interactive_view.animate({'loop': 'backAndForth'})
    interactive_view.zoomTo()
    interactive_viewer = Py3DMol(interactive_view, height=400, sizing_mode="stretch_width", name="Interactive")
    pn.Column(
        "## Interactive Example", interactive_viewer
    ).servable()

    examples = [(basic_view, basic_viewer), (grid_view, grid_viewer), (interactive_view, interactive_viewer)]
    
    def set_background(color='0xeeeeee'):
        for view, viewer in examples:
            view.setBackgroundColor(color)
            viewer.param.trigger("object")

    background = pn.widgets.ColorPicker(value=background_color, name="Background").servable(area="sidebar")
    pn.bind(set_background, color=background, watch=True)

    def set_style(style="stick"):
        for view, viewer in examples:
            view.setStyle({style: {}})
            view.zoomTo()
            viewer.param.trigger("object")
    
    pn.widgets.StaticText(value="Style").servable(area="sidebar")
    style=pn.widgets.RadioButtonGroup(value="sphere", options=["line", "cross", "stick", "sphere"], name="Style", button_type="success").servable(area="sidebar")
    set_style=pn.bind(set_style, style=style, watch=True)

if __name__.startswith("bokeh"):
    _create_app()