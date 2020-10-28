import panel as pn
import param
from bokeh.sampledata.autompg import autompg

pn.pane.DataFrame(autompg, height=300, width=700, background="blue").servable()
