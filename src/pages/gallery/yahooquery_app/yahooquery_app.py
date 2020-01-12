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

# import altair as alt
import pandas as pd
import panel as pn
import param
from yahooquery import Ticker

import awesome_panel.express as pnx

# from awesome_panel.express.widgets.dataframe import get_default_formatters

# TTodo
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
    """Wrapper around the yahooquery package"""

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
        except TypeError:
            data = getattr(ticker, attribute)
        return data

    @staticmethod
    @lru_cache(2048)
    def to_ticker(symbols: str) -> Ticker:
        """Converts a comma seperated list of tickers to a Ticker

        Args:
            symbols (str): Comma seperated list of tickers

        Returns:
            Ticker: Ticker object that can be used to request data from Yahoo Finance
        """
        symbols_list = [x.strip() for x in symbols.split(",")]
        return Ticker(symbols_list)


# TTodo: Move to pnx and create tests
# TTodo: Make Calendar Event stand beautifully
# TTodo: Add <hr>
def pnx_help(python_object: object) -> pn.pane.Viewable:
    """Helper function that convert a python object into a viewable help text

    Args:
        python_object (object): Any python object

    Returns:
        pn.pane.Viewable: A Viewable showing the docstring and more
    """
    return pnx.Code(
        f"""{str(type(python_object))}

{python_object.__doc__}""",
        language="bash",
    )


# TTodo: Move to pnx and create tests
def pnx_json(python_object: object, indent=2) -> pn.pane.Viewable:
    """Converts and json serialisabe object into Viewable

    Args:
        python_object (object): Any json serializable object
        indent (int, optional): The indentation level of the json output. Defaults to 2.

    Returns:
        pn.pane.Viewable: [description]
    """
    return pnx.Code(json.dumps(python_object, indent=indent), language="json")


class Page(param.Parameterized):
    """A base class for a Page.

    Don't use this on a standalone basis"""

    symbols = param.String("ORSTED.CO")


class HomePage(Page):
    """Provides the view of the Home Page"""

    def _text(self):
        return f"""
            This app demonstrates the use of the [YahooQuery]\
(https://github.com/dpguthrie/yahooquery) package.

            This app was first developed in Streamlit by [Doug Guthrie](https://github/dpguthrie)).
            See the [yahooquery-streamlit repo](https://github.com/dpguthrie/yahooquery-streamlit).

            You can see the Streamlit version in the gallery at
            [awesome-streamlit.org](awesome-streamlit.org)

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
    def view(self) -> pn.pane.Viewable:
        """The main view of the HomePage

        Returns:
            pn.pane.Viewable: The main view of the HomePage
        """
        return pnx.Markdown(self._text(), sizing_mode="stretch_width")


class BasePage(Page):
    """A view of the basic functionality of Ticker.

    The user can select an endpoint and the help text, code and result will be presented."""

    endpoint = param.ObjectSelector(default="asset_profile", objects=BASE_ENDPOINTS)
    frequency = param.ObjectSelector(default="a", objects={"Annual": "a", "Quarterly": "q"})

    @property
    def attr(self) -> object:
        """The Ticker.<endpoint> attribute

        Returns:
            object: The Ticker.<endpoint> attribute]
        """
        return getattr(Ticker, self.endpoint)

    @property
    def attr_is_property(self) -> bool:
        """Whether or not self.attr is a property

        Returns:
            bool: Return True if self.attr is a property. Oherwise False is returned.
        """
        return isinstance(self.attr, property)

    @param.depends("endpoint")
    def _help(self):
        if self.endpoint:
            return pnx_help(self.attr)
        return ""

    @param.depends("endpoint")
    def _frequency_widget(self):
        if self.attr_is_property:
            return pn.pane.HTML()
        return self.param.frequency

    @param.depends("endpoint", "frequency")
    def _code(self):
        if self.attr_is_property:
            return pnx.Code(f"Ticker('{self.symbols}').{self.endpoint}", language="python")
        return pnx.Code(f"Ticker('{self.symbols}').{self.endpoint}(frequency='{self.frequency}')")

    @param.depends("symbols", "endpoint", "frequency")
    def _data(self):
        if self.attr_is_property:
            data = YahooQueryService.get_data(self.symbols, self.endpoint)
        else:
            data = YahooQueryService.get_data(self.symbols, self.endpoint, self.frequency)
        if isinstance(data, pd.DataFrame):
            # Enable formatters when https://github.com/holoviz/panel/issues/941 is solved
            # formatters = get_default_formatters(data)
            return pn.widgets.DataFrame(data, fit_columns=True, sizing_mode="stretch_width")

        return pnx_json(data)

    @param.depends("symbols")
    def view(self) -> pn.pane.Viewable:
        """The main view of the BasePage

        Returns:
            pn.pane.Viewable: The main view of the BasePage
        """
        return pn.Column(
            pn.pane.Markdown(
                """
            ## Base - Single Endpoint

            Select an option below to see the data available through
            the base endpoints."""
            ),
            self.param.endpoint,
            self._frequency_widget,
            self._code,
            self._help,
            self._data,
            sizing_mode="stretch_width",
        )


class BaseMultiplePage(Page):
    """A view for multiple Ticker requests

    The user can select all or multiple endpoints and the help text, code and result will be
    presented."""

    all_endpoints = param.Boolean(
        default=False, doc="If True all endpoints should be requested otherwise only multiple"
    )
    endpoints = param.ListSelector(
        default=["assetProfile"],
        objects=sorted(Ticker._ENDPOINTS),  # pylint: disable=protected-access
    )

    @param.depends("all_endpoints")
    def _endpoints_widget(self):
        if not self.all_endpoints:
            return pn.Param(self.param.endpoints, widgets={"endpoints": {"height": 600},})
        return None

    @param.depends("all_endpoints", "endpoints")
    def _help(self):
        if self.all_endpoints:
            return pnx_help(Ticker.all_endpoints)
        return pnx_help(Ticker.get_endpoints)

    @param.depends("symbols", "all_endpoints", "endpoints")
    def _code(self):
        if self.all_endpoints:
            return pnx.Code(f"Ticker('{self.symbols}').all_endpoints", language="python")
        return pnx.Code(f"Ticker('{self.symbols}').get_endpoints({self.endpoints})")

    @param.depends("symbols", "all_endpoints", "endpoints")
    @PROGRESS.report(message="Requesting data from Yahoo Finance")
    def _data(self):
        if self.all_endpoints:
            data = YahooQueryService.get_data(self.symbols, "all_endpoints")
        else:
            if not self.endpoints:
                return pnx.InfoAlert("Please select one or more Endpoints")

            data = YahooQueryService.get_data(self.symbols, "get_endpoints")(self.endpoints)
        return pnx_json(data)

    @param.depends("symbols")
    def view(self) -> pn.pane.Viewable:
        """The main view of the BasePage

        Returns:
            pn.pane.Viewable: The main view of the BasePage
        """
        return pn.Column(
            pn.Row(
                pn.Column(
                    pn.pane.Markdown("## Base - Multiple Requests"),
                    self._help,
                    self._code,
                    self._data,
                    sizing_mode="stretch_width",
                ),
                pn.layout.VSpacer(width=1, margin=(0, 10)),
                pn.Column(self.param.all_endpoints, self._endpoints_widget,),
            ),
            sizing_mode="stretch_width",
        )


class OptionsPage(Page):
    """Options Page"""

    @param.depends("tickers")
    def view(self) -> pn.pane.Viewable:
        """The main view of the BasePage

        Returns:
            pn.pane.Viewable: The main view of the BasePage
        """
        return "Hello OptionsPage" + self.symbols


class HistoryPage(Page):
    """History Page"""

    @param.depends("tickers")
    def view(self) -> pn.pane.Viewable:
        """The main view of the BasePage

        Returns:
            pn.pane.Viewable: The main view of the BasePage
        """
        return "Hello HistoryPage" + self.symbols


class YahooQueryView(pn.Column):
    """A View of the Yahoo Query App"""

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
            self._symbols_widget(symbols),
            pn.layout.VSpacer(height=25),
            PROGRESS.view,
            self.pages_view(pages),
            sizing_mode=sizing_mode,
            **kwargs,
        )

    @staticmethod
    def _symbol_lookup_link() -> pn.pane.Viewable:
        return pn.pane.Markdown(
            "<a href='https://finance.yahoo.com/lookup' target='_blank'>"
            "<i class='fas fa-search'></i></a>"
        )

    def _symbols_widget(
        self, symbols: pn.pane.Viewable, sizing_mode: str = "stretch_width"
    ) -> pn.pane.Viewable:
        return pn.Row(symbols, self._symbol_lookup_link(), sizing_mode=sizing_mode)

    @staticmethod
    def pages_view(
        pages: List[Tuple[str, pn.pane.Viewable]], sizing_mode: str = "stretch_width"
    ) -> pn.Tabs:
        """A Tabbed view of the pages

        Args:
            pages (List[Tuple[str, pn.pane.Viewable]]): A list of Pages to display
            sizing_mode (str, optional): The sizing mode of the pages_view. Defaults to \
                "stretch_width".

        Returns:
            pn.Tabs: [description]
        """
        return pn.Tabs(*pages, sizing_mode=sizing_mode,)


class YahooQueryApp(Page):
    """The main app makes the yahooquery package interactive"""

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
    def _set_pages(self):
        for page in self.pages.values():
            page.symbols = self.symbols

    def view(self) -> pn.pane.Viewable:
        """The main view of the app

        Returns:
            pn.pane.Viewable: Serve this via .servable()
        """
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

    import ptvsd

    ptvsd.enable_attach(address=("localhost", 5678))
    print("Ready to attach the VS Code debugger")
    ptvsd.wait_for_attach()  # Only include this line if you always wan't to attach the debugger

    BaseMultiplePage().view().servable()
    # view().servable()
