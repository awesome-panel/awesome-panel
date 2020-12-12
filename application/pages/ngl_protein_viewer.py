"""
This is an example of a Protein viewer app, using the [NGL Viewer]\
(https://github.com/nglviewer/ngl).

You can import it from the `awesome-panel-extensions` package via
`from awesome_panel_extensions.widgets.ngl_viewer import NGLViewer`.

The NGL Viewer was developed with help from the community. Checkout [Discourse 583]\
(https://discourse.holoviz.org/t/how-to-use-ngl-webgl-protein-viewer-in-panel/583).
"""

import panel as pn
import param
from awesome_panel_extensions.frameworks.fast.templates import FastTemplate
from awesome_panel_extensions.widgets.ngl_viewer import NGLViewer

from application.config import site

APPLICATION = site.create_application(
    url="ngl-molecule-viewer",
    name="NGL Molecule Viewer",
    author="Jochem Smit",
    introduction="Demo of the the NGL Molecule Viewer widget",
    description=__doc__,
    thumbnail_url="ngl-molecule-viewer.png",
    code_url="ngl-molecule-viewer.py",
    mp4_url="ngl-molecule-viewer.mp4",
    tags=["Panel", "NGL", "Molecule"],
)

DEFAULT_RCSB_ID = "1NKT"


class ProteinViewer(param.Parameterized):
    """This is an example of a Protein viewer app, using the [NGL Viewer]\
(https://github.com/nglviewer/ngl)."""

    input_option = param.Selector(default="RCSB PDB", objects=["RCSB PDB", "Upload File"])
    rcsb_id = param.String(default=DEFAULT_RCSB_ID)
    load_structure = param.Action(label="LOAD STRUCTURE")

    def __init__(self, **params):
        super().__init__(**params)
        self.load_structure = self._load_structure
        self.file_widget = pn.widgets.FileInput(accept=".pdb")
        self.ngl_html = NGLViewer(sizing_mode="stretch_both")
        self.ngl_html_container = pn.Column(self.ngl_html, height=600, sizing_mode="stretch_width")
        pn.state.onload(self._load_structure)

    def _load_structure(self, *_):
        if self.input_option == "Upload File":
            if self.file_widget.value:
                string = self.file_widget.value.decode()
                self.ngl_html.pdb_string = string
            else:
                pass
        elif self.input_option == "RCSB PDB":
            self.ngl_html.rcsb_id = self.rcsb_id

    def view(self):
        """Returns a view of the app in the FastTemplate"""
        pn.config.sizing_mode = "stretch_width"
        template = FastTemplate(title="NGL Molecule Viewer")
        settings = pn.Column(
            pn.pane.Markdown("## Settings", margin=0),
            *pn.Param(
                self.param, widgets={"load_structure": {"button_type": "primary"}}, show_name=False
            ),
            self.file_widget,
            self.ngl_html.param.representation,
            self.ngl_html.param.color_scheme,
            self.ngl_html.param.spin,
        )
        template.sidebar[:] = [settings]
        alert = pn.pane.Alert(
            """You can find **Rcsb ids** at <a href="https://www.rcsb.org/"
target="_blank">rcsb.org</a>. A few examples are: `2GQ5`, `3UOG` and `5TXH`.""",
            margin=0,
        )
        template.main[:] = [APPLICATION.intro_section(), alert, self.ngl_html_container]

        return template


@site.add(APPLICATION)
def view():
    """Returns the ProteinViewer app view"""
    viewer = ProteinViewer()
    return viewer.view()


if __name__.startswith("bokeh"):
    view().servable()
