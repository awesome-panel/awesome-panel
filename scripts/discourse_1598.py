import panel as pn
import ipyvolume as ipv
import numpy as np
FONTAWESOME_LINK = "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.5.0/css/font-awesome.css"
pn.config.css_files.append(FONTAWESOME_LINK)

N = 1000
x, y, z = np.random.normal(0, 1, (3, N))

fig = ipv.figure()
scatter = ipv.scatter(x, y, z, color="#4464ad")
pn.Column(pn.pane.Markdown("## Panel meets IPyVolume"), pn.panel(fig, margin=50)).servable()