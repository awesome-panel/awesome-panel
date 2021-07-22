import panel as pn

pn.config.sizing_mode = "stretch_width"
pn.extension()

pn.template.MaterialTemplate(
    sidebar=[
        pn.Column(
            pn.widgets.AutocompleteInput(options=["test"] * 1000),
            pn.widgets.Select(options=["a", "b", "c"]),
            pn.widgets.Select(name="under"),
        )
    ]
).save("save.html")
