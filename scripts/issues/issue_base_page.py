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

class BasePage(param.Parameterized):
    """A view of the basic functionality of Ticker.

    The user can select an endpoint and the help text, code and result will be presented."""
    frequency = param.ObjectSelector(
        default="q", objects={"Annual": "a", "Quarterly": "q"}
    )

    @param.depends("frequency")
    def _data(self):
        data = YahooQueryService.get_data("ORSTED.CO", "balance_sheet", self.frequency)
        if isinstance(data, pd.DataFrame):
            formatters = get_default_formatters(data)
            print(formatters)
            return pn.widgets.DataFrame(
                data, fit_columns=True, formatters=formatters, sizing_mode="stretch_width"
            )
        else:
            raise NotImplementedError()

    def view(self):
        return pn.Column(
            self.param,
            self._data,
        )

BasePage().view().servable()