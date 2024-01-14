"""
Source: https://awesome-panel.org/resources/table_of_elements_with_wikipedia_row_content/
"""

import panel as pn
from bokeh.sampledata.periodic_table import elements

pn.extension("tabulator")

@pn.cache
def get_elements():
    return elements[
        ["atomic number", "name", "atomic mass", "metal", "year discovered"]
    ].set_index("atomic number")

periodic_df = get_elements()

@pn.cache # Caching is a hack to avoid flickering. It seems like row content is loaded twice otherwise
def content_fn(row):
    return pn.pane.HTML(
        f'<iframe src="https://en.wikipedia.org/wiki/{row["name"]}" width="100%" height="500px"></iframe>',
        sizing_mode="stretch_width"
    )

periodic_table = pn.widgets.Tabulator(
    periodic_df,
    layout="fit_columns",
    sizing_mode="stretch_both",
    row_content=content_fn,
    embed_content=True,
)

pn.template.FastListTemplate(
    site="Awesome Panel",
    site_url="https://awesome-panel.org",
    title="Table of Elements with Wikipedia row content",
    main=[periodic_table],
    accent="#F08080",
    main_layout=None,
    main_max_width="1024px",
).servable()
