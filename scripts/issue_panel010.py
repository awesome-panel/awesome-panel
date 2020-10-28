import panel as pn

long_text = "abcde" * 10

pn.template.MaterialTemplate(
    title="Hello World",
    sidebar=long_text,
    main=long_text,
).servable()
