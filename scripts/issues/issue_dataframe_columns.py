import panel as pn
from yahooquery import Ticker

data = Ticker("ORSTED.CO").balance_sheet(frequency="annual")
app = pn.pane.DataFrame(data, sizing_mode="stretch_width",)
app.servable()
