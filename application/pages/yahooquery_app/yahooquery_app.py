"""This app allows you to demo the [yahooquery](https://github.com/dpguthrie/yahooquery) python
package.

This app was first developed in Streamlit by [Doug Guthrie](https://github/dpguthrie)). See \
[yahooquery-streamlit](https://github.com/dpguthrie/yahooquery-streamlit). You can see a live
version in the gallery at [awesome-streamlit.org](awesome-streamlit.org)

This app could be speeded if the use of `panel.layout.Tabs` was replaced by the tabs of the
[Golden Layout Template](https://panel.holoviz.org/reference/templates/GoldenLayout.html) or a
[Custom Panel Template](https://panel.holoviz.org/user_guide/Templates.html). Furthermore the
implementation is something I did *early on* and could be simplified and made easier to understand.
"""
import datetime
from functools import lru_cache
from typing import Dict, List, Tuple

import altair as alt
import awesome_panel.express as pnx

# import awesome_panel.express as pnx
import pandas as pd
import panel as pn
import param
from awesome_panel_extensions.pane import Code
from awesome_panel_extensions.widgets.progress_ext import ProgressExt
from yahooquery import Ticker

from application.config import site

PERIOD_END_DATE = datetime.datetime.now().date()
PERIOD_START_DATE = PERIOD_END_DATE - datetime.timedelta(days=365)
DATE_BOUNDS = (
    datetime.datetime(
        1900,
        1,
        1,
    ).date(),
    PERIOD_END_DATE,
)

# from awesome_panel.express.widgets.dataframe import get_default_formatters

# TTodo
# - color active tab "info" blue
# - format table

PROGRESS = ProgressExt()

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
APPLICATION = site.create_application(
    name="Yahoo Query",
    introduction="Shows how you can use the Yahoo Query package in your Panel apps",
    description=__doc__,
    url="yahoo-query",
    thumbnail_url="yahooquery_app.png",
    code_url="yahooquery_app/yahooquery_app.py",
    mp4_url="",
    gif_url="",
    author="Marc Skov Madsen",
    tags=["Finance", "api"],
)


class YahooQueryService:
    """Wrapper around the yahooquery package"""

    @classmethod
    @lru_cache(2048)
    def get_data(
        cls,
        symbols: str,
        attribute: str,
        *args,
    ) -> Dict:
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
            data = getattr(
                ticker,
                attribute,
            )(*args)
        except TypeError:
            data = getattr(
                ticker,
                attribute,
            )
        return data

    @staticmethod
    @lru_cache(2048)
    def to_ticker(
        symbols: str,
    ) -> Ticker:
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
def pnx_help(
    python_object: object,
) -> pn.viewable.Viewable:
    """Helper function that convert a python object into a viewable help text

    Args:
        python_object (object): Any python object

    Returns:
        pn.viewable.Viewable: A Viewable showing the docstring and more
    """
    return pn.Column(
        pnx.SubHeader(" Documentation"),
        Code(
            str(python_object.__doc__),
            language="bash",
        ),
    )


# TTodo: Move to pnx and create tests
def pnx_json(python_object: object) -> pn.viewable.Viewable:
    """Converts and json serialisabe object into Viewable

    Args:
        python_object (object): Any json serializable object

    Returns:
        pn.viewable.Viewable: [description]
    """
    return pn.Column(
        pnx.SubHeader(" Response"),
        pn.pane.JSON(python_object, depth=5, theme="light"),
    )


def code_card(
    code: str,
) -> pn.viewable.Viewable:
    """Wraps the code into a Card with "Code" as header and code as body

    Args:
        code (str): The code snippet to show

    Returns:
        pn.viewable.Viewable: A Card with "Code" as header and code as body.
    """
    return pn.Column(
        pnx.SubHeader(" Code"),
        Code(code),
    )


class Page(param.Parameterized):
    """A base class for a Page.

    Don't use this on a standalone basis"""

    symbols = param.String("ORSTED.CO")


class HomePage(Page):
    """Provides the view of the Home Page"""

    @param.depends("symbols")
    def _code(
        self,
    ):
        return code_card(
            f"""from yahooquery import Ticker

tickers = Ticker("{self.symbols}")
        """
        )

    @staticmethod
    def _help_text():
        return pnx_help(Ticker)

    @param.depends("symbols")
    def view(
        self,
    ) -> pn.viewable.Viewable:
        """The main view of the HomePage

        Returns:
            pn.viewable.Viewable: The main view of the HomePage
        """
        return pn.Column(
            self._code,
            pn.layout.HSpacer(height=25),
            self._help_text,
            sizing_mode="stretch_width",
        )


class BasePage(Page):
    """A view of the basic functionality of Ticker.

    The user can select an endpoint and the help text, code and result will be presented."""

    endpoint = param.ObjectSelector(
        default="asset_profile",
        objects=BASE_ENDPOINTS,
    )
    frequency = param.ObjectSelector(
        default="a",
        objects={
            "Annual": "a",
            "Quarterly": "q",
        },
    )

    @property
    def attr(
        self,
    ) -> object:
        """The Ticker.<endpoint> attribute

        Returns:
            object: The Ticker.<endpoint> attribute]
        """
        return getattr(
            Ticker,
            self.endpoint,
        )

    @property
    def attr_is_property(
        self,
    ) -> bool:
        """Whether or not self.attr is a property

        Returns:
            bool: Return True if self.attr is a property. Oherwise False is returned.
        """
        return isinstance(
            self.attr,
            property,
        )

    @param.depends("endpoint")
    def _help(
        self,
    ):
        if self.endpoint:
            return pnx_help(self.attr)
        return ""

    @param.depends(
        "symbols",
        "endpoint",
        "frequency",
    )
    def _code(
        self,
    ):
        if self.attr_is_property:
            code = f"Ticker('{self.symbols}').{self.endpoint}"
        else:
            code = f"Ticker('{self.symbols}').{self.endpoint}(frequency='{self.frequency}')"
        return code_card(code)

    @param.depends(
        "symbols",
        "endpoint",
        "frequency",
    )
    @PROGRESS.report(message="Requesting A Single Endpoint from Yahoo Finance")
    def _data(
        self,
    ):
        if self.attr_is_property:
            data = YahooQueryService.get_data(
                self.symbols,
                self.endpoint,
            )
        else:
            data = YahooQueryService.get_data(
                self.symbols,
                self.endpoint,
                self.frequency,
            )
        if isinstance(
            data,
            pd.DataFrame,
        ):
            # Enable formatters when https://github.com/holoviz/panel/issues/941 is solved
            # formatters = get_default_formatters(data)
            return pn.Column(
                pnx.SubHeader(" Response"),
                pn.widgets.DataFrame(
                    data,
                    fit_columns=True,
                    sizing_mode="stretch_width",
                    margin=25,
                ),
            )

        return pnx_json(data)

    # TTodo: remove line
    @param.depends("endpoint")
    def _selections(
        self,
    ):
        if self.attr_is_property:
            parameters = ["endpoint"]
        else:
            parameters = [
                "endpoint",
                "frequency",
            ]

        return pn.Column(
            pnx.SubHeader(" Selections"),
            pn.Param(
                self,
                parameters=parameters,
                show_name=False,
                default_layout=pn.Row,
                widgets={
                    "endpoint": {"width": 300},
                    "frequency": {"width": 100},
                },
            ),
        )

    @param.depends("symbols")
    def view(
        self,
    ) -> pn.viewable.Viewable:
        """The main view of the BasePage

        Returns:
            pn.viewable.Viewable: The main view of the BasePage
        """
        return pn.Column(
            self._selections,
            self._data,
            self._code,
            self._help,
            sizing_mode="stretch_width",
        )

    def __repr__(self):
        return "BasePage"


class BaseMultiplePage(Page):
    """A view for multiple Ticker requests

    The user can select all or multiple endpoints and the help text, code and result will be
    presented."""

    all_endpoints = param.Boolean(
        default=False,
        doc="If True all endpoints should be requested otherwise only multiple",
    )
    endpoints = param.ListSelector(
        default=["assetProfile"],
        objects=sorted(Ticker._ENDPOINTS),  # pylint: disable=protected-access
    )

    @param.depends("all_endpoints")
    def _endpoints_widget(
        self,
    ):
        if not self.all_endpoints:
            return pn.Param(
                self.param.endpoints,
                widgets={
                    "endpoints": {"height": 600},
                },
            )
        return None

    @param.depends(
        "all_endpoints",
        "endpoints",
    )
    def _help(
        self,
    ):
        if self.all_endpoints:
            return pnx_help(Ticker.all_endpoints)
        return pnx_help(Ticker.get_endpoints)

    @param.depends(
        "symbols",
        "all_endpoints",
        "endpoints",
    )
    def _code(
        self,
    ):
        if self.all_endpoints:
            code = f"Ticker('{self.symbols}').all_endpoint"
        else:
            code = f"Ticker('{self.symbols}').get_endpoints({self.endpoints})"

        return code_card(code=code)

    @param.depends(
        "symbols",
        "all_endpoints",
        "endpoints",
    )
    @PROGRESS.report(message="Requesting Multiple Endpoints from Yahoo Finance")
    def _data(
        self,
    ):
        if self.all_endpoints:
            data = YahooQueryService.get_data(
                self.symbols,
                "all_endpoints",
            )
        else:
            if not self.endpoints:
                return pnx.InfoAlert("Please select one or more Endpoints")

            data = YahooQueryService.get_data(
                self.symbols,
                "get_endpoints",
            )(self.endpoints)
        return pnx_json(data)

    def _selections(
        self,
    ):
        return pn.Column(
            pnx.SubHeader(" Selections"),
            self.param.all_endpoints,
            self._endpoints_widget,
            sizing_mode="fixed",
        )

    def view(
        self,
    ) -> pn.viewable.Viewable:
        """The main view of the BasePage

        Returns:
            pn.viewable.Viewable: The main view of the BasePage
        """
        return pn.Column(
            self._selections,
            self._data,
            self._code,
            self._help,
            sizing_mode="stretch_width",
        )


class OptionsPage(Page):
    """A view of the Options request

    The user can select all or multiple endpoints and the help text, code and result will be
    presented."""

    @staticmethod
    def _help():
        return pnx_help(Ticker.option_chain)

    @param.depends("symbols")
    def _code(
        self,
    ):
        code = f"Ticker('{self.symbols}').option_chain"
        return code_card(code=code)

    @param.depends("symbols")
    @PROGRESS.report(message="Requesting Options Chain from Yahoo Finance")
    def _data(
        self,
    ):
        data = YahooQueryService.get_data(
            self.symbols,
            "option_chain",
        )
        if isinstance(
            data,
            pd.DataFrame,
        ):
            # Enable formatters when https://github.com/holoviz/panel/issues/941 is solved
            # formatters = get_default_formatters(data)
            # We also show the first 5 columns as other wise the app gets too slow.
            return pnx.Card(
                body=pn.widgets.DataFrame(
                    data.head(),
                    fit_columns=True,
                    sizing_mode="stretch_width",
                    margin=25,
                ),
                header="Response",
            )
        return pnx_json(data)

    def view(
        self,
    ) -> pn.viewable.Viewable:
        """The main view of the OptionsPage

        Returns:
            pn.viewable.Viewable: The main view of the OptionsPage
        """
        return pn.Column(
            self._data,
            self._code,
            self._help,
            sizing_mode="stretch_width",
        )


class GridBoxWithTwoColumns(pn.GridBox):
    """A Custom Gridbox with 3 columns"""

    def __init__(
        self,
        *objects,
        **params,
    ):
        super().__init__(
            *objects,
            **params,
            ncols=2,
        )


class HistoryPage(Page):
    """Provides an illustration of the `Ticker.history` method"""

    period_type = param.ObjectSelector(
        default="Period",
        objects=[
            "Dates",
            "Period",
        ],
    )
    # pylint: disable=protected-access
    interval = param.ObjectSelector(
        default="1d",
        objects=Ticker._INTERVALS,
    )
    period = param.ObjectSelector(
        default="1y",
        objects=Ticker._PERIODS,
    )
    # pylint: enable=protected-access
    start = param.Date(
        default=PERIOD_START_DATE,
        bounds=DATE_BOUNDS,
    )
    end = param.Date(
        default=PERIOD_END_DATE,
        bounds=DATE_BOUNDS,
    )

    @staticmethod
    def _help():
        return pnx_help(Ticker.history)

    @param.depends("period_type")
    def _param_view(
        self,
    ):
        if self.period_type == "Period":
            return pn.Param(
                self,
                parameters=[
                    "period_type",
                    "interval",
                    "period",
                ],
                default_layout=GridBoxWithTwoColumns,
                width=400,
                show_name=False,
            )
        return pn.Param(
            self,
            parameters=[
                "period_type",
                "interval",
                "start",
                "end",
            ],
            default_layout=GridBoxWithTwoColumns,
            widgets={
                "start": pn.widgets.DatePicker,
                "end": pn.widgets.DatePicker,
            },
            width=600,
            show_name=False,
        )

    @param.depends(
        "symbols",
        "period_type",
        "interval",
        "period",
        "start",
        "end",
    )
    def _code(
        self,
    ):
        code = f"""Ticker("{self.symbols}").history({', '.join(self._args_string)})"""
        return code_card(code=code)

    @property
    def _history_args(
        self,
    ):
        history_args = {}
        if self.period_type == "Period":
            history_args["period"] = self.period
            history_args["start"] = None
            history_args["end"] = None
        else:
            history_args["period"] = None
            history_args["start"] = self.start
            history_args["end"] = self.end
        history_args["interval"] = self.interval
        return history_args

    @property
    def _args_string(
        self,
    ):
        return [
            str(k) + "='" + str(v) + "'" for k, v in self._history_args.items() if v is not None
        ]

    # I cannot make the chart responsive. There is some starting information here
    # See https://stackoverflow.com/questions/55169344/how-to-make-altair-plots-responsive
    @staticmethod
    def _history_plot(
        dataframe: pd.DataFrame,
    ):
        if "symbol" in dataframe.columns:
            chart = (
                alt.Chart(dataframe.reset_index())
                .mark_line()
                .encode(
                    alt.Y(
                        "close:Q",
                        scale=alt.Scale(zero=False),
                    ),
                    x="dates",
                    color="symbol",
                    tooltip=["dates", "close", "symbol"],
                )
            )
        else:
            chart = (
                alt.Chart(dataframe.reset_index())
                .mark_line()
                .encode(
                    alt.Y(
                        "close:Q",
                        scale=alt.Scale(zero=False),
                    ),
                    x="dates:T",
                    tooltip=["dates", "close"],
                )
            )

        chart = chart.properties(
            width="container",
            height=300,
        )
        return chart

    @param.depends("symbols")
    @PROGRESS.report(message="Requesting Price History from Yahoo Finance")
    def _data(
        self,
    ):
        tickers = YahooQueryService.to_ticker(self.symbols)
        data = tickers.history(**self._history_args)
        if isinstance(
            data,
            pd.DataFrame,
        ):
            return pn.Column(
                pnx.SubHeader(" Response"),
                pn.pane.Vega(
                    self._history_plot(data),
                    sizing_mode="stretch_width",
                    height=325,
                ),
                sizing_mode="stretch_width",
            )
        return pnx_json(data)

    def view(
        self,
    ) -> pn.viewable.Viewable:
        """The main view of the OptionsPage

        Returns:
            pn.viewable.Viewable: The main view of the OptionsPage
        """
        return pn.Column(
            self._param_view,
            self._data,
            self._code,
            self._help,
            sizing_mode="stretch_width",
        )


class YahooQueryView(pn.Column):
    """A View of the Yahoo Query App"""

    def __init__(
        self,
        symbols: pn.viewable.Viewable,
        pages: List[
            Tuple[
                str,
                pn.viewable.Viewable,
            ]
        ],
        sizing_mode="stretch_width",
        **kwargs,
    ):
        super().__init__(
            self._symbols_widget(symbols),
            pn.layout.HSpacer(height=25),
            PROGRESS.view,
            self.pages_view(pages),
            sizing_mode=sizing_mode,
            **kwargs,
        )

    @staticmethod
    def _symbol_lookup_link() -> pn.viewable.Viewable:
        return pn.pane.Markdown(
            "<a href='https://finance.yahoo.com/lookup' target='_blank'>"
            "<i class='fas fa-search'></i></a>"
        )

    def _symbols_widget(
        self,
        symbols: pn.viewable.Viewable,
        sizing_mode: str = "stretch_width",
    ) -> pn.viewable.Viewable:
        return pn.Row(
            symbols,
            self._symbol_lookup_link(),
            sizing_mode=sizing_mode,
        )

    @staticmethod
    def pages_view(
        pages: List[
            Tuple[
                str,
                pn.viewable.Viewable,
            ]
        ],
        sizing_mode: str = "stretch_width",
    ) -> pn.Tabs:
        """A Tabbed view of the pages

        Args:
            pages (List[Tuple[str, pn.viewable.Viewable]]): A list of Pages to display
            sizing_mode (str, optional): The sizing mode of the pages_view. Defaults to \
                "stretch_width".

        Returns:
            pn.Tabs: [description]
        """
        return pn.Tabs(
            *pages,
            sizing_mode=sizing_mode,
        )


class YahooQueryApp(Page):
    """The main app makes the yahooquery package interactive"""

    def __init__(
        self,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.pages = {
            "Introduction": HomePage(),
            "Single Request": BasePage(),
            "Multiple Requests": BaseMultiplePage(),
            "Options Requests": OptionsPage(),
            "Historical Requests": HistoryPage(),
        }

    @param.depends(
        "symbols",
        watch=True,
    )
    def _set_pages(
        self,
    ):
        for page in self.pages.values():
            page.symbols = self.symbols

    def view(
        self,
    ) -> pn.viewable.Viewable:
        """The main view of the app

        Returns:
            pn.viewable.Viewable: Serve this via .servable()
        """
        pn.config.sizing_mode = "stretch_width"
        pages_list = [
            (
                key,
                value.view(),
            )
            for key, value in self.pages.items()
        ]

        main = [
            APPLICATION.intro_section(),
            YahooQueryView(
                self.param.symbols,
                pages_list,
                sizing_mode="stretch_width",
            ),
        ]
        return pn.template.FastListTemplate(title="Yahoo Query App", main=main)


@site.add(APPLICATION)
def view():
    """A Reactive View of the YahooQueryApp

    This function is required for use in the Gallery as awesome-panel.org
    """
    return YahooQueryApp().view()


if __name__.startswith("bokeh"):
    pn.extension()
    pnx.fontawesome.extend()
    pnx.bootstrap.extend()
    pn.config.sizing_mode = "stretch_width"

    view().servable()
