import holoviews as hv
import panel as pn

hv.extension("bokeh")
CSS = """
.bk-root .bk {
  background: blue;
}"""
# pn.config.raw_css.append(CSS)

relations = [
    ("William Gibson", "Alfred Bester", 1),
    ("John Maynard Keynes", "Alfred Marshall", 1),
    ("Haskell Curry", "Alfred North Whitehead", 1),
    ("Haskell Brooks Curry", "Alfred North Whitehead", 1),
    ("Willard Van Orman Quine", "Alfred North Whitehead", 1),
]
pn.config.sizing_mode = "stretch_width"

plot = hv.Graph(relations, vdims="weight")
pn.Column(plot).servable()
