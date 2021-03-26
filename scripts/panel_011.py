import panel as pn

pn.config.sizing_mode = "stretch_width"
header = pn.pane.Markdown(
    """# Autoreload Flag

The `--autoreload` flag enables high speed
reloads when you save the file

Use it via

```bash
panel serve name_of_file.py --autoreload
```

AWESOME!
"""
)

section = pn.Spacer(height=200, sizing_mode="stretch_width", background="purple")

app = pn.template.FastListTemplate(title="Panel - Autoreload", main=[header, section])
app.servable()
