import pathlib
from typing import List, NamedTuple

import numpy as np
import pandas as pd
import panel as pn
import param
from plotly import express as px
from products.products import Products

ABOUT_PATH = pathlib.Path(__file__).parent / "about.md"


class Orders:
    def __init__(self):
        chart_data = {
            "Day": [
                "Sunday",
                "Monday",
                "Tuesday",
                "Wednesday",
                "Thursday",
                "Friday",
                "Saturday",
            ],
            "Orders": [15539, 21345, 18483, 24003, 23489, 24092, 12034],
        }
        self.chart_data = pd.DataFrame(chart_data)

        table_data = [
            (1001, "Lorem", "ipsum", "dolor", "sit"),
            (1002, "amet", "consectetur", "adipiscing", "elit"),
            (1003, "Integer", "nec", "odio", "Praesent"),
            (1003, "libero", "Sed", "cursus", "ante"),
            (1004, "dapibus", "diam", "Sed", "nisi"),
            (1005, "Nulla", "quis", "sem", "at"),
            (1006, "nibh", "elementum", "imperdiet", "Duis"),
            (1007, "sagittis", "ipsum", "Praesent", "mauris"),
            (1008, "Fusce", "nec", "tellus", "sed"),
            (1009, "augue", "semper", "porta", "Mauris"),
            (1010, "massa", "Vestibulum", "lacinia", "arcu"),
            (1011, "eget", "nulla", "Class", "aptent"),
            (1012, "taciti", "sociosqu", "ad", "litora"),
            (1013, "torquent", "per", "conubia", "nostra"),
            (1014, "per", "inceptos", "himenaeos", "Curabitur"),
            (1015, "sodales", "ligula", "in", "libero"),
        ]
        self.table_data = pd.DataFrame(
            table_data, columns=["#", "Header", "Header", "Header", "Header"]
        ).set_index("#")

    def _chart(self):
        fig = px.line(self.chart_data, x="Day", y="Orders")
        fig.update_traces(
            mode="lines+markers", marker=dict(size=10), line=dict(width=4)
        )
        fig.layout.autosize = True
        fig.layout.paper_bgcolor = "rgba(0,0,0,0)"
        fig.layout.plot_bgcolor = "rgba(0,0,0,0)"
        return pn.pane.Plotly(fig)

    def _table(self):
        return pn.Row(self.table_data, sizing_mode="stretch_width")

    def view(self):
        return pn.Column(
            pn.pane.Markdown("## Dashboard"),
            self._chart(),
            pn.pane.Markdown("## Section Title"),
            self._table(),
            sizing_mode="stretch_width",
        )


def markdown_from_file(path: pathlib.Path) -> pn.Pane:
    with open(path, "r") as file:
        text = file.read()

    return pn.pane.Markdown(text)


def simple():
    path = pathlib.Path(__file__).parent / "templates" / "simple.html"
    with open(path, "r") as file:
        template_html = file.read()
    app = pn.Template(template_html)
    app = pn.panel(app)
    return app


class PageConfig(NamedTuple):
    name: str
    font_awesome_class: str
    pane: pn.Pane


PAGE_CONFIGS = [
    PageConfig("Dashboard", "fas fa-home", Orders().view()),
    PageConfig("Products", "far fa-file", Products()),
    PageConfig("Customers", "fas fa-file", simple()),
    PageConfig("Reports", "fas fa-file", pn.pane.Markdown("Reports")),
    PageConfig("Integrations", "fas fa-file", pn.pane.Markdown("Integrations")),
    PageConfig("About", "fas fa-file", markdown_from_file(ABOUT_PATH)),
]
PAGES = {page_config.name: page_config for page_config in PAGE_CONFIGS}
PAGE_NAMES = [page_config.name for page_config in PAGE_CONFIGS]


class PageView(param.Parameterized):
    page = param.ObjectSelector(default=PAGE_NAMES[0], objects=PAGE_NAMES)

    def select(self) -> pn.Pane:
        def set_page(event):
            self.page = event.obj.name

        menuitems = []
        for page in PAGES.values():
            button = pn.widgets.Button(name=page.name)
            button.on_click(set_page)
            menuitems.append(button)

        return pn.WidgetBox(
            *menuitems, sizing_mode="stretch_width", css_classes=["pageview-select"]
        )

    @param.depends("page")
    def view(self) -> pn.Pane:
        return pn.Column(
            PAGES[self.page].pane, sizing_mode="stretch_width", width_policy="max"
        )

