from io import BytesIO

import panel as pn
import requests
from PIL import Image

URL = "https://panel.pyviz.org/_static/logo_stacked.png"

response = requests.get(URL)
bytes_io = BytesIO(response.content)
img = Image.open(bytes_io)

app = pn.pane.PNG(bytes_io)
app = pn.Column(
    pn.pane.Markdown("# From URL"),
    pn.pane.PNG(URL),
    pn.pane.Markdown("# From PIL Image"),
    pn.pane.PNG(img),
)
app.servable()
