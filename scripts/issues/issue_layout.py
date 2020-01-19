import panel as pn

css = """
.widget-box {
  background: blue;
  border-radius: 0px !important;
  border-width: 0px !important;
}
"""
pn.extension(raw_css=[css])
gspec = pn.GridSpec(width=200, height=200,)
gspec[0, 0:2,] = pn.pane.Markdown("Grid1", background="green", margin=0,)
gspec[1, 0:1,] = pn.pane.Markdown("Grid2", background="green", margin=0,)
gspec[1, 1,] = pn.widgets.FloatSlider(name="Widget", margin=0, css_classes=["widget-box"],)
gspec.servable()
