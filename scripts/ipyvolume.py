"""Simple IpyVolume app to demonstrate that it is possible to use IpyWidgets in the site"""
import ipyvolume as ipv
import ipywidgets as ipw
import numpy as np
import panel as pn
from panel.template import FastListTemplate


def _get_ipyvolume_app():
    # pylint: disable=invalid-name, no-member
    x, y, z = np.random.random((3, 1000))
    ipv.quickscatter(x, y, z, size=1, marker="sphere")
    ipv_plot = ipv.current.figure
    ipv_plot.width = 600
    ipv_plot.height = 600

    def randomize(_):
        x, y, z = np.random.random((3, 1000))
        scatter = ipv_plot.scatters[0]
        with ipv_plot.hold_sync():
            scatter.x = x
            scatter.y = y
            scatter.z = z

    ip_randomize = ipw.Button(description="Randomize")
    ip_randomize.on_click(randomize)

    return ipw.VBox([ip_randomize, ipv_plot])


template = FastListTemplate(
    title="IpyVolume",
    row_height=100,
)
app = _get_ipyvolume_app()
template.main[:] = [pn.pane.IPyWidget(app, sizing_mode="stretch_both", margin=15, height=800)]
template.servable()
