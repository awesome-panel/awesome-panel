import panel as pn
import param

from awesome_panel.express.pane.web_component import WebComponent

JS = """
<script src="https://unpkg.com/@webcomponents/webcomponentsjs@2.2.7/webcomponents-loader.js"></script>
<script type="module" src="https://unpkg.com/@google/model-viewer/dist/model-viewer.js"></script>
<script nomodule src="https://unpkg.com/@google/model-viewer/dist/model-viewer-legacy.js"></script>
<script src="https://unpkg.com/resize-observer-polyfill@1.5.1/dist/ResizeObserver.js"></script>
"""

HTML="""
<model-viewer src="https://modelviewer.dev/shared-assets/models/Astronaut.glb" alt="A 3D model of an astronaut"
auto-rotate camera-controls>
</model-viewer>
"""

MODELS = {
    "Astronaut": "https://modelviewer.dev/shared-assets/models/Astronaut.glb",
    "Boom Box": "https://modelviewer.dev/shared-assets/models/glTF-Sample-Models/2.0/BoomBox/glTF-Binary/BoomBox.glb",
    "Brain Stem": "https://modelviewer.dev/shared-assets/models/glTF-Sample-Models/2.0/BrainStem/glTF-Binary/BrainStem.glb",
    "Corset": "https://modelviewer.dev/shared-assets/models/glTF-Sample-Models/2.0/Corset/glTF-Binary/Corset.glb",
    "Damaged Helmet": "https://modelviewer.dev/shared-assets/models/glTF-Sample-Models/2.0/DamagedHelmet/glTF-Binary/DamagedHelmet.glb",
    "Flight Helmet": "https://modelviewer.dev/shared-assets/models/glTF-Sample-Models/2.0/FlightHelmet/glTF/FlightHelmet.gltf",
    "Lantern": "https://modelviewer.dev/shared-assets/models/glTF-Sample-Models/2.0/Lantern/glTF-Binary/Lantern.glb",
    "Monkey": "https://modelviewer.dev/shared-assets/models/glTF-Sample-Models/2.0/Suzanne/glTF/Suzanne.gltf",
    "Water Bottles": "https://modelviewer.dev/shared-assets/models/glTF-Sample-Models/2.0/SpecGlossVsMetalRough/glTF-Binary/SpecGlossVsMetalRough.glb",
    "Robot Expressive": "https://modelviewer.dev/shared-assets/models/RobotExpressive.glb",
    "Transparency Test": "https://modelviewer.dev/shared-assets/models/alpha-blend-litmus.glb",
    "Metal Rough Spheres": "https://modelviewer.dev/shared-assets/models/glTF-Sample-Models/2.0/MetalRoughSpheres/glTF/MetalRoughSpheres.gltf",
}

SRC_DEFAULT = MODELS["Flight Helmet"]

HEIGHT_DEFAULT = 600
HEIGHT_BOUNDS = (50,1000)
WIDTH_DEFAULT = 600
WIDTH_BOUNDS = (50,1000)

BACKGROUND="#9E9E9E"

PARAMETERS = [
    "src",
    "height",
    "width",
    "exposure",
    # "auto_rotate",
    # "camera_controls",
]

class ModelViewer(WebComponent):
    """A Wired ModelViewer"""
    html = param.String(HTML)
    attributes_to_watch= param.Dict({"src": "src"})
    properties_to_watch= param.Dict({
        "exposure": "exposure",
        "auto-rotate": "auto_rotate",
        "camera-controls": "camera_controls",
    })

    src = param.ObjectSelector(default=SRC_DEFAULT, objects=MODELS)
    exposure = param.Number(1.0, bounds=(0, 2))
    auto_rotate = param.Boolean()
    camera_controls = param.Boolean()

    height = param.Integer(default=HEIGHT_DEFAULT, bounds=HEIGHT_BOUNDS)
    width = param.Integer(default=WIDTH_DEFAULT, bounds=WIDTH_BOUNDS)

    style = param.String()

    def __init__(self, **params):
        super().__init__(**params)

        self.css_pane = pn.pane.HTML()
        self.js_pane = pn.pane.HTML(JS)

        self._update_height_and_width()

    def view(self):
        return pn.Column(
            self,
            self.js_pane,
            self.css_pane,
            sizing_mode="stretch_both",
        )

    @param.depends("height", "width", watch=True)
    def _update_height_and_width(self):
        if self.height:
            height=self.height
        else:
            height=HEIGHT_DEFAULT
        if self.width:
            width=self.width
        else:
            width=WIDTH_DEFAULT

        self.css_pane.object = f"""
<style>
model-viewer {{
    height:{height}px;
    width:{width}px;
}}
</style>
"""
