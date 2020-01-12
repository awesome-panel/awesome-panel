"""
## YahooQuery Demo

This app allows you to demo the [yahooquery](https://github.com/dpguthrie/yahooquery) python package

This app was first developed in Streamlit by [Doug Guthrie](https://github/dpguthrie)). See \
    [yahooquery-streamlit](https://github.com/dpguthrie/yahooquery-streamlit). You can see a live
    version in the gallery at [awesome-streamlit.org](awesome-streamlit.org)

This version of the app is developed in [Panel](https://panel.pyviz.org/) by [Marc Skov Madsen]\
    (https://datamodelsanalytics.com)
"""
import json
from functools import lru_cache
from typing import Dict, List, Tuple

import altair as alt
import pandas as pd
import panel as pn
import param
from yahooquery import Ticker

import awesome_panel.express as pnx
from awesome_panel.express.widgets.dataframe import get_default_formatters

# Todo
# - color active tab "info" blue
# - format table

PROGRESS = pnx.ProgressExt()

BASE_ENDPOINTS = {
    "Asset Profile": "asset_profile",
    "Balance Sheet": "balance_sheet",
    "Calendar Events": "calendar_events",
    "Cash Flow": "cash_flow",
    "Company Officers": "company_officers",
    "ESG Scores": "esg_scores",
    "Earning History": "earning_history",
    "Financial Data": "financial_data",
    "Fund Bond Holdings": "fund_bond_holdings",
    "Fund Bond Ratings": "fund_bond_ratings",
    "Fund Equity Holdings": "fund_equity_holdings",
    "Fund Holding Information": "fund_holding_info",
    "Fund Ownership": "fund_ownership",
    "Fund Performance": "fund_performance",
    "Fund Profile": "fund_profile",
    "Fund Sector Weightings": "fund_sector_weightings",
    "Fund Top Holdings": "fund_top_holdings",
    "Grading History": "grading_history",
    "Income Statement": "income_statement",
    "Insider Holders": "insider_holders",
    "Insider Transactions": "insider_transactions",
    "Institution Ownership": "institution_ownership",
    "Key Statistics": "key_stats",
    "Major Holders": "major_holders",
    "Pricing": "price",
    "Quote Type": "quote_type",
    "Recommendation Trends": "recommendation_trend",
    "SEC Filings": "sec_filings",
    "Share Purchase Activity": "share_purchase_activity",
    "Summary Detail": "summary_detail",
    "Summary Profile": "summary_profile",
}


class YahooQueryService:
    @classmethod
    @lru_cache(2048)
    @PROGRESS.report(message="Requesting data from Yahoo Finance")
    def get_data(cls, symbols: str, attribute: str, *args) -> Dict:
        """Gets data from yahoo

        Arguments:
            symbols {str} -- a comma separated list of tickers
            attribute {str} -- The attribute of Ticker to call. Will return the results of a call to
                corresponding yahoo finance endpoint.

        Returns:
            Dict -- A Dictionary of data from Yahoo
        """
        ticker = cls.to_ticker(symbols)

        try:
            data = getattr(ticker, attribute)(*args)
            print(*args)
        except TypeError:
            print("error")
            data = getattr(ticker, attribute)
        return data

    @staticmethod
    @lru_cache(2048)
    def to_ticker(symbols: str) -> Ticker:
        symbols_list = [x.strip() for x in symbols.split(",")]
        return Ticker(symbols_list)


# Todo: Move to pnx and create tests
# Todo: Make Calendar Event stand beautifully
# Todo: Add <hr>
def pnx_help(python_object: object):
    return pnx.Code(
        f"""{str(type(python_object))}

{python_object.__doc__}""",
        language="bash",
    )


# Todo: Move to pnx and create tests
def pnx_json(python_object: object, indent=2):
    return pnx.Code(json.dumps(python_object, indent=indent), language="json")
    # try:
    #     return pnx.Code(json.dumps(python_object, indent=2), language="json")
    # except expression as identifier:
    #     return pnx.Code(json.dumps(python_object.to_dict(), indent=2), language="json")


class Page(param.Parameterized):
    """A base class for a Page.

    Don't use this on a standalone basis"""

    symbols = param.String("ORSTED.CO")
    # ticker = param.ClassSelector(class_=Ticker)


class HomePage(Page):
    """Provides the view of the Home Page"""

    def _text(self):
        return f"""
            This app demonstrates the use of the [YahooQuery]\
(https://github.com/dpguthrie/yahooquery) package.

            ### Instructions

            Enter a symbol or list of symbols in the box above (**comma
            separated**).  Then select different pages in the dropdown to view
            the data available to you.

            ### Installation

            ```python
            pip install yahooquery
            ```

            ### Ticker Usage

            The `Ticker` class provides the access point to data residing on
            Yahoo Finance.  It accepts either a symbol or list of symbols.
            Additionally, you can supply `formatted` as a keyword argument
            to the class to format the data returned from the API (default is
            `True`)

            ```python
            from yahooquery import Ticker

            tickers = Ticker({self.symbols})
            ```

            ```bash
            {str(type(Ticker))}

            {Ticker.__doc__}
            ```
            """

    @param.depends("symbols")
    def view(self):
        return pnx.Markdown(self._text(), sizing_mode="stretch_width")


class BasePage(Page):
    """A view of the basic functionality of Ticker.

    The user can select an endpoint and the help text, code and result will be presented."""

    endpoint = param.ObjectSelector(default="asset_profile", objects=BASE_ENDPOINTS)
    frequency = param.ObjectSelector(default="q", objects={"Annual": "a", "Quarterly": "q"})

    @property
    def attr(self):
        return getattr(Ticker, self.endpoint)

    @property
    def attr_is_property(self):
        return isinstance(self.attr, property)

    @param.depends("endpoint")
    def _help(self):
        if self.endpoint:
            return pnx_help(self.attr)
        return ""

    @param.depends("endpoint")
    def frequency_edit_view(self):
        if self.attr_is_property:
            return pn.pane.HTML()
        return self.param.frequency

    @param.depends("endpoint", "frequency")
    def _code(self):
        print("a")
        if self.attr_is_property:
            return pnx.Code(f"Ticker('{self.symbols}').{self.endpoint}", language="python")
        return pnx.Code(f"Ticker('{self.symbols}').{self.endpoint}(frequency='{self.frequency}')")

    @param.depends("symbols", "endpoint", "frequency")
    def _data(self):
        print("b")
        if self.attr_is_property:
            print("d1")
            data = YahooQueryService.get_data(self.symbols, self.endpoint)
        else:
            print("d2")
            data = YahooQueryService.get_data(self.symbols, self.endpoint, self.frequency)
        print("e")
        if isinstance(data, pd.DataFrame):
            print("f")
            formatters = get_default_formatters(data)
            print(formatters)
            print(data)
            print("g")
            try:
                dataframe = pn.widgets.DataFrame(
                    data, fit_columns=True, formatters=formatters, sizing_mode="stretch_width"
                )
            except Exception as e:
                print("h")
            print("i")
            return dataframe

        return pnx_json(data)

    @param.depends("symbols")
    def view(self):
        print("c")
        return pn.Column(
            pn.pane.Markdown(
                """
            ## Base Endpoints

            Select an option below to see the data available through
            the base endpoints."""
            ),
            self.param.endpoint,
            self.frequency_edit_view,
            self._code,
            self._help,
            self._data,
            sizing_mode="stretch_width",
        )


class BaseMultiplePage(Page):
    @param.depends("tickers")
    def view(self):
        return "Hello BaseMultiplePage" + self.symbols


class OptionsPage(Page):
    @param.depends("tickers")
    def view(self):
        return "Hello OptionsPage" + self.symbols


class HistoryPage(Page):
    @param.depends("tickers")
    def view(self):
        return "Hello HistoryPage" + self.symbols


class YahooQueryView(pn.Column):
    def __init__(
        self,
        symbols: pn.pane.Viewable,
        pages: List[Tuple[str, pn.pane.Viewable]],
        sizing_mode="stretch_width",
        **kwargs,
    ):
        super().__init__(
            pn.pane.Markdown(
                """# Welcome to [YahooQuery](https://github.com/dpguthrie/yahooquery)"""
            ),
            self.symbol_selection_view(symbols),
            pn.layout.VSpacer(height=25),
            PROGRESS.view,
            self.pages_view(pages),
            sizing_mode=sizing_mode,
            **kwargs,
        )

    def _symbol_lookup_view(self) -> pn.pane.Viewable:
        return pn.pane.Markdown(
            "<a href='https://finance.yahoo.com/lookup' target='_blank'>"
            "<i class='fas fa-search'></i></a>"
        )

    def symbol_selection_view(
        self, symbols: pn.pane.Viewable, sizing_mode: str = "stretch_width"
    ) -> pn.pane.Viewable:
        return pn.Row(symbols, self._symbol_lookup_view(), sizing_mode=sizing_mode)

    def pages_view(
        self, pages: List[Tuple[str, pn.pane.Viewable]], sizing_mode: str = "stretch_width"
    ):
        return pn.Tabs(*pages, sizing_mode=sizing_mode,)


class YahooQueryApp(Page):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pages = {
            "Introduction": HomePage(),
            "Base": BasePage(),
            "Base - Multiple": BaseMultiplePage(),
            "Options": OptionsPage(),
            "History": HistoryPage(),
        }

    @param.depends("symbols", watch=True)
    def set_tickers(self):
        for page in self.pages.values():
            page.symbols = self.symbols

    def view(self) -> pn.pane.Viewable:
        pages_list = [(key, value.view()) for key, value in self.pages.items()]

        return YahooQueryView(self.param.symbols, pages_list, sizing_mode="stretch_width")


def view():
    """A Reactive View of the YahooQueryApp

    This function is required for use in the Gallery as awesome-panel.org
    """
    return YahooQueryApp().view()


if __name__.startswith("bk"):
    pn.extension()
    pnx.Code.extend()
    pnx.fontawesome.extend()
    pnx.bootstrap.extend()
    view().servable()
