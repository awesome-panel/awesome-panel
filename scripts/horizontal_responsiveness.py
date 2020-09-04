import panel as pn
import plotly.graph_objects as go
import plotly.io as pio
# pio.renderers.default = "browser"

fig = go.Figure()
fig.add_trace(go.Scatter(x=[1, 2, 3], y=[1, 3, 1]))
fig.layout.autosize=True
pp = pn.pane.Plotly(fig, config={'responsive': True}, sizing_mode="stretch_both")
app = pn.Column(
    '# A responsive plot ?',
    pn.Row(pp, pn.Spacer(width=10, background="blue"), background="lightgray", sizing_mode="stretch_both"),
    sizing_mode='stretch_both')
app.servable()