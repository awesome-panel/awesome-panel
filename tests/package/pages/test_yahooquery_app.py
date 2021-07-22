"""In this module we test the YahooQuery App"""
# pylint: disable=redefined-outer-name,protected-access
import pytest

from application.pages.yahooquery_app.yahooquery_app import BasePage  # type: ignore


@pytest.mark.xfail
def test_base__page__data_balance_sheet_quarterly():
    """We have see an error thrown here"""
    base_page = BasePage()
    base_page.symbols = "ORSTED.CO"
    base_page.endpoint = "balance_sheet"
    base_page.frequency = "q"

    # assert isinstance(base_page.attr, Ticker.balance_sheet)
    assert not base_page.attr_is_property

    base_page._help()
    base_page._code()
    base_page._data()
    base_page.view()
