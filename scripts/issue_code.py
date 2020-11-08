"""An example use case is

```python
import time

import panel as pn
from awesome_panel_extensions.widgets.progress_ext import ProgressExt

progress = ProgressExt()
run_button = pn.widgets.Button(name="Click me")

@progress.increment(50, "incrementing ...")
def run(event):
    time.sleep(0.5)
run_button.on_click(run)

app = pn.Column(run_button, progress.view)
app.servable()
```

which will show the progress and reset every 2 clicks.
"""
import panel as pn

STYLE = """
<style>
div.codehilite pre {
    padding: 0.75rem 1.25rem;
    border-radius: 6px;
    background: rgb(246, 248, 250);
}
</style>
"""
pn.Column(
    pn.pane.Markdown(__doc__),
    pn.pane.HTML(STYLE),
).servable()
