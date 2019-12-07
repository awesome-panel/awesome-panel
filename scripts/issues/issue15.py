import panel as pn

text = r"""
```math
f(x) = \int_{-\infty}^\infty
\hat f(\xi)\,e^{2 \pi i \xi x}
\,d\xi
```
"""

app = pn.Column(pn.pane.Markdown(text))
app.servable()
