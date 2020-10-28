#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
"""

from io import StringIO

import panel as pn
import param
from bokeh.sampledata.autompg import autompg


class DownloadApp(param.Parameterized):
    raw_data = param.DataFrame(constant=True)

    years = param.List(label="Years")
    mpg = param.Tuple(label="Mile per Gallon")

    gold_data = param.DataFrame()
    gold_data_rows = param.Integer()

    view = param.Parameter()

    def __init__(self, raw_data, **params):
        params["raw_data"] = raw_data
        super().__init__(**params)
        self._create_view()
        self.mpg = (self.raw_data.mpg.min(), self.raw_data.mpg.max())

    def _create_view(self):
        self.selection_panel = pn.Param(
            self,
            parameters=["years", "mpg"],
            widgets={
                "years": {
                    "type": pn.widgets.MultiChoice,
                    "options": list(self.raw_data.yr.unique()),
                    "margin": (0, 50, 0, 0),
                    "width": 250,
                },
                "mpg": {
                    "type": pn.widgets.RangeSlider,
                    "start": self.raw_data.mpg.min(),
                    "end": self.raw_data.mpg.max(),
                    "width": 300,
                },
            },
            show_name=False,
            default_layout=pn.Row,
        )
        self.str_panel = pn.pane.Str(object="", width=700)

        self.file_download = pn.widgets.FileDownload(
            callback=self._get_gold_data_as_file, filename="filtered_autompg.csv"
        )

        self.table_panel = pn.pane.DataFrame(height=200, width=700, sizing_mode="fixed")

        self.view = pn.Column(
            self.selection_panel,
            self.str_panel,
            self.file_download,
            self.table_panel,
            width=700,
        )

    def _get_gold_data_as_file(self):
        df = self.gold_data
        sio = StringIO()
        df.to_csv(sio)
        sio.seek(0)
        return sio

    @param.depends("years", "mpg", watch=True)
    def _update_gold_data(self, *events):
        years = self.years
        mpg = self.mpg
        df = self.raw_data

        if years:
            df = df[df.yr.isin(years)]
        self.gold_data = df[(df.mpg >= mpg[0]) & (df.mpg <= mpg[1])]
        self.gold_data_rows = len(self.gold_data)

    @param.depends("gold_data_rows", watch=True)
    def _update_str_panel(self, *events):
        self.str_panel.object = f"Rows: {self.gold_data_rows}"

    @param.depends("gold_data", watch=True)
    def _update_table_panel(self, *events):
        self.table_panel.object = self.gold_data


DownloadApp(raw_data=autompg).view.servable()
