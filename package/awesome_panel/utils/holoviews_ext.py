import holoviews as hv
def _disable_logo_func(plot, element):
    plot.state.toolbar.logo = None

def disable_bokeh_logo():
    plot = hv.plotting.bokeh.ElementPlot
    if not _disable_logo_func in plot.hooks:
        plot.hooks.append(_disable_logo_func)