"""Demo of the PDBeMolstar component from panel-chemistry"""
import panel as pn
import param
from panel_chemistry.pane import PDBeMolStar

from awesome_panel import config

config.extension(url="pdbe_molstar")

local_pdbe = PDBeMolStar(
    name="Local File",
    sizing_mode="stretch_width",
    height=500,
    custom_data={
        "url": "https://raw.githubusercontent.com/MarcSkovMadsen/panel-chemistry/main/examples/assets/1qyn.pdb",  # pylint: disable=line-too-long
        "format": "pdb",
    },
).servable()

parameters = ["hide_water", "hide_polymer", "visual_style", "lighting", "spin"]


class Controller(param.Parameterized):
    """Controller for a PDBeMolstar component"""

    chain = param.Selector(default="A", objects=["A", "B", "C", "D"])
    apply_colors = param.Action()
    reset_colors = param.Action()
    residues = param.Tuple((20, 50))
    highlight = param.Action()
    clear_highlight = param.Action()
    reset = param.Action()

    def __init__(self, pdbe, **params):
        self.pdbe = pdbe

        super().__init__(**params)

        self.apply_colors = self._action_color
        self.reset_colors = self._action_reset_color
        self.highlight = self._action_highlight
        self.clear_highlight = lambda self: self.pdbe.clear_highlight()
        self.reset = self._action_reset

    def _action_color(self, _):
        """Color one chain yellow, color everything else blue"""

        data = {"struct_asym_id": self.chain, "color": {"r": 255, "g": 215, "b": 0}}

        self.pdbe.color([data], non_selected_color={"r": 0, "g": 87, "b": 183})

    def _action_reset_color(self, _):
        self.pdbe.clear_selection()

    def _action_highlight(self, _):
        data = {
            "start_residue_number": self.residues[0],
            "end_residue_number": self.residues[1],
            "struct_asym_id": self.chain,
            "color": {"r": 255, "g": 105, "b": 180},
        }

        self.pdbe.highlight([data])

    def _action_reset(self, _):
        data = {
            "camera": True,
            "theme": True,  # reset theme doesnt work
            "highlightcolor": True,
            "selectColor": True,
        }
        self.pdbe.reset(data)


ctrl = Controller(local_pdbe)
slider = pn.widgets.IntRangeSlider(name="Residues", start=15, end=150, value=(20, 50), step=1)

pn.Param(ctrl, name="Controls", widgets={"residues": slider}).servable(area="sidebar")
pn.Param(local_pdbe, parameters=parameters, name="Controls").servable(area="sidebar")
