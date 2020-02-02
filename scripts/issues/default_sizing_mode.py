import panel as pn

pn.config.sizing_mode = "stretch_width"

is_not_fixed_width = pn.Row("# Is not fixed width", background="salmon", width=300)
is_fixed_width = pn.Row("# Is fixed width", background="orange", width=300, sizing_mode="fixed")

pn.Column(is_not_fixed_width, is_fixed_width, background="lightgray").servable()

