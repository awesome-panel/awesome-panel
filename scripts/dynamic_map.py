import streamlit as st
import numpy as np
import holoviews as hv
import panel as pn

frequencies = [0.5, 0.75, 1.0, 1.25]


def sine_curve(phase, freq):
    xvals = [0.1 * i for i in range(100)]
    return hv.Curve((xvals, [np.sin(phase + freq * x) for x in xvals]))

@st.cache
def get_plots():
    plots = {}
    for i in range(10):
        for j in range(10):
            phase = 0.5+float(i)*0.05
            frequency = 0.5+float(j)+0.075
            plots[(phase, frequency)] = sine_curve(phase, frequency)
    return plots


plots = get_plots()
hmap = hv.HoloMap(plots, kdims=["phase", "frequency"])
hmap_bokeh = pn.panel(hmap).get_root()
st.bokeh_chart(hmap_bokeh)
