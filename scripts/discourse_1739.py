import panel as pn
import panel.widgets as pnw
import pandas as pd;
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvas

DATA_URL = "https://raw.githubusercontent.com/LuisM78/Occupancy-detection-data/master/datatraining.txt"

data = pd.read_csv(DATA_URL)
data['date'] = data.date.astype('datetime64[ns]')
data = data.set_index('date')

variable  = pnw.RadioButtonGroup(name='variable', value='Temperature',
                                 options=list(data.columns))
window  = pnw.IntSlider(name='window', value=10, start=1, end=60)

def mpl_plot(avg, highlight):
    fig = Figure()
    FigureCanvas(fig) # not needed in mpl >= 3.1
    ax = fig.add_subplot()
    avg.plot(ax=ax)
    if len(highlight): highlight.plot(style='o', ax=ax)
    return fig

def find_outliers(variable='Temperature', window=30, sigma=10, view_fn=mpl_plot):
    avg = data[variable].rolling(window=window).mean()
    residual = data[variable] - avg
    std = residual.rolling(window=window).std()
    outliers = (np.abs(residual) > std * sigma)
    return view_fn(avg, avg[outliers])

@pn.depends(variable, window)
def reactive_outliers(variable, window):
    return find_outliers(variable, window, 10)

widgets   = pn.Column("<br>\n# Room occupancy", variable, window)
occupancy = pn.Row(reactive_outliers, widgets)
occupancy.servable()