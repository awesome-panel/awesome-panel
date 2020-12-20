import panel as pn

pn.extension()

import pythreejs
import ipyvolume as ipv
import ipywidgets as widgets

import numpy as np
pn.sizing_mode="stretch_width"

FONTAWESOME_LINK = "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.5.0/css/font-awesome.css"
pn.config.css_files.append(FONTAWESOME_LINK)

N = 1000
x, y, z = np.random.normal(0, 1, (3, N))

fig = ipv.figure(width=400, height=400)
scatter = ipv.scatter(x, y, z, color="#4464ad")

control = pythreejs.OrbitControls(controlling=fig.camera)
fig.controls = control
control.autoRotate = False
fig.render_continuous = True  # the controls does not update itself
# if we toggle this setting, ipyvolume will update the controls

toggle_rotate = widgets.ToggleButton(description="Rotate")
widgets.jslink((control, "autoRotate"), (toggle_rotate, "value"))


pn.Column(
    pn.pane.Markdown("## Panel meets IPyVolume"),
    pn.panel(toggle_rotate),
    pn.panel(fig, margin=50),
    width=800,
).servable()
