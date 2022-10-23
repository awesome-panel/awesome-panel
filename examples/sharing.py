from panel_sharing import sharing

if __name__.startswith("bokeh"):
    sharing.create().servable()